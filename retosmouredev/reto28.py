"""/*
 * Crea una función que reciba una expresión matemática (String)
 * y compruebe si es correcta. Retornará true o false.
 * - Para que una expresión matemática sea correcta debe poseer
 *   un número, una operación y otro número separados por espacios.
 *   Tantos números y operaciones como queramos.
 * - Números positivos, negativos, enteros o decimales.
 * - Operaciones soportadas: + - * / % 
 *
 * Ejemplos:
 * "5 + 6 / 7 - 4" -> true
 * "5 a 6" -> false
 */"""
def calcula(exp):
    partes=exp.split(" ")
    while partes.count("*")>0:
        pos=partes.index("*")
        a=int(partes[pos-1])
        b=int(partes[pos+1])
        sol=a * b
        partes.remove(partes[pos-1])
        partes.remove(partes[pos-1])
        partes.remove(partes[pos-1])
        partes.insert(pos-1,sol)
    while partes.count("/")>0:
        pos=partes.index("/")
        a=int(partes[pos-1])
        b=int(partes[pos+1])
        sol=a / b
        partes.remove(partes[pos-1])
        partes.remove(partes[pos-1])
        partes.remove(partes[pos-1])
        partes.insert(pos-1,sol)
    while partes.count("+")>0:
        pos=partes.index("+")
        a=int(partes[pos-1])
        b=int(partes[pos+1])
        sol=a + b
        partes.remove(partes[pos-1])
        partes.remove(partes[pos-1])
        partes.remove(partes[pos-1])
        partes.insert(pos-1,sol)
    while partes.count("-")>0:
        #if partes.index("-",1)
        pos=partes.index("-")
        a=int(partes[pos-1])
        b=int(partes[pos+1])
        sol=a - b
        partes.remove(partes[pos-1])
        partes.remove(partes[pos-1])
        partes.remove(partes[pos-1])
        partes.insert(pos-1,sol)    

    print(partes)
    """ print(partes.count("/"))
    print(partes.count("-"))
    print(partes.count("+"))
    print(partes.find("+"))"""
    #partes.remove(partes[2])
    # insert (i,x)
    # index(X)    

    """print(partes)"""
calcula("5 + 6 / 7 - 4")
