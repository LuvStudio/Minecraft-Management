import aiomcrcon
from datetime import datetime


class Rcon:
    def __init__(self, host, port, password) -> None:
        self.host = host
        self.port = port
        self.password = password

        self.client = aiomcrcon.Client(self.host, self.port, self.password)

    async def mainloop(self):

        try:
            await self.client.connect()

        except aiomcrcon.RCONConnectionError:
            print("An error occurred whilst connecting to the server...")
            return

        except aiomcrcon.IncorrectPasswordError:
            print("The provided password was incorrect...")
            return

        try:
            command = "list"
            response = await self.client.send_cmd(command)
            print(f'[{datetime.now().strftime("%H:%M:%S")}] {response[0]}')

            while True:
                command = input("> ").strip()
                response = await self.client.send_cmd(command)
                print(f'[{datetime.now().strftime("%H:%M:%S")}] {response[0]}')

        except KeyboardInterrupt:
            await self.client.close()
            print("\nExiting...")
            return

        except aiomcrcon.ClientNotConnectedError:
            print("The client was not connected to the server for some reason?")
            return
