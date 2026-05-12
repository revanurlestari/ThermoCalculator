import streamlit as st

# ============================================
# KONSTANTA
# ============================================

R = 0.008314
R_gas = 0.0821

st.set_page_config(page_title="Kalkulator Termodinamika")

st.title("🔥 Kalkulator Termodinamika + Termokimia")

menu = st.sidebar.selectbox(
    "Pilih Menu",
    [
        "Hukum 1 Termodinamika",
        "Usaha",
        "Kalor",
        "Entalpi",
        "Hukum Hess",
        "ΔH Reaksi",
        "Energi Gibbs",
        "Entropi",
        "Gas Ideal",
        "Gas Nyata"
    ]
)

# ============================================
# 1. HUKUM 1
# ============================================

if menu == "Hukum 1 Termodinamika":

    st.header("Hukum 1 Termodinamika")
    st.latex(r"\Delta U = Q - W")

    du = st.number_input("ΔU (kJ)", value=0.0)
    Q = st.number_input("Q (kJ)", value=0.0)
    W = st.number_input("W (kJ)", value=0.0)

    if st.button("Hitung Hukum 1"):

        if du == 0:
            hasil = Q - W
            st.success(f"ΔU = {hasil:.3f} kJ")

        elif Q == 0:
            hasil = du + W
            st.success(f"Q = {hasil:.3f} kJ")

        elif W == 0:
            hasil = Q - du
            st.success(f"W = {hasil:.3f} kJ")

        else:
            st.error("Isi salah satu dengan 0")


# ============================================
# 2. USAHA
# ============================================

elif menu == "Usaha":

    st.header("Usaha")
    st.latex(r"W = P \times \Delta V")

    P = st.number_input("Tekanan P (Pa)")
    dV = st.number_input("ΔV (m³)")

    if st.button("Hitung Usaha"):

        hasil = P * dV

        st.success(f"W = {hasil:.3f} J")


# ============================================
# 3. KALOR
# ============================================

elif menu == "Kalor":

    st.header("Kalor")
    st.latex(r"Q = m \times c \times \Delta T")

    m = st.number_input("Massa (g)")
    c = st.number_input("Kalor jenis (J/g·K)")
    dT = st.number_input("ΔT (K)")

    if st.button("Hitung Kalor"):

        hasil = m * c * dT

        st.success(f"Q = {hasil:.3f} J")


# ============================================
# 4. ENTALPI
# ============================================

elif menu == "Entalpi":

    st.header("Entalpi")
    st.latex(r"\Delta H = \Delta U + \Delta nRT")

    dH = st.number_input("ΔH (kJ)", value=0.0)
    dU = st.number_input("ΔU (kJ)", value=0.0)
    dn = st.number_input("Δn (mol)")
    T = st.number_input("T (K)")

    if st.button("Hitung Entalpi"):

        nRT = dn * R * T

        if dH == 0:

            hasil = dU + nRT
            st.success(f"ΔH = {hasil:.3f} kJ")

        elif dU == 0:

            hasil = dH - nRT
            st.success(f"ΔU = {hasil:.3f} kJ")

        else:
            st.error("Isi ΔH atau ΔU dengan 0")


# ============================================
# 5. HUKUM HESS
# ============================================

elif menu == "Hukum Hess":

    st.header("Hukum Hess")

    data = st.text_input(
        "Masukkan ΔH tiap reaksi (pisahkan koma)"
    )

    if st.button("Hitung Hess"):

        nilai = [float(x) for x in data.split(",")]

        hasil = sum(nilai)

        st.success(f"ΔH total = {hasil:.3f} kJ")


# ============================================
# 6. ΔH REAKSI
# ============================================

elif menu == "ΔH Reaksi":

    st.header("ΔH Reaksi")

    p = st.text_input("ΔHf produk")
    r = st.text_input("ΔHf reaktan")

    if st.button("Hitung ΔH Reaksi"):

        produk = [float(x) for x in p.split(",")]
        reaktan = [float(x) for x in r.split(",")]

        hasil = sum(produk) - sum(reaktan)

        st.success(f"ΔH reaksi = {hasil:.3f} kJ/mol")


# ============================================
# 7. ENERGI GIBBS
# ============================================

elif menu == "Energi Gibbs":

    st.header("Energi Gibbs")
    st.latex(r"\Delta G = \Delta H - T\Delta S")

    dH = st.number_input("ΔH (kJ)")
    T = st.number_input("T (K)")
    dS = st.number_input("ΔS (kJ/K)")

    if st.button("Hitung Gibbs"):

        hasil = dH - (T * dS)

        st.success(f"ΔG = {hasil:.3f} kJ")


# ============================================
# 8. ENTROPI
# ============================================

elif menu == "Entropi":

    st.header("Entropi")
    st.latex(r"\Delta S = Q/T")

    Q = st.number_input("Q (kJ)")
    T = st.number_input("T (K)")

    if st.button("Hitung Entropi"):

        if T == 0:
            st.error("Temperatur tidak boleh 0")

        else:

            hasil = Q / T

            st.success(f"ΔS = {hasil:.3f} kJ/K")


# ============================================
# 9. GAS IDEAL
# ============================================

elif menu == "Gas Ideal":

    st.header("Gas Ideal")
    st.latex(r"PV = nRT")

    cara = st.radio(
        "Cara menentukan mol",
        ["Mol diketahui", "Dari massa dan Mr"]
    )

    if cara == "Mol diketahui":

        n = st.number_input("Mol (mol)")

    else:

        massa = st.number_input("Massa (g)")
        Mr = st.number_input("Mr")

        n = massa / Mr if Mr != 0 else 0

        st.info(f"Mol = {n:.3f} mol")

    pilihan = st.selectbox(
        "Cari",
        ["Tekanan", "Volume", "Temperatur", "Mol"]
    )

    if pilihan == "Tekanan":

        T = st.number_input("Temperatur (K)")
        V = st.number_input("Volume (L)")

        if st.button("Hitung Tekanan"):

            hasil = (n * R_gas * T) / V

            st.success(f"P = {hasil:.3f} atm")

    elif pilihan == "Volume":

        T = st.number_input("Temperatur (K)")
        P = st.number_input("Tekanan (atm)")

        if st.button("Hitung Volume"):

            hasil = (n * R_gas * T) / P

            st.success(f"V = {hasil:.3f} L")

    elif pilihan == "Temperatur":

        P = st.number_input("Tekanan (atm)")
        V = st.number_input("Volume (L)")

        if st.button("Hitung Temperatur"):

            hasil = (P * V) / (n * R_gas)

            st.success(f"T = {hasil:.3f} K")

    elif pilihan == "Mol":

        P = st.number_input("Tekanan (atm)")
        V = st.number_input("Volume (L)")
        T = st.number_input("Temperatur (K)")

        if st.button("Hitung Mol"):

            hasil = (P * V) / (R_gas * T)

            st.success(f"n = {hasil:.3f} mol")


# ============================================
# 10. GAS NYATA
# ============================================

elif menu == "Gas Nyata":

    st.header("Gas Nyata")
    st.latex(
        r"(P + an^2/V^2)(V - nb)=nRT"
    )

    n = st.number_input("Mol (mol)")
    T = st.number_input("Temperatur (K)")
    V = st.number_input("Volume (L)")
    a = st.number_input("Konstanta a")
    b = st.number_input("Konstanta b")

    if st.button("Hitung Gas Nyata"):

        hasil = (
            (n * R_gas * T) / (V - n*b)
        ) - (
            (a * n**2) / (V**2)
        )

        st.success(f"P = {hasil:.3f} atm")
