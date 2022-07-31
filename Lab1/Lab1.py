import cv2
import math
import numpy as np
import matplotlib.pyplot as plt


## Problema1
## Devuelve una imagen la cual tenga activos los canales de color indicado
## Parametros de ingreso
## img = imagen 
## color = 	{1: azul, 2:verde, 3:rojo, 10:rojo y verde, 20:verde y azul, 30:azul y rojo}

#imagen
img = cv2.imread('rae.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def problema1(img, color):
	alto = img.shape[0]
	ancho = img.shape[1]
	lienzo = np.zeros((alto, ancho, 3))

	for i in range(0, alto):
		for j in range(0,ancho):
			pixel = img[i,j]
			red = pixel[0]
			blue = pixel[2]
			green = pixel[1]

			if color == 1:
				lienzo[i,j] = [blue,0,0]
			if color == 2: 
				lienzo[i,j] = [0,green,0]
			if color == 3:
				lienzo[i,j] = [0,0,red]
			if color == 10: 
				lienzo[i,j] = [0,green,red]
			if color == 20: 
				lienzo[i,j] = [blue,green,0]
			if color == 30: 
				lienzo[i,j] = [blue,0,red]
	cv2.imwrite("problema1.jpg", lienzo)
	lienzo = cv2.imread("problema1.jpg")
	lienzo = cv2.cvtColor(lienzo, cv2.COLOR_BGR2RGB)
	plt.imshow(lienzo)
	plt.show()



#problema1(img, 30)


imagenazul = cv2.imread('C:/Users/bloom/Desktop/Text Mining and Image Recognition/TextMining-ImageRecognition/Lab1/perro/perro_salida_gray_azul.jpg')
imagenazul = cv2.cvtColor(imagenazul, cv2.COLOR_BGR2RGB)

imagenrojo = cv2.imread('C:/Users/bloom/Desktop/Text Mining and Image Recognition/TextMining-ImageRecognition/Lab1/perro/perro_salida_gray_rojo.jpg')
imagenrojo = cv2.cvtColor(imagenrojo, cv2.COLOR_BGR2RGB)

imagenverde = cv2.imread('C:/Users/bloom/Desktop/Text Mining and Image Recognition/TextMining-ImageRecognition/Lab1/perro/perro_salida_gray_verde.jpg')
imagenverde = cv2.cvtColor(imagenverde, cv2.COLOR_BGR2RGB)




## Problema2
## Devuelve una imagen la cual tenga activos los canales de color indicado
## Parametros de ingreso
## img = imagen 
## color = 	{1: azul, 2:verde, 3:rojo, 10:rojo y verde, 20:verde y azul, 30:azul y rojo}

def problema2(red, green, blue):

	alto = red.shape[0]
	ancho = red.shape[1]
	gris_ponderado = np.zeros((alto, ancho, 3))

	for i in range(0, alto):
		for j in range(0, ancho):
			red_pixel = red[i, j]
			green_pixel = green[i, j]
			blue_pixel = blue[i, j]

			blue_d = blue_pixel[2]
			green_d = green_pixel[1]
			red_d = red_pixel[0]

			gris_ponderado[i, j] = [blue_d, green_d ,red_d] 

	cv2.imwrite('problema2.jpg', gris_ponderado)
	gris_ponderado = cv2.imread("problema2.jpg")
	gris_ponderado = cv2.cvtColor(gris_ponderado, cv2.COLOR_BGR2RGB)
	plt.imshow(gris_ponderado)
	plt.show()



## Problema3
## Devuelve una imagen la cual tenga activos los canales de color indicado
## Parametros de ingreso
## img = imagen 
## color = 	{1: azul, 2:verde, 3:rojo, 10:rojo y verde, 20:verde y azul, 30:azul y rojo}


def problema3(imagen):

	alto = imagen.shape[0]
	ancho = imagen.shape[1]

	gris_ponderado = np.zeros((alto, ancho, 3))
	gris_green = np.zeros((alto,ancho,1))
	gris_blue = np.zeros((alto,ancho,1))
	gris_red = np.zeros((alto,ancho,1))

	for i in range(0, alto):
		for j in range(0, ancho):
			pixel = imagen[i, j]

			gris_blue[i,j] = pixel[2]
			gris_green[i,j] = pixel[1]
			gris_red[i,j] = pixel[0]

			blue = pixel[2]
			green = pixel[1]
			red = pixel[0]

				

	print("Escala de grises en Rojo")
	cv2.imwrite('problema3_red.jpg', gris_red)
	gris_ponderado = cv2.imread("problema3_red.jpg")
	gris_ponderado = cv2.cvtColor(gris_ponderado, cv2.COLOR_BGR2RGB)
	plt.imshow(gris_ponderado)
	plt.show()

	print("Escala de grises en Verde")
	cv2.imwrite('problema3_green.jpg', gris_green)
	gris_ponderado = cv2.imread("problema3_green.jpg")
	gris_ponderado = cv2.cvtColor(gris_ponderado, cv2.COLOR_BGR2RGB)
	plt.imshow(gris_ponderado)
	plt.show()

	print("Escala de grises en Azul")
	cv2.imwrite('problema3_blue.jpg', gris_blue)
	gris_ponderado = cv2.imread("problema3_blue.jpg")
	gris_ponderado = cv2.cvtColor(gris_ponderado, cv2.COLOR_BGR2RGB)
	plt.imshow(gris_ponderado)
	plt.show()


#problema3(img)


def problema4(img):
	alto = img.shape[0]
	ancho = img.shape[1]

	gris_ponderado = np.zeros((alto, ancho, 3))

	for i in range(0, alto):
		for j in range(0, ancho):
			pixel = img[i, j]
			blue = pixel[2]
			green = pixel[1]
			red = pixel[0]
			gris_ponderado[i, j] = int(0.299*blue + 0.587*green + 0.114*red) 

	colores = ['Rojo', 'Azul', 'Verde']
	for i in range(0,3):
		print("Grafica de gris ponderado en color: "+str(colores[i]))
		plt.style.use('ggplot')
		plt.hist(gris_ponderado[i])
		print(gris_ponderado[i])
		plt.axvline(gris_ponderado[i].mean(), color='k', linestyle='dashed', linewidth=1)
		plt.show()

problema4(img)