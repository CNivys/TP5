def calculer_salaire(heures_travaillees, salaire_horaire):
    salaire = min(heures_travaillees, 160) * salaire_horaire

    if heures_travaillees > 160:
        salaire += (min(heures_travaillees, 200) - 160) * salaire_horaire * 0.25

    if heures_travaillees > 200:
        salaire += (heures_travaillees - 200) * salaire_horaire * 0.50

    return salaire

n = int(input("Entrer le nombre d'heure travaillée: "))
salaire = calculer_salaire(n, 11.07)
print(round(salaire,2))