import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


def buildResult():
    VMTable = pd.read_csv("Dataset/vmtable.csv.gz", header=None)[[2, 9, 10]]

    VMTable[9] = pd.to_numeric(np.where(VMTable[9] == '>24', 30, VMTable[9]))
    VMTable[10] = pd.to_numeric(np.where(VMTable[10] == '>64', 70, VMTable[10]))

    groups = VMTable.groupby([9, 10])

    DeploymentsTable = pd.read_csv("Dataset/deployments.csv.gz", header=None)
    DeploymentsTable[1] = pd.to_numeric(DeploymentsTable[1])

    results = {'x': [], 'y': [], 'z': [], 'w': []}
    for key, group in groups:
        deployment_ids = DeploymentsTable[0].isin(group[2])
        deployment_ids = DeploymentsTable[deployment_ids]
        size = deployment_ids[1].sum() / deployment_ids.shape[0]
        results['x'].append(key[0])
        results['y'].append(key[1])
        results['z'].append(size)
        results['w'].append(size)

    return results


def plotResult(result):
    plt.rcParams['font.size'] = '6'

    fig, ax = plt.subplots()
    ax.scatter('x', 'y', c='z', s='w', data=result, cmap='viridis')
    ax.set_ylabel("vMemory (GB)")
    ax.set_xlabel("vCores")
    im = cm.ScalarMappable()
    im.set_clim(0, max(result['z']))
    plt.colorbar(im)
    plt.savefig('images/avg_size_deployment_vMem_vCore.png')


if __name__ == '__main__':
    plotResult(buildResult())
