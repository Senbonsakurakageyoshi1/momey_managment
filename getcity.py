import geograpy4
def get_city(text):

    city = geograpy4.get_place_context(text,ignoreEstablishments=False,addressOnly=True)

    return city