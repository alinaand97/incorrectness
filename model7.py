# Некорректность

class Car:
    def __init__(self, model, _vin, _numbers):
        self.model = model
        self._vin = self._is_valid_vin(_vin)
        self._numbers = self._is_valid_numbers(_numbers)

    def _is_valid_vin(self, _vin):
        if not isinstance(_vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if _vin < 1000000 or _vin > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return _vin
    def _is_valid_numbers(self, _numbers):
        if not isinstance(_numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(_numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return _numbers

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')