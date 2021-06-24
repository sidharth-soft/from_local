# Python program showing
# use of json package

import json

# {key:value mapping}
a ={"name":"John",
"age":31,
	"Salary":25000}

print(type(a))


# conversion to JSON done by dumps() function
b = json.dumps(a)

# printing the output
print(b)
print(type(b))




#to convert json data to dictionary

c=json.loads(b)
print(c)
print(type(c))
