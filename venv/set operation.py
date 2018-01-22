color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
color_list_3=set([item for item in color_list_1 if item not in color_list_2])
print(color_list_3)
