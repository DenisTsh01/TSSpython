class NumberProcessor:
    def __init__(self, x, y):
        """Inițializarea clasei NumberProcessor cu valori hardcodate pentru x și y."""
        self.x = x  # Valoare hardcodată pentru x
        self.y = y  # Valoare hardcodată pentru y

    def validate_integer(self, value):
        """Metodă care validează dacă o valoare este un întreg."""
        if not isinstance(value, int):
            raise ValueError("Valoarea trebuie să fie un număr întreg.")
        return value

    def process_numbers(self):
        """Metodă care procesează numerele x și y conform logicii specificate."""
        # Validăm că valorile hardcodate sunt întregi
        self.x = self.validate_integer(self.x)
        self.y = self.validate_integer(self.y)

        while self.x > 10:
            self.x = self.x - 10
            if self.x == 10:
                break

        if self.y < 20 and self.x % 2 == 0:
            self.y = self.y + 20
        else:
            self.y = self.y - 20

        return 2 * self.x + self.y
