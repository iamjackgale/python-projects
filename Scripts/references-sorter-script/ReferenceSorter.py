# SPDX-License-Identifier: MIT

# title: ReferenceSorter.py
# author: jackgale.eth
# dev: Script to alphabetise cells containing multiple listed academic references in a spreadsheet, and produce a duplicate 

# IMPORTS
import xlwings as xw
import os.path
from dotenv import load_dotenv
load_dotenv("references-sorter-script/.env")
importPath = os.getenv('IMPORT_PATH')
wb = xw.Book(importPath)

# PARAMETERS
# parameters = list of nested lists - one per sheet - in sheet order
# cell range list = [start column, start row, end column, end row]
parameters = [[3,3,9,6],[3,3,9,6],[3,3,9,9],[3,3,10,8]]

# SORT METHOD
def sort(sheet, column, row):
    value = sheet.range((column,row)).value
    print (value)
    
    if value is None:
        return ""
    else:
        referenceList = []
        startValue = 0
        for i in range(len(value)):
            if value[i] == ")":
                endValue = int(i)+2
                if value[startValue] == " ":
                    startValue = startValue+1
                reference = value[startValue:endValue]
                referenceList.append(reference)
                startValue = i+3
        referenceList.sort()
        output = ' '.join(referenceList)
        return output

# SCRIPT
for i in range(4):
    sheet = wb.sheets[i]
    startRow = parameters[i][0]
    startColumn = parameters[i][1]
    endRow = parameters[i][2]
    endColumn = parameters[i][3]

    for row in range(startRow,endRow):
        for column in range(startColumn,endColumn):
            orderedReferences = sort(sheet,column,row)
            sheet.range((column,row)).value = str(orderedReferences)