import streamlit as st
import pandas as pd

st.title("“Analyse de l’impact du temps d’écran sur les performances scolaires des étudiants“")
st.write("Bienvenue sur cette application d’analyse.Découvrez l’impact du temps d’écran sur les performances académiques des étudiants à travers des analyses statistiques et des modèles de machine learning.")



with st.container(border=True):
    st.number_input("temps d'ecran(hrs)")
    st.number_input("temps d'etude(hrs)")
    st.number_input("sommiel (hrs)")
    st.number_input("MGP (sur 4)")
 
import_file = st.file_uploader("Ou importer CSV", type="csv")   
if import_file:
    import_data = pd.read_csv(import_file)
    st.write(import_data)
    if st.button("Ajouter au dataset"):
        st.session_state.data = pd.concat(
            [st.session_state.data, import_data],
            ignore_index=True)
        st.success("Données ajoutées")

#if st.button("Ajouter csv file"):
   
#    pd.read_csv('file')
    
  

