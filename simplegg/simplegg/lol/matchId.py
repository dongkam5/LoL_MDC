from . import encryptId
import requests

def getMatchId(DEVELOPMENTAPIKEY,summonerName):
    encryptedId, encryptedPuuId = encryptId.encrypt(DEVELOPMENTAPIKEY,summonerName)
    headers = {
        "Origin": "https://developer.riotgames.com",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": DEVELOPMENTAPIKEY,
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
        }
    APIURL = "https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/" + encryptedPuuId + "/ids?start=0&count=20"
    res = requests.get(APIURL, headers=headers)
    data = res.json()
    return data

DEVELOPMENTAPIKEY = "RGAPI-6fe38e26-cb38-49c6-a0d6-29162b47d388"
summonerName = "동 캄"

print(getMatchId(DEVELOPMENTAPIKEY,summonerName))