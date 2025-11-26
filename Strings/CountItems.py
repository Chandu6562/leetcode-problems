# Count Items Matching a Rule
'''You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item.
You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule.'''


# items = [["phone","blue","pixel"],["computer","silver","phone"]             ,["phone","gold","iphone"]]
# ruleKey = "type"
# ruleValue = "phone"
# matching=0
# for i in range(len(items)):
#     if ruleKey == 'type':
#         if items[i][0]==ruleValue:
#             matching+=1
#     elif ruleKey == 'color':
#         if items[i][1]==ruleValue:
#             matching+=1
#     elif ruleKey == 'name':
#         if items[i][2]==ruleValue:
#             matching+=1
# print(matching)


items = [["phone","blue","pixel"],["computer","silver","phone"]             ,["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"

keyIndex = {"type": 0, "color": 1, "name": 2}[ruleKey]
count = 0
for item in items:
    if item[keyIndex] == ruleValue:
        count += 1
print(count)