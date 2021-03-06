import numpy as np
import pylab as pl
import time
import matplotlib

       
class BrainCell(object):
    
    
    def __init__(self):
        self.weights = np.array(list())
        self.children = list()
        self.vals = list()
        self.parents = list()
        
    def connect(self, braincell, weight=None):
        if braincell is self: raise Exception('A cell cannot be connected to itself')
        self.children.append(braincell)
        if weight is None:
            weight = np.random.uniform(-1, 1)
        weights = list(self.weights)
        weights.append(weight)
        self.set_weights(weights)
            
    def put(self, val):
        self.vals.append(float(val))
    
    def get(self):
        return np.mean(self.vals)
    
    def compute(self):
        out = self.get()
        if len(self.children) == 0: return
        for i in range(len(self.children)):
            self.children[i].put(out * self.weights[i])
        self.reset()
    
    def set_weights(self, weights):
        weights = np.array(weights)
        if weights.size != len(self.children): 
            raise Exception('weights must have len {}'.format(len(self.children)))
            
        weights = np.clip(weights, -1, 1)
        if weights.size == self.weights.size:
            self.gradient = weights - self.weights
            
        self.weights = weights
        
    def get_gradient(self):
        if not hasattr(self, 'gradient'): 
            return np.zeros(len(self.weights))
        else:
            return np.copy(self.gradient)
        
    def reset(self):
        self.vals = list()
        
    def randomize(self, scale):
        weights = np.copy(self.weights)
        gradient = np.random.standard_normal(size=weights.size) * scale
        self.apply_gradient(gradient)
    
    def apply_gradient(self, gradient=None):
        if gradient is None:
            gradient = self.get_gradient()
            
        self.set_weights(np.array(self.weights) + gradient)
        
    def invert_gradient(self):
        self.apply_gradient(-self.get_gradient())
            
class CellLayer(object):
    
    def __init__(self, size):
        self.cells = list()
        for i in range(size):
            self.cells.append(BrainCell())
            
    def connect(self, layer):
        if layer is self: raise Exception('A layer cannot be connected to itself')
        for icell in self.cells:
            for ichild in layer.cells:
                icell.connect(ichild)
            
    def get(self):
        result = list()
        for icell in self.cells:
            result.append(icell.get())
        return result
            
    def set_weights(self, weights):
        for icell in self.cells:
            icell.set_weights(weights)
            
    def put(self, vals):
        if len(vals) != len(self.cells): 
            raise Exception('vals len must be equal to {}'.format(len(self.cells)))
        for i in range(len(self.cells)):
            self.cells[i].put(vals[i])
            
    def compute(self):
        for icell in self.cells:
            icell.compute()
    
    def reset(self):
        for icell in self.cells:
            icell.reset()
            
    def randomize(self, scale):
        for icell in self.cells:
            icell.randomize(scale)
            
    def reapply_gradient(self):
        for icell in self.cells:
            icell.apply_gradient()
    
    def invert_gradient(self):
        for icell in self.cells:
            icell.invert_gradient()
            
class Brain(object):
    
    def __init__(self, sizes=(2,2)):
        
        self.layers = list()
        for isize in sizes:
            self.add_fully_connected_layer(isize)
            
    def add_fully_connected_layer(self, size):
        self.layers.append(CellLayer(size))
        if len(self.layers) > 1:
            self.layers[-2].connect(self.layers[-1]) # connect new layer to previous layer
            
    
    def show(self):
        fig = pl.figure(figsize=(10,10))
        coords = list()
        for ii in range(len(self.layers)):
            for ij in range(len(self.layers[ii].cells)):
                self.layers[ii].cells[ij].coords = (ii, ij)
        
        for ilayer in self.layers:
            for icell in ilayer.cells:
                pl.scatter(icell.coords[0], icell.coords[1], c='black')
                
                for i in range(len(icell.children)):
                    pl.arrow(icell.coords[0], icell.coords[1], 
                             icell.children[i].coords[0] - icell.coords[0],  
                             icell.children[i].coords[1] - icell.coords[1], 
                             ec=matplotlib.cm.RdYlBu_r((icell.weights[i] + 1.)/2.))
                
                    
                pl.text(icell.coords[0] - 0.2, icell.coords[1] + 0.2, ' '.join(['{:.2f}'.format(w) for w in icell.weights]), c='red')
                #pl.text(icell.coords[0] - 0.05, icell.coords[1] + 0.2, '{:.2f}'.format(icell.get()), c='green')
        fig.colorbar(matplotlib.cm.ScalarMappable(norm=matplotlib.colors.Normalize(vmin=-1, vmax=1), cmap='RdYlBu_r'))
                
            
    def think(self, vals):
        
        #stime = time.time()
        if len(vals) != len(self.layers[0].cells): 
            raise Exception('bad number of vals. shoud be {}'.format(len(self.layers[0].cells)))
            
        # 
        for ii in range(len(vals)):
            self.layers[0].put(vals)
        
        for ilayer in self.layers:
            ilayer.compute()
                
        result = self.layers[-1].get()
        self.layers[-1].reset()
        
        #print(time.time() - stime , 's')
        return result
    
    def clone(self):
        new_brain = Brain(sizes=[len(ilayer.cells) for ilayer in self.layers])
        for il in range(len(new_brain.layers)):
            for ic in range(len(new_brain.layers[il].cells)):
                new_brain.layers[il].cells[ic].set_weights(self.layers[il].cells[ic].weights)
        return new_brain   
    
    def randomize(self, scale):
        for ilayer in self.layers:
            ilayer.randomize(scale)
            
    def reapply_gradient(self):
        for ilayer in self.layers:
            ilayer.reapply_gradient()
    
    def invert_gradient(self):
        for ilayer in self.layers:
            ilayer.invert_gradient()
            
