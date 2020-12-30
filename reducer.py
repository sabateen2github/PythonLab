import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    VMTable = pd.read_csv("Dataset/vmtable.csv", header=None)
    newTable = VMTable.drop(index=list(range(100000, VMTable.shape[0])))
    newTable.to_csv('Dataset/vmtabe_test.csv', header=None, index=False)
