import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Lectura de la imagen original ---
src_path = r'D:\GitHub\TUIA_Segundo\2Cuatrimestre\4C_Imagenes1\U2\Ejercicios\john_canny_bio.png'
img = cv2.imread(src_path, cv2.IMREAD_GRAYSCALE) 
img_final = img.copy() 

# --- 2. Detección automática ---
mascara = img < 15 
sum_filas = np.sum(mascara, axis=1) 
sum_cols = np.sum(mascara, axis=0)  

filas_mancha = np.argwhere(sum_filas > 800)
cols_mancha = np.argwhere(sum_cols > 50)

y1, y2 = filas_mancha[0][0], filas_mancha[-1][0]
x1, x2 = cols_mancha[0][0], cols_mancha[-1][0]

# --- 3. Recorte (Crop) de la Región de Interés ---
mancha = img[y1:y2, x1:x2]

# --- 4. Recuperación del Dato (Binarización Selectiva) ---
mancha_ecualizada = cv2.equalizeHist(mancha)

# Generamos una matriz del mismo tamaño toda en blanco (255)
mancha_recuperada = np.full(mancha.shape, 255, dtype=np.uint8)

# Filtramos exclusivamente los grises correspondientes al texto (ignorando el fibrón en 0 y el papel en 255).
# A esos píxeles los forzamos a negro puro (0).
mancha_recuperada[(mancha_ecualizada > 10) & (mancha_ecualizada < 150)] = 0

# --- 5. Inserción (Crop and Replace) ---
# Reemplazamos la región con nuestro nuevo recorte limpio
img_final[y1:y2, x1:x2] = mancha_recuperada

# --- 6. Visualización y Guardado Físico ---
plt.figure(figsize=(15, 8))

plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title('1. Original')
plt.axis('off')

plt.subplot(2, 2, 2)
# Mostramos el histograma de la mancha ANTES de ecualizar (para entender el problema)
plt.hist(mancha.flatten(), 256, [0, 256])
plt.title('2. Histograma Original de la Mancha')

plt.subplot(2, 2, 3)
# Mostramos el histograma DESPUÉS de ecualizar
plt.hist(mancha_ecualizada.flatten(), 256, [0, 256])
plt.title('3. Histograma Ecualizado')

plt.subplot(2, 2, 4)
plt.imshow(img_final, cmap='gray', vmin=0, vmax=255)
plt.title('4. Recuperada')
plt.axis('off')

plt.tight_layout()

# Guardado en disco por si Tkinter falla
cv2.imwrite('resultado_mancha.png', img_final)
plt.savefig('resultado_grafico.png')

plt.show()