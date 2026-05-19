n=3
for i in range(n):
    #65 is ASCII value for 'A'
    char=chr(65+i)
    row=" ".join([char]*(i+1))

    #calculate the exact total width of the bottom row
    max_width = 2 * n - 1

    #center the row perfectly
    print(row.center(max_width))