#1
import random


def calculations(a, b):
    sum1= a + b
    sum2= a - b
    return(sum1, sum2)
num1=(int(input("Num1:")))
num2=(int(input("Num2:")))
print(calculations(num1, num2), "\n")





#2
l=[]
for i in range(5):
    l.append(random.randint(1, 5))
print(l)
def ListSum(l):
    sum=0
    for i in l:
        sum+=i
    return sum
print(ListSum(l), "\n")




#3
def func(*args):
    a=0
    for i in args:
        print(i,"-",a)
        a+=1
func(3, 4, ":)", 5)
print("\n")




#4
def ShowEmployee(name, salary):
    return print("Employee name:", name, "\n", "Employee salary:", salary)
name= input("Enter employee name:")
salary=(input("Enter employee salary:"))
if salary=='':
    ShowEmployee(name, salary=9000)
print(ShowEmployee(name, salary))
