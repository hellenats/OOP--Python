class Account:
    def __init__(self, id, balance, pin):
        self.__id = id
        self.balance = balance
        self.__pin = pin

    @staticmethod
    def wrong_pin():
        return 'Wrong pin'

    def get_id(self, pin):
        if pin == self.__pin:
            return self.__id
        return self.wrong_pin()

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "Pin changed"
        return self.wrong_pin()


account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))
print(account._Account__pin)
