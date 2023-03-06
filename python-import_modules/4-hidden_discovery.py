#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    names_list = dir(hidden_4)
    for hid in hidden:
        if hid[0] != '_':
            print("{}".format(hid))
