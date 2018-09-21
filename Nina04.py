# Informar 3 números

n1= float(input("digite o número: "))
n2= float(input("digite o número: "))
n3= float(input("digite o número: "))

if n1>n2>n3:
    print("O maior número é", n1,"e o menor número é", n3)
if n1>n3>n2:
    print("O maior número é", n1,"e o menor número é", n2)
if n2>n1>n3:
    print("O maior número é", n2, "e o menor número é", n3)
if n2>n3>n1:
    print("O maior número é", n2, "e o menor número é", n1)
if n3>n2>n1:
    print("O maior número é", n3, "e o menor número é", n1)
if n3>n1>n2:
    print("O maior número é", n3, "e o menor númenro é", n1)