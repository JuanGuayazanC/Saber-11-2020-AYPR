
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


def resultados(lista):
    ordenadas=[]
    primera=lista[0]
    for i in range(len(lista)):
        for i in lista:
            if i<primera:
                primera=i
        ordenadas.append(primera)
        print(ordenadas)


def numero(lista):
    """Determina la cantidad total de estudiantes de cada pais
    """
    num=[fila[1] for fila in lista]

def paises(datos):
    """ Listado de países ordenado alfabéticamente con cantidad total de estudiantes de cada país
    (list)
    """
    pai = [sub[1] for sub in datos]
    pai = partir_dos(pai)
    print(pai)
    paisinrep = []
    for i in range(len(pai)-1):
        if pai[i] != pai[i+1]:
            paisinrep.append(pai[i+1])
    num = []
    n =0
    for k in range(len(paisinrep)):
        if pai[k] == pai[k+1]:
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
        if nac == pai[i]:
            si.append(nac[i])



def bbinaria(lista,valor):
    izquierda=0
    derecha=len(lista)-1

    while izquierda <= derecha:
        medio=(izquierda+derecha)//2
        valor_medio= lista[medio]

        if valor_medio==valor:
            return medio
        elif valor_medio < valor:
            izquierda=medio+1
        else:
            derecha=medio-1
    return -1

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

def libros(lista):
    lib= [fila[28] for fila in lista]
    return lib

def orlib(lista):
    lis=[]
    for i in range(len(lista)):
        if lis[i]=="0 A 10 LIBROS":
            lis.append(i)
        if lis[i]=="11 A 25 LIBROS":
            lis.append(i)
        if lis[i]=="26 A 100 LIBROS":
            lis.append(i)
        
def bbin(lista,valor):
    izquierda=0
    derecha=len(lista)-1

    while izquierda <= derecha:
        medio=(izquierda+derecha)//2
        valor_medio= lista[medio]

        if valor_medio==valor:
            return medio
        elif valor_medio < valor:
            izquierda=medio+1
        else:
            derecha=medio-1
    return -1

def leccrit(lista):
    n=[fila[59] for fila in lista]
    return n

    
def main():
    lista=lecach()
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
            s=partir_dos(lista)
            print(s)
        elif o==3:
            val=input("Seleccione un pais: ")
            n=bbinaria(lista,val)
            d=puntaje(n)
            z=ordenar(d)
            print(z)

        elif o==4:
           a=libros(lista)
           b=orlib(lista)
           print(b)
           
        elif o==5:
            valor=input("Escriba la ciudad de la cual se desea saber la informacion")
            q=leccrit(lista)
            p=bbin(q,valor)
            
main()       
            
    
        
    


