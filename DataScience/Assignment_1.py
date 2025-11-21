#step1:Making a dict
employees = {
    101:{'name': 'Satya',
         'age':27,
         'department':'HR',
         'salary':50000}
}

#step2:Define menu syste,
def main_menu():
    print("\n1) To add employee:")
    print("2) View all employees")
    print("3) Search for employee")
    print("4) Exit")
    return input("Choose an option (1-4): ")

#step3:Add employee Functionality
def add_employee():
    emp_id = int(input("Enter the Employee Id: "))
    if emp_id in employees:
                 print("Id already existed!")
                 return
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    department = input("Enter the department: ")
    salary = float(input("Enter the salary: "))
    employees[emp_id] = {"name":name,"age":age,"department":department,"salary":salary}
    print("Employee added successfully!")

#step4:View all employees
def view_employees():
    if not employees:
        print("No employees to show.")
        return
    for emp_id, info in employees.items():
        print(f"ID: {emp_id}, Name: {info['name']}, Age: {info['age']}, Dept: {info['department']}, Salary: {info['salary']}")

#step5:Search for an employee id
def search_employee():
    emp_id = int(input("Enter the Email Id: "))
    if emp_id in employees:
        e = employees[emp_id]
        print(f" Name: {e['name']}, Age: {e['age']}, Department: {e['department']}, Salary: {e['age']}")
    else:
        print("Employee not found!")

#step6:Exit
while True:
    choice = main_menu()
    if choice == '1':
        add_employee()
    elif choice == '2':
        view_employees()
    elif choice == '3':
        search_employee()
    elif choice == '4':
        print("Exiting!")
        break