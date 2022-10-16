#ejercicio 1

numero1 = int(input("introduce un numero: "))
numero2 = int(input("introduce un numero: "))
numero3 = int(input("introduce un numero: "))

if numero1<numero2<numero3:
  print("orden ascendente")
else:
  print("no estan en orden ascensdente")
if numero1 == 0:
    print("error")
    
#ejercicio 2

numeros = [numero1, numero2, numero3]
if numero1<numero2<numero3:
  print("orden ascendente")
else:
  print("no estan en orden ascensdente")
if numero1 == 0:
    print("error")



#ejercicio 3

contador = 0
while True:
  if input("introduce un numero: ") == "a":
    contador = contador + 1
  elif input("introduce un numero: ") == ".":
    break

#ejercicio 4

colores = ["verde","rojo","morado"]
print(colores[0],len(colores[0]))
print(colores[1], len(colores[1]))
print(colores[2], len(colores[2]))
print(f"la palabra con mas caracteres es:", colores[2])


 