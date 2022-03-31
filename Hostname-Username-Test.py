import argparse

#set up argument parsing
PARSER = argparse.ArgumentParser()
PARSER.add_argument("hostname", help="Hostname can be one or many hostnames. Separate multiple hostnames by comma")
PARSER.add_argument("username", help="Username to connect to the hosts.")

ARGS = PARSER.parse_args()

#assign variables
hostname = ARGS.hostname
username = ARGS.username

#if not USERNAME:
#    USERNAME = admin

print('The hostname submitted was: ' + hostname + ' and the username was: ' + username)
