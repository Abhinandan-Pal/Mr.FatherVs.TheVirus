#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 18:28:41 2020

@author: ap
"""
import matplotlib.pyplot as plt
from typing import NamedTuple
import random

Countries_data = []
#---------------------HYPER-PARAMETER-----------------------------------
population_upper = 10000
population_lower =5000
money_upper = 700
money_lower = 30
no_of_countries = 10

fest_social_relation = 0.2
money_product_relation = 2
population_product_relation = 75000
infect_social_relation = 0.1
infect_hygine_relation = 0.2
lock_support_relation = 0.3
travel_imp_exp_val = 500000
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
    infected : int
    dead : int
    recovered : int
    
    population_arr : list
    money_arr : list
    infected_arr : list
    dead_arr : list
    recovered_arr : list
    productivity : float
    infectivity : float
    lock_down_ratio : float
    
player_index = -1
data_accuracy_value = 0.25
#---------------------xxxxxxxxxxxxxxx-----------------------------------
#------------------------GAME STATE-------------------------------------
#---------------------xxxxxxxxxxxxxxx-----------------------------------
def generate_country(no_of_countries):
    population = random.randint(population_lower, population_upper)
    hygine_value = random.randint(10, 30)/100
    money = random.randint(money_lower, money_upper)
    support = random.randint(60, 90)/100
    festivity = random.randint(10, 50)/100
    socialization = random.randint(30, 50)/100 + fest_social_relation*festivity
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
    productivity = random.randint(10, 50)/100
    infectivity = random.randint(0, 10)/100 + infect_social_relation*socialization - infect_hygine_relation*hygine_value
    lock_down_ratio =random.randint(50, 70)/100+ lock_support_relation*support
    country = Country(population,hygine_value,money,support,festivity,socialization,info_accuracy,export_v,import_v,infected,dead,recovered,population_arr,money_arr,infected_arr,dead_arr,recovered_arr,productivity,infectivity,lock_down_ratio)
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
    player_index = int(input("Choose Your Prefered Country : "))
    
def plot(x,label_y,is_mine,title):
    if(not is_mine):
        for i in range(len(x)):
            x[i] = x[i]*(random.randint(-int(data_accuracy_value*100),int(data_accuracy_value*100))/100+1)
            
    plt.figure(figsize=(len(x), 5))
    plt.plot(x)
    plt.xlabel("Days")
    plt.ylabel(label_y)
    plt.title(title)
    plt.show()

def travel_effect(c1,index):
    for i in range(no_of_countries):
        if (i == index):
            continue;
        export_i = c1.export_v[i]
        c2 = Countries_data[i]
        import_i = c2.import_v[index]
        c1.population = c1.population - c1.population*export_i*import_i/travel_imp_exp_val
        c2.population = c2.population + c1.population*export_i*import_i/travel_imp_exp_val
        c1.infected = c1.infected - c1.infected*export_i*import_i/travel_imp_exp_val
        c2.infected = c2.infected + c1.infected*export_i*import_i/travel_imp_exp_val

def change_param(c,index):
    c.socialization = c.socialization + fest_social_relation*c.festivity
    c.infectivity = c.infectivity + infect_social_relation*c.socialization - infect_hygine_relation*c.hygine_value
    c.money =  c.money + c.productivity*money_product_relation*c.population/population_product_relation 
    travel_effect(c,index)


def country_update():
    print('5')
    
def data_country_view(country,is_mine,name):
    factor = 1
    if(not is_mine):
        factor = (random.randint(-int(data_accuracy_value*100),int(data_accuracy_value*100))/100+1)
    print("population : ",str(country.population*factor)+"\n")
    print("hygine_value : ",str(country.hygine_value*factor)+"\n")
    print("money : ",str(country.money*factor)+"\n")
    print("Public Support Index : ",str(country.support*factor)+"\n")
    print("Socialization Index : ",str(country.socialization*factor)+"\n")
    print("Infected by diesease : ",str(country.infected*factor)+"\n")
    print("Death by diesease : ",str(country.dead*factor)+"\n")
    print("Recovered from diesease : ",str(country.recovered*factor)+"\n")
    plot(country.population_arr,"Population",is_mine,name)
    plot(country.money_arr,"Money",is_mine,name)
    plot(country.infected_arr,"Infected",is_mine,name)
    plot(country.dead_arr,"Dead",is_mine,name)
    plot(country.recovered_arr,"Recovered",is_mine,name)
    
def view_data():
    a = 0
    while(a != -1):
       print("Your Country number is " + str(player_index)+"\n")
       print("To EXIT WRITE -1")
       a = int(input("Enter Country number you want data of : "))
       b = (a == int(player_index))
       data_country_view(Countries_data[a],b,str("COUNTRY "+str(a)))
    
def days():
    view_data()
    change_param()
    for i in range(no_of_countries):
        country_update(Countries_data[i])
        
    
        
    