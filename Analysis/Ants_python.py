import math
import random

#DONE
def euc_2d(c1, c2):
    return round(math.sqrt((c1[0] - c2[0])**2.0 + (c1[1] - c2[1])**2.0))


#DONE
def cost(permutation, cities):
    distance = 0
    for i in range(len(permutation)):
        c2 = permutation[0] if (i == (len(permutation)-1)) else permutation[i+1]
        distance += euc_2d(cities[permutation[i]], cities[c2])
    return distance

#DONE
def random_permutation(cities):
    perm = list(range(len(cities)))
    for i in range(len(perm)):
        r = random.randint(0, len(perm)-(i+1)) + i
        perm[r], perm[i] = perm[i], perm[r]
    return perm

#DONE
def initialise_pheromone_matrix(num_cities, init_pher):
    return [[init_pher]*num_cities]*num_cities

#DONE
def calculate_choices(cities, last_city, exclude, pheromone, c_heur, c_hist):
    choices = []
    for i in range(len(cities)):
        if i not in exclude:
            prob = {'city':i}
            prob['history'] = pheromone[last_city][i] ** c_hist
            prob['distance'] = euc_2d(cities[last_city], cities[i])
            prob['heuristic'] = (1.0/prob['distance']) ** c_heur
            prob['prob'] = prob['history'] * prob['heuristic']
            choices.append(prob)
    return choices

#DONE
def prob_select(choices):
    total = sum(element['prob'] for element in choices)
    if total == 0.0:
        return choices[random.randint(0, len(choices)-1)]['city']
    v = random.random()
    for i in range(len(choices)):
        v -= ((choices[i]['prob'])/total)
        if v <= 0.0:
            return choices[i]['city']
    return choices[-1]['city']



#DONE
def greedy_select(choices):
    return max(choices, key=lambda x:x['prob'])['city']
	

#DONE
def stepwise_const(cities, phero, c_heur, c_greed):
    perm = []
    perm.append(random.randint(0, len(cities)-1))
    while (len(perm) < len(cities)):
        choices = calculate_choices(cities, perm[-1], perm, phero, c_heur, 1.0)
        greedy = (random.random() <= c_greed)
        next_city = greedy_select(choices) if (greedy) else prob_select(choices)
        perm.append(next_city)
    return perm

#DONE
def global_update_pheromone(phero, cand, decay):
    for i in range(len(cand['vector'])):
        y = cand['vector'][0] if (i == (len(cand['vector'])-1)) else cand['vector'][i+1]
        value = ((1.0-decay)*phero[cand['vector'][i]][y]) + (decay*(1.0/cand['cost']))
        phero[cand['vector'][i]][y] = value
        phero[y][cand['vector'][i]] = value
    return None

#DONE
def local_update_pheromone(pheromone, cand, c_local_phero, init_phero):
    for i in range(len(cand['vector'])):
        y = cand['vector'][0] if (i == (len(cand['vector'])-1)) else cand['vector'][i+1]
        value = ((1.0-c_local_phero)*pheromone[cand['vector'][i]][y])+(c_local_phero*init_phero)
        pheromone[cand['vector'][i]][y] = value
        pheromone[y][cand['vector'][i]] = value
    return None

#DONE
def search(cities, max_it, num_ants, decay, c_heur, c_local_phero, c_greed):
    best = {'vector':random_permutation(cities)}
    best['cost'] = cost(best['vector'], cities)
    init_pheromone = 1.0 / (float(len(cities)) * best['cost'])
    pheromone = initialise_pheromone_matrix(len(cities), init_pheromone)
    for iter in range (max_it):
        solutions = []
        for i in range(num_ants):
            cand = {}
            cand['vector'] = stepwise_const(cities, pheromone, c_heur, c_greed)
            cand['cost'] = cost(cand['vector'], cities)
            if (cand['cost'] < best['cost']):
                best = cand
            local_update_pheromone(pheromone, cand, c_local_phero, init_pheromone)
        global_update_pheromone(pheromone, best, decay)
        print(" > iteration #" + str(iter+1) + "; best=" + str(best['cost']))
    return best


# problem configuration
berlin52 = [[565,575],[25,185],[345,750],[945,685],[845,655],
   [880,660],[25,230],[525,1000],[580,1175],[650,1130],[1605,620],
   [1220,580],[1465,200],[1530,5],[845,680],[725,370],[145,665],
   [415,635],[510,875],[560,365],[300,465],[520,585],[480,415],
   [835,625],[975,580],[1215,245],[1320,315],[1250,400],[660,180],
   [410,250],[420,555],[575,665],[1150,1160],[700,580],[685,595],
   [685,610],[770,610],[795,645],[720,635],[760,650],[475,960],
   [95,260],[875,920],[700,500],[555,815],[830,485],[1170,65],
   [830,610],[605,625],[595,360],[1340,725],[1740,245]]


