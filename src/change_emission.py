# How much has the avoidance of CO2 emission in the Netherlands changed in the period 1990 to 2018
# and which renewable energy source has relatively reduced CO2 emission the most?
import pandas as pd
import numpy as np


def emission_changed(data):
    # How much has the avoidance of CO2 emission in the Netherlands changed in the period 1990 to 2018
    energy_applicability = "E007022"
    total_of_energy_sources = "T001028"

    data_emission = data[(data["Energietoepassingen"] == energy_applicability) & (
        data["BronTechniek"] == total_of_energy_sources)]

    try_ = data_emission.replace(to_replace=".", value=np.nan)
    data_set = try_.fillna(0)

    data_set["VermedenEmissie_5"] = data_set["VermedenEmissie_5"].astype(
        int)

    # making the index for the x-as (without 'JJ00')
    periods = data_set["Perioden"].tolist()
    stripped = [period[:4] for period in periods]

    # getting a dataframe of the data to graph
    data_emission_subset = pd.DataFrame(
        {'Avoided CO2 emission': data_set["VermedenEmissie_5"].tolist()}, index=stripped)

    # making a bar graph
    barchart = data_emission_subset.plot(
        rot=90, title="Total avoided CO2 emission from 1990-2018", color="#121846")
    barchart.set_xlabel("Periods")
    barchart.set_ylabel("Total avoided CO2 emission")

    return barchart


def renewable_source_relative(data):
    # Which renewable energy source has relatively reduced CO2 emission the most?
    energy_applicability = "E007022"

    water = "E006587"
    wind = "E006588"
    sun = "E006589"
    earth = "E006594"
    sky_warmth = "E006656"
    bio = "E006566"

    # emission = data[(data["Energietoepassingen"] == energy_applicability) & (
    #     data["BronTechniek"] == wind)]

    # print(emission)

    water_emission = data[(data["Energietoepassingen"] == energy_applicability) &
                          (data["BronTechniek"] == water)]

    # water_emission_periods = water_emission[(water_emission["Perioden"]) & (
    #     water_emission["VermedenEmissieRelatief_6"])]

    # emission_subset = pd.DataFrame(
    #     {'Avoided CO2 emission': water_emission["VermedenEmissieRelatief_6"].tolist()}, index=water_emission["Perioden"])
    # print(emission_subsets)
    # water_emission_2018 = water_emission[(
    #     water_emission["Perioden"] == "2018JJ00")]
    water_emission["VermedenEmissieRelatief_6"] = water_emission["VermedenEmissieRelatief_6"].astype(
        float)
    emission_subset = pd.DataFrame(
        {'Avoided CO2 emission': water_emission["VermedenEmissieRelatief_6"].tolist()}, index=water_emission["Perioden"])
    print(emission_subset)

    # print(type(water_emission_2018["VermedenEmissieRelatief_6"]))
    # print(type(water_emission_2018))

    # wind_emission = data[(data["Energietoepassingen"] == energy_applicability) & (
    #     data["BronTechniek"] == wind)]
    # wind_emission_2018 = wind_emission[(
    #     wind_emission["Perioden"] == "2018JJ00")]
    # wind_emission_2018["VermedenEmissieRelatief_6"] = wind_emission_2018["VermedenEmissieRelatief_6"].astype(
    #     float)

    # sun_emission = data[(data["Energietoepassingen"] ==
    #                      energy_applicability) & (data["BronTechniek"] == sun)]
    # sun_emission_2018 = sun_emission[(sun_emission["Perioden"] == "2018JJ00")]
    # sun_emission_2018["VermedenEmissieRelatief_6"] = sun_emission_2018["VermedenEmissieRelatief_6"].astype(
    #     float)

    # index = ["Waterpower", "Windenergy", "Sunenergy"]

    # water_emission_subset = pd.DataFrame(
    #     {'Relative avoided CO2 emission': [water_emission_2018["VermedenEmissieRelatief_6"].tofloat(), wind_emission_2018["VermedenEmissieRelatief_6"].tofloat(), sun_emission_2018["VermedenEmissieRelatief_6"].tofloat()]}, index=index)

    # # barchart = water_emission_subset.plot(
    # #     title="Total avoided CO2 emission", color="#121846")
    # # barchart.set_xlabel("Energy sources")
    # # barchart.set_ylabel("Total avoided CO2 emission")
    # # return barchart
