#!/usr/bin/env python

# Module used to read Excel workbooks.
# To install in Cygwin:
# cd ~/src
# wget https://pypi.python.org/packages/source/x/xlrd/xlrd-0.9.2.tar.gz
# tar xzvf xlrd-0.9.2.tar.gz
# cd xlrd-0.9.2
# python setup.py install
import xlrd

# Read the first cell from the English worksheet in the workbook hello_excel.xlsx.
# I'm using Excel 2010.
workbook = xlrd.open_workbook("hello_excel.xlsx")
worksheet = workbook.sheet_by_name("English")
cell = worksheet.cell(0, 0)
print "[0, 0] = %s" % cell.value

