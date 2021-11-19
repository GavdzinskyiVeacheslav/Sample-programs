import wikipedia

wikipedia.set_lang("ru")
print(wikipedia.summary("Facebook", sentences=3))