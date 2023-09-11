class Card:
    def __init__(self, term, definitions, image=None):
        self.term = term
        self.definitions = definitions
        if (image is None):
            self.image = None
        else:
            self.image = image

    def __str__(self):
        return f"{self.term}: {', '.join(self.definitions)}"
