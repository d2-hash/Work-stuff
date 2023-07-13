# Work-stuff
A brief overview of the technologies used are: Python, more specifically folium, geocoder, numpy, pandas, as well as a few other libraries.
The report was generated in DASH, cleaned with python, and translated into a CSV through our coordinate finding script for better layout 
in a pandas dataframe.

This assignment was given to me by the VP of Project management, and estimating.  The instructions were to pull the information from
an internal software we use from NextGear solutions, and generate useable data from it's reporting system.  I wrote a python script to
iterate over the address column, and write two new columns for lattitude and longitude to plot these as blips on a map.
I tried a few different geocoding api's prior to selecting one.  

Unfortunately, a little less than 1/3 of all the addresses did not populate a gps coordinate that was plotable.  Due to this 
data being crucial to the goal of the assignment, I populated the vacant fields manually.  I was able to achieve the desired result,
and present this on a one slide presentation that did influence the location of the new warehouse ultimately.
