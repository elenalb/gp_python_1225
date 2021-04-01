import json

# сериализация - преобразование данных к json-формату
# десериализация - обратный процесс

# сериализация
# dump(), dumps()
# dict -> object
# list, tuple -> array
# str -> string
# int, float -> number
# True, False -> true, false
# None -> null

data = {
    "data1": {
        "data2": "hello",
        "data3": "world"
    }
}

with open("json_example.json", "w") as f:
    json.dump(data, f)

json_str = json.dumps(data)
print(json_str)
print(type(json_str))

# десериализация
# load(), loads()
with open("json_example.json", "r") as f:
    read_data = json.load(f)
print(read_data)
print(type(read_data))

data_1 = json.loads(json_str)
print(data_1)
print(type(data_1))
