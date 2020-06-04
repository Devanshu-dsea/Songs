import requests
import json
import webbrowser

#Header
print('Welcome to the Genius lyrics app. This app uses API hosted by the Genius Systems.You can search songs of your favorite artist here..')
print('The app is encrypted in Python by DSEA!!!!!\n\n\n')

while True:
    #Search
    inp=input('Enter your search here-:')
    #Process
    url="https://genius.p.rapidapi.com/search"
    querystring = {"q": inp}

    headers = {
        'x-rapidapi-host': "genius.p.rapidapi.com",
        'x-rapidapi-key': "299b6e1362msh82f721abaa64c3fp158cb4jsnc2b6a4dee3cb"
    }
    try:
        response=requests.get(url,headers=headers,params=querystring)
    except:
        print('Error encountered!!!!!  Make sure you are connected to internet or try again with any other search.')
        continue
    js=response.json()
    print('The following result were found-:')
    a=1
    for i in js['response']['hits']:
        print('{}. {} '.format(a,i['result']['full_title']))
        a=a+1
    a=input('Did you find your song? [Y/N]-:')
    if a=='N' or a=='n':
        print('Please try again. Maybe your song is not in our database:(')
        continue
    b=int(input('Enter the S.No of the song-:'))
    if js['response']['hits'][b-1]['result']['lyrics_state']=='complete':
        link=js['response']['hits'][b-1]['result']['url']
        print('Lyrics to your song are avalaible..')
        asd = input('Press any key to continue...')
        webbrowser.open_new_tab(link)
    else:
        print('Sorry lyrics of the songs are not avalaible ....:(')
