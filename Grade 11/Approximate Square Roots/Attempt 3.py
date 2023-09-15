from jax import grad, jit
import jax.numpy as jnp
test = jnp.array([1.0])
sqrt = jnp.array([1.])
@grad
def equation(x, num):
    return jnp.abs(num - x**2)[0]
@jit
def update(grad, weight):
    return weight - grad * 0.5
for i in range(1000):
    s = equation(sqrt, test)
    sqrt = update(s, sqrt)
print(sqrt)