puntos = 0 


#Creacion de lista de respuestas
d1 = {
  "¿Eres mayor de 12 años?: ": "1 punto",
  "¿Tienes dinero para comprar su comida?: ": "3 puntos",
  "¿Tienes tiempo libre para sacarlo a pasar todos los dias al menos una hora, dos a tres veces al dia?: ": "2 puntos",
  "¿Te consideras una persona responsable?: " : "4 puntos",
  "¿Tu familia puede ayudarte a cuidarlo?: " : "3 puntos" 

}


#Funcion para mostrar los puntos del usuario
def puntos_persona(nombre, puntos):    
    print(f"{nombre}, tu puntuacion fue de {puntos} puntos")

#Introduccion al programa
print("Es muy importante encontrar un buen hogar para un perrito, veamos si eres apto para tener un perrito")
print("Por favor, responde unicamente con 'si' o 'no'")

#Preguntas de si/no al usario
nombre = input("Inserta tu nombre: ")

pregunta_1 = input("¿Eres mayor de 12 años?: ") 
if pregunta_1 == "si":
    puntos = (puntos + 1)
   
   
pregunta_2 = input("¿Tienes dinero para comprar su comida?: ")
if pregunta_2 == "si":
    puntos = (puntos + 3)
   

pregunta_3 = input("¿Tienes tiempo libre para sacarlo a pasar todos los dias al menos una hora, dos a tres veces al dia?: ")
if pregunta_3 == "si":
    puntos = (puntos + 2)
    

pregunta_4 = input("¿Te consideras una persona responsable?: ")
if pregunta_4 == "si":
    puntos = (puntos + 4)


pregunta_5 = input("¿Tu familia puede ayudarte a cuidarlo?: ")
if pregunta_5 == "si":
    puntos = (puntos + 3)
    
    

#Preguntas de calificacion
q1 = int(input("Del 1 al 5, que tan ordenado te consideras?: "))
while q1 <= 0: 
    print("¡Has escrito un numero negativo o cero! Intenta con un numero positivo")
    q1 = int(input("Escribelo de nuevo: ")) 
if q1 == 5: 
    puntos = (puntos + 5)
if q1 == 4:
    puntos = (puntos + 4)
if q1 == 3:
    puntos = (puntos + 3)
if q1 == 2:
    puntos = (puntos + 2)
if q1 == 1:
    puntos = (puntos + 1)

#Llamando a la funcion del puntaje del usuario
puntos_persona(nombre,puntos)

#Imprime la lista de preguntas con sus puntos respectivos
print(f"Estos son los puntajes de cada pregunta: {d1}" )


#Mensaje final (Salida)
if puntos == 18 and puntos >= 13:
    print("¡Muchas felicidades, puedes adoptar a un perrito!")
if puntos <13 and puntos >=8:
    print(nombre,"Puedes tener un perrito, pero te recomendamos mejorar en las areas en las que fallas")
if puntos <8:
    print(nombre,"Lo sentimos... Parece que por el momento no puedes cuidar de un perrito :(")


    
    













