import numpy as np
import matplotlib.pyplot as plt
import cv2

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

# ------------------------------------------------------------------------------------------------------
# -- Cargo el video 1 ----------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
video_person = {}
video_person["path"] = "Man_walking_with_green_screen_background.mp4"
cap = cv2.VideoCapture(video_person["path"])                 

# Obtengo Meta-Información 
video_person["width"] = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))      
video_person["height"] = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))    
video_person["fps"] = int(cap.get(cv2.CAP_PROP_FPS))                
video_person["n_frames"] = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))   
print(f'{video_person["path"]} --> Ancho={video_person["width"]} | Alto={video_person["height"]} | fps={video_person["fps"]} | Cant. frames = {video_person["n_frames"]}')

# --- Visualización del video ---------------------------------------------
while (cap.isOpened()):                                                 # Itero, siempre y cuando el video esté abierto
    ret, frame = cap.read()                                             # Obtengo el frame
    if ret==True:                                                       # ret indica si la lectura fue exitosa (True) o no (False)
        cv2.imshow('Frame',frame)                                       # Muestro el frame
        if cv2.waitKey(25) & 0xFF == ord('q'):                          # Corto la repoducción si se presiona la tecla "q"
            break
    else:
        break                                       # Corto la reproducción si ret=False, es decir, si hubo un error o no quedán mas frames.
cap.release()                   # Cierro el video
cv2.destroyAllWindows()         # Destruyo todas las ventanas abiertas

# --- Analizo un frame -----------------------------------------------------
cap = cv2.VideoCapture(video_person["path"])        # Abro el video
ret, frame = cap.read()                             # Obtengo 1 frame
cap.release()                                       # Cierro el video

frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
imshow(frame, title="Video person - Frame 1")

# ------------------------------------------------------------------------------------------------------
# -- Cargo el video 2 ----------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
video_background = {}
video_background["path"] = "Background.mp4"
cap2 = cv2.VideoCapture(video_background["path"])                  # Abro el video

# Obtengo Meta-Información 
video_background["width"] = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))      
video_background["height"] = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))    
video_background["fps"] = int(cap2.get(cv2.CAP_PROP_FPS))                
video_background["n_frames"] = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))   
print(f'{video_background["path"]} --> Ancho={video_background["height"]} | Alto={video_background["height"]} | fps={video_background["fps"]} | Cant. frames = {video_background["n_frames"]}')

# Visualización del video
while (cap2.isOpened()):                                                 # Itero, siempre y cuando el video esté abierto
    ret, frame = cap2.read()                                             # Obtengo el frame
    if ret==True:                                                       # ret indica si la lectura fue exitosa (True) o no (False)
        cv2.imshow('Frame',frame)                                       # Muestro el frame
        if cv2.waitKey(25) & 0xFF == ord('q'):                          # Corto la repoducción si se presiona la tecla "q"
            break
    else:
        break                                       # Corto la reproducción si ret=False, es decir, si hubo un error o no quedán mas frames.
cap2.release()                   # Cierro el video
cv2.destroyAllWindows()         # Destruyo todas las ventanas abiertas

# --- Analizo un frame -----------------------------------------------------
cap = cv2.VideoCapture(video_background["path"])               # Abro el video
ret, frame_background = cap.read()                             # Obtengo 1 frame
cap.release()                                       # Cierro el video

frame_background = cv2.cvtColor(frame_background, cv2.COLOR_BGR2RGB)
imshow(frame_background, title="Video background - Frame 1")


# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# -- Procesamiento -------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------

# --- Cargo un frame del video con la persona -----------------------------
cap = cv2.VideoCapture(video_person["path"])        # Abro el video
ret, frame = cap.read()                             # Obtengo 1 frame
cap.release()                                       # Cierro el video

frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
imshow(frame, title="Video person - Frame 1")

# --- Analizo un recorte del frame ----------------------------------------
bg_crop_RGB = frame[0:300, 0:300, :]                     # Cortar una porcion correspondiente al fondo.
imshow(bg_crop_RGB, title="Frame 1 - Crop fondo verde")

