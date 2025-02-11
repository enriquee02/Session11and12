d = {} #empty dictionary
print(d)


eng_to_spa = {"one": "uno","two": "dos","three": "tres"}
print(eng_to_spa)
print(eng_to_spa["one"])
eng_to_spa["tree"] = "arbol"
print(eng_to_spa["tree"])
eng_to_spa.update({"yes":"si", "no": "no"})
print(eng_to_spa)

del eng_to_spa["yes"]
print(eng_to_spa)

print("these are the spanish words that I know")
for key in eng_to_spa:
    print(f""
          f"{eng_to_spa[key]} means {key}")

print(dir(eng_to_spa))
#'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
#clearing the dictionary: eng_to_spa.clear()

eng_to_spa2 = eng_to_spa.copy()
eng_to_spa.clear()
print(eng_to_spa)

new_d = eng_to_spa2.fromkeys(eng_to_spa2, "YES")
print(new_d)

#get is one of the most useful
#if "car" in eng_to_spa2:
#   print(f"you say car as {eng_to_spa["car"]}")

print(f"car in spanish is {eng_to_spa2.get('car', 'unkown')}")
print(list(eng_to_spa2.items()))

print(eng_to_spa2.popitem())
print(eng_to_spa2.pop("one"))
eng_to_spa2.setdefault('red','rojo')
print(eng_to_spa2)
