#######################################
## Landmark suggestion demo
## by Brian Cohen
## (twitter: @N0TtheMessiah)
## 
## This script generates a random path
## and landmarks, and produces a
## ranking based off a convenience
## metric motivated by characteristics
## deemed to be of consideration to
## walking directions.
## 
## Notable ways this script may differ
## from real use is that paths are not
## uniform, so random paths may appear
## quite absurd. Also, landmarks as
## well as walking directions tend to
## be pseudo-discretized along street
## grids. These real-world
## considerations are accounted for in
## our metrics, but not our model.
## 
## This script uses Numpy+SciPy
## libraries and can be easily adapted
## for GPS latitude and longitude.
## Important considerations for such
## are latitude/longitude asymmetry.
#######################################

import numpy as np
import scipy as sp
import pylab as pl

path = np.random.rand(4,2) # Uniformly randomly selected path of 4 nodes
landmarks = np.random.rand(10,2) # Uniformly randomly places landmarks

def d2(a,b): return np.dot(a-b,a-b)
    
def scores(path,landmarks):
    t=[] #matrix of path vs walking distances
    ds = [] #distances along the path itself
    for i in range(path.shape[0]-1):
        a,b = path[i],path[i+1] #subpath points start & finish
	dist = np.sqrt(d2(a,b)) #subpath length
	ds.append(dist)
        t.append([(np.sqrt(d2(a,l))+np.sqrt(d2(b,l)))/np.sqrt(dist) for l in landmarks])
	#above: normalized deviant distances of landpoints
    return np.sum(np.array(map(lambda x: 1.0/x,np.array(t))),axis=0) #adds up scores along total path

D= scores(path,landmarks)

#### Pylab plotting ####

# Size of landmarks is arbitrary, all it need to do is preserve monotonicity
pl.scatter(landmarks[:,0],landmarks[:,1],s=[10*d*d*d*d for d in D],marker='o')
pl.plot(path[:,0],path[:,1])
pl.show()
