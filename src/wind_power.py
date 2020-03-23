# demo function for making one specific plot for RQ1: total avoided use of wind power changed over the period 2010-2018, and what part can be assigned
# to wind power on land or at sea

# make a bar plot with different colors of wind power at sea and wind power on land
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def wind_energy_plot(data):
    periods = ["2010JJ00",
               "2011JJ00",
               "2012JJ00",
               "2013JJ00",
               "2014JJ00",
               "2015JJ00",
               "2016JJ00",
               "2017JJ00",
               "2018JJ00"]

    # column wind power at sea
    wind_power_sea = "E006637"

    # column wind power on land
    wind_power_land = "E006638"

    # total energy of wind power column
    total_energy_applicability = "E007022"

    # subset data frame to get the data of sea and data of land in energy applicability
    data_sea = data[(data["BronTechniek"] == wind_power_sea) & (
        data["Energietoepassingen"] == total_energy_applicability)]
    data_land = data[(data["BronTechniek"] == wind_power_land) & (
        data["Energietoepassingen"] == total_energy_applicability)]

    # subset data frame sea & land to get periods 2010-2018
    data_sea_periods = data_sea[data_sea["Perioden"].isin(periods)]
    data_land_periods = data_land[data_land["Perioden"].isin(periods)]

    # change avoided use relative from strings to integers
    data_sea_periods["VermedenVerbruikRelatief_4"] = data_sea_periods["VermedenVerbruikRelatief_4"].astype(
        float)
    data_land_periods["VermedenVerbruikRelatief_4"] = data_land_periods["VermedenVerbruikRelatief_4"].astype(
        float)

    # subset data frame to get the avoided use relative
    data_sea_periods_avoided_relative = data_sea_periods[[
        "Perioden", "VermedenVerbruikRelatief_4"]]
    data_land_periods_avoided_relative = data_land_periods[[
        "Perioden", "VermedenVerbruikRelatief_4"]]

    # make a new dataframe of the two dataframes, make a list of it to be able to get them next to each other,
    data_total_periods_avoided_relative = pd.DataFrame(
        {'Wind power at sea': data_sea_periods_avoided_relative["VermedenVerbruikRelatief_4"].tolist(), 'Wind power on land': data_land_periods_avoided_relative["VermedenVerbruikRelatief_4"].tolist()}, index=periods)
    print(data_total_periods_avoided_relative)

    barchart = data_total_periods_avoided_relative.plot.bar(
        rot=0, title="Total avoided use of fossil energy relatively", color=['#0077be', '#7ec850'], width=0.8)
    barchart.set_xlabel("Periods")
    barchart.set_ylabel("Total relative avoided use of fossil energy")
    barchart.set_xticklabels(
        ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018"])
    return barchart
