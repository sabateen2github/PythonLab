import pandas as pd
import matplotlib.pyplot as plt
import random


def buildResult():
    VMTable = pd.read_csv("Dataset/vmtable.csv.gz", header=None)[[9, 10]]
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

        gr = {'key': c * 10 + m, 'name': name, 'count': count}
        results.append(gr)
    results.sort(key=lambda x: x['key'])
    return results


def plotResult(result):
    labels = []
    VMs_count = []
    VMs_std = []
    colors = []

    for i in range(len(result)):
        labels.append(result[i]['name'])
        VMs_count.append(result[i]['count'])
        VMs_std.append(1)
        colors.append((random.random(), random.random(), random.random(), 1.0))

    plt.rcParams['font.size'] = '6'

    fig, ax = plt.subplots()
    ax.bar(labels, VMs_count, 0.35, yerr=VMs_std, label='VM count', color=colors)
    ax.set_ylabel("VM count")
    handles = [plt.Rectangle((0, 0), 1, 1, color=colors[index]) for index in range(len(colors))]
    plt.legend(handles, labels)
    plt.savefig('images/vCPU_vMem_bucket.png')
    plt.show()


if __name__ == '__main__':
    plotResult(buildResult())
