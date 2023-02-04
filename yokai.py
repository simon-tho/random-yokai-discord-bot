import json
import random
import nextcord
from nextcord import Interaction
from nextcord.ext import commands

class Yokai(commands.Cog):
    def __init__(self, bot):
       super().__init__


    @nextcord.slash_command(name="random_yokai", description="returns 6 random Yo-kai", guild_ids=[895391092353138698, 1071437114270552126])
    async def ry_six(self, interaction: nextcord.Interaction):
        with open("playable-yokai.json", encoding="UTF-8") as f:
            data = json.load(f)
            name = str
            await interaction.channel.send("Your randomly generated team consists of the following yokai:")
            for i in range(6):
                yokai = random.choice(data)
                name = yokai["Deutsch"]
                id = yokai["Nummer"]
                rank = yokai["Rang"]
                tribe = yokai["Stamm"]
                element = yokai["Element"]
                fav = yokai["favoriteFood"]
                await interaction.channel.send(f"{i} \n **{name}** \n Rang: {rank} \n ID: {id} \n tribe: {tribe} \n Element: {element} \n Favorite Food: {fav}")


    @nextcord.slash_command(name="ry_plus_healer", description="returns 6 random Yo-kai including atleast one healer", guild_ids=[895391092353138698, 1071437114270552126])
    async def ry_six_heal(self, interaction: nextcord.Interaction):
        with open("playable-yokai.json", encoding="UTF-8") as f:
            data = json.load(f)
            name = str
            element_list = list()
            temp = False
            await interaction.channel.send("Your randomly generated team consists of the following yokai:")
            for i in range(5):
                yokai = random.choice(data)
                name = yokai["Deutsch"]
                id = yokai["Nummer"]
                rank = yokai["Rang"]
                tribe = yokai["Stamm"]
                element = yokai["Element"]
                element_list.append(element)
                fav = yokai["favoriteFood"]
                await interaction.channel.send(f"{i} \n **{name}** \n Rang: {rank} \n ID: {id} \n tribe: {tribe} \n Element: {element} \n Favorite Food: {fav}")   
            for i in element_list:
                if "Heilung" in element_list:
                    temp = True
                    break
            if(temp == False):
                while True:
                    yokai = random.choice(data)
                    if(yokai["Element"] == "Heilung"):
                        break
            else:
                yokai = random.choice(data)
            name = yokai["Deutsch"]
            id = yokai["Nummer"]
            rank = yokai["Rang"]
            tribe = yokai["Stamm"]
            element = yokai["Element"]
            element_list.append(element)
            fav = yokai["favoriteFood"]
            await interaction.channel.send(f"5 \n **{name}** \n Rang: {rank} \n ID: {id} \n tribe: {tribe} \n Element: {element} \n Favorite Food: {fav}") 


def setup(bot):
    bot.add_cog(Yokai(bot))