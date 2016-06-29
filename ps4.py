# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#       

def simulationWithDrugVariableSteps(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials, nStepBfDrug):
    """
    Runs simulations and plots graphs for Problem Set 3, problem 5.
    Return the results of final virus counts for the specified # of trials

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """

    # TODO
    #numVirusAllTrails = [0]*300
    #numGuttagonolResist = [0]*300
    finalNVirusAllTrials = [0]*numTrials
    
    
    for j in range(numTrials):
        
        virusList = []
        for i in range(numViruses):
            B = ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)
            virusList.append(B)
    
        Y = TreatedPatient(virusList, maxPop)
    
        for i in range(nStepBfDrug):
            Y.update()
            #numVirusAllTrails[i] += Y.getTotalPop()
            #numGuttagonolResist[i] += Y.getResistPop(['guttagonol'])
            #print "before: "+str(Y.getResistPop(['guttagonol']))
            
        Y.addPrescription('guttagonol')
        
        for i in range(150):
            Y.update()
            #numVirusAllTrails[i+nStepBfDrug] += Y.getTotalPop()
            #numGuttagonolResist[i+nStepBfDrug] += Y.getResistPop(['guttagonol'])
            #print "after: "+str(Y.getResistPop(['guttagonol']))
        
        finalNVirusAllTrials[j] = Y.getTotalPop()

    #for j in range(len(numVirusAllTrails)):
    #    numVirusAllTrails[j] = numVirusAllTrails[j]*1.0 / numTrials
    #    numGuttagonolResist[j] = numGuttagonolResist[j]*1.0 / numTrials

    
    nvirus = pylab.hist(finalNVirusAllTrials,bins=10)
    pylab.title(str(nStepBfDrug)+' steps before drug')
    pylab.xlabel('# of viruses at the end of trial')
    pylab.ylabel('freq')
    
    #pylab.legend()
    pylab.show()
    
    return nvirus
        
#    return finalNVirusAllTrials    # this statement if for the simulationDelayedTreatment() function
    

#stat = simulationWithDrugVariableSteps(100, 1000, 0.1, 0.05, {'guttagonol': True}, 0.005, 300, 150)

#print stat
# sum(stat[0]) = 300, the number of trials

def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """

    nStepBfDrug = 300
    
    nVirus1 = simulationWithDrugVariableSteps(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, numTrials, nStepBfDrug)
    nVirus2 = simulationWithDrugVariableSteps(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, numTrials, nStepBfDrug)
    nVirus3 = simulationWithDrugVariableSteps(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, numTrials, nStepBfDrug)
    nVirus4 = simulationWithDrugVariableSteps(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, numTrials, nStepBfDrug)       
                  
    pylab.subplot(4, 1, 1)
    pylab.hist(nVirus1,bins=20,label = str(nStepBfDrug)+' steps before drug')
    hist1 = pylab.title('Compare # of virus after variable time steps')
#    pylab.legend()
    pylab.ylabel('freq, '+str(nStepBfDrug)+' steps')
    

    pylab.subplot(4, 1, 2)
    nStepBfDrug = 150
    hist2 = pylab.hist(nVirus2,bins=10,label = str(nStepBfDrug)+' steps before drug')
#    pylab.legend()
    pylab.ylabel('freq, '+str(nStepBfDrug)+' steps')
    
    
    pylab.subplot(4, 1, 3)
    nStepBfDrug = 75
    hist31 = pylab.hist(nVirus3,bins=10,label = str(nStepBfDrug)+' steps before drug')
#    pylab.legend()
    pylab.ylabel('freq, '+str(nStepBfDrug)+' steps')
    
    
    pylab.subplot(4, 1, 4)
    nStepBfDrug = 0
    hist4 = pylab.hist(nVirus4,bins=10,label = str(nStepBfDrug)+' steps before drug')
#    pylab.legend()
    pylab.ylabel('freq, '+str(nStepBfDrug)+' steps')
    pylab.xlabel('# of viruses at the end of trial')

    pylab.show()
    
    return nVirus1, nVirus2, nVirus3, nVirus4

#simulationDelayedTreatment(300)


#===========================================================================================
#
# PROBLEM 2
#

def simulationWith2DrugsVariableSteps(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials, nStepBtwDrug):
    """
    Runs simulations and plots graphs for Problem Set 3, problem 5.
    Return the results of final virus counts for the specified # of trials

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """

    finalNVirusAllTrials = [0]*numTrials
    
    
    for j in range(numTrials):
        
        virusList = []
        for i in range(numViruses):
            B = ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)
            virusList.append(B)
    
        Y = TreatedPatient(virusList, maxPop)
    
        for i in range(150):
            Y.update()
            
        Y.addPrescription('guttagonol')
        
        for i in range(nStepBtwDrug):
            Y.update()
            
        Y.addPrescription('grimpex')
        
        for i in range(150):
            Y.update()
        
        finalNVirusAllTrials[j] = Y.getTotalPop()

    
    nvirus = pylab.hist(finalNVirusAllTrials,bins=10)
    pylab.title(str(nStepBtwDrug)+' steps between drugs')
    pylab.xlabel('# of viruses at the end of trial')
    pylab.ylabel('freq')
    
    #pylab.legend()
    pylab.show()
    
    return nvirus
        
#    return finalNVirusAllTrials    # this statement if for the simulationDelayedTreatment() function

stat = simulationWith2DrugsVariableSteps(100, 1000, 0.1, 0.05, {'guttagonol': False, 'grimpex': False}, 0.005, 300, 300)

print stat


def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
