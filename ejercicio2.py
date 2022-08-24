print ("ingrese la cantidad de numeros a comparar")
lim=int (input())

print("ingrese los numeros")

n= int (input("ingrese numero: " ))

men= n
may= n

for i in range( 1 , lim):
  n = int (input ("ingrese numero: "))
  

if n < men :
  men= n 

else: 
 if n > may :
  may= n

print ("el numero menor es: ")
print ("el numero mayor es: ")