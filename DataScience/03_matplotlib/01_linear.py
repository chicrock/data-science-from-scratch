# _*_ coding: utf-8 _*_

from matplotlib import pyplot as plt 

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14968.3]

# x축 연도, y축 gdp 인 선 그래프
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

plt.title("Nominal GDP")

plt.ylabel("Billions of $")
plt.xlabel("Years")

plt.show()