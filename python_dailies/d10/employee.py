class Employee:
    next_employee_number = 0

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

    def giveRaise(self,percentage):
        self.salary = self.salary*(1.0+(percentage*1.0)/100.)

    def __str__(self):
        print "[Employee name: %s, %s, %s, $%0.2f]" % (self.name.upper(),self.title.upper(),self.dept.upper(),self.salary)

#######################################
#if __name__=="__main__":
#    print "hi"
#    e = Employee("a",'woo',"wut",10000)
#    print e.next_employee_number
#    print e.getSalary()
#    e.giveRaise(10)
#    print e.getSalary()
#    e.__str__()
