import random


class Route:  # Chromosome
    def __init__(self, cityList):
        self.cityList = cityList
        self.route = self.createRoute()
        self.distance = self.routeDistance()
        self.fitness = self.routeFitness()

    def createRoute(self):
        route = random.sample(self.cityList, len(self.cityList))
        return route

    def routeDistance(self):
        pathDistance = 0
        for i in range(0, len(self.route)-1):
            fromCity = self.route[i]
            toCity = None
            if i + 1 < len(self.route):
                toCity = self.route[i + 1]
            else:
                toCity = self.route[0]
            pathDistance += fromCity.distance(toCity)
        return pathDistance

    # Fitness function = inverse of path distance i.e. maximize fitness=> minimum path length
    def routeFitness(self):
        fitness = 1 / float(self.distance)
        return fitness
