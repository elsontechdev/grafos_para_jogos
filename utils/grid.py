
def display_grid(grid):
    print()
    for row in grid:
        for tile in row:
            print(tile, end="\t")
        print('\n')