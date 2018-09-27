import argparse
import asyncio
from os import path as ospath

import database_server
import websockets


class Server:
    def __init__(self):
        _p = ospath.join(ospath.expanduser("~"), "Chat Server")
        database_server.create_database(_p, database_server.table_name, database_server.item_name, database_server.chat)
        self._database = database_server.DatabaseManager(_p)

    async def handle(self, websocket, path):
        message = await websocket.recv()
        print(message)

        with self._database as db:
            db.add_chat(path, message)

        await websocket.send("Received: {}".format(message))

    def start_server(self, _h: str, _p: int):
        server = websockets.serve(ws_handler=self.handle, host=_h, port=_p)

        asyncio.get_event_loop().run_until_complete(server)

        print("Server is Live.")

        asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Starts a chat server.")
    parser.add_argument("IP")
    parser.add_argument("Port")

    args = parser.parse_args()

    print(args)

    host = args.IP
    port = int(args.Port)

    print("A server will be started on {}:{}".format(host, port))

    ser = Server()

    ser.start_server(host, port)
