# Локальные переменные


class Auto:
    def on_auto_start(self):
        info = "Заводим автомобиль"
        return info


a = Auto()
info = a.on_auto_start()
print(info)


# Глобальные переменные


class Auto1:
    info_1 = "Автомобиль заведен"

    def on_auto_start(self):
        info_2 = "Автомобиль заводится"
        return info_2


a1 = Auto1()
print(a1.info_1)
