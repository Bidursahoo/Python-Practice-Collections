def print_salary(salary, age):
    time = int(input("Enter the time of service "))
    try:
        fsal = (salary * age) / time
        return fsal;
    except ZeroDivisionError:
        print("Time cannot be zero ")
    except:
        print("Opps error occured ")


age = int(input("Enter your age "))
salary = int(input("enter your salary "))
print(print_salary(salary, age))
