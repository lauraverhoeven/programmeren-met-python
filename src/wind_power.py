# demo function for making one specific plot for RQ1: total avoided use of wind power changed over the period 2010-2018, and what part can be assigned 
# to wind power on land or at sea

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
  total_wind_power = "E006588"
  total_energy_applicability = "E007022"

  # subset data frame to get the total wind power in energy applicablity
  data_total = data[(data["BronTechniek"]==total_wind_power) & (data["Energietoepassingen"]==total_energy_applicability)]

  # subset data frame to get periods 2010-2018 
  data_total_periods = data_total[data_total["Perioden"].isin(periods)]

  # change avoided use from strings to integers
  data_total_periods["VermedenVerbruik_3"] = data_total_periods["VermedenVerbruik_3"].astype(int)
  # subset data frame to get the avoided use
  data_total_periods_avoided = data_total_periods[["Perioden","VermedenVerbruik_3"]]

  # create barchart for total avoided use of fossil energy due to wind power in period 2010-2018
  barchart = data_total_periods_avoided.plot.bar(x="Perioden",y="VermedenVerbruik_3", legend=False, title="Total avoided use of fossil energy due to wind power")
  barchart.set_xlabel("Periods")
  barchart.set_ylabel("Total avoided use of fossil energy")
  barchart.set_xticklabels(["2010","2011","2012","2013","2014","2015","2016","2017","2018"])
  return barchart

  


  

