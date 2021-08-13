# Task 2
# Here is a print function with end param
print("Hello world", end=".")
print("\nThis me, Mario!")
# If the param 'end' was passed previously, the next print() will NOT be on the next line, as it turns out
print('Can', 'youseparete', 'string', 'properly?', end="!", sep=" ")
print(1, 2, 3, 4, 5, sep=",")  # Look! It's a sep param! Wow!

# Task 3
print("#" * 9, "\n#\t#\n#\t#\n#\t#\n#########")
# I wanted to multiply # by 9 again to print last row of letter O
# But it turns out if you do print("..\n", "#" * 9)
# The next row will be not only on the next line, but +1 space, which ruins the output for the task given, weird
print("\n#\t#\n#\t#\n#########\n#\t#\n#\t#")
# All done, hooray!
