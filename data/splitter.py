import pandas as pd
import numpy as np


def splitter(sourcefile, targetfile):
    df = pd.read_csv(sourcefile, header=None)
    b = df[np.mod(np.arange(df.index.size), 4) == 0]
    b.to_csv(targetfile)


if __name__ == '__main__':
    #splitter('suicide_rate_1985_2016.csv', 'suicide_rate_1985_2016_one_fourth.csv')
    splitter('adult.csv', 'adult_one_fourth.csv')
