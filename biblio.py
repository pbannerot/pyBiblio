class Document:

    def __init__ (self, titre, isbn):
        self._titre = titre
        self._isbn = isbn

    def __repr__ (self):
        return f"{self._isbn} {self._titre} "

    @property
    def titre (self):
        return self._titre

    @property
    def isbn (self):
        return self._isbn


class Livre (Document):

    def __init__ (self, titre, auteur, isbn):
        Document.__init__ (self, titre, isbn)
        self._auteur = auteur

    def __repr__ (self):
        return f"{Document.__repr__(self)} {self._auteur}"

    @property
    def auteur (self):
        return self._auteur


class Vidéo (Document):

    def __init__ (self, titre, réalisateur, durée, isbn):
        Document.__init__ (self, titre, isbn)
        self._réalisateur = réalisateur
        self._durée = durée

    def __repr__ (self):
        return f"{Document.__repr__(self)} {self._réalisateur} {self._durée}min"

    @property
    def réalisateur (self):
        return self._réalisateur

    @property
    def durée (self):
        return self._durée


class Bibliothèque:

    def __init__ (self):
        self._livres = {}

    def _ajouter_document (self, document):
        liste = self._livres.setdefault (document.isbn, [])
        liste.append (document)

    def ajouter_livre (self, titre, auteur, isbn):
        self._ajouter_document(Livre (titre, auteur, isbn))

    def ajouter_vidéo (self, titre, réalisateur, durée, isbn):
        self._ajouter_document (Vidéo (titre, réalisateur, durée, isbn))

    def listerInventaire (self):
        for isbn in self._livres:
            print (f"{self._livres[isbn][0]} {len (self._livres[isbn])} ex")


if __name__ == "__main__":
    bib = Bibliothèque()
    bib.ajouter_livre (titre="Sapiens", auteur="Harari", isbn="SH123")
    bib.ajouter_livre (titre="Une brève histoire du temps", auteur="Stephen Hawking", isbn="SGxxx")
    bib.ajouter_livre (titre="Sapiens", auteur="Harari", isbn="SH123")
    bib.ajouter_vidéo (titre="ET", réalisateur="Spielberg", durée=123, isbn="SP99")
    bib.listerInventaire()
