from openpyxl import Workbook, load_workbook
import os

file_name = "output.xlsx"

if os.path.exists(file_name):
    wb = load_workbook(file_name)
    ws = wb.active
else:
    wb = Workbook()
    ws = wb.active
    ws.title = "Inputs"
    ws.append(["Name", "Age", "Role"])  # Header only once

name = input("Enter name: ")
age = input("Enter age: ")
role = input("Enter role: ")

ws.append([name, age, role])

wb.save(file_name)
print("Data added successfully!")