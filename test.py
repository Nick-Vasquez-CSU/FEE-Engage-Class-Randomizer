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
                 "JID_ハイプリースト", "JID_グリフォンナイト", "JID_ドラゴンナイト", "JID_シーフJID_ダンサー"    
                ]

charDicts = {
                "Base" : ['MPID_Lueur', ],
                "Advanced" : ['MPID_Vandre',]
            }
parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse('testDATA.xml', parser=parser)
root = tree.getroot()

# if 'MPID_Lueur' in charDicts["Base"]:
count = 0
for char in root.iter('Param'):
    if count < 104:
        count+=1
        continue
    elif count > 155:
        break
    else:
        randNum = random.randrange(0,len(baseClass))
        char.set('Jid', baseClass[randNum])
        print(count, char.get('Name'), char.get('Jid'))
    count+=1
tree.write('Person-CAB-0aeafa07aee5943d8ee3f3cb13167761-3269709931539129592.xml', encoding='shift-jis') # Utilize shift-jis to output japanese characters 
