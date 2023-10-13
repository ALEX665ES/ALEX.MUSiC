from ALEXMUSiC.core.bot import ALEX
from ALEXMUSiC.core.dir import dirr
from ALEXMUSiC.core.git import git
from ALEXMUSiC.core.userbot import Userbot
from ALEXMUSiC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = ALEX()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
