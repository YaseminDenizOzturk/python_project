travel = [
    {
        "country": "Turkey",
        "cities": ["Ankara", "İstanbul", "İzmir"],
        "total_visits":3

    },
    {
        "country": "Germany",
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits":6
    },

]

def add_new_country(country_visited , cities_visited , times_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities"] = cities_visited
    new_country["total_visits"] = times_visited
    travel.append(new_country)

add_new_country("France" , ["Paris","Lille","Dijon"] , 4)
print(travel)

