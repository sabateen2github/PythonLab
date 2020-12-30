import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def buildResult():
    VMTable = pd.read_csv("Dataset/vmtable.csv.gz", header=None)[[8, 9]]
    VMTable[9] = pd.to_numeric(np.where(VMTable[9] == '>24', 30, VMTable[9]))

    groups = VMTable.groupby([8])

    results = {'labels': [], 'avg': []}
    for key, group in groups:
        results['labels'].append(key)
        results['avg'].append(group[9].mean())
    return results


def plotResult(result):
    print(result)

    plt.rcParams['font.size'] = '6'

    fig, ax = plt.subplots()
    ax.bar(result['labels'], result['avg'], 0.35)
    ax.set_ylabel("avg. vCore bucket")

    plt.savefig('images/vCore_bucket_category.png')


if __name__ == '__main__':
    plotResult(buildResult())