# Analisis
img_pixels = bg_crop_RGB.reshape(-1,3)                                 # Re-ordeno los pixels, de manera que cada pixel ocupe una fila.
colours, counts = np.unique(img_pixels, axis=0, return_counts=True) # Obtengo los valores únicos de todos los pixels y su frecuencia de aparición.
N_colours = colours.shape[0]                                        # Cantidad de colores.
N_colours
colours
counts

bg_color_RGB = colours[0]
bg_color_RGB = np.reshape(bg_color_RGB,(1,1,-1))
bg_color_HSV = cv2.cvtColor(bg_color_RGB, cv2.COLOR_RGB2HSV)    # Conversión a HSV.
bg_color_HSV

frame_hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)              # Convierto el frame a HSV también...

# ----------------------------------------------------------------------------
# --- Prueba 1: Match Exacto -------------------------------------------------
# ----------------------------------------------------------------------------
mask_bg = cv2.inRange(frame_hsv, bg_color_HSV[0,0,:], bg_color_HSV[0,0,:])
mask_person = cv2.bitwise_not(mask_bg)
bg = cv2.bitwise_and(frame, frame, mask=mask_bg)
person = cv2.bitwise_and(frame, frame, mask=mask_person)

plt.figure()
ax = plt.subplot(231); imshow(frame, title="Frame", new_fig=False)
plt.subplot(232, sharex=ax, sharey=ax), imshow(mask_bg, title="Máscara Background", new_fig=False)
plt.subplot(233, sharex=ax, sharey=ax), imshow(mask_person, title="Máscara persona", new_fig=False)
plt.subplot(235, sharex=ax, sharey=ax), imshow(bg, title="Background", new_fig=False)
plt.subplot(236, sharex=ax, sharey=ax), imshow(person, title="Persona", new_fig=False)
plt.suptitle(f'bg_RGB = {bg_color_RGB} | bg_HSV = {bg_color_HSV}')
plt.show(block=False)

# Analizemos en HSV...
bg_HSV = cv2.bitwise_and(frame_hsv, frame_hsv, mask=mask_bg)
person_HSV = cv2.bitwise_and(frame_hsv, frame_hsv, mask=mask_person)
plt.figure()
ax = plt.subplot(231); imshow(frame_hsv, title="Frame", new_fig=False)
plt.subplot(232, sharex=ax, sharey=ax), imshow(mask_bg, title="Máscara Background", new_fig=False)
plt.subplot(233, sharex=ax, sharey=ax), imshow(mask_person, title="Máscara persona", new_fig=False)
plt.subplot(235, sharex=ax, sharey=ax), imshow(bg_HSV, title="Background", new_fig=False)
plt.subplot(236, sharex=ax, sharey=ax), imshow(person_HSV, title="Persona", new_fig=False)
plt.subplot(234, sharex=ax, sharey=ax), imshow(frame, title="Frame RGB", new_fig=False)
plt.suptitle(f'HSV - bg_RGB = {bg_color_RGB} | bg_HSV = {bg_color_HSV}')
plt.show(block=False)


# ----------------------------------------------------------------------------
# --- Prueba 2: Rango --------------------------------------------------------
# ----------------------------------------------------------------------------
delta_bg = np.array([10.0, 150.0, 150.0])
# delta_bg = np.array([0, 0, 0])
lower_limmit = np.clip(bg_color_HSV - delta_bg, 0, 255)
upper_limmit = np.clip(bg_color_HSV + delta_bg, 0, 255)
mask_bg = cv2.inRange(frame_hsv, lower_limmit, upper_limmit)
mask_person = cv2.bitwise_not(mask_bg)
bg = cv2.bitwise_and(frame, frame, mask=mask_bg)
person = cv2.bitwise_and(frame, frame, mask=mask_person)

plt.figure()
ax = plt.subplot(231); imshow(frame, title="Frame", new_fig=False)
plt.subplot(232, sharex=ax, sharey=ax), imshow(mask_bg, title="Mascara bg", new_fig=False)
plt.subplot(233, sharex=ax, sharey=ax), imshow(mask_person, title="Mascara persona", new_fig=False)
plt.subplot(235, sharex=ax, sharey=ax), imshow(bg, title="Background", new_fig=False)
plt.subplot(236, sharex=ax, sharey=ax), imshow(person, title="Persona", new_fig=False)
plt.suptitle(f'bg_RGB = {bg_color_RGB} | bg_HSV = {bg_color_HSV} | delta = {delta_bg}')
plt.show(block=False)

