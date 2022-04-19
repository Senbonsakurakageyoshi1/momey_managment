# Python3 program to show the Implementation of VERBOSE in RegEX
import re


def validate_email(email):
    # RegexObject = re.compile( Regular expression, flag )
    # Compiles a regular expression pattern into
    # a regular expression object
    regex_email = re.compile(r"""
						^([a-z0-9_\.-]+)				 # local Part
						@							 # single @ sign
							([0-9a-z\.-]+)				 # Domain name
						\.							 # single Dot .
							([a-z]{2,6})$				 # Top level Domain	
						""", re.VERBOSE | re.IGNORECASE)

    # RegexObject is matched with the desired
    # string using fullmatch function
    # In case a match is found, search()
    # returns a MatchObject Instance
    res = regex_email.fullmatch(email)

    # If match is found, the string is valid
    if res:
        print("{} is Valid. Details are as follow:".format(email))

        # prints first part/personal detail of Email Id
        print("Local:{}".format(res.group(1)))

        # prints Domain Name of Email Id
        print("Domain:{}".format(res.group(2)))

        # prints Top Level Domain Name of Email Id
        print("Top Level domain:{}".format(res.group(3)))
        print()

    else:
        # If match is not found,string is invalid
        print("{} is Invalid".format(email))


# Driver Code
validate_email("expectopatronum@gmail.com")
validate_email("avadakedavra@yahoo.com@")
validate_email("Crucio@.com")
