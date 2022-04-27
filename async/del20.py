# %% [markdown]
# Koden under er en versjon som kjører synkront

# %%

def make_food(delay, what) :
    time.sleep(delay)
    print(what, ": ferdig")

def main():
    print("Startet: ", time.strftime('%X'))
    make_food(3, "Lage kaffe"),
    make_food(5, "Lage egg"),
    make_food(3, "Steike bacon"),
    make_food(5, "Varme bønner i tomatsaus"),
    make_food(3, "Riste brød"),
    make_food(1, "Sette på bordet")
    print("Ferdig: ", time.strftime('%X'))

main()

# %% [markdown]
# Og nå benytter vi oss av asyncio for å asynkront kjøre jobbene i parallell

# %%
import asyncio

async def make_food(delay, what) :
    await asyncio.sleep(delay)
    print(what, ": ferdig")

async def main():
    print("Startet: ", time.strftime('%X'))
    
    await asyncio.gather(
        make_food(3, "Lage kaffe"),
        make_food(5, "Lage egg"),
        make_food(3, "Steike bacon"),
        make_food(5, "Varme bønner i tomatsaus"),
        make_food(3, "Riste brød"),
        make_food(1, "Sette på bordet")
        )
    print("Ferdig: ", time.strftime('%X'))

# asyncio.run(main())

await main()

# %% [markdown]
# Skal man utveksle informasjon på tvers av jobber er det naturlig å gjøre dette via en kø. Under er et eksempel på producer/consumer applikasjon som samhandler via en slik kø. PS: Restauranten stenger når kokken har tømt ordre-boka.

# %%
import random

class Order : 
    def __init__(self, meal, how_long) :
        self.__meal = meal
        self.__how_long = how_long

    @property
    def meal(self) :
        return self.__meal

    @property
    def how_long(self):
        return self.__how_long

async def waiter(meal, how_long, queue) :
    while True :
        print("Legger matrett av typen", meal, "inn til bestilling")
        await queue.put(Order(meal, how_long))
        await asyncio.sleep(random.uniform(0,12))

async def chef(queue) :
    while not queue.empty() :
        order = await queue.get()
        print("Lager matrett av typen: ", order.meal, "ved å bruke", order.how_long, "sekunder. Køen er nå", queue.qsize(), "stor")
        await asyncio.sleep(order.how_long)
        queue.task_done()

    print("*** Kjøkkenet er stengt! ***")

async def main() :
    queue = asyncio.Queue(10)

    kelner1 = asyncio.create_task(waiter("Kjøttsuppe", 1, queue))
    kelner2 = asyncio.create_task(waiter("Biff", 2, queue))
    kelner3 = asyncio.create_task(waiter("Grøt", 3, queue))
    producers = [kelner1, kelner2, kelner3]

    consumer = asyncio.create_task(chef(queue))

    await asyncio.gather(consumer)
    await queue.join()

    for kelner in producers :
       kelner.cancel()

    print("=====")

await main()

    

# %% [markdown]
# Vi kan også se på et eksempel i en mer reel kontekst: Jobbing med I/O gjennom http. Under er et eksempel hentet fra realpython.com:

# %%
import asyncio
import time
import aiohttp


async def download_site(session, url):
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.create_task(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

sites = [
    "https://www.jython.org",
    "http://olympus.realpython.org/dice",
] * 80
start_time = time.time()
await download_all_sites(sites)
duration = time.time() - start_time
print(f"Downloaded {len(sites)} sites in {duration} seconds")


