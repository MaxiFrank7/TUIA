import cv2
import numpy as np
import matplotlib.pyplot as plt

# Defininimos función para mostrar imágenes
def imshow(img, new_fig=True, title=None, color_img=False, blocking=False, colorbar=False, ticks=False):
    if new_fig:
        plt.figure()
    if color_img:
        plt.imshow(img)
    else:
        plt.imshow(img, cmap='gray')
    plt.title(title)
    if not ticks:
        plt.xticks([]), plt.yticks([])
    if colorbar:
        plt.colorbar()
    if new_fig:
        plt.show(block=blocking)

# Definimos la función para adelgazar desarrollada en la Unidad 6: $Morfología$
G123_LUT = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1,
       0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0,
       1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
       0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1,
       0, 0, 0], dtype=np.bool_)

G123P_LUT = np.array([0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0,
       1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0,
       0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0,
       1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1,
       0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0], dtype=np.bool_)

def imthin(image, n_iter=None):
    """
    imthin: Realiza el adelgazamiento (thinning) morfológico de una imagen binaria.

    Parametros
    ----------
    image   : Imagen binaria (M,N) ndarray, valores permitidos: 0 y 1.
    n_iter  : int, numero de iteraciones (opcional).

    Salida
    ------
    out     : Imagen binaria (M,N) ndarray. Imagen adelgazada (thinned).

    Referencias
    ----------
    [1] Z. Guo and R. W. Hall, "Parallel thinning with two-subiteration algorithms," Comm. ACM, vol. 32, no. 3, pp. 359-373, 1989.
    [2] Lam, L., Seong-Whan Lee, and Ching Y. Suen, "Thinning Methodologies-A Comprehensive Survey," IEEE Transactions on Pattern Analysis and Machine Intelligence, Vol 14, No. 9, 1992, p. 879
    """
    # --- Check n_iter -----------------------------------------
    if n_iter is None:
        n = -1
    elif n_iter <= 0:
        raise ValueError('n_iter must be > 0')
    else:
        n = n_iter

    # --- Check image ------------------------------------------
    skel = np.array(image).astype(np.uint8)
    if skel.ndim != 2:
        raise ValueError('"image" debe ser un array 2D.')
    if not np.all(np.in1d(image.flat,(0,1))):
        raise ValueError('"image" debe contener valores 0s y 1s solamente.')

    # --- Definiciones iniciales -------------------------------
    mask = np.array([[ 8,  4,  2],
                     [16,  0,  1],
                     [32, 64,128]],dtype=np.uint8)

    # --- Procesamiento ----------------------------------------
    while n != 0:
        before = np.sum(skel)                                                   # Cuento la cantidad de pixels True antes de esta iteración...
        # ----------------------------------
        for lut in [G123_LUT, G123P_LUT]:                                       # sub-itero para cada LUT
            N = cv2.filter2D(skel, -1, mask, borderType=cv2.BORDER_CONSTANT)    # Correlación entre la imagen y la máscara
            D = np.take(lut, N)                                                 # Decido que pixels eliminar en base al resultado de la correlación y la LUT.
            skel[D] = 0                                                         # Elimino pixels (adelgazo)
        # ----------------------------------
        after = np.sum(skel)                                                    # Cuento la cantidad de pixels True al final de esta iteración.
        if before == after:                                                     # Si no hay cambios, no itero mas, termine el adelgazamiento...
            break
        n -= 1                                                                  # Caso contrario, decremento n
    return skel.astype(np.bool_)

# =====================================================================================================
# =====================================================================================================
# Descripción del ejercicio
# Dada una imagen de un cromosoma obtenida utilizando un microscopio, se plantea la necesidad de 
# contar la cantidad de extremidades que posee de manera automática.
# =====================================================================================================
# =====================================================================================================

# Cargamos la imagen y visualizamos
img = cv2.imread("cromosoma.tif", cv2.IMREAD_GRAYSCALE)
W,H = img.shape
print(img.dtype)
print(img.shape)
print(np.unique(img))
imshow(img, title="Imagen Original")

# Observando lo obtenido anteriormente, vemos que la imagen es del tipo binaria, por lo cual, no es necesario umbralar.
# Primero, filtramos el ruido presente en la imagen.
img_b = cv2.GaussianBlur(img, (25,25), 15.0)
print(np.unique(img_b))
imshow(img_b, title="Imagen Filtrada (PB)")

# Como observamos, si bien logramos eliminar el ruido de manera eficiente, la imagen ahora si está en niveles de 
# grises, por lo cual, debemos umbralizar."""
th, img_bin = cv2.threshold(img_b, 127, 255, cv2.THRESH_OTSU)
print(th)
imshow(img_bin, title="Imagen umbralada")

# Luego, obtenemos el contorno del cromosoma
ext_contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
img_out = cv2.merge((img_bin,img_bin,img_bin))
cv2.drawContours(img_out, ext_contours, -1, (255,0,0), 2)
imshow(img_out, title="Contorno exterior")

