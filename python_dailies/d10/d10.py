# Ashley Towne
# 2/15/2016
# d10.py

from employee import Employee as emp
import csv
import numpy as np

def giveEveryoneARaise(l, percentage):
    for i in xrange(len(l)):
        l[i].giveRaise(percentage)

def giveDeptARaise(l, dept, percentage):
    for i in xrange(len(l)):
        if (l[i].getDept()==dept):
            l[i].giveRaise(percentage)

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
    #ls = [e.getSalary() for e in l]
    #print "np.med =", np.median(ls)
    if (len(l)%2==0): # even
        return (l[num_peeps].getSalary() + l[num_peeps-1].getSalary())/2.
    else: # odd
        return l[num_peeps+1].getSalary()

def getOnePercent(l):
    l.sort()
    num_peeps = len(l)/100
    print len(l[-num_peeps:])
    return l[-num_peeps:]

if __name__=="__main__":
    inputfile = 'chisalaries.csv'
    employee_list = []

    # generate the list of city employees by reading chisalaries.csv
    with open(inputfile) as f:
        data = csv.DictReader(f)
        for row in data:
            if (row['Name']):
                name = row['Name']
                title = row['Position Title']
                dept = row['Department']
                salary =  float(row['Employee Annual Salary'].replace('$',''))
                e = emp(name, title, dept, salary)
                employee_list.append(e)

    print "Median salary of all city employees: $%.2f" % getMedianSalary(employee_list)
    print "Average salary of all city employees: $%.2f" % getAverageSalary(employee_list)
    # get the list containing the top 1% by salary
    top_1pc = getOnePercent(employee_list)
    # report the meidan and average salaries of the top 1%
    print "Median salary of the top 1%%: $%.2f" % getMedianSalary(top_1pc)
    print "Average salary of the top 1%%: $%.2f" % getAverageSalary(top_1pc)

    # give every a raise of 5%
    giveEveryoneARaise(employee_list,5)
    print "\nRaise of 5%"
    # report the median and average salaries of all city employees after the raise
    print "Median salary of all city employees: $%.2f" % getMedianSalary(employee_list)
    print "Average salary of all city employees: $%.2f" % getAverageSalary(employee_list)
    # get the list containing the top 1% by salary
    top_1pc = getOnePercent(employee_list)
    # report the meidan and average salaries of the top 1%
    print "Median salary of the top 1%%: $%.2f" % getMedianSalary(top_1pc)
    print "Average salary of the top 1%%: $%.2f" % getAverageSalary(top_1pc)

    # give every employee in FIRE dept. a 6% raise
    print "\nRaise of 6% for FIRE department"
    giveDeptARaise(employee_list,"FIRE",6)
    # report the median and average salaries of all city employees after the raise
    print "Median salary of all city employees: $%.2f" % getMedianSalary(employee_list)
    print "Average salary of all city employees: $%.2f" % getAverageSalary(employee_list)
    # get the list containing the top 1% by salary
    top_1pc = getOnePercent(employee_list)
    # report the meidan and average salaries of the top 1%
    print "Median salary of the top 1%%: $%.2f" % getMedianSalary(top_1pc)
    print "Average salary of the top 1%%: $%.2f" % getAverageSalary(top_1pc)
