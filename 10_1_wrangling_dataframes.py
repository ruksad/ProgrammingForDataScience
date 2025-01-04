from pathlib import Path
import os
import pandas as pd
import chardet
from timeit_util import time_decorator

@time_decorator
def examine_file(param):
    line = "{:<20}{}".format
    co2_file_path = Path(param)
    print(co2_file_path.stat())
    features_ = [os.path.getsize(co2_file_path), chardet.detect(co2_file_path.read_bytes())['encoding']]
    print(line('features:', features_))

    lines = co2_file_path.read_text().split('\n')
    print(line('No of lines:', len(lines)))
    #print(lines[:6])
    #print(lines[69:75])  # start exclusive and end inclusive
    dataframe = read_from_text_into_dataframe(filename=param)
    print(dataframe.head(3))
    print(dataframe.shape)  # gives rows * column
    describe_ = dataframe.describe()[3:]
    print(describe_)
    #print(dataframe.describe())

    print(dataframe.groupby('Mo')['Mo'].size())
    print(dataframe['Mo'].value_counts().reindex(
        range(1, 12)).tolist())  # alternative dataframe.groupby(['Mo'])['Mo'].size()

    line2 = '{:}\n{}\n{}'.format
    avg_ = dataframe[dataframe['Avg'] < 0]
    print(line2('Co2 average dataframe below 0', avg_,avg_.__class__.__name__))


def read_from_text_into_dataframe(filename):
    csv = pd.read_csv(filename, header=None, skiprows=72, sep='\\s+',
                      names=['Yr', 'Mo', 'DecDate', 'Avg', 'Int', 'Trend', 'days'])
    return csv


if __name__ == "__main__":
    examine_file('sources/co2_mm_mlo.txt')