class Thing(object):
    def __init__(self, x, y, universe, energy):
        self.x = x
        self.y = y
        self.universe = universe
        self.energy = energy
        self.signature = 0
        
    def distance_from(self, x, y):
        return np.sqrt((self.x - x)**2 + (self.y - y)**2)
    
    def eaten(self):
        give = float(self.energy)
        self.energy = 0
        return give
    
class Nothing(Thing):
    def __init__(self, x, y):
        Thing.__init__(self, x, y, None, 0)
    
class Food(Thing):
    MAX_ENERGY = 100000
    MAX_GIVE = 5
    def __init__(self, x, y, universe, energy=None):
        if energy is None:
            energy = int(np.random.uniform(np.sqrt(self.MAX_ENERGY), self.MAX_ENERGY))
        Thing.__init__(self, x, y, universe, energy)
        self.signature = -1
        
    def eaten(self):
        give = min(self.energy, np.random.uniform(1, self.MAX_GIVE))
        self.energy -= give
        return give
    
class ADN(object):
    
    def __init__(self, size):
        self.size = int(size)
        self.adn = np.random.uniform(-1, 1, self.size)
        
    def randomize(self, scale):
        self.adn += np.random.standard_normal(self.size)
        self.adn = np.clip(self.adn, -1, 1)
        
    def clone(self):
        new_adn = ADN(self.size)
        new_adn.adn = np.copy(self.adn)
    
class Cell(Thing):
    
    RANDOMIZE_SCALE = 0.03
    ADN_SIZE = 2
    TARGET_FEATURES = 3
    TARGET_NB = 10
    INPUT_BRAIN_SIZE = TARGET_FEATURES
    OUTPUT_BRAIN_SIZE = 1
    TOTAL_ENERGY_POWER = 1.1
    REPRODUCTION_TIME = 10
    
    def __init__(self, x, y, universe, brain=None, energy=1, adn=None):
        Thing.__init__(self, x, y, universe, energy)
        
        if adn is None:
            self.adn = ADN(self.ADN_SIZE)
        
        if brain is None:
            brain = Brain(sizes=(self.INPUT_BRAIN_SIZE, self.OUTPUT_BRAIN_SIZE))
            
        self.brain = brain
        self.signature = 1
        self.all_choices = list()
        self.all_targets = list()
        self.all_babies = list()
        
    def act(self):
        # herbivore = /, -1
        # carnivore = /, 1
        # animal = -1, /
        # plante = 1, /
        
        if self.energy <= 0: return
        targets = self.look()
        targets.append(Nothing(self.x, self.y)) # stay in place
        targets.append(Nothing(self.x + np.random.uniform(-0.1, 0.1), self.y + np.random.uniform(-0.1, 0.1))) # flee
        
        choices = list()
        max_energy = np.max([itarget.energy for itarget in targets])
        for itarget in targets:
            input_brain = (self.distance_from(self.x, self.y),
                           itarget.energy / max_energy,
                           float(itarget.signature))
            choices.append(self.brain.think(input_brain))
        choice = targets[np.nanargmax(choices)]
        self.all_choices.append(np.nanargmax(choices))
        self.all_targets.append(float(choice.signature))
        
        self.x = float(choice.x)
        self.y = float(choice.y)
        self.energy -= self.distance_from(choice.x, choice.y) * (self.adn.adn[0] + 1)
        
        if choice.energy > 0: # eat the choosen cell
            self.energy += choice.eaten() * choice.signature * (self.adn.adn[1])
                
        self.reproduce()
                
        self.energy -= 1. + 0.5 * (1 - self.adn.adn[0])
        
    def eaten(self):
        return Thing.eaten(self) ** self.TOTAL_ENERGY_POWER
        
    def reproduce(self):

        if np.random.randint(0, self.REPRODUCTION_TIME) > 0:
            return
        
        baby_energy = max(1, np.sqrt(self.energy) * 0.5)
        reproduction_energy = baby_energy ** self.TOTAL_ENERGY_POWER
        if self.energy < reproduction_energy + 1:
            return
                    
        new_cell = self.clone()
        new_cell.x += (np.random.uniform() - 0.5) * 0.01
        new_cell.y += (np.random.uniform() - 0.5) * 0.01
        new_cell.energy = baby_energy
        self.energy -= reproduction_energy
        new_cell.brain.randomize(self.RANDOMIZE_SCALE)
        new_cell.adn.randomize(self.RANDOMIZE_SCALE)
        self.universe.add_cell(new_cell)
        self.all_babies.append(baby_energy)
        
        
    def look(self):
        targets = self.universe.look_around(self, self.TARGET_NB)
        return targets
    
    def clone(self):
        return Cell(self.x, self.y, self.universe, brain=self.brain.clone(), energy=self.energy, adn=self.adn.clone())
    

        
