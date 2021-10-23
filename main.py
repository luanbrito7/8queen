import util

def main():
  print("=== running 8queen ===")
  population = []
  for _ in range(100):
    population.append(util.generate_valid_genotype())
  iterations = 0
  [g,f] = util.highest_fitness(population)
  print(g,f)
  #while(util.solution_found(population) or iterations > 10000):
  #  iterations += 1

if __name__ == "__main__":
  main()
