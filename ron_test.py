from rivescript import RiveScript
import re
import pdb

bot = RiveScript(utf8=True)
bot.load_directory("./test_rive")
bot.sort_replies()
bot.unicode_punctuation = re.compile(r'[.,!?;:]')

print('!!!!!!!!!!!!!!!!준비끝!!!!!!!!!!!!!!!!')
while True:
    msg = input('You> ')
    # pdb.set_trace()
    if msg == '/quit':
        quit()

    reply = bot.reply("localuser", msg)
    print('Bot>', reply)
