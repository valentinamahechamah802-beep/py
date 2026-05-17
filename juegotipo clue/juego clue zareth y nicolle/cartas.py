import random
personajes = [
    "el guardia nocturno",
    "la influencer ",
    "Gerente del mall",
    "La Cosplayer ",
    "Tecnico de arcade",
    "La vendedora de perfumes "
]
armas=[
    "Perfume lujoso toxico",
    "Katana decorativa",
    "Licuadora Industrial ",
    "Animatronico Gigante",
    "Escaleras electricas ",
    "Muleta ",
    "Abre cartas "
]
lugares=[
    "Perfumeria",
    "Zona Gamer",
    "Carniceria",
    "Banco",
    "Fuente Central",
    "Cine",
    "Centro de monitoreo",
    "Super mercado"
    "Tienda de ropa"
]
def preparar_partida():
    personaje_secreto=random.choice(personajes)
    arma_secreta=random.choice(armas)
    lugar_secreto=random.choice(lugares)
    
    sobre=[
        personaje_secreto,
        arma_secreta,
        lugar_secreto
        
    ]
    cartas_restantes=[]
    
    for personaje in personajes:
        if personaje != personaje_secreto:
            cartas_restantes.append(personaje)
    for arma in armas:
        if arma != arma_secreta:
            cartas_restantes.append(armas)
    for lugar in lugares:
        if lugar!= lugar_secreto:
            cartas_restantes.append(lugar)
    random.shuffle(cartas_restantes)
    Jugador1= cartas_restantes[:8]
    jugador2= cartas_restantes[8:16]
    return sobre,Jugador1,jugador2
        
    