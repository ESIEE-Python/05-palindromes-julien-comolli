"""
Module palindrôme.
"""

def ispalindrome(p):
    """
    Retourne vrai si la chaîne spécifiée est un palindrôme.
    """
    reverse = p[::-1].lower()
    tr = reverse.maketrans("àâäçéèêëîïôöùûüÿ", "aaaceeeeiioouuuy", " '-?!;,.:")

    print(reverse)
    print(p.lower().translate(tr))
    if p.lower().translate(tr) == reverse.translate(tr):
        return True
    return False


def main():
    """
    Fonction principale.
    """
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
