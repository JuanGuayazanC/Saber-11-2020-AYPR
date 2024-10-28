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
        print("1. Cantidad de estudiantes hombres y cantidad de estudiantes mujeres total")
        print("2. Listado de países ordenado alfabéticamente con cantidad total de estudiantes de cada pais que presentaron la prueba.")
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
        elif o == 4:
            libros(datos)
        elif o == 5:
            puntaje(datos)
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
    paireal = pai[1:]
    paiord = partir_dos(paireal)
    paisinrep = [paiord[0]]
    for i in range(len(paiord)-1):
        if paiord[i] != paiord[i+1]:
            paisinrep.append(paiord[i+1])
    num = []
    n = 1
    for k in range(len(paireal)-1):
        if paiord[k] == paiord[k+1]:
            n = n + 1
        else:
            num.append(n)
            n = 1
    num.append(n)
    for s in range(len(num)):
        print(paisinrep[s] , num[s])
def nacionalidad(datos):
    """ Determina listado a partir de una nacionalidad dada
    (list) -> list
    """
    nac = input("Ingrese el país de origen (SIN TILDES): ")
    pun = [sub[59] for sub in datos if sub[1] == nac]
    punord = partir_dos(pun)
    print(punord)
def libros(datos):
    """Listado ordenado de cantidad de estudiantes agrupados por cantidad de libros en casa
    (list)  -> list
    """
    lib = [fila[28] for fila in datos]
    libreal = lib[1:]
    libord = partir_dos(libreal)
    libsinrep = [libord[0]]
    for i in range(len(libord)-1):
        if libord[i] != libord[i+1]:
            libsinrep.append(libord[i+1])
    num = []
    n = 1
    for k in range(len(libreal)-1):
        if libord[k] == libord[k+1]:
            n = n + 1
        else:
            num.append(n)
            n = 1
    num.append(n)
    for s in range(len(num)):
        print(libsinrep[s] , num[s])
def puntaje(datos):
    """ Listado de estudiantes ordenado numéricamente de menor a mayor por puntaje en lectura crítica de una ciudad en particular.
    """
    ciudad = input("Ingrese la ciudad (SIN TILDES): ")
    pun = [fila[59] for fila in datos if fila[1] == ciudad]
    punord = partir_dos(pun)
    print(punord)
def main():
    lista = lecach()
    tabla = matriz(lista)
    menu(tabla)

main()
