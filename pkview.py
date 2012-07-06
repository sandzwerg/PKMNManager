#!/usr/bin/env python

#from gi.repository import Gtk
import sqlite3
import pkdao

# Gibt ein, mehrere oder alle Pokemon mitsamt Locationinformation aus.
def print_pokemon(pokem):

    pkinfo, locs = pkdao.get_pkinfo(pokem)

    catch = "nicht gefangen."
    if pkinfo[2] != 0:
        catch = "gefangen!"

    print u"{0} {1},\t {2}".format(pkinfo[0], pkinfo[1], catch)

    for loc in locs:
        print u"\t Fangbar in {0}, {1}".format(loc[0], loc[1])
    
def add_location():

    pokemon = raw_input('Pokemoninformation? > ')
    edition = raw_input('Welche Edition? > ')
    location = raw_input('Welche Location? > ')
    
    pkdao.add_loc(pokemon, edition, location)
    
    print_pokemon(pokemon)
    moreinput = raw_input("Moechten Sie mehr Daten einpflegen? yes/N > ")
    moreinput = moreinput.lower()
    
    while moreinput == 'yes' or moreinput == 'y':
        edition = raw_input('Welche Edition? > ')
        loc = raw_input('Welche Location? > ')
    
        pkdao.add_loc(pokemon, edition, loc)
        print_pokemon(pokemon)
        moreinput = raw_input("Moechten Sie mehr Daten einpflegen? yes/N > ")
        moreinput = moreinput.lower()
  
#gibt eine pokemonliste nach den uebergebenen argumenten gefiltert aus
def printa(arguments):
    arguments = arguments.split(' -')
    arguments = arguments [1:]
    
    if arguments.len() == 0:
        dispall = raw_input('Moechten Sie alle Pokemon anzeigen lassen? Y/no')
        if dispall == 'no' or dispall == 'n':
            return
    
    list = pkdao.get_pk(arguments)
    
    for pk in list:
        print_pokemon(pk)
    

    
def close():
    pkdao.close()
        
        
    
    
    