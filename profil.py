
def demander_note(matiere):
    note= float(input(f"Entrez la note de {matiere} : "))
    while not(0 <= note <= 20):
        print("Erreur, la note doit être comprise entre 0 et 20.")
        note = float(input(f"Entrez la note de {matiere} : "))
    return note

def obtenir_appreciation(moyenne) :
    if moyenne >= 16:
        mention = "Excellent"
    elif moyenne >= 14:
        mention = "Très Bien"
    elif moyenne >= 12:
        mention = "Bien"
    elif moyenne >= 10:
        mention = "Passable"
    else:
        mention = "Insuffisant"
    return mention

def creer_eleve():
    nom = input("Entrez Nom de l'élève : ")

    matieres = ["Mathématiques", "Anglais", "Français", "Espagnol"]

    notes = {}

    for matiere in matieres:
        note = demander_note(matiere)
        notes[matiere] = note

    moyenne = sum(notes.values()) / len(notes)

    appreciation = obtenir_appreciation(moyenne)

    eleve = {
        "Nom" : nom,
        "Notes" : notes,
        "Moyenne" : moyenne,
        "Appréciation" : appreciation,
    }
    return eleve

def afficher_bulletin(eleve) :
    print("\n----------------------------------")
    print(f"Elève : {eleve['Nom']}")

    print("\nNotes :")
    for matiere, note in eleve["Notes"].items():
        print(f" {matiere} : {note}")

    print(f"\nMoyenne : {eleve['Moyenne']:.2f}")
    print(f"Appréciation : {eleve['Appréciation']}")

def afficher_statistique_classe(eleves) :
    total = 0

    for eleve in eleves :
        total += eleve["Moyenne"]

    moyenne_generale = total / len(eleves)

    meilleur_eleve = eleves[0]
    plus_faible = eleves[0]

    for eleve in eleves :
        if eleve["Moyenne"] > meilleur_eleve["Moyenne"] :
            meilleur_eleve = eleve

        if eleve["Moyenne"] < plus_faible["Moyenne"] :
            plus_faible = eleve

    print("\n=====  STATISTIQUE DE LA CLASSE =====")
    print(f"\nLa moyenne générale de la classe est : {moyenne_generale:.2f}")
    print(f"\nMeilleur élève :{meilleur_eleve['Nom']} avec {meilleur_eleve['Moyenne']:.2f}")
    print(f"Elève le plus faible : {plus_faible['Nom']} avec {plus_faible['Moyenne']:.2f}")

nombre_eleves = int(input("Combien d'élèves voulez-vous enregistrer ? : "))
eleves = []

for nombre in range(nombre_eleves):
    eleve = creer_eleve()
    eleves.append(eleve)

print("\n==== BULLETINS ====")

for eleve in eleves :
    afficher_bulletin(eleve)

afficher_statistique_classe(eleves)