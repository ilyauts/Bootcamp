### Jesse's Bootcamp Week 3

Let's pick up where we left off two weeks ago!

1) Questions from last time?

2) Answer check from last lesson:

[5A] `SELECT year FROM fourth_table ORDER BY injuries DESC LIMIT 1`

[6A] See script

[7A] See script

3) The general approach to solving problems in data science
	A) Split the data that you are given into a:
		I) Training Set
			a) Train your model using this data set
		II) Testing Set
			a) Test your model on this set, see how accurately it can predict the testing set
		III) Evaluation Set
			a) Evaluate the validity of your model based on this set. You should not be able to see this set, this way you don't overfit to the values. 
	B) Such division can be found in online data science competitions like Kaggle
	C) This is just a blue print and can be used with every algorithm
		I) Such as Random Forests

4) Let's install R:

	brew tap homebrew/science
	brew install r

You can access r in terminal by typing `r`. Type `q()` to quit.

5) And R Studio:

	https://download1.rstudio.org/RStudio-1.0.136.dmg

6) Let's use some R: 

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

7) I was going to go into Random Forests this week, but it proved to be a little more complicated and difficult to explain than previously anticipated. We'll leave that until the next lesson. Instead, let's practice some more python and sql skills - without them, nothing is going to get done. 

For Homework:

* Get another dataset and add the data to your database, and follow the same instructions to extrapolate 1 value, and to interpolate another value. Make sure the output is clear. Finally upload your script to github. Oh and play around with RStudio some more!
