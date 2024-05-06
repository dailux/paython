#comenzzamos pidiendo al usuario que ingrese la cantidad de alumnos 
num_alumno=int(input("ingrese la cantidad e alumnos: "))
alumnos=[]
#pedir datos de caa alumno  
for i in range (num_alumno):
    print("\ningrese los datos del alumno",i+1)
    nombre=input("nombre del alumno:")
    edad=int(input("edad del alumno:"))
    alumnos.append({"nombre":nombre,"edad":edad})
 #inprimir datos 
    print("\ndatos de alumnos:" )
    for alumno in alumnos:
        print("nombre:",alumno['nombre'],"edad:",alumno['edad'])




