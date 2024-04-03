string=input("enter any string")
num=int(input("enter the num"))
if num < len(string):
    print(string[num:])
else:
    print("num must less than the length of the string")
