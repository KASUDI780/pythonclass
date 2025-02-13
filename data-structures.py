# list data structure
# it is ordered
# it is mutable
# it has index
fruits=["Mangoes","Banana","Oranges","Grapes"]
print(fruits)
fruits[1]="Grapes"
print(f"I love eating {fruits[0]}")
numbers=[1,3,5,0,1,4,2,5]
numbers.sort()
numbers.append("Pine apples")
numbers.pop(2)
numbers.remove(2)
numbers.reverse()
numbers.clear()
print(numbers)


# tuple data structure
# its ordered
# its immutable
# it has index

cars=("mercedes","Toyota","Mazda","Range rover","Honda")
nambari=(3,9,8,1,0,4,33,-73,-2)
print(cars)
print(f"Japan produces {(cars[1])} cars")
print(nambari)
print(sorted(nambari))

# set data structure
#not ordered
# not index
country={"Kenya","Uganda","Tanzania","Burundi","Dubai"}
print(country)
country.pop()
print(country)

# dictionary data structure
#key-value pair
student={"name":"Kasudi","age":"17","gender":"female","phone number":"+254784184065"}
print(f"My name is {student['name']} and am {student["age"]}")
print(f"My gender is {student['gender']} and my phone number is {student['phone number']}")
