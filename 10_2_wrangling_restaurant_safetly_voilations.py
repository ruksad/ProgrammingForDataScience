from pathlib import Path
import pandas as pd
from timeit_util import time_decorator, to_date_time_from_series
import os
import chardet
from file_util import head

bus = None
insp = None
viol = None


@time_decorator
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

    check_granularity_business(join)
    check_granularity_inspections(path_join)
    check_granularity_violations(os_path_join)


def check_granularity_business(path: Path):
    line = '{:<35},{}'.format
    detect = chardet.detect(path.read_bytes())
    print(line(f' file size in KiB:{os.path.getsize(path) / 1024}', f'Encoding: {detect['encoding']}'))
    print("Business shape:", bus.shape)
    head(path)
    print("business_id is unique key") if (len(bus['business_id']) == len(bus['business_id'].unique())) else print(
        "business_id is not unique")


def check_granularity_inspections(path: Path):
    line = '{:<35},{}'.format
    detect = chardet.detect(path.read_bytes())
    print(line(f' file size in KiB:{os.path.getsize(path) / 1024}', detect['encoding']))
    print("inspections shape:", insp.shape)
    modified_insp = insp.pipe(to_date_time_from_series)
    print(modified_insp.head(), "\n class", modified_insp.__class__.__name__)
    modified_insp2 = modified_insp['dayofweek'].value_counts().reset_index()
    modified_insp3 = modified_insp.groupby('dayofweek')['dayofweek'].size().reset_index(name='count')
    print(modified_insp2, "class name=", modified_insp2.__class__.__name__)
    print(modified_insp3, "class name", modified_insp3.__class__.__name__)


def check_granularity_violations(path: Path):
    line = '{:<35},{}'.format
    detect = chardet.detect(path.read_bytes())
    print(line(f' file size in KiB:{os.path.getsize(path) / 1024}', detect['encoding']))
    print("Violations shape:", viol.shape)


if __name__ == '__main__':
    read_files_for_wrangling(Path('sources'))
