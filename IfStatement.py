number = 5
if number==5:
    print("Number is 5")
else:
    print("Number is not 5")


if number:
    print("Number is defined and truthy")

text="Python"
if text:
    print("Text is defined and truthy")


text=""
if text:
    print("This will not execute")

a=1
b=3
x="bigger" if a>b else "smaller"
print(x)