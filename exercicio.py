def fatorialRecursivo(n):
    if n == 0 or n == 1:
        print(f"Fatorial de {n}: {n}")
        return 1
    else:
        fat =  n*fatorialRecursivo(n-1)
        print(f"Fatorial de {n}: {fat}") 
        return fat
def fibonnacciRecursivo(n):
    if n>1:
        return fibonnacciRecursivo(n-1) + fibonnacciRecursivo(n-2)  
    elif n == 1:
        return n + fibonnacciRecursivo(n-1)
    else:
        return 0
def diferencaPositivosNegativos(lista,tamanhoLista):
    def positivosMenosNegativos(lista,tamanhoLista):
        if tamanhoLista<1:
            return 0
        else:
            return lista[tamanhoLista-1] + positivosMenosNegativos(lista,tamanhoLista-1)
    return abs(positivosMenosNegativos(lista,tamanhoLista))
listaUser = [4,-5,9,-10]
tamanhoListaUser = len(listaUser)

print(diferencaPositivosNegativos(listaUser,tamanhoListaUser))
print(fatorialRecursivo(5))
print(fibonnacciRecursivo(10))
    