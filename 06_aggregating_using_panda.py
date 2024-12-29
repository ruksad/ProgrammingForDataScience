import pandas as pd


def group_by_and_sum(dataset):
    year__sum = dataset.groupby("Year")['Count'].sum()  # group by sum
    dataset.groupby('Year')
    print(year__sum)

def group_by_and_max(dataset):
    count__max = dataset.groupby('Year')['Count'].max()  # find max count of a name in a particular year
    print(count__max)
    print(count__max.__class__)


def count_the_number_of_times_unique_in_col(dataset):
    groupby = dataset.groupby('Name')['Name'].size()     # find the number of times name has appeared in dataset
    groupby_or= dataset['Name'].value_counts()   # vaule_counts will sort the results too unlike group by and size
    print(groupby_or)

'''
subset in a dataset
'''
def keep_rows_with_value(dataset):
    year_ = dataset.loc[baby['Year'] == 1881, :]
    year_or= dataset[dataset['Year']==1881]
    year_['Count'].sum()
    print(year_['Count'].sum())

'''
multiple group by, count the number of males and females born in a year
'''
def grouping_by_multiple_columns(dataset):
    count__sum = dataset.groupby(['Year', 'Sex'])['Count'].sum()
    print(count__sum)
    print(count__sum.to_frame())
    print(" reset index") # count__sum.to_frame() is multilevel indices it can be trick to iterate so try
    # reset_index() and observe output
    print(count__sum.to_frame().reset_index())

def test_method(dataset):
    var = dataset[dataset['Year'] == 1882]
    print(var[var['Sex']=='M'])

if __name__ == "__main__":
    baby = pd.read_csv('sources/babynames.csv')
    #group_by_and_sum(baby)
    #keep_rows_with_value(baby)
    #count_the_number_of_times_unique_in_col(baby)
    #test_method(baby)
    #grouping_by_multiple_columns(baby)
    group_by_and_max(baby)
