import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from ALEXMUSiC import LOGGER, app, userbot
from ALEXMUSiC.core.call import ALEX
from ALEXMUSiC.misc import sudo
from ALEXMUSiC.plugins import ALL_MODULES
from ALEXMUSiC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("ALEXMUSiC.plugins" + all_module)
    LOGGER("ALEXMUSiC.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await ALEX.start()
    try:
        await ALEX.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("ALEXMUSiC").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await ALEX.decorators()
    LOGGER("ALEXMUSiC").info(
        "𝘈𝘓𝘌𝘟 𝘉𝘖𝘛 𝘚𝘛𝘈𝘙𝘛\n  𝘈𝘓𝘌𝘟 𝘉𝘖𝘛 𝘚𝘛𝘈𝘛𝘌𝘋 𝘚𝘜𝘊𝘊𝘌𝘚𝘚𝘍𝘜𝘓𝘓𝘠\n𝘝𝘐𝘚𝘐𝘛 @𝘈𝘣𝘖𝘶𝘛𝘐𝘯𝘕𝘰𝘊𝘦𝘕𝘵"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("ALEXMUSiC").info("Stopping ALEX MUSiC Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
