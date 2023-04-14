import xml.etree.ElementTree as ET
import random

baseClass = [
             "JID_ソードファイター", "JID_ランスファイター", "JID_アクスファイター", "JID_アーチャー", 
             "JID_ソードアーマー", "JID_ランスアーマー", "JID_アクスアーマー", "JID_ソードナイト",
             "JID_ランスナイト", "JID_アクスナイト", "JID_マージ", "JID_モンク", "JID_ソードペガサス",
             "JID_ランスペガサス", "JID_アクスペガサス", "JID_シーフ", "JID_ダンサー"
            ]

advancedClass = [
                 "JID_ソードマスター", "JID_ブレイブヒーロー", "JID_ハルバーディア", "JID_ロイヤルナイト",
                 "JID_ベルセルク", "JID_ウォーリアー", "JID_ボウナイト", "JID_ジェネラル", "JID_グレートナイト",
                 "JID_パラディン", "JID_ウルフナイト", "JID_セイジ", "JID_マージナイト", "JID_マスターモンク",
                 "JID_ハイプリースト", "JID_グリフォンナイト", "JID_ドラゴンナイト", "JID_シーフ", "JID_ダンサー",
                 "JID_スナイパー"    
                ]

charDicts = {
                "Base" : ['PID_リュール', 'PID_クラン', 'PID_フラン', 'PID_アルフレッド', 'PID_エーティエ', 'PID_ブシュロン', 
                          'PID_セリーヌ', 'PID_クロエ', 'PID_ルイ', 'PID_ユナカ', 'PID_スタルーク', 'PID_シトリニカ', 'PID_ラピス',
                          'PID_ディアマンド', 'PID_アンバー', 'PID_ジェーデ', 'PID_アイビー', 'PID_ゼルコバ', 'PID_フォガート', 
                          'PID_ミスティラ', 'PID_オルテンシア', 'PID_セアダス', 'PID_アンナ', 'PID_ジャン'],

                "Advanced" : ['PID_ヴァンドレ', 'PID_カゲツ', 'PID_パンドロ', 'PID_ボネ', 'PID_パネトネ', 'PID_メリン', 'PID_ロサード', 
                              'PID_ゴルドマリー', 'PID_リンデン', 'PID_ザフィーア', 'PID_ヴェイル', 'PID_モーヴ']
            }

parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse('testDATA.xml', parser=parser)
root = tree.getroot()

# if 'MPID_Lueur' in charDicts["Base"]:
count = 0
for char in root.iter('Param'):
    if char.get('Pid') in charDicts["Base"]:
        randNum = random.randrange(0,len(baseClass))
        char.set('Jid', baseClass[randNum])
        print(count, char.get('Name'), char.get('Jid'))
    elif char.get('Pid') in charDicts["Advanced"]:
        randNum = random.randrange(0,len(advancedClass))
        char.set('Jid', advancedClass[randNum])
        print(count, char.get('Name'), char.get('Jid'))
    elif count > 155:
        break
    else:
        count+=1
        continue
    count+=1
tree.write('Person-CAB-0aeafa07aee5943d8ee3f3cb13167761-3269709931539129592.xml', encoding='shift-jis') # Utilize shift-jis to output japanese characters 
