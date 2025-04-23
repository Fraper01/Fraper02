import datetime
from os import system

def obtener_hora_actual():
    return datetime.datetime.now().hour

def obtener_momento_dia(hora):
    if 6 <= hora < 12:
        return "desayuno"
    elif 12 <= hora < 16:
        return "comida"
    elif 16 <= hora < 20:
        return "merienda"
    elif 20 <= hora < 23:
        return "cena"
    else:
        return "dormir"  

def ofrecer_menu(momento):
    menu = {}
    if momento == "desayuno":
        menu = {
            1: "Tostadas con tomate y aceite",
            2: "Yogur con granola y frutas",
            3: "Café con croissant"
        }
    elif momento == "comida":
        menu = {
            1: "Paella",
            2: "Ensalada mixta con pollo",
            3: "Lentejas estofadas"
        }
    elif momento == "merienda":
        menu = {
            1: "Bocadillo de jamón y queso",
            2: "Fruta fresca de temporada",
            3: "Batido de proteínas"
        }
    elif momento == "cena":
        menu = {
            1: "Tortilla de patata",
            2: "Merluza a la plancha con verduras",
            3: "Sopa de pollo"
        }
    return menu

def mostrar_menu(momento, menu):
    print(f"\n¡Es la hora de {momento}!")
    print("Aquí tienes algunas opciones para elegir:")
    for opcion, plato in menu.items():
        print(f"{opcion}. {plato}")
    print("¡Buen provecho!")

if __name__ == "__main__":
    system('cls')
    hora_actual = obtener_hora_actual()
    momento_del_dia = obtener_momento_dia(hora_actual)
    menu_hoy = ofrecer_menu(momento_del_dia)

    if momento_del_dia != "dormir":
        mostrar_menu(momento_del_dia, menu_hoy)
    else:
        print("\n¡Parece que es hora de descansar! 😴")