import json

import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import false


def charger_eleves():
    try:
        with open("eleves.json", "r") as fichier:
            return json.load(fichier)
    except:
        return []


def demander_note(matiere):
    while True:

        try:

            note = float(input(f"Entrez votre note de {matiere}: "))

            if 0 <= note <= 20:
                return note

            print(f"Le note n'est pas valide, elle doit être comprise entre 0 et 20!")


        except ValueError:
            print(f"Entrez un nombre !")


def obtenir_appreciation(moyenne):
    if moyenne < 0 or moyenne > 20:
        return "Moyenne invalide"

    if moyenne >= 18:
        return "Exceptionnel !"
    elif moyenne >= 16:
        return "Excellent !"
    elif moyenne >= 14:
        return "Très Bien !"
    elif moyenne >= 12:
        return "Bien !"
    elif moyenne >= 10:
        return "Passable !"
    else:
        return "Insuffisant !"


def demander_entier(message):
    while True:

        try:
            nombre = int(input(message))

            if nombre >= 0:
                return nombre

            print("Le nombre doit être positif.")

        except ValueError:
            print("Entrez un entier valide.")


def demander_texte(message):
    while True:
        texte = input(message)

        if texte.strip():
            return texte

        print("Erreur : le texte ne peut pas être vide.")


def demander_choix(message):
    while True:
        choix = demander_entier(message)

        if 1 <= choix <= 7:
            return choix

        print("Entrez un chiffre compris entre 1 et 6")

def export_csv_ou_excel(eleves) :
    if len(eleves) == 0 :
        print("Aucun élève à exporter.")
        return

    df = pd.DataFrame(eleves)

    df.to_excel("Rapport_calse_M_IDEA.xlsx", index = False)

    print("\n [SUCCES] Le fichier 'Rapport_Classe_M_IDEA.xlsx' a été généré avec succès !")

def creer_eleve():
    nom = demander_texte("Entrez le nom de l'élève : ")

    matieres = ["Mathématiques", "Anglais", "Français", "Espagnol"]
    notes = {}

    for matiere in matieres:
        note = demander_note(matiere)
        notes[matiere] = note

    moyenne = sum(notes.values()) / len(notes)
    appreciation = obtenir_appreciation(moyenne)

    eleve = {
        "Nom": nom,
        "Notes": notes,
        "Moyenne": moyenne,
        "Appréciation": appreciation

    }
    return eleve


def afficher_bulletin(eleve):
    print("\n----------------------------------------------")
    print(f"\n====== BULLETINS=========")
    print(f" Le nom de l'élève est : {eleve['Nom']}")
    print("\nNotes")
    for matiere, note in eleve["Notes"].items():
        print(f" {matiere} : {note}")
    print(f"\nMoyenne : {eleve['Moyenne']}")
    print(f"Appréciation : {eleve['Appréciation']}")


def calculer_statistique_classe(eleves):
    if len(eleves) == 0:
        print("Aucun élève")
        return

    df = pd.DataFrame(eleves)

    moyenne_generale = df["Moyenne"].mean()

    meilleur_eleve = df.loc[df["Moyenne"].idxmax()]
    plus_faible = df.loc[df["Moyenne"].idxmin()]

    print("\n===== STATISTIQUES DE LA CLASSE =====")
    print(f"Moyenne générale : {moyenne_generale:.2f}/20")
    print(f"Meilleur élève : {meilleur_eleve['Nom']} ({meilleur_eleve['Moyenne']:.2f})")
    print(f"Plus faible élève : {plus_faible['Nom']} ({plus_faible['Moyenne']:.2f})")

def generer_graphique_performances(eleves):
    if len(eleves) == 0 :
        print("Aucun élève pour générer un grpahique.")
        return

    df = pd.DataFrame(eleves)
    plt.figure(figsize = (10,6))
    plt.bar(df["Nom"], df["Moyenne"], color = "skyblue", edgecolor = "blue")

    plt.title("Classement des élèves par Moyenne", fontsize = 14, fontweight = "bold")
    plt.xlabel("Elèves", fontsize = 12)
    plt.ylabel("Moyenne / 20", fontsize = 12)

    plt.axhline(y = 10, color = "red", linestyle = "--", label = "seuil de passage (10/20)")
    plt.legend()

    plt.savefig("Graphisme_Performances_M_IDEA.png", dpi = 300)
    plt.close()

    print("\n[SUCCES] Le graphique automatique 'Graphique_Performances_M_IDEA.png' a été généré")

def sauvegarder_eleves(eleves):
    with open("eleves.json", "w") as fichier:
        json.dump(eleves, fichier, ensure_ascii=False, indent=4)


def supprimer_eleve(eleves):
    nom = input("Nom de l'élève à supprimer : ")

    eleve_a_supprimer = None

    for eleve in eleves:
        if eleve["Nom"] == nom:
            eleve_a_supprimer = eleve

    if eleve_a_supprimer is not None:
        eleves.remove(eleve_a_supprimer)
        print("Elève supprimé.")
    else:
        print("Elève introuvable.")


def modifier_eleve(eleves):
    nom = demander_texte("Nom de l'élève à modifier : ")

    eleve_a_modifier = None

    for eleve in eleves:
        if eleve["Nom"] == nom:
            eleve_a_modifier = eleve

    if eleve_a_modifier is not None:
        for matiere in eleve_a_modifier["Notes"]:
            nouvelle_note = demander_note(matiere)
            eleve_a_modifier["Notes"][matiere] = nouvelle_note

        moyenne = sum(eleve_a_modifier["Notes"].values()) / len(eleve_a_modifier["Notes"])

        eleve_a_modifier["Moyenne"] = moyenne
        eleve_a_modifier["Appréciation"] = obtenir_appreciation(moyenne)
        print(f"Elèves modifié.")


eleves = charger_eleves()

while True:
    print("\n ===========GESTIONNAIRE DE NOTES==========")
    print("\n 1: Ajouter un élève")
    print("\n 2: Afficher les bulletins")
    print("\n 3: Modifier un élève")
    print("\n 4: Supprimer un élève")
    print("\n 5: Afficher les statistiques")
    print("\n 6: Exporter")
    print("\n 7: Quitter")

    choix = demander_choix("Choisissez votre option ! ")

    if choix == 1:
        nombres = demander_entier("Combien d'élèves ??")
        for i in range(nombres):
            eleve = creer_eleve()
            eleves.append(eleve)
        sauvegarder_eleves(eleves)
    elif choix == 2:
        for eleve in eleves:
            afficher_bulletin(eleve)
    elif choix == 3:
        modifier_eleve(eleves)
        sauvegarder_eleves(eleves)
    elif choix == 4:
        supprimer_eleve(eleves)
        sauvegarder_eleves(eleves)
    elif choix == 5:
        calculer_statistique_classe(eleves)
    elif choix == 6:
        export_csv_ou_excel(eleves)
        generer_graphique_performances(eleves)
    elif choix == 7 :
        break
