def realizar_sospecha():
    print ("\nDECLARAR UNA SOSPECHA")
    
    personaje= input("Personaje: ")
    arma= input ("Arma: ")
    lugar= input ("Lugar: ")
    return [personaje,arma,lugar]
def realizar_acusacion ():
    print("\nDECLARAR UNA ACUSACIÓN")
    
    personaje= input ("Personaje: ")
    arma= input ("Arma: ")
    lugar= input("Lugar: ")
    return [personaje,arma,lugar]
def verificar_sospecha(sospecha, mano_oponente):
    for carta in sospecha:
        if carta in mano_oponente:
            
            return "El oponente tiene una carta relacionada..."
    return "No se han encontrado coincidencias"
def verificar_acusacion (acusacion,sobre):
    if acusacion == sobre:
        return True
    return False