# sala_de_control.py

import time
import random

# --- Simulación de la Sala de Control ---
def inicializar_supervision():
    print("// ITIEL: Iniciando supervisión del robot...")

def cerrar_supervision():
    print("// ITIEL: Cerrando supervisión del robot.")

def informar_sala(mensaje):
    print(f"// ITIEL: {mensaje}")

def informar_ubicacion(ubicacion):
    print(f"// ITIEL: Ubicación actual del robot: {ubicacion}")

def informar_charco(ubicacion_charco):
    print(f"// ITIEL: ¡Peligro! Charco detectado en: {ubicacion_charco}")

# --- Simulación del Robot ---
class RobotPaseador:
    def __init__(self):
        self.ubicacion_actual = "casa"
        self.mapa_area = self._cargar_mapa()
        self.bateria = 100
        self.nivel_minimo_bateria = 20
        self.nivel_requerido_bateria = 90
        self.tiene_bolsitas = True
        self.tiempo_total_paseo = 60  # minutos
        self.margen_seguridad_regreso = 10  # minutos
        self.tiempo_inicio_paseo = 0

    def _cargar_mapa(self):
        # Simulación de carga de mapa
        return ["punto_a", "punto_b", "punto_c", "charco_1", "punto_d", "casa"]

    def obtener_ubicacion_actual(self):
        return self.ubicacion_actual

    def inicializar_robot(self):
        informar_sala("Cargando mapa del área...")
        informar_sala(f"Ubicación actual: {self.obtener_ubicacion_actual()}")
        if self.bateria < self.nivel_minimo_bateria:
            informar_sala("Batería baja. Cargando...")
            while self.bateria < self.nivel_requerido_bateria:
                self.bateria += 10
                informar_sala(f"Batería al {self.bateria}%")
                time.sleep(1)  # Simular carga
        if not self.tiene_bolsitas:
            informar_sala("No hay bolsitas. Imposible pasear.")
            return "FALLO"
        informar_sala("Robot listo para pasear.")
        return "EXITO"

    def planificar_ruta(self, tiempo_disponible):
        informar_sala("Planificando ruta...")
        # Simulación de generación de ruta aleatoria evitando (si es posible) charcos
        ruta_posible = [p for p in self.mapa_area if "charco" not in p and p != self.ubicacion_actual and p != "casa"]
        ruta = [self.ubicacion_actual] + random.sample(ruta_posible, min(3, len(ruta_posible))) + ["casa"]
        informar_sala(f"Ruta planificada: {ruta}")
        return ruta

    def evitar_charco(self, ubicacion_charco):
        informar_sala(f"Evitando charco en: {ubicacion_charco}")
        # Simulación de cálculo y seguimiento de trayectoria alternativa
        informar_sala("Calculando trayectoria alternativa...")
        time.sleep(2)
        informar_sala("Siguiendo trayectoria alternativa...")
        time.sleep(3)

    def recoger_excremento(self):
        informar_sala("¡El perro hizo sus necesidades!")
        informar_sala("Localizando excremento...")
        informar_sala("Desplegando bolsa...")
        informar_sala("Accionando brazo recolector, llevándolo al excremento, barriéndolo al recolector, llenando bolsa...")
        informar_sala("Sellando bolsa...")
        informar_sala("Almacenando bolsa de forma segura...")
        informar_sala("Excremento recogido.")

    def desinfectar_orina(self, ubicacion_orina):
        informar_sala(f"¡El perro orinó en: {ubicacion_orina}!")
        informar_sala("Localizando orina...")
        informar_sala("Desplegando manguera con agua y detergente...")
        informar_sala("Desinfectando zona contagiada...")
        informar_sala("Zona desinfectada.")

    def tiempo_restante_regresar(self):
        tiempo_transcurrido = time.time() - self.tiempo_inicio_paseo
        tiempo_restante_total = self.tiempo_total_paseo * 60 - tiempo_transcurrido
        return tiempo_restante_total / 60  # en minutos

    def pasear_perro(self, ruta):
        informar_sala("Iniciando paseo...")
        self.tiempo_inicio_paseo = time.time()
        for punto in ruta:
            informar_ubicacion(self.ubicacion_actual)
            informar_sala(f"Moviendo a: {punto}")
            time.sleep(random.uniform(1, 3))  # Simular movimiento

            if "charco" in punto:
                informar_charco(punto)
                self.evitar_charco(punto)

            # Simulación de las necesidades del perro
            if random.random() < 0.2:  # 20% de probabilidad de hacer excremento
                self.recoger_excremento()
            elif random.random() < 0.1: # 10% de probabilidad de orinar
                ubicacion_orina = self.ubicacion_actual
                self.desinfectar_orina(ubicacion_orina)

            self.ubicacion_actual = punto

            if self.tiempo_restante_regresar() < self.margen_seguridad_regreso:
                informar_sala("Tiempo de regreso cercano. Iniciando retorno.")
                break

        informar_sala("Paseo completado.")

    def regresar_a_casa(self):
        informar_sala("Regresando a casa...")
        ruta_regreso = self._calcular_ruta_regreso()
        for punto in ruta_regreso:
            informar_ubicacion(self.ubicacion_actual)
            informar_sala(f"Moviendo a: {punto}")
            time.sleep(random.uniform(1, 2))
            self.ubicacion_actual = punto
            if self.ubicacion_actual == "casa":
                break
        informar_sala("Robot ha regresado a casa a tiempo.")

    def _calcular_ruta_regreso(self):
        # Simulación de cálculo de ruta óptima a casa
        ruta = [self.ubicacion_actual]
        if self.ubicacion_actual != "casa":
            ruta.append("casa")
        return ruta

# --- Programa Principal ---
if __name__ == "__main__":
    robot = RobotPaseador()
    inicializar_supervision()

    if robot.inicializar_robot() == "EXITO":
        tiempo_para_paseo = robot.tiempo_total_paseo  # Obtener tiempo disponible
        ruta_planificada = robot.planificar_ruta(tiempo_para_paseo)
        if ruta_planificada:
            robot.pasear_perro(ruta_planificada)
            robot.regresar_a_casa()
        else:
            informar_sala("No se pudo planificar una ruta válida.")

    cerrar_supervision()