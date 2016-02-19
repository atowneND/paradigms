# Ashley Towne
# 2/17/2016
# d11.py

#from employee import employee as emp
from employee.employee import *
from salaries import *
import csv


if __name__=="__main__":
    """
        Ashley Towne
        2/17/2016
        d11.py
    """
    # generates dictionary of job titles and classes
    roleclassfile = 'roleclass.csv'
    class_dict = {}
    with open(roleclassfile) as f:
        data = csv.DictReader(f,fieldnames=['Title','Class'])
        for row in data:
            if (row['Title']):
                title = row['Title']
                jobclass = row['Class']
                class_dict[title] = jobclass

    # generate the dictionary of city employees by reading chisalaries.csv
    inputfile = 'chisalaries.csv'
    employee_list = []
    with open(inputfile) as f:
        data = csv.DictReader(f)
        for row in data:
            if (row['Name']):
                name = row['Name']
                title = row['Position Title']
                dept = row['Department']
                emp_class = class_dict[title]
                salary =  float(row['Employee Annual Salary'].replace('$',''))
                if (emp_class == 'A'):
                    e = EmployeeA(name, title, dept, salary)
                elif (emp_class == 'AB'):
                    e = EmployeeAB(name, title, dept, salary)
                elif (emp_class == 'C'):
                    e = EmployeeC(name, title, dept, salary)
                employee_list.append(e)

    # compute and print the percentages of city salary being paid to employees for each class
    a,b,c=computeClassPercentages(employee_list,class_dict)
    print "Percent before raise (A,B,C): %.4f%%, %.4f%%, %.4f%%"%(a*100.,b*100.,c*100.)

    # give every employee 5 raises
    for i in xrange(5):
        giveEveryoneARaise(employee_list)

    # compute and print the percentages of city salary being paid to employees for each class
    a,b,c=computeClassPercentages(employee_list,class_dict)
    print "Percent after raise (A,B,C): %.4f%%, %.4f%%, %.4f%%"%(a*100.,b*100.,c*100.)

    # report the median and average salaries of all city employees after the raise
    print "Median salary of all city employees: $%.2f" % getMedianSalary(employee_list)
    print "Average salary of all city employees: $%.2f" % getAverageSalary(employee_list)
