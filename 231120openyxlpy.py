import openpyxl
wb=openpyxl.Workbook()
ws=wb.active
ws.title='Data'
data=[
    ['Name','Age'],
    ['ee','1'],
    ['cs','1']

]
for row in data:
    ws.append(row)
wb.save('append_example.xlsx')