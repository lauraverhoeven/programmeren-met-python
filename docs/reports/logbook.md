# Choice of data set
We have chosen to use the data set "Hernieuwbare energie; verbruik naar energiebron, techniek en toepassing" (Renewable energy; per energy source, technology and application, available at: https://opendata.cbs.nl/statline/portal.html?_la=nl&_catalog=CBS&tableId=83109NED&_theme=126)
for our research project. This data set includes information about use of renewable energy sources (wind-, water-, solarpower, geothermal energy, aerothermic energy and biomass) in the years 1990 to 2018 in the Netherlands,
including information about the avoided use of fossil energy and avoided CO2 emissions per renewable energy source. 
We are intereseted in this data set, because renewable energy is a very relevant topic with a huge impact on our generation. 
We are curious to see how renewable energy is used in the Netherlands and how its use and impact has changed in our lifetimes.
We think this is a topic which statistics should be more widely known and we think it would be good if the results from this research are easily accesible.
Thus, using this research project, we would like to create some insight in the use of renewable energy in the Netherlands for anyone interested in this topic.



# Research questions

**RQ1: How has the total avoided use of fossil energy due to wind power, changed over the period 2010-2018? 
What part of this avoided use of fossil energy can be assigned to wind power on land and to wind power at sea?** 
Possible methods: bar graphs per year (2010-2018) of the total avoided use of fossil energy due to wind power with the years on the x-axis, 
and the total avoided use of fossil energy on the y-axis, with different colors to highlight the assignment to wind power on land and to wind power at sea per year (i.e. on the bars).

**RQ2: How much has the CO2 emission in the Netherlands changed in the period of 1990 to 2018 and which renewable energy source has relatively reduced CO2 emission the most?** 
Possible methods: a line chart showing the CO2 emission, with the years 1990-2018 on the x-axis and CO2 emission on the y-axis. For the second part of the research question:
a bar graph with a bar for each renewable energy source per year (1990-2018) on the x-axis, with relative reduced CO2 emission on the y-axis. 

**RQ3: What is the difference in usage of wood in a household regarding a freestanding wooden stove and a freestanding pallet stove?**
Possible methods: Analysing the data from the charts and putting them in a graphic from different perspectives. Bar graphs with on the x axis the two bars and on the y axis the amount of wood used.

**RQ4 Which energy source was the most efficient in 2018 in terms of producing energy with the highest prevention of CO2 emission?** 
To answer the question, one must calculate how much CO2 is emitted per kilowatt-hour of energy ( of a particular renewable source).
Then you can make a bar chart of it with on the y- axis the efficiency and on the x-axis the different energy sources. 

# Possible Python Packages to Methods

| Analysis method | Python package | Function | Function description | Inputs | Outputs |
| ------ | ------ | ------ | ------ | ------ | ------ | 
| Bar chart | matplotlib | [pyplot.bar](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.bar.html) | Makes a bar chart of the data | Sequence of scalars (like width, height, orientation) | BarContainer |
| Bar plots | pypi | [barplots](https://pypi.org/project/barplots/) | This makes a bar plot of the data | Sequence of scalars (like width, height, orientation) | BarContainer |
| Bar plots | pypi.org | [barplots](https://pypi.org/project/barplots/) | Make barplots from multi-indexed dataframes | Sequence of scalars (like width, height, orientation) | A bar plot |
| Stacked bar chart | matplotlib | [pyplot.bar](https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/bar_stacked.html) | Creates a figure with axis | Sequence of scalars (like width, height, orientation) | A figure with axis to which bars can be added |
| Creating a line chart | matplotlib | [pyplot.plot](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html) | Adds a line to a line chart figure | x-axis and y-axis values or indexable data | A list of Line2D objects|
| Creating a legend | matplotlib | [pyplot.legend](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.legend.html) | Creates a legend | Sequence of strings | A legend |
| Showing the resulting figure(s) | matplotlib | [pyplot.show](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.show.html) | None | None |
| Reading the data file | pandas | [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) | Read comme-seperated values into DataFrame | Filepath, seperator, header | DataFrame |
| Filtering subsets from the data | pandas | [dataframe.filter](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.filter.html) | Creates subsets from the dataframe rows or columns according to the specified index labels | Items, like: ..., regex, axis | Same type as input ||

# Program flow

We have made an [activity diagram](results/figures/activity_diagram.jpeg) that gives a summary of the program flow.
The file [main.py](src/main.py) is a skeleton implementation of the planned main module. 
Planned additional files are [data_handling.py](src/data_handling.py) and the modules for the separate questions.

# Distribution of work

Since one of our members has stopped with the course, a few weeks before the end of the course, we had to improvise a little bit. Research question 1 and 2 have been answered by Laura Verhoeven. Research question 2 has been changed, it does not include the second part of the question ("which renewable energy source has relatively reduced CO2 emission the most"). The first part of research question 2 has been answered. 
Emiel Robben answered research question 3, and Maarten van Oschen answered research question 4. 

# Poster 

The poster containing the different graphs of our questions is located at [poster](docs/reports/Renewable_energy_poster_Teams_final_versionPDF.pdf)
