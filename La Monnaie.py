amount = int(input("Somme à décomposer : "))
nb_100 = amount // 100
remainder = amount % 100
nb_50 = remainder // 50
remainder = remainder % 50
nb_10 = remainder // 10
remainder = remainder % 10

nb_2 = remainder // 2
remainder = remainder % 2
nb_1 = remainder

print("{} euros, c'est donc {} billets de 100, {} de 50, {} de 10, {} pièces de 2 et {} pièce de 1.".format(amount, nb_100, nb_50, nb_10, nb_2, nb_1))