# Application de gestion des tâches - Version 1 (sans recherche)

taches = []  # liste des titres de tâches


def afficher_menu():
    print()
    print("=== GESTION DES TÂCHES ===")
    print("1. Ajouter une tâche   2. Afficher   0. Quitter")


def ajouter_tache():
    titre = input("Titre de la tâche : ").strip()
    if titre == "":
        print("Erreur : le titre ne peut pas être vide.")
    else:
        taches.append(titre)
        print("Tâche ajoutée avec succès.")


def afficher_taches():
    if len(taches) == 0:
        print("Aucune tâche pour le moment.")
    else:
        for i in range(len(taches)):
            print(f"{i + 1}. {taches[i]}")


def main():
    choix = ""
    while choix != "0":
        afficher_menu()
        choix = input("Votre choix : ").strip()
        if choix == "1":
            ajouter_tache()
        elif choix == "2":
            afficher_taches()
        elif choix == "0":
            print("Au revoir !")
        else:
            print("Choix invalide, veuillez réessayer.")


main()
