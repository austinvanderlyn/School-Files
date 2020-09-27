# geom_smooth confidence interval example
data("nhtemp")
data.frame(year = as.numeric(time(nhtemp)), temperature = as.numeric(nhtemp)) %>%
  ggplot(aes(year, temperature)) +
  geom_point() +
  geom_smooth() +
  ggtitle("Average Yearly Temperatures in New Haven")

# Monte Carlo simulation of confidence intervals
p <- 0.45
N <- 1000
# generate N observations
X <- sample(c(0,1), size = N, replace = TRUE, prob = c(1-p, p))
# calculate X_hat
X_hat <- mean(X)
# calculate SE_hat, SE of the mean of N observations
SE_hat <- sqrt(X_hat*(1-X_hat)/N)
# build interval of 2*SE above and below mean
c(X_hat - 2*SE_hat, X_hat + 2*SE_hat)

# solving for z with qnorm
# calculate z to solve for 99% confidence interval
z <- qnorm(0.995)
# demonstrating that qnorm gives the z value for a given probability
pnorm(qnorm(0.995))
# demonstrating symmetry of 1-qnorm
pnorm(qnorm(1-0.995))
# demonstrating that this z-value gives correct probability for interval
pnorm(z) - pnorm(-z)

# Monte Carlo simulation
B <- 10000
inside <- replicate(B, {
  X <- sample(c(0,1), size = N, replace = TRUE, prob = c(1-p, p))
  X_hat <- mean(X)
  SE_hat <- sqrt(X_hat*(1-X_hat)/N)
  between(p, X_hat - 2*SE_hat, X_hat + 2*SE_hat)
})
mean(inside)
