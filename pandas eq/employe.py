import pandas as pd
data = [
    {'Employee_ID': 1, 'Name': 'Alice', 'Department': 'HR', 'Years_of_Experience': 5, 'Salary': 50000},
    {'Employee_ID': 2, 'Name': 'Bob', 'Department': 'IT', 'Years_of_Experience': 3, 'Salary': 60000},
    {'Employee_ID': 3, 'Name': 'Charlie', 'Department': 'IT', 'Years_of_Experience': 6, 'Salary': 75000},
    {'Employee_ID': 4, 'Name': 'David', 'Department': 'Marketing', 'Years_of_Experience': 2, 'Salary': 45000},
    {'Employee_ID': 5, 'Name': 'Eve', 'Department': 'HR', 'Years_of_Experience': 8, 'Salary': 70000},
    {'Employee_ID': 6, 'Name': 'Frank', 'Department': 'Marketing', 'Years_of_Experience': 4, 'Salary': 55000},
    {'Employee_ID': 7, 'Name': 'Grace', 'Department': 'IT', 'Years_of_Experience': 7, 'Salary': 80000},
    {'Employee_ID': 8, 'Name': 'Heidi', 'Department': 'HR', 'Years_of_Experience': 10, 'Salary': 85000},
    {'Employee_ID': 9, 'Name': 'Ivan', 'Department': 'Marketing', 'Years_of_Experience': 1, 'Salary': 40000},
    {'Employee_ID': 10, 'Name': 'Judy', 'Department': 'IT', 'Years_of_Experience': 4, 'Salary': 65000}
]
#converting dic to dataframe
data=pd.DataFrame(data)
print(data.to_string())

# Find the average salary of employees in each department.
average_salary=data.groupby("Department")["Salary"].mean()
print(average_salary)

# Find the employee with the highest salary.
highest_employee=data.Salary.max()
name=data.loc[data["Salary"]== highest_employee,"Name"].values[0]
print(highest_employee)
print(f"the highest salary of employee is : {name} and the salary is {highest_employee}") 

# Question 3: Calculate the salary range (difference between the highest and lowest salaries).
highest_salary=data.Salary.max()
lowest_salary=data.Salary.min()
range_salary=highest_salary-lowest_salary


highest_name=data.loc[data["Salary"]==highest_salary,"Name"].values[0]
lowest_name=data.loc[data["Salary"] == lowest_salary,"Name"].values[0]
print(range_salary)


# Question 4: Add a new column called 'Experience_Level' that categorizes employees based on their years of experience:
# Junior: 0–4 years
# Mid: 5–7 years
# Senior: 8+ years
def cal(Years_of_Experience ):
    if Years_of_Experience <=4:
        return "junior"
    elif Years_of_Experience >=5 and Years_of_Experience <=7:
        return "mid"
    else:
        return "senior"
data['Experience_Level']=data["Years_of_Experience"].apply(cal)
print(data)

#creating a new column called salary category 
def salary_range(Salary):
    if Salary < 50000:
        return "lower"
    elif Salary>50000 and Salary<=75000:
        return "Medium"
    else:
        return "high"
data["Salary_Category"]=data["Salary"].apply(salary_range)
print(data)

#  Question 6: Count the number of employees in each Department.
count=data.Department.value_counts()
print(count)

# Question 7: Find the total salary expense for each Department.
# Your task:

# Group the data by the Department column.
# Calculate the total salary paid to employees in each department.
# Print the result.

total_salary=data.groupby("Department")["Salary"].sum()
print(total_salary)

# Question 8: Find the average Years_of_Experience for each Department.
# Your task:

# Group the data by the Department column.
# Calculate the average Years_of_Experience for employees in each department.
# Print the result.

avg_year=data.groupby("Department")["Years_of_Experience"].mean()
print(avg_year)

# Question 9: Find the highest salary and its corresponding employee name for each Department.
# Your task:

# Group the data by the Department column.
# For each department, find the highest salary and the name of the employee earning that salary.
# Print the result.

sal=data.groupby("Department").agg({"Salary":"max","Name":"first"})

print(sal)

