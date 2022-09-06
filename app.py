import streamlit as st
from streamlit_option_menu import option_menu
import time

# Gebruik hele scherm
st.set_page_config(layout="wide")

# Haal Watermerk weg van Streamlit
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Printer Oplossingen Pagina / Function
def printer_oplossingen():
    st.title(f"{selected}'s Snelle Oplossingen")
    st.markdown("---")
    st.subheader("Printer Toevoegen op HP PRO X2")
    st.markdown("> Oplossing...")
    st.markdown("---")
    st.subheader("Printer Verwijderen op HP PRO X2")
    st.markdown("> Oplossing...")

# Internet Oplossingen Pagina / Function
def internet_oplossingen():
    st.title(f"{selected}'s Snelle Oplossingen")
    st.markdown("---")
    st.subheader("Eduroam verbinden op HP PRO X2")
    st.markdown("> Oplossing...")
    st.markdown("---")

def apprechten_oplossingen():
    st.title(f"{selected} Snelle Oplossingen")
    st.markdown("---")
    st.subheader("Presto Account Rechtens")
    st.markdown("> Oplossing...")
    st.markdown("---")

    

# Sidebar met categorieën
with st.sidebar:
    st.success("Versie 0.1")
    st.title("Snelle Oplossingen")
    selected = option_menu(
        menu_title=None,
        options=["Printer", "Internet", "Applicatie Rechtens"],
    )
    st.markdown("---")

    st.title("Snelle Links")
    st.write("[Magister Onderwijzend Formulier](#)")
    st.write("[Magister Ondersteunend Formulier](#)")

# Gebruik de code die in de printer_oplossingen function staat en voer hier uit als de gebruiker op Printer klikt.
if selected == "Printer":
    printer_oplossingen()

if selected == "Internet":
    internet_oplossingen()

if selected == "Applicatie Rechten":
    apprechten_oplossingen()