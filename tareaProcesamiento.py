#!/usr/bin/env python
# Este archivo usa el encoding: utf-8

entrada="Soy el vigilante del Muro32. Soy el fuego que arde contra4 el frío, la 021 luz que trae el amanecer, e23l cuerno que despierta a los durmientes, el escudo que defiende los reinos de los hombres. Entrego mi vida y mi honor a la Guardia de la Noche, durante esta noche y todas las que estén por venir."
signos=".,:;-_()[]\"!¡¿?'*"
acentos="áéíóúü"
noAcentos="aeiouu"
numeros="0123456789"

print("Entrada= ",entrada)
#Separa texto en palabras y convierte mayúsculas en minúsculas
texto=entrada.lower().split()

#Elimina signos de puntuación
for s in signos:
	i=0
	while i<len(texto):
		if s in texto[i]:
			texto[i]=texto[i].replace(s,"")
		i+=1

#Elimina números
for n in numeros:
	i=0
	while i<len(texto):
		if n in texto[i]:
			texto[i]=texto[i].replace(n,"")
		i+=1

#Elimina acentos y diéresis
i=0
while i<len(texto):
	j=0
	while j<len(acentos):
		if acentos[j] in texto[i]:
			texto[i]=texto[i].replace(acentos[j],noAcentos[j])
		j+=1
	i+=1

#Imprime texto procesado
textoProcesado=""
for palabra in texto:
	textoProcesado+=palabra+" "
print(textoProcesado)

#Conteo de vocabulario
vocabulario=[]
conteo=0
for palabra in texto:
	if not palabra in vocabulario:
		vocabulario.append(palabra)
		conteo+=1
print("Conteo de vocabulario= ",conteo)

#Calcula la distribución de vocabulario
distribucion=conteo/len(texto)
print("Distribucion de vocabulario= ",distribucion)


