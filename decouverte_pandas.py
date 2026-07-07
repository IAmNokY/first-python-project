import pandas as pd # "pd" est l'alias universel utilisé par tous les Data Scientists

# 1. On crée une liste de dictionnaires (comme ce que tu as dans ton JSON)
donnees_eleves = [
    {"Nom": "Henoc", "Moyenne": 18.5, "Appreciation": "Excellent !"},
    {"Nom": "Marie", "Moyenne": 14.0, "Appreciation": "Bien !"},
    {"Nom": "Joel", "Moyenne": 09.5, "Appreciation": "Insuffisant"}
]

# 2. La magie Pandas : conversion en DataFrame
df = pd.DataFrame(donnees_eleves)

print("--- APPERÇU DU DATAFRAME ---")
print(df)

print("\n--- STATISTIQUES EN UNE LIGNE ---")
moyenne_classe = df["Moyenne"].mean()
note_max = df["Moyenne"].max()

print(f"Moyenne de la classe : {moyenne_classe}/20")
print(f"Meilleure moyenne : {note_max}/20")