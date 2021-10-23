import util

def main():
  print("=== running 8queen ===")
  population = []
  for _ in range(100):
    population.append(util.generate_valid_genotype())
  print(population)


if __name__ == "__main__":
  main()
