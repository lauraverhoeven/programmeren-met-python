# How much has the avoidance of CO2 emission in the Netherlands changed in the period 1990 to 2018
import pandas as pd
import numpy as np


def emission_changed(data):
    # How much has the avoidance of CO2 emission in the Netherlands changed in the period 1990 to 2018

    # total energy applicability
    energy_applicability = "E007022"
    # the total of energy sources
    total_of_energy_sources = "T001028"

    # getting a subset of the dataframe of the total energy applicability and the total of energy sources
    data_emission = data[(data["Energietoepassingen"] == energy_applicability) & (
        data["BronTechniek"] == total_of_energy_sources)]

    # getting rid of the missing values, by deleting these values from the data (instead of making them NaN values)
    data_emission = data_emission[(data_emission["VermedenEmissie_5"] != ".")]

    # changing the avoided use of CO2 emission from strings to integers using loc to avoid getting a warning that we are trying to set a value on a copy of a slice from a dataframe
    data_emission.loc[:, "VermedenEmissie_5"] = data_emission.loc[:, "VermedenEmissie_5"].astype(
        int)

    # making the index for the x-as (without 'JJ00')
    periods = data_emission["Perioden"].tolist()
    stripped = [period[:4] for period in periods]

    # getting a dataframe of the data to graph
    data_emission_subset = pd.DataFrame(
        {'Avoided CO2 emission': data_emission["VermedenEmissie_5"].tolist()}, index=stripped)

    # making a bar graph
    barchart = data_emission_subset.plot(
        rot=90, title="Total avoided CO2 emission from 1990-2018", color="#121846", legend=False)
    barchart.set_xlabel("Periods")
    barchart.set_ylabel("Total avoided CO2 emission")

    return barchart
