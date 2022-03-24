from new_get_city import *


def pre_treatment(result):
    z = []
    i = 0
    while i < len(result):
        z.append(result[i][1])
        i += 1

    i = 0
    while i < len(z):

        if new_get_city(z[i].capitalize())['cities'] != {}:
            Ville = z[i]


        i += 1


    return Ville