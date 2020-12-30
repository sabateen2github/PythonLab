import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random


def buildResult():
    VMTable = pd.read_csv("Dataset/vmtable.csv.gz", header=None)[[3, 4, 9, 10]]
    VMTable[9] = pd.to_numeric(np.where(VMTable[9] == '>24', 30, VMTable[9]))
    VMTable[10] = pd.to_numeric(np.where(VMTable[10] == '>64', 70, VMTable[10]))
    VMTable[3] = pd.to_numeric(VMTable[3])
    VMTable[4] = pd.to_numeric(VMTable[4])
    VMTable[4] = VMTable[4] - VMTable[3]

    groups = VMTable.groupby([9, 10])

    results = []
    for key, group in groups:
        name = "    {cpu} vCPUs / {mem} GB   ".format(cpu=key[0], mem=key[1])
        count = group.shape[0]

        try:
            c = int(key[0])
        except ValueError:
            c = 30
        try:
            m = int(key[1])
        except ValueError:
            m = 70

        gr = {'key': c * 10 + m, 'name': name, 'avg': group[4].mean() / 1000}
        results.append(gr)
    results.sort(key=lambda x: x['key'])
    print(results)
    return results


def plotResult(result):
    labels = []
    VMs_count = []
    VMs_std = []
    colors = []

    for i in range(len(result)):
        labels.append(result[i]['name'])
        VMs_count.append(result[i]['avg'])
        VMs_std.append(1)
        colors.append((random.random(), random.random(), random.random(), 1.0))

    plt.rcParams['font.size'] = '6'

    fig, ax = plt.subplots()
    ax.bar(labels, VMs_count, 0.35, yerr=VMs_std, color=colors)
    ax.set_ylabel("VM Lifetime in seconds")
    plt.savefig('images/spec_lifetime.png')

    handles = [plt.Rectangle((0, 0), 1, 1, color=colors[index]) for index in range(len(colors))]
    plt.legend(handles, labels)
    plt.show()


if __name__ == '__main__':
    plotResult(buildResult())
