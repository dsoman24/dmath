# Vertical free fall with drag

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from logarithm import ln
from exponential import exp

def freefall_displacement(t, density, drag_coef, cross_sectional_area, g, mass):
    """Returns displacement after t seconds"""
    k = 0.5*density*drag_coef*cross_sectional_area
    phi = (k/(g*mass))**0.5
    return (1/(g*phi**2))*ln((exp(-2*g*phi*t)+1)/exp(-2*g*phi*t))-t/phi-ln(2)/(g*phi**2)

def freefall_velocity(t, density, drag_coef, cross_sectional_area, g, mass):
    """Returns velocity after t seconds"""
    k = 0.5*density*drag_coef*cross_sectional_area
    phi = (k/(g*mass))**0.5
    return (1/phi)*((1-exp(-2*g*phi*t))/(1+exp(-2*g*phi*t)))
