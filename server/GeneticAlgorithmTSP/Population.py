from GeneticAlgorithmTSP.Route import Route


class Population:
    def __init__(self, popSize, cityList):
        self.popSize = popSize
        self.cityList = cityList
        self.routes, self.fitness = self.initialPopulation()

    def initialPopulation(self):
        population = []
        fitness = []
        for i in range(0, self.popSize):
            r = Route(self.cityList)
            population.append(r.route)
            fitness.append(r.routeFitness())
        return population, fitness
