# Convert Date to Binary

# date = "2080-02-29"
# a=date.split("-")
# l=[]
# for i in a:
#     l.append(bin(int(i))[2:])
# b="-".join(l)
# print(b)



date = "2080-02-29"
year,month,day=map(int,date.split("-"))
print(f'{bin(year)[2:]}-{bin(month)[2:]}-{bin(day)[2:]}')