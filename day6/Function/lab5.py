# Write a function called show_stars(rows). If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****

# number of rows
rows = 5
for i in range(0, rows):
    # nested loop for each column
    for j in range(0, i + 1):
        # print star
        print("*", end=' ')
    # new line after each row
    print("\lr")
