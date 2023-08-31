def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
print("Select an Operation -\n" \
      "1. Add\n" \
      "2. Subtract\n" \
      "3. Multiply\n" \
      "4. Divide\n"
      )
a=int(input("Select an Operation form 1, 2, 3, 4 :"))
x=int(input("Enter First Number: "))
y=int(input("Enter Second Number: "))

if a==1:
    print(x, "+",y, "=",add(x,y))

elif a==2:
    print(x, "-",y, "=",sub(x,y))

elif a == 3:
    print(x, "*", y, "=", mul(x, y))

elif a==4:
    print(x, "/",y, "=",div(x,y))

else:
    print("Invalid Input")