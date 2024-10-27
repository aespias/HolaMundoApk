import time

def main():
    for _ in range(50):
        print("Hola mundo")
        time.sleep(0.02)  # Espera 0.02 segundos (50 veces por segundo)

if __name__ == "__main__":
    main()
