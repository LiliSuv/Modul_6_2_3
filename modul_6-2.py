class Vehicle:
    __COLOR_VARIANTS = ['red', 'yellow', 'orange', 'green', 'blue', 'purple', 'brown', 'gray', 'white', 'black']
    def get_color_variants(self):
        return self.__COLOR_VARIANTS

    def __init__(self, model, engine_power, color, owner):
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
        self.owner = owner

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'



    def set_color(self, new_color):
        c=[]
        for i in range(len(self.__COLOR_VARIANTS)):
            c.append(self.__COLOR_VARIANTS[i].upper())

        if new_color.upper() in c:
            self.__color = new_color
        else:
            print (f"Нельзя сменить цвет на: {new_color.upper ()}"
                   f'\n{'-' * 40}')
        return self.__color

    def print_info(self):
        print (self.get_model ())
        print (self.get_horsepower ())
        print (self.get_color ())
        print (f'Владелец: {self.owner}'
               f'\n{'-' * 40}')


class Sedan (Vehicle):
    __PASSENGERS_LIMIT=5
    def get_passengers_limit(self):
        return self.__PASSENGERS_LIMIT
    def __init__(self, __model, __engine_power, __color, owner):
        super ().__init__ (__model, __engine_power, __color, owner)



car = Vehicle ('Жигуль', '50000', 'голубой', 'Лили')
car.print_info ()
car.owner = 'Фируз'
car.print_info ()
car.set_color ("red")
car.print_info ()
car.set_color ("re")
car.print_info ()
car.set_color ("rekk")
car.print_info ()
car.set_color ("white")
car.print_info ()
sedan = Sedan ('Жигуль', '50000', 'голубой', 'Лили')
car.print_info ()
sedan.owner = 'Тошка картошка'
sedan.print_info ()
sedan.set_color ("MMM")
sedan.set_color ('BLue')
sedan.print_info ()