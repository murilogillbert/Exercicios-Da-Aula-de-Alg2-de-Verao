def fatorialRecursivo(n):
    if n == 0 or n == 1:
        print(f"Fatorial de {n}: {n}")
        return 1
    else:
        fat =  n*fatorialRecursivo(n-1)
        print(f"Fatorial de {n}: {fat}") 
        return fat
print(fatorialRecursivo(5))
def fibonnacciRecursivo(n):
    if n>1:
        return fibonnacciRecursivo(n-1) + fibonnacciRecursivo(n-2)  
    elif n == 1:
        return n + fibonnacciRecursivo(n-1)
    else:
        return 0
print(fibonnacciRecursivo(10))
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

def listaExponenciada(lista,tamanhoLista):
    if tamanhoLista<1:
        return []
    else:
        #listaTemporaria = [lista[tamanhoLista-1]]*tamanhoLista
        return listaExponenciada(lista,tamanhoLista-1) + [lista[tamanhoLista-1]]*tamanhoLista

def listaExponenciada2(lista,tamanhoLista-1):
    if tamanhoLista<len(lista):
        return listaExponenciada(lista,tamanhoLista-1) + [lista[tamanhoLista-(tamanhoLista-1)]]*tamanhoLista
    return []

print(listaExponenciada([1,2,3,4],4))