
#Proyecto de Saber 11
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

def matriz(listss):
    mt=[s.split(",") for s in listss]
    return mt
    

def genero(listado):
    gen=[fila[2] for fila in listado]
    muj=0
    hom=0
    for i in range(len(gen)):
        if gen[i]==F:
            muj=muj+1
        else:
            hom=hom+1
    return hom,muj




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
    pai = [sub[1] for sub in datos]
    nac = input("Ingrese el pais de origen (SIN TILDES)")
    si =[]
    for i in range(len(datos)):
        if nac == pai[i]:
            si.append(nac[i])





def nac(lista):
    pai = [sub[1] for sub in lista]
    return pai

def busqueda(lista,valor):
    arreglo=[]
    for i in range(len(lista)):
        if lista[i]==valor:
            arreglo.append(lista[i])

    return arreglo            

def puntaje(lista):
    lec = [fila[74] for fila in lista]
    return lec

def ordenar(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-1):
            if lista[j] < lista[j+1]:
                temp=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=temp
        return lista    




def cuatro(datos):
    """ Listado ordenado de cantidad de estudiantes agrupados por cantidad de libros en casa.
    """
    lib = [sub[28] for sub in datos]
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





def plec(lista):
    lectura = [columna[1] for columna in lista]
    return lectura


    
def main():
    m=lecach()
    lista=matriz(m)
    o=6
    while o!=0:
        print("Elija entre las siguientes opciones:")
        print("1.Cantidad de estudiantes hombres y cantidad de estudiantes mujeres")
        print("2. Listado de paises ordenados alfabeticamente con cantidad total de estudiantes en cada uno")
        print("3. Listado de estudiantes de una nacionalidad dada ordenado por puntaje total de cada estudiante")
        print("4. Listado ordenado de cantidad de estudiantes agrupados por cantidad de libros en casa")
        print("5. Listado de estudiantes ordenado numericamente de menor a mayor por puntaje en lectura critica de una ciudad en particular")
        print("0. Finalizar")
        o=int(input("Elige una opcion"))
        if o==1:
            hombres,mujeres=genero(lista)
            print("Cantidad hombres",hombres)
            print("Cantidad mujeres",mujeres)

        elif o==2:
            n=paises(lista)
            print(n)
        elif o==3:
            val=input("Seleccione un pais: ")
            d=nac(lista)
            n=busqueda(d,val)
            z=ordenar(n)
            print(n)

        elif o==4:
           a=cuatro(lista)
           print(a)
           
        elif o==5:
            valor=input("Escriba la ciudad de la cual se desea saber la informacion")
            w=plec(lista)
            q=busqueda(lista,valor)
            
            
main()       
            
    
        
    


