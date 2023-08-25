"""/*
 * Crea una función que sea capaz de leer el número representado por el ábaco.
 * - El ábaco se representa por un array con 7 elementos.
 * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar
 *   operaciones) para las cuentas y una secuencia de "---" para el alambre.
 * - El primer elemento del array representa los millones, y el último las unidades.
 * - El número en cada elemento se representa por las cuentas que están a
 *   la izquierda del alambre.
 *
 * Ejemplo de array y resultado:
 * ["O---OOOOOOOO",
 *  "OOO---OOOOOO",
 *  "---OOOOOOOOO",
 *  "OO---OOOOOOO",
 *  "OOOOOOO---OO",
 *  "OOOOOOOOO---",
 *  "---OOOOOOOOO"]
 *  
 *  Resultado: 1.302.790
 */"""


ent = ["O---OOOOOOOO",
  "OOO---OOOOOO",
  "---OOOOOOOOO",
  "OO---OOOOOOO",
  "OOOOOOO---OO",
  "OOOOOOOOO---",
  "---OOOOOOOOO"]
def contar(ent):
    if len(ent)!=7:
        print("el abaco debe tener 7 lineas")
    else:    
     rows=[]
     for row in ent:
      if len(row) != 12 or row.count("O")!= 9 or row.count("-")!= 3 :
        print("las lineas del abaco tienen 9 cuentas (O) y tres alambres (-)")
        rows=[]
        break  
      else:     
        #ent.rsplit("-")
        #print(row[0])
        if row[0] == "-":
            rows.append(0)            
        else:
            rt=row.rsplit("-")
            rows.append(len(rt[0]))
        #print(rows)
    num="".join(str(e) for e in rows)
    #print(num)
    return num
    #print(rows)

rows=contar(ent)
#print("fin del programa")
print(rows)