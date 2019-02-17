#!/usr/bin/env python
# coding: utf-8

import pandas as pd

df = pd.read_csv('PSID.csv', parse_dates=True, index_col=0, sep=',')
df
