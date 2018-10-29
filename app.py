from slackbot.bot import Bot
from slackbot.bot import default_reply
from slackbot.bot import listen_to
import os
import naro

import pya3rt

def main():
    bot = Bot()
    bot.run()

@listen_to("小説")
@listen_to("しょうせつ")
@listen_to("本")
@listen_to("ほん")
@listen_to("ライトノベル")
@listen_to("らいとのべる")
@listen_to("らのべ")
@listen_to("ラノベ")
def syosetu(message):
    text = message.body['text']
    message.reply(naro.books())

@default_reply
def my_default_handler(message):
    key = os.environ["A3RT_TOKEN"]
    client = pya3rt.TalkClient(key)
    rep = client.talk(message.body['text'])
    if rep['message'] == "ok":
        rep = rep['results'][0]['reply']
        message.reply(rep)
    else:
        message.reply("seyana")
        message.react("apare")

if __name__ == "__main__":
    print('start slackbot')
    main()