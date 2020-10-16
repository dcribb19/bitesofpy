from dataclasses import dataclass, field
from typing import List, NamedTuple

Bracket = NamedTuple("Bracket", [("end", int), ("rate", float)])
Taxed = NamedTuple(
    "Taxed",
    [("amount", float), ("rate", float), ("tax", float)]
    )
BRACKET = [
    Bracket(9_700, 0.1),
    Bracket(39_475, 0.12),
    Bracket(84_200, 0.22),
    Bracket(160_725, 0.24),
    Bracket(204_100, 0.32),
    Bracket(510_300, 0.35),
    Bracket(510_301, 0.37),
]


@dataclass
class Taxes:
    """
    Taxes class
    Given a taxable income and optional tax bracket, it will
    calculate how much taxes are owed to Uncle Sam.
    """
    income: int
    bracket: List[NamedTuple] = field(default_factory=list)
    tax_amounts: List[NamedTuple] = field(default_factory=list)

    def __post_init__(self):
        if self.bracket == []:
            self.bracket = BRACKET
        self.taxes

    def __str__(self) -> str:
        """Summary Report

        Returns:
            str -- Summary report

            Example:

                      Summary Report
            ==================================
             Taxable Income:        40,000.00
                 Taxes Owed:         4,658.50
                   Tax Rate:           11.65%
        """
        title = f'{"Summary Report":^34}'
        line = '=' * 34
        income = f'{"Taxable Income:":>16}{self.income:>17,.2f}'
        owed = f'{"Taxes Owed:":>16}{self.total:>17,.2f}'
        rate = f'{"Tax Rate:":>16}{self.tax_rate:>16.2f}%\n'
        return '\n'.join([title, line, income, owed, rate])

    def report(self):
        """Prints taxes breakdown report"""
        s = str(self)
        breakdown = f'{"Taxes Breakdown":^34}'
        line = '=' * 34

        taxes = '\n'.join([
            f'{amt.amount:>12.2f} x {amt.rate:.2f} ={amt.tax:>13,.2f}'
            for amt in self.tax_amounts
            ])

        s_line = '-' * 34
        total = f'{"Total =":>21}{self.total:>13,.2f}'
        print('\n'.join([s, breakdown, line, taxes, s_line, total]))

    @property
    def taxes(self) -> float:
        """Calculates the taxes owed

        As it's calculating the taxes,
        it is also populating the tax_amounts list
        which stores the Taxed named tuples.

        Returns:
            float -- The amount of taxes owed
        """
        if self.total != 0:
            return self.total
        else:
            taxable = self.income
            last_end = 0

            for level in self.bracket:
                if level == self.bracket[-1]:
                    self.tax_amounts.append(
                        Taxed(
                            amount=taxable - level.end,
                            rate=level.rate,
                            tax=(taxable - level.end) * level.rate
                        )
                    )
                elif taxable > level.end:
                    self.tax_amounts.append(
                        Taxed(
                            amount=level.end - last_end,
                            rate=level.rate,
                            tax=(level.end - last_end) * level.rate
                        )
                    )
                    last_end = level.end
                else:  # if taxable < level.end:
                    self.tax_amounts.append(
                        Taxed(
                            amount=taxable - last_end,
                            rate=level.rate,
                            tax=(taxable - last_end) * level.rate
                        )
                    )
                    break
            return self.taxes

    @property
    def total(self) -> float:
        """Calculates total taxes owed

        Returns:
            float -- Total taxes owed
        """
        return sum([x.tax for x in self.tax_amounts])

    @property
    def tax_rate(self) -> float:
        """Calculates the actual tax rate

        Returns:
            float -- Tax rate
        """
        return round(self.total / self.income * 100, 2)


if __name__ == "__main__":
    salary = 40_000
    t = Taxes(salary)
    t.report()
