person1 = {"name": "Alice", "age": 25, "city": "New York"}
person2 = {"name": "Alice", "age": 10,}


if len(person1) > 0:
    print("Словник не порожній")
else:
    print("Словник порожній")
if len(person2) > 0:
    print("Словник не порожній")
else:
    print("Словник порожній")

person = {"name": "John", "age": 30, "city": "New York"}
print(person)

person2 = dict(name="John", age=30, city="New York")
print(person2)

name = "John"
age = 30
city = "New York"
person3 = {"name": name, "age": age, "city": city}
print(person3)
person4 = dict(name = "John", age = 30, city = "New York")
print(person4)

person = {
    "name":"John",
    "age": 30,
     "city":"New York",
     "subjects": ["Math", "Programming", "Physics"]
}