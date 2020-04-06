# demo function for making one specific plot for RQ3: What is the difference in usage of wood in a household regarding a freestanding wooden stove and a freestanding pallet stove?

# E006667 ;"Biomassa huishoudens hout
# E007204 ;"Biomassa huishoudens pallet

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def biomassa_wood_plot(data):
    periods = ["2010JJ00",
               "2011JJ00",
               "2012JJ00",
               "2013JJ00",
               "2014JJ00",
               "2015JJ00",
               "2016JJ00",
               "2017JJ00",
               "2018JJ00"]
    # Biomassa wooden stove and pallet stove
    total_biomassa_wood = "E006667"
    total_biomassa_pallet = "E007204"
    totaal_energietoepassingen = "E007022"

    # subset of the dataframe
    data_wood = data[(data["BronTechniek"] == total_biomassa_wood) & (
        data["Energietoepassingen"] == totaal_energietoepassingen)]
    data_pallet = data[(data["BronTechniek"] == total_biomassa_pallet) & (
        data["Energietoepassingen"] == totaal_energietoepassingen)]

    # subset of the data, using the periods
    data_wood_periods = data_wood[data_wood["Perioden"].isin(periods)]
    data_pallet_periods = data_pallet[data_pallet["Perioden"].isin(periods)]

    # getting the data to be integers instead of strings
    data_wood_periods.loc[:, "BrutoEindverbruik_1"] = data_wood_periods.loc[:,
                                                                            "BrutoEindverbruik_1"].astype(int)
    data_pallet_periods.loc[:, "BrutoEindverbruik_1"] = data_pallet_periods.loc[:,
                                                                                "BrutoEindverbruik_1"].astype(int)

    # creating a new dataframe with Usage wood and Usage pallet as columns
    subset_biomassa = pd.DataFrame(
        {'Usage Wood': data_wood_periods["BrutoEindverbruik_1"].tolist(), 'Usage Pallet': data_pallet_periods["BrutoEindverbruik_1"].tolist()}, index=periods)

    # create barchart for difference in used Biomassa between wooden and pallet stoves in households in period 2010-2018
    barchart = subset_biomassa.plot.bar(
        title="Difference in used Biomassa between wooden and pallet stove in households", color=['#0077be', '#7ec850'], width=0.8)
    barchart.set_xlabel("Periods")
    barchart.set_ylabel("Total difference in used Biomassa")
    barchart.set_xticklabels(
        ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018"])
    return barchart