# Observaciones: Funciona bastante bien, pero en el borde de la persona quedan pixels verdes.
#                Si extiendo el rango de unbraldo (es decir delta_bg), empieza a generar problemas 
#                con los pixels dentro de la persona.
#                Mejor dejarlo asi y agregar una nueva etapa de filtrado, pero solo en el borde de la persona.

# ----------------------------------------------------------------------------
# --- Prueba 2: Rango + Post procesamiento (Morfología) ----------------------
# ----------------------------------------------------------------------------
SE_SIZE = 2
se = cv2.getStructuringElement(cv2.MORPH_RECT, (SE_SIZE,SE_SIZE))
mask_bg_p1 = cv2.morphologyEx(mask_bg, cv2.MORPH_DILATE, se)
mask_person_p1 = cv2.bitwise_not(mask_bg_p1)
bg_p1 = cv2.bitwise_and(frame, frame, mask=mask_bg_p1)
person_p1 = cv2.bitwise_and(frame, frame, mask=mask_person_p1)

plt.figure()
ax = plt.subplot(231); imshow(frame, title="Frame", new_fig=False)
plt.subplot(232, sharex=ax, sharey=ax), imshow(bg, title="Background - p0", new_fig=False)
plt.subplot(233, sharex=ax, sharey=ax), imshow(person, title="Persona - p0", new_fig=False)
plt.subplot(235, sharex=ax, sharey=ax), imshow(bg_p1, title="Background - p1", new_fig=False)
plt.subplot(236, sharex=ax, sharey=ax), imshow(person_p1, title="Persona - p1", new_fig=False)
plt.suptitle(f'Dilate - SE size = {SE_SIZE}')
plt.show(block=False)

# Se puede ver q no funciona muy bien...

# ----------------------------------------------------------------------------
# --- Prueba 3: Rango + Filtro HSV en el borde -------------------------------
# ----------------------------------------------------------------------------
SE_SIZE = 5
mask_border = cv2.dilate(mask_bg, np.ones((SE_SIZE, SE_SIZE))) - mask_bg
border = cv2.bitwise_and(frame, frame, mask=mask_border)

plt.figure()
ax = plt.subplot(231); imshow(frame, title="Frame", new_fig=False)
plt.subplot(232, sharex=ax, sharey=ax), imshow(bg, title="Background - p0", new_fig=False)
plt.subplot(233, sharex=ax, sharey=ax), imshow(person, title="Persona - p0", new_fig=False)
plt.subplot(235, sharex=ax, sharey=ax), imshow(mask_border, title="Border - Mask", new_fig=False)
plt.subplot(236, sharex=ax, sharey=ax), imshow(border, title="Border", new_fig=False)
plt.show(block=False)

# Aplico filtro HSV al borde solamente
delta_border = np.array([20.0, 180.0, 180.0])
lower_limmit = np.clip(bg_color_HSV - delta_border, 0, 255)
upper_limmit = np.clip(bg_color_HSV + delta_border, 0, 255)
mask_ls = cv2.inRange(frame_hsv, lower_limmit, upper_limmit)
mask_border_ls = cv2.bitwise_and(mask_border, mask_border, mask=mask_ls)
border_ls = cv2.bitwise_and(frame, frame, mask=mask_border_ls)

plt.figure()
ax = plt.subplot(221); imshow(mask_border, title="Border - Mask", new_fig=False)
plt.subplot(222, sharex=ax, sharey=ax), imshow(border, title="Border", new_fig=False)
plt.subplot(223, sharex=ax, sharey=ax), imshow(mask_border_ls, title="Border - Mask - Low Selection", new_fig=False)
plt.subplot(224, sharex=ax, sharey=ax), imshow(border_ls, title="Border - Low Selection", new_fig=False)
plt.show(block=False)

