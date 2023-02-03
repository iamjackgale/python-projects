# SPDX-License-Identifier: MIT

# title: JSONFileGenerator.py
# author: jackgale.eth
# dev: tool to extract json output using xlwings from spreadsheet at specified file importPath and convert into fresh json files at specified folder exportPath, using parameters specified in a local .env file.

import xlwings as xw
import os.path
from dotenv import load_dotenv

# Imports from .env
load_dotenv()
importPath = os.getenv('IMPORT_PATH')
exportPath = os.getenv('EXPORT_PATH')
startRow = int(os.getenv('START_ROW'))
endRow = int(os.getenv('END_ROW'))
JSONColumn = int(os.getenv('JSON_COLUMN'))
numberingColumn = int(os.getenv('NUMBERING_COLUMN'))

# Setup for Relevant Workbook and Sheets
wb = xw.Book(importPath)
wb
sheet1 = wb.sheets[0]
sheet1
xw.books.active
xw.sheets.active

# Read JSON data and file number from specified rows in spreadsheet, and write to JSON file
for i in range(startRow,endRow):#102):
    rawJSONValue = sheet1.range((i,JSONColumn)).value
    newJSONValue = rawJSONValue.replace("'",'"')
    fileTitle = sheet1.range((i,numberingColumn)).value + '.json'
    filePath = os.path.join(exportPath,fileTitle)
    f = open(filePath, 'w')
    f.write(str(newJSONValue))
    f.close()