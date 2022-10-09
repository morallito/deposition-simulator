#  Simulations of computational mathematical modeling principles

This repo is dedicated to hosting all python files used during the discipline of computational mathematical modeling principles, 
taught at CEFET MG, 2022/2. 


## Repo structure
Each folder in the root dir is a python module, and each odule is used for one type of simulation. The plotter.py is the module used to plot the simulation results. The main file, in the root directory, is used as a CLI, to receive the simulation type and parameters, and run the simulator and the plotter. Each simulator and the plotter has it's own readme file, where the usage of it is documented. 

Have fun! 

```
.
├── random_relaxed_deposition
│   └── random_relaxed_simulator.py
├── random_deposition
│   └── random_simulator.py
├── balistic_deposition
│   └── balistic_simulator.py
├── plotter
│   └── plotter.py
├── requirements.txt
└── main.py
```

## Plotter

The plotter module plots a matrix M(m,n) where the element K(i,j) is an integer, 0-100 where 0 is a white square, and 100 a black square. 

```
m    | 
.    | 
.    |
.    |
m=2  |
m=1  |
m=0  |
       ─── ─── ─── ─── ─── ─── ───
       n=0 n=1 n=2  .   .   .   n
```

### Plotter class

### Methods 

## Balistic deposition simulator
## Random deposition simulator
## Random relaxed deposition


