from GeneticAlgorithmTSP.Population import Population
import random
from GeneticAlgorithmTSP.Route import Route


class GeneticAlgorithm:
    def __init__(self, popSize, cityList, tournament_size=3, pc=0.65, pm=0.1):
        self.tournament_size = tournament_size
        self.population = Population(popSize, cityList)
        self.pc = pc  # crossover probability
        self.pm = pm  # mutation probabaility
        self.fittest = 0
        self.fittest_route = 0
        self.parents = 0
        self.offspring = 0

    def selection(self):
        # Performs tournament selection without replacement of size s
        parents = []
        while len(parents) != self.population.popSize:
            participants = random.sample(
                self.population.fitness, self.tournament_size)
            # get index of fittest participant
            index = self.population.fitness.index(max(participants))

            # add fittest participant to parent list for reproduction
            parents.append(self.population.routes[index])
        # print("Parents:",index_routes(parents,cityList))
        self.parents = parents

    def crossover(self, cityList):
        # Performs order crossover with probability pc
        offspring = []
        # select parents by randomly generating indices
        while len(self.parents) != 0:
            # select mate for gene at position 0 by randomly generating index in range [1,len(parents)-1]
            index = random.randint(1, len(self.parents)-1)
            #print("Index: ",index)
            A = self.parents[0]
            #print("A:,",[cityList.index(city) for city in A])
            B = self.parents[index]
            #print("B:,",[cityList.index(city) for city in B])

            # generate random probability in range [0,1]
            pc = random.uniform(0, 1)

            # check against crossover probability
            if pc <= self.pc:
                # perform crossover
                # generate random crossover point
                crossover_index = random.randint(
                    0, len(cityList)-3)  # window size = 3 cities = 10
                #print("Crossover_index: ",crossover_index)

                # extract cities in selected window
                window_A = A[crossover_index:crossover_index+3]
                window_B = B[crossover_index:crossover_index+3]
                #print("Window A:",[cityList.index(city) for city in window_A])
                #print("Window B:",[cityList.index(city) for city in window_B])
                C = []
                D = []
                i = 0
                j = 0
                # Fill until crossover_index
                while len(C) != crossover_index:
                    if B[i] not in window_A:
                        C.append(B[i])
                    i = i+1
                while len(D) != crossover_index:
                    if A[j] not in window_B:
                        D.append(A[j])
                    j = j+1

                # Append windows
                C = C + window_A
                D = D + window_B

                # Fill remaining positions
                while len(C) != len(cityList):
                    if B[i] not in window_A:
                        C.append(B[i])
                    i = i+1
                while len(D) != len(cityList):
                    if A[j] not in window_B:
                        D.append(A[j])
                    j = j+1

                # Append to offspring
                offspring.append(C)
                offspring.append(D)
            else:
                # no crossover
                offspring.append(A)
                offspring.append(B)

            # remove selected parents from parents array
            self.parents.pop(index)
            self.parents.pop(0)

        self.offspring = offspring
        #print('\nOffspring: ',index_routes(self.offspring,cityList))

    def mutation(self, cityList):
        # Swap mutation is performed with probability pm

        for x in range(len(self.offspring)):
            # Generate mutation probability randomly
            pm = random.uniform(0, 1)
            if pm <= self.pm:
                # mutation occurs
                indexes = [random.randint(0, len(cityList)-1)
                           for i in range(2)]

                route = self.offspring[x]
                #print("Route: ",route)
                city = route[indexes[0]]
                route[indexes[0]] = route[indexes[1]]
                route[indexes[1]] = city
                #print("Mutate route: ",route)

                # Replace with mutated gene
                self.offspring[x] = route
                #print("Mutated offspring:",index_routes(self.offspring,cityList))

    def replacement(self, cityList):
        self.population.routes = self.offspring
        self.population.fitness = []
        for route in self.population.routes:
            r = Route(cityList)
            r.route = route
            r.routeDistance()
            self.population.fitness.append(r.routeFitness())
        self.fittest = max(self.fittest, max(self.population.fitness))
        if self.fittest in self.population.fitness:
            index = self.population.fitness.index(self.fittest)
            self.fittest_route = self.population.routes[index]
        self.offspring = []

        #print("\nGene pool : ",index_routes(self.population.routes,cityList))
        #print("\nFitness : ",self.population.fitness)
        print("\nFittest Individual: ", 1/self.fittest)
        print("\nFittest route: ", [cityList.index(city)
              for city in self.fittest_route])
        return {"Fittest Individual": str(1/self.fittest), "Fittest Route": str([cityList.index(city)
                                                                                 for city in self.fittest_route])}
