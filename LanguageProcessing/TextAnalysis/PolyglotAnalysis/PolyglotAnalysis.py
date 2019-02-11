import polyglot


# from polyglot.detect import Detector
#
# arabic_text = u"""
# Слава україні
# """
# detector = Detector(arabic_text)
# print(detector.language.code)





import os
import sys
import polyglot
dir_path = os.path.dirname(os.path.realpath(__file__))
path=os.path.join(dir_path, 'data')
polyglot.polyglot_path = path

from polyglot.text import Text
from polyglot.downloader import downloader








# downloader.download("ner2.uk")
#
#
# downloader.list(show_packages=False)

blob = u"""
Народні депутати фракції "Опозиційного блоку" Нестор Шуфрич, Вадим Рабінович і Василь Німченко просять Генпрокуратуру і Державне бюро розслідувань розслідувати "підготовку замаху" на кума президента Росії Віктора Медведчука. Депутатські звернення до директора ДБР Романа Труби і генпрокурора Юрія Луценка оприлюднила прес-служба партії "Опозиційна платформа - За життя".
Нардепи зазначають, що спираються на інформацію про підготовку замаху, яку оприлюднив екс-президент України Віктор Янукович на прес-конференції 6 лютого 2019 року.
"""
text = Text(blob)


for sent in text.sentences:
  print(sent, "\n")
  for entity in sent.entities:
    print(entity.tag, entity)


