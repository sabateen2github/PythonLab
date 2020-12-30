import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def buildResult():
    VMTable = pd.read_csv("Dataset/vmtable.csv.gz", header=None)[[2, 10]]
    VMTable[10] = pd.to_numeric(np.where(VMTable[10] == '>64', 70, VMTable[10]))

    DeploymentsTable = pd.read_csv("Dataset/deployments.csv.gz", header=None)
    DeploymentsTable[1] = pd.to_numeric(DeploymentsTable[1])

    groups = DeploymentsTable.groupby([1])

    results = {'deployment_size': [], 'avg': []}
    for key, group in groups:
        results['deployment_size'].append(key)
        related_vms = VMTable[2].isin(group[0])
        vms = VMTable[related_vms]
        results['avg'].append(vms[10].sum() / vms[10].shape[0])
    return results


def plotResult(result):
    print(result)

    plt.rcParams['font.size'] = '6'

    fig, ax = plt.subplots()

    ax.scatter(result['deployment_size'], result['avg'])
    ax.set_ylabel("avg. vMemory bucket (GB)")
    ax.set_xlabel("deployment size")

    plt.savefig('images/size_of_deployment_mean_of_vMem_bucket.png')
    plt.show()


if __name__ == '__main__':
    plotResult(buildResult())
