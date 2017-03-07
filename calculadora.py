def teclas(origen,destino):
    
    if origen == destino:
        return 0
    
    lista = [origen]
    nivel = 0
    buffer = [-1]*10000
    buffer[origen] = 0
    cabeza = 0
        
    while cabeza < len(lista):
        aux = lista[cabeza]
            
        sum = (aux + 1) % 10000
        if sum == destino:
            return buffer[aux] + 1
        if buffer[sum] == -1:
            buffer[sum] = buffer[aux] + 1
            lista.append(sum)

        prod = (aux * 2) % 10000
        if prod == destino:
            return buffer[aux] + 1
        if buffer[prod] == -1:
            buffer[prod] = buffer[aux] + 1
            lista.append(prod)
            
        div = (aux // 3) % 10000
        if div == destino:
            return buffer[aux] + 1
        if buffer[div] == -1:
            buffer[div] = buffer[aux] + 1
            lista.append(div)

        cabeza += 1