import requests
import json
import datetime
import sys
import os.path
# import xml.etree.ElementTree as ET
import urllib.parse
# from xml.dom import minidom
import html
import lists
import random

TAGS_TO_CHECK = lists.tags + lists.special_tags
# Increase or reduce this depending on how often the cronjob runs... Default is 24
NUM_POSTS_TO_CHECK = 24
WEBHOOK_URL = "https://discord.com/api/webhooks/914695501050437703/Jq5J_CoDEqYmiMRD6fNUJgsz0fvAbZyC3h58vLjKKhfQFDievo1guDTAMIJKWTBoRXI5"
PATH = "./"


# For safe file names
def slugify(value):
    return "".join([x if x.isalnum() else "_" for x in value])


# Returns number of new posts, number of removed posts.
def getNumNewPosts(oldJson, latestJson):
    for j in range(NUM_POSTS_TO_CHECK):
        print(j)
        oldLatestPost = oldJson[j]
        # if it reaches the end of the for loop then all posts are new
        # "What if there more than 24 posts an hour"? Idk maybe don't do that
        for i in range(NUM_POSTS_TO_CHECK):
            latestPost = latestJson[i]
            if latestPost == oldLatestPost:
                print("Matched post after " + str(i) + " iteration")
                return i, j
            else:
                print(latestPost['file_url'] + " != " + oldLatestPost['file_url'])
        print("Couldn't find the last saved post, trying the next last saved post...")
    print("Failed to find any posts. Giving up and posting them all.")
    return NUM_POSTS_TO_CHECK, 0

def get_gelImage(tags):
    """Returns pictures from Gelbooru with given tags."""
    formatted_tags = ""
    rating = ""
    tags = list(tags)
    ratings = {
        "re": "rating%3aexplicit",
        "rq": "rating%3aquestionable",
        "rs": "rating%3asafe"
    }

    if tags:  # if there are any tags, check for ratings
        for tag in tags:
            #print(tag)
            if tag in ratings:
                rating = ratings[tag]
                tags.remove(tag)
                print(tags)

    if rating == "":  # if rating wasn't specified, set safe one
        rating = ratings["rs"]

    # make tags suitable for Gelbooru API url
    formatted_tags = ' '.join(tags).replace(" ", "+")

    print(rating, formatted_tags)

    api_url = f"https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&limit=50&tags={formatted_tags}+{rating}"
    print(api_url)
    response = requests.get(api_url)
    # parsing json
    json_api_url = json.loads(response.text)
    print(json_api_url)
    # verify if there is anything within given tags
    if json_api_url:
        image = random.choice(json_api_url)["file_url"]
        return image
    else:
        return "No results with given tags or they are incorrect."



print(datetime.datetime.now())
for tag in TAGS_TO_CHECK:
    print("checking " + tag)
    # r = requests.get("https://old.reddit.com/r/"+sub+"/new/.json?count="+str(NUM_POSTS_TO_CHECK), headers = {'User-agent': 'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'})
    r = requests.get("https://gelbooru.com/index.php?page=dapi&json=1&s=post&q=index&limit=" + str(
        NUM_POSTS_TO_CHECK) + "&tags=" + tag.replace(' ', '+'))
    print("Got JSON from server.")
    latestJson = json.loads(r.text)
    # print(latestJson)

    # Number of new posts since last check
    newPosts = NUM_POSTS_TO_CHECK
    numRemovedPosts = 0
    fileName = PATH + slugify(tag) + ".json"
    if os.path.exists(fileName):
        with open(fileName, "r") as f:
            oldJson = json.loads(f.read())
            newPosts, numRemovedPosts = getNumNewPosts(oldJson, latestJson)

#        with open(PATH + sub + ".xml", "r") as f:
#            if newPosts == NUM_POSTS_TO_CHECK:
#                print("comparison failed! exiting...")
#                sys.exit(0)
    else:
        print("File not found. If this is the first time checking the tag, ignore this message.")
        newPosts = 2
    with open(fileName, "w") as f:
        f.write(r.text)
    print("Number of new posts: " + str(newPosts))

def spam():
    for tag in TAGS_TO_CHECK:
        for i in range(newPosts):
            post = latestJson[i]

            description = "\n[Source](" + html.unescape(post['source']) + ")"
            # description = post['tags']
            if i == 0 and numRemovedPosts > 1:
                description += "\nNote: The last post before this one was removed from this subreddit!"

            dataToSend = {
                "username": tag,
                "embeds": [{
                    "title": tag,
                    "description": description,
                    "url": "https://gelbooru.com/index.php?page=post&s=view&id=" + str(post['id'])
                }]
            }
            if post['file_url'].endswith(('.jpg', '.jpeg', '.png', '.gif')):
                dataToSend['embeds'][0]["image"] = {
                    "url": post['file_url']
                }
            else:
                dataToSend['embeds'][0]["image"] = {
                    "url": post['preview_url']
                }
            r = requests.post(
                WEBHOOK_URL,
                json=dataToSend
            )