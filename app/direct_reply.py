import os
import random

from app import wtf_reasons
from app.emoji_list import CRY_EMOJI_LIST


def pier_girl():
    random.seed(os.urandom(5))
    return random.choice(
        [
            'https://www.youtube.com/watch?v=BoD4yCTXTCU',
            'https://www.youtube.com/watch?v=M-MT0z6ac7g'
        ]
    )


def girlfriend():
    return [('image', 'https://i.imgur.com/g6WRWrk.jpg')]


def daughter_red():
    replies = [('image', 'https://i.imgur.com/vKGB3XM.jpg'), ('text', '杜家庄女兒紅 七日釀造 七星獎 口碑88分')]
    return replies


def bot_help():
    return '說明網頁 https://oripyon.weebly.com\n原始碼 https://github.com/leafwind/line_bot'


def poor_chinese():
    return '我覺的台灣人的中文水準以經爛ㄉ很嚴重 大家重來都不重視 因該要在加強 才能越來越利害'


def qq():
    random.seed(os.urandom(5))
    return f'幫QQ喔 {random.choice(CRY_EMOJI_LIST)}'


def mahoshoujo():
    return '／人◕ ‿‿ ◕人＼ 僕と契約して、魔法少女になってよ！'


def why():
    random.seed(os.urandom(5))
    return f'因為{random.choice(wtf_reasons.reasons)}。'


def tzguguaning():
    return '恭迎慈孤觀音⎝༼ ◕д ◕ ༽⎠\n渡世靈顯四方⎝༼ ◕д ◕ ༽⎠'


def gurulingpo():
    s = '''
*``･*+。
 ｜   `*｡
 ｜     *｡
 ｡∩∧ ∧   *
+   (･∀･ )*｡+ﾟ咕嚕靈波
`*｡ ヽ  つ*ﾟ*
 `･+｡*･`ﾟ⊃ +ﾟ
 ☆  ∪~ ｡*ﾟ
 `･+｡*･+ ﾟ
    '''
    return s

def unknown_schumi_behavior():
    return '朽咪對於你想做的事情感到驚恐 他慌張的跑到電話旁邊準備打給警察局'