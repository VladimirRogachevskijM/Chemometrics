import math

from openpyxl import load_workbook

from vector import Vector
from core import get_coords

wb = load_workbook('Tests/test.xlsx')
ws = wb.active

vector_1 = Vector(get_coords(6, 1, ws))
vector_2 = Vector(get_coords(6, 3, ws))

print(vector_1.evklid_dist(vector_2))