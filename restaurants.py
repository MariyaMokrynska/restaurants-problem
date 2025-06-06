def most_varied_visitor(visits):
    dict_names = {}
    for key, values in visits.items():
        set_values = set(values)
        for name in set_values:
            dict_names[name] = dict_names.get(name, 0) + 1
    return max(dict_names, key=dict_names.get)


visits_1 = {
    "Spicy City": ["Eliza"],
    "La Especial Norte": ["Eliza"],
    "Sushi Kashiba": ["Xinting"],
}
assert most_varied_visitor(visits_1) == "Eliza"

visits_2 = {
    "Spicy City": ["Auberon", "Elora"],
    "La Especial Norte": ["Elora", "Auberon", "Rowan"],
    "Sushi Kashiba": ["Xinting", "Aisha", "Xinting"],
    "Lyon's Grocery": ["Auberon", "Xinting", "Sam", "Xinting"],
    "Applebee's": ["Sam", "Eliza"],
}
assert most_varied_visitor(visits_2) == "Auberon"

visits_3 = {
    "Spicy City": ["Elora", "Elora", "Elora"],
}
assert most_varied_visitor(visits_3) == "Elora"
print("All tests passed! If time remains, discuss time/space complexity")
