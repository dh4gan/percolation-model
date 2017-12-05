# Written 05/01/17 by dh4gan
# Object runs a 2D percolation model
# for stellar settlement

import numpy as np

class PercolationModel3D(object):    
    '''
    Object that calculates and displays behaviour of 3D cellular automata
    '''
        
    def __init__(self, ni):
        '''
        Constructor reads:
        N = side of grid
        
        produces N x N x N blank grid
        '''
        
        self.N = ni
        self.Ntot = self.N*self.N*self.N
        
        self.sites = np.zeros((self.N,self.N,self.N,3))
        
        self.grid = np.zeros((self.N,self.N,self.N))        
        self.nextgrid = np.zeros((self.N,self.N,self.N))
        self.tested = np.zeros((self.N,self.N,self.N))
        self.complete = False
        
        for i in range(self.N):
            for j in range(self.N):
                for k in range(self.N):
                    self.sites[i,j,k,0] = i
                    self.sites[i,j,k,1] = j
                    self.sites[i,j,k,2] = k
            
        
        
    def getMooreNeighbourhood(self, i,j,k):
        '''
        Returns a set of indices corresponding to the Moore Neighbourhood
        (These are the cells immediately adjacent to (i,j), plus those diagonally adjacent)
        '''
        
        indices = []
        
        for iadd in range(i-1,i+2):
            for jadd in range(j-1, j+2):
                for kadd in range(k-1,k+2):        
                    if(iadd==i and jadd == j and kadd==k): continue
                
                    if(iadd>self.N-1): iadd = iadd - self.N
                    if(jadd>self.N-1): jadd = jadd - self.N
                    if(kadd>self.N-1): kadd = kadd - self.N
                
                    indices.append([iadd,jadd,kadd])
        
        return indices
    
    def getVonNeumannNeighbourhood(self,i,j,k):
        '''
        Returns a set of indices corresponding to the Von Neumann Neighbourhood
        (These are the cells immediately adjacent to (i,j), but not diagonally adjacent)
        '''
        
        indices = []
        
        for iadd in range(i-1,i+2):
            if(iadd==i): continue
            if(iadd>self.N-1): iadd = iadd - self.N        
                
            indices.append([iadd,j,k])
            
        for jadd in range(j-1,j+2):
            if(jadd==j): continue
            if(jadd>self.N-1): jadd = jadd - self.N
            
            indices.append([i,jadd,k])
            
        for kadd in range(k-1,k+2):
            if(kadd==k): continue
            if(kadd>self.N-1): kadd = kadd - self.N
            
            indices.append([i,j,kadd])
            
        return indices    
    
    
    def check_complete(self):
        
        ntested = np.sum(self.tested)
        
        if (ntested == self.N*self.N*self.N):
            self.complete=True
            
        return self.complete
    
    def randomise(self):
        '''
        Places a random selection of zeros and ones into grid
        '''
        
        for i in range(self.N):
            for j in range(self.N):
                for k in range(self.N):
                    self.grid[i,j,k] = np.rint(np.random.random())
                
    def randomise_with_symmetry(self):
        
        for i in range(self.N/2):
            for j in range(self.N/2):
                for k in range(self.N/2):
                    self.grid[i,j,k] = np.rint(np.random.random())
                    self.grid[i+self.N/2,j,k] = self.grid[i,j+self.N/2,k] =self.grid[i+self.N/2,j+self.N/2,k]= self.grid[i,j,k]
                
    def clear(self, icentre, jcentre,kcentre, extent):
        '''
        Clears a space on the grid
        '''
        
        for i in range(icentre-extent, icentre+extent):
            for j in range(jcentre-extent, jcentre+extent):
                for k in range(kcentre-extent,kcentre+extent):
                    if(i>0 and i<self.N and j>0 and j<self.N and k>0 and k<self.N):
                        self.grid[i,j,k] = 0
    
    def updateGrid(self):
        '''
        Takes the changes queued up on self.nextgrid, and applies them to self.grid
        '''
        
        self.grid = np.copy(self.nextgrid)
        self.nextgrid = np.zeros((self.N,self.N,self.N))
        
                 
    
    def ApplyPercolationModelRule(self, P):
        '''
        Constructs the self.nextgrid matrix based on the properties of self.grid
        Applies the Percolation Model Rules:
        
        1. Cells attempt to colonise their Moore Neighbourhood with probability P
        2. Cells do not make the attempt with probability 1-P
        '''
        
        for i in range(self.N):
            for j in range(self.N):
                for k in range(self.N):
                
                    if(self.tested[i,j,k]==1):
                        self.nextgrid[i,j,k]=self.grid[i,j,k]
                        continue
                
                    # If cell contains a coloniser, then decide whether to colonise
                    if(self.grid[i,j,k]==1 and self.tested[i,j,k]==0):
                   
                        randtest = np.random.rand()
                    
                        # If colonisation occurs
                        if(randtest<P):
                            self.nextgrid[i,j,k]=1
                            indices = self.getMooreNeighbourhood(i,j,k)
                        
                            for element in indices:
                                if(self.tested[element[0],element[1],element[2]]==1):
                                    continue
                                if(self.grid[element[0],element[1],element[2]]==0):
                                    self.nextgrid[element[0],element[1],element[2]]=1
                            
                        else:
                            self.nextgrid[i,j,k]=-1
                                                                                
                        self.tested[i,j] =1
                        
    def getColours(self):
        
        colour = []
        for i in range(self.N):
            for j in range(self.N):
                for k in range(self.N):
                    
                    if (self.grid[i,j,k]==0):
                        colour.append([1,1,1])
                    elif(self.grid[i,j,k]==-1):
                        colour.append([1,1,1])
                    elif(self.grid[i,j,k]==1):
                        colour.append([0,0,0])
                        

        return colour
        
