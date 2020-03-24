# How much has the avoidance of CO2 emission in the Netherlands changed in the period 1990 to 2018
# and which renewable energy source has relatively reduced CO2 emission the most?
import pandas as pd
import numpy as np


def emission_changed(data):
    energy_applicability = "E007022"
    total_of_energy_sources = "T001028"

    data_emission = data[(data["Energietoepassingen"] == energy_applicability) & (
        data["BronTechniek"] == total_of_energy_sources)]

    try_ = data_emission.replace(to_replace=".", value=np.nan)
    data_set = try_.fillna(0)

    data_set["VermedenEmissie_5"] = data_set["VermedenEmissie_5"].astype(
        int)

    data_emission_subset = pd.DataFrame(
        {'Avoided CO2 emission': data_set["VermedenEmissie_5"].tolist()}, index=data_set["Perioden"])

    barchart = data_emission_subset.plot(
        rot=90, title="Total avoided CO2 emission from 1990-2018", color="#121846")
    barchart.set_xlabel("Periods")
    barchart.set_ylabel("Total avoided CO2 emission")

    return barchart
