
def array_div(array1, array2):
    if len(array1) != len(array2):
        raise RuntimeError("Arrays should be of the same length")
    
    result = []
    
    for i in range(len(array1)):
        result.append(array1[i]/array2[i])

    return result

if __name__ == '__main__':
      array1 = [4, 3, 5, 7]
      array2 = [2.0, 2.0, 2.0, 3.0]
      
      print array_div(array1, array2)
      
