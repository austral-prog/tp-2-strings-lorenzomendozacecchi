def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    pass
    nombre = input("Cual es tu nombre?")
    apellido = input("Cual es tu apellido?")
    print(nombre.lower(), apellido.lower())
    print(nombre.title(), apellido.title())
    print(nombre.upper(), apellido.upper())
    print("\t" + nombre.lower() + " " + apellido.lower())
    if __name__ == "__main__":
        names()

