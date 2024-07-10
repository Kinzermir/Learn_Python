# name : str = input("what is your name? : \t")
# print(type (name))
# print(f'Welcome dear use {name}')

#  from this we can get input form console so we can get data by using argv from user.
import sys    # Import the sys module to access command-line arguments
print("line1")
print("line2")
print("All arguments ", sys.argv)
print(type(sys.argv))  # iterative data type of argv is list[str] and in list we have strings
# for run, open terminal and write python class.py to go to class.py
# then write 1 2 3 
# example PS C:\Users\Dell1\piaic\Learn_Python\CLass_09> python class.py 1 2 3 
# result :- line1
# line2
# ['class.py', '1', '2', '3', '4', '4']
# <class 'list'>