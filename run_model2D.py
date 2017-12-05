from PercolationModel2D import PercolationModel2D
import PercolationModelPatterns as game
import matplotlib.pyplot as plt
from time import sleep
from numpy import log10

N=200
nsteps = 200
nzeros = int(log10(nsteps))+1
icentre = N/2
jcentre = N/2

# Create the percolation model, and seed four colony sites at the centre

cell= PercolationModel2D(N)

cell.grid[:,jcentre-4:jcentre+4]=1
cell.grid[icentre-4:icentre+4,:]=1
# game.add_beehive(cell,icentre,jcentre)
# 
# game.add_beehive(cell,icentre/2,jcentre/2)
# game.add_beehive(cell,icentre/2,jcentre)
# game.add_beehive(cell,icentre,jcentre/2)

P=0.4

# Set up interactive plotting

plt.ion()

fig1 = plt.figure()
ax = fig1.add_subplot(111)

istep= 0
while istep < nsteps:    

    ax.clear()
    ax.axis("off")
    print istep
    # Draw the automaton
    
    hist = ax.pcolor(cell.grid,edgecolors='black',cmap='terrain',vmin=-1,vmax=1)
    #ax.text(0.9, 1.05,str(istep)+" Steps", horizontalalignment='center',verticalalignment='center',transform=ax.transAxes,fontsize=18)
    #ax.text(0.1,1.05, "P="+str(P),horizontalalignment='center',verticalalignment='center',transform=ax.transAxes,fontsize=18)
    #hist = ax.pcolor(cell.nextgrid,edgecolors='black', cmap='binary')

    plt.draw()
    plt.savefig('step_'+str(istep).zfill(nzeros)+".png", dpi=300)
    
    # Apply the Game of Life Rule, and update the grid
    cell.ApplyPercolationModelRule(P)
    cell.updateGrid()
    
    # Clear axes for next drawing
    
    sleep(0.01)
   
    if cell.check_complete():
        print "Run complete"
        break
    
    istep+=1

plt.ioff()

hist = ax.pcolor(cell.grid,edgecolors='black',cmap='binary',vmin=-1,vmax=1)

plt.show()
