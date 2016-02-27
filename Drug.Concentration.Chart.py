import numpy
import random
import pylab

class Drug(object):
    
    """
    Representation of a course of drug treatment.
    """
   

    def __init__(self, pharmaceutical, dose, dosesPerDay, halfLife, days):

        """
        Initializes a course of drug treatment, saves all parameters as attributes of the instance.
        
        pharmaceutical: the name of the drug (a string).
        
        dose: the dosage per administraction of the pharmaceutical in milligrams (a float).

        dosesPerDay: the number of administrations of the pharmaceutical at stregnth dose each day (an integer).

        halfLife: the time it takes in hours for half of the pharmaceutical to be cleared out of the system (a float).

        days: the number of day of treament (an integer).
        """

        self.pharmaceutical = pharmaceutical
        self.dose = float(dose)
        self.dosesPerDay = dosesPerDay
        self.halfLife = float(halfLife)
        self.days = days
        
    def name(self):
        return self.pharmaceutical

    def dosage(self):
        return self.dose

    def perDay(self):
        return self.dosesPerDay
    
    def halflife(self):
        return self.halfLife

    def days(self):
        return self.days

    def hoursPerDose(self):
        return 24/self.perDay()

    def listHours(self):
        self.hoursList = []
        for hour in range(0, 24*self.days+1):
            if hour%8 == 0:
                self.hoursList.append(hour)
        return self.hoursList
            
    def numPills(self):
        return len(self.hoursList)-1

    def pillsList(self):
        self.pillsList=[]
        pills = 0
        while pills < 90:
            pills += 1
            self.pillsList.append(pills)
        self.pillsList.append(pills)
        return self.pillsList

    def timeSteps(self):
        self.timeSteps=[]
        self.timeSteps=range(0,91)
        return self.timeSteps

    def ConcKey(self):
        self.concKey = []
        for hour in self.hoursList:
            self.concKey.append(self.dose*(2**(-hour/self.halfLife)))
        return self.concKey


    def Plot(self):
        """
        Plots s chart showing the concentration of a drug over the course of treatment.
        """

        hours = self.listHours()
        self.ConcKey()
        concentrations = self.concentrations=[]
        count = 1
        for i in range(0, (self.dosesPerDay*self.days)+1):
            concentration = 0
            for c in range(0, count):
                concentration += self.concKey[c]
            self.concentrations.append(concentration)
            count += 1
##        pylab.semilogy()
##        pylab.semilogx()
        pylab.title('Concentration of Drug Over Time')
        pylab.xlabel('Hours')
        pylab.ylabel('Drug Concentration')
        pylab.xlim(0,150)
        pylab.plot(hours, concentrations, 'bo', linewidth=2, label = 'Concentration')
        pylab.plot(hours, concentrations, linewidth=2, label = 'Concentration')
        pylab.legend(loc = 'best')
        pylab.show()                       

    
