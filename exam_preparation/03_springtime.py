def start_spring(**kwargs):
    spring_dict = {}
    for key, value in kwargs.items():
        if value not in spring_dict:
            spring_dict[value] = []
        spring_dict[value].append(key)
    sort_dict = dict(sorted(spring_dict.items(), key=lambda x: (x[1]), reverse=True))
    result = [f'{key}: {sorted(value)}' for key, value in sort_dict.items()]

    return result


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }
print(start_spring(**example_objects))