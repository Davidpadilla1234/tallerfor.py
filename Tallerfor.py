archivo  =  abrir =( 'paises.txt' , 'r' )
#imprime la posicion de colombia
"""
c=0
lista=[]
para i en archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1
  if(a=="Colombia: Bogotá \n "):
    descanso
  lista=[]   
imprimir (c)
"""
#Imprima todos los paises
"""
lista=[]
para i en archivo:
  a=i.index(":")
  para r en el rango (0,a):
    lista.append(i[r])
  a="".join(lista)
  imprimir (a)
  lista=[]
"""
#Imprima todas las Capitales
"""
lista=[]
para i en archivo:
  a=i.index(":")
  para r en el rango (a+2, len (i)):
    lista.append(i[r])
  a="".join(lista)
  imprimir (a)
  lista=[]
"""  
#Imprimir todos los paises que iniciaron con la letra C
"""
lista=[]
paises=[]
para i en archivo:
  a=i.index(":")
  para r en el rango (0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
para i en paises:
  si(i[0]=="C"):
    imprimir (yo)
"""  
#imprime todas las capitales que iniciaron con la leta B
"""
lista=[]
ciudad=[]
para i en archivo:
  a=i.index(":")
  para r en el rango (a+2, len (i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
para yo en ciudad:
  si(i[0]=="B"):
    imprimir (yo)  
"""
#Cuente e imprima cuantas ciudades inician con la latra M
"""
lista=[]
ciudad=[]
para i en archivo:
  a=i.index(":")
  para r en el rango (a+2, len (i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
para yo en ciudad:
  si(i[0]=="M"):
    imprimir (yo)
    lista.append(i)
imprimir (len (lista))
"""  
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
"""
lista=[]
pais_y_capital=[]
para i en archivo:
  a=i.index(":")
  para r en el rango (0,a):
    lista.append(i[r])
  a="".join(lista)
  pais_y_capital.append(a)
  lista=[]
para i en pais_y_capital:
  si(i[0]=="U"):
    imprimir (yo)
lista=[]
pais_y_capital=[]  
para i en archivo:
    b=i.index(":")
    para r en rango(b+2,len(i)):
      lista.append(i[r])
      b="".join(lista)
      pais_y_capital.append(b)
lista=[]
para i en pais_y_capital:
  si(i[0]=="U"):
   imprimir (yo)
"""
#Cuente e imprima cuantos paises que hay en el archivo
"""
c=0
lista=[]
para i en archivo:
  lista.append(i)
  a="".join(lista)
  c=c+1
imprimir (len (lista))
"""
#Busque e imprima la ciudad de Singapur
"""
palabra="Singapur: Singapur"
b=palabra.index(":")
tamaño=len(palabras)
lista=[]
para i en rango(b+1,tamaño):
    lista.append(palabra[i])
unir="".join(lista)
imprimir (unir)
"""
#Busque e imprima el pais de Venezuela y su capital
"""
palabra="Venezuela: Caracas"
b=palabra.index(":")
tamaño=len(palabras)
lista=[]
para i en el rango (0,18):
    lista.append(palabra[i])
unir="".join(lista)
imprimir (unir)
"""
#Cuente e imprima las ciudades que su pais inicia con la letra E
"""
lista=[]
paises=[]
para i en archivo:
  a=i.index(":")
  para r en el rango (0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
para i en paises:
  si(i[0]=="E"):
   imprimir (yo)
   lista.append(i)
imprimir (len (lista))
"""
#Buesque e imprima la Capiltal de Colombia
"""
palabra="Colombia: Bogota"
b=palabra.index(":")
tamaño=len(palabras)
lista=[]
para i en rango(b+1,tamaño):
    lista.append(palabra[i])
unir="".join(lista)
imprimir (unir)
"""
#imprime la posicion del pais de Uganda
"""
c=0
lista=[]
para i en archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1
  if(a=="Uganda: Kampala \n "):
    descanso
  lista=[]   
imprimir (c)
"""
#imprime la posicion del pais de mexico
"""
c=0
lista=[]
para i en archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1
  if(a=="México: Ciudad de México \n "):
    descanso
  lista=[]   
imprimir (c)
"""
"""
El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Use un For para cambiar ese Dato
"""
"""
lista=[]
para pais_y_capital en archivo:
pais_y_capital.remove=("Madagascar: rey julien")
lista.insert=(149,"Madagascar: Antananarivo")
imprimir(pais_y_capital)
"""
#Agregue un pais que no este en la lista
"""
lista=[]
pais_y_capital=[]
para pais_y_capital en archivo:
    lista.insert(149,"Catar:Doha")
    imprimir(pais_y_capital)
"""
"""
archivo.cerrar()
"""