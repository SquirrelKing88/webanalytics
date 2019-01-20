from SearchSuggestions.GoogleSuggestions import GoogleSuggestions

suggester = GoogleSuggestions()

print(suggester.get_suggestions(["кпі"]))
print(suggester.get_suggestions(["прикладна", "м"]))