"""
TeSt
  Syntax: .yo
by
  @TheFlashxD

"""
from telethon import events

import asyncio

import os

import sys

import random



@borg.on(events.NewMessage(pattern=r"\.yo", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    await event.edit(" let me Throw You A Punchline... 馃槈")

    await asyncio.sleep(2)

    x=(random.randrange(1,11))

    if x==1:

        await event.edit("`\"Yo mama is so ugly that she made the devil say amen.\"`")

    if x==2:

        await event.edit("`\"Yo mama is so dark she has a tatto done in chalk.\"`")

    if x==3:

        await event.edit("`\"Yo mama is so fat when she takes her clothes to the dry cleaners they say sorry we don't do curtains.\"`")

    if x==4:

        await event.edit("`\"Yo mama is so old every time she gets cuts she bleeds fossil fuel.\"`")

    if x==5:

        await event.edit("`\"YO MAMA IS SO SHORT, SHE BROKE HER LEG BY JUST JUMPING OF A TOILET!.\"`")

    if x==6:

        await event.edit("`\"Yo momma is so ugly even her reflection said I quit\"`")

    if x==7:

        await event.edit("`\"yo mamma is so fat she use a G.P.S. to find her belly button\"`")

    if x==8:

        await event.edit("`\"Yo mama so fat ,when she posted a nude pic of herself she broke the internet\"`")

    if x==9:

        await event.edit("`\"Yo mama is so ugly she gives the dead nightmares.\"`")

    if x==10:

        await event.edit("`\"Yo momma so ugly I took her to the zoo, guy at the door said "Thanks for bringing her back.\"`")

    if x==11:

        await event.edit("`\"Yo mama soooooo dark i clicked on her profile pic and thought my phone died!!!\"`")

    

