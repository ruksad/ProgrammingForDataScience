import pandas as pd
from pathlib import Path
import os
import plotly.express as px


def read_csv_from(path: Path):
    return pd.read_csv(os.path.join(path, 'sfhousing.csv'), low_memory=False)


def read_data_dogs_source(path: Path):
    return pd.read_csv(os.path.join(path, '11_akc.csv'))


def create_plot():
    fig = px.scatter(dogs, x="height", y="weight", labels=dict(height="Height (cm)", weight="Weight (Kg)"), width=350,
                     height=250, )
    print("scatter objet type: ", fig.__class__)
    fig.show()


def create_plot_with_facet_on_size():
    fig = px.scatter(dogs, x="height", y="weight", facet_col="size",
                     labels=dict(height="Height in CM", weight="Weight in Kgs"),
                     width=450,
                     height=250)
    fig.update_layout(margin=dict(t=40))
    fig.show()

def plot_weight_longevity():
    fig= px.scatter(dogs, x="weight", y= "longevity", title=" weight to longevity graph", width= 450, height=350)
    fig.update_yaxes(range=[5,18], title=" Typical life span")
    fig.update_xaxes(title=" Average weight")
    fig.update_layout(margin= dict(t=30))
    fig.show()


if __name__ == "__main__":
    # sfh_df = read_csv_from(Path('sources'))
    #sfh_df.info()
    dogs = read_data_dogs_source(Path('sources'))
    #create_plot_with_facet_on_size()
    plot_weight_longevity()
