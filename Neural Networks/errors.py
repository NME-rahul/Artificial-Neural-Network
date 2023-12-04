class Errors:
  def data_cardinality(x, y):
    length_x = len(x); length_y = len(y)
    if length_x != length_y:
      print(f'Error: Data Cardinality, recieved {length_x} and {length_y}, \n It must be same.')
      return True
    else:
      return False
