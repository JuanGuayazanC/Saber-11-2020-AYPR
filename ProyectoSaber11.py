#Proyecto
def partir_dos(lista):
    """divide la lista en dos partes de manera recurrente
    (list) -> list
    """
    if len(lista) == 1:
        return lista
    else:
        mitad = len(lista) // 2
        izq = lista[:mitad]
        izq = partir_dos(izq)
        der = lista[mitad:]
        der = partir_dos(der)
        nueva = mezclar_ord(izq,der)
        return nueva
def mezclar_ord(izq, der):
    """ mezcla de manera ordenada dos listas ordenadas
    (list,list) -> list
    """
    i = 0
    j = 0
    long_i = len(izq)
    long_j = len(der)
    nueva = []
    while i < long_i and j < long_j:
        if izq[i] < der[j]:
            nueva.append(izq[i])
            i += 1
        else:
            nueva.append(der[j])
            j += 1
    if i < long_i:
        nueva += izq[i:]
    if j < long_j:
        nueva.extend(der[j:])
    return nueva
def lecach():
    """Hace lectura de palabras a partir de un archivo
    (none) -> list
    """
    datos = []
    nom_arc = input("Digite nombre de archivo ")
    arch = open(nom_arc,"r")
    line = arch.readline().strip('\n')
    while line!= "":
        datos.append(line)
        line = arch.readline().strip('\n')
    arch.close()
    return datos
def matriz(lisstr):
    """ Convierte una lista de strings en una matris (lista de listas)
    list -> list
    """
    ma = [s.split(',') for s in lisstr]
    return ma
def menu(datos):
    """ Dispone de elegir entre las opcones a realizar
    (list) -> list or str
    """
    o = 6
    while o != 0:
        print("Por favor elegir entre las siguientes opciones")
        print("0. Finalizar")
        print("1.  Cantidad de estudiantes hombres y cantidad de estudiantes mujeres total")
        print("2.Listado de países ordenado alfabéticamente con cantidad total de estudiantes de cada pais que presentaron la prueba.")
        print("3. Listado de estudiantes de una nacionalidad dada ordenado por puntaje total de mayor a menor")
        print("4. Listado ordenado de cantidad de estudiantes agrupados por cantidad de libros en casa")
        print("5. Listado de estudiantes ordenado numéricamente de menor a mayor por puntaje en lectura crítica de una ciudad en particular.")
        o = int(input("Ingrese el numero con la opcion "))
        if o == 1:
            mujeres, hombres = genero(datos)
            print("Cantidad hombres", hombres)
            print("Cantidad mujeres", mujeres)
        elif o == 2:
            paises(datos)
        elif o == 3:
            nacionalidad(datos)
        #elif o == 4:

        #elif o == 5:

    print("Gracias")
def genero(datos):
    """ Cantidad de estudiantes hombres y cantidad de estudiantes mujeres total
    (list) -> int, int
    """
    gen = [sub[2] for sub in datos]
    fem = 0
    mas = 0
    for i in range(len(gen)):
        if gen[i] == 'F':
            fem = fem + 1
        elif gen[i] == 'M':
            mas = mas + 1
    return fem, mas
def paises(datos):
    """ Listado de países ordenado alfabéticamente con cantidad total de estudiantes de cada país
    (list)
    """
    pai = [sub[1] for sub in datos]
    paisinrep = []
    for i in range(len(pai)-1):
        if pai[i] != pai[i+1]:
            paisinrep.append(pai[i+1])
    paisinrep = partir_dos(paisinrep)
    num = []
    for k in range(len(paisinrep)):
        n =0
        for l in range(len(pai)):
            if paisinrep[k] == pai[l]:
                n = n + 1
        num.append(n)
    for s in range(len(num)):
        print(paisinrep[s] , num[s])
        
    print(paisinrep)
    print(num)
def nacionalidad(datos):
    """ Determina listado a partir de una nacionalidad dada
    (list) -> list
    """
    pai = [sub[1] for sub in datos]
    nac = input("Ingrese el pais de origen (SIN TILDES)")
    si =[]
    for i in range(len(datos)):
        if nac == pai[i][1]:
            for a in range(0,80):
                list(si.append(pai[i][a]))

        
def main():
    lista = lecach()
    tabla = matriz(lista)
    menu(tabla)

main()
