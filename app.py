import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.cluster import KMeans

st.title("Analyse de l’impact du temps d’écran sur les performances scolaires des étudiants")
st.write("Bienvenue sur cette application d’analyse. Découvrez l’impact du temps d’écran sur les performances académiques des étudiants à travers des analyses statistiques et des modèles de machine learning.")

# INITIALISATION
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=[
        "screen_time", "study_time", "sleep_time", "mgp"
    ])


# COLLECTE MANUELLE

st.subheader("Entrer les données")

screen = st.number_input("Temps d'écran (heures)")
study = st.number_input("Temps d'étude (heures)")
sleep = st.number_input("Sommeil (heures)")
mgp = st.number_input("MGP (sur 4)")

if st.button("Ajouter les données"):
    new_data = pd.DataFrame({
        "screen_time": [screen],
        "study_time": [study],
        "sleep_time": [sleep],
        "mgp": [mgp]
    })

    if st.session_state.data.empty:
        st.session_state.data = new_data
    else:
        st.session_state.data = pd.concat(
            [st.session_state.data, new_data],
            ignore_index=True
        )

    st.success("Données ajoutées")


# IMPORT CSV

file = st.file_uploader("Importer un fichier CSV", type=["csv"])

if file is not None:
    df_import = pd.read_csv(file)
    st.write(df_import)

    if st.button("Ajouter CSV"):
        st.session_state.data = pd.concat(
            [st.session_state.data, df_import],
            ignore_index=True
        )

        st.success("CSV ajouté")

df = st.session_state.data
st.write(df) 

st.subheader("📊 Analyse descriptive")
if len(df) > 0:

    st.write("📋 Aperçu des données")
    st.dataframe(df)

    st.write("📌 Moyennes")
    st.write("Temps d'écran moyen :", df["screen_time"].mean())
    st.write("Temps d'étude moyen :", df["study_time"].mean())
    st.write("Sommeil moyen :", df["sleep_time"].mean())
    st.write("MGP moyen :", df["mgp"].mean())

    st.write("📌 Valeurs extrêmes")
    st.write("Max MGP :", df["mgp"].max())
    st.write("Min MGP :", df["mgp"].min())

else:
    st.warning("Aucune donnée disponible")

st.subheader("📈 Régression linéaire")
if len(df) > 2 and all(col in df.columns for col in ["screen_time", "study_time", "sleep_time", "mgp"]):
    X = df[["screen_time", "study_time", "sleep_time"]]
    y = df["mgp"]
    model_reg = LinearRegression()
    model_reg.fit(X, y)
    st.success("Modèle de régression entraîné avec succès")
else:
    st.warning("Ajoute au moins 3 données complètes pour entraîner le modèle.")      


st.subheader("🧠 Classification (Régression logistique)")
st.write("La classification permet de prédire si un étudiant va réussir ou échouer selon ses habitudes.")

df = st.session_state.data

if len(df) > 3:

    # 🎯 création de la cible
    df["passed"] = df["mgp"].apply(lambda x: 1 if x >= 2 else 0)

    X_clf = df[["screen_time", "study_time", "sleep_time"]]
    y_clf = df["passed"]

    # ⚠️ sécurité : vérifier qu'il y a 2 classes
    if len(y_clf.unique()) > 1:

        model_clf = LogisticRegression()
        model_clf.fit(X_clf, y_clf)

        st.success("Modèle de classification entraîné avec succès")

    else:
        st.warning("Il faut au moins 2 classes (réussite et échec) pour entraîner le modèle.")

else:
    st.warning("Ajoute au moins 4 données pour activer la classification.")


st.subheader("🔵 Analyse des profils d'étudiants (Clustering)")

st.write("""
Cette analyse regroupe automatiquement les étudiants selon leurs habitudes afin d'identifier des profils similaires.
""")

df = st.session_state.data


if len(df) > 3 and len(df[["screen_time", "study_time", "sleep_time"]].drop_duplicates()) > 1:
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)

    df_cluster = df.copy()
    df_cluster["cluster"] = kmeans.fit_predict(
        df_cluster[["screen_time", "study_time", "sleep_time"]]
    )

    # 🧠 transformer les clusters en sens humain
    def label_cluster(row):
        if row["cluster"] == 0:
            return "📚 Étudiant discipliné"
        else:
            return "⚠️ Étudiant à risque"

    df_cluster["profil"] = df_cluster.apply(label_cluster, axis=1)

    st.success("Analyse terminée avec succès")

    # 📊 affichage utile
    st.subheader("📋 Résultats interprétés")
    st.dataframe(df_cluster[[
        "screen_time",
        "study_time",
        "sleep_time",
        "mgp",
        "profil"
    ]])

    # 📌 résumé utile utilisateur
    st.subheader("📌 Résumé")

    st.write("Nombre d'étudiants disciplinés :",
             len(df_cluster[df_cluster["profil"] == "📚 Étudiant discipliné"]))

    st.write("Nombre d'étudiants à risque :",
             len(df_cluster[df_cluster["profil"] == "⚠️ Étudiant à risque"]))

else:
    st.warning("Ajoute au moins 4 données pour activer le clustering.")



    
st.subheader("🔮 Tester une prédiction")
df = st.session_state.data
if len(df) > 2:
    # entraîner le modèle
    X = df[["screen_time", "study_time", "sleep_time"]]
    y = df["mgp"]

    model = LinearRegression()
    model.fit(X, y)

    # inputs utilisateur
    screen = st.number_input("Screen time", key="p1")
    study = st.number_input("Study time", key="p2")
    sleep = st.number_input("Sleep time", key="p3")

    if st.button("Prédire"):
        gpa_pred = model.predict([[screen, study, sleep]])
        st.write("MGP estimé :", round(gpa_pred[0], 2))

else:
    st.warning("Ajoute au moins 3 données pour activer la prédiction.")

