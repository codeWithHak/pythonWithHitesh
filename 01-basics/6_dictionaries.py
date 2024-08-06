my_info = {
    "name":"huzair",
    "age":18,
    "email":"huzairahmedkhan@gmail.com"
}
# print(my_info.get("namea")) -- None
# print(my_info["namea"]) -- error
# print(my_info["name"]) -- huzair
my_info["name"] = "khalil" 
# print(my_info)

# a method to print ke value pairs
"""for info in my_info:
    print(info,"=", my_info[info])"""

# another method to print key and values
"""for key,value in my_info.items():
    print (key,"=",value)     """

# adding new items in a dict

my_info["number"] = +923313391666
# print(my_info)

# removing items from a dict

"""my_info.popitem()
del my_info["email"]
del my_info["name"]
print(my_info)
my_info["password"] = 1234
print(my_info)"""


new_info = {
    "user":"hak",
    "role":"admin",
    "address":{
        "country":"pk",
        "city":"khi",
        "street":"phase 3"
    }
}
print(new_info["address"]["street"])

# printing key and value within a range using loop
squared = {x:x*x for x in range(2,11)}

#clearing the squared variable
squared.clear()
# print(squared)

my_keys = ["huzair","huzaifa","abdullah"]
my_value = "boy"
print(dict.fromkeys(my_value,my_keys))

