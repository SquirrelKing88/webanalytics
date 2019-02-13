from LanguageProcessing.TextAnalysis.TF_IDF.TF_IDF import TF_IDF

text = ["The quick brown fox jumped over the lazy dog.",
		"The dog.",
		"The fox"]


tf_idf = TF_IDF(text)


print(tf_idf.get_tf_idf())
