try:
    import gnureadline as readline
except ImportError:
    import readline
import logging

from rcon.completer import SimpleCompleter

LOG_FILENAME = "/tmp/completer.log"
logging.basicConfig(
    format="%(message)s",
    filename=LOG_FILENAME,
    level=logging.DEBUG,
)


def input_loop():
    line = ""
    while line != "stop":
        line = input('Prompt ("stop" to quit): ')
        print("Dispatch {}".format(line))


# 注册完成功能
OPTIONS = ["start", "stop", "list", "print"]
readline.set_completer(SimpleCompleter(OPTIONS).complete)

# 使用 Tab 键完成
readline.parse_and_bind("tab: complete")

# 提示用户输入文字
input_loop()
