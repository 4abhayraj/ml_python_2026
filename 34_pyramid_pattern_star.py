rows=5
for i in range(rows):
    row=("* "*(i+1))

    max_width=(3*rows)-1
    print(row.center(max_width))