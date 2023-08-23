first_number=int(input("Enter the first number:\n"))
second_number=int(input("Enter the second number:\n"))
def evens():
    first_number = 0
    while(first_number < second_number):
        first_number= first_number+ 2
        print (first_number)
        
print (evens())
