from numpy import random as rd
import matplotlib.pyplot as plt
import pandas as pd


def make_data(noise,size = 10000,dims = 20):

    df = {'Y':[],'X':[]}

    for i in range(dims):
        df['V'+str(i)] = []

    for i in range(size):
        ui = rd.normal(scale = noise)
        xi = rd.uniform(-1,1)
        v = []
        for j in range(dims):
            v.append(rd.normal())

        if xi<0:
            yi = xi**3-xi-1+sum(v)+ui
        else:
            yi = xi**3-xi+1+sum(v)+ui

        df['Y'].append(yi)
        df['X'].append(xi)
        for j in range(dims):
            df['V'+str(j)].append(v[j])

    return pd.DataFrame(df)


df = make_data(0.05,dims = 0)

df.to_csv('input.csv')

plt.scatter(list(df['X']),list(df['Y']))

plt.show()
