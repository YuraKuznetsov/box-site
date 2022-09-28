from .models import Prices20, Prices30


class Box:
    def __init__(self, params: dict):
        # Розмір
        self.num1 = 50
        self.length: int = int(params['length'])
        self.width: int = int(params['width'])
        self.height: int = int(params['height'])
        # Параметри
        self.layers: str = params['layers']
        self.mark: str = params['mark']
        self.profile: str = params['profile']
        self.color: str = params['color']
        self.printing: str = params['printing']
        # Ціна з бази
        self.meter_price: float = 0
        # Націнка (%)
        self.markup: int = 20
        # Ціна фарбування ящика
        self.print_cost: float = 0
        # Вартість роботи
        self.work: float = 1
        # Додаткові числа для обрахування площі ящика (на згинах додаються, мабуть)
        self.num1: int
        self.num2: int
        # Площа та ціна ящика
        self.square: float = 0
        self.price: float = 0


    def check_params(self):
        pass


    def find_num1(self):
        """ Визначає перше число """
        if self.profile in ('E', 'B', 'C'):
            self.num1 = 40
        else:
            self.num1 = 50


    def find_num2(self):
        """ Визначає друге число """
        if self.profile == 'E':
            self.num2 = 4
        if self.profile == 'B':
            self.num2 = 6
        if self.profile == 'C':
            self.num2 = 8
        if self.profile == 'EB':
            self.num2 = 12
        if self.profile == 'EC':
            self.num2 = 14
        if self.profile == 'BC':
            self.num2 = 16


    def find_square(self):
        """ Обрахування площі заготовки """
        self.find_num1()
        self.find_num2()
        self.square = ((self.length + self.width) * 2 + self.num1) * (self.width + self.height + self.num2) / 1000000


    def find_meter_price(self):
        if self.layers == "Т":
            self.meter_price = int(Prices20.objects.get(mark=self.mark, profile=self.profile, color=self.color).price)
        else:
            self.meter_price = 0


    def find_print_cost(self):
        if self.printing == '0':
            self.print_cost = 0
        elif self.printing == '1':
            self.print_cost = 0.1
        elif self.printing == '2':
            self.print_cost = 0.2
        else:
            self.print_cost = 1.4 * self.square


    def get_price(self) -> float or str:
        try:
            self.find_meter_price()
        except ValueError:
            return "Не доступно"
        self.find_square()
        self.find_print_cost()
        self.price = (self.square * self.meter_price + self.print_cost + (self.work * self.square)) * \
                     (1 + self.markup / 100)
        return format(round(self.price, 2), '.2f')


    def get_square(self):
        return self.square
