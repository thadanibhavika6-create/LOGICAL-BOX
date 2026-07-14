print("Welcome to the Pattern Generator and Number Analyzer \n")
print("Select an option:")
print("1.Genrate a pattern")
print("2.Analyze a Range of Numbers")
print("3.Exit")
choice=int(input("enter your choice:"))
rows=int(input("Enter the number of rows for the pattern:"))
print("\nPattern: ")
for i in range(1,rows+1):
    for j in range(i):
        print("*",end="")
    print("")

print("\nSelect an option:") 
print("1.Genrate a pattern")
print("2.Analyze a Range of Numbers")
print("3.Exit")
choice=int(input("enter your choice:"))
start=int(input("\nenter the start of the range:"))
end=int(input("enter the end of the range:"))
total=0
for i in range(start,end+1):
    if i%2==0:
       print("Number",i ,"is even")
    else:
       print("number",i,"is odd")
    total=total+i
print("sum of all number is ",total)


print("\nSelect an option:")
print("1.Genrate a pattern")
print("2.Analyze a Range of Numbers")
print("3.Exit")
choice=int(input("enter your choice:"))
print("exiting the program.Goodbye")
