# Create a vector
myVect <- c(1,2,3,4,5)

# Print it out to the screen
myVect

# Plot the vector
plot(myVect)

# Find the average
mean(myVect)

# Find the standard deviation
sd(myVect)

# Create a vector that is the square of the myVect vector
myVectSqd = myVect^2

# Now plot this vector in the same plot
plot(myVectSqd)

# Let's clear the plot area and only plot the second vector
plot.new()
plot(myVectSqd)

# Finally find the cross product between the two vectors
crossprod(t(myVect), myVectSqd)

# Just for funsies, let's create a diagonal identity matrix
diag(1, 5)

# What about a different number?
diag(532, 17)

# Find the cross product between a diagonalized matrix and a vector
newVector <- c(2,2,2,2,2,2,2,2,2,2)
crossprod(diag(10,10), newVector)