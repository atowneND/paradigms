class Employee:
    next_employee_number = 0

    def __init__(self, n, t, d, s):
        employee_number = self.next_employee_number
        self.next_employee_number += 1
        self.name = n
        self.title = t
        self.dept = d
        self.salary = s

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

if __name__=="__main__":
    print "hi"
    e = Employee("a",'woo',"wut",10000)
    print e.next_employee_number
    print e.getSalary()
    e.giveRaise(10)
    print e.getSalary()

