from rcon.shell import Rcon
from rcon.completer import SimpleCompleter
from rcon import history_path

try:
    import gnureadline as readline
except ImportError:
    import readline
import asyncio
import logging

# TODO: load config from file or input
HOST = "192.168.0.30"
PORT = 25575
PASSWORD = "logitech"

LOG_FILENAME = "/tmp/completer.log"
logging.basicConfig(
    format="%(message)s",
    filename=LOG_FILENAME,
    level=logging.DEBUG,
)

# 注册补全功能
with open(history_path, "r") as f:
    OPTIONS = f.readlines()

readline.set_completer(SimpleCompleter(OPTIONS).complete)

# 使用 Tab 键补全
readline.parse_and_bind("tab: complete")
# 使用 vi 模式
readline.parse_and_bind("set editing-mode vi")

if __name__ == "__main__":

    connection = Rcon(host=HOST, port=PORT, password=PASSWORD)

    asyncio.run(connection.mainloop())
