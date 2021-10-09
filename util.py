def diagonal_cross(q1_row, q1_col, q2_row, q2_col):
  row_vec = q1_row - q2_row
  col_vec = q1_col - q2_col
  return abs(row_vec) == abs(col_vec)

def get_fitness(genotype, queen_index):
  penality = 0
  queen_row = genotype[queen_index]
  queen_column = queen_index
  for neib_queen_column, neib_queen_row in enumerate(genotype):
    if queen_column == neib_queen_column:
      continue
    else:
      if queen_row == neib_queen_row:
        penality += 1
      elif diagonal_cross(queen_row, queen_column, neib_queen_row, neib_queen_column):
        penality += 1
  return 1/(1+penality)

