import openpyxl
from geopy.geocoders import Nominatim
import csv



geolocator = Nominatim(user_agent='my_geocoder')


with open(r'C:\Users\Alisha\Documents\Rescom\Data\Addresses.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    rows = list(reader)

    
    rows[0].extend(['Latitude', 'Longitude'])

    
    for row in rows[1:]:
        address = row[0]  

        try:
            
            location = geolocator.geocode(address)

            if location is not None:
                # Extract the latitude and longitude
                latitude = location.latitude
                longitude = location.longitude

                
                row.extend([latitude, longitude])
        except:
            
            print(f"Geocoding failed for address: {address}")


with open('output1.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(rows)