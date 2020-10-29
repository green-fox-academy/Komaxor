'''# Accidentally I got the wrong URL for a funny subreddit. It's probably "odds" and not "bots"
# Also, the URL is missing a crucial component, find out what it is and insert it too!

url = "https//www.reddit.com/r/nevertellmethebots"

print(url)'''


url = "https//www.reddit.com/r/nevertellmethebots"
correct_sub = url.replace('bots', 'odds')
correct_url = correct_sub[:5] + ':' + correct_sub[5:]
print(correct_url)