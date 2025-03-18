# https://www.twilio.com/en-us/blog/asynchronous-http-requests-in-python-with-aiohttp

# python3 -m pip install aiohttp
import aiohttp
import asyncio
import time

start_time = time.time()

# receives the "session" object and URL from main()
# stored as a "future" in the tasks list in main()
# gather runs the tasks in main()
async def get_pokemon(session, url):
	# use async "with" context manager to retrieve the URL
	async with session.get(url) as resp:
		# async "await" for the response
		pokemon = await resp.json()
		# return result to gather in main()
		return pokemon['name']

# runs the program
async def main():

	# use async "with" context manager to create a session
	# session can be passed to other functions as arguments
	async with aiohttp.ClientSession() as session:

		# tasks are async operations that will run concurrently
		# the "for" loop isn't async, so you don't need await
		tasks = []
		for number in range(1, 151):
			url = f'https://pokeapi.co/api/v2/pokemon/{number}'
			# append tasks that are "futures" objects, which "will" run an async function
			tasks.append(asyncio.ensure_future(get_pokemon(session, url)))

		# gather runs all of the tasks, as it iterates over the tasks list
		original_pokemon = await asyncio.gather(*tasks)
		for pokemon in original_pokemon:
			# synchronized tasks like print don't need the "await" keyword
			print(pokemon)

# async run the program
asyncio.run(main())
# takes about 1.25 seconds
print("--- %s seconds ---" % (time.time() - start_time))
