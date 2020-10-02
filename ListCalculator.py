import numpy as np

#output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
def calculate(list):
  #test list for 9 item size
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  
  #convert list to 3x3 matrix
  list_matrix = np.array(list).reshape(3,3)
  #create dictionary
  list_dict = {'mean':[], 'variance':[], 'max':[], 'min':[], 'sum':[]}
  
  #create and append mean of list_matrix along both axes and for the flattened matrix.
  #print(np.mean(list_matrix, axis=0))
  #print(type(list_dict['mean'])
  
  list_dict['mean'].append(np.mean(list_matrix, axis=0))
  list_dict['mean'].append(np.mean(list_matrix, axis=1))
  list_dict['mean'].append(np.mean(list_matrix.flatten()))
  
  #create and append varience of list_matrix along both axes and for the flattened matrix.
  list_dict['variance'].append(np.var(list_matrix, axis=0))
  list_dict['variance'].append(np.var(list_matrix, axis=1))
  list_dict['variance'].append(np.var(list_matrix.flatten()))
  
  #create and append max of list_matrix along both axes and for the flattened matrix.
  list_dict['max'].append(np.max(list_matrix, axis=0))
  list_dict['max'].append(np.max(list_matrix, axis=1))
  list_dict['max'].append(np.max(list_matrix.flatten()))
  
  #create and append min of list_matrix along both axes and for the flattened matrix.
  list_dict['min'].append(np.min(list_matrix, axis=0))
  list_dict['min'].append(np.min(list_matrix, axis=1))
  list_dict['min'].append(np.min(list_matrix.flatten()))
  
  #create and append sum of list_matrix along both axes and for the flattened matrix.
  list_dict['sum'].append(np.sum(list_matrix, axis=0))
  list_dict['sum'].append(np.sum(list_matrix, axis=1))
  list_dict['sum'].append(np.sum(list_matrix.flatten()))
  
  return(list_dict)

example = calculate([0,1,2,3,4,5,6,7,8])
print(example)