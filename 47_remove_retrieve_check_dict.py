car= {
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
print("Remaining key-value pairs:", list(all_pairs))