#Autor: Itzel Yanabany Castro Becerril
def dividir():
    dividendo=int(input("Dividendo:"))
    divisor=int(input("Divisor: "))
    dividendo2=dividendo
    suma=0
    while dividendo>=divisor:
        dividendo=dividendo-divisor
        suma+= 1
    print(dividendo2,"/",divisor,"= ",suma,", ","sobran", dividendo)


def encontrarMayor():
    print("Teclea una serie de números para encontrar el mayor")
    numero = int(input("Teclea un número [-1 es para salir]:"))
    mayor = numero
    while numero != -1:
        if numero > mayor:
            mayor = numero

        numero = int(input("Teclea un número [-1 es para salir]:"))
    if mayor != -1:
        print("El mayor es:", mayor)
    else:
        print("No hay resultado")


def main():
   print("""Mision 7.Ciclo While.
   Autor: Itzel Yanabany Castro Becerril
   Matricula: A01747242
   1.Calcular divisiones
   2.Encontrar el Mayor
   3.Salir """)
   numero=int(input("Teclea tu opción: "))
   while numero>=1 and numero<=2:
       if numero==1:
           dividir()
           print("""Mision 7.Ciclo While.
              Autor: Itzel Yanabany Castro Becerril
              Matricula: A01747242
              1.Calcular divisiones
              2.Encontrar el Mayor
              3.Salir """)
           numero=int(input("Teclea tu opción: "))
       if numero==2:
            encontrarMayor()
            print("""Mision 7.Ciclo While.
               Autor: Itzel Yanabany Castro Becerril
               Matricula: A01747242
               1.Calcular divisiones
               2.Encontrar el Mayor
               3.Salir """)
            numero = int(input("Teclea tu opcioón: "))
   if numero==3:
        print("Gracias por usar este pograma, regresa pronto.")





main()