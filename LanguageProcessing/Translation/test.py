
from LanguageProcessing.Translation import  GoogleTranslator

translator = GoogleTranslator()

result = translator.get_translation("Я люблю програмувати")
print(result)


