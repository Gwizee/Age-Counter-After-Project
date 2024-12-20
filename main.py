try:
    current_year = int(input("Enter current year: "))
    born_year = int(input("Enter birth year: "))
    age = current_year - born_year
    print("Your age is: ",age)
except ValueError:
    print(ValueError)
except:
    print("Something went wrong")
else :
    print("No exception")
finally :
    print("Your age wil be outputed")