import pandas as pd


def group_by_and_sum(dataset):
    year__sum = dataset.groupby("Year")['Count'].sum()  # group by sum
    dataset.groupby('Year')
    print(year__sum)


def group_by_and_max(dataset):
    count__max = dataset.groupby('Year')['Count'].max()  # find max count of a name in a particular year
    print(count__max)
    print(count__max.__class__)


def group_by_and_min(dataset):
    count__min = dataset.groupby('Year')['Count'].min()
    print(count__min)


def count_the_number_of_times_unique_in_col(dataset):
    groupby = dataset.groupby('Name')['Name'].size()  # find the number of times name has appeared in dataset
    groupby_or = dataset['Name'].value_counts()  # vaule_counts will sort the results too unlike group by and size
    print(groupby_or)


'''
subset in a dataset
'''


def keep_rows_with_value(dataset):
    year_ = dataset.loc[baby['Year'] == 1881, :]
    year_or = dataset[dataset['Year'] == 1881]
    year_['Count'].sum()
    print(year_['Count'].sum())


'''
multiple group by, count the number of males and females born in a year
'''


def grouping_by_multiple_columns(dataset):
    count__sum = dataset.groupby(['Year', 'Sex'])['Count'].sum()
    print(count__sum)
    print(count__sum.to_frame())
    print(" reset index")  # count__sum.to_frame() is multilevel indices it can be trick to iterate so try
    # reset_index() and observe output
    print(count__sum.to_frame().reset_index())


def test_method(dataset):
    var = dataset[dataset['Year'] == 1989]
    print(var[var['Sex'] == 'M'])


'''
1. find the difference between find the difference between the max name count and min name count, using custom aggregate
2. Find the size of unique names in a year 
'''


def custom_aggregate(dataset):
    range_ = (dataset.groupby('Year')['Count'].agg(data_range))
    print("Range of max names appear and min name appeared in an year:")
    print(range_)

    unique_ = (dataset.groupby('Year')['Name'].agg(count_unique))
    print("Unique names in a year:")
    print(unique_)


'''
input to this object is pd.series object which runs for each group'''


def data_range(counts):
    return counts.max() - counts.min()


'''
Input to this method is pd.series object which run for each group'''


def count_unique(counts):
    return len(counts.unique())


'''
pivote the sex index to column using pd.pivot_table()
'''


def pivoting_data_frame(dataset):
    group_by_year_and_sex = (dataset.groupby(['Year', 'Sex'])['Count'].sum())
    print("Year and sex group by will return pd.series object: ")
    print(group_by_year_and_sex.to_frame().reset_index())
    table = pd.pivot_table(dataset,
                           index='Year',  # column to turn into new index
                           columns='Sex',  # Column to turn into new columns
                           values='Count',  # Column to aggregate the values
                           aggfunc="sum")  # aggregate function
    print("Pivoted table: ")
    print(table)


if __name__ == "__main__":
    baby = pd.read_csv('sources/babynames.csv')
    #group_by_and_sum(baby)
    #keep_rows_with_value(baby)
    #count_the_number_of_times_unique_in_col(baby)
    #test_method(baby)
    #grouping_by_multiple_columns(baby)
    #group_by_and_max(baby)
    #group_by_and_min(baby)
    #custom_aggregate(baby)
    pivoting_data_frame(baby)
