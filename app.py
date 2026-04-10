import streamlit as st # A Streamlit könyvtár importálása

# --- Oldal alapbeállításai ---
st.set_page_config(page_title="Profi Portfólió", page_icon="🚀")

# --- Oldalsáv navigáció ---
st.sidebar.title("Menü")
valasztas = st.sidebar.selectbox("Válassz projektet:", ["Hőmérséklet Átalakító", "Caesar Dekódoló"])

# --- 1. PROJEKT: HŐMÉRSÉKLET ÁTALAKÍTÓ (Bővített verzió) ---
if valasztas == "Hőmérséklet Átalakító":
    st.title("🌡️ Univerzális Hőmérséklet Átalakító")
    st.write("Válaszd ki a mértékegységet és írd be az értéket!")

    # Kiválasztjuk, miből akarunk váltani
    egyseg = st.selectbox("Milyen egységről váltasz?", ["Celsius", "Fahrenheit", "Kelvin"])
    ertek = st.number_input(f"Add meg az értéket ({egyseg}):", value=0.0)

    # Logika: kiszámoljuk az összes variációt
    if egyseg == "Celsius":
        c = ertek
        f = (c * 9/5) + 32
        k = c + 273.15
    elif egyseg == "Fahrenheit":
        f = ertek
        c = (f - 32) * 5/9
        k = c + 273.15
    else: # Ha Kelvin
        k = ertek
        c = k - 273.15
        f = (c * 9/5) + 32

    # Eredmények megjelenítése 3 oszlopban
    st.divider() # Vízszintes elválasztó vonal
    col1, col2, col3 = st.columns(3)
    
    # Csak azokat mutatjuk eredményként, amik nem az eredeti egységek
    col1.metric("Celsius", f"{c:.2f} °C")
    col2.metric("Fahrenheit", f"{f:.2f} °F")
    col3.metric("Kelvin", f"{k:.2f} K")

# --- 2. PROJEKT: CAESAR DEKÓDOLÓ ---
elif valasztas == "Caesar Dekódoló":
    st.title("🔐 Caesar Titkosító")
    szoveg = st.text_input("Üzenet:", "Szia Átalakítva")
    eltolas = st.slider("Eltolás mértéke:", 1, 25, 3)

    def caesar_kodolo(szoveg, eltolas):
        eredmeny = ""
        for karakter in szoveg:
            if karakter.isalpha():
                shift = 65 if karakter.isupper() else 97
                eredmeny += chr((ord(karakter) - shift + eltolas) % 26 + shift)
            else:
                eredmeny += karakter
        return eredmeny

    st.subheader("Eredmény:")
    st.success(caesar_kodolo(szoveg, eltolas))

