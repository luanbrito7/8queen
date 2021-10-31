import random
import util
import math

def run_evolution():
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
  return {
    "iterations": iterations,
    "converged_number": util.converged_number(population),
    "average_fitness": util.average_fitness(population)
  }

def dp(iterations, mean):
  _sum = 0
  for i in iterations:
    _sum += pow((i - mean), 2)
  return math.sqrt(_sum/len(iterations))

def avaliate(iterations):
  total_generations = []
  converged_iterations = 0
  for i in range(iterations):
    res = run_evolution()
    generations = res["iterations"]
    converged_number = res["converged_number"]
    average_fitness = res["average_fitness"]
    print("Average fitness of ", i, " Iteration is: ", average_fitness)
    print("Number of individuals converged in ", i, " Iteration is: ", converged_number)
    total_generations.append(generations)
    if converged_number > 0:
      converged_iterations += 1
  mean = sum(total_generations) / iterations
  res_dp = dp(total_generations, mean)
  print("Generations mean: ", mean)
  print("Generations DP: ", res_dp)
  print("Converged in %", converged_iterations/iterations)


def main():
  avaliate(30)

if __name__ == "__main__":
  main()
