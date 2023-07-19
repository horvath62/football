from scrape_plays import scrape

s = scrape()
exc = s.scrapeplays(262432084, 0.2)
print("Exception Raised?", exc)