# #general way of opening the file
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
#
# #we need to close the file after the usage it uses resources of the computer
# file.close()



#but generally we forget to close , so we can use with keyword so that the file gets closed automatically after the usage

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)




#write in a file
# by default it stays in read only mode
#to write something we need to change the mode to "w"

# with open("my_file.txt",mode="w") as file:
#     file.write("new text")
# this replaces the previous text with this new text


# if we dont want to replace and just want to append the text we can change the mode to "a"
with open("my_file.txt",mode="a") as file:
    file.write("\nnew text")


#if we try to write something with "w" mode in a file that doesnt exist then python creates a new file for us
with open("new_file.txt",mode="w") as file:
     file.write("new text")


