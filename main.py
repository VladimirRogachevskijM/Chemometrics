from openpyxl import load_workbook

from load import load_dataset
from vector import Vector
from forel import get_cluster_vectors
from core import mape_calc

filename = 'Test.xlsx'
sheet = 'Data'

wb = load_workbook(filename)
ws = wb[sheet]

X = []
i = 1
col = 2
while ws.cell(row = 1, column = col).value != None:
    X_n_vals = []
    while ws.cell(row = i, column = 1).value != None:
        X_n_vals.append(ws.cell(row = i, column = 1).value)
        i += 1

    X.append(X_n_vals)
    col += 1

Y = []

i = 1
while ws.cell(row = i, column = 2).value != None:
    Y.append(ws.cell(row = i, column = 2).value)
    i += 1

