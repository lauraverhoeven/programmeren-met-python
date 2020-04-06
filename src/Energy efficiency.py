
def efficiency(data):
    a=data.loc[i,"VermedenEmissie_5"]
    b=data.loc[i,"BrutoEindverbruik_1"]
    #converting strings to integers
    int_a= int(a)
    int_b= int(b)
    yearsefficiency=(int_a/int_b)
    return yearsefficiency

def barchart(data, efficiency):
#setting some lists
    list0=["Waterforce", "Wind", "Sun","Earth energy", "Biomass"]
    list2018= [144,260,608,1304, 2232]
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
                list2.append(efficiency(data))
            Renewable_frame = pd.DataFrame({'Energy source':list0, 'Efficiency':list2})
            Efficiencybars = Renewable_frame.plot.bar(x= 'Energy source', y='Efficiency',title='Efficiency:Avoided Emission/Consumption (in Kton/TJ)', rot=0)
            plt.show()
        elif yearbar==2018:
            list2= []
            for i in list2018:
                list2.append(efficiency(data))
            Renewable_frame = pd.DataFrame({'Energy source':list0, 'Efficiency':list2})
            Efficiencybars = Renewable_frame.plot.bar(x= 'Energy source', y='Efficiency',title='Efficiency:Avoided Emission/Consumption (in Kton/TJ)', rot=0)
            return Efficiencybars
        else:
            print("You typed the wrong number. Please try again.")
        Quit=input("Do you want to quit? y/n") 
        if Quit=="y":
            Repeat=False
            



def linechart (data, efficiency): 
#setting up lists. 0 will be used in the graph, 2018 is used as a basis: when you want to
#know the efficiency of for example 2016, you mustdo 144-2: then you get at the line 
#where you can calculate the efficiency of in this example 2016. 
#the other lists here are still empty, but will be filled later.
list0=["Waterforce", "Wind", "Sun"]
list2018= [144,260,608]
wateryearlist= []
sunyearlist= []
windyearlist= []

#a while loop makes it possible to do multiple things.
repeat= True
while repeat:
    try:    
        print('Welcome to the linegraph function. You can select 2 years as a beginning and end of your x-axis of your line graph.')
        #the user must select 2 years: after this is done, the program can make a line graph of all yeras between year1 and year2
				year1= int(input('Which year do you want the line graph to start with?'))
        year2= int(input('Which year do you want the line graph to end with?'))
        #the year must be between 1990 and 2018 (thats the scope of the original dataset)
        #and for the order, year2 must be bigger than year1
        if 1989 <= year1 <= 2018 and 1989 <= year2 <= 2018 and year2>year1:
            #making a list with all dates in between year 1 and year2
            year=year2
            yearslist= []
            #for appending the last year
            yearslist.append(year)
            #making a list of the years in between year1 and year2. 
            #This looks like a listed countdown.
            while year>year1:
                year= year-1
                yearslist.append(year)
        
            #because the list is now like a countdown, we want to sort it,
            # for the right order of years, which we need for the graph
            yearslist.sort()
            
            #calculating the efficiencies per Year, per energy source, 
            #using def efficiency, with dataset renew
            #We do this with 5 different energy sources
            for k in yearslist:
                #list2018[0]is used to get to the rownumber
                #for the particular energysource in 2018. 
                #k is a year in between year1 and year2. for example:
                #i= 144-(2018-2016)= 142. This is 
                #the row of code out of which you can get 
                #the efficiency via a calculation.
                i=(list2018[0])-(2018-k)
                #i is used in def efficiency
                wateryearlist.append(efficiency(data))
           
            for k in yearslist:
                i=(list2018[1])-(2018-k)
                windyearlist.append(efficiency(data))
            
            for k in yearslist:
                i=(list2018[2])-(2018-k)
                sunyearlist.append(efficiency(data))
            
            #prapairing the multiline-graph
            sustainablestructure = pd.DataFrame({"Waterforce":wateryearlist, "Wind":windyearlist, "Sun":sunyearlist,"Earth energy":earthyearlist, "Biomass":bioyearlist},index=yearslist)
            lines = sustainablestructure.plot.line()
            #making a graph: setting some thing
            
            return lines
            
            
        else: 
            print("You typed the wrong number. Look out that the first number is smaller than te second. Please try again.")
    except Exception:
        print("You must typ a number/ numbers")   
    Quit=input("Do you want to quit? y/n") 
    if Quit=="y":
        repeat=False

