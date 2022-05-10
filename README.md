# TSP-Genetic-Algorithm

### This project aims to use Genetic Algorithms for optimizing the Travelling Salesperson Problem.

The datasets come from TSPLIB, a collection of traveling salseperson problem datasets maintained by ***Gerhard Reinelt*** at [Click Here](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp)
We have chosen a subset of EUC_2D examples as the dataset.

## Genetic Operators Used

**Selection:** Process of selecting two or more parent chromosomes from a given generation of population for mating. Here we have used ***tournament selection***.<br>
**Crossover:** Operation performed on the parents to produce offsprings. Here we have used ***order crossover*** with probability p<sub>c</sub>.<br>
**Mutation:** Permanent change in the sequence of DNA. Here, ***Swap mutation*** is performed with probability p<sub>m</sub><br>



### Running Instructions

1. Run the server using the server [README.md](server/README.md)
2. Run the client using the client [README.md](client/README.md)


### Screenshots

![TSP-1](/screenshots/1.png) <br><br>
![TSP-2](/screenshots/2.png)<br><br>
![TSP-3](/screenshots/3.png)<br><br>
![TSP-4](/screenshots/4.png)<br><br>



### Current known bugs (Might be resolved in future updates)

1. There are file parsing issues for some datasets in the getCitiesFromFile() function in [TSP.py](server/GeneticAlgorithmTSP/TSP.py)
