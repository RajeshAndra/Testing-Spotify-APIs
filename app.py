from dotenv import load_dotenv
import os
import base64
from requests import get, post
import json
load_dotenv()

client_id=os.getenv("Client_ID")
client_secret=os.getenv("Client_secret")


def get_token():
    aut_string=client_id +":"+client_secret
    aut_bytes=aut_string.encode("utf-8")
    aut_64=str(base64.b64encode(aut_bytes),"utf-8")

    url="https://accounts.spotify.com/api/token"
    headers={
        "Authorization":"Basic "+aut_64,
        "Content-type":"application/x-www-form-urlencoded"
    }
    data={"grant_type":"client_credentials"}
    result=post(url,headers=headers,data=data)
    json_result=json.loads(result.content)
    token=json_result["access_token"]
    return token

def get_header(token):
    return {"Authorization":"Bearer "+token}

def get_artist_id(token,artist):
    url=f"https://api.spotify.com/v1/search?q={artist}&type=artist&limit=1"
    result=get(url,headers=get_header(token))
    json_result=json.loads(result.content)
    response=json_result['artists']['items'][0]
    return response['id']

def get_song(token,id):
    url=f"https://api.spotify.com/v1/artists/{id}/top-tracks?country=US"
    result=get(url,headers=get_header(token))
    json_result=json.loads(result.content)['tracks']
    for id,song in enumerate(json_result):
        print(f"{id+1}. {song['name']}")
    
def get_albums(token):
    url="https://api.spotify.com/v1/albums/5EbpxRwbbpCJUepbqVTZ1U/tracks?limit=50&market=US"
    result=get(url,headers=get_header(token))
    json_result=json.loads(result.content)['items']
    for id,song in enumerate(json_result):
        print(f"{id+1}. {song['name']}")



token=get_token()
#get_song(token,get_artist_id(token,"weeknd"))
get_albums(token)
