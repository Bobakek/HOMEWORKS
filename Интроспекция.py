import inspect

def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Получаем список всех атрибутов и методов объекта
    all_attributes = dir(obj)

    # Отфильтруем только методы (callable)
    methods = [attr for attr in all_attributes if callable(getattr(obj, attr))]

    # Отфильтруем только атрибуты (не callable)
    attributes = [attr for attr in all_attributes if not callable(getattr(obj, attr))]

    # Получаем модуль, к которому принадлежит объект
    obj_module = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else None

    # Дополнительные свойства (опционально)
    is_class = inspect.isclass(obj)
    is_function = inspect.isfunction(obj)
    is_builtin = inspect.isbuiltin(obj)

    # Формируем словарь с информацией об объекте
    obj_info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module,
        'is_class': is_class,
        'is_function': is_function,
        'is_builtin': is_builtin,
    }

    return obj_info

# Пример использования
number_info = introspection_info(42)
print(number_info)

# Пример с собственным классом
class MyClass:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"Hello, {self.name}!"

my_object = MyClass("NIK")
my_object_info = introspection_info(my_object)
print(my_object_info)
