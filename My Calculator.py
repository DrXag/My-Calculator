#DrXag--------{Drax}

print("Welcome Here's my calculator \n Made by DraX")
print("Please choose your operator \n '+','-','*','/','%'")
n1=input()
print("Your first number!!")
n2=input()
print("Now \n Your Second number!")
n3=input()
if n1 == "+":
    print(int(n2)+int(n3))
elif n1 == "-":
    print(int(n2)-int(n3))
elif n1 == "*":
    print(int(n2)*int(n3))
elif n1 == "/":
    print(int(n2)/int(n3))
elif n1 == "%":
    print(int(n2)%int(n3))
print("Thanks ")