

import requests


#

# client_id = '0d290665f9fe4e9b8c65597ab9a7ac3b'
# client_secret = '25ead378e65a48acbc7a07b332a905f3'
# grant_type = 'client_credentials'
# body_params = {'grant_type' : grant_type}
# url='https://accounts.spotify.com/api/token'
# response=requests.post(url, data=body_params, auth = (client_id, client_secret))
#
# print(response.status_code)
#



client_id = '0d290665f9fe4e9b8c65597ab9a7ac3b'
client_secret = '25ead378e65a48acbc7a07b332a905f3'
redirect = 'http://localhost:8888/'
#util.prompt_for_user_token(username,scope,client_id='your-app-redirect-url',client_secret='your-app-redirect-url',redirect_uri='your-app-redirect-url')
import sys
import spotipy
import spotipy.util as util

#scope = 'user-library-read'
scope = 'user-top-read'
username = 'jmarter'

token = util.prompt_for_user_token(username, scope, client_id=client_id,client_secret=client_secret,redirect_uri=redirect)

if token:
    sp = spotipy.Spotify(auth=None)
    results = sp.current_user_saved_tracks(limit='5')
    # for line in results['items']:
    #     print(line['track']['artists'][0]['uri'])

    #print(results)
    #print(sp.current_user_saved_albums())
    for line in sp.current_user_top_artists():
        print(line)

    #
    # for item in results['items']:
    #     track = item['track']
    #     track_name = track['name']
    #     track_artist = track['artists'][0]['name']
    #     print('''
    #     Song: {}
    #
    #     Artist: {}
    #
    #     >>>>>>>>>>>>>>>>>>>>>>>>
    #     '''.format(track_name,track_artist))
    #



else:
    print ("Can't get token for", username)
