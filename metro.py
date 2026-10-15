# Estructura de datos del Metro de Caracas (Ejemplo ampliado con Linea 1 y Linea 2)
metro_caracas = {
    "Linea 1": {
        "Propatria": {
            "estaciones_siguientes": ["Pérez Bonalde"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Pérez Bonalde": {
            "estaciones_siguientes": ["Propatria", "Plaza Sucre"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Plaza Sucre": {
            "estaciones_siguientes": ["Pérez Bonalde", "Gato Negro"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Gato Negro": {
            "estaciones_siguientes": ["Plaza Sucre", "Agua Salud"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Agua Salud": {
            "estaciones_siguientes": ["Gato Negro", "Caño Amarillo"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Caño Amarillo": {
            "estaciones_siguientes": ["Agua Salud", "Capitolio"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Capitolio": {
            "estaciones_siguientes": ["Caño Amarillo", "Sociedad"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Hoyada": {
            "estaciones_siguientes": ["Capitolio", "Parque Carabobo"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Parque Carabobo": {
            "estaciones_siguientes": ["Hoyada", "Bellas Artes"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Bellas Artes": {
            "estaciones_siguientes": ["Parque Carabobo", "Bellas Colegio de Ingenieros"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Colegio de Ingenieros": {
            "estaciones_siguientes": ["Bellas Artes", "Plaza Venezuela"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Plaza Venezuela": {
            "estaciones_siguientes": ["Colegio de Ingenieros", "Sabana Grande"],
            "tiempo_siguiente": 2,
            "transbordo": "Linea 3" #Conexion con Linea 3
        },
        "Sabana Grande": {
            "estaciones_siguientes": ["Cole", "Sabana Grande"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Chacaito": {
            "estaciones_siguientes": ["Sabana Grande", "Chacao"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Chacao": {
            "estaciones_siguientes": ["Chacaito", "Altamira"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Altamira": {
            "estaciones_siguientes": ["Chacao", "Miranda"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Miranda": {
            "estaciones_siguientes": ["Altamira", "Los dos Caminos"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Los dos Caminos": {
            "estaciones_siguientes": ["Miranda", "Los Cortijos"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Los Cortijos": {
            "estaciones_siguientes": ["Los dos Caminos", "La California"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "La California": {
            "estaciones_siguientes": ["Los Cortijos", "Petare"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Petare": {
            "estaciones_siguientes": ["La California","Palo Verde"],
            "tiempo_siguiente": 2,
            "transbordo": None
                 
        }
    },
    "Linea 2": {
        "El Silencio": {
            "estaciones_siguientes": ["Capuchinos"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Capuchinos": {
            "estaciones_siguientes": ["El Silencio", "Maternidad"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Maternidad": {
            "estaciones_siguientes": ["Capuchinos", "Artigas"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Artigas": {
            "estaciones_siguientes": ["Maternidad", "La Paz"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "La Paz": {
            "estaciones_siguientes": ["Artigas", "La Yaguara"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "La Yaguara": {
            "estaciones_siguientes": ["La Paz", "Carapita"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Carapita": {
            "estaciones_siguientes": ["La Yaguara", "Antímano"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Antímano": {
            "estaciones_siguientes": ["Carapita", "Muelle"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Muelle": {
            "estaciones_siguientes": ["Antímano", "Ruiz Pineda"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Ruiz Pineda": {
            "estaciones_siguientes": ["Muelle", "Las Adjuntas"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Las Adjuntas": {
            "estaciones_siguientes": ["Ruiz Pineda"],
            "tiempo_siguiente": 2,
            "transbordo": None
        }
    },
    "Linea 3": {
        "Plaza Venezuela": {
            "estaciones_siguientes": ["Tres Inquietudes", "Cusco"], # Referencia interna o Ciudad Universitaria
            "tiempo_siguiente": 2,
            "transbordo": "Linea 1"
        },
        "Ciudad Universitaria": {
            "estaciones_siguientes": ["Plaza Venezuela", "Los Símbolos"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Los Símbolos": {
            "estaciones_siguientes": ["Ciudad Universitaria", "La Bandera"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "La Bandera": {
            "estaciones_siguientes": ["Los Símbolos", "El Valle"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "El Valle": {
            "estaciones_siguientes": ["La Bandera", "Coche"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "Coche": {
            "estaciones_siguientes": ["El Valle", "La Rinconada"],
            "tiempo_siguiente": 2,
            "transbordo": None
        },
        "La Rinconada": {
            "estaciones_siguientes": ["Coche"],
            "tiempo_siguiente": 2,
            "transbordo": None
        }
    }
}
def obtener_todas_las_estaciones():
    """Retorna una lista con los nombres de todas las estaciones disponibles."""
    estaciones = set()
    for linea in metro_caracas.values():
        for est in linea.keys():
            estaciones.add(est)
    return list(estaciones)

def buscar_estacion(nombre_estacion):
    """Busca en qué línea o líneas se encuentra una estación dada."""
    lineas_encontradas = []
    for nombre_linea, datos_linea in metro_caracas.items():
        if nombre_estacion in datos_linea:
            lineas_encontradas.append(nombre_linea)
    return lineas_encontradas

# planificador.py
from metro import metro_caracas, obtener_todas_las_estaciones, buscar_estacion
from collections import deque

def calcular_ruta_optima(origen, destino):
    """
    Calcula la ruta óptima (secuencia de estaciones) usando BFS,
    el tiempo total estimado y el número de estaciones recorridas.
    Maneja también los cambios de línea (transbordos).
    """
    if origen not in obtener_todas_las_estaciones() or destino not in obtener_todas_las_estaciones():
        return None, "Estación de origen o destino no válida.", 0, 0, []

    if origen == destino:
        return [origen], "Estación de origen y destino son la misma.", 0, 1, []

    # Cola para BFS: almacena tuplas (estacion_actual, ruta_hasta_aqui, linea_actual)
    # Buscamos en qué línea está el origen para empezar
    lineas_origen = buscar_estacion(origen)
    
    cola = deque()
    for l in lineas_origen:
        cola.append((origen, [origen], l))

    visitados = set()
    
    while cola:
        estacion_actual, ruta, linea_actual = cola.popleft()

        if estacion_actual == destino:
            # Calcular tiempo y notificaciones de transbordo
            tiempo_total = 0
            transbordos_realizados = []
            
            for i in range(len(ruta) - 1):
                est1 = ruta[i]
                est2 = ruta[i+1]
                # Verificamos el tiempo en la línea actual
                # Si hay cambio de línea en el trayecto:
                tiempo_total += metro_caracas[linea_actual][est1]["tiempo_siguiente"]
                
                # Detectar si pasamos por una estación de transferencia
                if "transbordo" in metro_caracas[linea_actual][est1] and metro_caracas[linea_actual][est1]["transbordo"]:
                    nueva_linea = metro_caracas[linea_actual][est1]["transbordo"]
                    if est2 in metro_caracas.get(nueva_linea, {}):
                        linea_actual = nueva_linea
                        transbordos_realizados.append(f"Cambio a {nueva_linea} en la estación {est1}")

            return ruta, "Ruta calculada con éxito", tiempo_total, len(ruta), transbordos_realizados

        estado_visitado = (estacion_actual, linea_actual)
        if estado_visitado in visitados:
            continue
        visitados.add(estado_visitado)

        # Explorar estaciones siguientes en la misma línea
        datos_estacion = metro_caracas[linea_actual].get(estacion_actual, {})
        vecinos = datos_estacion.get("estaciones_siguientes", [])

        for vecino in vecinos:
            if vecino not in ruta:  # Evitar ciclos
                cola.append((vecino, ruta + [vecino], linea_actual))

        # Explorar transbordos si la estación actual permite cambio de línea
        transbordo_linea = datos_estacion.get("transbordo")
        if transbordo_linea and transbordo_linea in metro_caracas:
            # Si la estación existe en la otra línea, podemos saltar de línea
            if estacion_actual in metro_caracas[transbordo_linea]:
                estado_transbordo = (estacion_actual, transbordo_linea)
                if estado_transbordo not in visitados:
                    # Agregamos a la cola manteniendo la misma ruta pero cambiando la línea activa
                    cola.append((estacion_actual, ruta, transbordo_linea))

    return None, "No se encontró una ruta disponible entre las estaciones.", 0, 0, []

def interfaz_usuario():
    """Interfaz de línea de comandos (CLI) interactiva para el usuario."""
    print("==================================================")
    print("      BIENVENIDO AL SISTEMA DEL METRO DE CARACAS  ")
    print("==================================================")
    
    while True:
        print("\nMenú Principal:")
        print("1. Planificar viaje (Calcular ruta óptima)")
        print("2. Consultar líneas y estaciones")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1-3): ").strip()
        
        if opcion == "1":
            print("\n--- Planificador de Rutas ---")
            origen = input("Ingrese la estación de ORIGEN: ").strip().title()
            destino = input("Ingrese la estación de DESTINO: ").strip().title()
            
            ruta, mensaje, tiempo, num_estaciones, notificaciones = calcular_ruta_optima(origen, destino)
            
            if ruta:
                print(f"\n[ÉXITO] {mensaje}")
                print(f"-> Ruta óptima: {' -> '.join(ruta)}")
                print(f"-> Número total de estaciones recorridas: {num_estaciones}")
                print(f"-> Tiempo total estimado del viaje: {tiempo} minutos")
                
                if notificaciones:
                    print("\n[NOTIFICACIONES DE CAMBIO DE LÍNEA / TRANSBORDOS]:")
                    for notif in notificaciones:
                        print(f"   * {notif}")
                else:
                    print("\n[NOTIFICACIÓN]: No se requieren cambios de línea (Viaje directo).")
            else:
                print(f"\n[ERROR]: {mensaje}")
                
        elif opcion == "2":
            print("\n--- Estaciones y Líneas Disponibles ---")
            for linea, estaciones in metro_caracas.items():
                print(f"\n* {linea}:")
                for est in estaciones.keys():
                    print(f"   - {est}")
                    
        elif opcion == "3":
            print("\n¡Gracias por utilizar el sistema del Metro de Caracas. ¡Buen viaje!")
            break
        else:
            print("\n[ADVERTENCIA]: Opción no válida. Por favor, ingrese 1, 2 o 3.")

if __name__ == "__main__":
    interfaz_usuario()