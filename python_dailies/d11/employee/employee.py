class Employee:
    next_employee_number = 0
    default_salary_inflator = 1.04

    def __init__(self, name, title, dept, salary):
        employee_number = Employee.next_employee_number
        Employee.next_employee_number += 1
        self.name = name
        self.title = title
        self.dept = dept
        self.salary = salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def getName(self):
        return self.name

    def getTitle(self):
        return self.title

    def getDept(self):
        return self.dept

    def getSalary(self):
        return self.salary

    def setName(self,newval):
        self.name = newval

    def setTitle(self,newval):
        self.title = newval

    def setDept(self,newval):
        self.dept = newval

    def setSalary(self,newval):
        self.salary = newval

    def giveRaise(self):
        self.salary = self.salary*(Employee.default_salary_inflator*1.0)

    def __str__(self):
        print "[Employee name: %s, %s, %s, $%0.2f]" % (self.name.upper(),self.title.upper(),self.dept.upper(),self.salary)

class EmployeeA(Employee):
    inflator_A = 1.02

    def giveRaise(self):
        self.salary = self.salary*(Employee.default_salary_inflator*EmployeeA.inflator_A*1.0)

    def __str__(self):
        print "[EmployeeA name: %s, %s, %s, $%0.2f]" % (self.name.upper(),self.title.upper(),self.dept.upper(),self.salary)

class EmployeeC(Employee):
    inflator_C = 1.01

    def giveRaise(self):
        self.salary = self.salary*(Employee.default_salary_inflator*EmployeeC.inflator_C*1.0)

    def __str__(self):
        print "[EmployeeC name: %s, %s, %s, $%0.2f]" % (self.name.upper(),self.title.upper(),self.dept.upper(),self.salary)

class EmployeeAB(EmployeeA):
    inflator_B = 1.08

    def giveRaise(self):
        self.salary = self.salary*(Employee.default_salary_inflator*EmployeeA.inflator_A*EmployeeAB.inflator_B*1.0)

    def __str__(self):
        print "[EmployeeAB name: %s, %s, %s, $%0.2f]" % (self.name.upper(),self.title.upper(),self.dept.upper(),self.salary)

