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

    # hieronder staand wilt hij niet uitvoeren, wat je moet doen is kijken nara mijn functie in wind_power (get_subset_dataframe_parts) en op basis
    # hiervan kijken wat je moet doen..

    data_total = data[(data["BronTechniek"] == total_biomassa_wood) & data[(data["BronTechniek"] == total_biomassa_pallet) & (
        data["Energietoepassingen"] == totaal_energietoepassingen)]]

    # subset data frame to get periods 2010-2018
    data_total_periods = data_total[data_total["Perioden"].isin(periods)]

    # create barchart for difference in used Biomassa between wooden and pallet stoves in households in period 2010-2018
    barchart = data_total_periods.plot.bar(x="Perioden", y="Verbruik_3", legend=False,
                                           title="Difference in used Biomassa between wooden and pallet stove in households")
    barchart.set_xlabel("Periods")
    barchart.set_ylabel("Total difference in used Biomassa")
    barchart.set_xticklabels(
        ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018"])
    return barchart
