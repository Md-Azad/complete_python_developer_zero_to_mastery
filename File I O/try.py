# how can we read a file.

# with open('text.txt') as my_file:
#     print(my_file.read())

# to write some thing into our file

with open('text.txt', mode='a') as my_file:
    text=my_file.write(':)')
    print(my_file.read())

#print(5+4)