# Luego, obtenemos el esqueleto del cromosoma, aplicando un afinamiento morfológico.
th, thin_input= cv2.threshold(img_bin,127, 1, cv2.THRESH_OTSU)  # Hacemos esto, porque imthin requiere que los valores de entrada sean 0/1.
print(np.unique(thin_input))

img_skel = imthin(thin_input)
print(np.unique(img_skel))
imshow(img_skel, "Esqueleto")

# Generamos una imagen con el contorno y el esqueleto resaltados.
img_out[img_skel] = (0,0,255)
imshow(img_out, title="Contorno exterior + Esqueleto")

# Ahora, procedemos a contar los extremos del cromosoma, para lo cual, hacemos uso del método Morfológico Hit-or-Miss.
# Definimos una función que detecta los puntos finales o $endpoints$ de los objetos en una imagen binaria.
def endpoints(f):
    B1 = np.array([[1, -1, -1], [-1, 1, -1], [-1, -1, -1]])
    B2 = np.array([[-1, 1, -1], [-1, 1, -1], [-1, -1, -1]])
    B3 = np.array([[-1, -1, 1], [-1, 1, -1], [-1, -1, -1]])
    B4 = np.array([[-1, -1, -1], [1, 1, -1], [-1, -1, -1]])
    B5 = np.array([[-1, -1, -1], [-1, 1, 1], [-1, -1, -1]])
    B6 = np.array([[-1, -1, -1], [-1, 1, -1], [1, -1, -1]])
    B7 = np.array([[-1, -1, -1], [-1, 1, -1], [-1, 1, -1]])
    B8 = np.array([[-1, -1, -1], [-1, 1, -1], [-1, -1, 1]])
    f1 = cv2.morphologyEx(f, cv2.MORPH_HITMISS, B1)
    f2 = cv2.morphologyEx(f, cv2.MORPH_HITMISS, B2)
    f3 = cv2.morphologyEx(f, cv2.MORPH_HITMISS, B3)
    f4 = cv2.morphologyEx(f, cv2.MORPH_HITMISS, B4)
    f5 = cv2.morphologyEx(f, cv2.MORPH_HITMISS, B5)
    f6 = cv2.morphologyEx(f, cv2.MORPH_HITMISS, B6)
    f7 = cv2.morphologyEx(f, cv2.MORPH_HITMISS, B7)
    f8 = cv2.morphologyEx(f, cv2.MORPH_HITMISS, B8)

    fend = f1 | f2 | f3 | f4 | f5 | f6 | f7 | f8

    return fend

# Ahora, antes de aplicar esta función, convertimos la imagen lógica en uint8.
f = img_skel.copy()
f = f.astype(np.uint8)*255
print(np.unique(f))

# Y ahora sí, encontramos la cantidad de extremos del cromosoma.
f_endpoints = endpoints(f)
N_extremos = (f_endpoints>0).sum()
print(N_extremos)

# Como podemos ver, se encontraron 5 extremos en vez de 4.
# Obtenemos las coordenadas de los extremos para analizar.
f_endpoints_cord = np.argwhere(f_endpoints)
print(f_endpoints_cord)

# Y ahora graficamos los extremos.
img_extremos = img_out.copy()
for p in f_endpoints_cord:
    cv2.circle(img_extremos, tuple((p[1],p[0])), 5, (0,255,0), -1)
imshow(img_extremos, title="Extremos")

# Debido a este problema, se propone realizar un suavizado de la primera umbralización, utilizando una apertura, y luego repetir las mismas operaciones que se realizaron anteriormente.
st = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (60,60))
img_bin_suav = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, st)

plt.figure()
ax1 = plt.subplot(121); imshow(img_bin, title="Imagen umbralada", new_fig=False)
plt.subplot(122, sharex=ax1, sharey=ax1); imshow(img_bin_suav, title="Imagen umbralada + Suavizado", new_fig=False)
plt.show(block=False)

ext_contours, _ = cv2.findContours(img_bin_suav, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
img_out = cv2.merge((img_bin_suav,img_bin_suav,img_bin_suav))
cv2.drawContours(img_out, ext_contours, -1, (255,0,0), 2)
imshow(img_out, title="Contorno exterior")

th, thin_input= cv2.threshold(img_bin_suav, 127, 1, cv2.THRESH_OTSU)
img_skel = imthin(thin_input)
imshow(img_skel, "Esqueleto")

img_out[img_skel] = (0,0,255)
imshow(img_out, title="Contorno exterior + Esqueleto")

f = img_skel.copy()
f = f.astype(np.uint8)*255

f_endpoints = endpoints(f)
(f_endpoints>0).sum()

f_endpoints_cord = np.argwhere(f_endpoints)
f_endpoints_cord

img_extremos = img_out.copy()
for p in f_endpoints_cord:
    cv2.circle(img_extremos, tuple((p[1],p[0])), 5, (0,255,0), -1)
imshow(img_extremos, title="Extremos")
# Puede verse que se logró el objetivo.
