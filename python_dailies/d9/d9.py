# Ashley Towne
# 2/15/2016
# d9.py

import csv

inputfile = 'chisalaries.csv'

name = []
position = []
department = []
salary = []

with open(inputfile) as f:
    # part 1
    data = csv.DictReader(f)
    for row in data:
        if (row['Name']):
            name.append(row['Name'])
            position.append(row['Position Title'])
            department.append(row['Department'])
            salary.append(row['Employee Annual Salary'])

    # part 2
    for i in xrange(len(salary)):
        salary[i] = float(salary[i].replace('$',''))

    # part 3
    total_salaries = 0
    num_employees = 0
    for i in xrange(len(salary)):
        if (salary[i]!=0):
            num_employees = num_employees +1
        total_salaries = total_salaries + salary[i]

    maxnumlen = len(str(total_salaries))
    avg_salary = total_salaries/num_employees

    # THIS FORMAT DOESN'T WORK ON THE PYTHON VERSION THAT THE STUDENT MACHINES
    # HAVE BUT IT WORKS ON MY LAPTOP
#    print 'Total payroll:       ${:>}'.format(total_salaries)
#    print 'Number of employees: {:>{}}'.format(num_employees,maxnumlen+1)
#    print 'Average yearly pay:  ${:>{}.>2f}'.format(avg_salary,maxnumlen)

    print 'Total payroll:       $%0.2f' % total_salaries
    print "Number of employees:  %s%i" % (" "*(maxnumlen-len(str(num_employees))), num_employees)
    print "Average yearly pay:  $%s%0.2f" % (" "*(maxnumlen-len(str(round(avg_salary,2)))), avg_salary)

    # part 4
    department_set = set(department)
    print "Number of city departments: %i" % len(department_set)
    print "Names of city departments: "
    for i in department_set:
        print "\"%s\"" % i
