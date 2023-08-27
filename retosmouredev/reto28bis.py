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
def verifica(exp):
    partes=exp.split(" ")
    for parte in partes :
        if parte.isdigit()==False:
           if len(parte)!=1:
            return False
           else:            
              if parte[0]!="*" and parte[0]!="/" and parte[0]!="+" and parte[0]!="-":            
                return False
    return True

print(verifica("- 524 + 634 / 56 / 7 - 4"))
