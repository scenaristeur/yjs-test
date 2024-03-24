import asyncio
import y_py as Y
from websockets import connect
from ypy_websocket import WebsocketProvider

async def client():
    ydoc = Y.YDoc()
    async with (
        connect("ws://localhost:1234/my-roomname") as websocket,
        WebsocketProvider(ydoc, websocket),
    ):

        def callback(event):
            print(yarray)

        yarray = ydoc.get_array("my-array")
        yarray.observe(callback)

        with ydoc.begin_transaction() as txn:
                    yarray.append(txn, "hello de python")

        await asyncio.Future()  # run forever

asyncio.run(client())