import requests,zipfile, io, csv
#Intento la descarga del archivo binario
r = requests.get ('https://ssl.smn.gob.ar/dpd/zipopendata.php?dato=tiepre')
#Muestro el código de respuesta del servidor
print("Código de respuesta:", r.status_code)
#Extraigo el contenido del zip en una variable
z = zipfile.ZipFile(io.BytesIO(r.content))
#Listo los archivos extraídos
file_list = z.namelist()
print("Archivos contenidos:")
print(file_list)
#Me quedo con el archivo que necesite, en este caso el primero y único
first_file = file_list[0]
#Guardo el contenido de ese archivo en otra variable
first_file_content = z.read(first_file)
#Decodifico el contenido binario en una variable str
csv_data_str = first_file_content.decode('ansi')
#Convierto el str en una lista de elementos str, una por cada renglon
lines = csv_data_str.strip().split(' / \r\n')
#Genero un archivo reader a partir del objeto iterable lista
reader = csv.reader(lines, delimiter=';')
#Defino el elemento a buscar
city = "Rosario"
#Itero la variable reader para encontrar el elemento buscado en la primer columna
for row in reader:
    row[0] = row[0].strip()
    if row[0] == city:
        print(row)
        exit()