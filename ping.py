import asyncio

from datetime import datetime

from userbot.legend import BOT

from .. import ALIVE_NAME, CMD_HELP

from ..utils import admin_cmd, edit_or_reply, sudo_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "KING BOY"

@borg.on(admin_cmd(pattern=f"hbping$", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    start = datetime.now()

    animation_interval = 0.2

    animation_ttl = range(0, 26)

    await event.edit("ping....")

    animation_chars = [

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›",

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬›",

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬›",

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› ",

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› ",

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬›",

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›",

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›",

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬›",

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›",

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›",

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬›",

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›",

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â¬›",

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›",

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬›",

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›",

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬›",

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›",

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›",

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â€ŽðŸ“¶â¬›â¬›â¬›â€ŽðŸ“¶â¬›",

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â€ŽðŸ“¶â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬›â¬›",

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â€ŽðŸ“¶â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›",

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â€ŽðŸ“¶â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬›",

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â€ŽðŸ“¶â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›",

        "â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â¬› \nâ¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â¬›â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â€ŽðŸ“¶â¬›â€ŽðŸ“¶â¬›â¬›â¬›â€ŽðŸ“¶â¬› \nâ¬›â¬›â€ŽðŸ“¶â€ŽðŸ“¶â¬›â¬›â€ŽðŸ“¶â¬›â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ¬›â€ŽðŸ“¶â¬›â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â€ŽðŸ“¶â¬› \nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \n \n My ðŸ‡µ ðŸ‡® ðŸ‡³ ðŸ‡¬  Is : Calculating...",

    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 26])

    end = datetime.now()

    ms = (end - start).microseconds / 1000

    await event.edit(

        "â€Žâ€Žâ€Žâ€Žâ€Žâ€Žâ€Žâ€Žâ€Žâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›\nâ¬›ðŸ“¶ðŸ“¶ðŸ“¶ðŸ“¶ðŸ“¶ðŸ“¶ðŸ“¶â¬›\nâ¬›â¬›â¬›â¬›ðŸ“¶â¬›â¬›ðŸ“¶â¬›\nâ¬›â¬›â¬›â¬›ðŸ“¶â¬›â¬›ðŸ“¶â¬›\nâ¬›â¬›â¬›â¬›ðŸ“¶â¬›â¬›ðŸ“¶â¬›\nâ¬›â¬›â¬›â¬›â¬›ðŸ“¶ðŸ“¶â¬›â¬›\nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›\nâ¬›â¬›ðŸ“¶ðŸ“¶ðŸ“¶ðŸ“¶ðŸ“¶â¬›â¬›\nâ¬›ðŸ“¶â¬›â¬›â¬›â¬›â¬›ðŸ“¶â¬›\nâ¬›ðŸ“¶â¬›â¬›â¬›â¬›â¬›ðŸ“¶â¬›\nâ¬›ðŸ“¶â¬›â¬›â¬›â¬›â¬›ðŸ“¶â¬›\nâ¬›â¬›ðŸ“¶ðŸ“¶ðŸ“¶ðŸ“¶ðŸ“¶â¬›â¬›\nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›\nâ¬›ðŸ“¶ðŸ“¶ðŸ“¶ðŸ“¶ðŸ“¶ðŸ“¶ðŸ“¶â¬›\nâ¬›â¬›â¬›â¬›â¬›â¬›ðŸ“¶â¬›â¬›\nâ¬›â¬›â¬›â¬›â¬›ðŸ“¶â¬›â¬›â¬›\nâ¬›â¬›â¬›â¬›ðŸ“¶â¬›â¬›â¬›â¬›\nâ¬›ðŸ“¶ðŸ“¶ðŸ“¶ðŸ“¶ðŸ“¶ðŸ“¶ðŸ“¶â¬›\nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›\nâ¬›â¬›ðŸ“¶ðŸ“¶ðŸ“¶ðŸ“¶ðŸ“¶â¬›â¬›\nâ¬›ðŸ“¶â¬›â¬›â¬›â¬›â¬›ðŸ“¶â¬›\nâ¬›ðŸ“¶â¬›â¬›â¬›â¬›â¬›ðŸ“¶â¬›\nâ¬›ðŸ“¶â¬›ðŸ“¶â¬›â¬›â¬›ðŸ“¶â¬›\nâ¬›â¬›ðŸ“¶ðŸ“¶â¬›â¬›ðŸ“¶â¬›â¬›\nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›\nâ¬›ðŸ“¶â¬›ðŸ“¶ðŸ“¶ðŸ“¶ðŸ“¶ðŸ“¶â¬›\nâ¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬›â¬› \nâ€Žâ€Žâ€Žâ€Žâ€Žâ€Žâ€Žâ€Žâ€Ž \n \n My ðŸ‡µ ðŸ‡® ðŸ‡³ ðŸ‡¬  Is : {} ms".format(

            ms

        )

    )

@borg.on(admin_cmd(pattern="ping$"))

async def _(event):

    if event.fwd_from:

        return

    start = datetime.now()

    event = await edit_or_reply(event, "__**(â› á‘­ÏƒÉ³Ö âœ!__**")

    end = datetime.now()

    ms = (end - start).microseconds / 1000

    await event.edit(

        f"__**ê§ Pong! ê§‚__**\n\n   âš˜ {ms}\n   âš˜ __**My**__ __**Master**__ [{DEFAULTUSER}]\n\n\n MY NAME IS [{BOT}] THANKS MASTER TO DEPLOY ME ðŸ’ðŸ’ "

    )

CMD_HELP.update(

    {

        "ping": "__**PLUGIN NAME :** Ping__\

    \n\nðŸ“Œ** CMD â˜…** `.hping`\

    \n**USAGE   â˜…  **A kind ofping with extra animation\

    \n\nðŸ“Œ** CMD â˜…** `.ping`\

    \n**USAGE   â˜…  **Shows you the ping speed of server"

    }

)

