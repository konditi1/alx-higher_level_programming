#!/usr/bin/python3
#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for raw in matrix:
        for element in raw:
            print("{:d}".format(element), end=' ')
        print()
