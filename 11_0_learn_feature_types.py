import numpy as np
import pandas as pd
from pathlib import Path
import os
import plotly.express as px

from scipy.stats import gaussian_kde


def read_dataS_source(path: Path):
    return pd.read_csv(os.path.join(path, '11_akc.csv'))


def general_stats():
    print(dogs['breed'].value_counts())  # output length is 172 i.e breed column is unique
    print(dogs['group'].value_counts())
    counts_ = dogs['longevity'].value_counts()
    print("=====\n", counts_, "=============\n", counts_[counts_ >= 5].index)

    only_longevity_GT_5 = dogs[dogs['longevity'].isin(counts_[counts_ >= 5].index)]

    print("+++++++++++\n", only_longevity_GT_5.loc[:, ["breed", "group", "longevity", "purchase_price"]])
    print("------------- info \n")
    only_longevity_GT_5.info()
    print("describe: \n", dogs.describe())
    print("shape: \n", only_longevity_GT_5.shape)


def relabel_categories(dogs=None):
    ''' we will relabel children to kids into low, medium and high '''
    kids = {3: 'Low', 2: 'Medium', 1: 'High'}
    dogs = dogs.assign(kids=dogs['children'].replace(kids))
    print(dogs.loc[:, ["breed", "group", "longevity", "purchase_price", "score", "kids"]])
    #dogs = dogs.drop(["purchase_price", "grooming", "group", "size", "weight", "height", "repetition"],axis=1)
    #print(dogs.loc[167:168])


if __name__ == "__main__":
    dogs = read_dataS_source(Path('sources'))
    print(f"shape {dogs.shape}")

    '''
    dataframe.info() will print below meta 
    <class 'pandas.core.frame.DataFrame'>
RangeIndex: 172 entries, 0 to 171
Data columns (total 12 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   breed           172 non-null    object 
 1   group           172 non-null    object 
 2   score           87 non-null     float64
 3   longevity       135 non-null    float64
 4   ailments        148 non-null    float64
 5   purchase_price  146 non-null    float64
 6   grooming        112 non-null    float64
 7   children        112 non-null    float64
 8   size            172 non-null    object 
 9   weight          86 non-null     float64
 10  height          159 non-null    float64
 11  repetition      132 non-null    object 
dtypes: float64(8), object(4)
memory usage: 16.3+ KB'''
    dogs.info()
    #general_stats()
    #relabel_categories(dogs)

    fig = px.histogram(dogs, x="longevity", marginal="rug", nbins=20,
                       histnorm='percent', width=450, height=350,
                       labels={'longevity': 'Typical lifespan (yr)'})

    # Show the chart
    fig.show()