class Universe(object):
    
    def __init__(self, ncells, nfoods, regenerate_ratios=(0.05, 0.02), size=1):
        self.size = float(size)
        self.time = 0
        self.cells = list()
        self.foods = list()
        self.babies_nb = 0
        self.generate(ncells, nfoods)
        self.regenerate_ratios = regenerate_ratios
        
    def generate(self, ncells, nfoods, energy=1):
        # create cells at random positions
        for i in range(ncells):
            x = np.random.uniform(high=self.size)
            y = np.random.uniform(high=self.size)
            self.cells.append(Cell(x, y, self))
        for i in range(nfoods):
            x = np.random.uniform(high=self.size)
            y = np.random.uniform(high=self.size)
            self.foods.append(Food(x, y, self))
            
    def add_cell(self, cell):
        if not isinstance(cell, Cell): 
            raise TypeError('cell must be a Cell')
        for icell in self.cells:
            if icell is cell:
                raise Exception('new cell must not already be in the universe')
        self.cells.append(cell)
        self.babies_nb += 1
        
    def update(self):
        cells = list()
        for icell in self.cells:
            if icell.energy > 0:
                cells.append(icell)
        self.cells = cells
        foods = list()
        for ifood in self.foods:
            if ifood.energy > 0:
                foods.append(ifood)
        self.foods = foods
    
    def look_around(self, cell, max_number):
        things = list()
        everything = self.cells + self.foods
        distances = list()
        for ithing in everything:
            distances.append(ithing.distance_from(cell.x, cell.y))
        order = np.argsort(distances)
        for i in order:
            ithing = everything[i]
            if ithing is cell: continue
            if ithing.energy <= 0: continue
                
            things.append(ithing)
            if len(things) == max_number:
                break
            
        return things
    
    def step(self):
        order = np.arange(len(self.cells))
        np.random.shuffle(order)
        for i in order:
            self.cells[i].act()
        median_energy = self.get_mean_energy()
        ncells = len(self.cells) * self.regenerate_ratios[0]
        if ncells < 1:
            ncells = int(np.random.uniform() < ncells)
        nfoods = len(self.foods) * self.regenerate_ratios[1]
        if nfoods < 1:
            nfoods = int(np.random.uniform() < nfoods)
        self.generate(int(ncells), int(nfoods),
                      energy=self.get_mean_energy())
        self.update()
        
    
    def show(self):
        pl.figure()
        x = list()
        y = list()
        c = list()
        
        for ifood in self.foods:
            x.append(float(ifood.x))
            y.append(float(ifood.y))
            c.append(float(ifood.energy))
        pl.scatter(x, y, c=c, vmin=0, vmax=np.max(c), marker='+', cmap='Reds')
        pl.colorbar()
        print(np.max(c))
        
        x = list()
        y = list()
        c = list()
        for icell in self.cells:
            x.append(float(icell.x))
            y.append(float(icell.y))
            c.append(float(icell.energy))
        pl.scatter(x, y, c=c, vmin=0, vmax=np.max(c), alpha=0.3)
        pl.colorbar()
        print(np.max(c))
        
    def get_best_cell(self):
        min_energy = 0
        for icell in self.cells:
            if icell.energy > min_energy:
                best = icell
                min_energy = icell.energy
        return best
    
    def get_mean_energy(self):
        energies = list()
        for icell in self.cells:
            energies.append(icell.energy)
        return np.mean(energies)

    def get_regime(self):
        carnivorous = list()
        herbivorous = list()
        for icell in self.cells:
            if icell.adn.adn[1] > 0:
                carnivorous.append(icell)
            else:
                herbivorous.append(icell)
        return len(carnivorous), len(herbivorous)
