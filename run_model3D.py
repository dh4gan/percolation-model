from PercolationModel3D import PercolationModel3D
import PercolationModelPatterns as game
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from time import sleep
from numpy import log10,sum,abs,array
from itertools import combinations,product
import sys

N=10
nsteps = 1000
nzeros = int(log10(nsteps))+1
icentre = 5
jcentre = 5

# Create the percolation model, and seed four colony sites at the centre

cell= PercolationModel3D(N)

cell.randomise()

#game.add_block(cell,icentre,jcentre)

P=0.6

# Set up interactive plotting

plt.ion()

fig1 = plt.figure()
ax = fig1.add_subplot(111, projection='3d')

istep= 0
while istep < nsteps:    

    ax.clear()
    ax.axis("off")
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    print istep
    # Draw the grid
    

    ax.scatter(cell.sites[:,:,:,0],cell.sites[:,:,:,1], cell.sites[:,:,:,2], color =cell.getColours())
    
    #hist = ax.pcolor(cell.grid[:,:,0],edgecolors='black',cmap='binary',vmin=-1,vmax=1)
    #ax.text(0.9, 1.05,str(istep)+" Steps", horizontalalignment='center',verticalalignment='center',transform=ax.transAxes,fontsize=18)
    #ax.text(0.1,1.05, "P="+str(P),horizontalalignment='center',verticalalignment='center',transform=ax.transAxes,fontsize=18)
    #hist = ax.pcolor(cell.nextgrid,edgecolors='black', cmap='binary')

    plt.draw()
    plt.savefig('step_'+str(istep).zfill(nzeros)+".png")
    
    # Apply the Game of Life Rule, and update the grid
    cell.ApplyPercolationModelRule(P)
    cell.updateGrid()
    
    # Clear axes for next drawing
    
    sleep(0.1)
   
    if cell.check_complete():
        print "Run complete"
        break
    
    istep+=1

plt.ioff()

#hist = ax.pcolor(cell.grid[:,:,0],edgecolors='black',cmap='binary',vmin=-1,vmax=1)

plt.show()
