from flashgeotext.geotext import GeoText

def new_get_city(text):
    geotext = GeoText()

    return  geotext.extract(text)