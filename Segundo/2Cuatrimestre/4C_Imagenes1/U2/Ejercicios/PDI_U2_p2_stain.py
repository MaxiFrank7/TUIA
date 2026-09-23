# -*- coding: utf-8 -*-
import os

import cv2
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

## --- Global Variables ---------------------------------

JOHN_CANNY_BIO_PATH = Path.cwd() / "john_canny_bio.png"

## ------------------------------------------------------

## --- Métodos ------------------------------------------

def imdata(
    image: cv2.typing.MatLike = None, 
    image_name: str = None
) -> None:
    ''' Método que obtiene y expone la información básica sobre la imagen `<image>`.
        ## Args:
            - image [MatLike]: Imagen de entrada.
            - image_name [str]: Nombre de la imagen de entrada.
        ## Outputs:
            - None
    '''

    if image is None:
        print('No se ha detectado una imagen de entrada.')
        return None

    print(f'''
        Imagen: {image_name}
        Tipo de la representación de la imagen: {type(image)}
        Tipo de dato de cada elemento de la matriz: {image.dtype}
        Dimensiones la matriz: {image.shape} (Alto, Ancho, Canales)
        Valor mínimo de intensidad de píxel: {image.min()}
        Valor máximo de intensidad de píxel: {image.max()}
        Valores únicos de intensidad de píxel: {np.unique(image)}
    ''')

    return None

def imshow(
    image: cv2.typing.MatLike, 
    title: str = None, 
    figure_id: int = None, 
    figure_flag: bool = True, 
    subplot_id: int = None, 
    subplot_axes: plt.Axes = None, 
    subplot_flag: bool = False, 
    color_flag: bool = False, 
    block_flag: bool = False, 
    colorbar_flag: bool = False, 
    ticks_flag: bool = False, 
    adjust_flag: bool = False
) -> plt.Axes:
    ''' Método personalizado que permite expandir las configuraciones del método imshow(..) de MatplotLib, 
        centralizando las opciones de configuración más utilizadas.
        ## Args:
            - image [MatLike]: Imagen de entrada.
            - title [str]: Título de la visualización.
            - figure_id [int]: ID de la figura.
            - figure_flag [bool]: Bandera del uso de figura con ID.
            - subplot_id [int]: ID del subplot.
            - subplot_axes [Axes]: Ejes relacionados del subplot.
            - subplot_flag [bool]: Bandera del uso de subplot con ID.
            - color_flag [bool]: Bandera del uso de mapa de color (True) o escala de grises (False).
            - block_flag [bool]: Bandera del uso del bloqueo de ventana.
            - colorbar_flag [bool]: Bandera del uso de la barra de color.
            - ticks_flag [bool]: Bandera del uso de ejes.
            - adjust_flag [bool]: Bandera del uso del rango dinámico [min(), max()] (True) o del rango dinámico [0, 255] (False).
        ## Outputs:
            - axes [Axes]: Ejes relacionados del subplot.
    '''

    axes = None
    if image is None:
        print('No se ha detectado una imagen de entrada.')
        return axes

    if figure_flag:
        plt.figure(figure_id)
    
    if subplot_flag and subplot_id:
        if subplot_axes:
            axes = plt.subplot(subplot_id, sharex = subplot_axes, sharey = subplot_axes)
        else:
            axes = plt.subplot(subplot_id)

    if color_flag:
        plt.imshow(image)
    else:
        if adjust_flag:
            plt.imshow(image, cmap = 'gray')
        else:
            plt.imshow(image, cmap = 'gray', vmin = 0, vmax = 255)
    
    plt.title(title)
    
    if not(ticks_flag):
        plt.xticks([]), plt.yticks([])
    
    if colorbar_flag:
        plt.colorbar()
    
    if figure_flag:
        plt.show(block = block_flag)

    return axes

## ------------------------------------------------------

## --- Principal ----------------------------------------

# -- Carga de la imagen original
bgr_image = cv2.imread(JOHN_CANNY_BIO_PATH, cv2.IMREAD_COLOR)
if bgr_image is None:
    print(f'No fue posible cargar la imagen desde \'{JOHN_CANNY_BIO_PATH}\'.')
    exit()

# -- Conversión a escala de grises
rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)

axes = imshow(rgb_image, 'Imagen original', figure_id = 1, subplot_flag = True, subplot_id = 121, adjust_flag = True)
imshow(gray_image, 'Imagen en Escala de Grises', figure_id = 1, subplot_flag = True, subplot_id = 122, subplot_axes = axes, adjust_flag = True)

