####pentru prezentarea mutantiilor la examen
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

    def process_numbers_mutant2(self):
        self.x = self.validate_integer(self.x)
        self.y = self.validate_integer(self.y)

        while self.x >= 10:  # Mutant 1: schimbat > în >=
            self.x = self.x - 10
            if self.x == 10:
                break

        if self.y <= 20 and self.x % 2 == 1:  # Mutant 2: schimbat < în <= și % 2 == 0 în % 2 == 1
            self.y = self.y + 20
        else:
            self.y = self.y - 20

        return 2 * self.x + self.y

#first order         
    def process_numbers_mutant1(self):
        self.x = self.validate_integer(self.x)
        self.y = self.validate_integer(self.y)

        while self.x >= 10:  # Mutant: schimbat > în >=
            self.x = self.x - 10
            if self.x == 10:
                break

        if self.y < 20 and self.x % 2 == 0:
            self.y = self.y + 20
        else:
            self.y = self.y - 20

        return 2 * self.x + self.y

    # high order
    def process_numbers_mutant2(self):
        self.x = self.validate_integer(self.x)
        self.y = self.validate_integer(self.y)

        while self.x >= 10:  # Mutant 1: schimbat > în >=
            self.x = self.x - 10
            if self.x == 10:
                break

        if self.y <= 20 and self.x % 2 == 1:  # Mutant 2: schimbat < în <= și % 2 == 0 în % 2 == 1
            self.y = self.y + 20
        else:
            self.y = self.y - 20

        return 2 * self.x + self.y


    #mutant weak

    def process_numbers_weak(self):
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

        return 2 / self.x + self.y  # Mutant: schimbat * în /
    
    #mutant strong 
    def process_numbers_strong(self):
        self.x = self.validate_integer(self.x)
        self.y = self.validate_integer(self.y)

        while self.x > 10:
            self.x = self.x - 10
            if self.x == 10:
                break

        if self.y < 20 and self.x % 2 == 0:
            self.y = self.y + 20
        else:
            self.y = self.y + 20  # Mutant: schimbat - în +

        return 2 * self.x + self.y
    
    #mutant1 neechivalent
    def process_numbers_neechivalent1(self):
        self.x = self.validate_integer(self.x)
        self.y = self.validate_integer(self.y)

        while self.x >= 10:  # Mutant: schimbat > în >=
            self.x = self.x - 10
            if self.x == 10:
                break

        if self.y < 20 and self.x % 2 == 0:
            self.y = self.y + 20
        else:
            self.y = self.y - 20

        return 2 * self.x + self.y
    
    #mutant2 neechivalent
    def process_numbers_neechivalent2(self):
        self.x = self.validate_integer(self.x)
        self.y = self.validate_integer(self.y)

        while self.x > 10:
            self.x = self.x - 10
            if self.x == 10:
                break

        if self.y <= 20 and self.x % 2 == 0:  # Mutant: schimbat < în <=
            self.y = self.y + 20
        else:
            self.y = self.y - 20

        return 2 * self.x + self.y

