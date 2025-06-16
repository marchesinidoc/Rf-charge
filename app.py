def calculate_charge(V, R, t_total, freq=2.0, ton_ms=20):
    # Convert on-time from ms to seconds
    ton = ton_ms / 1000.0
    # Calculate duty cycle
    period = 1 / freq
    duty_cycle = ton / period
    # Calculate current
    I = V / R
    # Calculate charge
    Q = I * t_total * duty_cycle
    return Q

def calculate_time_from_charge(V, R, Q_target, freq=2.0, ton_ms=20):
    # Convert on-time from ms to seconds
    ton = ton_ms / 1000.0
    # Calculate duty cycle
    period = 1 / freq
    duty_cycle = ton / period
    # Calculate current
    I = V / R
    # Calculate time needed
    t_needed = Q_target / (I * duty_cycle)
    return t_needed

def main():
    print("Calcolo della carica nella radiofrequenza pulsata")
    mode = input("Vuoi calcolare la carica (C) o il tempo necessario (T)? [C/T]: ").strip().upper()

    V = float(input("Inserisci la tensione (Volt): "))
    R = float(input("Inserisci l'impedenza (Ohm): "))

    freq = input("Inserisci la frequenza (Hz) [predefinito = 2]: ").strip()
    freq = float(freq) if freq else 2.0

    ton_ms = input("Inserisci la durata ON di ogni ciclo (ms) [predefinito = 20]: ").strip()
    ton_ms = float(ton_ms) if ton_ms else 20.0

    if mode == "C":
        t_total = float(input("Inserisci il tempo di erogazione (secondi): "))
        Q = calculate_charge(V, R, t_total, freq, ton_ms)
        print(f"Carica erogata: {Q:.6f} Coulomb")
    elif mode == "T":
        Q_target = float(input("Inserisci la carica desiderata (Coulomb): "))
        t_needed = calculate_time_from_charge(V, R, Q_target, freq, ton_ms)
        print(f"Tempo necessario: {t_needed:.2f} secondi")
    else:
        print("Scelta non valida. Usa 'C' per carica o 'T' per tempo.")

if __name__ == "__main__":
    main()
