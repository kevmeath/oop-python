def make_new_row(old_row):
    """
    Requires:
        -- list old_row that begins and ends with a 1 and has zero or more
            integers in between (has to have at least [1,1])
            OR list [] or [1]
    Returns:
        -- list beginning and ending with a 1 and each interior (non 1)
            integer is the sum of the corresponding old_row elements
            For example if old_row = [1,4,6,4,1], then new_row = [1,5,10,10,5,1],
            i.e. 5=1+4, 10=4+6, 10=6+4, 5=4+1
    """

    if not old_row:  # check for empty row
        return [1]
    elif old_row == [1]:  # check for row 1
        return [1,1]
    else:
        new_row = [1]  # start the new row with 1

        for row_index in range(len(old_row) - 1):
            new_row.append(old_row[row_index] + old_row[row_index+1])  # add next number to the new row

        new_row.append(1)  # end the new row with 1

    return new_row  # return the new row


def make_new_triangle(height):
    """
    Creates a triangle of given height using a list for each row
    Returns the triangle as a list of rows
    """
    new_triangle = []  # make an empty list for the new triangle
    row = []  # start with an empty row to be passed to make_new_row

    for triangle_index in range(height):
        row = make_new_row(row)  # make a new row
        new_triangle.append(row)  # add the new row to the triangle

    return new_triangle  # return the complete triangle


input_height_str = input("Enter desired height of Pascal's Triangle (integer greater than 0): ")  # read height input

while True:  # repeat until an acceptable value is entered
    try:
        input_height_int = int(input_height_str)  # try to convert from string to int
    except ValueError:  # throw exception if the height is not an integer
        input_height_str = input("Please enter an integer: ")  # prompt for an integer
    else:
        if input_height_int > 0:  # check if the height is greater than 0
            break  # break from the loop
        else:
            input_height_str = input("Please enter an integer greater than 0: ")  # prompt for an integer greater than 0

triangle = make_new_triangle(input_height_int)  # make a new triangle of height input_height

print("Printing whole list of lists: ")
print(triangle)  # print the triangle as a list

print("Printing list of lists, one list at a time: ")
for i in range(len(triangle)):  # print each row of the triangle individually
    print(triangle[i])

center_width = len(' '.join([str(i) for i in triangle[input_height_int-1]]))  # use the width of the last row to center

print("Printing as a triangle: ")
for i in range(len(triangle)):
    print((' '.join([str(i) for i in triangle[i]])).center(center_width))  # print the triangle as a centered triangle
