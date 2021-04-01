"""
Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию
об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""
goods_num = int(input('Введите кол-во товаров: '))
goods_list = []
names = []
prices = []
qty = []
unit = []
n = 1
while goods_num >= n:
    goods_dict = {'Название': input('Название '), 'цена': input('цена '), 'кол-во': input('кол-во '), 'ед': input('ед ')}
    names.append(goods_dict.get('Название'))
    prices.append(goods_dict.get('цена'))
    qty.append(goods_dict.get('кол-во'))
    unit.append(goods_dict.get('ед'))
    goods_tuple = (n, goods_dict)
    goods_list.append(goods_tuple)
    n += 1

print(goods_list)
analytics = {'название': names, 'цена': prices, 'кол-во': qty, 'ед': unit}
print(f'Аналитика: {analytics}')
