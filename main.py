from scrape_plays import scrape

s = scrape()
exc = s.scrapeplays(401403975, 0.2)
print("Exception Raised?", exc)