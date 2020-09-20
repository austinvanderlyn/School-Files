# N represents the number of people polled
N <- 25

# Create a variable p that contains 100 proportions ranging from 0 to 1 using the seq functions
p <- seq(0, 1, length.out = 100)

# create a variable se that contains the standard error of each sample average
se <- sqrt((p*(1-p))/N)

# plot p on the x-axis and se on the y-axis
plot(p, se, ylim = c(0,0.1))

# the vector p contains proportions of Democrats ranging from 0 to 1 using the seq function
p <- seq(0, 1, length = 100)

# the vector 'sample sizes' contains the three sample sizes
sample_sizes <- c(25, 100, 1000)

# Write a for-loop that calculates the standard error `se` for every value of `p` for each of the three samples sizes `N` in the vector `sample_sizes`. Plot the three graphs, using the `ylim` argument to standardize the y-axis across all three plots.
for(N in sample_sizes){
  se <- sqrt(p*(1-p)/N)
  plot(p, se, ylim = c(0, 0.1))
}

# Say the actual proportion of Democratic voters is p=0.45. In this case, the Republican party is winning by a relatively large margin of d=???0.1, or a 10% margin of victory. What is the standard error of the spread 2X¯???1 in this case?
# 'N' represents the number of people polled 
N <- 25

# 'p' represents the proportion of Democratic voters
p <- 0.45

# Calculate the standard error of the spread.
se <- 2*sqrt((p*(1-p)/N)

             