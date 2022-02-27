import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','whisky.settings')

import django
django.setup()
from pages.models import Distillery,Whisky

def populate():
    Ardbeg_whiskies = [
        {'id' : '1',
        'name':'Ar1',
        'age':'0',
        'abv':'0',
        'description':'The first-ever Ar bottling is a big beast, showing the power that southern Islay is known for. Ar1 makes a statement, and is laden with sweet spice and malty goodness'},
        {'id' : '2',
        'name':'Ar2',
        'age':'0',
        'abv':'0',
        'description':'Even bigger than Ar1, this is a peaty powerhouse loaded with flavour and character. The perfect marriage of ex-bourbon hogsheads with southern Islay spirit'}]

    Bowmore_whiskies = [
        {'id' : '3',
        'name':'Bw1',
        'age':'0',
        'abv':'0',
        'description':'The first-ever Bw bottling shows the maritime side of Islay malts, with whisky from the famed mid-1990s period'},
        {'id' : '4',
        'name':'Bw2',
        'age':'0',
        'abv':'0',
        'description':'Bw2 is a travel-retail only expression with malt whisky from a single 1990s vintage. Smoke takes a back seat here with Bowmores trademark tropical fruit taking centre stage'}]

    distilleries = {'Ardbeg':{'id':'1','whiskies':Ardbeg_whiskies,'location':'Port Ellen Isle of Islay Argyll PA42 7DU United Kingdom','description':'Opened in 1815, at one time Ardbeg was the largest distillery on Islay, supporting an entire community. Now, it is the second smallest, although due to its huge worldwide following, its community is bigger than ever'},
                    'Bowmore':{'id':'2','whiskies':Bowmore_whiskies,'location':'School St Bowmore (Islay) PA43 7JS United Kingdom','description':'The oldest distillery on Islay, and among the oldest in Scotland, Bowmore was founded in 1779, in the heart of the town of the same name, the islands capital. It is the second-biggest-selling whisky on Islay, producing a medium-peated malt with a character that has varied over the years'}}

    for distillery,distillery_data in distilleries.items():
        dist = add_distillery(distillery_data['id'],distillery,distillery_data['location'],distillery_data['description'])
        for whisky in distillery_data['whiskies']:
            add_whisky(whisky['id'],whisky['name'],whisky['age'],whisky['abv'],whisky['description'],dist)

    #debug
    for dist in Distillery.objects.all():
        for whisky in Whisky.objects.filter(distillery=dist):
            print(f'- {dist}: {whisky}')

def add_whisky(id,name,age,abv,description,dist):
    table_whisky = Whisky.objects.get_or_create(distillery = dist,id=id)[0]
    table_whisky.name=name
    table_whisky.age=age
    table_whisky.abv=abv
    table_whisky.description=description
    table_whisky.save()
    return table_whisky

def add_distillery(id,name,location,description):
    table_distillery = Distillery.objects.get_or_create(id=id)[0]
    table_distillery.name=name
    table_distillery.location=location
    table_distillery.description=description
    table_distillery.save()
    return table_distillery


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()