plt.figure()
ax = plt.subplot(231); imshow(mask_person, title="Mascara persona", new_fig=False)
plt.subplot(232, sharex=ax, sharey=ax); imshow(mask_border, title="Border - Mask", new_fig=False)
plt.subplot(233, sharex=ax, sharey=ax), imshow(mask_border_ls, title="Border - Mask - Low Selection", new_fig=False)
plt.subplot(234, sharex=ax, sharey=ax), imshow(person, title="Persona", new_fig=False)
plt.subplot(235, sharex=ax, sharey=ax), imshow(border, title="Border", new_fig=False)
plt.subplot(236, sharex=ax, sharey=ax), imshow(border_ls, title="Border - Low Selection", new_fig=False)
plt.show(block=False)

# Genero mascaras finales 
mask_bg_2 = cv2.bitwise_or(mask_bg, mask_border_ls)
mask_person_2 = cv2.bitwise_not(mask_bg_2)
bg_2 = cv2.bitwise_and(frame, frame, mask=mask_bg_2)
person_2 = cv2.bitwise_and(frame, frame, mask=mask_person_2)

plt.figure()
ax = plt.subplot(221); imshow(mask_person, title="Mascara persona", new_fig=False)
plt.subplot(222, sharex=ax, sharey=ax), imshow(person, title="Persona", new_fig=False)
plt.subplot(223, sharex=ax, sharey=ax), imshow(mask_person_2, title="Mascara persona v2", new_fig=False)
plt.subplot(224, sharex=ax, sharey=ax), imshow(person_2, title="Persona v2", new_fig=False)
plt.show(block=False)

plt.figure()
ax = plt.subplot(231); imshow(frame, title="Frame", new_fig=False)
plt.subplot(232, sharex=ax, sharey=ax), imshow(mask_bg_2, title="Mascara bg v2", new_fig=False)
plt.subplot(233, sharex=ax, sharey=ax), imshow(mask_person_2, title="Mascara persona v2", new_fig=False)
plt.subplot(235, sharex=ax, sharey=ax), imshow(bg_2, title="Background v2", new_fig=False)
plt.subplot(236, sharex=ax, sharey=ax), imshow(person_2, title="Persona v2", new_fig=False)
plt.show(block=False)

# Obersvaciones: Se pudo eliminar varios pixels verdes del borde,sin eliminar bordes de la persona.
#                Igualmmente, aun quedan pixels verdes en el borde...

# --- Genero Frame final ----------------------------------------
bg_2n = cv2.bitwise_and(frame_background, frame_background, mask=mask_bg_2)
res = person_2 + bg_2n

plt.figure()
ax = plt.subplot(121); imshow(person_2, title="Persona", new_fig=False)
plt.subplot(122, sharex=ax, sharey=ax), imshow(bg_2n, title="Fondo", new_fig=False)
plt.show(block=False)

plt.figure()
ax = plt.subplot(221); imshow(person_2, title="Persona", new_fig=False)
plt.subplot(222, sharex=ax, sharey=ax), imshow(bg_2n, title="Fondo", new_fig=False)
plt.subplot(223, sharex=ax, sharey=ax), imshow(res, title="Frame Final", new_fig=False)
plt.show(block=False)

imshow(res, title="Frame Final")


# ------------------------------------------------------------------------------------------------
# --- Prueba 4: Rango + Filtro HSV en el borde + Filtro PB sobre el borde en imagen completa -------------------------------
# ------------------------------------------------------------------------------------------------
SE_BORDER_FULL_SIZE = 3
FILTER_PB_KERNEL_SIZE = 3
FILTER_PB_SIGMA = 0

border_mask = cv2.dilate(mask_bg_2, np.ones((SE_BORDER_FULL_SIZE, SE_BORDER_FULL_SIZE))) - cv2.erode(mask_bg_2, np.ones((SE_BORDER_FULL_SIZE, SE_BORDER_FULL_SIZE)))    # Mascara del borde de la persona/borde
border_mask_not = cv2.bitwise_not(border_mask)

res_blurred = cv2.GaussianBlur(res, (FILTER_PB_KERNEL_SIZE, FILTER_PB_KERNEL_SIZE), FILTER_PB_SIGMA)
res_p1 = cv2.bitwise_and(res_blurred, res_blurred, mask=border_mask)
res_p2 = cv2.bitwise_and(res, res, mask=border_mask_not)
res_v2 = res_p1 + res_p2

