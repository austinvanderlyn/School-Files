# function example: add 1 to a and store as b
def add(a):
    b = a + 1
    print(a, "if you add one", b)
    return(b)

# get help on add function
help(add)

# call the add function
add(1)
add(2)

# define a function for multiple numbers
def Mult(a, b):
    c = a * b
    return(c)

# use Mult function to multiply 2 and 3
print(Mult(2, 3))

# use mult to multiply two floats
print(Mult(10.0, 3.14))

# use Mult to multiply two different type values together
print(Mult(2, "Michael Jackson "))

# function definition
def square(a):
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c)
    return(c)

# initializes global variable
x = 3
y = square(x)
print(y)
print(square(2))

# define functions, one with return value None and other without return value
def MJ():
    print('Michael Jackson')
def MJ1():
    print('Michael Jackson')
    return(None)

# define the function for combining strings
def con(a, b):
    return(a + b)

# test the con() function
print(con("This ", "is"))

# a and b calculation block 1
a1 = 4
b1 = 5
c1 = a1 + b1 + 2 * a1 * b1 - 1
if(c1 < 0):
    c1 = 0
else:
    c1 = 5
print(c1)

# a and b calculation block 2
a2 = 0
b2 = 0
c2 = a2 + b2 + 2 * a2 * b2 - 1
if(c2 < 0):
    c2 = 0
else:
    c2 = 5
print(c2)

# make a function for the calculation above
def Equation(a, b):
    c = a + b + 2 * a * b - 1
    if(c < 0):
        c = 0
    else:
        c = 5
    return(c)

# block 3 calculation
a1 = 4
b1 = 5
c1 = Equation(a1, b1)
print(c1)

# block 4 calculation
a2 = 0
b2 = 0
c2 = Equation(a2, b2)
print(c2)

# print function
album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5]
print(album_ratings)

# the sum function
print(sum(album_ratings))

# show the length of the list
print(len(album_ratings))

# function example
def type_of_album(artist, album, year_released):
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)

# print the list
def PrintList(the_list):
    for element in the_list:
        print(element)

# implement print list
PrintList(['1', 1, 'the man', "abc"])

# setting param with default value
def isGoodRating(rating = 4):
    if(rating < 7):
        print("this album sucks it's rating is", rating)
    else:
        print("this album is good its rating is", rating)

# test the value with default ratings
isGoodRating(5)
isGoodRating(10)

# example of global variable
artist = "Michael Jackson"
def printer1(artist):
    internal_var = artist
    print(artist, "is an artist")
printer1(artist)

# create global variables within a function
artist = "Michael Jackson"
def printer(artist):
    global internal_var
    internal_var = "Whitney Houston"
    print(artist, "is an artist")
printer(artist)
printer(internal_var)

# example of global variable
myFavouriteBand = "AC/DC"
def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0
print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is:", getBandRating("Deep Purple"))
print("My favourite band is:", myFavouriteBand)



