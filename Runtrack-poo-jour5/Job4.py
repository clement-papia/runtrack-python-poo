class PlusGrandChiffre:
    def trouver_plus_grand(chiffres):
        if len(chiffres) == 1:
            return chiffres[0]
        else:
            plus_grand = PlusGrandChiffre.trouver_plus_grand(chiffres[1:])
            return chiffres[0] if chiffres[0] > plus_grand else plus_grand
  
chiffres = [int(c) for c in input("Entrez une liste de chiffres : ").split()]
resultat = PlusGrandChiffre.trouver_plus_grand(chiffres)
print("Le plus grand chiffre de la liste", chiffres, "est", resultat)
