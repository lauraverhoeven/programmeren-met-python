import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data= pd.read_csv("raw_data_renewable_energy.csv", sep=";")

def barchart(data):
#setting some lists
    list0=["Waterforce", "Wind", "Sun","Earth energy", "Biomass"]
    list2018= [144,160,608,1304, 2232]
    list2017= []
    for i in list2018:
        d=i-1
        list2017.append(d)
#controle:print(list2017)
#calculating efficiency
    Repeat= True
    while Repeat:
        yearbar=int(input("Of which year do you want to see the efficiency? 2017 of 2018?"))
        if yearbar==2017:
            list2= []
            for i in list2017:
                a=data.loc[i,"VermedenEmissie_5"]
                b=data.loc[i,"BrutoEindverbruik_1"]
                int_a= int(a)
                int_b= int(b)
                efficiency=(int_a/int_b)
                list2.append(efficiency)
            Renewable_frame = pd.DataFrame({'Energy source':list0, 'Efficiency':list2})
            Efficiencybars = Renewable_frame.plot.bar(x= 'Energy source', y='Efficiency',title='Efficiency:Avoided Emission/Consumption (in Kton/TJ)', rot=0)
            plt.show()
        elif yearbar==2018:
            list2= []
            for i in list2018:
                a=data.loc[i,"VermedenEmissie_5"]
                b=data.loc[i,"BrutoEindverbruik_1"]
                int_a= int(a)
                int_b= int(b)
                efficiency=(int_a/int_b)
                list2.append(efficiency)
            Renewable_frame = pd.DataFrame({'Energy source':list0, 'Efficiency':list2})
            Efficiencybars = Renewable_frame.plot.bar(x= 'Energy source', y='Efficiency',title='Efficiency:Avoided Emission/Consumption (in Kton/TJ)', rot=0)
            return Efficiencybars
        else:
            print("You typed the wrong number. Please try again.")
        Quit=input("Do you want to quit? y/n") 
        if Quit=="y":
            Repeat=False
            

def efficiency(data):
    a=data.loc[i,"VermedenEmissie_5"]
    b=data.loc[i,"BrutoEindverbruik_1"]
    #converting strings to integers
    int_a= int(a)
    int_b= int(b)
    yearsefficiency=(int_a/int_b)
    return yearsefficiency

def linechart (data): 
#setting some lists
list0=["Waterforce", "Wind", "Sun","Earth energy", "Biomass"]
list2018= [144,160,608,1304, 2232]
wateryearlist= []
sunyearlist= []
windyearlist= []
earthyearlist= []
bioyearlist= []

repeat= True
while repeat:
    try:    
        print('Welcome to the linegraph function. You can select 2 years as a beginning and end of your x-axis of your line graph.')
        year1= int(input('Which year do you want the line graph to start with?'))
        year2= int(input('Which year do you want the line graph to end with?'))
        if 1990 <= year1 <= 2018 and 1990 <= year2 <= 2018 and year2>year1:
            year=year2
            yearslist= []
            yearslist.append(year)
            #making a list of the years in between year1 and year2
            while year>year1:
                year= year-1
                yearslist.append(year)
            print(yearslist)
            yearslist.sort()
            print(yearslist)
            #calculating the efficiencies per Year, per energy source
            for k in yearslist:
                i=(list2018[0])-(2018-k)
                wateryearlist.append(efficiency(renew))
            print(wateryearlist)
            for k in yearslist:
                i=(list2018[1])-(2018-k)
                windyearlist.append(efficiency(renew))
            print(windyearlist)
            for k in yearslist:
                i=(list2018[2])-(2018-k)
                sunyearlist.append(efficiency(renew))
            print(sunyearlist)
            for k in yearslist:
                i=(list2018[3])-(2018-k)
                earthyearlist.append(efficiency(renew))
            print(earthyearlist)
            for k in yearslist:
                i=(list2018[4])-(2018-k)
                bioyearlist.append(efficiency(renew))
            print(bioyearlist)
            #making a graph
            plt.title("Efficiency over the years")
            plt.xlabel("Years")
            plt.ylabel("Efficiency")
            sustainablestructure = pd.DataFrame({"Waterforce":wateryearlist, "Wind":windyearlist, "Sun":sunyearlist,"Earth energy":earthyearlist, "Biomass":bioyearlist},index=yearslist)
            lines = sustainablestructure.plot.line()
            return lines
          
            
        else: 
            print("You typed the wrong number. Look out that the first number is smaller than te second. Please try again.")
    except Exception:
        print("You must typ a number/ numbers")   
    Quit=input("Do you want to quit? y/n") 
    if Quit=="y":
        repeat=False

