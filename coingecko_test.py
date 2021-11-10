import requests
from pprint import pprint
import time



prev_ranking = None

z = 0

while True:
	res = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd")
	parsed_res = list(res.json())

	# TESTING
	if (z == 3):
		r1 = parsed_res[0]
		r2 = parsed_res[1]
		parsed_res[0] = r2
		parsed_res[1] = r1


	if not prev_ranking:
		prev_ranking = parsed_res
	else:
		for i in range(len(parsed_res)):
			curr_coin = parsed_res[i]
			prev_coin = prev_ranking[i]
			if (curr_coin['id'] != prev_coin['id']):
				print(f'Rank Changed!! Rank {i} used to be {prev_coin["id"]} but now it is {curr_coin["id"]}', flush=True)
		prev_ranking = parsed_res
	z += 1
	time.sleep(3)
