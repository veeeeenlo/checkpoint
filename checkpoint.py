import pickle     #librieria para convertir objetos a bytes
import os         #libreria para interactuar con los archivos
import time       #libreria para manejar pausas

FILENAME = "respaldo.pkl"       #nombre del archivo donde se guardara la info


def progreso(datos):        #funcion para guardar los datos
    with open(FILENAME, "wb") as f:
        pickle.dump(datos, f)
    print(f"\n[Checkpoint] Progreso actual: {datos['iteracion']}")


def cargar_progreso():      #funcion para revisar si existe archivo anterior y cargarlo
    if os.path.exists(FILENAME):          #si el archivo existe, se abre
        with open(FILENAME, "rb") as f:         #se recupera la info
            return pickle.load(f)               #regresa la info al programa
    return {"iteracion": 0}               #si no hay nada guardado, se devuelve el estado incial

#se recupera el progreso anterior
estado = cargar_progreso()
inicio = estado["iteracion"]

print(f"Iniciando desde la iteracion: {inicio}")

try:
    for i in range(inicio, 50):       #definimos el ultimo numero a iterar
        estado["iteracion"] = i           #actualizamos la info en la memoria

        print(f"Procesando {i}...", end="\r")     #mostramos el progreso
        time.sleep(0.3)
        if i % 5 == 0:              #checkpoint actual, guardamos cada 10 iteraciones
            progreso(estado)

except KeyboardInterrupt:              #si el usuario termina el programa, guarda la info
    print("\nPrograma pausado por el usuario.")
    progreso(estado)