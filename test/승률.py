import matchId
import encryptId
import requests

def WinorLose(DEVELOPMENTAPIKEY,summonerName):
    encryptedId, encryptedPuuId = encryptId.encrypt(DEVELOPMENTAPIKEY,summonerName)
    gameId = matchId.getMatchId(DEVELOPMENTAPIKEY,summonerName)
    headers = {
        "Origin": "https://developer.riotgames.com",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": DEVELOPMENTAPIKEY,
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
        }
    win=0
    all=10
    for k in range(10):
        APIURL = "https://asia.api.riotgames.com/lol/match/v5/matches/" + str(gameId[k])
        res = requests.get(APIURL, headers=headers)
        data = res.json()
        for i in range(0,10):
            ith_info=data['info']['participants'][i]
            if encryptedPuuId == ith_info["puuid"]:
                participantId = i
        if(data['info']["teams"][0]["win"]=="Win"):
            if(participantId <=5):
                win+= 1
        else:
            if(participantId > 5):
                win+=1
    return win*100/all
DEVELOPMENTAPIKEY = "RGAPI-41a0cbed-7981-437d-b919-91965410d595"
summonerName = "동 캄"
print(WinorLose(DEVELOPMENTAPIKEY,summonerName))