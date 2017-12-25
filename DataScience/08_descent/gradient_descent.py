# _*_coding: utf-8 _*_
from __future__ import division, unicode_literals
from collections import Counter
import math, random
import matplotlib.pyplot as plt

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def vector_subtract(v, w):
    """subtracts two vectors componentwise"""
    return [v_i - w_i for v_i, w_i in zip(v,w)]

def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
   return math.sqrt(squared_distance(v, w))

def difference_quotient(f, x, h):
    """ 미분 함수"""
    return (f(x + h) - f(x)) / h

def square(x):
    return x * x

def derivative(x):
    return 2 * x

def partial_difference_quotient(f, v, i, h):
    """ i번째 편도함수가 v에서 가지는 값"""
    w = [v_j + (h if j == i else 0)
            for j, v_j in enumerate(v)]

    return (f(w) - f(v)) / h

def estimate_gradient(f, v, h=0.00001):
    return [partial_difference_quotient(f, v, i, h)
            for i, _ in enumerate(v)]

def step(v, direction, step_size):
    """ v에서 step_size 만큼씩 이동"""
    return [v_i + step_size * direction_i
            for v_i, direction_i in zip(v, direction)]

def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]

v = [random.randint(-10, 10) for i in range(3)]

print("v: %s" % v)
tolerance = 0.0000001

while True:
    gradient = sum_of_squares_gradient(v)
    print("gradient: %s" % gradient)
    next_v = step(v, gradient, -0.01)
    print("next: %s" % next_v)
    if distance(next_v, v) < tolerance:
        break
    v = next_v

print(v)
"""
derivative_estimate = lambda x: difference_quotient(square, x, h=0.00001)

x = range(10)

plt.title("Actual Derivatives vs. Estimates")
plt.plot(x, map(derivative, x), 'rx', label="Actual")
plt.plot(x, map(derivative_estimate, x), 'b+', label="Estimate")
plt.legend(loc=9)
plt.show()
"""
