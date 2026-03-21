def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    pass
    nombre_completo = input("Ingrese un nombre completo: ").strip()
    email = input("Ingrese un email: ").strip()

    nota1 = int(input("Ingrese la 1era nota: "))
    nota2 = int(input("Ingrese la 2da nota: "))
    nota3 = int(input("Ingrese la 3ra nota: "))

    # PROCESAMIENTO
    nombre_limpio = nombre_completo.title()
    email_limpio = email.lower()
    # maria garcia
    # maria.garcia@universidad.edu
    espacio = nombre_completo.find(" ")

    iniciales = f"{nombre_completo[0].upper()}{nombre_completo[espacio + 1].upper()}"
    usuario = f"{nombre_completo[espacio + 1:].lower()}.{nombre_completo[:espacio].lower()}"
    dominio = email_limpio[email_limpio.find("@") + 1:]
    nombre_archivo = nombre_completo.replace(" ", "_").title()
    cantidad_a = nombre_completo.lower().count("a")
    codigo_secreto = nombre_completo[::-1].upper()

    suma = nota1 + nota2 + nota3
    promedio = suma / 3
    promedio_entero = int(promedio)
    print("""========================
    FICHA DEL ALUMNO
========================""")
    print(f"Nombre: {nombre_limpio}")
    print(f"Email: {email_limpio}")
    print(f"Caracteres en nombre: {len(nombre_completo)}")
    print(f"Iniciales: {iniciales}")
    print(f"Usuario: {usuario}")
    print(f"Email valido: {'@' in email}")
    print(f"Dominio: {dominio}")
    print(f"Nombre para archivo: {nombre_archivo}")
    print(f"Cantidad de a: {cantidad_a}")
    print(f"Codigo secreto: {codigo_secreto}")

    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")
    print(f"Promedio entero: {promedio_entero}")

    print("=" * 24)


ficha()