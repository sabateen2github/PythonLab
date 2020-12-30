import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def buildResult():
    SubTable = pd.read_csv("Dataset/subscriptions.csv.gz", header=None)[[0, 2]]

    SubTable[2] = pd.to_numeric(SubTable[2])

    SubTable.sort_values(by=2, inplace=True, ascending=True)

    results = {'cSubscribers': [0], 'cVMs': [0]}

    num = 0
    for i in range(SubTable.shape[0]):
        results['cSubscribers'].append(num + 1)
        results['cVMs'].append(SubTable[2].values[i] + results['cVMs'][-1])
        num += 1
    return results


def plotResult(result):
    print(result['cSubscribers'])

    plt.rcParams['font.size'] = '6'

    fig, ax = plt.subplots()

    ax.plot(result['cSubscribers'], result['cVMs'])
    ax.set_ylabel("Number of VMs in Millions")
    ax.set_xlabel("Number of subscriptions")

    plt.savefig('images/vms_Subscribers.png')


if __name__ == '__main__':
    plotResult(buildResult())
