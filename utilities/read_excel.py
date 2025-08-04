import openpyxl
from openpyxl.reader.excel import load_workbook
import logging
import os


class ExcelUtils:
    @staticmethod
    def read_data_from_excel(filename, sheet_name):
        """
        Read data from Excel file and return as list of dictionaries
        """
        try:
            if not os.path.exists(filename):
                raise FileNotFoundError(f"Excel file not found: {filename}")

            workbook = load_workbook(filename=filename)

            if sheet_name not in workbook.sheetnames:
                raise ValueError(f"Sheet '{sheet_name}' not found in {filename}")

            sheet = workbook[sheet_name]
            data_list = []

            # Get headers from first row
            headers = [cell.value for cell in sheet[1]]

            # Read data rows
            for row in sheet.iter_rows(min_row=2, values_only=True):
                row_dict = dict(zip(headers, row))
                data_list.append(row_dict)

            return data_list

        except Exception as e:
            logging.error(f"Error reading Excel file: {str(e)}")
            raise