# -- Matriz booleana condicional y sumas máximas en las filas (líneas horizontales)
boolean_matrix = gray_image < 5
sum_rows = np.sum(boolean_matrix, axis = 1)
sum_max = sum_rows.max()
threshold_h1 = int(np.argwhere(sum_rows == sum_max)[0][0])
threshold_h2 = int(np.argwhere(sum_rows == sum_max)[-1][0])

# -- Recorte horizontal de la zona inferior
cropped_image = gray_image[threshold_h1:threshold_h2, :]

# Matriz booleana condicional y, primera y última suma máxima en las columnas (límites de la mancha)
boolean_matrix = cropped_image < 5
sum_columns = np.sum(boolean_matrix, axis = 0)
sum_max = sum_columns.max()
threshold_w1 = int(np.argwhere(sum_columns == sum_max)[0][0])
threshold_w2 = int(np.argwhere(sum_columns == sum_max)[-1][0])

# -- Recorte vertical de la zona de la mancha
cropped_image = cropped_image[:, threshold_w1:threshold_w2]

imshow(cropped_image, 'Zona de Afectada', figure_id = 2, adjust_flag = True)

# -- Cálculo de histogramas
global_histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
local_histogram = cv2.calcHist([cropped_image], [0], None, [256], [0, 256])
''' Nota:
    - cv2.calcHist(): Método de cálculo de histograma con con efiencia alta en imágenes, permite el uso de multicanal y máscaras.
    - np.histogram(): Método de cálculo de histograma con con efiencia media en imágenes pero soporta cualquier tipo de datos. Sin embargo, no soporta multicanal ni el uso de máscaras.
    - plt.hist(): Método de cálculo de histograma con con efiencia baja en imágenes, apunta a sólo la visualización del mismo.
'''

# -- Ecualización de histogramas
global_equalized_histogram = cv2.equalizeHist(gray_image)
local_equalized_histogram = cv2.equalizeHist(cropped_image)

# -- Información de las imágenes
imdata(rgb_image, os.path.basename(JOHN_CANNY_BIO_PATH))
imdata(gray_image, f'{os.path.basename(JOHN_CANNY_BIO_PATH)} en escala de grices')
imdata(global_equalized_histogram, f'{os.path.basename(JOHN_CANNY_BIO_PATH)} globalmente ecualizada.')
imdata(cropped_image, 'ROI de la Mancha')
imdata(local_equalized_histogram, f'{os.path.basename(JOHN_CANNY_BIO_PATH)} localmente ecualizada.')

# -- Resultados de la ecualización global
plt.figure(3)
subplot_axes = plt.subplot(121)
plt.hist(gray_image.flatten(), 256, [0, 256]), plt.title('Histograma Global')
plt.subplot(122, sharex = subplot_axes, sharey = subplot_axes), plt.hist(global_equalized_histogram.flatten(), 256, [0, 256]), plt.title('Histograma Global Ecualizado')
plt.show(block = False)

axes = imshow(gray_image, 'Imagen Original', figure_id = 4, subplot_flag = True, subplot_id = 121, adjust_flag = True)
imshow(global_equalized_histogram, 'Imagen Ecualizada', figure_id = 4, subplot_flag = True, subplot_id = 122, subplot_axes = axes, adjust_flag = True)

# -- Resultados de la ecualización local
plt.figure(5)
subplot_axes = plt.subplot(121)
plt.hist(cropped_image.flatten(), 256, [0, 256]), plt.title('Histograma Local')
plt.subplot(122, sharex = subplot_axes, sharey = subplot_axes), plt.hist(local_equalized_histogram.flatten(), 256, [0, 256]), plt.title('Histograma Local Ecualizado')
plt.show(block = False)

axes = imshow(cropped_image, 'Zona de Mancha', figure_id = 6, subplot_flag = True, subplot_id = 121, adjust_flag = True)
imshow(local_equalized_histogram, 'Zona de Mancha Ecualizada', figure_id = 6, subplot_flag = True, subplot_id = 122, subplot_axes = axes, adjust_flag = True)

# -- Reemplazo en la imagen completa
restored_image = rgb_image.copy()
restored_image[threshold_h1:threshold_h2, threshold_w1:threshold_w2] = cv2.cvtColor(local_equalized_histogram, cv2.COLOR_GRAY2RGB)

# -- Resultados finales
axes = imshow(rgb_image, 'Información Oculta', figure_id = 7, subplot_flag = True, subplot_id = 121, adjust_flag = True)
imshow(restored_image, 'Información Recuperada', figure_id = 7, subplot_flag = True, subplot_id = 122, subplot_axes = axes, adjust_flag = True, block_flag = True)

## ------------------------------------------------------
