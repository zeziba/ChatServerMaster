import argparse
import asyncio
from os import path as ospath

try:
    from . import database_server
except ImportError:
    import database_server

import websockets


class Server:
    def __init__(self):
        _p = ospath.join(ospath.expanduser("~"), "Chat Server", "chat")
        _pi = ospath.join(ospath.expanduser("~"), "Chat Server", "ip")
        database_server.create_database(_p, database_server.table_name, database_server.item_name, database_server.chat)
        database_server.create_database(_pi, "IP_LOGS", "IP_ADDRS", "ORIGIN")
        self._database_chat_log = database_server.DatabaseManager(_p)
        self._database_ip = database_server.DatabaseManager(_pi)
        self._recently_connected = set()

    async def handle(self, websocket, path):
        self._recently_connected.add(websocket)

        try:
            message = await websocket.recv()

            with self._database_chat_log as db:
                db.add_chat(path, message)

            with self._database_ip as db:
                db.add_chat("{}:{}".format(websocket.host, websocket.port), websocket.origin)

            print("USER: {} @ {}, Message: {}".format(websocket.origin, "{}:{}".
                                                      format(websocket.host, websocket.port), message))
            for user in self._recently_connected:
                await user.send("Received: {}".format(message))
        finally:
            self._recently_connected.remove(websocket)

    def start_server(self, _h: str, _p: int):
        server = websockets.serve(ws_handler=self.handle, host=_h, port=_p)

        asyncio.get_event_loop().run_until_complete(server)

        print("Server is Live.")

        asyncio.get_event_loop().run_forever()


def main():
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


if __name__ == "__main__":
    main()
