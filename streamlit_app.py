# ============================================
# KALKULATOR TERMODINAMIKA + TERMOKIMIA
# ============================================

R = 0.008314      # kJ/mol·K
R_gas = 0.0821    # L·atm/mol·K


# ============================================
# 1. HUKUM 1 TERMODINAMIKA
# ============================================

def hukum1():

    print("\n=== HUKUM 1 TERMODINAMIKA ===")
    print("Rumus: ΔU = Q − W")
    print("Masukkan 0 pada yang ingin dicari\n")

    du = float(input("ΔU (kJ): "))
    Q = float(input("Q (kJ): "))
    W = float(input("W (kJ): "))

    if du == 0:

        hasil = Q - W

        print(f"\nΔU = {Q} − {W}")
        print(f"ΔU = {hasil:.3f} kJ")

    elif Q == 0:

        hasil = du + W

        print(f"\nQ = {du} + {W}")
        print(f"Q = {hasil:.3f} kJ")

    elif W == 0:

        hasil = Q - du

        print(f"\nW = {Q} − {du}")
        print(f"W = {hasil:.3f} kJ")

    else:
        print("❌ Isi salah satu dengan 0")


# ============================================
# 2. USAHA
# ============================================

def usaha():

    print("\n=== USAHA ===")
    print("Rumus: W = P × ΔV\n")

    P = float(input("Tekanan P (Pa): "))
    dV = float(input("Perubahan volume ΔV (m³): "))

    hasil = P * dV

    print(f"\nW = {P} × {dV}")
    print(f"W = {hasil:.3f} J")


# ============================================
# 3. KALOR
# ============================================

def kalor():

    print("\n=== KALOR ===")
    print("Rumus: Q = m × c × ΔT\n")

    m = float(input("Massa m (g): "))
    c = float(input("Kalor jenis c (J/g·K): "))
    dT = float(input("Perubahan suhu ΔT (K): "))

    hasil = m * c * dT

    print(f"\nQ = {m} × {c} × {dT}")
    print(f"Q = {hasil:.3f} J")


# ============================================
# 4. ENTALPI
# ============================================

def entalpi():

    print("\n=== ENTALPI ===")
    print("Rumus: ΔH = ΔU + ΔnRT")
    print("R = 0.008314 kJ/mol·K")
    print("Masukkan 0 pada yang ingin dicari\n")

    dH = float(input("ΔH (kJ): "))
    dU = float(input("ΔU (kJ): "))
    dn = float(input("Δn (mol): "))
    T = float(input("T (K): "))

    nRT = dn * R * T

    if dH == 0:

        hasil = dU + nRT

        print(f"\nΔH = {dU} + ({dn} × {R} × {T})")
        print(f"ΔH = {hasil:.3f} kJ")

    elif dU == 0:

        hasil = dH - nRT

        print(f"\nΔU = {dH} − {nRT:.3f}")
        print(f"ΔU = {hasil:.3f} kJ")

    else:
        print("❌ Isi ΔH atau ΔU dengan 0")


# ============================================
# 5. HUKUM HESS
# ============================================

def hess():

    print("\n=== HUKUM HESS ===")
    print("Rumus: ΔH total = ΣΔH\n")

    data = input("Masukkan ΔH tiap reaksi (pisahkan koma): ")

    nilai = [float(x) for x in data.split(",")]

    hasil = sum(nilai)

    print(f"\nΔH total = {hasil:.3f} kJ")


# ============================================
# 6. ΔH REAKSI
# ============================================

def deltaH_reaksi():

    print("\n=== ΔH REAKSI ===")
    print("Rumus: ΔH = ΣΔHf produk − ΣΔHf reaktan\n")

    p = input("ΔHf produk (pisahkan koma): ")
    r = input("ΔHf reaktan (pisahkan koma): ")

    produk = [float(x) for x in p.split(",")]
    reaktan = [float(x) for x in r.split(",")]

    hasil = sum(produk) - sum(reaktan)

    print(f"\nΔH reaksi = {hasil:.3f} kJ/mol")


# ============================================
# 7. ENERGI GIBBS
# ============================================

def gibbs():

    print("\n=== ENERGI GIBBS ===")
    print("Rumus: ΔG = ΔH − TΔS\n")

    dH = float(input("ΔH (kJ): "))
    T = float(input("T (K): "))
    dS = float(input("ΔS (kJ/K): "))

    hasil = dH - (T * dS)

    print(f"\nΔG = {dH} − ({T} × {dS})")
    print(f"ΔG = {hasil:.3f} kJ")


# ============================================
# 8. ENTROPI
# ============================================

def entropi():

    print("\n=== ENTROPI ===")
    print("Rumus: ΔS = Q / T\n")

    Q = float(input("Q (kJ): "))
    T = float(input("T (K): "))

    if T == 0:
        print("❌ Temperatur tidak boleh 0")

    else:

        hasil = Q / T

        print(f"\nΔS = {Q} / {T}")
        print(f"ΔS = {hasil:.3f} kJ/K")


# ============================================
# 9. GAS IDEAL
# ============================================

