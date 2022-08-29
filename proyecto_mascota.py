puntos = 0 

print("Es muy importante encontrar un buen hogar para un perrito, veamos si eres apto para tener un perrito")
print("Por favor, responde unicamente con 'si' o 'no'")

pregunta_1 = input("¿Eres mayor de 12 años?: ") 
if pregunta_1 == "si":
    puntos = (puntos + 1)
pregunta_2 = input("¿Tienes dinero para comprar su comida?: ")
if pregunta_2 == "si":
    puntos = (puntos + 1)
pregunta_3 = input("¿Tienes tiempo libre para sacarlo a pasar todos los dias al menos una hora, dos a tres veces al dia?: ")
if pregunta_3 == "si":
    puntos = (puntos + 1)
pregunta_4 = input("¿Te consideras una persona responsable?: ")
if pregunta_4 == "si":
    puntos = (puntos + 1)
pregunta_5 = input("¿Tu familia puede ayudarte a cuidarlo?: ")
if pregunta_5 == "si":
    puntos = (puntos + 1)

if puntos >= 4:
    print("¡Muchas felicidades, puedes adoptar a un perrito!")
if puntos == 3:
    print("Puedes tener un perrito, pero te recomendamos mejorar en las areas en las que fallas")
if puntos <= 2:
    print("Lo sentimos... Parece que por el momento no puedes cuidar de un perrito :(")