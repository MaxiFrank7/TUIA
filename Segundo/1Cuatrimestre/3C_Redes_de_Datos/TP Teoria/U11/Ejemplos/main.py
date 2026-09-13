import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Configura tus credenciales
client_id = '093a2e8901a04ee28ff6096e6a22b636'
client_secret = '9ead7f4fc91541c29d97fa7dc2225993'
redirect_uri = 'http://localhost:8888/callback'

# Inicia la autenticación de Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='user-library-read user-read-playback-state user-modify-playback-state'))

# Obtén la información del usuario
user_info = sp.me()
print(f'Bienvenido, {user_info["display_name"]}!')

# Obtiene los dispositivos activos
devices = sp.devices()['devices']

# Imprime los dispositivos disponibles
print("Dispositivos activos:")
for i, device in enumerate(devices, start=1):
    print(f"{i}. {device['name']} ({device['type']})")

# Solicita al usuario que seleccione un dispositivo
selected_device_index = int(input("Ingrese el número del dispositivo en el que desea reproducir la canción: "))

# Verifica si el índice seleccionado es válido
if 1 <= selected_device_index <= len(devices):
    selected_device_id = devices[selected_device_index - 1]['id']

    # Obtén las playlists del usuario
    playlists = sp.current_user_playlists()['items']
    print("\nTus playlists:")
    for i, playlist in enumerate(playlists, start=1):
        print(f"{i}. {playlist['name']} (Total: {playlist['tracks']['total']} canciones)")

    # Solicita al usuario seleccionar una playlist
    playlist_index = int(input("\nIngrese el número de la playlist que desea usar: "))
    if 1 <= playlist_index <= len(playlists):
        playlist_id = playlists[playlist_index - 1]['id']
        playlist_name = playlists[playlist_index - 1]['name']
        print(f"\nHas seleccionado la playlist: {playlist_name}")

        # Inicializa el contador de canciones
        contador_canciones = 0

        # Parámetros para la paginación
        limit = 100
        offset = 0
        canciones = []

        print(f'\nCanciones en la playlist "{playlist_name}":')
        while True:
            playlist_tracks = sp.playlist_tracks(playlist_id, limit=limit, offset=offset)

            for track in playlist_tracks['items']:
                # Incrementa el contador de canciones
                contador_canciones += 1

                # Agrega la canción a la lista
                canciones.append({
                    'numero': contador_canciones,
                    'nombre': track['track']['name'],
                    'artista': track['track']['artists'][0]['name'],
                    'uri': track['track']['uri']
                })

                # Imprime información de la canción
                print(f'{contador_canciones}. {track["track"]["name"]} - {track["track"]["artists"][0]["name"]}')

            # Actualiza el offset para la próxima página
            offset += limit

            # Verifica si hay más páginas
            if not playlist_tracks['next']:
                break

        # Solicita al usuario que seleccione una canción
        metodo_seleccion = input("\n¿Desea buscar por nombre (N) o por número (núm)? ").strip().lower()

        cancion_encontrada = None
        if metodo_seleccion == 'n':
            nombre_cancion_buscada = input("Ingrese el nombre de la canción que desea reproducir (sin distinguir mayúsculas o minúsculas): ").strip().lower()
            for cancion in canciones:
                if nombre_cancion_buscada == cancion['nombre'].lower():
                    cancion_encontrada = cancion['uri']
                    break
        else:
            numero_cancion = int(input("Ingrese el número de la canción que desea reproducir: "))
            if 1 <= numero_cancion <= len(canciones):
                cancion_encontrada = canciones[numero_cancion - 1]['uri']

        # Reproduce la canción encontrada en el dispositivo seleccionado
        if cancion_encontrada:
            print("Reproduciendo canción seleccionada en el dispositivo ...")
            sp.start_playback(uris=[cancion_encontrada], device_id=selected_device_id)
        else:
            print("La canción no se encontró.")
    else:
        print("Número de playlist no válido.")
else:
    print("Número de dispositivo no válido.")
