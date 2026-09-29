with open("Employee.txt", "w") as f:
    f.write("Aman,101,50000,1\nRiya,102,60000,1\nAli,103,40000,2\n")
with open("Department.txt", "w") as f:
    f.write("1,HR,Delhi\n2,IT,Mumbai\n")
emp_file = open("Employee.txt", "r")
dept_salary = {}
dept_name = {}
for line in open("Department.txt", "r"):
    did, dname, loc = line.strip().split(',')
    dept_name[did] = dname
    dept_salary[did] = [0, 0]
for line in emp_file:
    name, eid, salary, did = line.strip().split(',')
    if did in dept_salary:
        dept_salary[did][0] += int(salary)
        dept_salary[did][1] += 1
print("Department wise Average Salary:")
for did in dept_salary:
    total, count = dept_salary[did]
    if count > 0:
        avg = total / count
        print(f"{dept_name[did]} (DID {did}): {avg}")
