import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def buildResult():
    VMTable = pd.read_csv("Dataset/vmtable.csv.gz", header=None)[[6, 8, 9]]
    VMTable[9] = pd.to_numeric(np.where(VMTable[9] == '>24', 30, VMTable[9]))
    VMTable[6] = pd.to_numeric(VMTable[6]).round()
    VMTable[6] = VMTable[6] * VMTable[9]

    groups = VMTable.groupby([8])

    results = {'labels': [], 'util': []}
    for key, group in groups:
        results['labels'].append(key)
        results['util'].append(round(group[6].sum() / group[9].sum(), 0))
    return results


def plotResult(result):
    print(result)

    plt.rcParams['font.size'] = '6'

    fig, ax = plt.subplots()
    ax.bar(result['labels'], result['util'], 0.35, label='VM count')
    ax.set_ylabel("vCPU avg. utilization")

    plt.savefig('images/vCPU_util_category.png')


if __name__ == '__main__':
    plotResult(buildResult())
