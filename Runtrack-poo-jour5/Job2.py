class Puissance:
    def calculer_puissance(x, n):
        if n == 0:
            return 1
        elif n % 2 == 0:
            return Puissance.calculer_puissance(x, n/2) ** 2
        else:
            return x * Puissance.calculer_puissance(x, n-1)
  
x = int(input("Entrez un nombre x : "))
n = int(input("Entrez un nombre entier n : "))
resultat = Puissance.calculer_puissance(x, n)
print(x, "à la puissance", n, "est égal à", resultat)
