# double quotes define a string
s <- "Hello!"
# single quotes define a string
s <- 'Hello!'
# string parsing for inches
s <- '10"'
cat(s)
# to correctly parse feet and inches
s <- '5\'10"'
# to correctly parse feet and inches 2
s <- "5'10\""
cat(s)
