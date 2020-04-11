#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 19:54:47 2020

@author: ap
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 18:28:41 2020
@author: ap
"""
import matplotlib.pyplot as plt
import math
import random

Countries_data = []
Day = 0
#---------------------HYPER-PARAMETER-----------------------------------
population_upper = 10000
population_lower =5000
money_upper = 700
money_lower = 30
no_of_countries = 10

fest_social_relation = 0.2
money_product_relation = 2
population_product_relation = 750
infect_social_relation = 0.1
infect_hygine_relation = 0.2
lock_support_relation = 0.3
travel_imp_exp_val = 50000
remove_ratio_ub = 0.2
intial_infect_num = 100
no_of_infected_con = 2
#---------------------xxxxxxxxxxxxxxx-----------------------------------


#------------------------PARAMETER--------------------------------------
class Country(object):
    def __init__(self,population,hygine_value,money,support,festivity,socialization,info_accuracy,export_v,import_v,infected,dead,recovered,population_arr,money_arr,infected_arr,dead_arr,recovered_arr,productivity,infectivity,lock_down_ratio,dead_reco_ratio,is_country_removed):
        self.population = population
        self.hygine_value = hygine_value
        self.money = money
        self.support = support
        self.festivity = festivity
        self.socialization = socialization
        self.info_accuracy  = info_accuracy
        self.export_v = export_v
        self.import_v = import_v
        self.infected = infected
        self.dead = dead
        self.recovered = recovered
            
        self.population_arr = population_arr
        self.money_arr = money_arr
        self.infected_arr = infected_arr
        self.dead_arr = dead_arr
        self.recovered_arr = recovered_arr
        self.productivity = productivity
        self.infectivity = infectivity
        self.lock_down_ratio = lock_down_ratio
        self.dead_reco_ratio = dead_reco_ratio
        self.is_country_removed = is_country_removed
        
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
    dead_reco_ratio = random.randint(20, 40)/100
    is_country_removed = 0
    country = Country(population,hygine_value,money,support,festivity,socialization,info_accuracy,export_v,import_v,infected,dead,recovered,population_arr,money_arr,infected_arr,dead_arr,recovered_arr,productivity,infectivity,lock_down_ratio,dead_reco_ratio,is_country_removed)
    return country

def inital_infect():
    for i in range(no_of_infected_con):  
        
        index = random.randint(0, no_of_countries-1)
        print(index)
        Countries_data[index].infected = intial_infect_num
        Countries_data[index].population = Countries_data[index].population - intial_infect_num
    
    
def big_bang():
    global  Day
    Day = 0
    global Countries_data
    Countries_data = []
    for i in range(no_of_countries):
        country_temp = generate_country(no_of_countries)
        Countries_data.append(country_temp)
    
def choose_country():
    global Countries_data,player_index
    for i in range(no_of_countries):
        print("COUNTRY "+ str(i)+"\n")
        print(str(Countries_data[i])+"\n\n")
    player_index = int(input("Choose Your Prefered Country : "))
    inital_infect()
    
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
    global Countries_data
    for i in range(no_of_countries):
        if (i == index):
            continue;
        export_i = c1.export_v[i]
        c2 =  Countries_data[i]
        import_i = c2.import_v[index]
        c1.population = math.ceil(c1.population - c1.population*export_i*import_i/travel_imp_exp_val)
        c2.population = math.ceil(c2.population + c1.population*export_i*import_i/travel_imp_exp_val)
        c1.infected = math.ceil(c1.infected - c1.infected*export_i*import_i/travel_imp_exp_val)
        c2.infected = math.ceil(c2.infected + c1.infected*export_i*import_i/travel_imp_exp_val)        
def remove(c):
    if(Day>3):
        temp = c.infected * random.randint(0,remove_ratio_ub*100)/100
        c.infected = math.ceil(c.infected - temp)
        ratio = c.dead_reco_ratio*(random.randint(-10,10)/100+1)
        c.dead = math.ceil(c.dead + temp*ratio)
        c.recovered = math.ceil(c.recovered + temp*(1-ratio))
        
def infect_others(c):
    c.infected =  math.ceil(c.infected + c.infectivity*c.infected)
    c.population = math.ceil(c.population - c.infectivity*c.infected)
    
def change_param(c,index):
    c.socialization = min(1,c.socialization + fest_social_relation*c.festivity)
    c.infectivity = max(0,min(1,c.infectivity + infect_social_relation*c.socialization - infect_hygine_relation*c.hygine_value))
    c.money =  c.money + c.productivity*money_product_relation*c.population/population_product_relation 
    travel_effect(c,index)
    infect_others(c)
    remove(c)


def country_update():
    global Countries_data,player_index
    for i in range(no_of_countries):
        c = Countries_data[i]
        if(c.is_country_removed == 1):
            continue
        change_param(c,i)
        c.population = max(0,c.population)
        if(c.population == 0):
            c.is_country_removed = 1
        c.population_arr.append(c.population)
        c.infected_arr.append(c.infected)
        c.dead_arr.append(c.dead)
        c.recovered_arr.append(c.recovered)
        c.money_arr.append(c.money)
    
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
       
def change_param_user():
    #the user makes his choices to change parameters of his country 
    print('5')
    
def days():
    #view_data()
    change_param_user()
    country_update()
    check_pop()

def check_pop():
    p =0
    for i in range(no_of_countries):
        p = p + Countries_data[i].population + Countries_data[i].infected + Countries_data[i].dead + Countries_data[i].recovered
    print(str(Day)+ " : "+str(p))
    
big_bang()  
choose_country()  
for i in range(20):
    Day = Day + 1
    days()

# handel stop condition.
# make sure infection never overflows
c = Countries_data[0]