import pyshorteners

s = pyshorteners.Shortener()
print("Short link - ", s.tinyurl.short(
    'http://krivaksin.ru/vneurochnoe-zanyatie-po-informatike-pishem-igru-pole-chudes-na-python/'))