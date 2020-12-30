import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cm


def buildResult():
    VMTable = pd.read_csv("Dataset/vmtable.csv.gz", header=None)[[6, 9, 10]]
    groups = VMTable.groupby([9, 10])

    results = []
    for key, group in groups:

        try:
            c = int(key[0])
        except ValueError:
            c = 30
        try:
            m = int(key[1])
        except ValueError:
            m = 70

        gr = {'key': c * 10 + m, 'vCores': c, 'vMem': m, 'util': group[6].mean()}
        results.append(gr)
    results.sort(key=lambda x: x['key'])

    res = {'x': [], 'y': [], 'z': [], 'w': []}
    for i in range(len(results)):
        res['x'].append(results[i]['vCores'])
        res['y'].append(results[i]['vMem'])
        res['z'].append(results[i]['util'])
        res['w'].append(results[i]['util'] * 10)
    return res


def plotResult(result):
    plt.rcParams['font.size'] = '6'

    fig, ax = plt.subplots()
    ax.scatter('x', 'y', c='z', s='w', data=result, cmap='viridis')
    ax.set_ylabel("vMemory")
    ax.set_xlabel("vCores")
    im = cm.ScalarMappable()
    im.set_clim(0, max(result['z']))
    plt.colorbar(im)
    plt.savefig('images/scatter_vCore_vMem_vCPU_util.png')


if __name__ == '__main__':
    plotResult(buildResult())
