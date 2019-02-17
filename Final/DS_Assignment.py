#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import scipy.stats as st
import scipy.special as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import math
# needs pillow for jpg save

df = pd.read_csv('PSID.csv', parse_dates=True, index_col=0, sep=',')
df

sampleEarningsMean = df["earnings"].mean()
sampleEarningsStdDev = df["earnings"].std()
sampleEarningsMean, sampleEarningsStdDev

sampleSize = 2000
subsample = df.sample(sampleSize)
subsample

subsampleEarningsmean = subsample["earnings"].mean()
subsampleEarningsStdDev = subsample["earnings"].std()
subsampleEarningsmean, subsampleEarningsStdDev

n = sampleSize
q = sampleEarningsMean  # null-hypothesis

xbar = subsampleEarningsmean # sample mean
std_dev = sampleEarningsStdDev # population standard deviation
z = (xbar - q) * np.sqrt(n )/ std_dev

pval = st.norm.sf(abs(z))*2
z, pval

mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
pdf = st.norm.pdf(x, mu, sigma)
plt.plot(x, pdf)

# two tail test
plt.fill_between(x,st.norm.pdf(x, mu, sigma),where = x <=-1.96, color='red')
plt.fill_between(x,st.norm.pdf(x, mu, sigma),where = x >=1.96, color='red')
#plt.show()
plt.savefig('Vis_1.jpg')

plt.plot(x, pdf)
plt.fill_between(x,st.norm.pdf(x, mu, sigma),where = x <=-1.96, color='red')
plt.fill_between(x,st.norm.pdf(x, mu, sigma),where = x >=z, color='lightgrey')
#plt.show()
plt.savefig('Vis_2.jpg')


