# _*_ coding: utf-8 _*_
from __future__ import division, unicode_literals

def safe(f):
    """ f와 같은 함수를 반환하지만 f에 오류 발생시 무한대 반환 """
    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return float('inf')
    return safe_f

def step(v, direction, step_size):
    return [v_i + step_size * direction_i
            for v_i, direction_i in zip(v, direction)]

def negate(f):
    return lambda *args, **kwargs: -f(*args, **kwargs)

def negate_all(f):
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]

def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    """ 목적 함수를 최소화시키는 theta 를 경사 하강법을 사용해서 찾아줌 """
    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]

    theta = theta_0
    target_fn = safe(target_fn)
    value = target_fn(theta)

    while True:
        gradient = gradient_fn(theta)
        next_thetas = [step(theta, gradient, -step_size)
                        for step_size in step_sizes]

        next_theta = min(next_thetas, key=target_fn)
        next_value = target_fn(next_theta)

        if abs(value - next_value) < tolerance:
            return theta
        else:
            theta, value = next_theta, next_value

def maximize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    return minimize_batch(negate(target_fn)
                          , negate_all(gradient_fn)
                          , theta_0
                          , tolerance)