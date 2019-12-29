import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print("< {}".format(name))

    greeting = "Hello {}!".format(name)
    await websocket.send(greeting)
    print("> {}".format(greeting))

start_server = websockets.serve(hello, 'localhost' , 12345)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
