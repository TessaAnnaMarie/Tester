from discord.ext import commands
import discord
import asyncio
import MySQLdb
import _mysql_exceptions

data = open("settings.priv", "r")
info = data.readlines()

#WAS FIGURING OUT HOW TO ADD AND SELECT THE USER FROM THE DATABASE

def setup(bot):
    bot.add_cog(Experience(bot))


def memberForID(checkid, server):
    for member in server.members:
        if str(member.id) == str(checkid):
            return member
    return None

class Experience:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def givexp(self, ctx, member = None):
        """gives xp to a user"""
        #db = MySQLdb.connect(host=info[0], user=info[1], passwd=info[2], db="clients")
        #try:
        #    c = db.cursor()
        #    c.execute()
        #member = discord.utils.get(ctx.server.members, name=mentioned)
        await ctx.channel.send("user id: " + str(ctx.author.id) + "mentioned id:" + str(member.id))


'''
    @commands.command(pass_context=True)
    async def _FUNCNAME(self, ctx, user):
        """_FUNC_DEF_"""
        await ctx.channel.send(_OUTPUT)
'''