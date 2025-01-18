from pathlib import Path
import os
import re
from timeit_util import time_decorator
import pandas as pd


def load_data_frame(path: Path):
    return Path(os.path.join(path, 'stateoftheunion1790-2022.txt')).read_text()


def extract_parts(speech):
    split = speech.strip().split("\n")[1:]  # removing the name of the speech
    [name, date, *lines] = split  # take first two lines as name, date and remaining ones are speech lines
    body = '\n'.join(lines).strip()
    return [name, date, body]


"""
r'\[[^\]]+\]'   this will match [laughter] [claps] \[ \] matches the bracket in speech [^\]]+ will match one or more chars which are not 
"""


def clean_text(df):
    brackets_re = re.compile(r'\[[^\]]+\]')
    apart_from_words= re.compile(r'[^a-z\s]')

    cleaned= df['text'].str.lower().str.replace(brackets_re,'',regex=True).str(apart_from_words,' ',regex=True)
    return df.assign(text=cleaned)


def read_speeches_into_df():
    return pd.DataFrame([extract_parts(i) for i in total_records[1:]],
                        columns=["name", "date", "text"])


if __name__ == "__main__":
    line = "{}{:<35}".format
    text = load_data_frame(Path('sources'))
    allSpeeches = re.findall(r'\*\*\*', text)
    print(line('Total speeches: ', len(allSpeeches)))
    total_records = text.split('***')
    df = read_speeches_into_df()
    df_cleaned = clean_text(df)
