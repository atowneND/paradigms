#import numpy as np

def giveEveryoneARaise(l):
    for i in xrange(len(l)):
        l[i].giveRaise()

def giveDeptARaise(l, dept):
    for i in xrange(len(l)):
        if (l[i].getDept()==dept):
            l[i].giveRaise()

def getHighestSalary(l):
    highest = 0
    for i in xrange(len(l)):
        if (l[i].getSalary()>highest):
            highest = l[i].getSalary()
    return highest

def getAverageSalary(l):
    salary_sum = 0
    #ls = [e.getSalary() for e in l]
    #print "np.avg =", np.mean(ls)
    for i in xrange(len(l)):
        salary_sum = salary_sum + l[i].getSalary()
    return salary_sum*1.0/len(l)

def getMedianSalary(l):
    l.sort()
    num_peeps = len(l)/2
    if (len(l)%2==0): # even
        return (l[num_peeps].getSalary() + l[num_peeps-1].getSalary())/2.
    else: # odd
        return l[num_peeps-1].getSalary()

def getOnePercent(l):
    l.sort()
    num_peeps = len(l)/100
    return l[-num_peeps:]

def computeClassPercentages(l,cd):
    """
        l = list of employees
        cd = class dictionary
    """
    a_salary = 0
    ab_salary = 0
    c_salary = 0
    tot_salary = 0
    for e in l:
        emp_class = cd[e.title]
        s = e.getSalary()
        if (emp_class == 'A'):
            a_salary += s
            tot_salary += s
        elif (emp_class == 'AB'):
            ab_salary += s
            tot_salary += s
        elif (emp_class == 'C'):
            c_salary += s
            tot_salary += s

    ap = a_salary*1.0/tot_salary
    abp = ab_salary*1.0/tot_salary
    cp = c_salary*1.0/tot_salary

    return ap,abp,cp

