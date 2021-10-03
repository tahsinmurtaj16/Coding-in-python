class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')
# create a new object of Person Class
harry = Person()

# Output: 10
print(Person.age)

# Output: <function Person.greet>
print(Person.greet)

# Output:
print(harry.greet)

# Output: "This is a person class"
print(Person.__doc__)

# true call to greet from harry
harry.greet()