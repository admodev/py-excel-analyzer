import sys
from WorkbookManager import WorkbookMan

wmb = WorkbookMan()
wb_system_path = ''.join(sys.argv[1:])

wmb.workbook_path = wb_system_path

wmb.open_workbook()
