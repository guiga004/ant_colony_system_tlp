from tsp_genetic import *
from parsing import *
from Ants_python import *
import time

file = "qa194.txt"
numOfCities = 194
cityList = []
# print(cityList)

print("\n********** qa194 testing **********\n")

# testing genetic algorithm
print("\n***** Genetic Algorithm *****\n")

for i in range(0, numOfCities):
    cityList.append(City(x=allData[file][i][0], y=allData[file][i][1]))

start = time.time()

# geneticAlgorithmPlot(population=cityList, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)
geneticAlgorithm(population=cityList, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)

end = time.time()
print()
print("Genetic Algorithm Run Time: ", end - start, " seconds")
print()
# testing ant colony algorithm
print("\n***** Ant Colony Algorithm *****\n")


cityList = allData[file]

 # algorithm configuration
max_it = 100
num_ants = 25
decay = 0.1
c_heur = 2.5
c_local_phero = 0.1
c_greed = 0.9

start = time.time()

best = search(cityList, max_it, num_ants, decay, c_heur, c_local_phero, c_greed)
end = time.time()
print()
print("Ant Colony Run Time: ", end - start, " seconds")
print()
print("Done. Best Solution: c=" + str(best['cost']) + " v=" + str(best['vector']))