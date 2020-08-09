# set a=5 and check if condition is true
a = 5
print(a == 6)

# greater than sign
i = 6
print(i > 5)
i = 2
print(i > 5)

# use inequality sign to check value
i = 2
print(i != 6)
i = 6
print(i != 6)

# use equality sign to compare strings
print("ACDC" != "Michael Jackson")

# if statement example
age = 19
if age > 18:
    print("you can enter")
print("move on")

# else statement example
age = 18
if age > 18:
    print("you can enter" )
else:
    print("go see Meat Loaf" )
print("move on")

# elif statement example
age = 18
if age > 18:
    print("you can enter")
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf")
print("move on")

# condition statement example
album_year = 1983
if album_year > 1980:
    print("Album year is greater than 1980")
print('do something..')

# condition statement example
album_year = 1983
if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("less than 1980")
print('do something..')

# condition statement example
album_year = 1980
if(album_year > 1979) and (album_year < 1990):
    print("Album year was in between 1980 and 1989")
print("")
print("Do stuff")

# condition statement example
album_year = 1990
if(album_year < 1980) or (album_year > 1989):
    print("Album was not made in the 1980s")
else:
    print("Album was made in the 1980s")

# condition statement example
album_year = 1983
if not (album_year == '1984'):
    print("Album year is not 1984")