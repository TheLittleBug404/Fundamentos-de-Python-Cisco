#introduciendo datos por teclado
numero1:int = int(input("Introduzca primer numero: "))
numero2:int = int(input("Introduzca segundo numero: "))
texto:str = input("Introduzca el texto ")
producto = numero1 * numero2
if(producto <= 1000):
    print(producto)
else:
    suma = numero1 + numero2
    print(suma)
print(texto)