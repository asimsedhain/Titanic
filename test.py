import numpy as numpy
import pandas as pandas
# import StringIO
str = open('D:\\Programs\\Python\\test.csv', 'r')
data = pandas.read_csv("D:\\Programs\\Python\\test.csv")
# cvs = numpy.genfromtxt(s,delimiter=',', missing_values=" ", skip_header=1)
# print(data.head())
print(data.loc[:, 'Cabin'].head())
# print(data.mean())
