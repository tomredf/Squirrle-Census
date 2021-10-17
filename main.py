from typing import Any

import numpy
import pandas
from pandas import Series, DataFrame
from pandas.io.parsers import TextFileReader

data = pandas.read_csv("Squirrel_Data.csv")

df = data.groupby(by=['Primary Fur Color']).size().reset_index(name='counts')
print(df)
df.to_csv("squirrel_count.csv")