import aiomcrcon
import asyncio
from time import sleep

host = "192.168.0.30"
port = 25575
password = "logitech"


async def main():

    client = aiomcrcon.Client(host, 25575, password)

    try:
        await client.connect()

    except aiomcrcon.RCONConnectionError:
        print("An error occurred whilst connecting to the server...")
        return

    except aiomcrcon.IncorrectPasswordError:
        print("The provided password was incorrect...")
        return

    try:
        while True:
            command = "weather clear"
            response = await client.send_cmd(command)
            print(response)

            command = "say set weather to clear every 2 minutes"
            response = await client.send_cmd(command)
            print(response)

            sleep(120)

    except KeyboardInterrupt:
        await client.close()
        print("Exiting...")
        return

    except aiomcrcon.ClientNotConnectedError:
        print("The client was not connected to the server for some reason?")
        return


if __name__ == "__main__":
    asyncio.run(main())
