import random

def binary_to_decimal(val):
  return int(val, 2)

def dec_to_bin(x):
  return int(bin(x)[2:]) 

def diagonal_cross(q1_row, q1_col, q2_row, q2_col):
  row_vec = q1_row - q2_row
  col_vec = q1_col - q2_col
  return abs(row_vec) == abs(col_vec)

def get_penality(genotype, queen_index):
  penality = 0
  # our representation assumes that 2 queens can't be in the same column or row
  # so the column of a queen is represented by it's genotype relative index (index/3)
  # and the row value is represented by value genotype[index:index+3]
  queen_row = binary_to_decimal(genotype[queen_index:queen_index+3])
  queen_column = int(queen_index/3)
  # only compute penality from index to end
  # to avoid compute same penality twice
  for i in range(queen_index, len(genotype), 3):
    neib_queen_column = int(i/3)
    neib_queen_row = binary_to_decimal(genotype[i:i+3])
    if queen_column == neib_queen_column:
      # it self
      continue
    else:
      # we don't verify if there is a column collision because
      # in our representation each queen is in one specific column
      if diagonal_cross(queen_row, queen_column, neib_queen_row, neib_queen_column):
        penality += 1
  return penality

def get_fitness(genotype):
  total_penality = 0
  # because each queen is represented by a 3-len binary we use this step
  # loop to traverse genotype
  for i in range(0, len(genotype), 3):
    total_penality += get_penality(genotype, i)
  return 1/(1+total_penality)

def solution_found(population):
  for p in population:
    if get_fitness(p) == 1.0:
      return True
  return False

def highest_fitness(population):
  found, fitness = "", 0
  for p in population:
    actual_fit = get_fitness(p)
    if actual_fit > fitness:
      fitness = actual_fit
      found = p
  return [found, fitness]

def smallest_fitness(population):
  index, fitness = -1, 1
  for i in range(len(population)):
    actual_fit = get_fitness(population[i])
    if actual_fit <= fitness:
      fitness = actual_fit
      index = i
  return [index, fitness]

def get_random_point():
  return random.randint(0, 7) * 3

def crossover_cut_and_crossfill(parent1, parent2):
  cut_point = get_random_point()
  # copy first part of parents to childs
  child1 = parent1[0:cut_point]
  child2 = parent2[0:cut_point]
  c1_elements, c2_elements = {}, {}
  # these dicts will track which elements are in each child
  for i in range(0, cut_point, 3):
    c1_elements[binary_to_decimal(child1[i:i+3])] = True
    c2_elements[binary_to_decimal(child2[i:i+3])] = True
  # fulfill childs with other parent's genotype
  # from cut point to end of parent
  for i in range(cut_point, len(parent1), 3):
    if binary_to_decimal(parent2[i:i+3]) not in c1_elements:
      child1 += parent2[i:i+3]
      c1_elements[binary_to_decimal(parent2[i:i+3])] = True
    if binary_to_decimal(parent1[i:i+3]) not in c2_elements:
      child2 += parent1[i:i+3]
      c2_elements[binary_to_decimal(parent1[i:i+3])] = True
  # fulfill childs with other parent's genotype
  # from start to cut point (remaining values)
  for i in range(0, cut_point, 3):
    if binary_to_decimal(parent2[i:i+3]) not in c1_elements:
      child1 += parent2[i:i+3]
      c1_elements[binary_to_decimal(parent2[i:i+3])] = True
    if binary_to_decimal(parent1[i:i+3]) not in c2_elements:
      child2 += parent1[i:i+3]
      c2_elements[binary_to_decimal(parent1[i:i+3])] = True
  return [child1, child2]

def generate_valid_genotype():
  genotype = ''
  options = list(range(8))
  for _ in range(8):
    value = random.choice(options)
    row_value = str(dec_to_bin(value))
    while len(row_value) < 3:
      row_value = '0' + row_value
    genotype += row_value
    options.remove(value)
  return genotype

def mutation_switch_genes(genotype):
  switch_points = random.sample(range(8),2)
  switch_points = [x*3 for x in switch_points]
  switch_points.sort()

  new_gen = genotype[0:switch_points[0]]
  new_gen += genotype[switch_points[1]:switch_points[1]+3]
  new_gen += genotype[switch_points[0]+3:switch_points[1]]
  new_gen += genotype[switch_points[0]:switch_points[0]+3]
  new_gen += genotype[switch_points[1]+3:]
  return new_gen 

def mutation_invert_bit(genotype):
  invert_point = get_random_point()
  if(genotype[invert_point] == '1'):
    genotype[invert_point] = '0'
  else:
    genotype[invert_point] = '1'
  
  return genotype

def best_two_of_random_five(population):
  chosen_ones = random.sample(range(len(population)),5)
  randon_five = []
  for i in chosen_ones:
    randon_five.append(population[i])
  
  parent1 = highest_fitness(randon_five)
  randon_five.pop(randon_five.index(parent1[0]))
  parent2 = highest_fitness(randon_five)

  return[parent1[0],parent2[0]]
