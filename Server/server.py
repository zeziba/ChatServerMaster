import argparse
import asyncio

import database_server
import websockets


async def handle(websocket, path, database=database_server.DatabaseManager):
    message = await websocket.recv()
    print(message)

    with database as db:
        db.add_chat(path, message)

    await websocket.send("Received: {}".format(message))


def start_server(_h: str, _p: int):
    database = database_server.DatabaseManager()

    server = websockets.serve(handle, _h, _p, database)

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

    start_server(host, port)
