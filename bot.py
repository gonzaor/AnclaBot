#Importo librerias
import asyncio
import os

import discord
from discord import member
from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv
from discord.utils import get
import urllib.request
import json
import praw
import random

#Le digo al bot que sintaxis usar.

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot: Bot = commands.Bot(command_prefix= '!')


#Funcionalidades.

#Esto tira una frase random

@bot.command(name='fraseancla')
async def fraseancla(ctx):
    frasesprueba = [frase1, frase2, frase3, frase4, frase5, frase6, frase7, frase8, frase9, frase10, frase11, frase12, frase13, frase14, frase15, frase16, frase17, frase18]
    oratorio = random.choice(frasesprueba)
    await ctx.send(oratorio)

#Esto para mutear un usuario (Sobretodo a JS, chupala gil)

@bot.command(name='mutear')
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("A quien queres mutear?")
        return
    role = discord.utils.get(ctx.guild.roles, name="muteado")
    await member.add_roles(role)
    await ctx.send("Listo.")

#Esto agrega al usuario al rol "conga" para arrobarlos en caso de querer jugar.

@bot.command(name='conga')
async def conga(ctx):
    role = discord.utils.get(ctx.guild.roles, name="conga")
    await member.add_roles(role)
    await ctx.send("Listo ahora formas parte de la secta conguera.")





#de cuando empece xd

@bot.command(name='sumar')
async def sumar(ctx, num1,num2):
    response = int(num1)+int(num2)
    await ctx.send(response)

@bot.command(name='mundo')
async def mundo(ctx):
    await ctx.send("Hola mundo!")



#Frases caracterisiticas de miembros.

@bot.command(name='republicana')
async def republicana(ctx):
    frasesprueba = ['Tenes futuro en la republicana buri.', 'Dedicate a jugar al magic o otra cosa. putito']
    oratorio = random.choice(frasesprueba)
    print(oratorio)
    await ctx.send(oratorio)

@bot.command(name='js')
async def js(ctx):
    await ctx.send("Que tipo virgo")


@bot.command(name='narnia')
async def narnia(ctx):
    await ctx.send(
        "La monarquía es una forma de Estado en la cual un grupo integrado en el Estado, generalmente una familia que representa una dinastía, encarna la identidad nacional del país y su cabeza, el monarca, ejerce el papel de jefe de Estado.")


@bot.command(name='alo')
async def alo(ctx):
    await ctx.send("Que chetito de mierda")


@bot.command(name='lasrou')
async def lasrou(ctx):
    await ctx.send("Manya putoo")


@bot.command(name='Juani')
async def Juani(ctx):
    await ctx.send("La luz entra tanta oscuridad")


@bot.command(name='moy')
async def moy(ctx):
    await ctx.send("tipazo, lastima juega al lol.")


@bot.command(name='mani')
async def mani(ctx):
    await ctx.send("Que pija esto que pija lo otro, dios hermano deja de quejarte.")


@bot.command(name='sb')
async def sb(ctx):
    await ctx.send("Tipazo.")


@bot.command(name='foo')
async def foo(ctx):
    await ctx.send("Milico, que traumo a un tal eze. Haciendolo que caiga bajo")


@bot.command(name='samus')
async def samus(ctx):
    await ctx.send("deben de obedecer.")


@bot.command(name='bemont')
async def bemont(ctx):
    await ctx.send("Que tipo fachero, debe de activar mas...")


@bot.command(name='tina')
async def tina(ctx):
    await ctx.send("Jugadora de lol... nada mas que decir")


@bot.command(name='falling')
async def falling(ctx):
    await ctx.send("comprate un net decente haceme el favor...")


@bot.command(name='patas')
async def patas(ctx):
    await ctx.send("Pa los gustos los colores...")


@bot.command(name='specific')
async def specific(ctx):
    await ctx.send("El chico que tiene tatuada violencia en la espalda")


@bot.command(name='calamarino')
async def calamarino(ctx):
    await ctx.send("Montevideano que vive en pocitos, que mas decir...")


@bot.command(name='antel')
async def antel(ctx):
    await ctx.send("QUE SERVICIO DE MIERDA POBRE FALLING NI CARGAR LOS GIFS DE DISCORD PUEDE")


@bot.command(name='anclas')
async def anclas(ctx):
    await ctx.send("Me rindo, le pongo la mejor pero son un ancla al cuello.")


#Variables para hacer las frases.

frase1 = 'Me rindo, le pongo la mejor pero son un ancla al cuello'
frase2 = 'narnia ve el futuro'
frase3 = 'ahi lo banee como pidio tan amablemente'
frase4 = 'esto es una monarquia chief'
frase5 = 'emp1jada'
frase6 = 'No se como no embarace a mis primas'
frase7 = 'ta cantado que vamos a chupar p1jas'
frase8 = 'Pimikizzz - que sabes tu gordo'
frase9 = 'Negro garrafero'
frase10 = 'Vamo peñarol carajo '
frase11 = 'vayan a dormir downs'
frase12 = 'las tetas son de jugar lol'
frase13 = 'Si tan solo tuviera novia'
frase14 = 'empijada'
frase15 = 'te van a tocar los negros rompeculos del comcar'
frase16 = 'al tipo ese le dan un revolver para matar a todos los negros y dudo que lo haga'
frase17 = 'servis para milico'
frase18 = 'si tan solo tuviera novia...'



bot.run(TOKEN)

