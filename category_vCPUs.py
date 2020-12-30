import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def buildResult():
    VMTable = pd.read_csv("Dataset/vmtable.csv.gz", header=None)[[8, 9]]
    groups = VMTable.groupby([8])
    results = []
    for key, group in groups:
        group[9] = np.where(group[9] == '>24', '30', group[9])
        count = pd.to_numeric(group[9]).sum()

        gr = {'label': key, 'count': count}
        results.append(gr)

    res = {'labels': [], 'counts': []}
    for i in range(len(results)):
        res['labels'].append(results[i]['label'])
        res['counts'].append(results[i]['count'])

    return res


def plotResult(result):
    plt.title('vCores share per category')
    plt.pie(result['counts'], labels=result['labels'], autopct='%1.1f%%', startangle=0, explode=(0.2, 0.2, 0.2))
    plt.legend()
    plt.savefig('images/category_vCPU.png')


if __name__ == '__main__':
    plotResult(buildResult())
