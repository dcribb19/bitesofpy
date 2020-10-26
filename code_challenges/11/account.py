from functools import total_ordering


@total_ordering
class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    # add dunder methods below
    def __add__(self, transaction):
        if not isinstance(transaction, int):
            raise ValueError
        self._transactions.append(transaction)

    def __sub__(self, transaction):
        if not isinstance(transaction, int):
            raise ValueError
        self._transactions.append(-transaction)

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __iter__(self):
        yield from self._transactions

    def __str__(self):
        return f'{self.name} account - balance: {self.balance}'
