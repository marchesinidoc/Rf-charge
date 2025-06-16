import streamlit as st

def calculate_charge(V, R, f, t_total, t_on_start, t_on_end, pct_start):
    p = pct_start / 100.0
    n_cycles = f * t_total
    current = V / R
    Q = n_cycles * current * (p * t_on_start + (1 - p) * t_on_end)
    return Q

def calculate_time(V, R, f, Q_target, t_on_start):
    current = V / R
    energy_per_cycle = current * t_on_start
    cycles_needed = Q_target / energy_per_cycle
    t_needed = cycles_needed / f
    return t_needed

st.title("Calcolo della Carica o del Tempo nella Radiofrequenza Pulsata")

mode = st.radio("Vuoi calcolare la carica o il tempo necessario?", ("Carica (C)", "Tempo (T)"))

V = st.number_input("Tensione (Volt)", min_value=1.0, value=65.0)
R = st.number_input("Resistenza (Ohm)", min_value=1.0, value=350.0)
f = st.number_input("Frequenza (Hz)", min_value=0.1, value=2.0)

if mode == "Carica (C)":
    t_total = st.number_input("Tempo totale di erogazione (secondi)", min_value=1.0, value=300.0)
    t_on_start = st.number_input("Tempo ON iniziale (secondi)", min_value=0.001, value=0.02)
    t_on_end = st.number_input("Tempo ON finale (secondi)", min_value=0.001, value=0.005)
    pct_start = st.slider("Percentuale del tempo a parametri iniziali", 0, 100, 70)

    if st.button("Calcola Carica"):
        Q = calculate_charge(V, R, f, t_total, t_on_start, t_on_end, pct_start)
        st.success(f"Carica totale erogata: {Q:.2f} Coulomb")

elif mode == "Tempo (T)":
    Q_target = st.number_input("Carica desiderata (Coulomb)", min_value=0.01, value=10.0)
    t_on_start = st.number_input("Tempo ON stimato (secondi)", min_value=0.001, value=0.02)

    if st.button("Calcola Tempo"):
        t_needed = calculate_time(V, R, f, Q_target, t_on_start)
        st.success(f"Tempo necessario stimato: {t_needed:.2f} secondi")

