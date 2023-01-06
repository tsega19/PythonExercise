a = "Hello, Wld!"
print(a.upper())
#-------Python exercise 1:-----------
def Mul_Sum(num1, num2):
    p = num1 * num2
    if p < 1000:
      return p
    else: 
      return num1 + num2 
result = Mul_Sum(20, 30)
print("The result is", result)      
#------python Exercise 2:-----------
previous_num = 0
for i in range(1, 11):
 	x_sum = previous_num + i
 	print("Current Number ", i, "previous number ", previous_num, "sum: ", x_sum)
 	previous_num = i
# -----------#python Exercise 3:-------
name = input("enter Employ name: ")
salary =int(input("Enter salary: "))
company = input("Enter company name: ")
print("\n")
print("printing Employee")
print("Name", "salary", "company")
print(type(name), name , type(salary),salary, type(company), company)
#--------python Exercise 4-------------
# list to store multi line input
# press enter two times to exit
data = []
print("Tell me about yourself")
while True:
      line = input()
      if line:
            data.append(line)
      else:
            break
finalText = '\n'.join(data)
print(finalText)
#----python Exercise 5--------
word = input("Enter Word")
print("Orginal String: ", word)
size = len (word)
print ("Printing only even index chars")
for i in range (0, size-1, 2):
    print(word[i])
  #-----python Exercise 5--------
word = input("Enter the word")
print("Orginal Word :", word)
size = len(word)
for i in range(1, size):
 print(word[i])