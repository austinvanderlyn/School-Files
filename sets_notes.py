# create a set
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set1)

# create a set from a list
album_list = ["Michael Jackson", "Thriller", 1982, "00:42:19",
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)
print(album_set)

# create a set of genres
music_genres = {"pop", "pop", "rock", "folk rock", "hard rock", "soul",
                "progressive rock", "soft rock", "R&B", "disco"}
print(music_genres)

# sample set
A = {"Thriller", "Back in Black", "AC/DC"}
print(A)

# add element to set
A.add("NSYNC")
print(A)

# remove element from set
A.remove("NSYNC")
print(A)

# verify that the element is in set
print("AC/DC" in A)

# sample sets
album_set1 = {"Thriller", 'AC/DC', 'Back in Black'}
album_set2 = {"AC/DC", "Back in Black", "The Dark Side of the Moon"}

# print two sets
print(album_set1, album_set2)

# find the intersection
intersection = album_set1 & album_set2
print(intersection)

# find the difference in set1 but not set 2
diff = album_set1.difference(album_set2)
print(diff)

# find the union of two sets
union = album_set1.union(album_set2)
print(union)

# check if superset
print(set(album_set1).issuperset(album_set2))

# check if subset
print(set(album_set2).issubset(album_set1))

