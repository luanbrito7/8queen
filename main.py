import random
import util

def main():
  print("=== running 8queen ===")
  population = []
  for _ in range(100):
    population.append(util.generate_valid_genotype())
  iterations = 0
  [g,f] = util.highest_fitness(population)
  while(iterations <= 10000 and not util.solution_found(population)):
    #Crossover
    crossover_prob = random.random()
    if(crossover_prob <= 0.9):
      parents = util.best_two_of_random_five(population)
      childs = util.crossover_cut_and_crossfill(parents[0],parents[1])
      population.extend(childs)
    #Mutation
    mutation_prob = random.random()
    if(mutation_prob <= 0.4):
      chosen_index = random.randint(0,len(population)-1)
      chosen_one = population.pop(chosen_index)
      chosen_one = util.mutation_switch_genes(chosen_one)
      population.append(chosen_one)
    #Selection
    for _ in range(len(population)-100):
      population.pop(util.smallest_fitness(population)[0])

    iterations += 1
  
  print('Best Answer: ', util.highest_fitness(population))
  print("Generations computed: ", iterations)

if __name__ == "__main__":
  main()
