from pathlib import Path
import chardet
import os

import numpy as np

from timeit_util import time_decorator


@time_decorator
def detect_file_encoding():
    line = '{:<35}{:<10}{}'.format
    print(line('File name', 'Encoding', 'Confidence'))

    for filepath in Path('sources').glob('*'):
        detect = chardet.detect(filepath.read_bytes())  # tells you encoding of the file data and gives the
        # confidence too, we need to specify this encoding while reading into pandas
        # pd.read_csv('data/businesses.csv', encoding='ISO-8859-1')
        print(line(str(filepath), detect['encoding'], detect['confidence']))


@time_decorator
def check_file_size(dir):
    KiB = 1024
    MiB= 1024**2
    line = '{:<35}{:<25}{}'.format
    print(line('File name', 'File size in KiB', 'File size in MiB'))

    for filepath in Path(dir).glob('*'):
        getsize = os.path.getsize(filepath) # number of chars
        print(line(str(filepath), np.round(getsize/KiB), np.round(getsize/MiB)))


if __name__ == "__main__":
    detect_file_encoding()
    check_file_size('sources')
