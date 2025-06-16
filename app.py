import streamlit as st

st.set_page_config(page_title="Calcolo Carica RF", layout="centered")

st.title("Calcolo della Carica in Radiofrequenza Pulsata")

# Selezione modalità
mode = st.radio("Seleziona modalità di calcolo", ["Calcola Carica (C)", "Calcola Tempo (s)"])

# Inserimento parametri
V = st.number_input("Tensione (Volt)", min_value=0.0, value=65.0)
R = st.number_input("Impedenza (Ohm)", min_value=0.1, value=350.0)
freq = st.number_input("Frequenza (Hz)", min_value=0.1, value=2.0)
ton_ms = st.number_input("Durata ON per ciclo (ms)", min_value=1.0, value=20.0)

# Calcoli base
ton = ton_ms / 1000.0
period = 1 / freq
duty = ton / period
I = V / R

# Controllo consistenza duty cycle
if duty > 1:
    st.error("Errore: la durata ON supera il periodo. Riduci 'ton' o aumenta la frequenza.")
else:
    if mode == "Calcola Carica (C)":
        t = st.number_input("Tempo totale di erogazione (secondi)", min_value=0.0, value=300.0)
        Q = I * t * duty
        st.success(f"Carica erogata: **{Q:.6f} Coulomb**")
    else:
        Q_target = st.number_input("Carica desiderata (Coulomb)", min_value=0.0, value=2.0)
        if I * duty == 0:
            st.error("Errore: corrente o duty cycle nullo. Controlla i parametri.")
        else:
            t_needed = Q_target / (I * duty)
            st.success(f"Tempo necessario: **{t_needed:.2f} secondi**")
