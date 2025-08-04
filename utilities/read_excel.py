import openpyxl
from openpyxl.reader.excel import load_workbook


class Utils:
    def read_data_from_excel(filename):
        # data_list = []
        # workbook = load_workbook(filename=filename)
        # sheet = workbook[sheet]
        # row_count = sheet.max_row
        # column_count = sheet.max_column
        #
        # for i in range(2, row_count+1):
        #     row = []
        #     for j in range(1,column_count+1):
        #         row.append(sheet.cell(row=i,column=j).value)
        #     data_list.append(row)
        # return data_list
        workbook = openpyxl.load_workbook(filename)
        sheet = workbook.active
        data = []
        for row in sheet.iter_rows(min_row=2, values_only=True):  # Skip headers
            data.append((row[0], row[1]))
        return data




