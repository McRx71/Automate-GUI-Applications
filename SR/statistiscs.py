from riotwatcher import LolWatcher, ApiError
import pandas as pd

# golbal variables
api_key = ''
watcher = LolWatcher(api_key)
my_region = 'euw1'

me = watcher.summoner.by_name(my_region, '')

my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])