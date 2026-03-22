def slice_simple():
    """Dado el texto 'Awesome', imprime distintos substrings
    usando slicing y lower().
    """
    texto = "Awesome"
    print(texto[0:3].lower())
    print(texto[2:5].lower())
    print(texto.lower())
    if __name__ == "__main__":
        slice_simple()
