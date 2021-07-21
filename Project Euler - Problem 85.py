store_dict = {}

# Consider drawing two vertical lines in a grid of size (x,y). There are (x+1,Choose,2) choices. Similarly,
# there are (y+1,Choose,2) choices for two horizontal lines.
# Multiplying theses together, gives total number of rectangles.
def count_rectangle(size_x, size_y):
    number_rect = int(0.25 * size_x * (size_x+1) * size_y * (size_y+1))
    return number_rect


def search(target):
    area, store_answers = 0, []
    difference = 1000000000
    x = 2000
    y = 1
    while x >= y:
        num_rect = count_rectangle(x, y)
        if difference > abs(num_rect-target):
            area = x*y
            store_answers = [x, y]
            difference = abs(num_rect - target)

        if num_rect > target:
            x -= 1
        else:
            y += 1
    return area, store_answers


print(search(2000000)[0])
