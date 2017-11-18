# _*_ coding: utf-8 _*_

from matplotlib import pyplot as plt 

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# 막대의 기본 너비가 0.8 이므로 0.1을 밀어줘서 가운데 오도록 해줌
xs = [i + 0.1 for i, _ in enumerate(movies)]

plt.bar(xs, num_oscars)
plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")

plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
plt.show()