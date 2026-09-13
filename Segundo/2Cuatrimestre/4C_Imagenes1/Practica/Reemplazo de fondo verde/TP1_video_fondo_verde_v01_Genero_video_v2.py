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

# ----------------------------------------------------------------------------
# --- Genero Video -----------------------------------------------------------
# ----------------------------------------------------------------------------
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_v2.avi', fourcc, 20.0, (video_person["width"], video_person["height"]))
cap_person = cv2.VideoCapture(video_person["path"])                  # Abro el video
cap_background = cv2.VideoCapture(video_background["path"])                # Abro el video

# Proceso 
BG_REPLACE_HSV = np.array([[[ 59, 247, 255]]], dtype=np.uint8)
DELTA_BG = np.array([10.0, 150.0, 150.0])
DELTA_BORDER = np.array([20.0, 180.0, 180.0])
SE_DILATE_BORDER_SIZE = 5
SE_BORDER_FULL_SIZE = 3
FILTER_PB_KERNEL_SIZE = 3
FILTER_PB_SIGMA = 0
k = 0
while(cap_person.isOpened()):
    # --- Cargo los frames ------------------------------------------
    ret, frame = cap_person.read()    
    ret_background, frame_background = cap_background.read()    
    if ret==False or ret_background==False:            
        break
    k+=1
    print(f'Procesando frame {k:5d}/{video_person["n_frames"]:5d}')

    # --- Pre-proceso frames -----------------------------------------------------
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)                          # Convierto para poder visualizar bien, de ser necesario.
    frame_background = cv2.cvtColor(frame_background, cv2.COLOR_BGR2RGB)    #
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)                      # Convierto a HSV para procesar

    # --- Paso 1: Umbralado sobre todo el frame -------------------------------------
    lower_limmit = np.clip(BG_REPLACE_HSV - DELTA_BG, 0, 255)
    upper_limmit = np.clip(BG_REPLACE_HSV + DELTA_BG, 0, 255)
    mask_bg = cv2.inRange(frame_hsv, lower_limmit, upper_limmit)
    mask_person = cv2.bitwise_not(mask_bg)
    bg = cv2.bitwise_and(frame, frame, mask=mask_bg)
    person = cv2.bitwise_and(frame, frame, mask=mask_person)

    # --- Paso 2: Umbralado sobre el borde ------------------------------------------
    # Obtengo el borde
    mask_border = cv2.dilate(mask_bg, np.ones((SE_DILATE_BORDER_SIZE, SE_DILATE_BORDER_SIZE))) - mask_bg
    border = cv2.bitwise_and(frame, frame, mask=mask_border)

    # Aplico filtro HSV al borde solamente
    lower_limmit = np.clip(BG_REPLACE_HSV - DELTA_BORDER, 0, 255)
    upper_limmit = np.clip(BG_REPLACE_HSV + DELTA_BORDER, 0, 255)
    mask_ls = cv2.inRange(frame_hsv, lower_limmit, upper_limmit)
    mask_border_ls = cv2.bitwise_and(mask_border, mask_border, mask=mask_ls)
    border_ls = cv2.bitwise_and(frame, frame, mask=mask_border_ls)

    # Genero mascaras finales 
    mask_bg_2 = cv2.bitwise_or(mask_bg, mask_border_ls)
    mask_person_2 = cv2.bitwise_not(mask_bg_2)
    bg_2 = cv2.bitwise_and(frame, frame, mask=mask_bg_2)
    person_2 = cv2.bitwise_and(frame, frame, mask=mask_person_2)

    # --- Paso 3: Genero Frame de salida -----------------------------------
    bg_2n = cv2.bitwise_and(frame_background, frame_background, mask=mask_bg_2)
    res = person_2 + bg_2n
    res = cv2.cvtColor(res, cv2.COLOR_RGB2BGR)

    # --- Paso 4: Agrego borrosidad solo en el borde de la persona --------------------------
    border_mask = cv2.dilate(mask_bg_2, np.ones((SE_BORDER_FULL_SIZE, SE_BORDER_FULL_SIZE))) - cv2.erode(mask_bg_2, np.ones((SE_BORDER_FULL_SIZE, SE_BORDER_FULL_SIZE)))    # Mascara del borde de la persona/borde
    border_mask_not = cv2.bitwise_not(border_mask)

    res_blurred = cv2.GaussianBlur(res, (FILTER_PB_KERNEL_SIZE, FILTER_PB_KERNEL_SIZE), FILTER_PB_SIGMA)
    res_p1 = cv2.bitwise_and(res_blurred, res_blurred, mask=border_mask)
    res_p2 = cv2.bitwise_and(res, res, mask=border_mask_not)
    res = res_p1 + res_p2

    # --- Paso 5: Grabo frame en video -------------------------------------------
    out.write(res)

cap_person.release()
cap_background.release()
out.release()

