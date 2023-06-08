#!/usr/bin/python3

if __name__ == '__main__':
    import hidden_4
    names_in_hidden = dir(hidden_4)
    for name in names_in_hidden:
        if not name.startswith('__'):
            print(name)
