# use the range
print(range(3))

# for loop example
dates = [1982, 1980, 1973]
N = len(dates)

for i in range(N):
    print(dates[i])

# example of for loop
for i in range(0,8):
    print(i)

# example of for loop, loop through list
for year in dates:
    print(year)

# use for loop to change the elements in list
squares = ['red', 'yellow', 'green', 'purple', 'blue']
for i in range(0, 5):
    print("Before square", i, 'is', squares[i])
    squares[i] = 'weight'
    print("After square", i, 'is', squares[i])

# loop through the list and iterate on both index and element value
squares = ['red', 'yellow', 'green', 'purple', 'blue']
for i, square in enumerate(squares):
    print(i, square)

# while loop example
dates = [1982, 1980, 1973, 2000]
i = 0
year = 0
while(year != 1973):
    year = dates[i]
    i = i + 1
    print(year)
print("It took", i, "repetitions to get out of loop")