def gas_ideal():

    print("\n================================")
    print("      PERSAMAAN GAS IDEAL")
    print("================================")

    print("Rumus:")
    print("PV = nRT")
    print("R = 0.0821 L·atm/mol·K")

    print("\nMol gas dapat:")
    print("1. Langsung diketahui")
    print("2. Dihitung dari massa dan Mr")

    opsi = input("\nPilih cara menentukan mol (1/2): ")

    # =====================================
    # MOL SUDAH DIKETAHUI
    # =====================================

    if opsi == "1":

        n = float(input("\nMasukkan jumlah mol n (mol): "))

    # =====================================
    # MOL DARI MASSA DAN Mr
    # =====================================

    elif opsi == "2":

        print("\n=== MENGHITUNG MOL ===")
        print("Rumus: n = m / Mr")

        senyawa = input("Nama senyawa: ")

        massa = float(input("Massa senyawa (g): "))

        Mr = float(input(f"Mr {senyawa}: "))

        n = massa / Mr

        print("\nPerhitungan mol:")
        print(f"n = m / Mr")
        print(f"n = {massa} g / {Mr}")
        print(f"n = {n:.3f} mol")

    else:
        print("❌ Pilihan tidak valid")
        return

    # =====================================
    # PILIH PERHITUNGAN
    # =====================================

    print("\n================================")
    print("      PILIH PERHITUNGAN")
    print("================================")

    print("1. Cari tekanan (P)")
    print("2. Cari volume (V)")
    print("3. Cari temperatur (T)")
    print("4. Cari mol (n)")

    pilih = input("\nPilihan: ")

    # =====================================
    # CARI TEKANAN
    # =====================================

    if pilih == "1":

        T = float(input("Temperatur T (K): "))
        V = float(input("Volume V (L): "))

        hasil = (n * R_gas * T) / V

        print(f"\nP = ({n:.3f} × {R_gas} × {T}) / {V}")
        print(f"P = {hasil:.3f} atm")

    # =====================================
    # CARI VOLUME
    # =====================================

    elif pilih == "2":

        T = float(input("Temperatur T (K): "))
        P = float(input("Tekanan P (atm): "))

        hasil = (n * R_gas * T) / P

        print(f"\nV = ({n:.3f} × {R_gas} × {T}) / {P}")
        print(f"V = {hasil:.3f} L")

    # =====================================
    # CARI TEMPERATUR
    # =====================================

    elif pilih == "3":

        P = float(input("Tekanan P (atm): "))
        V = float(input("Volume V (L): "))

        hasil = (P * V) / (n * R_gas)

        print(f"\nT = ({P} × {V}) / ({n:.3f} × {R_gas})")
        print(f"T = {hasil:.3f} K")

    # =====================================
    # CARI MOL
    # =====================================

    elif pilih == "4":

        P = float(input("Tekanan P (atm): "))
        V = float(input("Volume V (L): "))
        T = float(input("Temperatur T (K): "))

        hasil = (P * V) / (R_gas * T)

        print(f"\nn = ({P} × {V}) / ({R_gas} × {T})")
        print(f"n = {hasil:.3f} mol")

    else:
        print("❌ Pilihan tidak valid")


# ============================================
# 10. GAS NYATA
# ============================================

def gas_nyata():

    print("\n================================")
    print("       GAS NYATA")
    print("    Persamaan Van der Waals")
    print("================================")

    print("Rumus:")
    print("(P + an²/V²)(V − nb) = nRT")
    print("R = 0.0821 L·atm/mol·K\n")

    n = float(input("Jumlah mol n (mol): "))
    T = float(input("Temperatur T (K): "))
    V = float(input("Volume V (L): "))

    print("\nKonstanta gas:")
    a = float(input("Konstanta a: "))
    b = float(input("Konstanta b: "))

    if V == 0 or (V - n*b) == 0:
        print("❌ Volume tidak valid")
        return

    hasil = ((n * R_gas * T) / (V - n*b)) - ((a * n**2) / (V**2))

    print("\nLangkah perhitungan:")
    print(f"P = (nRT / (V - nb)) - (an² / V²)")

    print(f"\nP = {hasil:.3f} atm")


# ============================================
# MENU UTAMA
# ============================================

while True:

    print("\n====================================")
    print(" KALKULATOR TERMODINAMIKA")
    print("====================================")

    print("1. Hukum 1 Termodinamika")
    print("2. Usaha")
    print("3. Kalor")
    print("4. Entalpi")
    print("5. Hukum Hess")
    print("6. ΔH Reaksi")
    print("7. Energi Gibbs")
    print("8. Entropi")
    print("9. Gas Ideal")
    print("10. Gas Nyata")
    print("0. Keluar")

    pilih = input("\nPilih menu: ")

    if pilih == "1":
        hukum1()

    elif pilih == "2":
        usaha()

    elif pilih == "3":
        kalor()

    elif pilih == "4":
        entalpi()

    elif pilih == "5":
        hess()

    elif pilih == "6":
        deltaH_reaksi()

    elif pilih == "7":
        gibbs()

    elif pilih == "8":
        entropi()

    elif pilih == "9":
        gas_ideal()

    elif pilih == "10":
        gas_nyata()

    elif pilih == "0":

        print("\nProgram selesai.")
        break

    else:
        print("❌ Pilihan tidak valid!")

