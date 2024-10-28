#Proyecto de Saber 11
def lecach():
    """Hace lectura de palabras a partir de un archivo
    (none) -> list
    """
    datos = []
    nom_arc = input("Digite nombre de archivo ")
    arch = open(nom_arc,"r")
    line = arch.readline().strip('\n').split(",")
    while line!= "":
        datos.append(line)
        line = arch.readline().strip('\n').split(",")
    arch.close()
    return datos

def matriz(listss):
    num_filas = 50
    num_columnas = 81
    matriz = [listss[i * num_columnas:(i + 1) * num_columnas] for i in range(num_filas)]
    return matriz
    

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
    

def resultados(lista):
    ordenadas=[]
    primera=lista[0]
    for i in lista:
        if i<primera:
            primera=i
    ordenadas.append(primera)
    print(ordenadas)


def numero(lista):
    """Determina la cantidad total de estudiantes de cada pais
    """
    num=[fila[1] for fila in lista]
    
    


