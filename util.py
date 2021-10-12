def binary_to_decimal(val):
  return int(val, 2)

def diagonal_cross(q1_row, q1_col, q2_row, q2_col):
  row_vec = q1_row - q2_row
  col_vec = q1_col - q2_col
  return abs(row_vec) == abs(col_vec)

def get_fitness(genotype):
  total_penality = 0
  for i in range(0, len(genotype), 3):
    total_penality += get_penality(genotype, i)
  return 1/(1+total_penality)

def get_penality(genotype, queen_index):
  penality = 0
  queen_row = binary_to_decimal(genotype[queen_index:queen_index+3])
  queen_column = int(queen_index/3)
  for i in range(queen_index, len(genotype), 3):
    neib_queen_column = int(i/3)
    neib_queen_row = binary_to_decimal(genotype[i:i+3])
    if queen_column == neib_queen_column:
      # it self
      continue
    else:
      if queen_row == neib_queen_row:
        penality += 1
      elif diagonal_cross(queen_row, queen_column, neib_queen_row, neib_queen_column):
        penality += 1
  return penality

