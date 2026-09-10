import json
from dataclasses import dataclass
import os


path = "todolist.json" #chemin vers la to do list

@dataclass
class Element: #chaque element d'une to do list 

    Fait: bool #si la tache est faite
    Task: str #contenu de la tache

def charger_to_do_list():
    if os.path.exists(path): #regarde si le chemin existe deja 
        with open(path, "r") as file:
            return json.load(file) #retourne les taches a faire

    else:
        return {} #retourne un dictionnaire vide sinon

def ajouter_tache(tache, liste):
    liste[tache] = False #cree une nouvelle tasche 

#a changer apres pour une classe avec plusieur to do list 
to_do_list = charger_to_do_list()

while True:
    reponse = input("que voulez vous faire ? ecrivez help pour la liste des commandes.  ")

    if reponse == "help":
         print("\n confirmer: indique que la tache a ete effectuee " \
         "\n actualiser: actualise la to do list " \
         "\n ajouter: ajoute un element a la liste " \
         "\n retirer: retire un element de la liste " \
         "\n annuler: indique que la tache n'est pas effectuee " \
         "\n tout effacer: supprime la to do list" \
         "\n quitter: sauvegarde la to do list et quitte le programme")

    if reponse == "ajouter":
        ajouter_tache(input("que voulez vous ajouter ? "), to_do_list)

    if reponse == "confirmer":
        a_confirmer = input("quelle tache voulez vous confirmer ? ")
        if a_confirmer in to_do_list:
            to_do_list[a_confirmer] = True
        else:
            print("Cette tache n'existe pas")

    if reponse == "actualiser":
        with open(path, "w") as file:
                    json.dump(to_do_list, file, indent=4)


    if reponse == "retirer":
        a_retirer = input("quelle tache voulez vous retirer ? ")
        if a_retirer in to_do_list:
            del to_do_list[a_retirer]
        else:
            print("Cette tache n'existe pas")


    if reponse == "annuler":
            a_annuler = input("quelle tache voulez vous annuler ? ")
            if a_annuler in to_do_list:
                to_do_list[a_annuler] = False
            else:
                print("Cette tache n'existe pas")

    if reponse == "tout effacer":
        to_do_list = {}

    if reponse == "quitter":
        with open(path, "w") as file:
            json.dump(to_do_list, file, indent=4)
            exit()