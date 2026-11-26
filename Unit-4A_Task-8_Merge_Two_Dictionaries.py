dict_data = {"a": 1, "b": 2}
dict_extra = {"b": 3, "c": 4}

dict_merged = dict_data.copy()
dict_merged.update(dict_extra)
print("Merged:", dict_merged)