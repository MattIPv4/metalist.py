[![PyPI](https://img.shields.io/pypi/v/metalist.py.svg)](https://pypi.org/project/metalist.py/)

# metalist.py
**A simple API wrapper to post Discord bot stats to all known bot lists using metalist.xyz data.**

## Installation

Install via pip (recommended)

    pip install metalist.py

## Features

* POST server count
* AUTOMATIC server count updating
* ALL bot lists' APIs included

## Example Discord.py Rewrite cog


```Python
    import metalist


    class Stats:
        def __init__(self, bot):
            self.bot = bot
            self.metalist = metalist.Client(self.bot)  # Create a Client instance
            self.metalist.start_loop()  # Posts the server count every 30 minutes
            self.metalist.set_auth("botsfordiscord.com", "cfd28b742fd7ddfab1a211934c88f3d483431e639f6564193") # Set authorisation token for a bot list

    def setup(bot):
        bot.add_cog(Stats(bot))
```

## Discussion, Support and Issues
For general support and discussion of this project, please join the Discord server: https://discord.gg/qyXqA7y \
[![Discord Server](https://discordapp.com/api/guilds/204663881799303168/widget.png?style=banner2)](https://discord.gg/qyXqA7y)

To check known bugs and see planned changes and features for this project, please see the GitHub issues.\
Found a bug we don't already have an iss