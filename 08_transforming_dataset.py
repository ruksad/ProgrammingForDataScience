import pandas as pd

'''pd.Series object contains an .apply() method that takes a method and applies to all objects in the series if we do 
dataset['Initials'] = names.apply(first_letter) then it will modify the original dataset'''


def test_method(dataset):
    name_ = dataset['Name']
    name_.apply(len)
    return name_


def first_letter_of_str(string):
    return string[0]


'''Assign first letter to a new column from Name column, NOTE: assign creates a new dataframe instead of altering the 
original'''


def transform_dataset(dataset):
    assign = dataset.assign(Initials=test_method(dataset).apply(first_letter_of_str))
    print(assign)


if __name__ == "__main__":
    csv = pd.read_csv('sources/babynames.csv')
    transform_dataset(csv)
    #test_method(csv)
