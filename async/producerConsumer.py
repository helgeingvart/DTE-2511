import asyncio, random
import sys

if sys.platform:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
async def rich(q, total):
    """ The wayward rich , Throw money at random """
    while total > 0:
        money = random.randint(10,100)
        total -= money
        await q.put(money) # Random generation [10,100] Integer between 
        print(' Rich and easy to throw away %d Yuan '%money)
        await asyncio.sleep(3*random.random()) # stay 0-3 Random delay between seconds 

async def lucky(q, name):
    """ The lucky one who can find money at any time """
    while True:
        money = await q.get()
        q.task_done()
        print('%s Got it %d Yuan ！'%(name, money))

async def run():
    q = asyncio.Queue(1)
    producers = [asyncio.create_task(rich(q, 3000))]
    consumers = [asyncio.create_task(lucky(q, name)) for name in 'ABC']
    await asyncio.gather(*producers,)
    await q.join()
    for c in consumers:
        c.cancel()

if __name__ == '__main__':
    asyncio.run(run())
