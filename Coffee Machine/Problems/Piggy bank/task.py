class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposite_dollars, deposite_cents):
        if self.cents + deposite_cents >= 100:
            # self.dollars += 1
            # self.cents = 0
            tmp = self.cents + deposite_cents
            tmp_dollars = tmp // 100
            tmp_cents = tmp % 100
            self.cents += tmp_cents - 1
            self.dollars += tmp_dollars
        else:
            self.cents += deposite_cents

        self.dollars += deposite_dollars


# pb = PiggyBank(1,1)
#
# while True:
#     dollars = int(input('Deposite dollars: '))
#     cents = int(input('Deposite cents: '))
#     pb.add_money(dollars, cents)
#     print(f'PiggyBank: {pb.dollars} and {pb.cents}')

