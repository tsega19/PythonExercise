#------Python Exercise 1---------
def FirstLast(numList):
    print("Given List:", numList)
    first_num = numList[0]
    last_num = numList[-1]
    if first_num == last_num:
            return True
    else:
            return False
x = [10, 23, 32, 10]
print("Result is :", FirstLast(x))   
y = [10,32, 43,10, 23]  
print ("Result is :", FirstLast(y))
