import openpyxl


class WorkbookMan:
    def __init__(self):
        self.workbook_path = ''

    def open_workbook(self):
        print("Operating with excel workbook...")
        wb = openpyxl.open(str(self.workbook_path))
        ws = wb.active
        print('Total number of rows: '+str(ws.max_row) +
              '. And total number of columns: '+str(ws.max_column))
