flag=True
numero=0
lista_numeros=[]
while flag:
    numero=int(input("Ingrese un número,\nSi ingresa el 0, el programa se detendrá: "))   
    if numero == 0:
        flag=False
    else:
        lista_numeros.append(numero);
lista_numeros.sort();
print(lista_numeros)
print("la lista tiene largo: ",len(lista_numeros))
print("la suma de la lista es: ",sum(lista_numeros))
cantidad_elementos=len(lista_numeros)
suma_lista=sum(lista_numeros)
promedio=suma_lista/cantidad_elementos
print("el promedio de la lista es:",promedio)