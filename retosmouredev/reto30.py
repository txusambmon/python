"""/*
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su
 * representación con letras.
 * - Debes buscar cuál era su correspondencia original.
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
 */"""
t9={
    1:["1"],
    2:["A","B","C","2"],
    3:["D","E","F","3"],
    4:["G","H","I","4"],
    5:["J","K","L","5"],
    6:["M","N","O","Ñ","6"],
    7:["P","Q","R","S","7"],
    8:["T","U","V","8"],
    9:["W","X","Y","9"],
    0:[" "]
} 
def convert(x):
    if  x=="":
        return ""
    y=x.rsplit("-")
    mensaje=""
    for letra in y:
        tecla=int(letra[0])
        pulsaciones=int(len(letra))-1        
        l=t9[tecla][pulsaciones]       
        mensaje= mensaje +l        
    return mensaje     
entrada= "8-8-99-88-7777-1-3333"
print (convert(entrada))