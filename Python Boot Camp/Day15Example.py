class Fraction:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __mul__(self, other):
        new_numer = self.numer * other.numer
        new_denom = self.denom * other.denom
        return Fraction(new_numer, new_denom)

    def __repr__(self):
        return str(self.numer) + "/" + str(self.denom)






class Account:
	total_accounts = 0
	def __init__(self, initial_balance):
		self._balance = initial_balance
		Account.total_accounts += 1
	def balance(self):
		return self._balance

    @staticmethod
    def num_accounts():
        return total_accounts
