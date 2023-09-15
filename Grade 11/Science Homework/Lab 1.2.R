temp_vec <- c(20.9, 20.6, 20.2, 21.6, 20.3, 21.1)
fun <- function(vector, bool=FALSE) {
  print(var(vector))
  print(sqrt(var(vector)))
  if (bool){
    print(var(vector)/mean(vector) * 100)
    print(sqrt(var(vector))/mean(vector) * 100)
  }
}
fun(temp_vec)

# Getting pH variance
pH_vec <- c(8.09, 8.45, 8.28, 7.53, 8.14, 8.46)
fun(pH_vec)

# Getting the Dissolved Oxygen:
Dissolved_oxygen <- c(6.54, 6.93, 6.93, 3.60, 5.05, 6.09)
fun(Dissolved_oxygen)

# Getting the conductivity:
cond_vec <- c(3550.0, 1128, 839, 116, 354, 470)
fun(cond_vec, TRUE)
