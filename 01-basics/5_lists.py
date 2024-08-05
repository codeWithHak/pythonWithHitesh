my_friends = ["Huzaifa","Khizar","Abdullah","Hamza"]

#print(my_friends)
nums = [0,1,2,3,4,5,6,7,8,9]

#print(my_friends[1:2])
#print(my_friends)
#print(nums[0:9:2])
#print(my_friends[:2])
#print(my_friends[0:5:2])

#for friend in my_friends:
 #   print(friend,end= " - ")

#if "Huzafa" in my_friends:
 #   print("Available")

#else:
 #   print("Unavailable!!!")

my_friends_copy = my_friends.copy()

my_friends_copy.append("Helllowww")

#print(my_friends_copy)
#print(my_friends)

"""my_friends.remove("Hamza")
print(my_friends)
my_friends.insert(0,"Hamza")
print(my_friends)"""


"""table_of_z = [x for x in range(1,11) ]
table_of_y = [y for y in range(2,11)]
for x in table_of_z:
     print(x,y)"""

counted_two = [x*2 for x in range(1,11)]
for count in counted_two:
    one_to_ten = int(count/2)
    print(f"2 x {one_to_ten} = {count}") 
