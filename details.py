import os
FILE_NAME="employee.txt"
def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    salary = input("Enter Salary: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{emp_id},{name},{salary}\n")

    print("Employee Added Successfully!")


def view_employees():
    if not os.path.exists(FILE_NAME):
        print("No employee records found.")
        return

    with open(FILE_NAME, "r") as file:
        records = file.readlines()

    if not records:
        print("No employee records found.")
        return

    print("\nEmployee Records")
    print("-" * 30)

    for record in records:
        emp_id, name, salary = record.strip().split(",")
        print(f"ID: {emp_id} | Name: {name} | Salary: {salary}")


def search_employee():
    emp_id = input("Enter Employee ID to Search: ")

    found = False

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for record in file:
                eid, name, salary = record.strip().split(",")

                if eid == emp_id:
                    print("\nEmployee Found")
                    print(f"ID: {eid}")
                    print(f"Name: {name}")
                    print(f"Salary: {salary}")
                    found = True
                    break

    if not found:
        print("Employee not found.")


def delete_employee():
    emp_id = input("Enter Employee ID to Delete: ")

    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return

    records = []

    with open(FILE_NAME, "r") as file:
        records = file.readlines()

    found = False

    with open(FILE_NAME, "w") as file:
        for record in records:
            eid, name, salary = record.strip().split(",")

            if eid != emp_id:
                file.write(record)
            else:
                found = True

    if found:
        print("Employee deleted successfully.")
    else:
        print("Employee not found.")


while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        delete_employee()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
