working_hours = int(input("Enter the number of working hours: "))

required_hours = 100
normal_salary = 100.0
overtime_rate1 = 1.25
overtime_rate2 = 1.5
penalty_rate = 0.5

total_salary = 0.0

if working_hours > required_hours:
    overtime_hours = working_hours - required_hours
    if overtime_hours <= 30:
        total_salary = normal_salary + (overtime_hours * overtime_rate1)
    else:
        total_salary = normal_salary + (30 * overtime_rate1) + ((overtime_hours - 30) * overtime_rate2)
elif working_hours < required_hours:
    less_hours = required_hours - working_hours
    total_salary = normal_salary - (less_hours * penalty_rate)
else:
    total_salary = normal_salary

print("\n===============================")
print("Worker Report")
print(f"Working Hours: {working_hours} hours")
print(f"Total Salary: ${total_salary:.2f}")
print("===============================")
