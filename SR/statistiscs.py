from riotwatcher import LolWatcher, ApiError
import pandas as pd
class statistics:

    def __init__(self, me, watcher, my_region, my_ranked_stats):
        self.me = me
        self.watcher = watcher
        self.my_region = my_region
        self.my_ranked_stats = my_ranked_stats

    def connectAPI(self):
        # golbal variables
        api_key = ' '
        self.watcher = LolWatcher(api_key)
        self.my_region = 'euw1'

    def getSummonerStats(self,usrname):
        self.me = self.watcher.summoner.by_name(self.my_region, usrname)
        self.my_ranked_stats = self.watcher.league.by_summoner(self.my_region, self.me['id'])
        print(self.my_ranked_stats)

    def wr(self):
        #0 = SoloQ 1 = Flex
        mrs = self.my_ranked_stats[0]
        print(mrs['queueType'])
        soloQ_insgesamt = int(mrs['wins']) + int(mrs['losses'])
        print('Spiele insgesamt ' + str(soloQ_insgesamt))
        winrate = (int(mrs['wins']) / soloQ_insgesamt) * 100 #Anzahl der Siege durch die gesamten Spiele

        print(winrate)
    def test(self):
        all_matchlist = self.watcher.match.matchlist_by_account(self.my_region, self.me['accountId'])
        print(all_matchlist)
        print(type(all_matchlist))
        matchlist = all_matchlist['matches']


def Main():
    stats = statistics(None, None, None, None)
    stats.connectAPI()
    stats.getSummonerStats(str(input('Enter your Summonername: ')))
    stats.test()
    #stats.wr()

Main()
