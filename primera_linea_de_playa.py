def intersecta(intervalo1, intervalo2):
    izq = max(intervalo1[0],intervalo2[0])
    der = min(intervalo1[1],intervalo2[1])
    return (izq,der)

def playa(lista_edificios):    
    num_pasadizos = 0
    
    lista_edificios.sort()
    
    for edificio in lista_edificios:
        conectado = False
        print("edificio",edificio)
        if num_pasadizos > 0:
            interseccion = intersecta(ultimo_pasadizo,edificio)
            print("Interseccion con pasadizo:", ultimo_pasadizo,"=",interseccion)
            if interseccion[0] < interseccion[1]:
                print("Reduccion del pasadizo:", ultimo_pasadizo,"->",interseccion)
                ultimo_pasadizo = interseccion
                conectado = True

        if not conectado:
            ultimo_pasadizo = edificio
            num_pasadizos += 1
            print("Nuevo pasadizo:", edificio)
    
    return num_pasadizos