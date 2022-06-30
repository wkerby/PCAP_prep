import csv
file_name = '/Users/jefferykerby/Desktop/Python/Excel Data/Countries.csv'
with open(file_name) as file_object:
    lines = list(csv.reader(file_object))
    country_population = {}
    for line in lines[1:]:
        country_population[line[0]] = float(line[1])
    #print(country_population)

country_list = list(country_population.keys())
country_index_list = list(range(0,len(country_population.keys())))
population_list = list(country_population.values())

from matplotlib import pyplot as plt
figure = plt.figure(dpi=128,figsize = (10,6))
plt.scatter(country_list, population_list, linewidth = 2, c = 'Blue')
plt.xlabel("Country", fontsize = 16)
plt.ylabel("Population", fontsize = 16)
#plt.show()
figure.autofmt_xdate()


code_list = []
from pygal import i18n
print(country_list)
