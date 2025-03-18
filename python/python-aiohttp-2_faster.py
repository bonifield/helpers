# https://www.twilio.com/en-us/blog/asynchronous-http-requests-in-python-with-aiohttp

import aiohttp
import asyncio
import time

start_time = time.time()

async def main():

	# create web client session
	async with aiohttp.ClientSession() as session:

		for number in range(1, 151):
			pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
			# makes next request while waiting for previous results
			async with session.get(pokemon_url) as resp:
				pokemon = await resp.json()
				print(pokemon['name'])

asyncio.run(main())
# takes about 8 seconds
print("--- %s seconds ---" % (time.time() - start_time))
