import random
import ipaddress

def generar_ip_privada():
    """Genera una IP dentro de los rangos privados (RFC 1918)."""
    prefijo = random.choice(['10', '172', '192'])
    if prefijo == '10':
        return f"10.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
    elif prefijo == '172':
        return f"172.{random.randint(16,31)}.{random.randint(0,255)}.{random.randint(0,255)}"
    else:
        return f"192.168.{random.randint(0,255)}.{random.randint(0,255)}"

def generar_ip_publica():
    """Genera una IP aleatoria que sea pública."""
    while True:
        ip = ".".join(map(str, (random.randint(1, 254) for _ in range(4))))
        ip_obj = ipaddress.ip_address(ip)
        if not ip_obj.is_private and not ip_obj.is_reserved and not ip_obj.is_multicast:
            return ip

def ejecutar_desafio():
    puntuacion = 0
    print("==========================================")
    print("   🏆 MODO DESAFÍO: IPv4 STREAK 🏆")
    print("==========================================")
    print("Acierta tantas como puedas. ¡Un fallo y termina!")
    print("(Escribe '3' para retirarte con tu puntuación actual)\n")

    while True:
        es_realmente_privada = random.choice([True, False])
        ip_sorteada = generar_ip_privada() if es_realmente_privada else generar_ip_publica()

        print(f"Puntuación actual: ⭐ {puntuacion}")
        print(f"IP: **{ip_sorteada}**")
        print("1. Pública | 2. Privada | 3. Salir")
        
        entrada = input("Respuesta: ").strip().lower()

        if entrada in ['3', 'salir', 'exit', 'q']:
            print(f"\nTe has retirado. Puntuación final: **{puntuacion}** puntos.")
            break

        if entrada == '1':
            usuario_cree_privada = False
        elif entrada == '2':
            usuario_cree_privada = True
        else:
            print("\n⚠️ Opción inválida. Intenta de nuevo.")
            continue

        if usuario_cree_privada == es_realmente_privada:
            puntuacion += 1
            print("\n✅ ¡Correcto! +1 punto.")
            print("-" * 30)
        else:
            tipo_correcto = "PRIVADA" if es_realmente_privada else "PÚBLICA"
            print("\n" + "!" * 20)
            print(f"❌ ¡INCORRECTO! La IP era {tipo_correcto}.")
            print(f"GAME OVER. Puntuación alcanzada: **{puntuacion}**")
            print("!" * 20)
            break

    # --- EL TRUCO PARA MANTENER LA VENTANA ABIERTA ---
    print("\n" + "=" * 40)
    input("Presiona ENTER para cerrar esta ventana...")

if __name__ == "__main__":
    ejecutar_desafio()
