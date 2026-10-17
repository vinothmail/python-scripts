"""
no = int(input("Enter a number to generate table: "))
print(f"\n{no} Table")
print("----------")
for i in range(1, 13):
    print(f"{i} x {no} = {no * i}")
       
numb = int(input("Enter no.till to generate table: "))
print("----------")
l=0
j=0
k=1
for k in range (1, numb+1):
    print("------------")
    for j in range(1, 13):
       # j=1
        l=k
        print(f"{j} x {l} = {j *l}")
        j+=j
"""
numb = int(input("Enter no.till to generate table: "))
for m in range(1, 13):
    for h in range(1, numb+1):
        #print(f"{m} x {h} = {m*h}")
        print(f"{m} x {h} = {m*h}", end="\t")
    print()