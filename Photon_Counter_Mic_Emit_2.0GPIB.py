
"""
Created on Saturday Feb 27 2021

@authors: Lucas Wright
for help pyvisa documentaion:
https://pyvisa.readthedocs.io/en/latest/introduction/example.html
"""

#--------------------------------Library Imports------------------------------#


import sys
import pyvisa
import datetime
import time
import os
import numpy as np
import serial
import random
      
#------------------------ Setting up Arduino Connectivity---------------------#
#arduino = serial.Serial('COM6', 9600)
#arduino.close()

#--------------------------Setting Up GPIB Connectivity-----------------------#


def collectData(freq_width, centered_freq, num_of_readings, legnth_of_collection):
    #get in contact with the PhotonCounter and MicEmit
    rm = visa.ResourceManager()
    instList = rm.list_resources()
    print(instList)
    #connecting to the instroments:
    photonCounter = rm.open_resource('GPIB0::23::INSTR')
    micEmit = rm.open_resource('GPIB0::27::INSTR')
    
    #generate the list of data point we want to get pointlist[[freqLocation, length of collection],[]...]:
    stepSize = freq_width/num_readings
    starting_freq = (centered_freq - freq_width/2)
    pointList = []
    for j in range(num_readings):
        pointlist.append([starting_freq * j, length_of_collection])
    
    #shuffle this list to decrease systematic error
    random.shuffle(pointList)
    
    #create an empty list to store the data:
    dataList = []
    #run a loop to gather the points: 
    for point in dataList:
        dataList.append(measure(point, micEmit, photonCounter))
    # here we send the list on the form dataList = [[freq, count]...]    
    return dataList
        
    
    
    #create a list of the frequencies we are testing in random order
    #run a loop through that list that captures the flourenecy at those intervals.
    #add that data point to the list dataList
    return (dataList)



def measure(freq, legnth_of_collection, micEmit, photonCounter):
    #set the microwave to correct freq\
    for i in range(4):
        test = 1000000
        micEmit.query("FREQ?")
        query = "FREQ"+str((i+1)*int(test))
        print(query)
        micEmit.query(query)
        micEmit.query('fREQ5000000')
        time.sleep(2)
        
        
    
    
    
"""
#functions for preping the instroments for taking data:
interval_in_ms = 500
num_of_redings = 100
photonCounter.write("stuff here for the set up")
micEmit.write("stuff here for the set up")

#function used by collect data to build data point
def AddData(dataTimes, counts, rates):                                          
    ""Given three lists of the same length, add all the data to data file""
    for entry in range(len(dataTimes)):
        
        DataString = (str(dataTimes[entry]) + ",   " + str(counts[entry]) +
                      ",   " + str(rates[entry]) + "\n")                        
        # writes datastring into tempporary data file
        temp.write(DataString)          

# Here we will write a function that collects data.
def collectData(freq_width, centered_freq, num_of_readings, legnth_of_collection):
    #create a list of the frequencies we are testing in random order
    #run a loop through that list that captures the flourenecy at those intervals.
    #add that data point to the list dataList
    return (dataList)

def plot_data(dataList):
    #plot the data real quick
    return
def saveData_CV;
    #quick things to save the data to a CV
    return




    def TSETtoFloat(self, text):
        #converts a string of the form NUMeNUM to an float
        return float(text)

        #set the sr400 to that time period
        photonCounter.write('CP2, ' + TSET)
    
            
        #this will need some changing for sending the right data to be saved
        "starts the data collection"
        #reset data and tracking variables
        photonCounter.write('cr')
     
       
        #sets dwell time, 
        photonCounter.write("DT 2E-3")
        #set number of periods (aka time bins)
        photonCounter.write("NP 2000")
        #When the number of time bins (Nperiods) reaches its maximum of 2000, 
        #reset to 0 and continue measuring 
        photonCounter.write("NE 1")
        #ask for the current period (1-2000) -> should = 1 here
        self.curPeriod= int(photonCounter.query("NN"))
       
        #start counter        
        photonCounter.write("cs")
        #starts the QTimer at timeInt, already includes 2ms dwell time
        self.graphTimer.start((self.TimeInt) * 1000)
        
    #very important
    def FileSetup(self):
        "sets up files"
        TimeL = str(datetime.datetime.now().time())
        #this version of windows does not allow you to save a file with ":" in its title,
        # so i had to replace all the colons with semi-colons.
        TimeS = TimeL[0:2] + ";" + TimeL[3:5] + ";" + TimeL[6:8]
        folder = DateL + "_" + TimeS + "_SavedData"  
        #The directory FileName goes in, look in SavedData folder in documents!
        saveDir = "C:/Users/HorowitzLab/Documents/SavedData/" + folder 
        os.makedirs(saveDir)
        os.chdir(saveDir)
        self.RunCount += 1
        global tempFileName 
        tempFileName = (DateS + "_Data_" + TimeS + ".csv")
        global temp
        temp = open(tempFileName, "w+")
        temp.write(Header)
    
    #this gathers data ino a list. we will need to change to data being stored here
    def Update(self):
        #gets current count and updates instance variables
        #create list holders for times and rates
        countVals = []
        timeVals = []
        rateVals = []
        
        #ask SR400 to give current Nperiod number
        self.curPeriod= int(photonCounter.query("NN"))
        #ask SR400 to give the photon count
        data = int(photonCounter.query("QA " + str(self.curPeriod))) 
        
        #get data: continually ask for i-th point until not -1, add to list
        #poll for data until get -1
        while (data > -1):
           
            #add to list, update other vals
            countVals.append(data)
            self.curTimeVal += self.TimeInt
            self.curTimeVal = round(self.curTimeVal, 3)
            #print(self.curTimeVal)
            timeVals.append(self.curTimeVal)
            #print(timeVals)
            rateVals.append(round(data / (self.TimeInt-0.002), 1))
            
            #at small time bins (> 0.2sec), the code will try to catch up to the measurements being taken
            # and produce a rateVals with multiple measurements, with only the last one being new data.
            #this if else loop ensures that this lag doesnt interfere with data collection
            if len(rateVals) > 1: 
                self.Ratelst.append(rateVals[-1])
                self.Countlst.append(countVals[-1])
                self.Timelst.append(round(self.curTimeVal,3))
            else:  
                self.Ratelst.append(rateVals[0])
                self.Timelst.append(round(timeVals[0],3))
                self.Countlst.append(countVals[0])
            
            #calculates the avg, stdv, sterr and appends them to their respective lists 
            self.average = round(sum(self.Ratelst)/len(self.Ratelst), 1)
            self.StDev = round(np.std(self.Ratelst), 0)
            self.StErr = round( self.StDev / np.sqrt(len(self.Ratelst)), 0)

            #increase curPeriod, query for next data point
            self.curPeriod += 1
            data = int(photonCounter.query("QA " + str(self.curPeriod)))
        """
        
def main():
    #User input Vars:
        #Hz
    freq_width = 1
        #Hz range 950kHz-6.075GHz
    centered_freq = 5e6
    number_of_readings = 1
        #sec
    legnth_of_collection = 1
        #dBm range(-110-16.5)
    Amplitude = 
    # def collectData(freq_width, centered_freq, num_of_readings, legnth_of_collection):
    
    
    
    
if __name__=='__main__':
    main()
