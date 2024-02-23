import logging

import click
import pyfiglet
import requests
from rich.console import Console
from rich.logging import RichHandler

from util.build import Build
from util.config import Config
from util.makeenv import MakeEnv
from util.obfuscate import DoObfuscate
from util.writeconfig import WriteConfig


def main():

    # logging.basicConfig(
    #     level="NOTSET",
    #     format="%(message)s",
    #     datefmt="[%X]",
    #     handlers=[RichHandler(rich_tracebacks=True,
    #                           tracebacks_suppress=[click])]
    # )

    # logging.getLogger("rich")

    # console = Console()

    # console.print(pyfiglet.figlet_format("YSL", font="big"),
    #               justify="center", highlight=False, style="cyan", overflow="ignore")


    config = Config()
    config_data = config.get_config()
    # print(config_data)
    # exit()

    make_env = MakeEnv()
    make_env.make_env()
    make_env.get_src()

    write_config = WriteConfig(config_data)
    write_config.write_config()

    do_obfuscate = DoObfuscate()
    do_obfuscate.run()

    build = Build()
    build.get_pyinstaller()
    build.get_upx()
    build.build()


if __name__ == "__main__":
    main()
