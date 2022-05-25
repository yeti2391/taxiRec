
print("##########################")
print("\t comienza el turno")
print("########################## \n \n")


movil= int(input("Ingresa el numero de movil: "))
print(f"El movil usado para el servicio de hoy es el {movil} \n")


kmsalida= int(input("ingresa el km de salida: "))
print(f"se establecio el kilometraje de salida en: {kmsalida}km \n")

#### a partir de aca, recaudacion y subtotal
importe=[0]
print("ingresa el importe del viaje")
while importe[-1] != -103:  
    importe.append(int(input()))
    #contar viajes:
    print(f"Vas haciendo {len(importe)-1} viajes")
    #total
    print(sum(importe))