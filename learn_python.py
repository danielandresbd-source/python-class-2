# 1. Variables and Data Types
name = "Alice"
age = 30
height = 5.5
is_student = True  
print(f"Name: {name}, Age: {age}, Height: {height}, Is Student: {is_student}")

# 2. Control Structures
if age > 18:
    print("You are an adult.")
else:
    print("You are a minor.")
    
# 3. Loops
for i in range(5):
    print(f"Iteration {i}")
    
# 4. Functions
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))

# 5. Lists and Dictionaries
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
person = {"name": "Alice", "age": 30}
print(person["name"])  # Output: Alice

# 6. Iterating over Collections
for fruit in fruits:
    print(fruit)

for key, value in person.items():
    print(f"{key}: {value}")

for i in range(len(fruits)):
    print(f"Index: {i}, Fruit: {fruits[i]}")

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

for key in person:
    print(f"Key: {key}, Value: {person[key]}")


    
# 7. Classes and Objects (Instance of a class)
class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
    def greet(self, target):
        return f"Hello, my name is {self.name}, I'm a {self.job} and I am {self.age} years old. Nice to meet you {target.name}."

person1 = Person("Alice", 30, "teacher")
person2 = Person("Bob", 20, "student")

print(person1.greet(person2))