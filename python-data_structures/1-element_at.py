#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or  idx > (len(my_list)):
        return None
    return my_list[idx]
my_list =[2,4,6,8,10]
idx = 2
print({}.format((idx, element_at(my_list, idx)))
