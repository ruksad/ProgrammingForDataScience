import pandas as pd

def group_by_and_sum(baby):
    year__sum = baby.groupby("Year")['Count'].sum()
    print(year__sum)
def keep_rows_with_value(baby):
    year_ = baby.loc[baby['Year'] == 1881, :]
    year_['Count'].sum()
    print(year_['Count'].sum())

if __name__=="__main__":
    baby= pd.read_csv('sources/babynames.csv')
    group_by_and_sum(baby)
    keep_rows_with_value(baby)