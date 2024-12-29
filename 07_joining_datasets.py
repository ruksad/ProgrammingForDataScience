import pandas as pd

'''Inner join will drop non matching columns from left and right '''


def inner_join(dataset1, dataset2):
    merge = dataset1.merge(dataset2, left_on='Name', right_on='Name')
    print(merge)


def left_join(dataset1, dataset2):
    merge = dataset1.merge(dataset2, left_on='Name', right_on='Name', how='left')
    print(merge)


'''return all the matching rows fro the left table and non matching rows form right table'''


def right_join(dataset1, dataset2):
    merge = dataset1.merge(dataset2, left_on='Name', right_on='Name', how='right')
    print(merge)


''' join keeps rows from both the tables even when there are no matching rows'''


def out_join(dataset1, dataset2):
    merge = dataset1.merge(dataset2, left_on='Name', right_on='Name', how='outer')
    print(merge)


if __name__ == "__main__":
    baby_names = pd.read_csv('sources/babynames.csv')
    baby_categories = pd.read_csv('sources/babynames_category.csv')
    #inner_join(baby_names, baby_categories)
    #left_join(baby_names, baby_categories)
    right_join(baby_names, baby_categories)
