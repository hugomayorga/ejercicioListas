numero_ingresado=int(input("Ingrese un número"))
resultado=0
x=range(1,11)
lista_tabla=[]
for n in x:
    resultado=n*numero_ingresado
    lista_tabla.append(resultado)
   # print(f"{n}*{numero_ingresado}={resultado}")
print("la tabla de multiplicar del número:",numero_ingresado)
print(lista_tabla)
