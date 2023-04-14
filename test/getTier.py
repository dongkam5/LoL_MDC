import encryptId
import requests

def getTier(DEVELOPMENTAPIKEY,summonerName):
    encryptedId,encryptedPuuId = encryptId.encrypt(DEVELOPMENTAPIKEY,summonerName)
    headers = {
        "Origin": "https://developer.riotgames.com",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": DEVELOPMENTAPIKEY,
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
        }
    APIURL = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" + encryptedId
    res = requests.get(APIURL, headers=headers)
    data = res.json()
    return data[0]["tier"]

DEVELOPMENTAPIKEY = "RGAPI-41a0cbed-7981-437d-b919-91965410d595"
summonerName = "동 캄"

print(getTier(DEVELOPMENTAPIKEY,summonerName))