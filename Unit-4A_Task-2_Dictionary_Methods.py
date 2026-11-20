dict_data = {"a": 1, "b": 2, "c": 3}
print("Keys:", dict_data.keys())
print("Values:", dict_data.values())
print("Items:", dict_data.items())
print("get b:", dict_data.get("b"))
print("get z:", dict_data.get("z"))

dict_data.update({"b": 20, "d": 4})
print("After update:", dict_data)

removed = dict_data.pop("a")
print("Removed:", removed)
print("After pop:", dict_data)