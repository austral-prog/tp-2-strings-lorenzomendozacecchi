def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass
    precio = int(input("ingresar precio: "))
    descuento = float(input("ingresar descuento: "))
    cantidad = int(input("ingresar cantidad: "))
    precio_descuento = precio - descuento
    print("Precio:", precio)
    print("Descuento:", descuento)
    print("Precio con descuento:", precio_descuento)
    print("Total:", precio_descuento * cantidad)
casting()
