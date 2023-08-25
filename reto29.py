"""/*
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres. 
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 * 
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
 */"""

f1="Me llamo.Brais Moure" 
f2="Me llamo brais moure"

if len(f1)!=len(f2):
    print("las cadenas deben tener la misma longitud")
else:
    i=0
    r=[]
    for l in f1:
        if l!=f2[i]:
            r.append(f2[i])
        i=i+1
print(r)    




