import discord
from discord.ext import commands
import google.generativeai as genai
from config import GENAI_KEY

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

async def gemini(ctx,* ,text):
    genai.configure(api_key=GENAI_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(text)
    candidates = response.candidates

    if not candidates:
        await ctx.send(f"{ctx.author.mention}, não foi possível gerar uma resposta.", delete_after=10)
        return

    message = candidates[0].content.parts[0].text


    if not text :
        await ctx.send(f"{ctx.author.mention}, você precisa digitar algo!", delete_after=5)
        return
    await ctx.send(f"{ctx.author.mention} Resposta de gemini:\n```{message}```")