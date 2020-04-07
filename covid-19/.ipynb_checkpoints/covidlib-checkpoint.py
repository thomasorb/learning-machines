import numpy as np
import pylab as pl
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

style = {'description_width': 'initial'}
@interact(contacts_per_day=widgets.FloatSlider(min=0, max=6, step=0.3, value=3, style=style), 
          infection_probability=widgets.FloatSlider(min=0.01, max=0.3, step=0.01, value=0.1, style=style), 
          recovery_time=widgets.IntSlider(min=1, max=30, step=1, value=10, style=style), 
          mortality=(0, 1, 0.01))
def SIR(contacts_per_day, infection_probability, recovery_time, mortality):
    N = 10000
    S0 = float(N)
    R0 = 0
    I0 =1
    
    I = list()
    S = list()
    R = list()
    
    gamma = 1/recovery_time # rate of recovery or mortality per day
    beta = contacts_per_day * infection_probability
    
    I.append(I0)
    S.append(S0)
    R.append(R0)
    
    dT = 1 # day
    
    stop = False
    iday = 0
    while not stop:
        i = I[-1]
        s = S[-1]
        r = R[-1]
        
        dS = - beta * i * s / (s + i + r) * dT
        dR = (gamma * i) * dT
        dI = -dS -dR
      
        S.append(s + dS)
        R.append(r + dR)
        I.append(i + dI)
        
        iday += 1
        if iday > 10000: stop = True # hardbreak
        if i <= 1 and r > N/2: stop = True
    
    number_infected = N - S[-1]
    print('Percentage of people infected: {:.1f} %'.format((number_infected)/N * 100))
    print('Number of deaths: {:d}'.format(int(number_infected * mortality)))
    pl.figure(figsize=(15,5))
    pl.plot(S, label='Susceptible')
    pl.plot(I, label='Infectious')
    pl.plot(R, label='Recovered')
    pl.xlabel('Days')
    pl.ylabel('Number')
    pl.legend()
    pl.grid()