import math

def distancia_euclidiana(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def par_cercano_bruto(puntos):
    min_dist = float('inf')
    p_cercano1, p_cercano2 = None, None
    for i in range(len(puntos)):
        for j in range(i + 1, len(puntos)):
            dist = distancia_euclidiana(puntos[i], puntos[j])
            if dist < min_dist:
                min_dist = dist
                p_cercano1 = puntos[i]
                p_cercano2 = puntos[j]
    return p_cercano1, p_cercano2, min_dist

def par_cercano_dividir_conquistar(puntos_x, puntos_y):
    n = len(puntos_x)
    if n <= 3:
        return par_cercano_bruto(puntos_x)

    mitad = n // 2
    punto_medio = puntos_x[mitad]

    # Divide los puntos
    puntos_x_izq = puntos_x[:mitad]
    puntos_y_izq = [p for p in puntos_y if p[0] <= punto_medio[0]]
    puntos_x_der = puntos_x[mitad:]
    puntos_y_der = [p for p in puntos_y if p[0] > punto_medio[0]]

    # Resuelve recursivamente
    p1_izq, p2_izq, dist_izq = par_cercano_dividir_conquistar(puntos_x_izq, puntos_y_izq)
    p1_der, p2_der, dist_der = par_cercano_dividir_conquistar(puntos_x_der, puntos_y_der)
    
    if dist_izq < dist_der:
        min_dist = dist_izq
        p1, p2 = p1_izq, p2_izq
    else:
        min_dist = dist_der
        p1, p2 = p1_der, p2_der

    # Considera los puntos en la franja central
    franja = [p for p in puntos_y if abs(p[0] - punto_medio[0]) < min_dist]
    for i in range(len(franja)):
        for j in range(i + 1, min(i + 7, len(franja))): # Optimización clave
            dist = distancia_euclidiana(franja[i], franja[j])
            if dist < min_dist:
                min_dist = dist
                p1, p2 = franja[i], franja[j]
    
    return p1, p2, min_dist

# Ejemplo de uso
puntos = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
puntos_ordenados_x = sorted(puntos, key=lambda p: p[0])
puntos_ordenados_y = sorted(puntos, key=lambda p: p[1])

p1, p2, dist_min = par_cercano_dividir_conquistar(puntos_ordenados_x, puntos_ordenados_y)

print(f"Puntos más cercanos: {p1} y {p2}")
print(f"Distancia mínima: {dist_min:.4f}")
