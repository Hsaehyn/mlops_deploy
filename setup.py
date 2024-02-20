# setup.py is responsible for creating the machine learning application as a package
# and even deploy it at PyPi so others can use it as a library
from typing import List
from setuptools import find_packages, setup

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)-> List[str]:
    '''
    this function will return a list of all libraries in the requiremmets.txt
    '''
    requirements = []
    
    with open(file_path) as file:
        libraries = file.readlines()
        # pu all the libararies into a list, seperate them by \n
        requirements = [library.replace("\n", "")for library in libraries]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements
        
        
setup(
    name = 'mlproject', 
    version = '0.0.1',
    author = "J-shyne",
    author_email = 'jshyneyap@gmail.com',
    packages = find_packages(),
    # install_requires = ['pandas', 'numpy', 'seaborn'],   
    install_requires = get_requirements('requirements.txt')
)

# for the packages, we create the 'src' folder and the find_packag() will directly 
# go look for how many packages are there in the folder.
# and then it will try to build the application, 
# which menas people can just import them anywhere they want