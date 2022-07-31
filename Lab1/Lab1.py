import cv2
import math
import numpy as np
import matplotlib.pyplot as plt


## Problema1
## Devuelve una imagen la cual tenga activos los canales de color indicado
## Parametros de ingreso
## img = imagen 
## color = 	{1: azul, 2:verde, 3:rojo, 10:rojo y verde, 20:verde y azul, 30:azul y rojo}


img = cv2.imread('paris.jpg')


def problema1(img, color):
	if color != 1 or color != 2 or color != 3 or color != 10 or color != 20 or color != 30:
		return "El numero ingresado no es posible procesar"

	else: 
		pass



