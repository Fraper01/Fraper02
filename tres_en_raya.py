# tres en raya python
from ollama import chat
import os

class tres_en_raya:
    def __init__(self):
        #Crear el tablero del Juego
        self.tablero = [
                        [' ', ' ', ' '],  # Fila 0
                        [' ', ' ', ' '],  # Fila 1
                        [' ', ' ', ' ']   # Fila 2
                    ]
        self.jugador = "X"
        self.computa = "O"
        self.modelo = "llama3"

    def limpiar_pantalla(self):
        os.system("cls")
    
    def mostrar_tablero(self):
        # Mostramos el tablero
        self.limpiar_pantalla()
        print("\n    Tres en Raya vs IA\n")
        print("    +-----+-----+-----+")    
        print(f"    |  {self.tablero[0][0]}  |  {self.tablero[0][1]}  |  {self.tablero[0][2]}  |  Opciones 1 ó 2 ó 3 para esta fila")
        print("    +-----+-----+-----+")    
        print(f"    |  {self.tablero[1][0]}  |  {self.tablero[1][1]}  |  {self.tablero[1][2]}  |  Opciones 4 ó 5 ó 6 para esta fila")
        print("    +-----+-----+-----+")
        print(f"    |  {self.tablero[2][0]}  |  {self.tablero[2][1]}  |  {self.tablero[2][2]}  |  Opciones 7 ó 8 ó 9 para esta fila")
        print("    +-----+-----+-----+")    
        print("\n")

    def revisar_ganador_horizontal(self, jugador)-> bool:
        #Comprobar si hay un ganador horizontal
        for i in range(0, 3, 6):
            if self.tablero[i] == self.tablero[i+1] == self.tablero[i+2] == "jugador":
                return True
            return False

    def revisar_ganador_vertical(self, jugador)-> bool:
        #Comprobar si hay un ganador vertical
        for i in range(0, 1, 2):
            if self.tablero[i] == self.tablero[i+3] == self.tablero[i+6] == "jugador":
                return True
            return False

    def revisar_ganador_diagonal(self, jugador)-> bool:
        #Comprobar si hay un ganador diagonal
        for i in range(0, 1):
            if self.tablero[i] == self.tablero[i+4] == self.tablero[i+8] == "jugador":
                return True
            return False
        
    def revisar_ganador(self, jugador)-> bool:
        #verificar si hay un ganador horizontal, vertical o diagonal
        return (self.revisar_ganador_horizontal(jugador) or self.revisar_ganador_vertical(jugador) or self.revisar_ganador_diagonal(jugador))

    def revisar_empate(self)-> bool:
        #Comprobar si hay un empate
        for i in self.tablero:
            if i == " ":
                return False
        return True
    
    def jugada_valida(self, posicion)-> bool:
        #Comprobar si la jugada es valida
        if posicion < 1 or posicion > 9:
            return False
        if self.tablero[posicion] != " ":
            return False
        return True
    
    def obtener_jugada_ia(self)-> int:
        #Obtener la jugada de la IA
        print(f"✨La IA {self.modelo} esta pensando...✨")
        tablero_texto = (" ".join(self.tablero)).replace(" ", "_")
        prompt = f"Estamos Jugando tres en Raya, a ti te corresponde la 'O' indicame tu desicion con un valor valido entre 0 y 8 Juega en la posicion {tablero_texto}"
        respuesta = chat(self.modelo,prompt).get_response()
        repuesta = respuesta.strip()
        respuesta = respuesta.replace(" ", "").replace("_", "")
        #Limpiar la respuesta de la IA 
        #Convertir la respuesta en un entero
        try:
            posicion = int(respuesta)
            if self.jugada_valida(posicion):
                return posicion
        except ValueError:
            print("La IA no ha jugado bien, elige una posicion valida")
            #Si la IA no juega bien, elegir una posicion valida
            for i in range(0, 9):
                if self.tablero[i] == " ":
                    return i    
            pass
           
                
    def jugar_ia(self, posicion):
        #Jugar contra la IA
        posicion = self.obtener_jugada_ia()
        if self.jugada_valida(posicion):
            self.tablero[posicion] = self.jugador
            if self.revisar_ganador(self.jugador):
                print("Ganaste!")
                return True
            elif self.revisar_empate():
                print("Empate!")
                return True
            else:
                #Jugar IA
                posicion_ia = chat(f"Juega en la posicion {self.tablero}")
                self.tablero[posicion_ia] = self.computa
                if self.revisar_ganador(self.computa):
                    print("Perdiste!")
                    return True
                elif self.revisar_empate():
                    print("Empate!")
                    return True
        else:
            print("Jugada no valida")
            return False    

    def jugar(self):    
        #Jugar el juego
        while True:
            self.mostrar_tablero()
            try:
                posicion = int(input("Tu Turno - Elige una posicion entre 1 y 9: "))
                if self.jugada_valida(posicion):
                    self.tablero[posicion] = self.jugador
                    if self.revisar_ganador(self.jugador):
                        print("Ganaste!")
                        break
                    elif self.revisar_empate():
                        print("Empate!")
                        break
                else:
                    print("Jugada no valida. Intenta de nuevo")
                    continue            
                if self.jugar_ia(posicion):
                    break
                else:
                    print("Jugada no valida. Intenta de nuevo")
                    continue
            except KeyboardInterrupt:
                    break                
            except ValueError:
                print("Posicion no valida, elige un numero entre 0 y 8")    
                continue
        self.mostrar_tablero()

if __name__ == "__main__":
    tresEnRaya = tres_en_raya()
    try:
        tresEnRaya.jugar()
        tresEnRaya.mostrar_tablero()
    except KeyboardInterrupt:
        print("\nJuego terminado por el usuario")
    print("Gracias por jugar")
    print("Fin del juego")
    print("Hasta la proxima")
    print("Adios")


