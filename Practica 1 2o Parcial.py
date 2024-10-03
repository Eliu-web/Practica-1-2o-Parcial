#Punto 1
print (" ")
precios = [43, 57, 92, 20, 37, 5, 9]
print (precios)
print ("El mayor es", precios[2])
print ("El menor es", precios[5])
print (" ")

#Punto 2
materias = ["Humanidades", "Ingles", "Ecosistemas", "Metodologias", "Frameworks", "Socioemocional", "Lengua y comunicacion", "Matematicas" ]
print (materias)
print (" ")

#Punto 3 
print ("Estoy cursando", materias[0])
print ("Estoy cursando", materias[1])
print ("Estoy cursando", materias[2])
print ("Estoy cursando", materias[3])
print ("Estoy cursando", materias[4])
print ("Estoy cursando", materias[5])
print ("Estoy cursando", materias[6])
print ("Estoy cursando", materias[7])
print (" ")

#Punto 4 
calificacion = [8,6,9,10,5,7,7,8]
print (calificacion)
print (" ")
print ("En", materias[0],  "has obtenido", calificacion[0])
print ("En", materias[1],  "has obtenido", calificacion[1])
print ("En", materias[2],  "has obtenido", calificacion[2])
print ("En", materias[3],  "has obtenido", calificacion[3])
print ("En", materias[4],  "has obtenido", calificacion[4])
print ("En", materias[5],  "has obtenido", calificacion[5])
print ("En", materias[6],  "has obtenido", calificacion[6])
print ("En", materias[7],  "has obtenido", calificacion[7])
print (" ")

#Punto 5

num1_loteria = (input("Cuales es el primer numero triunfador de la lotería: "))
num2_loteria = (input("Cuales es el sgundo numero triunfador de la lotería: "))
num3_loteria = (input("Cuales es el tercer numero triunfador de la lotería: "))

num_loteria = [num1_loteria, num2_loteria, num3_loteria]
num_loteria.sort()

print(num_loteria)