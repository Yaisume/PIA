import requests
import json
import statistics

url="https://restcountries.com/v3.1/region/america?fields=name,area,unMember,languages,independent,population"

respuesta = requests.get(url)
lista_datos=[]

if respuesta.status_code==200:
	datos=respuesta.json()
	with open('datos.json', 'w') as archivo:
		json.dump(datos, archivo, indent=4)

	for pais in datos:
		if pais.get("independent")==True:
			nombre=pais["name"]["common"]
			area=pais["area"]
			lenguajes=list(pais["languages"].values())
			miembro_onu=pais["unMember"]
			poblacion=pais["population"]

			lista_datos.append({"País":nombre, "Área": area, "Lenguajes": lenguajes, "Población": poblacion, "Miembro de la Onu": miembro_onu,})
	


datos_america=str(lista_datos)

with open('paises_america.txt', 'a') as archivo:
	archivo.write(datos_america)


def main_areas(lista_datos):
	areas=[]
	for i in range (len(lista_datos)):
		a=lista_datos[i]["Área"]
		areas.append(a)
	return areas
main_areas(lista_datos)

def analisis_areas(areas):
	print(f"El area promedio de los países en Ámerica es: {statistics.mean(areas):.2f} kilometros cuadrados")
	print(f"Mediana: {statistics.median(areas):.2f} kilometros cuadrados")
areas=main_areas(lista_datos)
analisis_areas(areas)


def frecuencia_idiomas (lista_datos): #Definimos la función

	from collections import Counter		#Importamos Counter para sacar la frecuencia
	import matplotlib.pyplot as plt 	#Importamos matplotlib


	#Sacamos la frecuencia de idiomas hablados en el continente americano
	frecuencia_idiomas=Counter(lenguajes)	
	for pais in lista_datos:
		frecuencia_idiomas.update(pais["Lenguajes"])	#Cuenta los países que coinciden en el idioma
	for idioma, count in frecuencia_idiomas.most_common():
		print(f"{idioma}: {count}")	#Muestra los datos obtenidos
 
 
	#Realizamos gráfica de barras con matplotlib
	etiquetas = ["Español","Inglés","Guaraní","Francés","Aymara","Quechua","Criollo Haitiano","Criollo Beliceño","Holandés","Dialecto Jamaiquino","Portugés"] 
	valores = [19, 15, 3, 2, 2, 2, 1, 1, 1, 1, 1] 
	plt.bar(etiquetas, valores, color='purple') 
	plt.title("Frecuencia de idiomas en América") 
	plt.show()	#Muestra la grafica


def porcentaje_idiomas(lista_datos):	#Definimos la función
	
	from collections import Counter		#Importamos Counter para sacar la frecuencia
	import matplotlib.pyplot as plt 	#Importamos matplotlib
	#No usamos la la función frecuencia_idiomas ya que no queremos saturar al imprimir los datos ni hacer la gráfica	

	frecuencia_idiomas=Counter(lenguajes)	#Cuenta los países que coinciden en el idioma
	for pais in lista_datos:
		frecuencia_idiomas.update(pais["Lenguajes"])

	#Sacamos porcentajes
	total_paises=len(datos)
	porcentajes = {idioma: (count / total_paises) * 100
		for idioma, count in frecuencia_idiomas.most_common()
	}
	print("Porcentaje de idiomas en América (por países)")
	for idioma, porcentaje in porcentajes.items():
    		print(f"{idioma}: {porcentaje:.2f}%")	#Imprimimos los datos

	#Realizamos gráfica de pastel
	idiomas= list(porcentajes.keys()) 
	valores = list(porcentajes.values()) 
	plt.pie(valores, labels=idiomas, autopct='%1.1f%%') 
	plt.title("Porcentaje de idiomas hablados en el continente americano") 
	plt.axis('equal') 
	plt.show() 	#Muestra la gráfica



