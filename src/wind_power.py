# demo function for making one specific plot for RQ1: total avoided use of wind power changed over the period 2010-2018, and what part can be assigned
# to wind power on land or at sea

# make a bar plot with different colors of wind power at sea and wind power on land
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_subset_dataframe_total(data, sort=0):
    # getting a subset of the data, the total avoided use of fossil energy (absolute and relative) due to wind power

    periods = ["2010JJ00",
               "2011JJ00",
               "2012JJ00",
               "2013JJ00",
               "2014JJ00",
               "2015JJ00",
               "2016JJ00",
               "2017JJ00",
               "2018JJ00"]

    # total energy of wind power column
    total_energy_applicability = "E007022"
    # total wind power
    total_wind_power = "E006588"

    # subset of data total wind power and total energy applicability
    data_total = data[(data["BronTechniek"] == total_wind_power) & (
        data["Energietoepassingen"] == total_energy_applicability)]

    # subset of the data with only these periods
    data_total_periods = data_total[data_total["Perioden"].isin(periods)]

    # change the data to the correct type
    data_total_periods["VermedenVerbruik_3"] = data_total_periods["VermedenVerbruik_3"].astype(
        int)
    data_total_periods["VermedenVerbruikRelatief_4"] = data_total_periods["VermedenVerbruikRelatief_4"].astype(
        float)

    # get the new subset of the total avoided use of fossil energy and relative avoided use of fossil energy with these periods
    if sort == 0:
        data_subset = pd.DataFrame(
            {'Absolutely': data_total_periods["VermedenVerbruik_3"].tolist()}, index=periods)
    elif sort == 1:
        data_subset = pd.DataFrame(
            {'Relatively': data_total_periods["VermedenVerbruikRelatief_4"].tolist()}, index=periods)
    else:
        raise ValueError("Incorrect value, put in correct value (0 or 1).")

    # get the dataframe
    return data_subset

# getting subset of the data, avoided use of fossil energy (with a choice whether you want the absolute or the relative data) due to wind power on land and at sea.


def get_subset_dataframe_parts(data, sort=0):
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
    data_sea_periods["VermedenVerbruik_3"] = data_sea_periods["VermedenVerbruik_3"].astype(
        int)
    data_land_periods["VermedenVerbruik_3"] = data_land_periods["VermedenVerbruik_3"].astype(
        int)

    # make a new dataframe of the two dataframes, make a list of it to be able to get them next to each other,
    if sort == 0:
        data_total_periods_avoided = pd.DataFrame({'Wind power at sea': data_sea_periods["VermedenVerbruik_3"].tolist(
        ), 'Wind power on land': data_land_periods["VermedenVerbruik_3"].tolist()}, index=periods)
    elif sort == 1:
        data_total_periods_avoided = pd.DataFrame(
            {'Wind power at sea': data_sea_periods["VermedenVerbruikRelatief_4"].tolist(), 'Wind power on land': data_land_periods["VermedenVerbruikRelatief_4"].tolist()}, index=periods)
    else:
        raise ValueError("Incorrect value, put in a correct value (0 or 1).")

    # get the dataframe
    return data_total_periods_avoided


def bar_graph_total(dataframe, sort_graph=0):
    # Make a bar graph of the total avoided use of fossil energy due to the total wind power (choice between relatively and absolutely)
    if sort_graph == 0:
        graph = "absolutely"
    elif sort_graph == 1:
        graph = "relatively"
    else:
        raise ValueError("Incorrect value, put in correct value (0 or 1).")

    barchart = dataframe.plot.bar(
        rot=0, title=f"Total {graph} avoided use of fossil energy due to wind power", color="#121846", width=0.8)
    barchart.set_xlabel("Periods")
    barchart.set_ylabel(f"Total {graph} avoided use of fossil energy")
    barchart.set_xticklabels(
        ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018"])

    return barchart


def wind_energy_plot(data, sort_graph=0):
    # Make a bar graph of the total avoided use of fossil energy due to the wind power, with subdivisions on land and at sea (choice between relatively and absolutely)
    if sort_graph == 0:
        graph = "absolutely"
    elif sort_graph == 1:
        graph = "relatively"
    else:
        raise ValueError("Incorrect value, put in correct value (0 or 1).")

    barchart = data.plot.bar(
        rot=0, title=f"Total {graph} avoided use of fossil energy", color=['#0077be', '#7ec850'], width=0.8)
    barchart.set_xlabel("Periods")
    barchart.set_ylabel(f"Total {graph} avoided use of fossil energy")
    barchart.set_xticklabels(
        ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018"])
    return barchart
