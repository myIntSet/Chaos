import numpy as np
import matplotlib.pyplot as plt

x0 = 0.1
#r = 3.2
r = 1

#for plot of return map:
start_x = 0
end_x = 1

def logistic_map_step(r, xn):
    return r*xn*(1-xn)

def tent_map_step(r, xn):
    if xn < (end_x-start_x)/2:
        return 2*r*xn
    else:
        return 2*r-2*r*xn

def get_x_y(map_type):
    xplot = np.linspace(start_x,end_x,100)
    if map_type == "Logistic map":
        yplot = logistic_map_step(r, xplot)
    elif map_type == "Tent map":

        yplot = np.zeros(len(xplot))
        for idx, xn in enumerate(xplot):
            yplot[idx] = tent_map_step(r, xn)
    return xplot, yplot

def logistic_map(nbr_steps):
    x = np.zeros(nbr_steps+1)
    x[0] = x0
    for i in range(0,nbr_steps):
        x[i+1] = logistic_map_step(r, x[i])
    #print(x)
    j = np.linspace(0,nbr_steps,nbr_steps+1)
    #print(j)
    return j, x

if __name__ == "__main__":
    #perform 20 iterations of logistic map
    logistic_map(20)
    