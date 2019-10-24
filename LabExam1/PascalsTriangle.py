def make_new_row(old_row):
    """Requires:
           -- list old_row that begins and ends with a 1 and has zero or more
              integers in between (has to have at least [1,1])
           Returns:
           -- list beginning and ending with a 1 and each interior (non 1)
              integer is the sum of the corresponding old_row elements
              For example if old_row = [1,4,6,4,1], then new_row = [1,5,10,10,5,1],
              i.e. 5=1+4, 10=4+6, 10=6+4, 5=4+1 """

    new_row = [1]
    for i in range(len(old_row) - 1):
        new_row.append(old_row[i] + old_row[i+1])

    new_row.append(1)

    return new_row


row_1 = [1, 1]
row_2 = make_new_row(row_1)
print(row_2)
