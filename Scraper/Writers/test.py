import datetime

from Scraper.Writers.FileWriter import FileWriter

data = {'url':
                {
                  "key1":'vakue',
                  'key2':None,
                  'date':datetime.datetime.now()
                }
        }

writer = FileWriter('text.txt')
writer.write(data)