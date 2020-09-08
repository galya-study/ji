# Страны и города
# Дан список стран и городов каждой страны. 
# Затем даны названия городов. Для каждого 
# города укажите, в какой стране он находится.

count_countries_cities = int(input())
cities = dict()

for i in range(count_countries_cities):
    countries_cities = [str(i) for i in input().split()]
    for i in range(1, len(countries_cities)):
        cities[countries_cities[i]] = countries_cities[0]

count_cities = int(input())
for i in range(count_cities):
    print(cities[str(input())])