# --- Visualizo --------------------------------------------------------------
# Mascaras
plt.figure()
ax = plt.subplot(121); imshow(border_mask, title="border_mask", new_fig=False)
plt.subplot(122, sharex=ax, sharey=ax), imshow(border_mask_not, title="border_mask_not", new_fig=False)
plt.show(block=False)

# Blurred vs not blurred
plt.figure()
ax = plt.subplot(121); imshow(res, title="res", new_fig=False)
plt.subplot(122, sharex=ax, sharey=ax), imshow(res_blurred, title="res_blurred", new_fig=False)
plt.show(block=False)

# Resultado de aplicar mascaras
plt.figure()
ax = plt.subplot(121); imshow(res_p1, title="res_p1", new_fig=False)
plt.subplot(122, sharex=ax, sharey=ax), imshow(res_p2, title="res_p2", new_fig=False)
plt.show(block=False)

aux = cv2.bitwise_and(res, res, mask=border_mask)
plt.figure()
ax = plt.subplot(121); imshow(res_p1, title="Borde con borrosidad", new_fig=False)
plt.subplot(122, sharex=ax, sharey=ax), imshow(aux, title="Borde sin borrosidad", new_fig=False)
plt.show(block=False)

# Comparo resultados finales
plt.figure()
ax = plt.subplot(121); imshow(res, title="Frame Final v1", new_fig=False)
plt.subplot(122, sharex=ax, sharey=ax), imshow(res_v2, title="Frame Final v2", new_fig=False)
plt.show(block=False)

# Check diferencias de pixels entre ambos resultados
auxi = res==res_v2  # Analiza independientemente cada plano
x = np.all(auxi,2)  # Asigno TRUE solo si los 3 planos tienen TRUE
imshow(x, title="Diferencias entre res y res_v2")


# ------------------------------------------------------------------------------------------------
# --- SOMBRA -------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
cap = cv2.VideoCapture(video_person["path"])        # Abro el video
ret, frame = cap.read()                             # Obtengo 1 frame
cap.release()                                       # Cierro el video

frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
frame_hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)              

plt.figure()
ax = plt.subplot(121); imshow(frame, title="Frame 1 - RGB", new_fig=False)
plt.subplot(122, sharex=ax, sharey=ax), imshow(frame_hsv, title="Frame 1 - HSV", new_fig=False)
plt.show(block=False)

SHADOW_COLOR_HSV = np.array([59, 245, 175])    # Por inspeccion, llego a este valor

# --- Obtengo mascara de la sombra: Umbralado + rango ------------------------------------
delta_shadow = np.array([10.0, 70.0, 70.0])
lower_limmit = np.clip(SHADOW_COLOR_HSV - delta_shadow, 0, 255)
upper_limmit = np.clip(SHADOW_COLOR_HSV + delta_shadow, 0, 255)
mask_shadow = cv2.inRange(frame_hsv, lower_limmit, upper_limmit)
mask_shadow_not = cv2.bitwise_not(mask_shadow)
shadow = cv2.bitwise_and(frame, frame, mask=mask_shadow)
shadow_not = cv2.bitwise_and(frame, frame, mask=mask_shadow_not)

plt.figure()
ax = plt.subplot(121); imshow(frame, title="Frame 1 - RGB", new_fig=False)
plt.subplot(122, sharex=ax, sharey=ax), imshow(mask_shadow, title="Mascara shadow", new_fig=False)
plt.show(block=False)

plt.figure()
ax = plt.subplot(231); imshow(frame, title="Frame", new_fig=False)
plt.subplot(232, sharex=ax, sharey=ax), imshow(mask_shadow, title="Mascara shadow", new_fig=False)
plt.subplot(233, sharex=ax, sharey=ax), imshow(mask_shadow_not, title="Mascara shadow NOT", new_fig=False)
plt.subplot(235, sharex=ax, sharey=ax), imshow(shadow, title="shadow", new_fig=False)
plt.subplot(236, sharex=ax, sharey=ax), imshow(shadow_not, title="shadow NOT", new_fig=False)
plt.suptitle(f'SHADOW_COLOR_HSV = {SHADOW_COLOR_HSV} | delta = {delta_shadow}')
plt.show(block=False)

