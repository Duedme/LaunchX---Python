velocidad = 49
dimension = 25

if velocidad > 25:
    print("Advertencia")
else:
    print("Todo normal")

if velocidad == 20:
    print("¡Mira al cielo!")
elif velocidad > 20:
    print("¡Mira al cielo otra vez!")
else:
    print("No haga nada joven")

if dimension > 25 and velocidad > 25:
    print("Habrán problemas")
elif velocidad == 20:
    print("¡Mira al cielo!")
elif dimension < 25:
    print("Váyase joven")
else:
    print("Váyase joven")