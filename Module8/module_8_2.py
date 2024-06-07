class InvalidDataException(Exception):
    pass


class ProcessingException(Exception):
    pass


def process_data(value):
    try:
        if value < 0:
            raise InvalidDataException("значение меньше нуля")
        elif value == 0:
            raise ProcessingException("значение равно нулю")
        else:
            return value * 2
    except InvalidDataException as e:
        print(f"Ошибка: {e}")
        raise
    except ProcessingException as e:
        print(f"Ошибка обработки: {e}")


try:
    result = process_data(5)
    print(f"Результат обработки данных: {result}")
except InvalidDataException as e:
    print(f"Ошибка в данных: {e}")
except ProcessingException as e:
    print(f"Ошибка обработки данных: {e}")
except Exception as e:
    print(f"Неожиданная ошибка: {e}")
