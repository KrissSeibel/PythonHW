def my_func (**kwargs):
    user = kwargs.values()
    user = ", ".join(user)
    return user

print(my_func(name=input("Enter name: "), surname=input("Enter surname: "), year=input("Enter birth year: "),
        city=input("Enter city: "), email=input("Enter email: "), phone_number=input("Enter phone number: ")))

