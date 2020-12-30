import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def buildResult():
    VMTable = pd.read_csv("Dataset/vmtable.csv.gz", header=None)[[8, 10]]
    VMTable[10] = pd.to_numeric(np.where(VMTable[10] == '>64', 70, VMTable[10]))

    groups = VMTable.groupby([8])

    results = {'labels': [], 'avg': []}
    for key, group in groups:
        results['labels'].append(key)
        results['avg'].append(group[10].mean())
    return results


def plotResult(result):
    print(result)

    plt.rcParams['font.size'] = '6'

    fig, ax = plt.subplots()
    ax.bar(result['labels'], result['avg'], 0.35)
    ax.set_ylabel("avg. vMemory bucket (GB)")

    plt.savefig('images/vMem_bucket_category.png')


if __name__ == '__main__':
    plotResult(buildResult())
