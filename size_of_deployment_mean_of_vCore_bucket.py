import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def buildResult():
    VMTable = pd.read_csv("Dataset/vmtable.csv.gz", header=None)[[2, 9]]
    VMTable[9] = pd.to_numeric(np.where(VMTable[9] == '>24', 30, VMTable[9]))

    DeploymentsTable = pd.read_csv("Dataset/deployments.csv.gz", header=None)
    DeploymentsTable[1] = pd.to_numeric(DeploymentsTable[1])

    groups = DeploymentsTable.groupby([1])

    results = {'deployment_size': [], 'avg': []}
    for key, group in groups:
        results['deployment_size'].append(key)
        related_vms = VMTable[2].isin(group[0])
        vms = VMTable[related_vms]
        results['avg'].append(vms[9].sum() / vms[9].shape[0])
    return results


def plotResult(result):
    print(result)

    plt.rcParams['font.size'] = '6'

    fig, ax = plt.subplots()

    ax.scatter(result['deployment_size'], result['avg'])
    ax.set_ylabel("avg. vCore bucket")
    ax.set_xlabel("deployment size")

    plt.savefig('images/size_of_deployment_mean_of_vCore_bucket.png')


if __name__ == '__main__':
    plotResult(buildResult())
