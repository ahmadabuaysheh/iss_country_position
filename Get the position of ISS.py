import requests

def get_country_of_ISS(google_api_key):
    iss_api = "http://api.open-notify.org/iss-now.json"
    iss_api_data = rq.get(iss_api).json()
    lat = float(iss_api_data["iss_position"]["latitude"])
    lon = float(iss_api_data["iss_position"]["longitude"])
    link = "https://maps.googleapis.com/maps/api/geocode/json?key="+google_api_key+"&result_type=country&latlng="+str(lat)+","+str(lon)
    google_maps_data = requests.get(link).json()
    Country = google_maps_data["results"][0]["address_components"][0]["long_name"]
    return Country
