
def some_func(user_input, num):
    lst = []
    for i in user_input:
        lst.append(i/num)
    print(lst)


try:
    user_input = list(map(int,input("Enter a list of numbers").split(',')))
    num = int(input("Enter a number to divive the list with"))
    some_func(user_input, num)
except ZeroDivisionError:
    print("division by zero bruh")
except ValueError:
    print("Please enter a number to divide the list by")

