import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def buildResult():
    VMTable = pd.read_csv("Dataset/vmtable.csv.gz", header=None)[[3, 4, 8]]
    VMTable[3] = pd.to_numeric(VMTable[3])
    VMTable[4] = pd.to_numeric(VMTable[4])
    VMTable[4] = VMTable[4] - VMTable[3]

    groups = VMTable.groupby([8])

    results = []
    for key, group in groups:
        name = key
        count = group.shape[0]

        gr = {'key': hash(name), 'name': name, 'avg': group[4].mean() / 1000}
        results.append(gr)
    results.sort(key=lambda x: x['key'])
    print(results)
    return results


def plotResult(result):
    labels = []
    VMs_count = []
    VMs_std = []

    for i in range(len(result)):
        labels.append(result[i]['name'])
        VMs_count.append(result[i]['avg'])
        VMs_std.append(1)

    plt.rcParams['font.size'] = '6'

    fig, ax = plt.subplots()
    ax.bar(labels, VMs_count, 0.35, yerr=VMs_std)
    ax.set_ylabel("VM Lifetime in seconds")

    plt.savefig('images/category_lifetime.png')


if __name__ == '__main__':
    plotResult(buildResult())
