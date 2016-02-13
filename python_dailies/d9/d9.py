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
    data = csv.DictReader(f)
    total_salaries = 0
    num_employees = 0
    for row in data:
        if (row['Name']):
            name.append(row['Name'])
            position.append(row['Position Title'])
            department.append(row['Department'])
            salary.append(row['Employee Annual Salary'])
    for i in xrange(len(salary)):
        s = float(salary[i].replace('$',''))
        if (s!=0):
            num_employees = num_employees +1
        total_salaries = total_salaries + s
    maxnumlen = len(str(total_salaries))
    avg_salary = total_salaries/num_employees
    print 'Total payroll:       ${0}'.format(total_salaries)
    print 'Number of employees:  {0}{1}'.format(' '*(maxnumlen-len(str(num_employees))),num_employees)
    print 'Average yearly pay:  ${:>10}'.format(' '*(maxnumlen-len(str(avg_salary))),avg_salary)
