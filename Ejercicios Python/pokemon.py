def simular_batalla(vida, ataques):
    # 1. Crea aquí tu bucle for para recorrer 'ataques'
    for ataque in ataques:
        # 2. Resta el ataque a la vida
        vida -= ataque
        # 3. Imprime la vida restante
        print(f"Vida restante: {vida}")
        # 4. Pon un if para comprobar si la vida es <= 0
        # (Si es as í, imprime un mensaje y usa 'break')
        if vida <= 0:
            print("¡El jefe ha sido derrotado!")
            break

# Variables iniciales
vida_boss = 100
mis_ataques = [30, 50, 40]

# Llamada a la función
simular_batalla(vida_boss, mis_ataques)