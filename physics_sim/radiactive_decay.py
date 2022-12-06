# Radiactive decay simulator

import random
import matplotlib.pyplot as plt
import pandas as pd

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from logarithm import ln
from checkdp import cdp

class Radioactive():
    
    def __init__(self, init_mass, half_life):
        self.N0 = init_mass
        self.N = self.N0
        self.t_half = half_life

    def decay(self, dt, reach, T, tau):
        decayconst = ln(tau)/self.t_half # probability of decay per unit time (lambda, decay constant)
        
        t = 0 # counter, elapsed time
        self.activity = []
        self.time = []

        while t < T:
            
            if self.N <= reach:
                print('t = '+str(round(t+dt, cdp(dt)))+', N = '+str(reach))
                self.activity.append(reach)
                self.time.append(t+dt)
                
                break

            self.activity.append(self.N)
            self.time.append(t)
            print('t = '+str(round(t, cdp(dt)))+', N = '+str(self.N))

            for i in range(0, self.N+1):
                i
                prob = random.random()/dt
                if prob < decayconst:
                    self.N -= 1
            t += dt 
        print('\nIt took t = '+str(round(r.time[-1], cdp(dt)))+' to decay '+str(self.N0-self.activity[-1])+'\n')

##### INPUTS ####

N0 = 100 # initial activity
dt = 0.1 # time increments
constant = 2 # This input is the time it takes for 1/tau of the activity to decay. tau is defined below. For radiactive decay, the constant is the half-life so tau=2.
T = 10000 # total time to run simulation unless the N = reach is reached
reach = 0 # stop simulation if N reaches this number
tau = 2 # when tau = 2 the constant is the half life
trials = 1

##################

time_activity = pd.DataFrame()

for i in range(trials):

    r = Radioactive(N0, constant)
    r.decay(dt, reach, T, tau)

    trial_data = pd.DataFrame(r.activity, r.time)
    time_activity = pd.concat([time_activity, trial_data], axis=1)

#time_activity.to_csv('decaydata.csv')
plt.plot(r.time, r.activity)
plt.show()