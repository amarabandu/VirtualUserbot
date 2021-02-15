"""Emoji

Available Commands:

.wtf"""


import asyncio

from virtualuserbot import CMD_HELP
from virtualuserbot.utils import friday_on_cmd


@friday.on(friday_on_cmd("wtf"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    await event.edit("wtf")
    animation_chars = [
        "What",
        "What The",
        "What The Fuck",
        "What The Fuck Man",
        "[What The Fuck Man](https://telegra.ph/file/68d79cf544086e6eff1ec.jpg)",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 5])


CMD_HELP.update(
    {
        "wtf": "**wtf**\
\n\n**Syntax : **`.wtf`\
\n**Usage :** Creates wtf expression with text."
    }
)
