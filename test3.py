import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import csv

def test(a):
    return a**2

list1 = [1,2,3,4,5,6,7]

for i in list1:
    print("i : {},  a = {}".format(i, test(i)))
