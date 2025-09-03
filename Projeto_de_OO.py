#Implementações atuais do projeto de software 
from datetime import datetime
from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name, age, email):
        self._name = name  
        self._age = age
        self._email = email

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if isinstance(value, int) and value > 0:
            self._age = value
        else:
            raise ValueError("Age must be a positive number")
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if "@" in value:
            self._email = value
        else:
            raise ValueError("Email must contain @")
    
    @abstractmethod
    def get_role(self):
        pass
    
    @abstractmethod
    def display_info(self):
        pass

class Employee(Person):
    number_of_employees = 0
    
    def __init__(self, name, age, email, department, work_position, salary_per_hour, hire_date):
        super().__init__(name, age, email)
        self._department = department
        self._work_position = work_position
        self._salary_per_hour = salary_per_hour
        self._hire_date = hire_date
        self._benefits = []
        self._performance = []
        self._training = []
        self._requests = []
        Employee.number_of_employees += 1
    
    @property
    def department(self):
        return self._department
    
    @department.setter
    def department(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._department = value
        else:
            raise ValueError("Department must be a non-empty string")
    
    @property
    def work_position(self):
        return self._work_position
    
    @work_position.setter
    def work_position(self, value):
        self._work_position = value
    
    @property
    def salary_per_hour(self):
        return self._salary_per_hour
    
    @salary_per_hour.setter
    def salary_per_hour(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self._salary_per_hour = value
        else:
            raise ValueError("Salary must be a positive number")
    
    @property
    def hire_date(self):
        return self._hire_date
    
    @hire_date.setter
    def hire_date(self, value):
        self._hire_date = value
    
    def get_role(self):
        return f"Employee - {self._work_position}"
    
    def display_info(self):
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Email: {self._email}")
        print(f"Department: {self._department}")
        print(f"Position: {self._work_position}")
        print(f"Salary per hour: {self._salary_per_hour}")
        print(f"Hire Date: {self._hire_date}")
        print(f"Benefits: {', '.join(self._benefits) if self._benefits else 'None'}")
    
    def __str__(self):
        return self._name

    def add_leave_request(self, start_date, end_date, reason):
        leave = {
            "f_Date": start_date,
            "s_Date": end_date,
            "Description": reason
        }
        self._requests.append(leave)
    
    def remove_leave_request(self, index):
        if len(self._requests) <= 0:
            print("There's nothing here")
        elif 0 <= index < len(self._requests):
            removed = self._requests.pop(index)
            print(f"The leave request period {removed['f_Date']} to {removed['s_Date']} was removed")
        else:
            print("Invalid index")
    
    def show_leave_requests(self):
        print(f"Leave requests scheduled for {self._name}")
        if not self._requests:
            print(f"There's no leave request scheduled for {self._name}")
        else:
            for i, leave in enumerate(self._requests, 1):
                print(f"{i}) {leave['f_Date']} to {leave['s_Date']} - {leave['Description']}")
    
    def add_training(self, date_str, time_str, description):
        session = {
            "Date": date_str,
            "Time": time_str,
            "Description": description
        }
        self._training.append(session)
    
    def remove_training(self, index):
        if len(self._training) <= 0:
            print("There's nothing here")
        elif 0 <= index < len(self._training):
            removed = self._training.pop(index)
            print(f"The training session on {removed['Date']} at {removed['Time']} was removed.")
        else:
            print("Invalid Index")
    
    def show_training(self):
        print(f"Meeting sessions scheduled for {self._name}")
        if not self._training:
            print(f"There's no session scheduled for {self._name}")
        else:
            for i, session in enumerate(self._training, 1):
                print(f"{i}) {session['Date']} at {session['Time']} - {session['Description']}")
    
    def add_performance_evaluation(self, level):
        performance_levels = {1: "Good", 2: "Average", 3: "Bad"}
        if level in performance_levels:
            self._performance.append(level)
            print(f"Evaluation '{performance_levels[level]}' added for {self._name}.")
        else:
            print("Invalid input")
    
    def remove_performance_evaluation(self, level):
        performance_levels = {1: "Good", 2: "Average", 3: "Bad"}
        if 0 <= level < len(self._performance):
            removed = self._performance.pop(level)
            print(f"Evaluation '{performance_levels[removed]}' was removed successfully.")
        else:
            print("Invalid index")
    
    def show_performance(self):
        performance_levels = {1: "Good", 2: "Average", 3: "Bad"}
        print(f"\nPerformance evaluation of {self._name}:")
        if self._performance:
            for i, level in enumerate(self._performance, 1):
                print(f"{i}) {performance_levels[level]}")
        else:
            print("No one evaluated")
    
    
    def add_benefit(self, benefit):
        if benefit not in self._benefits:
            self._benefits.append(benefit)
            print(f"The benefit {benefit} was added to {self._name}")
        else:
            print("The benefit was already added")
    
    def remove_benefit(self, benefit):
        if benefit in self._benefits:
            self._benefits.remove(benefit)
            print(f"The benefit {benefit} was removed from {self._name}")
        else:
            print("The benefit was already removed")


class Manager(Employee):
    def __init__(self, name, age, email, department, salary_per_hour, hire_date, team_size=0):
        super().__init__(name, age, email, department, "Manager", salary_per_hour, hire_date)
        self._team_size = team_size
        self._managed_employees = []
    
   
    def get_role(self):
        return f"Manager - {self._department} Department"
    
    def display_info(self):
        super().display_info()  
        print(f"Team Size: {self._team_size}")
        print(f"Managed Employees: {len(self._managed_employees)}")

class Intern(Employee):
    def __init__(self, name, age, email, department, salary_per_hour, hire_date, mentor=None):
        super().__init__(name, age, email, department, "Intern", salary_per_hour, hire_date)
        self._mentor = mentor
    
    def get_role(self):
        return f"Intern - {self._department} Department"
    
    def display_info(self):
        super().display_info()
        print(f"Mentor: {self._mentor.name if self._mentor else 'Not assigned'}")

class Report(ABC):
    def __init__(self, employee):
        self._employee = employee
    
    @abstractmethod
    def generate_report(self):
        pass

class Attendance(Report):
    def __init__(self, employee):
        super().__init__(employee)
        self._record = []
    
    def clock_in(self):
        now = datetime.now()
        self._record.append({"in": now, "out": None})
        print(f"{self._employee.name} clocked in at {now.strftime('%H:%M:%S')}")
    
    def clock_out(self):
        now = datetime.now()
        if self._record and self._record[-1]["out"] is None:
            self._record[-1]["out"] = now
            print(f"{self._employee.name} clocked out at {now.strftime('%H:%M:%S')}")
        else:
            print("You need to clock in before clock out")
    
    def show_records(self):
        print(f"\nRecords of {self._employee.name}: ")
        for i, record in enumerate(self._record, 1):
            in_time = record['in'].strftime('%Y-%m-%d %H:%M:%S')
            out_time = record['out'].strftime('%Y-%m-%d %H:%M:%S') if record['out'] else "Still working"
            print(f"{i}) IN: {in_time} | OUT: {out_time}")

    def worked_hours_per_day(self):
        print(f"\nWorked hours for {self._employee.name}:")
        total_seconds = 0

        for i, record in enumerate(self._record, 1):
            in_time = record["in"]
            out_time = record["out"]

            if out_time is not None:
                worked = out_time - in_time
                total_seconds += worked.total_seconds()
                print(f"{i}) {in_time.strftime('%Y-%m-%d')} - {worked}")
            else:
                print(f"{i}) {in_time.strftime('%Y-%m-%d')} - still working...")

        total_hours = total_seconds // 3600
        total_minutes = (total_seconds % 3600) // 60

        print(f"\nTotal worked time: {int(total_hours)} hours and {int(total_minutes)} minutes\n")
    
    def generate_report(self):
        self.show_records()

class PaymentCalculator(ABC):
    def __init__(self, attendance, salary_per_hour):
        self._attendance = attendance
        self._salary_per_hour = salary_per_hour
    
    @abstractmethod
    def calculate_payment(self):
        pass

class Payment(PaymentCalculator):
    def calculate_payment(self):
        total_seconds = 0
        for record in self._attendance._record:
            if record["in"] and record["out"]:
                worked = record["out"] - record["in"]
                total_seconds += worked.total_seconds()
        total_hours = total_seconds / 3600
        pay = total_hours * self._salary_per_hour
        return pay

class Compliance(Report):
    def __init__(self, employee):
        super().__init__(employee)
        self._violations = []
    
    def add_violation(self, date_str, description, severity):
        violation = {
            "Date": date_str,
            "Description": description,
            "Severity": severity
        }
        self._violations.append(violation)
        print(f"Violation added for {self._employee.name}: {description} ({severity})")

    def remove_violation(self, index):
        if 0 <= index < len(self._violations):
            removed = self._violations.pop(index)
            print(f"Violation on {removed['Date']} removed successfully.")
        else:
            print("Invalid index")

    def show_violations(self):
        print(f"\nCompliance Violations for {self._employee.name}:")
        if not self._violations:
            print("No violations recorded.")
        else:
            for i, v in enumerate(self._violations, 1):
                print(f"{i}) {v['Date']} - {v['Description']} | Severity: {v['Severity']}")

    def generate_report(self):
        print(f"\nCompliance Report for {self._employee.name}")
        print(f"Employee: {self._employee.name}")
        print(f"Department: {self._employee.department}")
        print(f"Work Position: {self._employee.work_position}")
        print(f"Number of Violations: {len(self._violations)}")
        if self._violations:
            print("Details:")
            for v in self._violations:
                print(f" - {v['Date']} | {v['Description']} (Severity: {v['Severity']})")
        else:
            print("Employee is compliant with company policies.")

employee_1 = Employee("Marcela Rocha", 19, "Marcela_2023@gmail.com", "Sistemas embarcados", "Especialista em Hardware", 500, 2023)
employee_2 = Manager("Fernando Emídio", 21, "Fe_Emi@gmail.com", "Redes de computadores", 200, 2024)
employee_3 = Intern("David Kelve", 20, "dkob@ic.ufal.br", "Recursos humanos", 300, 2025)

attendance_1 = Attendance(employee_1)
attendance_2 = Attendance(employee_2)
attendance_3 = Attendance(employee_3)

employees_list = [employee_1, employee_2, employee_3]
attendance_list = [attendance_1, attendance_2, attendance_3]

compliance_list = []
for employee in employees_list:
    compliance_list.append(Compliance(employee))

while True:
    print("============== Human Resources Management System ==============\n")
    print("Choose your action: ")
    print("(1) Employees Data\n(2) Management\n(3) Payment\n(4) Compliance Report\n(5) Exit")

    try:
        chose = int(input())

        match chose:
            case 1:
                print("Choose your action: ")
                print("(1) Employees documentation\n(2) Add a new employee\n(3) Employees modify\n(4) Remove an Employee\n(5) Benefits management ")
                chose_1 = int(input())
                
                match chose_1:
                    case 1: 
                        print("\n")
                        for employee in employees_list:
                            employee.display_info() 
                            print(f"Role: {employee.get_role()}")  
                            print("\n")
                        print(f"Number of employees: {Employee.number_of_employees}")
                    
                    case 2: 
                       print("Please, right below add the new employee documentation!")

                       while True:
                            try:
                                name = input("Name: ")
                                try:
                                    age = int(input("Age: "))
                                except ValueError:
                                    print("Age must be a number. Please try again.")
                                    continue
                                
                                email = input("Email: ")
                                department = input("Department: ")
                                work_position = input("Work Position: ")
                            
                                try:
                                    salary = float(input("Salary per hours: "))
                                except ValueError:
                                    print("Salary must be a number. Please try again.")
                                    continue
                                
                                hire_date = input("Hire Date: ")
                                
                                print("Employee Type: (1) Regular Employee (2) Manager (3) Intern")
                                try:
                                    emp_type = int(input("Choose type: "))
                                except ValueError:
                                    print("Invalid type, creating regular employee")
                                    emp_type = 1
                                
                                try:
                                    if emp_type == 1:
                                        new_employee = Employee(name, age, email, department, work_position, salary, hire_date)
                                    elif emp_type == 2:
                                        new_employee = Manager(name, age, email, department, salary, hire_date)
                                    elif emp_type == 3:
                                        new_employee = Intern(name, age, email, department, salary, hire_date)
                                    else:
                                        print("Invalid type, creating regular employee")
                                        new_employee = Employee(name, age, email, department, work_position, salary, hire_date)

                                    employees_list.append(new_employee)
                                    attendance_list.append(Attendance(new_employee))
                                    compliance_list.append(Compliance(new_employee))

                                    print("\nEmployee successfully added!")
                                    print(f"Number of employees: {Employee.number_of_employees}")
                                    
                                    again = input("Do you want to add another employee? (y/n) ").lower()
                                    if again != 'y':
                                        break
                                
                                except ValueError as e:

                                    print(f"Validation error: {e}")
                                    print("Please try again with correct data.")
                                    continue
                                    
                            except KeyboardInterrupt:
                                print("\nOperation cancelled by user.")
                                break
                            except Exception as e:
                                print(f"Unexpected error: {e}")
                                continue
                    
                    case 3:
                        while True:
                            j = 1
                            print("Employees list")
                            for employee in employees_list:
                                print(f"({j}) {employee.name}")
                                j += 1
                            try:
                                mod = int(input("Choose the employee you want to modify: "))
                                if 1 <= mod <= len(employees_list):
                                    chosen_one = employees_list[mod-1]

                                    types_of_data = {
                                        1: "name",
                                        2: "age", 
                                        3: "email",
                                        4: "department",
                                        5: "work_position",
                                        6: "salary_per_hour",
                                        7: "hire_date"
                                    }
                                    
                                    print("(1) Name || (2) Age || (3) Email || (4) Department || (5) Work Position || (6) Salary per hours || (7) Hire Date")
                                    data = int(input("Choose data you want to modify: "))
                                    
                                    if data in types_of_data:
                                        new_value = input(f"Enter the new data for {types_of_data[data]}: ")
                                        if types_of_data[data] in ["age", "salary_per_hour"]:
                                            new_value = float(new_value) if types_of_data[data] == "salary_per_hour" else int(new_value)

                                        if types_of_data[data] == "name":
                                            chosen_one.name = new_value

                                        elif types_of_data[data] == "age":
                                            chosen_one.age = new_value
                                        elif types_of_data[data] == "email":
                                            chosen_one.email = new_value

                                        elif types_of_data[data] == "department":
                                            chosen_one.department = new_value

                                        elif types_of_data[data] == "work_position":
                                            chosen_one.work_position = new_value
                                        elif types_of_data[data] == "salary_per_hour":
                                            chosen_one.salary_per_hour = new_value
                                            
                                        elif types_of_data[data] == "hire_date":
                                            chosen_one.hire_date = new_value
                                        
                                        print(f"{types_of_data[data]} was modified successfully")
                                    else:
                                        print("Invalid data option")

                                    loop = input("Do you want to modify some attribute again (y/n)? ")
                                    if loop != 'y':
                                        break
                                else:
                                    print("Invalid employee number\n")
                                    
                            except (ValueError, Exception) as e:
                                print(f"Error: {e}")
                    
                    case 4: 
                        while True:
                            if len(employees_list) == 0:
                                print("There's nothing here")
                                break
                            
                            i = 1
                            print("Employees list")
                            for employee in employees_list:
                                print(f"({i}) {employee.name}")
                                i += 1
                            
                            try:
                                remove_index = int(input("Enter the number of the employee to remove: "))
                                if 1 <= remove_index <= len(employees_list):
                                    removed = employees_list.pop(remove_index-1)
                                    attendance_list.pop(remove_index-1)
                                    compliance_list.pop(remove_index-1)
                                    Employee.number_of_employees -= 1
                                    print(f"{removed.name} has been removed from the system.\n")
                                else:
                                    print("Invalid employee number\n")
                            except ValueError:
                                print("Invalid input. Please enter a number.\n")

                            again = input("Do you want to remove another employee? (y/n) ").lower()
                            if again != 'y':
                                break
                    
                    case 5: 
                        print("Employees list")
                        for i, employee in enumerate(employees_list, start=1):
                            print(f"({i}) {employee.name}")
                        try:
                            chosen = int(input("Choose an employee: "))-1
                            if 0 <= chosen < len(employees_list):
                                chosen_one = employees_list[chosen]
                                print(f"Managing benefits of {chosen_one.name}")
                                print("(1) Add benefit\n(2) Remove benefit\n(3) Show benefits")
                                
                                act = int(input("Choose your action: "))

                                if act == 1:
                                    benefit = input("Enter the benefit to add: ")
                                    chosen_one.add_benefit(benefit)
                                elif act == 2:
                                    benefit = input("Enter the benefit to remove: ")
                                    chosen_one.remove_benefit(benefit)
                                elif act == 3:
                                    print("Benefits:", ", ".join(chosen_one._benefits) if chosen_one._benefits else "None")
                                else:
                                    print("Invalid option")
                            else:
                                print("Invalid Employee number")

                        except ValueError:
                            print("Invalid input. Please enter a number.\n")
                    
                    case _:
                        print("Invalid option")

            case 2: 
                print("Choose your action: ")
                print("(1) Time tracking register\n(2) Attendance Records\n(3) Show worked hours per employee\n(4) Performance Evaluation management\n(5) Meetings\n(6) Leave request")
                chose_2 = int(input())
                
                match chose_2:
                    case 1: 
                        clock = int(input("What you want to register?\n(1)Clock in\n(2)Clock out\n"))
                        print("Employees list")
                        for i, employee in enumerate(employees_list, start=1):
                            print(f"({i}) {employee.name}")
                        try:
                            chose = int(input("Choose one employee to register: "))-1
                            if 0 <= chose < len(employees_list):
                                chosen_one = attendance_list[chose]

                                if clock == 1:
                                    chosen_one.clock_in()
                                elif clock == 2:
                                    chosen_one.clock_out()
                                else:
                                    print("Invalid option")
                            else:
                                print("Invalid employee number")
                        except ValueError:
                            print("Invalid input. Please enter a number.\n")
                    
                    case 2:
                        for attendance in attendance_list:
                            attendance.show_records()  
                            print()
                    
                    case 3: 
                        print("Employees list")
                        for i, employee in enumerate(employees_list, start=1):
                            print(f"({i}) {employee.name}")
                        try:
                            chose = int(input("Choose one employee to view worked hours: "))-1
                            if 0 <= chose < len(employees_list):
                                attendance_list[chose].worked_hours_per_day()
                            else:
                                print("Invalid employee number.\n")
                        except ValueError:
                            print("Invalid input")
                    
                    case 4: 
                        print("Employees list")
                        for i, employee in enumerate(employees_list, start=1):
                            print(f"({i}) {employee.name}")
                            
                        try:
                            chose = int(input())-1
                            if 0 <= chose < len(employees_list):
                                chosen_one = employees_list[chose]
                                print("(1) Add an evaluation\n(2) Remove an evaluation\n(3) Show the evaluation")
                                case = int(input("Choose one index: "))
                                
                                if case == 1:
                                    print("Choose the evaluation level:")
                                    print("(1) Good\n(2) Average\n(3) Bad")
                                    eva = int(input("Level: "))
                                    chosen_one.add_performance_evaluation(eva)
                                elif case == 2:
                                    chosen_one.show_performance()
                                    index = int(input("Type the number you want to remove: ")) - 1
                                    chosen_one.remove_performance_evaluation(index)
                                elif case == 3:
                                    chosen_one.show_performance()
                                else:
                                    print("Invalid index")
                            else:
                                print("Invalid employee number.\n")

                        except ValueError:
                            print("Invalid input")
                    
                    case 5: 
                        print("Employees list")
                        for i, employee in enumerate(employees_list, start=1):
                            print(f"({i}) {employee.name}")
                        try:
                            chose = int(input("Choose one employee to analyze the meeting schedule: ")) - 1
                            if 0 <= chose < len(employees_list):
                                chosen_one = employees_list[chose]
                                print("(1) Add a new meeting\n(2) Remove a meeting\n(3) Show the meetings")
                                case = int(input("Choose one index: "))
                                
                                if case == 1:
                                    data = str(input("Date: "))
                                    temp = str(input("Hour: "))
                                    description = str(input("Description: "))
                                    chosen_one.add_training(data, temp, description)
                                elif case == 2:
                                    chosen_one.show_training()
                                    index = int(input("Type the number you want to remove: "))-1
                                    chosen_one.remove_training(index)
                                elif case == 3:
                                    chosen_one.show_training()
                                else:
                                    print("Invalid index")
                            else:
                                print("Invalid employee number.\n")

                        except ValueError:
                            print("Invalid input")
                    
                    case 6: 
                        print("Employees list")
                        for i, employee in enumerate(employees_list, start=1):
                            print(f"({i}) {employee.name}")
                        try:
                            chose = int(input("Choose one employee to manage leave requests: ")) - 1
                            if 0 <= chose < len(employees_list):
                                chosen_one = employees_list[chose]
                                print(f"Managing leave requests for {chosen_one.name}")
                                print("(1) Add leave request\n(2) Remove leave request\n(3) Show leave requests")
                                action = int(input("Choose your action: "))

                                if action == 1:
                                    start_date = input("Enter start date (e.g., 01/08): ")
                                    end_date = input("Enter end date (e.g., 05/08): ")
                                    reason = input("Enter reason: ")
                                    chosen_one.add_leave_request(start_date, end_date, reason)
                                elif action == 2:
                                    chosen_one.show_leave_requests()
                                    index = int(input("Enter the index of the leave request to remove: ")) - 1
                                    chosen_one.remove_leave_request(index)
                                elif action == 3:
                                    chosen_one.show_leave_requests()
                                else:
                                    print("Invalid option")
                            else:
                                print("Invalid employee number.")
                        except ValueError:
                            print("Invalid input. Please enter numbers.")
                    
                    case _:
                        print("Invalid option")

            case 3: 
                print("(1) Payment without benefits")
                chose = int(input("Choose your action: "))
                
                match chose:
                    case 1:
                        for i, employee in enumerate(employees_list, start=1):
                            print(f"({i}) {employee.name}")
                        person = int(input("Choose the employee you want to calculate the salary: "))-1
                        
                        try:
                            if 0 <= person < len(employees_list):
                                employee = employees_list[person]
                                attendance = attendance_list[person]
                                payment = Payment(attendance, employee.salary_per_hour)  # POLIMORFISMO
                                money = payment.calculate_payment()

                                print(f"\nTotal payment for {employee.name}: R$ {money:.2f}\n")
                            else:
                                print("Invalid employee number\n")
                        except ValueError:
                            print("Invalid input")
                    case _:
                        print("Invalid option")

            case 4: 
                print("Compliance Management")
                print("(1) Add Violation\n(2) Remove Violation\n(3) Show Violations\n(4) Generate Compliance Report")
                action = int(input("Choose your action: "))
                
                print("Employees list:")
                for i, employee in enumerate(employees_list, start=1):
                    print(f"({i}) {employee.name}")
                
                try:
                    chose = int(input("Choose the employee: ")) - 1

                    if 0 <= chose < len(employees_list):
                        chosen_one = compliance_list[chose]

                        if action == 1:
                            date_str = input("Enter violation date (dd/mm/yyyy): ")
                            description = input("Enter violation description: ")
                            severity = input("Enter severity (Low/Medium/High): ")
                            chosen_one.add_violation(date_str, description, severity)

                        elif action == 2:
                            chosen_one.show_violations()
                            if chosen_one._violations:
                                index = int(input("Enter violation index to remove: ")) - 1
                                chosen_one.remove_violation(index)

                        elif action == 3:
                            chosen_one.show_violations()

                        elif action == 4:
                            chosen_one.generate_report() 

                        else:
                            print("Invalid option.")
                    else:
                        print("Invalid employee number.")
                        
                except ValueError:
                    print("Invalid input. Please enter numbers.")

            case 5: 
                exit_confirm = input("Are you sure? (y/n) ").lower()
                if exit_confirm == 'y':
                    break
            
            case _:
                print("Invalid option")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")