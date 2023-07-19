from scrape_plays import scrape

gameID = 262432084


s = scrape()
exc = s.scrapeplays(gameID, 0.2)
print("Exception Raised?", exc)


filename = 'scrape' + str(gameID)

f = open(filename, 'w' )

for line in s.rawplaylist:
    f.write( line + '\n')

f.close()