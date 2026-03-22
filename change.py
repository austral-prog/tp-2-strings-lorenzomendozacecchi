def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass
    gasto = float(input("Ingresar el gasto: "))
    dinero = int(input("ingrese el dinero recibido: "))
    print("Ingresar gasto:")
    print(gasto)
    print("Dinero recibido")
    print(dinero)
    print("")
    print("Vuelto")
    print("")
    vuelto = dinero - gasto
    pesos = int(vuelto)
    print("Pesos:")
    print(pesos)
    centavos = round((vuelto - pesos) * 100)
    print("Centavos:")
    print(centavos)
    if __name__ == "__main__":
        change()