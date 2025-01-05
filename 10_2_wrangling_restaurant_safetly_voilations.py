import os
from pathlib import Path

import chardet
import pandas
import pandas as pd

from timeit_util import time_decorator, to_date_time_from_series

bus: pd.DataFrame = None
insp: pd.DataFrame = None
viol: pd.DataFrame = None

businesspath = None


@time_decorator
def read_files_for_wrangling(path: Path):
    join = Path(os.path.join(path, 'businesses.csv'))
    global bus
    global insp
    global viol
    bus = pd.read_csv(join)

    line = '{:<35},{}'.format
    detect = chardet.detect(join.read_bytes())
    print(line(f' file size in KiB:{os.path.getsize(join) / 1024}', detect['encoding']))

    path_join = Path(os.path.join(path, 'inspections.csv'))
    insp = pd.read_csv(path_join)

    line = '{:<35},{}'.format
    detect = chardet.detect(path_join.read_bytes())
    print(line(f' file size in KiB:{os.path.getsize(path_join) / 1024}', detect['encoding']))

    os_path_join = Path(os.path.join(path, 'violations.csv'))
    viol = pd.read_csv(os_path_join)

    line = '{:<35},{}'.format
    detect = chardet.detect(os_path_join.read_bytes())
    print(line(f' file size in KiB:{os.path.getsize(os_path_join) / 1024}', detect['encoding']))


def check_granularity_business():
    print("Business shape:", bus.shape)
    print("business_id is unique key") if (len(bus['business_id']) == len(bus['business_id'].unique())) else print(
        "business_id is not unique")


def check_granularity_inspections():
    print("inspections shape:", insp.shape)
    modified_insp = insp.pipe(to_date_time_from_series)
    print(modified_insp.head(), "\n class", modified_insp.__class__.__name__)
    modified_insp2 = modified_insp['dayofweek'].value_counts().reset_index()
    modified_insp3 = modified_insp.groupby('dayofweek')['dayofweek'].size().reset_index(name='count')
    print(modified_insp2, "class name=", modified_insp2.__class__.__name__)
    print(modified_insp3, "class name", modified_insp3.__class__.__name__)

    df_find_max_day_in2016 = modified_insp.pipe(sub_set_of_year)['dayofweek'].value_counts().reset_index()
    ''' below line find the day of the week which has maximum inspections during the year 2016'''
    print(df_find_max_day_in2016.loc[df_find_max_day_in2016['count'].idxmax()]['dayofweek'])
    return insp.pipe(to_date_time_from_series)


def check_granularity_violations():
    print("Violations shape:", viol.shape)
    ''' below line give no of violation for particular business in year=2016 only'''
    index = viol.pipe(to_date_time_from_series).pipe(sub_set_of_year).groupby([
        'business_id', 'timestamp']).size().reset_index().rename(columns={0: 'numOfViol'}).head(3)
    print(index)
    return viol.pipe(to_date_time_from_series)


def sub_set_of_year(df: pd.DataFrame, year: str = '2016'):
    return df.query(f'year=={year}')


def left_join_vios(ins: pandas.DataFrame, vios: pandas.DataFrame):
    merge = ins.merge(vios, left_on=['business_id', 'timestamp'], right_on=['business_id', 'timestamp'], how='left')
    return merge


if __name__ == '__main__':
    read_files_for_wrangling(Path('sources'))
    check_granularity_business()
    inspections = check_granularity_inspections().pipe(sub_set_of_year)
    violations = check_granularity_violations().pipe(sub_set_of_year)
    noOfViolationsForBusiness = violations.groupby(['business_id', 'timestamp']).size().reset_index().rename(
        columns={0: 'noOfViol'})
    insp_merge_viol=inspections.merge(noOfViolationsForBusiness, left_on=['business_id', 'timestamp'],
                      right_on=['business_id', 'timestamp'], how='left')
    print("aggregating violations with inspections\n", insp_merge_viol)

    print("no fo violation is null for year 2016:",insp_merge_viol['noOfViol'].isnull().sum())