# --- Aplico Morfología para mejorar la máscara ------------------------------------
# Apertura y clausura para remover huecos y puntos aislados.
SE_SIZE = 3
mask_shadow_v2 = cv2.morphologyEx(mask_shadow, cv2.MORPH_OPEN, np.ones((SE_SIZE, SE_SIZE)))
mask_shadow_v2 = cv2.morphologyEx(mask_shadow_v2, cv2.MORPH_CLOSE, np.ones((SE_SIZE, SE_SIZE)))

mask_shadow_not_v2 = cv2.bitwise_not(mask_shadow_v2)
shadow_v2 = cv2.bitwise_and(frame, frame, mask=mask_shadow_v2)
shadow_not_v2 = cv2.bitwise_and(frame, frame, mask=mask_shadow_not_v2)

plt.figure()
ax = plt.subplot(121); imshow(mask_shadow, title="Mascara shadow", new_fig=False)
plt.subplot(122, sharex=ax, sharey=ax), imshow(mask_shadow_v2, title="Mascara shadow + Morfologia", new_fig=False)
plt.show(block=False)

plt.figure()
ax = plt.subplot(121); imshow(frame, title="Frame 1 - RGB", new_fig=False)
plt.subplot(122, sharex=ax, sharey=ax), imshow(mask_shadow_v2, title="Mascara shadow + Morfologia", new_fig=False)
plt.show(block=False)

plt.figure()
ax = plt.subplot(231); imshow(frame, title="Frame", new_fig=False)
plt.subplot(232, sharex=ax, sharey=ax), imshow(mask_shadow_v2, title="Mascara shadow + Morfologia", new_fig=False)
plt.subplot(233, sharex=ax, sharey=ax), imshow(mask_shadow_not_v2, title="Mascara shadow  + Morfologia NOT", new_fig=False)
plt.subplot(235, sharex=ax, sharey=ax), imshow(shadow_v2, title="shadow v2", new_fig=False)
plt.subplot(236, sharex=ax, sharey=ax), imshow(shadow_not_v2, title="shadow v2 NOT", new_fig=False)
plt.show(block=False)

# --- Genero el frame final ------------------------------------
res_v3_shadow = cv2.bitwise_and(res_v2, res_v2, mask=mask_shadow_v2)
res_v3 = cv2.bitwise_and(res_v2, res_v2, mask=mask_shadow_not_v2)

plt.figure()
ax = plt.subplot(121); imshow(res_v3_shadow, title="Parte de la sombra", new_fig=False)
plt.subplot(122, sharex=ax, sharey=ax), imshow(res_v3, title="Frame final con sombra negra", new_fig=False)
plt.show(block=False)

# --- Mejoramiento: Resto una suma fija ---------------------------------------------------------------
delta_sh = [40, 40, 40]
res_v4_shadow = np.clip(res_v3_shadow - delta_sh, 0, 255)
res_v4 = res_v3 + res_v4_shadow

plt.figure()
ax = plt.subplot(121); imshow(res_v3, title="Sombra negra", new_fig=False)
plt.subplot(122, sharex=ax, sharey=ax), imshow(res_v4, title="Sombra restando cantidad fija", new_fig=False)
plt.show(block=False)

# --- Mejoramiento: Resto una suma fija multiplicada por la mascara + blur ----------------------------
np.unique(mask_shadow_v2)
mask_shadow_v2_blur = cv2.GaussianBlur(mask_shadow_v2/255, (3, 3), 0)
np.unique(mask_shadow_v2_blur)

plt.figure()
ax = plt.subplot(121); imshow(mask_shadow_v2, title="Mascara shadow + Morfologia", new_fig=False)
plt.subplot(122, sharex=ax, sharey=ax), imshow(mask_shadow_v2_blur, title="Mascara shadow + Morfologia + Blurred", new_fig=False)
plt.show(block=False)

res_v5 = np.empty_like(res_v3)
for n in range(3):
    res_v5[:, :, n] = np.clip(res_v4[:, :, n] - mask_shadow_v2_blur*40, 0, 255)

imshow(res_v5)

plt.figure()
ax = plt.subplot(121); imshow(res_v4, title="Sombra restando cantidad fija", new_fig=False)
plt.subplot(122, sharex=ax, sharey=ax), imshow(res_v5, title="Sombra restando cantidad fija + blur", new_fig=False)
plt.show(block=False)



