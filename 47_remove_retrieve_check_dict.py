car={
    "brand": "Toyota",
    "model": "Camery",
    "year": "2022",
    "color": "blue"
}

print(car)
del_item=car.pop("brand") #delete specific key from dict
print(car)


for i in car.items(): #retrive all key value pairs
    print(i)

#check whether a given key exists
exists_key="model"
exists= exists_key in car

print(f"{exists_key} exists in car?: {exists}")







"""car= {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022,
    "color": "blue"
}

#remove a specific key and grab its value safely
removed_color =car.pop("color",None)

#Check whether a given key exists
key_to_check = "model"
exists = key_to_check in car

#3. Retrieve all key-value pairs remaining
all_pairs =car.items()

print(f"Removed color: {removed_color}")
print(f"Does '{key_to_check}' exists?: {exists}")
print("Remaining key-value pairs:", list(all_pairs))"""