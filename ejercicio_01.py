def OrdenarLista(lista):
    """Función que recibe una lista de números
    Parámetros: recibir numeros enteros y escribir otro fichero
    en formato txt. Donde la lista ordenada contiene solo numeros pares
    Salida: sera ejecutado las dps funciones
    """
    numero = len (lista)
    lista =[]
    with open('ListaOrdenada.txt', 'w') as file:
        file.write('')
    for numero in range(numero):
        lista.append(OrdenarLista(lista[numero]))
        lista.sort()
        return lista
def NumeroPar():