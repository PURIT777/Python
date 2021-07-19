print("Welcome Dear Coustmer, Pls Enter Your Cost")
print("price and Sell prise.....")
a=int(input("S.P.= "))
b=int(input("C.P.= "))
if (b<a):
    print("Congo! you have a profit of ", a-b)
elif(a<b):
    print("It's a Loss of ", b-a)
else:
    priint("Invalid entry")
print("Thanku to use our servise")
