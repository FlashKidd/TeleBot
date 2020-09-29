# Copyright (c) By Midhun KM [@flashkidd]
# I Am Noob
# Official Web : nekobot.xyz
# "Copy It As You Want But Don't Edit Credits"
import requests
from uniborg.util import admin_cmd, edit_or_reply, sudo_cmd


@borg.on(admin_cmd("ttt ?(.*)"))
@borg.on(sudo_cmd("ttt ?(.*)", allow_sudo=True))
async def noobishere(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        ipman = event.pattern_match.group(1)
    elif reply.text:
        ipman = reply.message
    else:
        await edit_or_reply(event, "Trump : What Should I Tweet For You ?")
        return

    url = f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={ipman}"
    flashgang = requests.get(url=url).json()
    meikobot = flashgang.get("message")
    tweetimg = meikobot
    flashkidd = f"Trump Has Tweeted {ipman}"
    await edit_or_reply(event, "Trump : Wait I Am Tweeting Your Texts")
    await event.client.send_file(
        event.chat_id, tweetimg, caption=flashkidd, reply_to=reply_to_id
    )


@borg.on(admin_cmd("tweet ?(.*)"))
@borg.on(sudo_cmd("tweet ?(.*)", allow_sudo=True))
async def noobishere(event):
    reply_to_id = event.message.id
    text = event.pattern_match.group(1)
    input_str = event.pattern_match.group(1)
    if text:
        if ":" in text:
            flash = input_str.split(":", 1)
        else:
            await event.reply(
                "You Are Using Invalid Syntax ! Make Sure To Use tweetusername:text Regex"
            )
            return
    if len(flash) != 2:
        await event.reply(
            "You Are Using Invalid Syntax ! Make Sure To Use tweetusername:text Regex"
        )
        return

    flashy = flash[0]
    ipman = flash[1]
    url = f"https://nekobot.xyz/api/imagegen?type=tweet&username={flashy}&text={ipman}"
    flashgang = requests.get(url=url).json()
    meikobot = flashgang.get("message")
    tweetimg = meikobot
    flashkidd = f"{flashy} Has Tweeted {ipman}"
    await edit_or_reply(event, f"{flashy} : Wait I Am Tweeting Your Texts")
    await event.client.send_file(
        event.chat_id, tweetimg, caption=flashkidd, reply_to=reply_to_id
    )
