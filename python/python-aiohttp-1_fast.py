# https://www.twilio.com/en-us/blog/asynchronous-http-requests-in-python-with-aiohttp

import aiohttp
import asyncio

# create async function
async def main():

	# create async "with" context manager
	# session handles web connections
	async with aiohttp.ClientSession() as session:

		pokemon_url = 'https://pokeapi.co/api/v2/pokemon/151'
		async with session.get(pokemon_url) as resp:
			pokemon = await resp.json()
			print(pokemon['name'])

asyncio.run(main())
