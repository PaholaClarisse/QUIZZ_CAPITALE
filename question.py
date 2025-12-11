import json
import random
import unicodedata  # pour normaliser le texte : minuscules, sans accents, sans espaces

# Fonction pour normaliser le texte
def normaliser(texte):
    texte = texte.strip().lower()  # enlever les espaces et mettre en minuscules
    texte = unicodedata.normalize('NFD', texte)
    texte = ''.join(c for c in texte if unicodedata.category(c) != 'Mn')  # supprimer les accents
    return texte

# Charger le fichier JSON
with open("quizzCapitale/questionnaire.json", "r", encoding="utf-8") as f:
    all_capitale = json.load(f)

# Afficher les continents disponibles
print("Voici tous les continents disponibles :")
for c in all_capitale.keys():
    print("-", c)

# Demander le continent
print("\nBienvenue dans le quiz des capitales !")
print("Choisissez un continent : Afrique, Amerique, Europe, Asie, Oceanie")
continent_input = input("> ")
continent_normalise = normaliser(continent_input)

# Créer un dictionnaire pour gérer la saisie normalisée
continent_keys = {normaliser(k): k for k in all_capitale.keys()}

if continent_normalise not in continent_keys:
    print("Continent invalide !")
    print("Options possibles :", ", ".join(all_capitale.keys()))
    exit()

# Récupérer les capitales du continent choisi
capitale = all_capitale[continent_keys[continent_normalise]]

# Quiz
score = 0
nombres_question = 10

print(f"\n=== QUIZ: CAPITALES DU CONTINENT {continent_keys[continent_normalise]} ===\n")

for i in range(nombres_question):
    # Choisir un pays au hasard du continent sélectionné
    country = random.choice(list(capitale.keys()))
    bonne_capitale = capitale[country]

    print(f"Question {i+1}: Quelle est la capitale de {country} ?")
    reponse = input("> ")

    if normaliser(reponse) == normaliser(bonne_capitale):
        print("✔ Bonne réponse !\n")
        score += 1
    else:
        print(f"✘ Mauvaise réponse. La capitale de {country} est : {bonne_capitale}\n")

print(f"Ton score final : {score} / {nombres_question}")