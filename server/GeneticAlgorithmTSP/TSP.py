from http.client import LineTooLong
from GeneticAlgorithmTSP.GeneticAlgorithm import GeneticAlgorithm
import random
from GeneticAlgorithmTSP.City import City
import matplotlib.pyplot as plt
from matplotlib.text import OffsetFrom
import os


def index_routes(routes, cityList):
    return [[cityList.index(city) for city in route] for route in routes]


def cleanDataset():
    filenames = next(os.walk(os.getcwd ()+"/TSP Datasets/"),
                     (None, None, []))[2]  # [] if no file
    print(filenames)
    validDatasetFiles = []
    for filename in filenames:
        if filename.endswith(".tsp"):
            validDatasetFiles.append(filename.split('.')[0])
            filepath = os.getcwd ()+"/TSP Datasets/" + filename
            if "EUC_2D" not in open(filepath).read():
                tour_filepath = os.getcwd ()+"/TSP Datasets/" + \
                    filename.split('.')[0] + ".opt.tour"
                if os.path.exists(filepath):
                    os.remove(filepath)
                if os.path.exists(tour_filepath):
                    os.remove(tour_filepath)
    print(validDatasetFiles)

def getCitiesFromFile(filename):

    filepath = os.getcwd () +"/TSP Datasets/" + filename + ".tsp"
    fileContents = open(filepath, 'r').readlines()[6:-1]
    cityList = []
    for line in fileContents:
        city = [float(s) for s in line.split(" ") if s!=""]
        cityList.append(City(city[1], city[2]))

    return cityList

def generateRandomCities(numberOfCities):
    cityList = []
    for i in range(0, int(numberOfCities)):
        cityList.append(City(x=int(random.random() * 25),
                        y=int(random.random() * 25)))
    return cityList



def findTSPSolution(request):
    ans = {}
    cityList = []
    popSize = int(request["pop_size"])
    n_generations = int(request["n_generations"])
    if request["type"] == "DATASET":
        cityList = getCitiesFromFile(request["value"])
    elif request["type"] == "VALUE":
        cityList = generateRandomCities(request["value"])
    print(cityList)
    ga = GeneticAlgorithm(popSize, cityList)
    ans['Cities'] = str(cityList)
    ans["Initial Population"] = index_routes(ga.population.routes, cityList)
    generation ={}
    for i in range(n_generations):
        print("--------Generation ", i, "-----------")
        ga.selection()
        ga.crossover(cityList)
        ga.mutation(cityList)
        generation["Generation " + str(i)] = ga.replacement(cityList)
    # print(ans)
    ans["Generation Data"] = generation
    X = [cityList[i].x for i in range(len(cityList))]
    y = [cityList[i].y for i in range(len(cityList))]

    fig, ax = plt.subplots()
    ax.scatter(X, y, s=10)
    for i in range(len(cityList)):
        ax.annotate(i, (X[i], y[i]))

    def connectpoints(route, p1, p2, cost):
        x1, x2 = route[p1].x, route[p2].x
        y1, y2 = route[p1].y, route[p2].y
        xmid = (x1+x2)/2
        ymid = (y1+y2)/2
        # ax.plot([x1,x2],[y1,y2])
        c = "{:.2f}".format(cost)
        an1 = ax.annotate('', xy=(x1, y1), xycoords='data', xytext=(x2, y2), textcoords='data',
                          arrowprops=dict(arrowstyle="<-", connectionstyle="arc3"),)
        offset_from = OffsetFrom(an1, (0, 0))
        an2 = ax.annotate(c, (xmid+0.1, ymid))

        # plt.setp(line,linewidth=0.5)
    cost = []
    for i in range(len(ga.fittest_route)-1):
        x1, y1 = ga.fittest_route[i].x, ga.fittest_route[i].y
        x2, y2 = ga.fittest_route[i+1].x, ga.fittest_route[i+1].y
        cost.append(City(x1, y1).distance(City(x2, y2)))
    cost.append(City(ga.fittest_route[0].x, ga.fittest_route[0].y).distance(City(
        ga.fittest_route[len(ga.fittest_route)-1].x, ga.fittest_route[len(ga.fittest_route)-1].y)))
    for i in range(len(ga.fittest_route)-1):
        connectpoints(ga.fittest_route, i, i+1, cost[i])
    connectpoints(ga.fittest_route, len(ga.fittest_route) -
                1, 0, cost[len(ga.fittest_route)-1])
    print("Cost:", cost)
    ans["Cost"] = cost
    parentLoc = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "/client"+"/src/"
    plotLocation = "imgs/" + str(random.randint(0,100000000000000)%1000000007)+".png"
    plt.savefig(parentLoc + plotLocation)
    # plt.show()
    ans["plt"] = plotLocation
    return ans


# findTSPSolution({"type": "VALUE", "value": "5"})
