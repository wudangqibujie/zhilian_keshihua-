import xlsxwriter

workbook = xlsxwriter.Workbook("data.xlsx")
worksheet = workbook.add_worksheet()
worksheet.write_row("A1",["A","B"])
workbook.close()
