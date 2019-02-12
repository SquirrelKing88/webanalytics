# from polyglot.detect import Detector
#
# from LanguageProcessing.TextAnalysis.PolyglotAnalysis.PolyglotAnalysis import PolyglotAnalysis
#
# arabic_text = u"""
# Слава україні
# """
# detector = Detector(arabic_text)
# print(detector.language.code)
from LanguageProcessing.TextAnalysis.PolyglotAnalysis.PolyglotAnalysis import PolyglotAnalysis

blob = u"""
Президент РФ Володимир Путін заявив, що на Казанському авіаційному заводі реалізований проект з доопрацювання надзвукового ракетоносця Ту-160 для Міноборони Росії, і вважає за необхідне створити громадянський надзвуковий літак.

Про це він розповів у вівторок на зустрічі з представниками громадськості, передає російський "Інтерфакс".

"Ми зараз в Казані реалізували блискучий проект: фактично створили нову машину Ту-160 для збройних сил - надзвуковий бойової ракетоносець. І не тільки сам носій, але і зброю до нього допрацювали. Працює все як годинник", - сказав Путін.

При цьому підкреслив необхідність створення подібного цивільного літака.

"Чому не створити і надзвуковий пасажирський літак?" - додав він.

У виданні відзначили, що в кінці січня минулого року Путін вже висловлювався за створення цивільної версії надзвукового літака на базі Ту-160.
"""

pa = PolyglotAnalysis(blob)
