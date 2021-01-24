from riotwatcher import LolWatcher, ApiError


import os
import pandas as pd

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


class statistics:

    def __init__(self):
        with open('api_key.txt', 'r') as file:
            api_key = file.read()
        self.watcher = LolWatcher(api_key)
        self.my_region = 'euw1'

    def getSummonerStats(self,usrname, region):
        self.me = self.watcher.summoner.by_name(region, usrname)
        print('Me: ',self.me)
        self.my_ranked_stats = self.watcher.league.by_summoner(region, self.me['id'])
        print(self.my_ranked_stats)

    def wr(self):
        #1 = SoloQ 0 = Flex
        mrs = self.my_ranked_stats[0]
        games_insgesamt = int(mrs['wins']) + int(mrs['losses'])
        winrate = (int(mrs['wins']) / games_insgesamt) * 100 #Anzahl der Siege durch die gesamten Spiele
        print('Spiele insgesamt ' + str(games_insgesamt) + ' in ' + mrs['queueType'])
        print('Winrate: ' + str(winrate))


    def test(self, region):
        all_matchlist = self.watcher.match.matchlist_by_account(region, self.me['accountId'])
        matchlist = all_matchlist['matches']
        totalgames = all_matchlist['totalGames']
        print(totalgames)
        print(len(matchlist))
        print(type(matchlist))



def Main():
    stats = statistics()
    stats.getSummonerStats(str(input('Enter your Summonername: ')), 'euw1')
    stats.test('euw1')
    #stats.wr()

Main()


