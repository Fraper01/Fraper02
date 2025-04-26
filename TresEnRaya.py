import ollama
import os

class tres_en_raya:
    def __init__(self):
        #Crear el tablero del juego
        self.tablero =[
            " ", " ", " ", #Fila superior (0,1,2)
            " ", " ", " ", #Fila del medio (3,4,5)
            " ", " ", " " #Fila inferior (6,7,8)
        ]

        #Los jugadores
        self.jugador = "X"
        self.computadora = "O"
        self.modelo ="llama3"

    def limpiar_pantalla(self):
        #Limpiamos la terminal
        os.system("cls")


    def mostrar_tablero(self):
        self.limpiar_pantalla()

        #Mostramos el titulo del juego
        print("\n== TRES EN RAYA vs IA ==\n")

        #Mostramos la guia de numeros para el jugador
        print("     0 | 1 | 2")
        print("     --+---+---")
        print("     3 | 4 | 5")
        print("     --+---+---")
        print("     6 | 7 | 8")

        #Mostramos el tablero actual
        print("\nAsí se ve el juego ahora:\n")
        print(f"       {self.tablero[0]} | {self.tablero[1]} | {self.tablero[2]}")
        print("       --+---+---")
        print(f"       {self.tablero[3]} | {self.tablero[4]} | {self.tablero[5]}")
        print("       --+---+---")
        print(f"       {self.tablero[6]} | {self.tablero[7]} | {self.tablero[8]}")

    #Verificadores horizontales, verticales y diagonales
    def revisar_ganador_horizontal(self, jugador):
        #Revisamos si hay tres simbolos iguales en alguna fila
        #Primera fila
        if(self.tablero[0] == jugador and
           self.tablero[1] == jugador and
           self.tablero[2] == jugador):
            return True
        
        #Segunda fila
        if(self.tablero[3] == jugador and
           self.tablero[4] == jugador and
           self.tablero[5] == jugador):
            return True

        #Tercer fila
        if(self.tablero[6] == jugador and
           self.tablero[7] == jugador and
           self.tablero[8] == jugador):
            return True
        
        return False


    def revisar_ganador_vertical(self, jugador):
        #Revisamos si hay tres simbolos iguales en alguna fila
        #Primera fila
        if(self.tablero[0] == jugador and
           self.tablero[3] == jugador and
           self.tablero[6] == jugador):
            return True
        
        #Segunda fila
        if(self.tablero[1] == jugador and
           self.tablero[4] == jugador and
           self.tablero[7] == jugador):
            return True

        #Tercer fila
        if(self.tablero[2] == jugador and
           self.tablero[5] == jugador and
           self.tablero[8] == jugador):
            return True
        
        return False


    def revisar_ganador_diagonal(self, jugador):
        #Revisamos si hay tres simbolos iguales en alguna fila
        #Primera fila
        if(self.tablero[0] == jugador and
           self.tablero[4] == jugador and
           self.tablero[8] == jugador):
            return True
        
        #Segunda fila
        if(self.tablero[2] == jugador and
           self.tablero[4] == jugador and
           self.tablero[6] == jugador):
            return True


        return False
    

    def hay_ganador(self, jugador):
        #Verificamos ganador, horizontalmente, verticalmente, diagonalmente
        return (self.revisar_ganador_horizontal(jugador) or
                self.revisar_ganador_vertical(jugador) or
                self.revisar_ganador_diagonal(jugador))
    
    def tablero_lleno(self):
        #El tablero esta lleno cuando no hay espacios vacios
        for casilla in self.tablero:
            if casilla == " ":
                return False
        
        return True


    def movimiento_valido(self, posicion):
        #Verificamos que sea de 0 a 8 y por otro lado que la casilla este vacia.
        if posicion < 0 or posicion > 8:
            return False
        
        if self.tablero[posicion] != " ":
            return False

        return True


    def obtener_movimiento_ia(self):
        #Preparamos el tablero actual como texto para la IA
        tablero_texto = (
            f"{self.tablero[0]} | {self.tablero[1]} | {self.tablero[2]}\n"
            f"{self.tablero[3]} | {self.tablero[4]} | {self.tablero[5]}\n"
            f"{self.tablero[6]} | {self.tablero[7]} | {self.tablero[8]}"
        )

    #Le pedimos a la IA que haga un movimiento
        prompt = f"""
            Estas jugando a tres en raya, debes intentar ganar, te pasare un texto
             con las posiciones donde puedes jugar para intentar ganar, 
            Eres O en este tres en raya: {tablero_texto} responde solo con un número del
            0 al 8 para una casilla vacia.
        """

        try:
            #Intentamos obtener y validar la respuesta de la IA
            #respuesta = chat(model=self.modelo, prompt).strip()
            respuesta = ollama.chat(model=self.modelo, messages=
            [
                {
                    'role':'user',
                    'content':prompt
                }
            ])

            pos = respuesta['message']['content']

            movimiento_ia = int(pos.strip())
            if self.movimiento_valido(movimiento_ia):
                return movimiento_ia
            
        except:
            pass

        movimiento_en_orden = [
            4,
            0,2,6,8,
            1,3,5,7
        ]

        for movimiento in movimiento_en_orden:
            if self.movimiento_valido(movimiento):
                return movimiento
        

def jugar():
    juego = tres_en_raya()
    #Iniciamos el juego

    juego.mostrar_tablero()
    
    while True:
        try:
            #Pedimos al jugador que elija una casilla
            movimiento = int(input("\nTu turno - elige un numero del 0 a 8: "))

            #Verificamos si el movimiento es válido
            if juego.movimiento_valido(movimiento):
                #Colcamos la X en la casilla elegida
                juego.tablero[movimiento] = juego.jugador
                #break
            else:
                print("😒 Esa casilla no esta disponible o el número es invalido")
        
        except:
            print("Por favor, ingresa un número del 0 al 8")

        juego.mostrar_tablero()

        #Verificamos si el jugador ganó
        if juego.hay_ganador(juego.jugador):
            print("\n🎉 Felicitaciones! has ganado la partida")
            #break
        
        if juego.tablero_lleno():
            print("\n 😊 es empate! buen jugado! ")
            break

        #Turno de la IA
        print(f"\n 🤔 {juego.modelo} está pensando su jugada")

        movimiento_ia = juego.obtener_movimiento_ia()

        juego.tablero[movimiento_ia] = juego.computadora
        juego.mostrar_tablero()

        if juego.hay_ganador(juego.computadora):
            print("\n🤖 {juego.modelo} ha ganado!")
        
        if juego.tablero_lleno():
            print("\n 😊 es empate! buen jugado! ")
            break

if __name__ == "__main__":
    try:
        jugar()
    except KeyboardInterrupt:
        print("\n\n 😒 Juego terminado por el usuario, hasta pronto!")