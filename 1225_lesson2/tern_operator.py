# тернарный оператор
# condition_if_true if condition else condition_if_false

is_true = True
var = 1 if is_true else 0
print(var)

# (condition_if_false, condition_if_true)[condition]
var = (0, 1)[is_true]
print(var)

print(True or "some value")
print(False or "some value")

func_return = None
message = func_return or "Функция ничего не вернула"
print(message)
