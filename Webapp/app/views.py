from django.shortcuts import render
import joblib
# Create your views here.
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import re
import pandas as pd
import numpy as np
from django.shortcuts import render



# Create your views here.
def home(request) :
    name = 'tshirt'

    my_url = "https://www.flipkart.com/search?q=" + name + "&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    uClient = uReq ( my_url )
    page_html = uClient.read ( )
    uClient.close ( )
    page_soup = soup ( page_html, "html.parser" )

    containers = page_soup.find ( "div", {"class" : "_3O0U0u"} )

    items = containers.find_all ( class_='_2B_pmu' )
    prices = containers.find_all ( class_='_1vC4OE' )

    names = list ( )
    for i in items :
        names.append ( i.text )

    price = list ( )
    for i in prices :
        price.append ( i.text )

    list1 = list ( )
    links = containers.find_all ( class_='IIdQZO _1SSAGr' )
    for i in links :
        tint = i.find_all ( class_="_3dqZjq", href=True )
        for link in tint :
            list1.append ( link [ 'href' ] )

    name1 = "shoes"
    my_url1 = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=" + name1 + "&_sacat=0"
    uClient1 = uReq ( my_url1 )
    page_html1 = uClient1.read ( )
    uClient1.close ( )
    page_soup1 = soup ( page_html1, "html.parser" )

    containers1 = page_soup1.find_all ( "div", {"class" : "s-item__wrapper clearfix"} )

    temp = list ( )
    links = list ( )
    names1 = list ( )
    price1 = list ( )
    for i in range ( 0, 4 ) :
        container = containers1 [ i ]
        items = container.find ( "h3", {"class" : "s-item__title s-item__title--has-tags"} )
        names1.append ( items.text )
        prices1 = container.find ( "span", {"class" : "s-item__price"} )
        price1.append ( prices1.text )
        container_tint = container.find ( "div", {"class" : "s-item__info clearfix"} )
        tint = container_tint.find_all ( 'a', href=True )
        for link in tint :
            temp.append ( link [ 'href' ] )
        links.append ( temp [ 0 ] )
        temp = list ( )

    context = {'name1': names[0],'name2': names[1],'name3': names[2],'name4': names[3], 'price1': price[0],'link1':list1[0],
               'price2': price[1],'price3': price[2],'price4': price[3],'link2':list1[1],'link3':list1[2],'link4':list1[3],
               'name5': names1[0],'name6': names1[1],'name7': names1[2],'name8': names1[3],'price5': price1[0],
               'price6': price1[1],'price7': price1[2],'price8': price1[3],'link5':links[0],'link6':links[1],'link7':links[2],
               'link8':links[3]}


    return render(request,'webapp/home.html',context)