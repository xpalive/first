# This is a sample Python script.
import sys


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def boyan_hi(name):
    age = 10
    grade = ['5(2)班']
    print(grade[0])
    grade1 = grade
    grade[0] = '4(2)班'
    print(grade[0])
    print(grade1[0])
    # teacher = '马莲莲'
    # print(f'Hi, My name is {name}，I am {age} years old, {grade}.')

def boyan_hi_1(name):
    print(f'Hi, {name}')
    age = 10
    grade = '5(2)班'
    print(grade)
    grade1 = grade
    grade = '4(2)班'
    print(grade)
    print(grade1)
    # teacher = '马莲莲'
    # print(f'Hi, My name is {name}，I am {age} years old, {grade}.')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    name = 'Boyan'
    boyan_hi_1(name)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
