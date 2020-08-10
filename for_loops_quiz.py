# write a for loop printing out all the values between -5 and 5 using the range function
for i in range(-5, 6):
    print(i)

# print elements of the following list:
Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for genre in Genres:
    print(genre)

# write a for loop that prints out the following squares:
squares=['red', 'yellow', 'green', 'purple', 'blue']
for square in squares:
    print(square)

# while loop example
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 1
Rating = PlayListRatings[0]
while (Rating >= 6):
    print(Rating)
    Rating = PlayListRatings[i]
    i = i + 1

# while loop example
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print(new_squares)



