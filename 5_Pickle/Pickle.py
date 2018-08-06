# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 22:10:07 2018
@author: SilverDoe
"""

# Serialize
import pickle
characters = {1:"Taki",2:"Mitsuha",3:"Yotsuha",4:"Miki",5:"Tsukasa"}
pic = open("E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\characters.pickle","wb")
pickle.dump(characters, pic)
pic.close()

# Deserialize
picread = open("E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\characters.pickle","rb")
characterz = pickle.load(picread)
print(characterz)


'''

Pickle.PicklingError: This exception is raised when you are trying to pickle an object that doesn’t support pickling.

Pickle.UnpicklingError: This exception is raised when a file contains corrupted data.

EOFError: This exception is raised when the end of file is detected.

'''


# cpickle
import _pickle as pickle
import pprint

data1 = [ {1:"Taki",2:"Mitsuha",3:"Yotsuha",4:"Miki",5:"Tsukasa"} ]
cpic = open("E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\charactersC.pickle","wb")
pprint.pprint(data1)

pickle.dump(data1,cpic)
cpic.close()

cpicread = open("E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\charactersC.pickle","rb")
data2 = pickle.load(cpicread)
pprint.pprint(data2)
cpicread.close()

print('SAME?:', (data1 is data2))
print('EQUAL?:', (data1 == data2))












