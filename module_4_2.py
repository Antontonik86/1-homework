def test_function():        # 1
    def inner_function():   # 2
        print("Я в области видимости функции test_function")

    inner_function()        # 3 - здесь ничего не возвращает

inner_function()  # ЗДЕСЬ НЕ РАБОТАЕТ! (ошибка)
# Вызов функци inner_function() вне функции test_function приводит к появлению ошбики -
# NameError: name 'inner_function' is not defined
# вследствие различия пространства имён, т.к.  мы не можем доставать значения внутри функции (извне)

test_function()     # Здесь - работает :-)