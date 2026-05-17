def crear_hoja():
    hoja={
    "personajes":{},
    "armas":{},
    "lugares":{}}
    return hoja
def mostrar_hoja(hoja):
    print ("\n ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
    print("♥ HOJA DEL DETECTIVE ♥")
    print ("\n ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
    
    print("\n ♥ PERSONAJES ♥")
    for dato in hoja ["Personajes"]:
        print (dato,"→",hoja["Personajes"][dato])
    print ("\n ♥ ARMAS ♥")
    for dato in hoja ["Armas"]:
        print (dato,"→",hoja["Armas"][dato])
    print("\n ♥ LUGARES ♥")
    for dato in hoja ["Lugares"]:
        print (dato,"→",hoja["Lugares"][dato])
    
    
    
    