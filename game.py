#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 18:28:41 2020

@author: ap
"""
from typing import NamedTuple
import random

Countries_data = []
#---------------------HYPER-PARAMETER-----------------------------------
population_upper = 10000
population_lower =5000
money_upper = 700
money_lower = 30
fest_social_realation = 0.2
no_of_countries = 10
#---------------------xxxxxxxxxxxxxxx-----------------------------------


#------------------------PARAMETER--------------------------------------
class Country(NamedTuple):
    population : int
    hygine_value : float
    money : int
    support : float
    festivity : float
    socialization : float
    info_accuracy  : float
    export_v : list
    import_v : list
    infected: int
    dead: int
    recovered : int
    
    population_arr : list
    money_arr : list
    infected_arr : list
    dead_arr : list
    recovered_arr : list

player_index = -1
data_accuracy_value = 0.25
#---------------------xxxxxxxxxxxxxxx-----------------------------------
def generate_country(no_of_countries):
    population = random.randint(population_lower, population_upper)
    hygine_value = random.randint(10, 30)/100
    money = random.randint(money_lower, money_upper)
    support = random.randint(60, 90)/100
    festivity = random.randint(20, 80)/100
    socialization = random.randint(30, 50)/100 + fest_social_realation*festivity
    info_accuracy = random.randint(30, 90)/100
    export_v = random.sample(range(100), no_of_countries)
    import_v = random.sample(range(100), no_of_countries)
    infected = 0
    dead = 0
    recovered = 0
    population_arr =[population]
    money_arr =[ money]
    infected_arr =[infected]
    dead_arr =[dead]
    recovered_arr =[recovered]
    country = Country(population,hygine_value,money,support,festivity,socialization,info_accuracy,export_v,import_v,infected,dead,recovered,population_arr,money_arr,infected_arr,dead_arr,recovered_arr)
    return country
def big_bang():

    for i in range(no_of_countries):
        country_temp = generate_country(no_of_countries)
        Countries_data.append(country_temp)
    
def choose_country():
    global Countries_data,player_index
    for i in range(no_of_countries):
        print("COUNTRY "+ str(i)+"\n")
        print(str(Countries_data[i])+"\n\n")
    player_index = input("Choose Your Prefered Country : ")
    
    