import os
from pathlib import Path

import pandas as pd
from timeit_util import to_date_time_from_series

bus: pd.DataFrame = None
insp: pd.DataFrame = None
viol: pd.DataFrame = None


def check_granularity_business():
    print("Business shape:", bus.shape)
    print("business_id is unique key") if (len(bus['business_id']) == len(bus['business_id'].unique())) else print(
        "business_id is not unique")


def sub_set_of_year(df: pd.DataFrame, year: str = '2016'):
    return df.query(f'year=={year}')


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


def read_files_for_wrangling(path: Path):
    join = Path(os.path.join(path, 'businesses.csv'))
    global bus
    global insp
    global viol
    bus = pd.read_csv(join)

    path_join = Path(os.path.join(path, 'inspections.csv'))
    insp = pd.read_csv(path_join)

    os_path_join = Path(os.path.join(path, 'violations.csv'))
    viol = pd.read_csv(os_path_join)


def zero_vios_for_perfect_score(df):
    copy_df = df.copy()
    copy_df.loc[copy_df['score'] == 100, 'noOfViol'] = 0
    return copy_df


def find_all_rows_score_not100_and_noOfViol_are_null(df):
    return df[(df['score'] != 100) & (df['noOfViol'].isnull())]


def group_by_feature_in_violation(df):
    return df['description'].value_counts().head(15).to_frame()


def make_vio_desc_cate(df: pd.DataFrame):
    def has(term):
        return df['description'].str.contains(term)

    return df[['business_id', 'timestamp']].assign(
        high_risk=has(r"high risk"),
        clean=has(r"clean|sanit"),
        food_surface=(has(f"surface") & has(r"\Wfood")),
        vermin=has(r"vermin"),
        storage=has(r"thaw|cool|therm|storage"),
        permit=has(r"certif|permit"),
        non_food_surface=has(r"wall|ceiling|floor|surface"),
        human=has(r"hand|glove|hair|nail")
    )


if __name__ == "__main__":
    read_files_for_wrangling(Path('sources'))

    inspections = check_granularity_inspections().pipe(sub_set_of_year)
    violations = check_granularity_violations().pipe(sub_set_of_year)
    noOfViolationsForBusiness = violations.groupby(['business_id', 'timestamp']).size().reset_index().rename(
        columns={0: 'noOfViol'})
    insp_merge_viol_2016 = inspections.merge(noOfViolationsForBusiness, left_on=['business_id', 'timestamp'],
                                             right_on=['business_id', 'timestamp'], how='left')
    print("aggregating violations with inspections\n", insp_merge_viol_2016)

    print("no fo violation is null for year 2016:", insp_merge_viol_2016['noOfViol'].isnull().sum())
    '''set check score==100 then no of violations is NaN i.e there is no violation for the business score= 100 so sum 
    is NaN, lets set noOfViol= 0'''
    zeroViosScore = insp_merge_viol_2016.pipe(zero_vios_for_perfect_score)
    print(zeroViosScore.pipe(find_all_rows_score_not100_and_noOfViol_are_null))
    #print(violations.pipe(group_by_feature_in_violation))
    '''make categories out of violation given in the description'''
    vio_ctg = violations.pipe(make_vio_desc_cate)
    print(vio_ctg.head(15))
    voi_ctg_cnt = vio_ctg.groupby(['business_id', 'timestamp']).sum().reset_index()
    print(voi_ctg_cnt.head(15))

    '''Join inspection and description and set value for features=0 if no match for score=100 in right table'''

    insp_vio_left = inspections[['business_id', 'timestamp', 'score']].merge(voi_ctg_cnt,
                                                                             on=['business_id', 'timestamp'],
                                                                             how='left')
    insp_vio_left.loc[insp_vio_left['score'] == 100, ['high_risk', 'clean', 'food_surface', 'vermin',
                                                      'storage', 'permit', 'non_food_surface', 'human']] = 0
    print(insp_vio_left)

    features = insp_vio_left.melt(id_vars=['business_id', 'timestamp', 'score'],
                                  var_name='violation', value_name='noOfViol')
    features['vio'] = features['noOfViol'] > 0
    any_vio = {False:"No", True:"Yes"}
    features['vio'] = features['vio'].map(any_vio)

    print("\n")
    print(features)
