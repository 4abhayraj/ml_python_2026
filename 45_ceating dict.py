a={"x":1, "b":2}
print(a)

user_info=dict(name= "abhay", age=25, country="India")
print(user_info)



#Accessing Dictionary item []
d={"name":"Abhay", "age":"20"}
print(d["name"])

print(d.get("age","not found"))


#adding &updating Dictionary items
d={"name":"Abhay"}
d["age"]=20
print(d)
d["name"]="Sachin"
print(d)

print("\n\n")
#Removing Dictionary items
#del: removes an  item using its key
d={"a":1, "b":2}
del d["a"]
print(d)

print("\n")
#pop: removes the items with the given key and return its value.
d={"a":1, "b":2}
val=d.pop("a")
print(val) #returns deleted item
print(d)

print("\n")
#popitem(): removes and return the last  inserted key value pair
d={"a":1,"b":2}
print(d.popitem())


#clear(): removes all items from the dictionary

d={"a":1,"b":2}

d.clear()
print(d)
