salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]
new_salary_list = []
indexation_list = []
for salary in salary_list:
    indexation = round(salary * 0.3, 2)
    new_salary = round(salary + indexation, 2)
    new_salary_list.append(new_salary)
    indexation_list.append(indexation)
print("Salary table:")
for i in range(len(salary_list)):
    print(salary_list[i], new_salary_list[i], indexation_list[i])