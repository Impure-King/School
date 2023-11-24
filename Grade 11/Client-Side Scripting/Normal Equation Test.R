# Sample data
x <- c(20, 2, 3, 4, 5)
y <- c(1.2, 3.1, 7.0, 12.5, 20.2)

# Create a design matrix for the quadratic model
X <- cbind(1, x, x^2)

# Use the normal equation to estimate coefficients
coefficients <- solve(t(X) %*% X) %*% t(X) %*% y
cat(coefficients)
for (i in 1:5){
  xs <- x[i]
  y[i] <- coefficients[3] * xs^2 + coefficients[2] * xs + coefficients[1]
}
cat(y)
