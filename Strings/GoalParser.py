# Goal Parser Interpretation
'''You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G",
"()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()"
as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.'''




# command = "G()()()()(al)"
# l=['G','()','(al)']
# li=['G','o','al']
# for i in range(len(l)):
#     if l[i] in command:
#         command=command.replace(l[i],li[i])
# print(command)


command = "G()()()()(al)"
command = command.replace("()", "o")
command = command.replace("(al)", "al")
print(command)


