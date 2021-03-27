import json

def item_name():
    with open('testleroyj.json', 'r', encoding='utf-8') as f:
        test = json.load(f)
        rez = test['displayedName']['displayedName']['value']
    return f'Название товара: {rez}'

def shop_list():
    with open('testleroyj.json', 'r', encoding='utf-8') as f:
        test = json.load(f)
        dict_shops = test['stock']['stocks']['34']
        shops = []
        for k, v in dict_shops.items():
            if int(v) > 0:
                shops.append(int(k))
    return f'Список номеров магазинов в которых есть товары в в наличии: {shops}'

def max_items():
    with open('testleroyj.json', 'r', encoding='utf-8') as f:
        test = json.load(f)
        dict_shops = test['stock']['stocks']['34']
        shops = []
        items_s = []
        for k, v in dict_shops.items():
            shops.append(int(k))
            items_s.append(int(v))
        result = []
        max = sorted(items_s, reverse= True)[0]
        res = {k : v for k, v in dict_shops.items() if int(v) == max}
    return f'Максимальное количество товара в регионе: номер магазина - {res}'

print(item_name())
print(shop_list())
print(max_items())
