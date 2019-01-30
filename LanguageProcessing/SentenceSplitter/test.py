import nltk.data

from LanguageProcessing.SentenceSplitter.SentenceSplitterTrainer import SentenceSplitterTrainer

trainer = SentenceSplitterTrainer("Ukrainian",1000)
trainer.train()

# is_text = "Hann var þríkvæntur. Fyrsta kona hans var Þorbjörg Þórarinsdóttir frá Múla í Aðaldal, f. 19. júlí 1786 á Myrká, d. 19. júlí 1846 á Völlum. Önnur kona Þorbjörg Bergsdóttir (1807-1851) frá Eyvindarstöðum í Sölvadal. Þriðja kona Guðrún Sigfúsdóttir (1812-1864). Hún var 32 árum yngri en brúðguminn, sem var 72 ára er hann kvæntist henni. Hans klaufi er ævintýri eftir H.C. Andersen. "
# tokenizer = nltk.data.load('tokenizers/icelandic.pickle')
# print(tokenizer.tokenize(is_text.strip()))
#
# ko_text = u'1월 20일(현지 시각), 아이티에서 12일 7.0의 강진에 이어 규모 5.9의 강한 지진(사진)이 다시 발생하였다.'
# tokenizer = nltk.data.load('tokenizers/korean.pickle')
# print(tokenizer.tokenize(ko_text.strip()))
#
# hu_text = """II. József (Bécs, 1741. március 13. – Bécs, 1790. február 20.) osztrák főherceg, Mária Terézia és I. Ferenc császár legidősebb fia. 1765-től német-római császár, 1780-tól magyar és cseh király, az első uralkodó, aki a Habsburg–Lotaringiai-házból származott."""
# tokenizer = nltk.data.load('tokenizers/hungarian.pickle')
# print(tokenizer.tokenize(hu_text.strip()))
#
# text = "Ай да А.С. Пушкин!"
# tokenizer = nltk.data.load('tokenizers/russian.pickle')
# print(tokenizer.tokenize(text.strip()))
#
#
#
# text = "Ой! Я що це робиться, люди! І.В. Франко"
# tokenizer = nltk.data.load('tokenizers/ukrainian.pickle')
# print(tokenizer.tokenize(text.strip()))