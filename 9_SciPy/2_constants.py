# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 14:48:43 2018

@author: SilverDoe
"""

'''
SciPy constants package provides a wide range of constants, which are used in 
the general scientific area.

https://docs.scipy.org/doc/scipy/reference/constants.html


#============= Physical Constant ==============================================
	
c : Speed of light in vacuum
	
speed_of_light : Speed of light in vacuum
	
h : Planck constant

Planck : Planck constant h
	
G : Newton’s gravitational constant
	
e : Elementary charge
	
R : Molar gas constant
	
Avogadro : Avogadro constant

k : Boltzmann constant

electron_mass(OR) m_e : Electronic mass
	
proton_mass (OR) m_p : Proton mass
	
neutron_mass(OR)m_n : Neutron mass

#============ Other Constants =================================================

1	gram	        0.001 kg
2	atomic mass	  Atomic mass constant
3	degree	        Degree in radians
4	minute	        One minute in seconds
5	day	One        day in seconds
6	inch	        One inch in meters
7	micron      	One micron in meters
8	light_year  	One light-year in meters
9	atm	          Standard atmosphere in pascals
10	acre	        One acre in square meters
11	liter	       One liter in cubic meters
12	gallon	       One gallon in cubic meters
13	kmh	          Kilometers per hour in meters per seconds
14	degree_Fahrenheit	One Fahrenheit in kelvins
15	eV	          One electron volt in joules
16	hp	          One horsepower in watts
17	dyn         	One dyne in newtons
18	lambda2nu	   Convert wavelength to optical frequency

'''

import scipy.constants as sc
from math import pi

print("sciPy - pi = %.16f"%sc.pi)
print("math - pi = %.16f"%pi)
print(sc.golden)


#=============== find keys ====================================================

import scipy.constants
res = scipy.constants.physical_constants["alpha particle mass"]
print(res)

res1 = scipy.constants.find("alpha particle mass")
res1

res2 = scipy.constants.physical_constants["alpha particle mass energy equivalent in MeV"]
res2










