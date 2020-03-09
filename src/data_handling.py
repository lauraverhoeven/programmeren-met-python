# this is a module containing the data handling functions for our data set
import pandas as pd

# function to load the data in a new file
def load_data(file):
  # read the file
  data_file = pd.read_csv(file, sep=";")
  
  # trim whitespaces
  data_file_obj = data_file.select_dtypes(['object'])
  data_file[data_file_obj.columns] = data_file_obj.apply(lambda x: x.str.strip()) 
  
  # return the data
  return data_file
  
  



