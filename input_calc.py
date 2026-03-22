def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    pass
    base = int(input("ingresar la base "))
    altura = int(input("ingresar la altura "))
    print("Base:", base)
    print("Altura:", altura)
    print("Area:", base * altura)
    print("Perimetro:", base * 2 + altura * 2)
    if __name__ == "__main__":
        rectangle()


