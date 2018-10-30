import time
from sys import exit

response = ["yes","Yes"]

print("*********************")
print("REPORT CARD GENERATOR")
print("*********************")
name = input("Name:")
cat1 = int(input("CAT 1:"))
cat2 = int(input("CAT 2:"))
cat3 = int(input("CAT 3:"))

assignment1 = int(input("Assignment 1:"))
assignment2 = int(input("Assignment 2:"))

exam = int(input("Exam:"))

total  = int(cat1+cat2+cat3+assignment1+assignment2+exam)

if total>80:
    print (name,"your total is:",total)
    print("Grade A")
    
elif total>=70 and total <80:
    print (name,"your total is:",total)
    print("Grade B")
    
    
elif total >=60 and total <70:
    print (name,"your total is:",total)
    print("Grade c")
    
elif total >=50 and total <60:
    print (name,"your total is:",total)
    print("Grade D") 
    
elif total<40:
    print (name,"your total is:",total)
    print("Grade E")
    
else:
    print(name,"you have not done the exam")
    
print(name,"do you wish to create a text report card?")
print("1.Yes")
print("2.No")
option = input(">>")

if option == "1" or option == "Yes":
    y = input("Total marks:")
    z = input("Grade:")
    
    doc = open("reportcard.txt","w")
    doc.write("Name: "+name+"\n")
    doc.write("Marks:"+y+"\n")
    doc.write("Grade:"+z)
    time.sleep(3)
    
    print("The report card has been made...bye!")

    time.sleep(5)

elif option == "2" or option == "No":
    print("Bye")
    time.sleep(2)
    exit()
    
else:
    exit()
    