class Player:

    def __innit__(self, name, deck, is_computer=False):
        self.name = name 
        self.deck = deck
        self.is_computer = is_computer

    @property 
    def is_computer(self):
        return self._is_computer
    
    @property
    def deck(self):
        return self._deck
    
    def has_empty_deck(self):
        return self._deck.size == 0
    
    def draw_card(self):
        if not self.has_empty_deck():
            return self.deck.draw()
        else:
            return None
        
    def add_card(self, card): 
        self._deck.add(card)
       