import discord
from discord.ext import commands
#import os


from help_cog import help_cog
from music_cog import music_cog


intents = discord.Intents.default()
bot = commands.Bot(command_prefix='/', intents=intents)

bot.remove_command("help")

bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))

bot.run('MTA1MjQ1NTA0NzU3NDg1OTc3Ng.G43pGr.xmhYH1qZpo4QsQLsmO3zE5VgtcGZ82ekEi66P4')