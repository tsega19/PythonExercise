#------Python Exercise 1---------
# def FirstLast(numList):
#     print("Given List:", numList)
#     first_num = numList[0]
#     last_num = numList[-1]
#     if first_num == last_num:
#             return True
#     else:
#             return False
# x = [10, 23, 32, 10]
# print("Result is :", FirstLast(x))   
# y = [10,32, 43,10, 23]  
# print ("Result is :", FirstLast(y))

#-------Python Exercise 2 --------
#-- Cheking if the number is divisble by 5 or not
# number = int(input("Enter the number  :"))
# if number % 5 == 0:
#     print("The number is divisble by 5 :",number)
# else:
#     print("The Number is not divisble by 5")
#------Python Exercise 3 ---------
#-- Geting list number input from the user
# list_number = input("Enter the list of number")
# print("\n") 
# lists = list_number.split()
# print("List: ", lists)
# for i in range(len(lists)):
#    lists[i] = int(list_number[i])
#     # print("Sum = ", sum(lists))
# print(lists)
num = int(input("Enter a number greater than 1: "))

oper = input("Choose a math operation (+, -, *): ")
for i in range(1, num):
    if oper == '+':
        print(num, oper, i, '=', num + i)
    elif oper == '-':
        print(num, oper, i, '=', num - i)
    elif oper == '*':
        print(num, oper, i, '=', num * i)
    else:
        print('operator is not supported')
    