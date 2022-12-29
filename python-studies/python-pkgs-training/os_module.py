import os
import stat

#Get environment variables
NEW_ENV_VARIABLE = os.getenv('VARIABLE-NAME')

#Get the current working directory
current_directory = os.getcwd()
print('Current directory:', current_directory)

#Change directory 
os.chdir('../')
print('Current directory after:', current_directory)

#Paths
new_directory = 'os_test'
parent_dir = r'C:\Users\Vegh\Documents\Estudo\python-packages-study\packages'

#Join the directory path with the new directory to be created with mkdir
path = os.path.join(parent_dir, new_directory)

#Create new directory - use os.mkdirs() if any parent directory do not exists in file path
os.mkdir(path)
print(f'Directory {new_directory} created')

#List files in directory
file_list = os.listdir(parent_dir)
print('Current files in the path {}: {}'.format(parent_dir, file_list))

#Remove directory/files
os.remove(path)

#Change the mode of the path(Useful on permission errors and other cases)
os.chmod(path, mode=stat.S_IRWXU)


