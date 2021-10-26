# Podcast API Python Library

[![Build Status](https://travis-ci.com/ListenNotes/podcast-api-python.svg?branch=main)](https://travis-ci.com/ListenNotes/podcast-api-python)

The Podcast API Python library provides convenient access to the [Listen Notes Podcast API](https://www.listennotes.com/api/) from
applications written in the Python language.

Simple and no-nonsense podcast search & directory API. Search the meta data of all podcasts and episodes by people, places, or topics. It's the same API that powers [the best podcast search engine Listen Notes](https://www.listennotes.com/).

If you have any questions, please contact [hello@listennotes.com](hello@listennotes.com?subject=Questions+about+the+Python+SDK+of+Listen+API)

<a href="https://www.listennotes.com/api/"><img src="https://raw.githubusercontent.com/ListenNotes/ListenApiDemo/master/web/src/powered_by_listennotes.png" width="300" /></a>


**Table of Contents**
- [Podcast API Python Library](#podcast-api-python-library)
  - [Installation](#installation)
    - [Requirements](#requirements)
  - [Usage](#usage)
    - [Handling exceptions](#handling-exceptions)
  - [API Reference](#api-reference)
    - [Full-text search](#full-text-search)
    - [Typeahead search](#typeahead-search)
    - [Fetch detailed meta data and episodes for a podcast by id](#fetch-detailed-meta-data-and-episodes-for-a-podcast-by-id)
    - [Fetch detailed meta data for an episode by id](#fetch-detailed-meta-data-for-an-episode-by-id)
    - [Fetch a list of supported languages for podcasts](#fetch-a-list-of-supported-languages-for-podcasts)
    - [Fetch a list of podcast genres](#fetch-a-list-of-podcast-genres)
    - [Fetch a list of best podcasts by genre](#fetch-a-list-of-best-podcasts-by-genre)
    - [Fetch a list of supported countries/regions for best podcasts](#fetch-a-list-of-supported-countriesregions-for-best-podcasts)
    - [Fetch recommendations for a podcast](#fetch-recommendations-for-a-podcast)
    - [Fetch recommendations for an episode](#fetch-recommendations-for-an-episode)
    - [Batch fetch basic meta data for episodes](#batch-fetch-basic-meta-data-for-episodes)
    - [Batch fetch basic meta data for podcasts](#batch-fetch-basic-meta-data-for-podcasts)
    - [Fetch a random podcast episode](#fetch-a-random-podcast-episode)
    - [Fetch a curated list of podcasts by id](#fetch-a-curated-list-of-podcasts-by-id)
    - [Fetch curated lists of podcasts](#fetch-curated-lists-of-podcasts)
    - [Submit a podcast to Listen Notes database](#submit-a-podcast-to-listen-notes-database)
    - [Request to delete a podcast](#request-to-delete-a-podcast)
    - [Fetch a playlist&#x27;s info and items (i.e., episodes or podcasts).](#fetch-a-playlists-info-and-items-ie-episodes-or-podcasts)
    - [Fetch a list of your playlists.](#fetch-a-list-of-your-playlists)
    - [Fetch trending search terms](#fetch-trending-search-terms)
    - [Fetch related search terms](#fetch-related-search-terms)
    - [Spell check on a search term](#spell-check-on-a-search-term)

## Installation

Install [the official PIP package](https://pypi.org/project/podcast-api/) of the Listen Notes Podcast API:

```sh
pip install --upgrade podcast-api
```

You can also install from source:

```sh
make && source venv/bin/activate
```

### Requirements

- Python 3.5+

## Usage

The library needs to be configured with your account's API key which is
available in your [Listen API Dashboard](https://www.listennotes.com/api/dashboard/#apps). Set `api_key` to its
value:

```python
from listennotes import podcast_api

api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)

response = client.search(q='star wars')

print(response.json())
```

If `api_key` is None, then we'll connect to a [mock server](https://www.listennotes.com/api/tutorials/#faq0) that returns fake data for testing purposes.


### Handling exceptions

Unsuccessful requests raise exceptions. The class of the exception will reflect
the sort of error that occurred.

| Exception Class  | Description |
| ------------- | ------------- |
|  AuthenticationError | wrong api key or your account is suspended  |
| APIConnectionError  | fail to connect to API servers  |
| InvalidRequestError  | something wrong on your end (client side errors), e.g., missing required parameters  |
| RateLimitError  | you are using FREE plan and you exceed the quota limit  |
| NotFoundError  | endpoint not exist, or podcast / episode not exist  |
| PodcastApiError  | something wrong on our end (unexpected server errors)  |

All exception classes can be found in [this file](https://github.com/ListenNotes/podcast-api-python/blob/main/listennotes/errors.py).

And you can see some sample code [here](https://github.com/ListenNotes/podcast-api-python/blob/main/examples/sample.py#L17).




## API Reference

Each function is a wrapper to send an HTTP request to the corresponding endpoint on the
[API Docs](https://www.listennotes.com/api/docs/).



### Full-text search

Function Name: **search**

Full-text search on episodes, podcasts, or curated lists of podcasts.
Use the `offset` parameter to paginate through search results.
The FREE plan allows to see up to 30 search results (or `offset` &lt; 30) per query.
The PRO plan allows to see up to 300 search results (or `offset` &lt; 300) per query.
The ENTERPRISE plan allows to see up to 10,000 search results (or `offset` &lt; 10000) per query.


Example:
```python

from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)      

response = client.search(
    q='star wars', sort_by_date=1, only_in='title,description')
            
print(response.json())

```

See all available parameters on the [API Docs page](https://www.listennotes.com/api/docs/#get-api-v2-search).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "took": 0.328,
  "count": 10,
  "total": 8972,
  "results": [
    {
      "id": "ea09b575d07341599d8d5b71f205517b",
      "rss": "https://theroughcut.libsyn.com/rss",
      "link": "http://theroughcutpod.com/?p=786&utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/ea09b575d07341599d8d5b71f205517b/",
      "image": "https://production.listennotes.com/podcasts/the-rough-cut-matt-feury-YMha8DxnUbc-53MLh7NpAwm.1400x1400.jpg",
      "podcast": {
        "id": "8758da9be6c8452884a8cab6373b007c",
        "image": "https://production.listennotes.com/podcasts/the-rough-cut-matt-feury-YMha8DxnUbc-53MLh7NpAwm.1400x1400.jpg",
        "genre_ids": [
          68,
          264
        ],
        "thumbnail": "https://production.listennotes.com/podcasts/the-rough-cut-matt-feury-DEkF_8ybj6A-53MLh7NpAwm.300x300.jpg",
        "listen_score": 38,
        "title_original": "The Rough Cut",
        "listennotes_url": "https://www.listennotes.com/c/8758da9be6c8452884a8cab6373b007c/",
        "title_highlighted": "The Rough Cut",
        "publisher_original": "Matt Feury",
        "publisher_highlighted": "Matt Feury",
        "listen_score_global_rank": "2.5%"
      },
      "itunes_id": 1471556007,
      "thumbnail": "https://production.listennotes.com/podcasts/the-rough-cut-matt-feury-DEkF_8ybj6A-53MLh7NpAwm.300x300.jpg",
      "pub_date_ms": 1579507216047,
      "guid_from_rss": "004f03c8-cdf9-4ff5-9d89-b2147f8d55cf",
      "title_original": "Star Wars - The Force Awakens",
      "listennotes_url": "https://www.listennotes.com/e/ea09b575d07341599d8d5b71f205517b/",
      "audio_length_sec": 1694,
      "explicit_content": false,
      "title_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> - The Force Awakens",
      "description_original": "In this episode of The Rough Cut we close out our study of the final Skywalker trilogy with a look back on the film that helped the dormant franchise make the jump to lightspeed, Episode VII - The Force Awakens.\u00a0 Recorded in Amsterdam in front of a festival audience in 2018, editor Maryann Brandon ACE recounts her work on The Force Awakens just as she was about to begin editing what would come to be known as Episode IX - The Rise of Skywalker. \u00a0 Go back to the beginning and listen to our podcast with Star Wars and 'Empire' editor, Paul Hirsch. Hear editor Bob Ducsay talk about cutting The Last Jedi. Listen to Maryann Brandon talk about her work on The Rise of Skywalker. Get your hands on the non-linear editor behind the latest Skywalker trilogy,\u00a0 Avid Media Composer! Subscribe to The Rough Cut for more great interviews with the heroes of the editing room! \u00a0 \u00a0",
      "description_highlighted": "...Go back to the beginning and listen to our podcast with <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> and 'Empire' editor, Paul Hirsch. Hear editor Bob Ducsay talk about cutting The Last Jedi.",
      "transcripts_highlighted": []
    },
    {
      "id": "42b1898db6a84973b41879618002937b",
      "rss": "http://thevintagerpgpodcast.libsyn.com/rss",
      "link": "https://thevintagerpgpodcast.libsyn.com/star-wars-galaxy-guides?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/42b1898db6a84973b41879618002937b/",
      "image": "https://production.listennotes.com/podcasts/the-vintage-rpg-podcast-vintage-rpg-V8MjvNnSRBt-eq8uGUY6vXN.1400x1400.jpg",
      "podcast": {
        "id": "f3094a0b14684300a3d6b69a1063e708",
        "image": "https://production.listennotes.com/podcasts/the-vintage-rpg-podcast-vintage-rpg-V8MjvNnSRBt-eq8uGUY6vXN.1400x1400.jpg",
        "genre_ids": [
          82,
          85,
          83
        ],
        "thumbnail": "https://production.listennotes.com/podcasts/the-vintage-rpg-podcast-vintage-rpg-Mg-2ZYcmERT-eq8uGUY6vXN.300x300.jpg",
        "listen_score": 47,
        "title_original": "The Vintage RPG Podcast",
        "listennotes_url": "https://www.listennotes.com/c/f3094a0b14684300a3d6b69a1063e708/",
        "title_highlighted": "The Vintage RPG Podcast",
        "publisher_original": "Vintage RPG",
        "publisher_highlighted": "Vintage RPG",
        "listen_score_global_rank": "1%"
      },
      "itunes_id": 1409477830,
      "thumbnail": "https://production.listennotes.com/podcasts/the-vintage-rpg-podcast-vintage-rpg-Mg-2ZYcmERT-eq8uGUY6vXN.300x300.jpg",
      "pub_date_ms": 1575867600088,
      "guid_from_rss": "9861105d-bf98-4684-871a-5cbe11484159",
      "title_original": "Star Wars Galaxy Guides",
      "listennotes_url": "https://www.listennotes.com/e/42b1898db6a84973b41879618002937b/",
      "audio_length_sec": 1519,
      "explicit_content": false,
      "title_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Galaxy Guides",
      "description_original": "Because Star Wars is hitting the critical mass point for 2019, we figured we'd add to the fun with an episode that looks at the Galaxy Guides series of sourcebooks for the West End Games Star Wars Role Playing Game. We take a quick tour through each of the twelve volumes and chat about what they added to the RPG experience and how they formed the backbone of the greater Star Wars Expanded Universe. * * * If\u00a0 you dig what we do, join us on the Vintage RPG Patreon for more roleplaying fun and surprises! Patrons keep us going! Like, Rate, Subscribe and Review the Vintage RPG Podcast! Send questions, comments or corrections to\u00a0info@vintagerpg.com. Follow\u00a0Vintage RPG\u00a0on\u00a0Instagram,\u00a0Tumblr\u00a0and\u00a0Facebook. Learn more at the\u00a0Vintage RPG FAQ. Follow\u00a0Stu Horvath,\u00a0John McGuire,\u00a0VintageRPG\u00a0and\u00a0Unwinnable\u00a0on Twitter. Intro music by\u00a0George Collazo. The Vintage RPG illustration is by\u00a0Shafer Brown. Follow\u00a0him on Twitter. Tune in next week for the next episode. Until then, may the dice always roll in your favor!",
      "description_highlighted": "...Because <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> is hitting the critical mass point for 2019, we figured we'd add to the fun with an episode that looks at the Galaxy Guides series of sourcebooks for the West End Games <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Role",
      "transcripts_highlighted": []
    },
    {
      "id": "6280a11466dd407e99c66130f203167a",
      "rss": "https://snlafterparty.libsyn.com/rss",
      "link": "https://snlpodcast.com/episodes/2019/12/24/sample-star-wars-tv-talk-podcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/6280a11466dd407e99c66130f203167a/",
      "image": "https://production.listennotes.com/podcasts/saturday-night-live-snl-afterparty-john-sEoTraLnKPB-_iOE4lLZ2pD.1400x1400.jpg",
      "podcast": {
        "id": "09b986e503d4448ab0b625f6233bdd65",
        "image": "https://production.listennotes.com/podcasts/saturday-night-live-snl-afterparty-john-sEoTraLnKPB-_iOE4lLZ2pD.1400x1400.jpg",
        "genre_ids": [
          68,
          133,
          134
        ],
        "thumbnail": "https://production.listennotes.com/podcasts/saturday-night-live-snl-afterparty-john-wm1CtQVkRfy-_iOE4lLZ2pD.300x300.jpg",
        "listen_score": 44,
        "title_original": "Saturday Night Live (SNL) Afterparty",
        "listennotes_url": "https://www.listennotes.com/c/09b986e503d4448ab0b625f6233bdd65/",
        "title_highlighted": "Saturday Night Live (SNL) Afterparty",
        "publisher_original": "John Murray / Spry FM",
        "publisher_highlighted": "John Murray / Spry FM",
        "listen_score_global_rank": "1%"
      },
      "itunes_id": 1133381225,
      "thumbnail": "https://production.listennotes.com/podcasts/saturday-night-live-snl-afterparty-john-wm1CtQVkRfy-_iOE4lLZ2pD.300x300.jpg",
      "pub_date_ms": 1576989000044,
      "guid_from_rss": "98206b6e-fc6e-45a5-85a6-e54eb4657299",
      "title_original": "Sample: Star Wars TV Talk Podcast",
      "listennotes_url": "https://www.listennotes.com/e/6280a11466dd407e99c66130f203167a/",
      "audio_length_sec": 1690,
      "explicit_content": false,
      "title_highlighted": "Sample: <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> TV Talk Podcast",
      "description_original": "While John is hard at work editing our coverage of Eddie Murphy's triumphant return to Studio 8H, please enjoy this excerpt from the Star Wars TV Talk podcast\u2014on which John is regularly featured. This excerpt is from their discussion of the Disney+ streaming series The Mandalorian chapter 3: \"The Sin\", and contains heavy spoilers. John's take on all things Star Wars TV, can be heard weekly at starwarstvtalk.com or by subscribing to \"Star Wars TV Talk\" wherever better podcasts can be found. Get Our Full-Length Episodes on Patreon  Patreon: Become a patron to access our full-length, ad-free episodes and other exclusive member rewards.  Notes  Daryl's All Natural Protein Bars: Wholesome, nutritious, great tasting, gluten free, low-carb protein bars.   Connect with us at:  snlpodcast.com Patreon: snlpodcast Twitter: @snlpodcast Instagram: snlpodcast Facebook: @snlpodcast feedback@snlpodcast.com   ",
      "description_highlighted": "...John's take on all things <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> TV, can be heard weekly at starwarstvtalk.com or by subscribing to \"<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> TV Talk\" wherever better podcasts can be found.",
      "transcripts_highlighted": []
    },
    {
      "id": "39746ccfc0d64f62aea8e96641366109",
      "rss": "https://www.spreaker.com/show/3200822/episodes/feed",
      "link": "https://www.spreaker.com/user/mcucast/star-wars-is-better-than-star-trek?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/39746ccfc0d64f62aea8e96641366109/",
      "image": "https://production.listennotes.com/podcasts/marvel-cinematic-universe-podcast-deRo7LDQBfn-aXR7VuG2z4p.1400x1400.jpg",
      "podcast": {
        "id": "593c42e343ba44e7b6f8634a946f0b52",
        "image": "https://production.listennotes.com/podcasts/marvel-cinematic-universe-podcast-deRo7LDQBfn-aXR7VuG2z4p.1400x1400.jpg",
        "genre_ids": [
          68,
          99,
          122
        ],
        "thumbnail": "https://production.listennotes.com/podcasts/marvel-cinematic-universe-podcast-wVDeHrdxZJh-aXR7VuG2z4p.300x300.jpg",
        "listen_score": 60,
        "title_original": "Marvel Cinematic Universe Podcast: The Falcon and the Winter Soldier",
        "listennotes_url": "https://www.listennotes.com/c/593c42e343ba44e7b6f8634a946f0b52/",
        "title_highlighted": "Marvel Cinematic Universe Podcast: The Falcon and the Winter Soldier",
        "publisher_original": "Stranded Panda",
        "publisher_highlighted": "Stranded Panda",
        "listen_score_global_rank": "0.5%"
      },
      "itunes_id": 907175322,
      "thumbnail": "https://production.listennotes.com/podcasts/marvel-cinematic-universe-podcast-wVDeHrdxZJh-aXR7VuG2z4p.300x300.jpg",
      "pub_date_ms": 1575521386132,
      "guid_from_rss": "https://api.spreaker.com/episode/20495415",
      "title_original": "Star Wars is better than Star Trek",
      "listennotes_url": "https://www.listennotes.com/e/39746ccfc0d64f62aea8e96641366109/",
      "audio_length_sec": 734,
      "explicit_content": false,
      "title_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> is better than <span class=\"ln-search-highlight\">Star</span> Trek",
      "description_original": "A just for fun episode.  Time to punish Matt for his sins against baby yoda",
      "description_highlighted": "...A just for fun episode.  Time to punish Matt for his sins against baby yoda",
      "transcripts_highlighted": []
    },
    {
      "id": "f13d8c2343e748858464167b426fe67b",
      "rss": "https://feeds.megaphone.fm/ROOSTER7199250968",
      "link": "https://supercarlinbrothers.libsyn.com/star-wars-theory-the-white-saber-theory?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/f13d8c2343e748858464167b426fe67b/",
      "image": "https://production.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-Fyq7cYS9NOs-BodDr7iIAR3.1400x1400.jpg",
      "podcast": {
        "id": "8bdbb906eef04e5d8b391e947998e9af",
        "image": "https://production.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-Fyq7cYS9NOs-BodDr7iIAR3.1400x1400.jpg",
        "genre_ids": [
          68,
          214,
          265,
          99
        ],
        "thumbnail": "https://production.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-TSfxiBaqOwK-BodDr7iIAR3.300x300.jpg",
        "listen_score": 52,
        "title_original": "Super Carlin Brothers",
        "listennotes_url": "https://www.listennotes.com/c/8bdbb906eef04e5d8b391e947998e9af/",
        "title_highlighted": "Super Carlin Brothers",
        "publisher_original": "J and Ben Carlin",
        "publisher_highlighted": "J and Ben Carlin",
        "listen_score_global_rank": "0.5%"
      },
      "itunes_id": 1479112798,
      "thumbnail": "https://production.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-TSfxiBaqOwK-BodDr7iIAR3.300x300.jpg",
      "pub_date_ms": 1576602000177,
      "guid_from_rss": "1a2b9678-7879-4480-94c7-afa1493e9ef9",
      "title_original": "Star Wars Theory: The White Saber Theory",
      "listennotes_url": "https://www.listennotes.com/e/f13d8c2343e748858464167b426fe67b/",
      "audio_length_sec": 762,
      "explicit_content": false,
      "title_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Theory: The White Saber Theory",
      "description_original": "With Star Wars Episode 9 The Rise of Skywalker just days away J dives into the Star Wars Galaxy to discuss the future of Kylo Ren\u2019s Lightsaber and the White Saber theory!",
      "description_highlighted": "...With <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Episode 9 The Rise of Skywalker just days away J dives into the <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Galaxy to discuss the future of Kylo Ren\u2019s Lightsaber and the White Saber theory!",
      "transcripts_highlighted": []
    },
    {
      "id": "7d10e4bf2c1446d8b095df043fb39d68",
      "rss": "https://www.omnycontent.com/d/playlist/b004fc18-3e73-404c-9a0a-aaa2001f4448/fdc7f23c-a55d-492f-8899-aaa40023fd0e/5879b0b2-04a5-45e2-9e20-aaa400241c06/podcast.rss",
      "link": "https://viewfinder.expedia.com/travel-podcast-bonus-return-to-star-wars-galaxys-edge/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/7d10e4bf2c1446d8b095df043fb39d68/",
      "image": "https://production.listennotes.com/podcasts/out-travel-the-system-expedia-905g8Xv-mCa-1X9JaE0p7TV.1400x1400.jpg",
      "podcast": {
        "id": "84bc40c6aa2948edbf6fbb53cd73707c",
        "image": "https://production.listennotes.com/podcasts/out-travel-the-system-expedia-905g8Xv-mCa-1X9JaE0p7TV.1400x1400.jpg",
        "genre_ids": [
          123,
          82,
          122,
          244
        ],
        "thumbnail": "https://production.listennotes.com/podcasts/out-travel-the-system-expedia-N0J98aznigq-1X9JaE0p7TV.300x300.jpg",
        "listen_score": 43,
        "title_original": "Out Travel The System",
        "listennotes_url": "https://www.listennotes.com/c/84bc40c6aa2948edbf6fbb53cd73707c/",
        "title_highlighted": "Out Travel The System",
        "publisher_original": "Expedia",
        "publisher_highlighted": "Expedia",
        "listen_score_global_rank": "1.5%"
      },
      "itunes_id": 1477909314,
      "thumbnail": "https://production.listennotes.com/podcasts/out-travel-the-system-expedia-N0J98aznigq-1X9JaE0p7TV.300x300.jpg",
      "pub_date_ms": 1575586800048,
      "guid_from_rss": "d044f77b-3738-4c9e-8d54-ab1a01559db0",
      "title_original": "Return to Star Wars: Galaxy's Edge",
      "listennotes_url": "https://www.listennotes.com/e/7d10e4bf2c1446d8b095df043fb39d68/",
      "audio_length_sec": 1166,
      "explicit_content": false,
      "title_highlighted": "Return to <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span>: Galaxy's Edge",
      "description_original": "Kent and Canaan Reiersgaard from &lsquo;No Vacation Required' are back for a special bonus episode, with early access to the new Rise of the Resistance ride at Star Wars: Galaxy's Edge opening today in Orlando.\nWe first got the initial full scoop on Star Wars: Galaxy's Edge at Disneyland with Kent and Canaan, back in Episode Three of this season of Out Travel the System.\nTell us about your Disney experience at podcast@expedia.com or find us on&nbsp;Twitter, Facebook and Instagram!&nbsp;See omnystudio.com/listener for privacy information.",
      "description_highlighted": "...We first got the initial full scoop on <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span>: Galaxy's Edge at Disneyland with Kent and Canaan, back in Episode Three of this season of Out Travel the System.",
      "transcripts_highlighted": []
    },
    {
      "id": "a34693ebf8b04a64b448208281965298",
      "rss": "https://feeds.megaphone.fm/ROOSTER7199250968",
      "link": "https://supercarlinbrothers.libsyn.com/star-wars-theory-was-han-solo-force-sensitive?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/a34693ebf8b04a64b448208281965298/",
      "image": "https://production.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-Fyq7cYS9NOs-BodDr7iIAR3.1400x1400.jpg",
      "podcast": {
        "id": "8bdbb906eef04e5d8b391e947998e9af",
        "image": "https://production.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-Fyq7cYS9NOs-BodDr7iIAR3.1400x1400.jpg",
        "genre_ids": [
          68,
          214,
          265,
          99
        ],
        "thumbnail": "https://production.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-TSfxiBaqOwK-BodDr7iIAR3.300x300.jpg",
        "listen_score": 52,
        "title_original": "Super Carlin Brothers",
        "listennotes_url": "https://www.listennotes.com/c/8bdbb906eef04e5d8b391e947998e9af/",
        "title_highlighted": "Super Carlin Brothers",
        "publisher_original": "J and Ben Carlin",
        "publisher_highlighted": "J and Ben Carlin",
        "listen_score_global_rank": "0.5%"
      },
      "itunes_id": 1479112798,
      "thumbnail": "https://production.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-TSfxiBaqOwK-BodDr7iIAR3.300x300.jpg",
      "pub_date_ms": 1575997200179,
      "guid_from_rss": "a3f1ff19-7ce1-4069-8efe-ae7727fb0b98",
      "title_original": "Star Wars Theory: Was Han Solo Force Sensitive?",
      "listennotes_url": "https://www.listennotes.com/e/a34693ebf8b04a64b448208281965298/",
      "audio_length_sec": 855,
      "explicit_content": false,
      "title_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Theory: Was Han Solo Force Sensitive?",
      "description_original": "Today J dives into the Star Wars Galaxy to try and answer an age old question: Could Han Solo use The Force? We meet Han Solo as a somewhat overconfident pilot who seems to make his way through the galaxy thanks to his charm, a bit of wit, and a lot of luck. But today we examine whether or not all of that luck behind Han\u2019s success is simply luck OR is it something else?!",
      "description_highlighted": "...Today J dives into the <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Galaxy to try and answer an age old question: Could Han Solo use The Force?",
      "transcripts_highlighted": []
    },
    {
      "id": "8d6fdee228dc452bbfc422af1ced5e68",
      "rss": "https://feeds.megaphone.fm/ROOSTER7199250968",
      "link": "https://traffic.libsyn.com/secure/supercarlinbrothers/Lil_Yoda.mp3?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/8d6fdee228dc452bbfc422af1ced5e68/",
      "image": "https://production.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-Fyq7cYS9NOs-BodDr7iIAR3.1400x1400.jpg",
      "podcast": {
        "id": "8bdbb906eef04e5d8b391e947998e9af",
        "image": "https://production.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-Fyq7cYS9NOs-BodDr7iIAR3.1400x1400.jpg",
        "genre_ids": [
          68,
          214,
          265,
          99
        ],
        "thumbnail": "https://production.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-TSfxiBaqOwK-BodDr7iIAR3.300x300.jpg",
        "listen_score": 52,
        "title_original": "Super Carlin Brothers",
        "listennotes_url": "https://www.listennotes.com/c/8bdbb906eef04e5d8b391e947998e9af/",
        "title_highlighted": "Super Carlin Brothers",
        "publisher_original": "J and Ben Carlin",
        "publisher_highlighted": "J and Ben Carlin",
        "listen_score_global_rank": "0.5%"
      },
      "itunes_id": 1479112798,
      "thumbnail": "https://production.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-TSfxiBaqOwK-BodDr7iIAR3.300x300.jpg",
      "pub_date_ms": 1574365061183,
      "guid_from_rss": "095b0add-db46-452b-af45-4bd1eed34bdd",
      "title_original": "Star Wars Theory: Where Does Yoda Come From!?",
      "listennotes_url": "https://www.listennotes.com/e/8d6fdee228dc452bbfc422af1ced5e68/",
      "audio_length_sec": 749,
      "explicit_content": false,
      "title_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Theory: Where Does Yoda Come From!?",
      "description_original": "The Mandalorian has introduced us to an ADORABLE tiny little Yoda creature. We keep calling it a \"Yoda Creature\" because despite the vast Star Wars expanded universe... Yoda's species has intentionally remained a mystery. Today we dive in to find out more!\u00a0",
      "description_highlighted": "...We keep calling it a \"Yoda Creature\" because despite the vast <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> expanded universe... Yoda's species has intentionally remained a mystery. Today we dive in to find out more!\u00a0",
      "transcripts_highlighted": []
    },
    {
      "id": "3348a2918d8643aa8dfe3b8471846e2c",
      "rss": "https://feeds.buzzsprout.com/726630.rss",
      "link": "http://www.youtube.com/c/starwarsexplained?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/3348a2918d8643aa8dfe3b8471846e2c/",
      "image": "https://production.listennotes.com/podcasts/star-wars-explained-alex-mollie-c8Ju4l6grFQ-zuwl0R2DOjf.1400x1400.jpg",
      "podcast": {
        "id": "699701ca2479411f9c0bbf8dd85323e8",
        "image": "https://production.listennotes.com/podcasts/star-wars-explained-alex-mollie-c8Ju4l6grFQ-zuwl0R2DOjf.1400x1400.jpg",
        "genre_ids": [
          168,
          68,
          265,
          185
        ],
        "thumbnail": "https://production.listennotes.com/podcasts/star-wars-explained-alex-mollie-_li6TLEwgs2-zuwl0R2DOjf.300x300.jpg",
        "listen_score": 46,
        "title_original": "Star Wars Explained",
        "listennotes_url": "https://www.listennotes.com/c/699701ca2479411f9c0bbf8dd85323e8/",
        "title_highlighted": "Star Wars Explained",
        "publisher_original": "Alex & Mollie",
        "publisher_highlighted": "Alex & Mollie",
        "listen_score_global_rank": "1%"
      },
      "itunes_id": 1488511803,
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-explained-alex-mollie-_li6TLEwgs2-zuwl0R2DOjf.300x300.jpg",
      "pub_date_ms": 1574614800060,
      "guid_from_rss": "Buzzsprout-2155283",
      "title_original": "Star Wars Jedi: Fallen Order - Full Story Review",
      "listennotes_url": "https://www.listennotes.com/e/3348a2918d8643aa8dfe3b8471846e2c/",
      "audio_length_sec": 605,
      "explicit_content": false,
      "title_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Jedi: Fallen Order - Full Story Review",
      "description_original": "I wholeheartedly love the story being told in Star Wars Jedi: Fallen Order. Now that the game has been out for a bit, this is my full spoiler review of what happens.---Subscribe for more Star Wars videos every day!---Support the channel: https://www.patreon.com/starwarsexplainInstagram: http://instagram.com/starwarsexplainedTwitter: https://twitter.com/StarWarsExplainFacebook: https://www.facebook.com/groups/starw...Discord: https://discord.gg/KEJfSHuSnapchat: SWMinuteGoogle+: http://goo.gl/Q3gDkYStar Wars Tees: http://shrsl.com/?~9i83VLOG channel: https://www.youtube.com/c/malexvlog---#starwarsSupport the show (https://www.patreon.com/starwarsexplain)",
      "description_highlighted": "...---Subscribe for more <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> videos every day!",
      "transcripts_highlighted": []
    },
    {
      "id": "3085778cddee458ab009140359ab230e",
      "rss": "https://feeds.buzzsprout.com/191780.rss",
      "link": "http://www.forcematerial.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/3085778cddee458ab009140359ab230e/",
      "image": "https://production.listennotes.com/podcasts/force-material-a-star-wars-podcast-force-nI3R8G7BYbF-0x25uB7_DtW.1400x1400.jpg",
      "podcast": {
        "id": "b3c5943ff8f74d968675365259b27c68",
        "image": "https://production.listennotes.com/podcasts/force-material-a-star-wars-podcast-force-nI3R8G7BYbF-0x25uB7_DtW.1400x1400.jpg",
        "genre_ids": [
          68
        ],
        "thumbnail": "https://production.listennotes.com/podcasts/force-material-a-star-wars-podcast-force-vnMI68HTZoL-0x25uB7_DtW.300x300.jpg",
        "listen_score": 38,
        "title_original": "Force Material: A Star Wars Podcast",
        "listennotes_url": "https://www.listennotes.com/c/b3c5943ff8f74d968675365259b27c68/",
        "title_highlighted": "Force Material: A Star Wars Podcast",
        "publisher_original": "Force Material: A Star Wars Podcast",
        "publisher_highlighted": "Force Material: A Star Wars Podcast",
        "listen_score_global_rank": "2%"
      },
      "itunes_id": 1290847550,
      "thumbnail": "https://production.listennotes.com/podcasts/force-material-a-star-wars-podcast-force-vnMI68HTZoL-0x25uB7_DtW.300x300.jpg",
      "pub_date_ms": 1572184800051,
      "guid_from_rss": "Buzzsprout-1940420",
      "title_original": "Heavy Metal Star Wars w/ Galactic Empire",
      "listennotes_url": "https://www.listennotes.com/e/3085778cddee458ab009140359ab230e/",
      "audio_length_sec": 960,
      "explicit_content": false,
      "title_highlighted": "Heavy Metal <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> w/ Galactic Empire",
      "description_original": "YouTube sensations Galactic Empire tell us how they turn classic John Williams themes into heavy metal bangers! Galactic Empire are bringing their fully armed and operational battle station to Australia in November, so we got frontman Dark Vader (aka Chris Kelly) on the phone to talk about the band&apos;s unique Star Wars covers and music videos; how the music of the sequel trilogy compares to the scores we grew up with; the future of Star Wars music after John Williams; and his fan expectations for The Rise of Skywalker.\u00a0 Galactic Empire will play the following dates in Australia: Friday 1 November \u2014 Supanova (Adelaide)Sunday 3 November \u2014 170 Russell (Melbourne)Tuesday 5 November \u2014 The Basement (Canberra)Thursday 7 November \u2014 Factory Theatre (Sydney)Friday 8 November \u2014 Supanova (Brisbane)Sunday 10 November \u2014 Coolangatta Hotel (Gold Coast) For tickets, visit tickets.destroyalllines.com.",
      "description_highlighted": "...<span class=\"ln-search-highlight\">Wars</span> covers and music videos; how the music of the sequel trilogy compares to the scores we grew up with; the future of <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> music after John Williams; and his fan expectations for The Rise of Skywalker",
      "transcripts_highlighted": []
    }
  ],
  "next_offset": 10
}
```   
</details>



<details>
  <summary>Click to see response schema</summary>
  
```json
{
  "type": "object",
  "properties": {
    "took": {
      "type": "number",
      "example": 0.093,
      "description": "The time it took to fetch these search results. In seconds."
    },
    "count": {
      "type": "integer",
      "example": 10,
      "description": "The number of search results in this page."
    },
    "total": {
      "type": "integer",
      "example": 1989,
      "description": "The total number of search results."
    },
    "results": {
      "type": "array",
      "items": {
        "oneOf": [
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "example": "4d82e50314174754a3b603912448e812",
                "description": "Episode id."
              },
              "rss": {
                "type": "string",
                "example": "https://sw7x7.libsyn.com/rss",
                "description": "RSS url of this podcast. This field is available only in the PRO/ENTERPRISE plan."
              },
              "link": {
                "type": "string",
                "example": "https://www.npr.org/2020/01/22/798532179/soleimanis-iran",
                "description": "Web link of this episode."
              },
              "audio": {
                "type": "string",
                "example": "https://www.listennotes.com/e/p/11b34041e804491b9704d11f283c74de/",
                "description": "Audio url of this episode, which can be played directly."
              },
              "image": {
                "type": "string",
                "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
                "description": "Image url for this episode.\nIf an episode doesn't have its own image, then this field would be the url of the podcast artwork image.\nIf you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
              },
              "podcast": {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "string",
                    "example": "4d3fe717742d4963a85562e9f84d8c79",
                    "description": "Podcast id."
                  },
                  "image": {
                    "type": "string",
                    "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
                    "description": "Image url for this podcast's artwork. If you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
                  },
                  "genre_ids": {
                    "type": "array",
                    "items": {
                      "type": "integer",
                      "description": "Genre ids."
                    },
                    "example": [
                      138,
                      86,
                      160,
                      68,
                      82,
                      100,
                      101
                    ]
                  },
                  "thumbnail": {
                    "type": "string",
                    "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
                    "description": "Thumbnail image url for this podcast's artwork (300x300)."
                  },
                  "listen_score": {
                    "type": "integer",
                    "example": 81,
                    "description": "The estimated popularity score of a podcast compared to all other rss-based public podcasts in the world on a scale from 0 to 100.\nIf the score is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
                  },
                  "title_original": {
                    "type": "string",
                    "example": "Star Wars 7x7 | Star Wars News, Interviews, and More!",
                    "description": "Plain text of podcast name."
                  },
                  "listennotes_url": {
                    "type": "string",
                    "example": "https://www.listennotes.com/c/4d3fe717742d4963a85562e9f84d8c79/",
                    "description": "The url of this podcast on [ListenNotes.com](https://www.ListenNotes.com)."
                  },
                  "title_highlighted": {
                    "type": "string",
                    "example": "<span class=\\\"ln-search-highlight\\\">Star</span> <span class=\\\"ln-search-highlight\\\">Wars</span> 7x7 | <span class=\\\"ln-search-highlight\\\">Star</span> <span class=\\\"ln-search-highlight\\\">Wars</span> News, Interviews, and More!",
                    "description": "Highlighted segment of podcast name."
                  },
                  "publisher_original": {
                    "type": "string",
                    "example": "Star Wars Daily, by Allen Voivod",
                    "description": "Plain text of this podcast's publisher name."
                  },
                  "publisher_highlighted": {
                    "type": "string",
                    "example": "<span class=\\\"ln-search-highlight\\\">Star</span> <span class=\\\"ln-search-highlight\\\">Wars</span> Daily, by Allen Voivod",
                    "description": "Highlighted segment of this podcast's publisher name."
                  },
                  "listen_score_global_rank": {
                    "type": "string",
                    "example": "0.5%",
                    "description": "The estimated popularity ranking of a podcast compared to all other rss-based public podcasts in the world.\nFor example, if the value is 0.5%, then this podcast is one of the top 0.5% most popular shows out of all podcasts globally, ranked by Listen Score.\nIf the ranking is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
                  }
                },
                "description": "The podcast that this episode belongs to."
              },
              "itunes_id": {
                "type": "integer",
                "example": 896354638,
                "description": "iTunes id for this podcast."
              },
              "thumbnail": {
                "type": "string",
                "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
                "description": "Thumbnail image (300x300) url for this episode.\nIf an episode doesn't have its own image, then this field would be the url of the podcast artwork thumbnail image.\n"
              },
              "pub_date_ms": {
                "type": "integer",
                "example": 1474873200000,
                "description": "Published date for this episode. In millisecond."
              },
              "title_original": {
                "type": "string",
                "example": "815: Star Wars 2020 Movie and Beyond!",
                "description": "Plain text of this episode' title"
              },
              "listennotes_url": {
                "type": "string",
                "example": "https://www.listennotes.com/e/4d82e50314174754a3b603912448e812/",
                "description": "The url of this episode on [ListenNotes.com](https://www.ListenNotes.com)."
              },
              "audio_length_sec": {
                "type": "integer",
                "example": 567,
                "description": "Audio length of this episode. In seconds."
              },
              "explicit_content": {
                "type": "boolean",
                "example": false,
                "description": "Whether this podcast contains explicit language."
              },
              "title_highlighted": {
                "type": "string",
                "example": "815: <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> 2020 Movie and Beyond!",
                "description": "Highlighted segment of this episode's title"
              },
              "description_original": {
                "type": "string",
                "example": "Yeah, Star Wars Celebration Orlando is 32 days away, but what's the scoop on Celebration 2018? Plus, Rebels Day is Saturday, and much more in our update. Punch it! ***We're listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u00e2\u20ac\u2122ll get some fabulous rewards for your pledge.***  Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast. Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!\n",
                "description": "Plain text of this episode's description"
              },
              "description_highlighted": {
                "type": "string",
                "example": "...Go to http://Patreon.com/sw7x7 to donate to the <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> 7x7 podcast, and you'll get some fabulous rewards for your pledge.***  Check out SW7x7.com for full <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> 7x7 show notes and links, and to\n",
                "description": "Highlighted segment of this episode's description"
              },
              "transcripts_highlighted": {
                "type": "array",
                "items": {
                  "type": "string",
                  "example": "00:21:27  when Disney bought the <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> franchise from George Lucas they had a plan lots of <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> movies new <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> movies every month another one was just released while I was talking\n"
                },
                "description": "Up to 2 highlighted segments of the audio transcript of this episode."
              }
            },
            "description": "When **type** is *episode*."
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "example": "4d3fe717742d4963a85562e9f84d8c79",
                "description": "Podcast id."
              },
              "rss": {
                "type": "string",
                "example": "https://sw7x7.libsyn.com/rss",
                "description": "RSS url of this podcast. This field is available only in the PRO/ENTERPRISE plan."
              },
              "email": {
                "type": "string",
                "example": "hello@example.com",
                "description": "The email of this podcast's producer. This field is available only in the PRO/ENTERPRISE plan."
              },
              "image": {
                "type": "string",
                "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
                "description": "Image url for this podcast's artwork. If you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
              },
              "website": {
                "type": "string",
                "example": "http://sw7x7.com/",
                "description": "Website url of this podcast."
              },
              "genre_ids": {
                "type": "array",
                "items": {
                  "type": "integer",
                  "description": "Genre ids."
                },
                "example": [
                  138,
                  86,
                  160,
                  68,
                  82,
                  100,
                  101
                ]
              },
              "itunes_id": {
                "type": "integer",
                "example": 896354638,
                "description": "iTunes id for this podcast."
              },
              "thumbnail": {
                "type": "string",
                "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
                "description": "Thumbnail image url for this podcast's artwork (300x300)."
              },
              "listen_score": {
                "type": "integer",
                "example": 81,
                "description": "The estimated popularity score of a podcast compared to all other rss-based public podcasts in the world on a scale from 0 to 100.\nIf the score is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
              },
              "title_original": {
                "type": "string",
                "example": "Star Wars 7x7 | Star Wars News, Interviews, and More!",
                "description": "Plain text of podcast name."
              },
              "total_episodes": {
                "type": "integer",
                "example": 324,
                "description": "Total number of episodes in this podcast."
              },
              "listennotes_url": {
                "type": "string",
                "example": "https://www.listennotes.com/c/4d3fe717742d4963a85562e9f84d8c79/",
                "description": "The url of this podcast on [ListenNotes.com](https://www.ListenNotes.com)."
              },
              "explicit_content": {
                "type": "boolean",
                "example": false,
                "description": "Whether this podcast contains explicit language."
              },
              "title_highlighted": {
                "type": "string",
                "example": "<span class=\\\"ln-search-highlight\\\">Star</span> <span class=\\\"ln-search-highlight\\\">Wars</span> 7x7 | <span class=\\\"ln-search-highlight\\\">Star</span> <span class=\\\"ln-search-highlight\\\">Wars</span> News, Interviews, and More!",
                "description": "Highlighted segment of podcast name."
              },
              "latest_pub_date_ms": {
                "type": "integer",
                "example": 1557499770000,
                "description": "The published date of the latest episode of this podcast. In milliseconds"
              },
              "publisher_original": {
                "type": "string",
                "example": "Star Wars Daily, by Allen Voivod",
                "description": "Plain text of this podcast's publisher name."
              },
              "description_original": {
                "type": "string",
                "example": "The Star Wars 7x7 Podcast is Rebel-rousing fun for everyday Jedi, between 7 and 14 minutes a day, 7 days a week. Join host Allen Voivod for Star Wars news, history, interviews, trivia, and deep dives into the Star Wars story as told in movies, books, comics, games, cartoons, and more. Subscribe now for your daily dose of Star Wars joy. It's destiny unleashed! #SW7x7\n",
                "description": "Plain text of podcast description"
              },
              "earliest_pub_date_ms": {
                "type": "integer",
                "example": 1470667902000,
                "description": "The published date of the oldest episode of this podcast. In milliseconds"
              },
              "publisher_highlighted": {
                "type": "string",
                "example": "<span class=\\\"ln-search-highlight\\\">Star</span> <span class=\\\"ln-search-highlight\\\">Wars</span> Daily, by Allen Voivod",
                "description": "Highlighted segment of this podcast's publisher name."
              },
              "description_highlighted": {
                "type": "string",
                "example": "...Join host Allen Voivod for <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> news, history, interviews, trivia, and deep dives into the <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> story as told in movies, books, comics, games, cartoons, and more.\n",
                "description": "Highlighted segment of podcast description"
              },
              "listen_score_global_rank": {
                "type": "string",
                "example": "0.5%",
                "description": "The estimated popularity ranking of a podcast compared to all other rss-based public podcasts in the world.\nFor example, if the value is 0.5%, then this podcast is one of the top 0.5% most popular shows out of all podcasts globally, ranked by Listen Score.\nIf the ranking is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
              }
            },
            "description": "When **type** is *podcast*."
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "example": "Vb017Sx3l8F",
                "description": "Curated list id."
              },
              "total": {
                "type": "integer",
                "example": 25,
                "description": "The total number of podcasts in this curated list."
              },
              "podcasts": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string",
                      "example": "4d3fe717742d4963a85562e9f84d8c79",
                      "description": "Podcast id."
                    },
                    "image": {
                      "type": "string",
                      "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
                      "description": "Image url for this podcast's artwork. If you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
                    },
                    "title": {
                      "type": "string",
                      "example": "Star Wars 7x7 | Star Wars News, Interviews, and More!",
                      "description": "Podcast name."
                    },
                    "publisher": {
                      "type": "string",
                      "example": "Planet Broadcasting",
                      "description": "Podcast publisher name."
                    },
                    "thumbnail": {
                      "type": "string",
                      "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
                      "description": "Thumbnail image url for this podcast's artwork (300x300)."
                    },
                    "listen_score": {
                      "type": "integer",
                      "example": 81,
                      "description": "The estimated popularity score of a podcast compared to all other rss-based public podcasts in the world on a scale from 0 to 100.\nIf the score is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
                    },
                    "listennotes_url": {
                      "type": "string",
                      "example": "https://www.listennotes.com/c/4d3fe717742d4963a85562e9f84d8c79/",
                      "description": "The url of this podcast on [ListenNotes.com](https://www.ListenNotes.com)."
                    },
                    "listen_score_global_rank": {
                      "type": "string",
                      "example": "0.5%",
                      "description": "The estimated popularity ranking of a podcast compared to all other rss-based public podcasts in the world.\nFor example, if the value is 0.5%, then this podcast is one of the top 0.5% most popular shows out of all podcasts globally, ranked by Listen Score.\nIf the ranking is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
                    }
                  }
                },
                "description": "Up to 5 podcasts in this curated list."
              },
              "source_url": {
                "type": "string",
                "example": "https://parade.com/718913/ashley_johnson/7-bookish-podcasts-for-avid-readers-on-the-go/",
                "description": "Url of the source of this curated list."
              },
              "pub_date_ms": {
                "type": "integer",
                "example": 1556843484301,
                "description": "Published date of this curated list. In milliseconds."
              },
              "source_domain": {
                "type": "string",
                "example": "parade.com",
                "description": "The domain name of the source of this curated list."
              },
              "title_original": {
                "type": "string",
                "example": "What are some good Star Wars Podcast to listen to?",
                "description": "Plain text of this curated list's title"
              },
              "listennotes_url": {
                "type": "string",
                "example": "https://www.listennotes.com/curated-podcasts/7-bookish-podcasts-for-avid-readers-on-H2r-TCWai8K/",
                "description": "The url of this curated list on [ListenNotes.com](https://www.ListenNotes.com)."
              },
              "title_highlighted": {
                "type": "string",
                "example": "What are some good <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Podcast to listen to?\n",
                "description": "Highlighted segment of this curated list's title"
              },
              "description_original": {
                "type": "string",
                "example": "Star Wars fans in Reddit shared their favorite podcasts.",
                "description": "Plain text of this curated list's description"
              },
              "description_highlighted": {
                "type": "string",
                "example": "...<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> fans in Reddit shared their favorite podcasts.",
                "description": "Highlighted segment of this curated list's description"
              }
            },
            "description": "When **type** is *curated*."
          }
        ]
      },
      "description": "A list of search results."
    },
    "next_offset": {
      "type": "integer",
      "example": 10,
      "description": "Pass this value to the **offset** parameter to do pagination of search results."
    }
  }
}
```   
</details>




### Typeahead search

Function Name: **typeahead**

Suggest search terms, podcast genres, and podcasts.

Example:
```python

from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)      

response = client.typeahead(q='star wars', show_podcasts=1)
            
print(response.json())

```

See all available parameters on the [API Docs page](https://www.listennotes.com/api/docs/#get-api-v2-typeahead).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "terms": [
    "star wars"
  ],
  "genres": [
    {
      "id": 160,
      "name": "Star Wars",
      "parent_id": 68
    }
  ],
  "podcasts": [
    {
      "id": "ca3b35271db04291ba56fab8a4f731e4",
      "image": "https://production.listennotes.com/podcasts/rebel-force-radio-star-wars-podcast-star-wars-GSQTPOZCqAx-4v5pRaEg1Ub.1400x1400.jpg",
      "thumbnail": "https://production.listennotes.com/podcasts/rebel-force-radio-star-wars-podcast-star-wars-Na1ogntxKO_-4v5pRaEg1Ub.300x300.jpg",
      "title_original": "Rebel Force Radio: Star Wars Podcast",
      "explicit_content": false,
      "title_highlighted": "Rebel Force Radio: <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Podcast",
      "publisher_original": "Star Wars",
      "publisher_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span>"
    },
    {
      "id": "912f36444ea6475693ab3ab899cc3782",
      "image": "https://production.listennotes.com/podcasts/star-wars-theory-jigowatt-media-2ymqOIn0BAj-FGYt8XM-sIK.1400x1400.jpg",
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-theory-jigowatt-media--12pFlUErbi-FGYt8XM-sIK.300x300.jpg",
      "title_original": "Star Wars Theory",
      "explicit_content": false,
      "title_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Theory",
      "publisher_original": "Jigowatt Media",
      "publisher_highlighted": "Jigowatt Media"
    },
    {
      "id": "8e90b8f0c9eb4c11b13f9dc331ed747c",
      "image": "https://production.listennotes.com/podcasts/inside-star-wars-wondery-F8ZBEqObITM-e8ydUYnAOJv.1400x1400.jpg",
      "thumbnail": "https://production.listennotes.com/podcasts/inside-star-wars-wondery-2Ep_n06B8ad-e8ydUYnAOJv.300x300.jpg",
      "title_original": "Inside Star Wars",
      "explicit_content": false,
      "title_highlighted": "Inside <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span>",
      "publisher_original": "Wondery",
      "publisher_highlighted": "Wondery"
    },
    {
      "id": "ff1938a1747c4698976943bf5f685600",
      "image": "https://production.listennotes.com/podcasts/children-of-the-watch-a-star-wars-show-star-T-SkJRxBrs3-lt7yMQIx2fP.1400x1400.jpg",
      "thumbnail": "https://production.listennotes.com/podcasts/children-of-the-watch-a-star-wars-show-star-imRISqzWeth-lt7yMQIx2fP.300x300.jpg",
      "title_original": "Children of the Watch: A Star Wars Show",
      "explicit_content": false,
      "title_highlighted": "Children of the Watch: A <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Show",
      "publisher_original": "Star Wars",
      "publisher_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span>"
    },
    {
      "id": "9af8a811286b4fffa82e4c083cf5e711",
      "image": "https://production.listennotes.com/podcasts/star-wars-minute-star-wars-minute-RCHpuilvzfZ-GJRN7_nAPOM.1400x1400.jpg",
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-minute-star-wars-minute-dkYIhKa6oZB-GJRN7_nAPOM.300x300.jpg",
      "title_original": "Star Wars Minute",
      "explicit_content": false,
      "title_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Minute",
      "publisher_original": "Star Wars Minute",
      "publisher_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Minute"
    }
  ]
}
```   
</details>



<details>
  <summary>Click to see response schema</summary>
  
```json
{
  "type": "object",
  "required": [
    "terms"
  ],
  "properties": {
    "terms": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "example": [
        "startup sales",
        "startup",
        "startups",
        "star wars"
      ],
      "description": "Search term suggestions."
    },
    "genres": {
      "type": "array",
      "items": {
        "type": "object",
        "example": {
          "id": 140,
          "name": "Web Design",
          "parent_id": 127
        },
        "properties": {
          "id": {
            "type": "integer",
            "example": 93,
            "description": "Genre id"
          },
          "name": {
            "type": "string",
            "example": "Business",
            "description": "Genre name."
          },
          "parent_id": {
            "type": "integer",
            "example": 95,
            "description": "Parent genre id."
          }
        }
      },
      "description": "Genre suggestions. It'll show up when the **show_genres** parameter is *1*."
    },
    "podcasts": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "example": "4d3fe717742d4963a85562e9f84d8c79",
            "description": "Podcast id."
          },
          "image": {
            "type": "string",
            "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
            "description": "Image url for this podcast's artwork. If you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
          },
          "thumbnail": {
            "type": "string",
            "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
            "description": "Thumbnail image url for this podcast's artwork (300x300)."
          },
          "title_original": {
            "type": "string",
            "example": "Star Wars 7x7 | Star Wars News, Interviews, and More!",
            "description": "Plain text of podcast name."
          },
          "explicit_content": {
            "type": "boolean",
            "example": false,
            "description": "Whether this podcast contains explicit language."
          },
          "title_highlighted": {
            "type": "string",
            "example": "<span class=\\\"ln-search-highlight\\\">Star</span> <span class=\\\"ln-search-highlight\\\">Wars</span> 7x7 | <span class=\\\"ln-search-highlight\\\">Star</span> <span class=\\\"ln-search-highlight\\\">Wars</span> News, Interviews, and More!",
            "description": "Highlighted segment of podcast name."
          },
          "publisher_original": {
            "type": "string",
            "example": "Star Wars Daily, by Allen Voivod",
            "description": "Plain text of this podcast's publisher name."
          },
          "publisher_highlighted": {
            "type": "string",
            "example": "<span class=\\\"ln-search-highlight\\\">Star</span> <span class=\\\"ln-search-highlight\\\">Wars</span> Daily, by Allen Voivod",
            "description": "Highlighted segment of this podcast's publisher name."
          }
        }
      },
      "description": "Podcast suggestions. It'll show up when the **show_podcasts** parameter is 1."
    }
  }
}
```   
</details>




### Fetch detailed meta data and episodes for a podcast by id

Function Name: **fetch_podcast_by_id**

Fetch detailed meta data and episodes for a specific podcast (up to 10 episodes each time).
You can use the **next_episode_pub_date** parameter to do pagination and fetch more episodes.


Example:
```python

from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)      

response = client.fetch_podcast_by_id(id='4d3fe717742d4963a85562e9f84d8c79')
            
print(response.json())

```

See all available parameters on the [API Docs page](https://www.listennotes.com/api/docs/#get-api-v2-podcasts-id).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "id": "4d3fe717742d4963a85562e9f84d8c79",
  "rss": "http://sw7x7.libsyn.com/rss",
  "type": "episodic",
  "email": "allen@sw7x7.com",
  "extra": {
    "url1": "",
    "url2": "",
    "url3": "",
    "google_url": "https://play.google.com/music/listen?u=0#/ps/I7gdcrqcmvhfnhh2cyqkcg32tkq",
    "spotify_url": "https://open.spotify.com/show/2rQJUP9Y3HxemiW3JHt9WV",
    "youtube_url": "https://www.youtube.com/sw7x7",
    "linkedin_url": "",
    "wechat_handle": "",
    "patreon_handle": "sw7x7",
    "twitter_handle": "",
    "facebook_handle": "sw7x7",
    "instagram_handle": ""
  },
  "image": "https://production.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-HN08OoDE7pc-AIg3cZVKCsL.1400x1400.jpg",
  "title": "Star Wars 7x7: The Daily Star Wars Podcast",
  "country": "United States",
  "website": "https://sw7x7.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
  "episodes": [
    {
      "id": "4e7c59e10e4640b98f2f3cb1777dbb43",
      "link": "https://sw7x7.libsyn.com/864-part-2-of-my-new-conversation-with-bobby-roberts?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/4e7c59e10e4640b98f2f3cb1777dbb43/",
      "image": "https://production.listennotes.com/podcasts/star-wars-7x7-the/864-part-2-of-my-new--vDBMTjY_mK-2WVsxtU0f3m.600x315.jpg",
      "title": "864: Part 2 of My (New) Conversation With Bobby Roberts",
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-7x7-the/864-part-2-of-my-new-yqjrzNDEXaS-2WVsxtU0f3m.300x157.jpg",
      "description": "<p>The second half of my latest conversation with Bobby Roberts, Podcast Emeritus from Full of Sith and now Star Wars \"Podcast Force Ghost at Large.\" Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1479110401571,
      "guid_from_rss": "bbada2b3a99054ce93b0eb95dd762b4d",
      "listennotes_url": "https://www.listennotes.com/e/4e7c59e10e4640b98f2f3cb1777dbb43/",
      "audio_length_sec": 2447,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/4e7c59e10e4640b98f2f3cb1777dbb43/#edit"
    },
    {
      "id": "9ae0e2e49a9c477191263df90adf7f3e",
      "link": "https://sw7x7.libsyn.com/863-a-new-conversation-with-bobby-roberts-part-1?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/9ae0e2e49a9c477191263df90adf7f3e/",
      "image": "https://production.listennotes.com/podcasts/star-wars-7x7-the/863-a-new-conversation-with-e_vHo9SM7ft-0YRBTlgiVeU.600x315.jpg",
      "title": "863: A (New) Conversation With Bobby Roberts, Part 1",
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-7x7-the/863-a-new-conversation-with-lcQsDS5uvYb-0YRBTlgiVeU.300x157.jpg",
      "description": "<p>An in-depth conversation about the Star Wars \"Story\" movies and so much more, featuring Bobby Roberts, Star Wars \"Podcast Force Ghost at Large.\" Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1479024001572,
      "guid_from_rss": "2c298fe68246aad30bd5afe0b79fdd76",
      "listennotes_url": "https://www.listennotes.com/e/9ae0e2e49a9c477191263df90adf7f3e/",
      "audio_length_sec": 2916,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/9ae0e2e49a9c477191263df90adf7f3e/#edit"
    },
    {
      "id": "98bcfa3fd1b44727913385938788bcc5",
      "link": "https://sw7x7.libsyn.com/862-assassin-clone-wars-briefing-season-3-episode-7?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/98bcfa3fd1b44727913385938788bcc5/",
      "image": "https://production.listennotes.com/podcasts/star-wars-7x7-the/862-assassin-clone-wars-lP94b2q5iOz-jEcMAdTntzs.600x315.jpg",
      "title": "862: \"Assassin\" - Clone Wars Briefing, Season 3, Episode 7",
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-7x7-the/862-assassin-clone-wars-Uh3E0GwOQRX-jEcMAdTntzs.300x157.jpg",
      "description": "<p>The beginnings of the true power of the Force, revealed in \"Assassin,\" season 3, episode 7 of the Star Wars: The Clone Wars cartoon series. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478937601573,
      "guid_from_rss": "6f64d1b37c661bbd066e773ae3b72d5e",
      "listennotes_url": "https://www.listennotes.com/e/98bcfa3fd1b44727913385938788bcc5/",
      "audio_length_sec": 636,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/98bcfa3fd1b44727913385938788bcc5/#edit"
    },
    {
      "id": "61d1de72f97e48e887c5d6280d3de384",
      "link": "https://sw7x7.libsyn.com/861-rogue-one-international-trailer-breakdown?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/61d1de72f97e48e887c5d6280d3de384/",
      "image": "https://production.listennotes.com/podcasts/star-wars-7x7-the/861-rogue-one-international-6rZOEiJHPpx-nGxaRC95V6o.600x315.jpg",
      "title": "861: Rogue One International Trailer Breakdown",
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-7x7-the/861-rogue-one-international-AFlEBXPHG6d-nGxaRC95V6o.300x157.jpg",
      "description": "<p>Surprise! An international trailer for Rogue One has dropped, and it includes new scenes, new dialogue, and some heavy foreshadowing about Jyn Erso's fate. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478851457574,
      "guid_from_rss": "10f042cf7346e078e201769b1097d651",
      "listennotes_url": "https://www.listennotes.com/e/61d1de72f97e48e887c5d6280d3de384/",
      "audio_length_sec": 1082,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/61d1de72f97e48e887c5d6280d3de384/#edit"
    },
    {
      "id": "53f5d00491134367ac3baf8c75b9a46b",
      "link": "https://sw7x7.libsyn.com/860-will-jyn-and-cassian-survive-rogue-one?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/53f5d00491134367ac3baf8c75b9a46b/",
      "image": "https://production.listennotes.com/podcasts/star-wars-7x7-the/860-will-jyn-and-cassian-VHAJQ1N57hE-l_3qXNfHAU0.600x315.jpg",
      "title": "860: Will Jyn and Cassian Survive Rogue One?",
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-7x7-the/860-will-jyn-and-cassian-k-2Si6HYjTP-l_3qXNfHAU0.300x157.jpg",
      "description": "<p>Today I conclude a two-episode set looking at the odds of survival for major Rogue One characters. Today: Jyn Erso, Cassian Andor, Bodhi Rook, and K-2SO. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478764801575,
      "guid_from_rss": "18062743dbffa4ce293686607ce30af4",
      "listennotes_url": "https://www.listennotes.com/e/53f5d00491134367ac3baf8c75b9a46b/",
      "audio_length_sec": 651,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/53f5d00491134367ac3baf8c75b9a46b/#edit"
    },
    {
      "id": "76c00b559f7d4f1c8be3ff1e2d808af9",
      "link": "https://sw7x7.libsyn.com/859-the-odds-who-will-survive-rogue-one?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/76c00b559f7d4f1c8be3ff1e2d808af9/",
      "image": "https://production.listennotes.com/podcasts/star-wars-7x7-the/859-the-odds-who-will-nM7l1BNPbIa-kprAXUCS8uQ.600x315.jpg",
      "title": "859: The Odds: Who Will Survive Rogue One?",
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-7x7-the/859-the-odds-who-will-RlXojiI5Wm6-kprAXUCS8uQ.300x157.jpg",
      "description": "<p>Will Galen Erso, Lyra Erso, Saw Gerrera, and Orson Krennic survive the events of Rogue One: A Star Wars Story? Starting a mini-series to look at the odds... Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478678401576,
      "guid_from_rss": "98e4d31b23bc7f48db490effe4d77e73",
      "listennotes_url": "https://www.listennotes.com/e/76c00b559f7d4f1c8be3ff1e2d808af9/",
      "audio_length_sec": 483,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/76c00b559f7d4f1c8be3ff1e2d808af9/#edit"
    },
    {
      "id": "62cdfe0b9ef64d1288a975a659dcf442",
      "link": "https://sw7x7.libsyn.com/858-together-new-rogue-one-commercial-dialogue?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/62cdfe0b9ef64d1288a975a659dcf442/",
      "image": "https://production.listennotes.com/podcasts/star-wars-7x7-the/858-together-new-rogue-one-TsLghBq5enX-WpFSsNUOzcL.600x315.jpg",
      "title": "858: \"Together\" - New Rogue One Commercial Dialogue",
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-7x7-the/858-together-new-rogue-one-dJF6XLmfYl4-WpFSsNUOzcL.300x157.jpg",
      "description": "<p>A new Rogue One commercial dropped Sunday, with some new dialogue that hints at the relationship between Jyn Erso, Saw Gerrera, the Rebellion, and the Partisans. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478592001577,
      "guid_from_rss": "c6dd42254e561130bf891f92e944041b",
      "listennotes_url": "https://www.listennotes.com/e/62cdfe0b9ef64d1288a975a659dcf442/",
      "audio_length_sec": 448,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/62cdfe0b9ef64d1288a975a659dcf442/#edit"
    },
    {
      "id": "a98c9cb497f04aec9e09cc50ce25ea59",
      "link": "https://sw7x7.libsyn.com/857-imperial-supercommandos-star-wars-rebels-season-3-episode-7?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/a98c9cb497f04aec9e09cc50ce25ea59/",
      "image": "https://production.listennotes.com/podcasts/star-wars-7x7-the/857-imperial-supercommandos-d0c7L1grbaI-L6bAOKCmyqt.600x315.jpg",
      "title": "857: \"Imperial Supercommandos\" - Star Wars Rebels Season 3, Episode 7",
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-7x7-the/857-imperial-supercommandos-OFpdNki02M_-L6bAOKCmyqt.300x157.jpg",
      "description": "<p>\"Imperial Supercommandos\" is Season 3, episode 7 of Star Wars Rebels, referring to Mandalorians serving the Empire. But can Fenn Rau be trusted, either? Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478505601578,
      "guid_from_rss": "007883a51d5ddc49b8b8d7fee80cb1ba",
      "listennotes_url": "https://www.listennotes.com/e/a98c9cb497f04aec9e09cc50ce25ea59/",
      "audio_length_sec": 494,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/a98c9cb497f04aec9e09cc50ce25ea59/#edit"
    },
    {
      "id": "e055bd1750a745a6adfcb70b935c03b7",
      "link": "https://sw7x7.libsyn.com/856-the-academy-clone-wars-briefing-season-3-episode-6?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/e055bd1750a745a6adfcb70b935c03b7/",
      "image": "https://production.listennotes.com/podcasts/star-wars-7x7-the/856-the-academy-clone-wars-6-EXfkbp4Sz-l6QpC-2RDTH.600x315.jpg",
      "title": "856: \"The Academy\" - Clone Wars Briefing, Season 3, Episode 6",
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-7x7-the/856-the-academy-clone-wars-x6_sqVGe-KS-l6QpC-2RDTH.300x157.jpg",
      "description": "<p>\"The Academy,\" Season 3 Episode 6 of the Clone Wars cartoon series, is a quieter episode that highlights the importance of Mandalore to the Star Wars franchise. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478415601579,
      "guid_from_rss": "f346a6e7575ab41197cacc6648070da2",
      "listennotes_url": "https://www.listennotes.com/e/e055bd1750a745a6adfcb70b935c03b7/",
      "audio_length_sec": 561,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/e055bd1750a745a6adfcb70b935c03b7/#edit"
    },
    {
      "id": "d602a45cdb524f3fac1effd79a61f828",
      "link": "https://sw7x7.libsyn.com/855-episode-viii-and-han-solo-movie-updates?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/d602a45cdb524f3fac1effd79a61f828/",
      "image": "https://production.listennotes.com/podcasts/star-wars-7x7-the/855-episode-viii-and-han-3Wkgr82DBxf-9vz38ko_X2s.600x315.jpg",
      "title": "855: Episode VIII and Han Solo Movie Updates",
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-7x7-the/855-episode-viii-and-han-naM8NWQxR19-9vz38ko_X2s.300x157.jpg",
      "description": "<p>Daisy Ridley says wait for Episode VIII for answers about Rey's parents. Bradford Young says the Han Solo movie won't be what you expect. Updates here... Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478329201580,
      "guid_from_rss": "89ac7c92db19f7d06f523eb2c093bde6",
      "listennotes_url": "https://www.listennotes.com/e/d602a45cdb524f3fac1effd79a61f828/",
      "audio_length_sec": 1103,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/d602a45cdb524f3fac1effd79a61f828/#edit"
    }
  ],
  "language": "English",
  "genre_ids": [
    86,
    67,
    68,
    82,
    100,
    101,
    160,
    138
  ],
  "itunes_id": 896354638,
  "publisher": "Star Wars 7x7",
  "thumbnail": "https://production.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-2LryqMj-sGP-AIg3cZVKCsL.300x300.jpg",
  "is_claimed": false,
  "description": "The Star Wars 7x7 Podcast is Rebel-rousing fun for everyday Jedi, generally between 7 and 14 minutes a day, always 7 days a week. Join host Allen Voivod for Star Wars news, history, interviews, trivia, and deep dives into the Star Wars story as told in movies, books, comics, games, cartoons, and more. Follow now for your daily dose of Star Wars joy. It's destiny unleashed! #SW7x7",
  "looking_for": {
    "guests": false,
    "cohosts": false,
    "sponsors": false,
    "cross_promotion": false
  },
  "listen_score": 48,
  "total_episodes": 2726,
  "listennotes_url": "https://www.listennotes.com/c/4d3fe717742d4963a85562e9f84d8c79/",
  "explicit_content": false,
  "latest_pub_date_ms": 1635145200000,
  "earliest_pub_date_ms": 1404637200000,
  "next_episode_pub_date": 1478329201580,
  "listen_score_global_rank": "1%"
}
```   
</details>



<details>
  <summary>Click to see response schema</summary>
  
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "example": "4d3fe717742d4963a85562e9f84d8c79",
      "description": "Podcast id."
    },
    "rss": {
      "type": "string",
      "example": "https://sw7x7.libsyn.com/rss",
      "description": "RSS url of this podcast. This field is available only in the PRO/ENTERPRISE plan."
    },
    "type": {
      "enum": [
        "episodic",
        "serial"
      ],
      "type": "string",
      "example": "episodic",
      "description": "The type of this podcast - episodic or serial."
    },
    "email": {
      "type": "string",
      "example": "hello@example.com",
      "description": "The email of this podcast's producer. This field is available only in the PRO/ENTERPRISE plan."
    },
    "extra": {
      "type": "object",
      "properties": {
        "url1": {
          "type": "string",
          "description": "Url affiliated with this podcast"
        },
        "url2": {
          "type": "string",
          "description": "Url affiliated with this podcast"
        },
        "url3": {
          "type": "string",
          "description": "Url affiliated with this podcast"
        },
        "google_url": {
          "type": "string",
          "example": "https://play.google.com/music/listen?u=0#/ps/I7gdcrqcmvhfnhh2cyqkcg32tkq",
          "description": "Google Podcasts url for this podcast"
        },
        "spotify_url": {
          "type": "string",
          "example": "https://open.spotify.com/show/2rQJUP9Y3HxemiW3JHt9WV",
          "description": "Spotify url for this podcast"
        },
        "youtube_url": {
          "type": "string",
          "example": "https://www.youtube.com/sw7x7",
          "description": "YouTube url affiliated with this podcast"
        },
        "linkedin_url": {
          "type": "string",
          "description": "LinkedIn url affiliated with this podcast"
        },
        "wechat_handle": {
          "type": "string",
          "description": "WeChat username affiliated with this podcast"
        },
        "patreon_handle": {
          "type": "string",
          "example": "sw7x7",
          "description": "Patreon username affiliated with this podcast"
        },
        "twitter_handle": {
          "type": "string",
          "example": "SW7x7podcast",
          "description": "Twitter username affiliated with this podcast"
        },
        "facebook_handle": {
          "type": "string",
          "example": "sw7x7",
          "description": "Facebook username affiliated with this podcast"
        },
        "instagram_handle": {
          "type": "string",
          "example": "sw7x7",
          "description": "Instagram username affiliated with this podcast"
        }
      }
    },
    "image": {
      "type": "string",
      "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
      "description": "Image url for this podcast's artwork. If you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
    },
    "title": {
      "type": "string",
      "example": "Star Wars 7x7 | Star Wars News, Interviews, and More!",
      "description": "Podcast name."
    },
    "country": {
      "type": "string",
      "example": "United States",
      "description": "The country where this podcast is produced."
    },
    "website": {
      "type": "string",
      "example": "http://sw7x7.com/",
      "description": "Website url of this podcast."
    },
    "episodes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "example": "4d82e50314174754a3b603912448e812",
            "description": "Episode id."
          },
          "link": {
            "type": "string",
            "example": "https://www.npr.org/2020/01/22/798532179/soleimanis-iran",
            "description": "Web link of this episode."
          },
          "audio": {
            "type": "string",
            "example": "https://www.listennotes.com/e/p/11b34041e804491b9704d11f283c74de/",
            "description": "Audio url of this episode, which can be played directly."
          },
          "image": {
            "type": "string",
            "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
            "description": "Image url for this podcast's artwork. If you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
          },
          "title": {
            "type": "string",
            "example": "Celebration Recap, Jason Fry and Christian Blauvelt Interviews \u2013 SWBW #101",
            "description": "Episode name."
          },
          "thumbnail": {
            "type": "string",
            "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
            "description": "Thumbnail image url for this podcast's artwork (300x300)."
          },
          "description": {
            "type": "string",
            "example": "<p>Disney chief Bob Iger shared news about Star Wars movies in 2020 and beyond, but some media outlets gave conflicting reports about it. Here's the real scoop. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>\n",
            "description": "Html of this episode's full description"
          },
          "pub_date_ms": {
            "type": "integer",
            "example": 1474873200000,
            "description": "Published date for this episode. In millisecond."
          },
          "listennotes_url": {
            "type": "string",
            "example": "https://www.listennotes.com/e/4d82e50314174754a3b603912448e812/",
            "description": "The url of this episode on [ListenNotes.com](https://www.ListenNotes.com)."
          },
          "audio_length_sec": {
            "type": "integer",
            "example": 567,
            "description": "Audio length of this episode. In seconds."
          },
          "explicit_content": {
            "type": "boolean",
            "example": false,
            "description": "Whether this podcast contains explicit language."
          },
          "maybe_audio_invalid": {
            "type": "boolean",
            "example": false,
            "description": "Whether or not this episode's audio is invalid. Podcasters may delete the original audio."
          },
          "listennotes_edit_url": {
            "type": "string",
            "example": "https://www.listennotes.com/e/11b34041e804491b9704d11f283c74de/#edit",
            "description": "Edit url of this episode where you can update the audio url if you find the audio is broken."
          }
        }
      }
    },
    "language": {
      "type": "string",
      "example": "English",
      "description": "The language of this podcast. You can get all supported languages from `GET /languages`."
    },
    "genre_ids": {
      "type": "array",
      "items": {
        "type": "integer",
        "description": "Genre ids."
      },
      "example": [
        138,
        86,
        160,
        68,
        82,
        100,
        101
      ]
    },
    "itunes_id": {
      "type": "integer",
      "example": 896354638,
      "description": "iTunes id for this podcast."
    },
    "publisher": {
      "type": "string",
      "example": "Planet Broadcasting",
      "description": "Podcast publisher name."
    },
    "thumbnail": {
      "type": "string",
      "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
      "description": "Thumbnail image url for this podcast's artwork (300x300)."
    },
    "is_claimed": {
      "type": "boolean",
      "example": true,
      "description": "Whether this podcast is claimed by its producer on [ListenNotes.com](https://www.ListenNotes.com)."
    },
    "description": {
      "type": "string",
      "example": "<p>The Star Wars 7x7 Podcast is Rebel-rousing fun for everyday Jedi, between 7 and 14 minutes a day, 7 days a week. Join host Allen Voivod for Star Wars news, history, interviews, trivia, and deep dives into the Star Wars story as told in movies, books, comics, games, cartoons, and more. Subscribe now for your daily dose of Star Wars joy. It's destiny unleashed!</p>",
      "description": "Html of this episode's full description"
    },
    "looking_for": {
      "type": "object",
      "properties": {
        "guests": {
          "type": "boolean",
          "example": true,
          "description": "Whether this podcast is looking for guests."
        },
        "cohosts": {
          "type": "boolean",
          "example": true,
          "description": "Whether this podcast is looking for cohosts."
        },
        "sponsors": {
          "type": "boolean",
          "example": true,
          "description": "Whether this podcast is looking for sponsors."
        },
        "cross_promotion": {
          "type": "boolean",
          "example": true,
          "description": "Whether this podcast is looking for cross promotion opportunities with other podcasts."
        }
      }
    },
    "listen_score": {
      "type": "integer",
      "example": 81,
      "description": "The estimated popularity score of a podcast compared to all other rss-based public podcasts in the world on a scale from 0 to 100.\nIf the score is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
    },
    "total_episodes": {
      "type": "integer",
      "example": 324,
      "description": "Total number of episodes in this podcast."
    },
    "listennotes_url": {
      "type": "string",
      "example": "https://www.listennotes.com/c/4d3fe717742d4963a85562e9f84d8c79/",
      "description": "The url of this podcast on [ListenNotes.com](https://www.ListenNotes.com)."
    },
    "explicit_content": {
      "type": "boolean",
      "example": false,
      "description": "Whether this podcast contains explicit language."
    },
    "latest_pub_date_ms": {
      "type": "integer",
      "example": 1557499770000,
      "description": "The published date of the latest episode of this podcast. In milliseconds"
    },
    "earliest_pub_date_ms": {
      "type": "integer",
      "example": 1470667902000,
      "description": "The published date of the oldest episode of this podcast. In milliseconds"
    },
    "next_episode_pub_date": {
      "type": "integer",
      "example": 1470667902000,
      "description": "Passed to the **next_episode_pub_date** parameter of `GET /podcasts/{id}` to paginate through episodes of that podcast."
    },
    "listen_score_global_rank": {
      "type": "string",
      "example": "0.5%",
      "description": "The estimated popularity ranking of a podcast compared to all other rss-based public podcasts in the world.\nFor example, if the value is 0.5%, then this podcast is one of the top 0.5% most popular shows out of all podcasts globally, ranked by Listen Score.\nIf the ranking is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
    }
  }
}
```   
</details>




### Fetch detailed meta data for an episode by id

Function Name: **fetch_episode_by_id**

Fetch detailed meta data for a specific episode.

Example:
```python

from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)      

response = client.fetch_episode_by_id(
    id='6b6d65930c5a4f71b254465871fed370', show_transcript=1)
            
print(response.json())

```

See all available parameters on the [API Docs page](https://www.listennotes.com/api/docs/#get-api-v2-episodes-id).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "id": "6b6d65930c5a4f71b254465871fed370",
  "link": "https://audioboom.com/posts/7742178?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
  "audio": "https://www.listennotes.com/e/p/6b6d65930c5a4f71b254465871fed370/",
  "image": "https://production.listennotes.com/podcasts/a-winning-mindset/16-arly-velasquez-on-xPbM1hpZqFK-c5khPVKzowB.1400x1400.jpg",
  "title": "16: Arly Velasquez on Managing Risk",
  "podcast": {
    "id": "073a66b496824a5d9e80d52621f372dc",
    "rss": "https://audioboom.com/channels/5031508.rss",
    "type": "episodic",
    "email": "ipc.media@paralympic.org",
    "extra": {
      "url1": "https://www.paralympic.org/a-winning-mindset-lessons-from-the-paralympicsz",
      "url2": "",
      "url3": "",
      "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9hdWRpb2Jvb20uY29tL2NoYW5uZWxzLzUwMzE1MDgucnNz",
      "spotify_url": "https://open.spotify.com/show/5yDllc2ceZxQR7bJqIex5l",
      "youtube_url": "https://www.youtube.com/paralympics",
      "linkedin_url": "https://www.linkedin.com/company/international-paralympic-committee",
      "wechat_handle": "",
      "patreon_handle": "",
      "twitter_handle": "paralympics",
      "facebook_handle": "paralympics",
      "instagram_handle": "paralympics"
    },
    "image": "https://production.listennotes.com/podcasts/a-winning-mindset-lessons-from-the-w5rmBZaXpoK-BktA4YUzNbu.1400x1400.jpg",
    "title": "A Winning Mindset",
    "country": "Germany",
    "website": "https://www.paralympic.org/a-winning-mindset-lessons-from-the-paralympics?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
    "language": "English",
    "genre_ids": [
      77,
      122,
      217,
      111,
      88,
      191,
      181,
      90
    ],
    "itunes_id": 1527733477,
    "publisher": "A Winning Mindset: Lessons From The Paralympics",
    "thumbnail": "https://production.listennotes.com/podcasts/a-winning-mindset-lessons-from-the-W7yPpwRV6_z-BktA4YUzNbu.300x300.jpg",
    "is_claimed": true,
    "description": "WINNER OF BEST BRANDED PODCAST AT THE 2021 WEBBY AWARDS!\nWINNER OF BEST PODCAST AT 2021 DIGIDAY MEDIA EUROPE AWARDS!\nWINNER OF BEST SPORT PODCAST AT 2021 SPORT INDUSTRY AWARDS!\n\nA Winning Mindset is a fascinating journey into the minds of Paralympians, as they share experiences that can benefit your own personal and professional life.\u00a0\n\nThis empowering weekly series is the official podcast of the International Paralympic Committee, in partnership with Allianz.\u00a0\n\nEach podcast provides a platform for Para athletes to talk about their empowering and inspirational stories, sporting lives allows each athlete to showcase their personalities.\n\nEpisodes go beyond Paralympic stories by covering a range of educational, confidence and self-improvement themes.\u00a0 Athletes also tackle subjects that are close to their hearts and of interest to fans. Issues explored include activism, leadership, motivation, changing attitudes, overcoming failure, mental health, resilience, positivity, diversity and inclusion, body confidence, compassion, decision-making, communication, self-understanding, happiness, organisation and efficiency techniques, combining family with a sport career, parenting, the power of purpose and a personal vision, assertiveness, empathy, friendship and teamwork.\u00a0\n\nA Winning Mindset also explores the progress and transformational impact made by the Paralympic Movement so far in making for a more inclusive world. How Para sport has helped to change attitudes, increase mobility and accessibility and create more opportunities for people with a disability whether to have an education, play sport, have access to healthcare or employment.\n\nThe Paralympic podcast series is presented by British broadcaster Andy Stevenson, who has reported on the Paralympic Games since 2012 for BBC and Channel 4.\n\nFeatured athletes have so far included Tatyana McFadden, Jonnie Peacock and Arly Velasquez.",
    "looking_for": {
      "guests": false,
      "cohosts": false,
      "sponsors": false,
      "cross_promotion": true
    },
    "listen_score": 41,
    "total_episodes": 25,
    "listennotes_url": "https://www.listennotes.com/c/073a66b496824a5d9e80d52621f372dc/",
    "explicit_content": false,
    "latest_pub_date_ms": 1630040400000,
    "earliest_pub_date_ms": 1598436120022,
    "listen_score_global_rank": "1.5%"
  },
  "thumbnail": "https://production.listennotes.com/podcasts/a-winning-mindset/16-arly-velasquez-on-ftCxqnUg0Sr-c5khPVKzowB.300x300.jpg",
  "transcript": "\nA Paralympic skiier from Mexico isn\u2019t something you expect to see too often. But Arly Velasquez doesn\u2019t believe in expectations. \n\nVelasquez, one of a select few to ever represent Mexico at a Winter Paralympic Games, discusses the role of risk in his life - and how we can all learn to manage it.\u00a0\n\n\u201cI have developed because of taking decisions where I have no idea. It\u2019s a matter of 'does it feel right or not?'\" he said.\n\n\"I don't see it as a risk, I see that when I am in the mountain on a sit ski, I just feel the most free.\u201d\u00a0\n\nThe former BMX champion also discusses the risks he took when leaving Mexico on the spur of a moment, building a new life on the ski slopes in Canada. \u00a0\n\n\u201c(Skiing) gave me the belief to go back to Mexico, sell all my stuff,\u00a0 sell my car and pretty much fly to the border,\" he said.\u00a0\n\n\"It's very, rare that there are moments in your life where you are feeling and your gut tells you that you are in the right place. That you are doing the right thing and that it's something that you want to keep doing in your life. That's what I felt for the first time.\u201d\u00a0\n\nLearning topics for this episode include managing risk, how to build a brand, self-understanding, defiance, thrill-seeking and exploration. \u00a0\n\nAllianz is a long-standing partner of the International Paralympic Committee. Together, we\u2019re proud to bring you A Winning Mindset: Lessons From The Paralympics. We aim to help you move forward in all aspects of your personal and professional life.\u00a0\n\nBy hearing from Paralympic stars, you\u2019ll be introduced to stories that inspire and change the way you think. Stories of facing life\u2019s challenges with confidence, determination and excellence, and the true power of having the right team behind you.\u00a0",
  "description": "<div>\n<strong>A Paralympic skiier from Mexico isn\u2019t something you expect to see too often. But Arly Velasquez doesn\u2019t believe in expectations. </strong><br>\n<br>\nVelasquez, one of a select few to ever represent Mexico at a Winter Paralympic Games, discusses the role of risk in his life - and how we can all learn to manage it.\u00a0<br>\n<br>\n\u201cI have developed because of taking decisions where I have no idea. It\u2019s a matter of 'does it feel right or not?'\" he said.<br>\n<br>\n\"I don't see it as a risk, I see that when I am in the mountain on a sit ski, I just feel the most free.\u201d\u00a0<br>\n<br>\nThe former BMX champion also discusses the risks he took when leaving Mexico on the spur of a moment, building a new life on the ski slopes in Canada. \u00a0<br>\n<br>\n\u201c(Skiing) gave me the belief to go back to Mexico, sell all my stuff,\u00a0 sell my car and pretty much fly to the border,\" he said.\u00a0<br>\n<br>\n\"It's very, rare that there are moments in your life where you are feeling and your gut tells you that you are in the right place. That you are doing the right thing and that it's something that you want to keep doing in your life. That's what I felt for the first time.\u201d\u00a0<br>\n<br>\nLearning topics for this episode include managing risk, how to build a brand, self-understanding, defiance, thrill-seeking and exploration. \u00a0<br>\n<br>\nAllianz is a long-standing partner of the International Paralympic Committee. Together, we\u2019re proud to bring you A Winning Mindset: Lessons From The Paralympics. We aim to help you move forward in all aspects of your personal and professional life.\u00a0<br>\n<br>\nBy hearing from Paralympic stars, you\u2019ll be introduced to stories that inspire and change the way you think. Stories of facing life\u2019s challenges with confidence, determination and excellence, and the true power of having the right team behind you.\u00a0</div>",
  "pub_date_ms": 1607054220006,
  "guid_from_rss": "tag:audioboom.com,2020-12-02:/posts/7742178",
  "listennotes_url": "https://www.listennotes.com/e/6b6d65930c5a4f71b254465871fed370/",
  "audio_length_sec": 1637,
  "explicit_content": false,
  "maybe_audio_invalid": false,
  "listennotes_edit_url": "https://www.listennotes.com/e/6b6d65930c5a4f71b254465871fed370/#edit"
}
```   
</details>



<details>
  <summary>Click to see response schema</summary>
  
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "example": "4d82e50314174754a3b603912448e812",
      "description": "Episode id."
    },
    "link": {
      "type": "string",
      "example": "https://www.npr.org/2020/01/22/798532179/soleimanis-iran",
      "description": "Web link of this episode."
    },
    "audio": {
      "type": "string",
      "example": "https://www.listennotes.com/e/p/11b34041e804491b9704d11f283c74de/",
      "description": "Audio url of this episode, which can be played directly."
    },
    "image": {
      "type": "string",
      "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
      "description": "Image url for this episode.\nIf an episode doesn't have its own image, then this field would be the url of the podcast artwork image.\nIf you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
    },
    "title": {
      "type": "string",
      "example": "Celebration Recap, Jason Fry and Christian Blauvelt Interviews \u2013 SWBW #101",
      "description": "Episode name."
    },
    "podcast": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "example": "4d3fe717742d4963a85562e9f84d8c79",
          "description": "Podcast id."
        },
        "rss": {
          "type": "string",
          "example": "https://sw7x7.libsyn.com/rss",
          "description": "RSS url of this podcast. This field is available only in the PRO/ENTERPRISE plan."
        },
        "type": {
          "enum": [
            "episodic",
            "serial"
          ],
          "type": "string",
          "example": "episodic",
          "description": "The type of this podcast - episodic or serial."
        },
        "email": {
          "type": "string",
          "example": "hello@example.com",
          "description": "The email of this podcast's producer. This field is available only in the PRO/ENTERPRISE plan."
        },
        "extra": {
          "type": "object",
          "properties": {
            "url1": {
              "type": "string",
              "description": "Url affiliated with this podcast"
            },
            "url2": {
              "type": "string",
              "description": "Url affiliated with this podcast"
            },
            "url3": {
              "type": "string",
              "description": "Url affiliated with this podcast"
            },
            "google_url": {
              "type": "string",
              "example": "https://play.google.com/music/listen?u=0#/ps/I7gdcrqcmvhfnhh2cyqkcg32tkq",
              "description": "Google Podcasts url for this podcast"
            },
            "spotify_url": {
              "type": "string",
              "example": "https://open.spotify.com/show/2rQJUP9Y3HxemiW3JHt9WV",
              "description": "Spotify url for this podcast"
            },
            "youtube_url": {
              "type": "string",
              "example": "https://www.youtube.com/sw7x7",
              "description": "YouTube url affiliated with this podcast"
            },
            "linkedin_url": {
              "type": "string",
              "description": "LinkedIn url affiliated with this podcast"
            },
            "wechat_handle": {
              "type": "string",
              "description": "WeChat username affiliated with this podcast"
            },
            "patreon_handle": {
              "type": "string",
              "example": "sw7x7",
              "description": "Patreon username affiliated with this podcast"
            },
            "twitter_handle": {
              "type": "string",
              "example": "SW7x7podcast",
              "description": "Twitter username affiliated with this podcast"
            },
            "facebook_handle": {
              "type": "string",
              "example": "sw7x7",
              "description": "Facebook username affiliated with this podcast"
            },
            "instagram_handle": {
              "type": "string",
              "example": "sw7x7",
              "description": "Instagram username affiliated with this podcast"
            }
          }
        },
        "image": {
          "type": "string",
          "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
          "description": "Image url for this podcast's artwork. If you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
        },
        "title": {
          "type": "string",
          "example": "Star Wars 7x7 | Star Wars News, Interviews, and More!",
          "description": "Podcast name."
        },
        "country": {
          "type": "string",
          "example": "United States",
          "description": "The country where this podcast is produced."
        },
        "website": {
          "type": "string",
          "example": "http://sw7x7.com/",
          "description": "Website url of this podcast."
        },
        "language": {
          "type": "string",
          "example": "English",
          "description": "The language of this podcast. You can get all supported languages from `GET /languages`."
        },
        "genre_ids": {
          "type": "array",
          "items": {
            "type": "integer",
            "description": "Genre ids."
          },
          "example": [
            138,
            86,
            160,
            68,
            82,
            100,
            101
          ]
        },
        "itunes_id": {
          "type": "integer",
          "example": 896354638,
          "description": "iTunes id for this podcast."
        },
        "publisher": {
          "type": "string",
          "example": "Planet Broadcasting",
          "description": "Podcast publisher name."
        },
        "thumbnail": {
          "type": "string",
          "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
          "description": "Thumbnail image url for this podcast's artwork (300x300)."
        },
        "is_claimed": {
          "type": "boolean",
          "example": true,
          "description": "Whether this podcast is claimed by its producer on [ListenNotes.com](https://www.ListenNotes.com)."
        },
        "description": {
          "type": "string",
          "example": "<p>The Star Wars 7x7 Podcast is Rebel-rousing fun for everyday Jedi, between 7 and 14 minutes a day, 7 days a week. Join host Allen Voivod for Star Wars news, history, interviews, trivia, and deep dives into the Star Wars story as told in movies, books, comics, games, cartoons, and more. Subscribe now for your daily dose of Star Wars joy. It's destiny unleashed!</p>",
          "description": "Html of this episode's full description"
        },
        "looking_for": {
          "type": "object",
          "properties": {
            "guests": {
              "type": "boolean",
              "example": true,
              "description": "Whether this podcast is looking for guests."
            },
            "cohosts": {
              "type": "boolean",
              "example": true,
              "description": "Whether this podcast is looking for cohosts."
            },
            "sponsors": {
              "type": "boolean",
              "example": true,
              "description": "Whether this podcast is looking for sponsors."
            },
            "cross_promotion": {
              "type": "boolean",
              "example": true,
              "description": "Whether this podcast is looking for cross promotion opportunities with other podcasts."
            }
          }
        },
        "listen_score": {
          "type": "integer",
          "example": 81,
          "description": "The estimated popularity score of a podcast compared to all other rss-based public podcasts in the world on a scale from 0 to 100.\nIf the score is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
        },
        "total_episodes": {
          "type": "integer",
          "example": 324,
          "description": "Total number of episodes in this podcast."
        },
        "listennotes_url": {
          "type": "string",
          "example": "https://www.listennotes.com/c/4d3fe717742d4963a85562e9f84d8c79/",
          "description": "The url of this podcast on [ListenNotes.com](https://www.ListenNotes.com)."
        },
        "explicit_content": {
          "type": "boolean",
          "example": false,
          "description": "Whether this podcast contains explicit language."
        },
        "latest_pub_date_ms": {
          "type": "integer",
          "example": 1557499770000,
          "description": "The published date of the latest episode of this podcast. In milliseconds"
        },
        "earliest_pub_date_ms": {
          "type": "integer",
          "example": 1470667902000,
          "description": "The published date of the oldest episode of this podcast. In milliseconds"
        },
        "listen_score_global_rank": {
          "type": "string",
          "example": "0.5%",
          "description": "The estimated popularity ranking of a podcast compared to all other rss-based public podcasts in the world.\nFor example, if the value is 0.5%, then this podcast is one of the top 0.5% most popular shows out of all podcasts globally, ranked by Listen Score.\nIf the ranking is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
        }
      }
    },
    "thumbnail": {
      "type": "string",
      "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
      "description": "Thumbnail image (300x300) url for this episode.\nIf an episode doesn't have its own image, then this field would be the url of the podcast artwork thumbnail image.\n"
    },
    "transcript": {
      "type": "string",
      "example": "00:00:07 Welcome to this podcast...\n",
      "description": "The transcript of this episode, in plain text (with the newline character \\n). If there's not transcript, it is null. This field is available only in the PRO/ENTERPRISE plan."
    },
    "description": {
      "type": "string",
      "example": "<p>Disney chief Bob Iger shared news about Star Wars movies in 2020 and beyond, but some media outlets gave conflicting reports about it. Here's the real scoop. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>\n",
      "description": "Html of this episode's full description"
    },
    "pub_date_ms": {
      "type": "integer",
      "example": 1474873200000,
      "description": "Published date for this episode. In millisecond."
    },
    "listennotes_url": {
      "type": "string",
      "example": "https://www.listennotes.com/e/4d82e50314174754a3b603912448e812/",
      "description": "The url of this episode on [ListenNotes.com](https://www.ListenNotes.com)."
    },
    "audio_length_sec": {
      "type": "integer",
      "example": 567,
      "description": "Audio length of this episode. In seconds."
    },
    "explicit_content": {
      "type": "boolean",
      "example": false,
      "description": "Whether this podcast contains explicit language."
    },
    "maybe_audio_invalid": {
      "type": "boolean",
      "example": false,
      "description": "Whether or not this episode's audio is invalid. Podcasters may delete the original audio."
    },
    "listennotes_edit_url": {
      "type": "string",
      "example": "https://www.listennotes.com/e/11b34041e804491b9704d11f283c74de/#edit",
      "description": "Edit url of this episode where you can update the audio url if you find the audio is broken."
    }
  }
}
```   
</details>




### Fetch a list of supported languages for podcasts

Function Name: **fetch_podcast_languages**

Get a list of languages that are supported in Listen Notes database. You can use the language string as query parameter in `GET /search`.


Example:
```python

from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)      

response = client.fetch_podcast_languages()
            
print(response.json())

```

See all available parameters on the [API Docs page](https://www.listennotes.com/api/docs/#get-api-v2-languages).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "languages": [
    "Any language",
    "Afar",
    "Abkhazian",
    "Afrikaans",
    "Akan",
    "Albanian",
    "Arabic",
    "Azerbaijani",
    "Bambara",
    "Bashkir",
    "Basque",
    "Belarusian",
    "Bengali",
    "Bosnian",
    "Bulgarian",
    "Burmese",
    "Catalan",
    "Chamorro",
    "Chinese",
    "Croatian",
    "Czech",
    "Danish",
    "Dutch",
    "English",
    "Estonian",
    "Faeroese",
    "Farsi",
    "Finnish",
    "French",
    "Gaelic",
    "Galician",
    "German",
    "Greek",
    "Hebrew",
    "Hindi",
    "Hungarian",
    "Icelandic",
    "Indonesian",
    "Irish",
    "Italian",
    "Japanese",
    "Khmer",
    "Kirghiz",
    "Korean",
    "Latin",
    "Latvian",
    "Lithuanian",
    "Macedonian",
    "Malay",
    "Malayalam",
    "Marathi",
    "Mongolian",
    "Nepali",
    "Northern Sami",
    "Norwegian",
    "Polish",
    "Portuguese",
    "Romanian",
    "Russian",
    "Serbian",
    "Singhalese",
    "Slovak",
    "Slovenian",
    "Spanish",
    "Swahili",
    "Swedish",
    "Tamil",
    "Telugu",
    "Thai",
    "Turkish",
    "Twi",
    "Ukranian",
    "Urdu",
    "Vietnamese"
  ]
}
```   
</details>



<details>
  <summary>Click to see response schema</summary>
  
```json
{
  "type": "object",
  "required": [
    "languages"
  ],
  "properties": {
    "languages": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "example": [
        "Any language",
        "Afar",
        "Abkhazian",
        "Afrikaans",
        "Akan",
        "Albanian",
        "Arabic",
        "Azerbaijani",
        "Bambara",
        "Bashkir",
        "Basque",
        "Belarusian",
        "Bulgarian",
        "Catalan",
        "Chamorro",
        "Chinese",
        "Croatian",
        "Czech",
        "Danish",
        "Dutch",
        "English",
        "Estonian",
        "Faeroese",
        "Finnish",
        "French",
        "Gaelic",
        "Galician",
        "German",
        "Greek"
      ]
    }
  }
}
```   
</details>




### Fetch a list of podcast genres

Function Name: **fetch_podcast_genres**

Get a list of podcast genres that are supported in Listen Notes.
The genre id can be passed to other endpoints as a parameter to get podcasts in a specific genre,
e.g., `GET /best_podcasts`, `GET /search`...
You may want to cache the list of genres on the client side.


Example:
```python

from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)      

response = client.fetch_podcast_genres(top_level_only=1)
            
print(response.json())

```

See all available parameters on the [API Docs page](https://www.listennotes.com/api/docs/#get-api-v2-genres).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "genres": [
    {
      "id": 144,
      "name": "Personal Finance",
      "parent_id": 67
    },
    {
      "id": 151,
      "name": "Locally Focused",
      "parent_id": 67
    },
    {
      "id": 68,
      "name": "TV & Film",
      "parent_id": 67
    },
    {
      "id": 127,
      "name": "Technology",
      "parent_id": 67
    },
    {
      "id": 135,
      "name": "True Crime",
      "parent_id": 67
    },
    {
      "id": 100,
      "name": "Arts",
      "parent_id": 67
    },
    {
      "id": 93,
      "name": "Business",
      "parent_id": 67
    },
    {
      "id": 133,
      "name": "Comedy",
      "parent_id": 67
    },
    {
      "id": 111,
      "name": "Education",
      "parent_id": 67
    },
    {
      "id": 168,
      "name": "Fiction",
      "parent_id": 67
    },
    {
      "id": 117,
      "name": "Government",
      "parent_id": 67
    },
    {
      "id": 88,
      "name": "Health & Fitness",
      "parent_id": 67
    },
    {
      "id": 125,
      "name": "History",
      "parent_id": 67
    },
    {
      "id": 132,
      "name": "Kids & Family",
      "parent_id": 67
    },
    {
      "id": 82,
      "name": "Leisure",
      "parent_id": 67
    },
    {
      "id": 134,
      "name": "Music",
      "parent_id": 67
    },
    {
      "id": 99,
      "name": "News",
      "parent_id": 67
    },
    {
      "id": 69,
      "name": "Religion & Spirituality",
      "parent_id": 67
    },
    {
      "id": 107,
      "name": "Science",
      "parent_id": 67
    },
    {
      "id": 122,
      "name": "Society & Culture",
      "parent_id": 67
    },
    {
      "id": 77,
      "name": "Sports",
      "parent_id": 67
    }
  ]
}
```   
</details>



<details>
  <summary>Click to see response schema</summary>
  
```json
{
  "type": "object",
  "required": [
    "genres"
  ],
  "properties": {
    "genres": {
      "type": "array",
      "items": {
        "type": "object",
        "example": {
          "id": 140,
          "name": "Web Design",
          "parent_id": 127
        },
        "properties": {
          "id": {
            "type": "integer",
            "example": 93,
            "description": "Genre id"
          },
          "name": {
            "type": "string",
            "example": "Business",
            "description": "Genre name."
          },
          "parent_id": {
            "type": "integer",
            "example": 95,
            "description": "Parent genre id."
          }
        }
      }
    }
  }
}
```   
</details>




### Fetch a list of best podcasts by genre

Function Name: **fetch_best_podcasts**

Get a list of curated best podcasts by genre,
which are curated by Listen Notes staffs based on various signals from the Internet, e.g.,
top charts on other podcast platforms, recommendations from mainstream media,
user activities on listennotes.com...
You can get the genre ids from `GET /genres` endpoint.
This endpoint returns same data as https://www.listennotes.com/best-podcasts/


Example:
```python

from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)      

response = client.fetch_best_podcasts(genre_id=93, page=2, region='us')
            
print(response.json())

```

See all available parameters on the [API Docs page](https://www.listennotes.com/api/docs/#get-api-v2-best_podcasts).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "id": 93,
  "name": "Business",
  "total": 644,
  "has_next": true,
  "podcasts": [
    {
      "id": "0d362b13399240de97602ef614acdcbc",
      "rss": "https://feeds.megaphone.fm/startup",
      "type": "episodic",
      "email": "admin@gimletmedia.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://play.google.com/music/m/Ihs2lujac7unjyp2u7hp6ale7hq?t=StartUp_Podcast",
        "spotify_url": "https://open.spotify.com/show/5CnDmMUG0S5bSSw612fs8C",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "podcaststartup",
        "facebook_handle": "hearstartup",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/startup-podcast-gimlet-14zU0c_MOmv-n9PpCBTQvoJ.1400x1400.jpg",
      "title": "StartUp Podcast",
      "country": "United States",
      "website": "https://www.gimletmedia.com/startup?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        171,
        127,
        68,
        97,
        94,
        157
      ],
      "itunes_id": 913805339,
      "publisher": "Gimlet",
      "thumbnail": "https://production.listennotes.com/podcasts/startup-podcast-gimlet-8If7QBKU5jb-n9PpCBTQvoJ.300x300.jpg",
      "is_claimed": false,
      "description": "A series about what it's really like to start a business.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 76,
      "total_episodes": 153,
      "listennotes_url": "https://www.listennotes.com/c/0d362b13399240de97602ef614acdcbc/",
      "explicit_content": false,
      "latest_pub_date_ms": 1598004000000,
      "earliest_pub_date_ms": 1396742400000,
      "listen_score_global_rank": "0.01%"
    },
    {
      "id": "34beae8ad8fd4b299196f413b8270a30",
      "rss": "https://feeds.feedburner.com/WorklifeWithAdamGrant",
      "type": "episodic",
      "email": "podcasts@ted.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5mZWVkYnVybmVyLmNvbS9Xb3JrbGlmZVdpdGhBZGFtR3JhbnQ=",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "https://www.linkedin.com/in/adammgrant/",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "AdamMGrant",
        "facebook_handle": "AdamMGrant",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/worklife-with-adam-grant-ted-KgaXjFPEoVc.1400x1400.jpg",
      "title": "WorkLife with Adam Grant",
      "country": "United States",
      "website": "https://www.ted.com/podcasts/worklife?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        111,
        97,
        67
      ],
      "itunes_id": 1346314086,
      "publisher": "TED",
      "thumbnail": "https://production.listennotes.com/podcasts/worklife-with-adam-grant-ted-KgaXjFPEoVc.300x300.jpg",
      "is_claimed": false,
      "description": "\n      <p>You spend a quarter of your life at work. You should enjoy it! Organizational psychologist Adam Grant takes you inside the minds of some of the world\u2019s most unusual professionals to discover the keys to a better work life. From learning how to love your rivals to harnessing the power of frustration, one thing\u2019s for sure: You\u2019ll never see your job the same way again. Produced in partnership with Transmitter Media.</p>\n    ",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 76,
      "total_episodes": 56,
      "listennotes_url": "https://www.listennotes.com/c/34beae8ad8fd4b299196f413b8270a30/",
      "explicit_content": false,
      "latest_pub_date_ms": 1634659959000,
      "earliest_pub_date_ms": 1518044524053,
      "listen_score_global_rank": "0.01%"
    },
    {
      "id": "ee84d7d11875465fb89487675ff5425d",
      "rss": "https://edmylett.libsyn.com/rss",
      "type": "episodic",
      "email": "edwardmylett@yahoo.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9lZG15bGV0dC5saWJzeW4uY29tL3Jzcw==",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "EdMylett",
        "facebook_handle": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-ed-mylett-show-ed-mylett-FIRVobOKiqj-PEUIT9RBhZD.1400x1400.jpg",
      "title": "THE ED MYLETT SHOW",
      "country": "United States",
      "website": "http://edmylett.libsyn.com/podcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        157,
        67,
        88,
        89,
        90,
        93
      ],
      "itunes_id": 1181233130,
      "publisher": "Ed Mylett",
      "thumbnail": "https://production.listennotes.com/podcasts/the-ed-mylett-show-ed-mylett-FR-34rvs_So-PEUIT9RBhZD.300x300.jpg",
      "is_claimed": false,
      "description": "The Ed Mylett Show showcases the greatest peak-performers across all industries in one place, sharing their journey, knowledge and thought leadership. With Ed Mylett and featured guests in almost every industry including business, health, collegiate and professional sports, politics, entrepreneurship, science, and entertainment, you'll find motivation, inspiration and practical steps to help you become the best version of you!",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 74,
      "total_episodes": 209,
      "listennotes_url": "https://www.listennotes.com/c/ee84d7d11875465fb89487675ff5425d/",
      "explicit_content": false,
      "latest_pub_date_ms": 1634637600000,
      "earliest_pub_date_ms": 1477433232151,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "fc6d33e22b7f4db38df3bb64a9a8c227",
      "rss": "https://tonyrobbins.libsyn.com/rss",
      "type": "episodic",
      "email": "tonyrobbins.social@gmail.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly90b255cm9iYmlucy5saWJzeW4uY29tL3Jzcw==",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "tonyrobbins",
        "facebook_handle": "TonyRobbins",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-tony-robbins-podcast-tony-robbins-eh9wNFJcP1W.1400x1400.jpg",
      "title": "The Tony Robbins Podcast",
      "country": "United States",
      "website": "http://tonyrobbins.com/podcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        90,
        93,
        181,
        157,
        78,
        67,
        97,
        111,
        144
      ],
      "itunes_id": 1098413063,
      "publisher": "Tony Robbins",
      "thumbnail": "https://production.listennotes.com/podcasts/the-tony-robbins-podcast-tony-robbins-eh9wNFJcP1W.300x300.jpg",
      "is_claimed": false,
      "description": "\u201cWhy live an ordinary life, when you can live an extraordinary one?\u201d Tony Robbins, the #1 Life and Business Strategist, has helped over 50 million people from 100 countries create real and lasting change in their lives. In this podcast, he shares proven strategies and tactics so you, too, can achieve massive results in your business, relationships, health and finances. In addition to excerpts from his signature events and other exclusive, never-before-released audio content, Tony and his team also conduct deeply insightful interviews with the most prominent masterminds and experts on the global stage.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 74,
      "total_episodes": 145,
      "listennotes_url": "https://www.listennotes.com/c/fc6d33e22b7f4db38df3bb64a9a8c227/",
      "explicit_content": false,
      "latest_pub_date_ms": 1632249685000,
      "earliest_pub_date_ms": 1459373820099,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "ed79b615ed074204bc4702b56a264a78",
      "rss": "http://thelifecoachschool.libsyn.com/rss",
      "type": "episodic",
      "email": "brooke@thelifecoachschool.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cDovL3RoZWxpZmVjb2FjaHNjaG9vbC5saWJzeW4uY29tL3Jzcw==",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "brookecastillo",
        "facebook_handle": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-life-coach-school-podcast-brooke-castillo-1QLMA8ydOIg-V5of7JlG_RD.1400x1400.jpg",
      "title": "The Life Coach School Podcast",
      "country": "United States",
      "website": "http://www.thelifecoachschool.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        88,
        90,
        93,
        94,
        111,
        115
      ],
      "itunes_id": 870239631,
      "publisher": "Brooke Castillo",
      "thumbnail": "https://production.listennotes.com/podcasts/the-life-coach-school-podcast-brooke-castillo-vMtPswHLm2F-V5of7JlG_RD.300x300.jpg",
      "is_claimed": false,
      "description": "The Life Coach School Podcast is your go-to resource for learning, growing, and becoming certified as a Life Coach & Weight Loss Coach. Through this podcast, you'll hear directly from the Master Coach Brooke Castillo to help you better understand life coaching, the required skills and mindsets, and how we focus on serving the client to get them the results they seek.  At The Life Coach School, we offer a thorough and intense certification course that produces some of the most successful coaches coaching today. Learn more at TheLifeCoachSchool.com.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 74,
      "total_episodes": 418,
      "listennotes_url": "https://www.listennotes.com/c/ed79b615ed074204bc4702b56a264a78/",
      "explicit_content": false,
      "latest_pub_date_ms": 1634806800000,
      "earliest_pub_date_ms": 1398606925393,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "5f237b79824e4dfb8355f6dff9b1c542",
      "rss": "https://feeds.npr.org/510325/podcast.xml",
      "type": "episodic",
      "email": "podcasts@npr.org",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5ucHIub3JnLzUxMDMyNS9wb2RjYXN0LnhtbA==",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "planetmoney",
        "facebook_handle": "planetmoney",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-indicator-from-planet-money-npr-uFAcdQm6ILr-G2EDjFO-TLA.1400x1400.jpg",
      "title": "The Indicator from Planet Money",
      "country": "United States",
      "website": "https://www.npr.org/sections/money/567724614/the-indicator?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        93,
        171,
        99,
        144,
        98
      ],
      "itunes_id": 1320118593,
      "publisher": "NPR",
      "thumbnail": "https://production.listennotes.com/podcasts/the-indicator-from-planet-money-npr-67Cryeo5VYn-G2EDjFO-TLA.300x300.jpg",
      "is_claimed": false,
      "description": "A little show about big ideas. From the people who make <em>Planet Money</em>, <em>The Indicator</em> helps you make sense of what's happening today. It's a quick hit of insight into work, business, the economy, and everything else. Listen weekday afternoons.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 74,
      "total_episodes": 862,
      "listennotes_url": "https://www.listennotes.com/c/5f237b79824e4dfb8355f6dff9b1c542/",
      "explicit_content": false,
      "latest_pub_date_ms": 1635201989000,
      "earliest_pub_date_ms": 1527108300299,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "2184bada602d431689dbb4c6c1bc5839",
      "rss": "https://feeds.simplecast.com/atgtihd0",
      "type": "episodic",
      "email": "interactive@life.church",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5zaW1wbGVjYXN0LmNvbS9hdGd0aWhkMA==",
        "spotify_url": "",
        "youtube_url": "https://www.youtube.com/user/LifeChurchtv",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "lifechurch",
        "facebook_handle": "life.church",
        "instagram_handle": "life.church"
      },
      "image": "https://production.listennotes.com/podcasts/craig-groeschel-leadership-podcast-lifechurch--_K8zgsM0x1-dy-uJsHC_9T.1400x1400.jpg",
      "title": "Craig Groeschel Leadership Podcast",
      "country": "United States",
      "website": "https://www.life.church/leadershippodcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        69,
        75
      ],
      "itunes_id": 1070649025,
      "publisher": "Life.Church",
      "thumbnail": "https://production.listennotes.com/podcasts/craig-groeschel-leadership-podcast-lifechurch-OU5cY0mgjsb-dy-uJsHC_9T.300x300.jpg",
      "is_claimed": false,
      "description": "The Craig Groeschel Leadership Podcast offers personal, practical coaching lessons that take the mystery out of leadership. In each episode of the Craig Groeschel Leadership Podcast, Craig brings you empowering insights and easy-to-understand takeaways you can use to lead yourself and lead your team. You\u2019ll learn effective ways to grow as a leader, optimize your time, develop your team, and structure your organization.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 73,
      "total_episodes": 100,
      "listennotes_url": "https://www.listennotes.com/c/2184bada602d431689dbb4c6c1bc5839/",
      "explicit_content": false,
      "latest_pub_date_ms": 1633600800000,
      "earliest_pub_date_ms": 1452675180098,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "d863da7f921e435fb35f512b54e774d6",
      "rss": "https://rss.art19.com/masters-of-scale",
      "type": "episodic",
      "email": "hello@mastersofscale.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://play.google.com/music/m/Ify6fvmlw7taa25qkxdricygohe?t=Masters_of_Scale",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "mastersofscale",
        "facebook_handle": "mastersofscale",
        "instagram_handle": "mastersofscale"
      },
      "image": "https://production.listennotes.com/podcasts/masters-of-scale-with-reid-hoffman-waitwhat-XJEPjQYftIs-mYoV0CUyxTD.1400x1400.jpg",
      "title": "Masters of Scale with Reid Hoffman",
      "country": "United States",
      "website": "http://www.mastersofscale.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        171,
        157,
        127,
        173,
        149,
        93,
        97,
        67,
        122
      ],
      "itunes_id": 1227971746,
      "publisher": "WaitWhat ",
      "thumbnail": "https://production.listennotes.com/podcasts/masters-of-scale-with-reid-hoffman-waitwhat-xKpqPZgMB8a-mYoV0CUyxTD.300x300.jpg",
      "is_claimed": false,
      "description": "\n      <p>The best startup advice from Silicon Valley and beyond. Iconic CEOs \u2014 from Nike to Netflix, Starbucks to Slack \u2014 share the stories and strategies that helped them grow from startups into global brands.</p><p>On each episode, host Reid Hoffman \u2014 LinkedIn cofounder, Greylock partner and legendary Silicon Valley investor \u2014 proves an unconventional theory about how businesses scale, while his guests share the story of how I built this company. Reid and guests talk entrepreneurship, leadership, strategy, management, fundraising. But they also talk about the human journey \u2014 with all its failures and setbacks.&nbsp;</p><p>With original, cinematic music and hilariously honest stories, Masters of Scale is a business podcast that doesn\u2019t sound like a business podcast.</p><p>Guests on Masters of Scale have included the founders and CEOs of Netflix, Google, Facebook, Starbucks, Nike, Fiat, Spotify, Instagram, Airbnb, Uber, Paypal, Huffington Post, Twitter, Bumble, Slack, Spanx, Shake Shack, Dropbox, TaskRabbit, 23andMe, Mailchimp, Evite, Flickr, CharityWater, Endeavor, IAC and many more.</p>\n    ",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 73,
      "total_episodes": 227,
      "listennotes_url": "https://www.listennotes.com/c/d863da7f921e435fb35f512b54e774d6/",
      "explicit_content": false,
      "latest_pub_date_ms": 1634806800000,
      "earliest_pub_date_ms": 1492543297205,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "5590cb1318054bceb942564a4f067eb6",
      "rss": "https://feeds.publicradio.org/public_feeds/marketplace-pm/itunes/rss",
      "type": "episodic",
      "email": "marketplacecomments@marketplace.org",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5wdWJsaWNyYWRpby5vcmcvcHVibGljX2ZlZWRzL21hcmtldHBsYWNlLXBtL2l0dW5lcy9yc3M=",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "Marketplace",
        "facebook_handle": "marketplaceapm",
        "instagram_handle": "marketplaceapm"
      },
      "image": "https://production.listennotes.com/podcasts/marketplace-marketplace-Jing2WtK5UE.1400x1400.jpg",
      "title": "Marketplace",
      "country": "United States",
      "website": "https://www.marketplace.org/shows/marketplace/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        173,
        99,
        93,
        67,
        95
      ],
      "itunes_id": 201853034,
      "publisher": "Marketplace",
      "thumbnail": "https://production.listennotes.com/podcasts/marketplace-marketplace-Jing2WtK5UE.300x300.jpg",
      "is_claimed": false,
      "description": "<p>Every weekday, host Kai Ryssdal helps you make sense of the day\u2019s business and economic news \u2014 no econ degree or finance background required. \u201cMarketplace\u201d takes you beyond the numbers, bringing you context. Our team of reporters all over the world speak with CEOs, policymakers and regular people just trying to get by.</p>\n",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 73,
      "total_episodes": 1316,
      "listennotes_url": "https://www.listennotes.com/c/5590cb1318054bceb942564a4f067eb6/",
      "explicit_content": false,
      "latest_pub_date_ms": 1635205011000,
      "earliest_pub_date_ms": 1478016905000,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "c5ce6c02cbf1486496206829f7d42e8e",
      "rss": "https://feeds.megaphone.fm/marketsnacks-daily",
      "type": "episodic",
      "email": "podcasts@cadence13.com",
      "extra": {
        "url1": "http://www.marketsnacks.com/",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5tZWdhcGhvbmUuZm0vbWFya2V0c25hY2tzLWRhaWx5",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "marketsnacks",
        "facebook_handle": "MarketSnacks",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-F_0RTie7PzG-kmx0XIZTAys.1400x1400.jpg",
      "title": "Snacks Daily",
      "country": "United States",
      "website": "https://snacks.robinhood.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        67,
        99,
        98,
        95
      ],
      "itunes_id": 1386234384,
      "publisher": "Robinhood Financial, LLC",
      "thumbnail": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-Yp5jkwN1GKi-kmx0XIZTAys.300x300.jpg",
      "is_claimed": false,
      "description": "Digestible financial news. Get smarter fast with an entertaining breakdown of our top 3 business stories in 15 minutes. Pairs perfectly with your commute, workout, or morning oatmeal ritual. Hosted by Jack Kramer and Nick Martell.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 72,
      "total_episodes": 609,
      "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
      "explicit_content": false,
      "latest_pub_date_ms": 1635152400000,
      "earliest_pub_date_ms": 1553519100604,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "73bebcbe52654d1cb94cd1639f736be3",
      "rss": "https://www.omnycontent.com/d/playlist/9b7dacdf-a925-4f95-84dc-ac46003451ff/7029f3ae-fc09-45dd-9e7a-ac5400edbc2f/7cd3d0a4-5749-4d43-9400-ac5400edbc3d/podcast.rss",
      "type": "episodic",
      "email": "danny@kastmedia.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly93d3cub21ueWNvbnRlbnQuY29tL2QvcGxheWxpc3QvOWI3ZGFjZGYtYTkyNS00Zjk1LTg0ZGMtYWM0NjAwMzQ1MWZmLzcwMjlmM2FlLWZjMDktNDVkZC05ZTdhLWFjNTQwMGVkYmMyZi83Y2QzZDBhNC01NzQ5LTRkNDMtOTQwMC1hYzU0MDBlZGJjM2QvcG9kY2FzdC5yc3M=",
        "spotify_url": "",
        "youtube_url": "https://www.youtube.com/user/tailopezofficial",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "tailopez",
        "facebook_handle": "TaiLopezOfficial",
        "instagram_handle": "tailopez"
      },
      "image": "https://production.listennotes.com/podcasts/the-tai-lopez-show-tai-lopez-509rFHaG-1o-kTnaZBogLC0.1400x1400.jpg",
      "title": "The Tai Lopez Show",
      "country": "United States",
      "website": "https://art19.com/shows/the-tai-lopez-show?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        111,
        97,
        88,
        93,
        90,
        157
      ],
      "itunes_id": 877968260,
      "publisher": "Tai Lopez",
      "thumbnail": "https://production.listennotes.com/podcasts/the-tai-lopez-show-tai-lopez-GYBslgCVEa2-kTnaZBogLC0.300x300.jpg",
      "is_claimed": false,
      "description": "<p>The Tai Lopez podcast brings you the best business education straight from the world's top entrepreneurs. I will also review the best books in health, wealth, love and happiness that will help you achieve your maximum potential and live the best life possible. </p>",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 72,
      "total_episodes": 596,
      "listennotes_url": "https://www.listennotes.com/c/73bebcbe52654d1cb94cd1639f736be3/",
      "explicit_content": true,
      "latest_pub_date_ms": 1595585332000,
      "earliest_pub_date_ms": 1400098196595,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "499661f3589f42aaa1532673e0e0aedf",
      "rss": "https://rss.art19.com/smart-passive-income-podcast",
      "type": "episodic",
      "email": "podcasts@teamspi.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9yc3MuYXJ0MTkuY29tL3NtYXJ0LXBhc3NpdmUtaW5jb21lLXBvZGNhc3Q=",
        "spotify_url": "",
        "youtube_url": "https://www.youtube.com/user/smartpassiveincome",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "patflynn",
        "facebook_handle": "smartpassiveincome",
        "instagram_handle": "patflynn"
      },
      "image": "https://production.listennotes.com/podcasts/the-smart-passive-income-online-business-Qe7TJXl_NUu-NDa6-ySp9kw.1400x1400.jpg",
      "title": "The Smart Passive Income Online Business and Blogging Podcast",
      "country": "United States",
      "website": "https://art19.com/shows/smart-passive-income-podcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        173,
        93,
        171,
        144,
        157,
        97,
        98,
        67,
        94,
        111,
        115,
        127
      ],
      "itunes_id": 383084001,
      "publisher": "Pat Flynn",
      "thumbnail": "https://production.listennotes.com/podcasts/the-smart-passive-income-online-business-4QaYUNViG_j-NDa6-ySp9kw.300x300.jpg",
      "is_claimed": false,
      "description": "\n      Pat Flynn from The Smart Passive Income Blog reveals all of his online business and blogging strategies, income sources and killer marketing tips and tricks so you can be ahead of the curve with your online business or blog. Discover how you can create multiple passive income streams that work for you so that you can have the time and freedom to do what you love, whether it's traveling the world, or just living comfortably at home. Since 2008, he's been supporting his family with his many online businesses, and he's been openly sharing his wins, his losses, and all the lessons in between with the community of energetic but humble entrepreneurs who follow him. Self-proclaimed \"crash test dummy of online business\", you'll learn about building authority online, email marketing, building a team and outsourcing, content marketing, podcasting, search engine optimization, niche sites, social media strategies, how to get more traffic, creating online courses, affiliate marketing, and productivity tips so that you create something amazing without burning yourself out. It's a mix of interviews, special co-hosts and solo shows from Pat you're not going to want to miss. Hit subscribe, and get ready to change your life.\n    ",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 72,
      "total_episodes": 530,
      "listennotes_url": "https://www.listennotes.com/c/499661f3589f42aaa1532673e0e0aedf/",
      "explicit_content": false,
      "latest_pub_date_ms": 1634886000000,
      "earliest_pub_date_ms": 1279551600523,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "7d730bb2a72e4268b28ee4c52de1915b",
      "rss": "https://anchor.fm/s/12746230/podcast/rss",
      "type": "episodic",
      "email": null,
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy8xMjc0NjIzMC9wb2RjYXN0L3Jzcw==",
        "spotify_url": "https://open.spotify.com/show/3iJpUGgGD6WHJHL3fsOSOu",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/call-me-candid-haley-pham-lilly-ann-_dSsBumNY9x-LY-c8VNnzRO.1400x1400.jpg",
      "title": "Call Me Candid",
      "country": "United States",
      "website": "https://anchor.fm/callmecandid?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        67,
        171
      ],
      "itunes_id": 1494577260,
      "publisher": "Haley Pham & Lilly Ann",
      "thumbnail": "https://production.listennotes.com/podcasts/call-me-candid-haley-pham-lilly-ann-wbmDUyde8-A-LY-c8VNnzRO.300x300.jpg",
      "is_claimed": false,
      "description": "Two gals chattin about business, advice, and our experiences!",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 71,
      "total_episodes": 33,
      "listennotes_url": "https://www.listennotes.com/c/7d730bb2a72e4268b28ee4c52de1915b/",
      "explicit_content": false,
      "latest_pub_date_ms": 1600063200000,
      "earliest_pub_date_ms": 1579047805031,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "fbecfdd4116e4e7a954bd6bc4cb0b406",
      "rss": "https://amyporterfield.libsyn.com/rss",
      "type": "episodic",
      "email": "podcast@amyporterfield.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9hbXlwb3J0ZXJmaWVsZC5saWJzeW4uY29tL3Jzcw==",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "AmyPorterfield",
        "facebook_handle": "AmyPorterfield",
        "instagram_handle": "amyporterfield"
      },
      "image": "https://production.listennotes.com/podcasts/online-marketing-made-easy-with-amy-WRDY2-5eH6j-jXUyf4vBV20.1400x1400.jpg",
      "title": "Online Marketing Made Easy with Amy Porterfield",
      "country": "United States",
      "website": "https://amyporterfield.com/category/podcast/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        173,
        93,
        157,
        94,
        97,
        67
      ],
      "itunes_id": 594703545,
      "publisher": "Amy Porterfield",
      "thumbnail": "https://production.listennotes.com/podcasts/online-marketing-made-easy-with-amy-XK8o-V9vgSu-jXUyf4vBV20.300x300.jpg",
      "is_claimed": false,
      "description": "Ever wish you had a business mentor with over a decade of experience whispering success secrets in your ear? That\u2019s exactly what you\u2019ll get when you tune into the top-ranked Online Marketing Made Easy Podcast with your host, 9 to 5er turned CEO of a multi-million dollar business, Amy Porterfield. Her specialty? Breaking down big ideas and strategies into actionable step-by-step processes designed to get you results with a whole lot less stress. Tune in, get inspired, and get ready to discover why hundreds of thousands of online business owners turn to Amy for guidance when it comes to all things online business including digital courses, list building, social media, content, webinars, and so much more. Whether you're a budding entrepreneur, have a comfy side-hustle, or are looking to take your business to the next level, each episode is designed to help you take immediate action on the most important strategies for starting and growing your online business today.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 71,
      "total_episodes": 430,
      "listennotes_url": "https://www.listennotes.com/c/fbecfdd4116e4e7a954bd6bc4cb0b406/",
      "explicit_content": false,
      "latest_pub_date_ms": 1635145260000,
      "earliest_pub_date_ms": 1358200867417,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "4e272a4cec844b32be6ad2048d614b28",
      "rss": "https://www.omnycontent.com/d/playlist/aaea4e69-af51-495e-afc9-a9760146922b/73fd80c2-48d6-433c-817f-aaa4017c3c16/1c35c947-56d2-49cc-be15-aaa4017c3c1e/podcast.rss",
      "type": "episodic",
      "email": null,
      "extra": {
        "url1": "https://bythebookpod.com/",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly93d3cub21ueWNvbnRlbnQuY29tL2QvcGxheWxpc3QvYWFlYTRlNjktYWY1MS00OTVlLWFmYzktYTk3NjAxNDY5MjJiLzczZmQ4MGMyLTQ4ZDYtNDMzYy04MTdmLWFhYTQwMTdjM2MxNi8xYzM1Yzk0Ny01NmQyLTQ5Y2MtYmUxNS1hYWE0MDE3YzNjMWUvcG9kY2FzdC5yc3M=",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "bythebookpod",
        "facebook_handle": "kristenandjolenta",
        "instagram_handle": "bythebookpod"
      },
      "image": "https://production.listennotes.com/podcasts/by-the-book-stitcher-jolenta-greenberg-ipRlfg9cJXZ--sCyAljv4BT.1400x1400.jpg",
      "title": "By The Book",
      "country": "United States",
      "website": "https://www.stitcher.com/podcast/stitcher/by-the-book?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        104,
        191,
        78,
        93,
        67,
        88,
        90,
        122,
        133
      ],
      "itunes_id": 1217948628,
      "publisher": "Stitcher & Jolenta Greenberg, Kristen Meinzer",
      "thumbnail": "https://production.listennotes.com/podcasts/by-the-book-stitcher-jolenta-greenberg-OlvzI-AT7Gm--sCyAljv4BT.300x300.jpg",
      "is_claimed": false,
      "description": "<p>Half reality show, half self-help podcast, and one wild social experiment. Join comedian Jolenta Greenberg and culture critic Kristen Meinzer as they live by the rules of a different self-help book each episode to figure out which ones might actually be life changing.</p>",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 71,
      "total_episodes": 187,
      "listennotes_url": "https://www.listennotes.com/c/4e272a4cec844b32be6ad2048d614b28/",
      "explicit_content": true,
      "latest_pub_date_ms": 1634788860000,
      "earliest_pub_date_ms": 1489787580182,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "295925e24d5a478f8478ee1026560efc",
      "rss": "http://feeds.wnyc.org/trumpinc",
      "type": "episodic",
      "email": "wnycdigital@gmail.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cDovL2ZlZWRzLndueWMub3JnL3RydW1waW5j",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "WNYCStudios",
        "facebook_handle": "WNYCStudios",
        "instagram_handle": "wnycstudios"
      },
      "image": "https://production.listennotes.com/podcasts/trump-inc-wnyc-studios-KfHE1-pj3iw-r2THU0gu3fB.1400x1400.jpg",
      "title": "Trump, Inc. ",
      "country": "United States",
      "website": "https://www.wnycstudios.org/podcasts/trumpinc?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        216,
        99,
        135,
        67,
        93
      ],
      "itunes_id": 1344894187,
      "publisher": "WNYC Studios ",
      "thumbnail": "https://production.listennotes.com/podcasts/trump-inc-wnyc-studios-Luv2o8CKclT-r2THU0gu3fB.300x300.jpg",
      "is_claimed": false,
      "description": "He\u2019s the President, yet we\u2019re still trying to answer basic questions about how his business works: What deals are happening, who they\u2019re happening with, and if the President and his family are keeping their promise to separate the Trump Organization from the Trump White House. \u201cTrump, Inc.\u201d is a joint reporting project from WNYC Studios and ProPublica that digs deep into these questions. We\u2019ll be layout out what we know, what we don\u2019t and how you can help us fill in the gaps. \r\nWNYC Studios is a listener-supported producer of other leading podcasts, including On the Media, Radiolab, Death, Sex & Money, Here\u2019s the Thing with Alec Baldwin, Nancy and many others. ProPublica is a non-profit investigative newsroom.\r\n\u00a9 WNYC Studios",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 71,
      "total_episodes": 96,
      "listennotes_url": "https://www.listennotes.com/c/295925e24d5a478f8478ee1026560efc/",
      "explicit_content": false,
      "latest_pub_date_ms": 1611075600000,
      "earliest_pub_date_ms": 1517806800000,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "a409b8bb93f44054a7be2d6b30843899",
      "rss": "https://entrepreneuronfire.libsyn.com/rss",
      "type": "episodic",
      "email": "John@EntrepreneurOnFire.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9lbnRyZXByZW5ldXJvbmZpcmUubGlic3luLmNvbS9yc3M=",
        "spotify_url": "",
        "youtube_url": "https://www.youtube.com/channel/UCXfzpliAfdjParawJljHo2g",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "johnleedumas",
        "facebook_handle": "johnleedumas1",
        "instagram_handle": "johnleedumas"
      },
      "image": "https://production.listennotes.com/podcasts/entrepreneurs-on-fire-john-lee-dumas-of-_faXwKkD9hi-1WOhT7u6VQb.1400x1400.jpg",
      "title": "Entrepreneurs on Fire",
      "country": "United States",
      "website": "https://www.eofire.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        171,
        173,
        157,
        169,
        67,
        88,
        111,
        90,
        94,
        97
      ],
      "itunes_id": 564001633,
      "publisher": "John Lee Dumas of EOFire",
      "thumbnail": "https://production.listennotes.com/podcasts/entrepreneurs-on-fire-john-lee-dumas-of-cr_NzRxX1uS-1WOhT7u6VQb.300x300.jpg",
      "is_claimed": true,
      "description": "John Lee Dumas is the founder and host of the award winning podcast, Entrepreneurs On Fire. With over 100 million listens of his 3000+ episodes, JLD has turned Entrepreneurs On Fire into a media empire that generates over a million listens every month and 7-figures of NET annual revenue 8-years in a row. His first traditionally published book, The Common Path to Uncommon Success is the modern day version of Think and Grow Rich with a revolutionary 17-step roadmap to financial freedom and fulfillment. Learn more at UncommonSuccessBook.com",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 71,
      "total_episodes": 2790,
      "listennotes_url": "https://www.listennotes.com/c/a409b8bb93f44054a7be2d6b30843899/",
      "explicit_content": false,
      "latest_pub_date_ms": 1635150600000,
      "earliest_pub_date_ms": 1348297202688,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "7911e245980f460bb072d4aca3e59278",
      "rss": "https://kwikbrain.libsyn.com/rss",
      "type": "episodic",
      "email": "kwiksupport@gmail.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9rd2lrYnJhaW4ubGlic3luLmNvbS9yc3M=",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "jimkwik",
        "facebook_handle": "",
        "instagram_handle": "jimkwik"
      },
      "image": "https://production.listennotes.com/podcasts/kwik-brain-with-jim-kwik-jim-kwik-your-xlL8GdyQWMc-ZQJshPf4_6w.1400x1400.jpg",
      "title": "Kwik Brain with Jim Kwik",
      "country": "United States",
      "website": "https://www.kwikbrain.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        93,
        88,
        90,
        111,
        115
      ],
      "itunes_id": 1208024744,
      "publisher": "Jim Kwik, Your Brain Coach, Founder www.KwikLearning.com",
      "thumbnail": "https://production.listennotes.com/podcasts/kwik-brain-with-jim-kwik-jim-kwik-your-XAjnIu6G4M5-ZQJshPf4_6w.300x300.jpg",
      "is_claimed": false,
      "description": "Kwik Brain is a fun, fast-paced show designed to help busy people learn and achieve anything in a fraction of the time! Your coach, Jim Kwik (his real name), is the brain & memory trainer to elite mental performers, including many of the world\u2019s leading CEO\u2019s and celebrities. In this easy to digest bite-sized podcast, you will discover Kwik\u2019s favorite shortcuts to read faster, remember more, and \u2018supercharge\u2019 your greatest wealth-building asset: your brain. Whether you\u2019re a student, senior, entrepreneur or educator, you will get the edge with these simple actionable tools to sharpen your mind, enhance your focus, and fast-track your fullest potential. Get show notes, Jim\u2019s latest brain-training, and submit your questions in our private community (free) at: www.KwikBrain.com\n\nJim Kwik is the founder of KwikLearning.com, a widely recognized world leader in speed-reading, memory improvement, brain performance, and accelerated learning with students in over 150 countries.\n\nAfter a childhood brain injury left him learning-challenged, Kwik created strategies to dramatically enhance his mental performance. He has since dedicated his life to helping others unleash their true genius and brainpower to learn anything faster and live a life of greater power, productivity, and purpose.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 71,
      "total_episodes": 249,
      "listennotes_url": "https://www.listennotes.com/c/7911e245980f460bb072d4aca3e59278/",
      "explicit_content": false,
      "latest_pub_date_ms": 1635181867000,
      "earliest_pub_date_ms": 1490733924244,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "f4a7bdbef7a84fd0b4a712b70a3c5ec5",
      "rss": "http://choosefi.libsyn.com/rss",
      "type": "episodic",
      "email": "feedback@choosefi.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cDovL2Nob29zZWZpLmxpYnN5bi5jb20vcnNz",
        "spotify_url": "",
        "youtube_url": "https://www.youtube.com/choosefi",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "choosefi",
        "facebook_handle": "ChooseFi",
        "instagram_handle": "choosefiradio"
      },
      "image": "https://production.listennotes.com/podcasts/choosefi-jonathan-mendonsa-brad-barrett-Xb8c9pQA_y--e8_g1GAYHIj.1400x1400.jpg",
      "title": "ChooseFI",
      "country": "United States",
      "website": "https://www.choosefi.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        144,
        67,
        93,
        97,
        122,
        123,
        127,
        129,
        98
      ],
      "itunes_id": 1187770032,
      "publisher": "The Unstuck Network",
      "thumbnail": "https://production.listennotes.com/podcasts/choosefi-jonathan-mendonsa-brad-barrett-UCfs8WRklv0-e8_g1GAYHIj.300x300.jpg",
      "is_claimed": false,
      "description": "How would your life change if you reached Financial Independence and got to the point where working is optional? What actions can you take today to make that not just possible but probable. Jonathan & Brad explore the tactics that the FI community uses to reclaim decades of their lives. They discuss reducing expenses, crushing debt, tax optimization, building passive income streams through online businesses and real estate and how to travel the world for free. Every episode is packed with actionable tips and no topic is too big or small as long as it speeds up the process of reaching financial independence.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 70,
      "total_episodes": 509,
      "listennotes_url": "https://www.listennotes.com/c/f4a7bdbef7a84fd0b4a712b70a3c5ec5/",
      "explicit_content": false,
      "latest_pub_date_ms": 1635138000000,
      "earliest_pub_date_ms": 1482062785436,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "23bd4f3432c2452d93f525e2446a5878",
      "rss": "https://www.omnycontent.com/d/playlist/aaea4e69-af51-495e-afc9-a9760146922b/0b794591-3d49-40af-8da4-aac0014e4183/9eb6abf8-729d-41a3-9518-aac00155e40b/podcast.rss",
      "type": "episodic",
      "email": "rss@earwolf.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly93d3cub21ueWNvbnRlbnQuY29tL2QvcGxheWxpc3QvYWFlYTRlNjktYWY1MS00OTVlLWFmYzktYTk3NjAxNDY5MjJiLzBiNzk0NTkxLTNkNDktNDBhZi04ZGE0LWFhYzAwMTRlNDE4My85ZWI2YWJmOC03MjlkLTQxYTMtOTUxOC1hYWMwMDE1NWU0MGIvcG9kY2FzdC5yc3M=",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/scam-goddess-earwolf-laci-mosley-u9lrIHk18yK-PstEMgqXCUd.1400x1400.jpg",
      "title": "Scam Goddess",
      "country": "United States",
      "website": "https://www.earwolf.com/show/scam-goddess/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        133,
        135,
        93
      ],
      "itunes_id": 1479455008,
      "publisher": "Earwolf & Laci Mosley",
      "thumbnail": "https://production.listennotes.com/podcasts/scam-goddess-earwolf-laci-mosley-N6ZDk3hq9gx-PstEMgqXCUd.300x300.jpg",
      "is_claimed": false,
      "description": "\u201cScam Goddess is a podcast dedicated to fraud and all those who practice it! Each week host Laci Mosley (aka Scam Goddess) keeps listeners up to date on current rackets, digs deep into the latest scams, and breaks down historic hoodwinks alongside some of your favorite comedians! It's like true crime only without all the death! True fun crime!\u201d \n ",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 70,
      "total_episodes": 113,
      "listennotes_url": "https://www.listennotes.com/c/23bd4f3432c2452d93f525e2446a5878/",
      "explicit_content": true,
      "latest_pub_date_ms": 1634616000000,
      "earliest_pub_date_ms": 1420099200041,
      "listen_score_global_rank": "0.05%"
    }
  ],
  "parent_id": 67,
  "page_number": 2,
  "has_previous": true,
  "listennotes_url": "https://www.listennotes.com/best-business-podcasts-93/",
  "next_page_number": 3,
  "previous_page_number": 1
}
```   
</details>



<details>
  <summary>Click to see response schema</summary>
  
```json
{
  "type": "object",
  "required": [
    "has_next",
    "has_previous",
    "id",
    "listennotes_url",
    "name",
    "next_page_number",
    "page_number",
    "parent_id",
    "podcasts",
    "previous_page_number",
    "total"
  ],
  "properties": {
    "id": {
      "type": "integer",
      "example": 95,
      "description": "The id of this genre"
    },
    "name": {
      "type": "string",
      "example": "Business News",
      "description": "This genre's name."
    },
    "total": {
      "type": "integer",
      "example": 325
    },
    "has_next": {
      "type": "boolean",
      "example": true
    },
    "podcasts": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "example": "4d3fe717742d4963a85562e9f84d8c79",
            "description": "Podcast id."
          },
          "rss": {
            "type": "string",
            "example": "https://sw7x7.libsyn.com/rss",
            "description": "RSS url of this podcast. This field is available only in the PRO/ENTERPRISE plan."
          },
          "type": {
            "enum": [
              "episodic",
              "serial"
            ],
            "type": "string",
            "example": "episodic",
            "description": "The type of this podcast - episodic or serial."
          },
          "email": {
            "type": "string",
            "example": "hello@example.com",
            "description": "The email of this podcast's producer. This field is available only in the PRO/ENTERPRISE plan."
          },
          "extra": {
            "type": "object",
            "properties": {
              "url1": {
                "type": "string",
                "description": "Url affiliated with this podcast"
              },
              "url2": {
                "type": "string",
                "description": "Url affiliated with this podcast"
              },
              "url3": {
                "type": "string",
                "description": "Url affiliated with this podcast"
              },
              "google_url": {
                "type": "string",
                "example": "https://play.google.com/music/listen?u=0#/ps/I7gdcrqcmvhfnhh2cyqkcg32tkq",
                "description": "Google Podcasts url for this podcast"
              },
              "spotify_url": {
                "type": "string",
                "example": "https://open.spotify.com/show/2rQJUP9Y3HxemiW3JHt9WV",
                "description": "Spotify url for this podcast"
              },
              "youtube_url": {
                "type": "string",
                "example": "https://www.youtube.com/sw7x7",
                "description": "YouTube url affiliated with this podcast"
              },
              "linkedin_url": {
                "type": "string",
                "description": "LinkedIn url affiliated with this podcast"
              },
              "wechat_handle": {
                "type": "string",
                "description": "WeChat username affiliated with this podcast"
              },
              "patreon_handle": {
                "type": "string",
                "example": "sw7x7",
                "description": "Patreon username affiliated with this podcast"
              },
              "twitter_handle": {
                "type": "string",
                "example": "SW7x7podcast",
                "description": "Twitter username affiliated with this podcast"
              },
              "facebook_handle": {
                "type": "string",
                "example": "sw7x7",
                "description": "Facebook username affiliated with this podcast"
              },
              "instagram_handle": {
                "type": "string",
                "example": "sw7x7",
                "description": "Instagram username affiliated with this podcast"
              }
            }
          },
          "image": {
            "type": "string",
            "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
            "description": "Image url for this podcast's artwork. If you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
          },
          "title": {
            "type": "string",
            "example": "Star Wars 7x7 | Star Wars News, Interviews, and More!",
            "description": "Podcast name."
          },
          "country": {
            "type": "string",
            "example": "United States",
            "description": "The country where this podcast is produced."
          },
          "website": {
            "type": "string",
            "example": "http://sw7x7.com/",
            "description": "Website url of this podcast."
          },
          "language": {
            "type": "string",
            "example": "English",
            "description": "The language of this podcast. You can get all supported languages from `GET /languages`."
          },
          "genre_ids": {
            "type": "array",
            "items": {
              "type": "integer",
              "description": "Genre ids."
            },
            "example": [
              138,
              86,
              160,
              68,
              82,
              100,
              101
            ]
          },
          "itunes_id": {
            "type": "integer",
            "example": 896354638,
            "description": "iTunes id for this podcast."
          },
          "publisher": {
            "type": "string",
            "example": "Planet Broadcasting",
            "description": "Podcast publisher name."
          },
          "thumbnail": {
            "type": "string",
            "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
            "description": "Thumbnail image url for this podcast's artwork (300x300)."
          },
          "is_claimed": {
            "type": "boolean",
            "example": true,
            "description": "Whether this podcast is claimed by its producer on [ListenNotes.com](https://www.ListenNotes.com)."
          },
          "description": {
            "type": "string",
            "example": "<p>The Star Wars 7x7 Podcast is Rebel-rousing fun for everyday Jedi, between 7 and 14 minutes a day, 7 days a week. Join host Allen Voivod for Star Wars news, history, interviews, trivia, and deep dives into the Star Wars story as told in movies, books, comics, games, cartoons, and more. Subscribe now for your daily dose of Star Wars joy. It's destiny unleashed!</p>",
            "description": "Html of this episode's full description"
          },
          "looking_for": {
            "type": "object",
            "properties": {
              "guests": {
                "type": "boolean",
                "example": true,
                "description": "Whether this podcast is looking for guests."
              },
              "cohosts": {
                "type": "boolean",
                "example": true,
                "description": "Whether this podcast is looking for cohosts."
              },
              "sponsors": {
                "type": "boolean",
                "example": true,
                "description": "Whether this podcast is looking for sponsors."
              },
              "cross_promotion": {
                "type": "boolean",
                "example": true,
                "description": "Whether this podcast is looking for cross promotion opportunities with other podcasts."
              }
            }
          },
          "listen_score": {
            "type": "integer",
            "example": 81,
            "description": "The estimated popularity score of a podcast compared to all other rss-based public podcasts in the world on a scale from 0 to 100.\nIf the score is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
          },
          "total_episodes": {
            "type": "integer",
            "example": 324,
            "description": "Total number of episodes in this podcast."
          },
          "listennotes_url": {
            "type": "string",
            "example": "https://www.listennotes.com/c/4d3fe717742d4963a85562e9f84d8c79/",
            "description": "The url of this podcast on [ListenNotes.com](https://www.ListenNotes.com)."
          },
          "explicit_content": {
            "type": "boolean",
            "example": false,
            "description": "Whether this podcast contains explicit language."
          },
          "latest_pub_date_ms": {
            "type": "integer",
            "example": 1557499770000,
            "description": "The published date of the latest episode of this podcast. In milliseconds"
          },
          "earliest_pub_date_ms": {
            "type": "integer",
            "example": 1470667902000,
            "description": "The published date of the oldest episode of this podcast. In milliseconds"
          },
          "listen_score_global_rank": {
            "type": "string",
            "example": "0.5%",
            "description": "The estimated popularity ranking of a podcast compared to all other rss-based public podcasts in the world.\nFor example, if the value is 0.5%, then this podcast is one of the top 0.5% most popular shows out of all podcasts globally, ranked by Listen Score.\nIf the ranking is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
          }
        }
      }
    },
    "parent_id": {
      "type": "integer",
      "example": 93,
      "description": "The id of parent genre."
    },
    "page_number": {
      "type": "integer",
      "example": 2
    },
    "has_previous": {
      "type": "boolean"
    },
    "listennotes_url": {
      "type": "string",
      "example": "https://www.listennotes.com/best-business-news-podcasts-95/",
      "description": "Url of the list of best podcasts on [ListenNotes.com](https://www.ListenNotes.com)."
    },
    "next_page_number": {
      "type": "integer",
      "example": 3
    },
    "previous_page_number": {
      "type": "integer",
      "example": 1
    }
  }
}
```   
</details>




### Fetch a list of supported countries/regions for best podcasts

Function Name: **fetch_podcast_regions**

It returns a dictionary of country codes (e.g., us, gb...) &amp; country names (United States, United Kingdom...). The country code is used in the query parameter **region** of `GET /best_podcasts`.


Example:
```python

from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)      

response = client.fetch_podcast_regions()
            
print(response.json())

```

See all available parameters on the [API Docs page](https://www.listennotes.com/api/docs/#get-api-v2-regions).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "regions": {
    "ae": "United Arab Emirates",
    "ag": "Antigua and Barbuda",
    "ai": "Anguilla",
    "al": "Albania",
    "am": "Armenia",
    "ao": "Angola",
    "ar": "Argentina",
    "at": "Austria",
    "au": "Australia",
    "az": "Azerbaijan",
    "bb": "Barbados",
    "bd": "Bangladesh",
    "be": "Belgium",
    "bf": "Burkina-Faso",
    "bg": "Bulgaria",
    "bh": "Bahrain",
    "bj": "Benin",
    "bm": "Bermuda",
    "bn": "Brunei Darussalam",
    "bo": "Bolivia",
    "br": "Brazil",
    "bs": "Bahamas",
    "bt": "Bhutan",
    "bw": "Botswana",
    "by": "Belarus",
    "bz": "Belize",
    "ca": "Canada",
    "ch": "Switzerland",
    "cl": "Chile",
    "cn": "China",
    "co": "Colombia",
    "cr": "Costa Rica",
    "cv": "Cape Verde",
    "cy": "Cyprus",
    "cz": "Czech Republic",
    "de": "Germany",
    "dk": "Denmark",
    "dm": "Dominica",
    "do": "Dominican Republic",
    "dz": "Algeria",
    "ec": "Ecuador",
    "ee": "Estonia",
    "eg": "Egypt",
    "es": "Spain",
    "fi": "Finland",
    "fj": "Fiji",
    "fr": "France",
    "gb": "United Kingdom",
    "gd": "Grenada",
    "gh": "Ghana",
    "gm": "Gambia",
    "gr": "Greece",
    "gt": "Guatemala",
    "gw": "Guinea Bissau",
    "gy": "Guyana",
    "hk": "Hong Kong",
    "hn": "Honduras",
    "hr": "Croatia",
    "hu": "Hungary",
    "id": "Indonesia",
    "ie": "Ireland",
    "il": "Israel",
    "in": "India",
    "is": "Iceland",
    "it": "Italy",
    "jm": "Jamaica",
    "jo": "Jordan",
    "jp": "Japan",
    "ke": "Kenya",
    "kg": "Krygyzstan",
    "kh": "Cambodia",
    "kr": "South Korea",
    "kw": "Kuwait",
    "ky": "Cayman Islands",
    "kz": "Kazakhstan",
    "la": "Laos",
    "lb": "Lebanon",
    "lc": "Saint Lucia",
    "lk": "Sri Lanka",
    "lr": "Liberia",
    "lt": "Lithuania",
    "lu": "Luxembourg",
    "lv": "Latvia",
    "md": "Moldova",
    "mg": "Madagascar",
    "mk": "Macedonia",
    "ml": "Mali",
    "mn": "Mongolia",
    "mo": "Macau",
    "mr": "Mauritania",
    "ms": "Montserrat",
    "mt": "Malta",
    "mu": "Mauritius",
    "mw": "Malawi",
    "mx": "Mexico",
    "my": "Malaysia",
    "mz": "Mozambique",
    "na": "Namibia",
    "ne": "Niger",
    "ng": "Nigeria",
    "ni": "Nicaragua",
    "nl": "Netherlands",
    "no": "Norway",
    "np": "Nepal",
    "nz": "New Zealand",
    "om": "Oman",
    "pa": "Panama",
    "pe": "Peru",
    "pg": "Papua New Guinea",
    "ph": "Philippines",
    "pk": "Pakistan",
    "pl": "Poland",
    "pt": "Portugal",
    "pw": "Palau",
    "py": "Paraguay",
    "qa": "Qatar",
    "ro": "Romania",
    "ru": "Russia",
    "sa": "Saudi Arabia",
    "sb": "Soloman Islands",
    "sc": "Seychelles",
    "se": "Sweden",
    "sg": "Singapore",
    "si": "Slovenia",
    "sk": "Slovakia",
    "sl": "Sierra Leone",
    "sn": "Senegal",
    "so": "Somalia",
    "sr": "Suriname",
    "sv": "El Salvador",
    "sz": "Swaziland",
    "td": "Chad",
    "th": "Thailand",
    "tj": "Tajikistan",
    "tm": "Turkmenistan",
    "tn": "Tunisia",
    "tr": "Turkey",
    "tw": "Taiwan",
    "tz": "Tanzania",
    "ua": "Ukraine",
    "ug": "Uganda",
    "us": "United States",
    "uy": "Uruguay",
    "uz": "Uzbekistan",
    "ve": "Venezuela",
    "vg": "British Virgin Islands",
    "vn": "Vietnam",
    "ye": "Yemen",
    "za": "South Africa",
    "zw": "Zimbabwe"
  }
}
```   
</details>



<details>
  <summary>Click to see response schema</summary>
  
```json
{
  "type": "object",
  "required": [
    "regions"
  ],
  "properties": {
    "regions": {
      "type": "object",
      "example": {
        "au": "Australia",
        "de": "Germany",
        "ua": "Ukraine",
        "us": "United States"
      }
    }
  }
}
```   
</details>




### Fetch recommendations for a podcast

Function Name: **fetch_recommendations_for_podcast**

Fetch up to 8 podcast recommendations based on the given podcast id.

Example:
```python

from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)      

response = client.fetch_recommendations_for_podcast(id='25212ac3c53240a880dd5032e547047b')
            
print(response.json())

```

See all available parameters on the [API Docs page](https://www.listennotes.com/api/docs/#get-api-v2-podcasts-id-recommendations).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "recommendations": [
    {
      "id": "805535e1de5a4c7991f4f323e82ce9e7",
      "rss": "https://bryankramer.libsyn.com/rss",
      "type": "episodic",
      "email": "bryan.kramer@purematter.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9icnlhbmtyYW1lci5saWJzeW4uY29tL3Jzcw==",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "bryankramer",
        "facebook_handle": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-bryan-kramer-show-bryan-kramer-Br0M_IayKc3-0SCl91ZT-bU.1400x1400.jpg",
      "title": "The Bryan Kramer Show",
      "country": "United States",
      "website": "http://bryankramer.libsyn.com/podcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        88,
        90,
        93,
        97
      ],
      "itunes_id": 1078655111,
      "publisher": "Bryan Kramer",
      "thumbnail": "https://production.listennotes.com/podcasts/the-bryan-kramer-show-bryan-kramer-E7o80typv_b-0SCl91ZT-bU.300x300.jpg",
      "is_claimed": false,
      "description": "Join us as Bryan Kramer deconstructs human behavior and digs deep to share tactics, tools and tricks you can use every day to help you reach peak performance. In each show, Bryan interviews high-profile guests hitting consistent home runs in business, entrepreneurialism marketing and social. Bryan is a TED speaker, USA Today best-selling author, and CEO who consults Fortune 500 clients such as IBM, Cisco, NFL, Harvard University and NASA. He's known for his books Human to Human, #H2H and Shareology. Forbes calls him a \"Zen master to digital marketers.\"",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 38,
      "total_episodes": 64,
      "listennotes_url": "https://www.listennotes.com/c/805535e1de5a4c7991f4f323e82ce9e7/",
      "explicit_content": false,
      "latest_pub_date_ms": 1502287200000,
      "earliest_pub_date_ms": 1453246535000,
      "listen_score_global_rank": "2.5%"
    },
    {
      "id": "6dbbce41ba9e46e49e7f6c7ae43765eb",
      "rss": "https://anchor.fm/s/67178f10/podcast/rss",
      "type": "episodic",
      "email": null,
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-buci-koci-LMzZXdGDaP2-ZGO9yQqSm0N.1400x1400.jpg",
      "title": "The Buci Koci",
      "country": "United States",
      "website": "https://anchor.fm/the-buci-koci?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        67,
        171
      ],
      "itunes_id": 1581186562,
      "publisher": "Tim Ferriss: Bestselling Author, Human Guinea Pig",
      "thumbnail": "https://production.listennotes.com/podcasts/the-buci-koci-SkjOwD8-rCI-ZGO9yQqSm0N.300x300.jpg",
      "is_claimed": false,
      "description": "Productivity is about doing the RIGHT things at the RIGHT time for the RIGHT reasons. ",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": null,
      "total_episodes": 10,
      "listennotes_url": "https://www.listennotes.com/c/6dbbce41ba9e46e49e7f6c7ae43765eb/",
      "explicit_content": false,
      "latest_pub_date_ms": 1629012571000,
      "earliest_pub_date_ms": 1629012479009,
      "listen_score_global_rank": null
    },
    {
      "id": "7060b5d48b3440ba9668f9af2a90fa7f",
      "rss": "https://www.spreaker.com/show/4920844/episodes/feed",
      "type": "episodic",
      "email": null,
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://www.google.com/podcasts?feed=aHR0cHM6Ly9hbmNob3IuZm0vcy80ZjJjNjZmMC9wb2RjYXN0L3Jzcw==",
        "spotify_url": "https://open.spotify.com/show/62soqGPhnYJBRrP2vSAk6b",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-tim-ferriss-show-5-minute-podcast-mpqMa73u08D-mYx8LcSkhz1.1400x1400.jpg",
      "title": "The Tim Ferriss Show | 5 minute podcast summaries",
      "country": "United States",
      "website": "https://www.spreaker.com/show/the-tim-ferriss-show-5-minute-podcast-su?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        181,
        111
      ],
      "itunes_id": 1556286643,
      "publisher": "5 minute podcast summaries",
      "thumbnail": "https://production.listennotes.com/podcasts/the-tim-ferriss-show-5-minute-podcast-XMuN8q2Jorb-mYx8LcSkhz1.300x300.jpg",
      "is_claimed": false,
      "description": "5 minute summaries of The Tim Ferriss Show's podcast episodes. Get the best insights and ideas in much less time, more at owltail.com<br /><br />Written summaries: <a href=\"https://www.owltail.com/summaries/75553-the-tim-ferriss-show\" rel=\"noopener\">https://www.owltail.com/summaries/75553-the-tim-ferriss-show</a><br /><br />Other podcast summaries in Apple Podcasts: <a href=\"http://bit.ly/5-min-summaries\" rel=\"noopener\">http://bit.ly/5-min-summaries</a><br /><br />Other podcast summaries In other apps, search 'podcast summaries'.<br /><br />Tim Ferriss is a self-experimenter and bestselling author, best known for The 4-Hour Workweek, which has been translated into 40+ languages. Newsweek calls him \"the world's best human guinea pig,\" and The New York Times calls him \"a cross between Jack Welch and a Buddhist monk.\" In this show, he deconstructs world-class performers from eclectic areas (investing, chess, pro sports, etc.), digging deep to find the tools, tactics, and tricks that listeners can use.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 28,
      "total_episodes": 12,
      "listennotes_url": "https://www.listennotes.com/c/7060b5d48b3440ba9668f9af2a90fa7f/",
      "explicit_content": false,
      "latest_pub_date_ms": 1625881044000,
      "earliest_pub_date_ms": 1619229600011,
      "listen_score_global_rank": "10%"
    },
    {
      "id": "f9d5885d7cf7485d891e82dea3186640",
      "rss": "https://feeds.npr.org/510313/podcast.xml",
      "type": "episodic",
      "email": "podcasts@npr.org",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5ucHIub3JnLzUxMDMxMy9wb2RjYXN0LnhtbA==",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "HowIBuiltThis",
        "facebook_handle": "howibuiltthis",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/how-i-built-this-with-guy-raz-npr-G7ePAvBMW2l-UC0qH23iP9T.1400x1400.jpg",
      "title": "How I Built This with Guy Raz",
      "country": "United States",
      "website": "https://www.npr.org/podcasts/510313/how-i-built-this?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        127,
        171,
        106,
        94,
        173,
        90,
        157
      ],
      "itunes_id": 1150510297,
      "publisher": "NPR",
      "thumbnail": "https://production.listennotes.com/podcasts/how-i-built-this-with-guy-raz-npr-AbxLGkT50v9-UC0qH23iP9T.300x300.jpg",
      "is_claimed": false,
      "description": "Guy Raz dives into the stories behind some of the world's best known companies. <em>How I Built This</em> weaves a narrative journey about innovators, entrepreneurs and idealists\u2014and the movements they built. Order the <em data-stringify-type=\"italic\">How I Built This</em> book at https://www.guyraz.com/",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 85,
      "total_episodes": 381,
      "listennotes_url": "https://www.listennotes.com/c/f9d5885d7cf7485d891e82dea3186640/",
      "explicit_content": false,
      "latest_pub_date_ms": 1635135331000,
      "earliest_pub_date_ms": 1472828160375,
      "listen_score_global_rank": "0.01%"
    },
    {
      "id": "fe6864628066420c8103c94e91e72eb3",
      "rss": "http://askgaryvee.garyvee.libsynpro.com/rss",
      "type": "episodic",
      "email": "justin.schnell@vaynermedia.com",
      "extra": {
        "url1": "https://medium.com/@garyvee",
        "url2": "https://www.snapchat.com/add/garyvee",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cDovL2Fza2dhcnl2ZWUuZ2FyeXZlZS5saWJzeW5wcm8uY29tL3Jzcw==",
        "spotify_url": "",
        "youtube_url": "https://www.youtube.com/user/garyvaynerchuk",
        "linkedin_url": "https://www.linkedin.com/in/garyvaynerchuk/",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "garyvee",
        "facebook_handle": "gary",
        "instagram_handle": "garyvee"
      },
      "image": "https://production.listennotes.com/podcasts/the-garyvee-audio-experience-gary-vaynerchuk-3dCqxBQZSX9-X0Dfm7O_o3y.1400x1400.jpg",
      "title": "The GaryVee Audio Experience",
      "country": "United States",
      "website": "http://www.garyvaynerchuk.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        171,
        98,
        173,
        157,
        97,
        78,
        169,
        127,
        67,
        95
      ],
      "itunes_id": 928159684,
      "publisher": "Gary Vaynerchuk",
      "thumbnail": "https://production.listennotes.com/podcasts/the-garyvee-audio-experience-gary-vaynerchuk-G6zR28cWvB1-X0Dfm7O_o3y.300x300.jpg",
      "is_claimed": false,
      "description": "Welcome to The Garyvee Audio Experience, hosted by entrepreneur, CEO, investor, vlogger, and public speaker Gary Vaynerchuk. On this podcast you'll find a mix of my #AskGaryVee show episodes, keynote speeches on marketing and business, segments from my WEEKLYVEE video series, interviews and fireside chats I've given, as well as new and current thoughts I record originally for this audio experience!",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 82,
      "total_episodes": 2044,
      "listennotes_url": "https://www.listennotes.com/c/fe6864628066420c8103c94e91e72eb3/",
      "explicit_content": true,
      "latest_pub_date_ms": 1635156000000,
      "earliest_pub_date_ms": 1412179201956,
      "listen_score_global_rank": "0.01%"
    },
    {
      "id": "a409b8bb93f44054a7be2d6b30843899",
      "rss": "https://entrepreneuronfire.libsyn.com/rss",
      "type": "episodic",
      "email": "John@EntrepreneurOnFire.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9lbnRyZXByZW5ldXJvbmZpcmUubGlic3luLmNvbS9yc3M=",
        "spotify_url": "",
        "youtube_url": "https://www.youtube.com/channel/UCXfzpliAfdjParawJljHo2g",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "johnleedumas",
        "facebook_handle": "johnleedumas1",
        "instagram_handle": "johnleedumas"
      },
      "image": "https://production.listennotes.com/podcasts/entrepreneurs-on-fire-john-lee-dumas-of-_faXwKkD9hi-1WOhT7u6VQb.1400x1400.jpg",
      "title": "Entrepreneurs on Fire",
      "country": "United States",
      "website": "https://www.eofire.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        171,
        173,
        157,
        169,
        67,
        88,
        111,
        90,
        94,
        97
      ],
      "itunes_id": 564001633,
      "publisher": "John Lee Dumas of EOFire",
      "thumbnail": "https://production.listennotes.com/podcasts/entrepreneurs-on-fire-john-lee-dumas-of-cr_NzRxX1uS-1WOhT7u6VQb.300x300.jpg",
      "is_claimed": true,
      "description": "John Lee Dumas is the founder and host of the award winning podcast, Entrepreneurs On Fire. With over 100 million listens of his 3000+ episodes, JLD has turned Entrepreneurs On Fire into a media empire that generates over a million listens every month and 7-figures of NET annual revenue 8-years in a row. His first traditionally published book, The Common Path to Uncommon Success is the modern day version of Think and Grow Rich with a revolutionary 17-step roadmap to financial freedom and fulfillment. Learn more at UncommonSuccessBook.com",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 71,
      "total_episodes": 2790,
      "listennotes_url": "https://www.listennotes.com/c/a409b8bb93f44054a7be2d6b30843899/",
      "explicit_content": false,
      "latest_pub_date_ms": 1635150600000,
      "earliest_pub_date_ms": 1348297202688,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "499661f3589f42aaa1532673e0e0aedf",
      "rss": "https://rss.art19.com/smart-passive-income-podcast",
      "type": "episodic",
      "email": "podcasts@teamspi.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9yc3MuYXJ0MTkuY29tL3NtYXJ0LXBhc3NpdmUtaW5jb21lLXBvZGNhc3Q=",
        "spotify_url": "",
        "youtube_url": "https://www.youtube.com/user/smartpassiveincome",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "patflynn",
        "facebook_handle": "smartpassiveincome",
        "instagram_handle": "patflynn"
      },
      "image": "https://production.listennotes.com/podcasts/the-smart-passive-income-online-business-Qe7TJXl_NUu-NDa6-ySp9kw.1400x1400.jpg",
      "title": "The Smart Passive Income Online Business and Blogging Podcast",
      "country": "United States",
      "website": "https://art19.com/shows/smart-passive-income-podcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        173,
        93,
        171,
        144,
        157,
        97,
        98,
        67,
        94,
        111,
        115,
        127
      ],
      "itunes_id": 383084001,
      "publisher": "Pat Flynn",
      "thumbnail": "https://production.listennotes.com/podcasts/the-smart-passive-income-online-business-4QaYUNViG_j-NDa6-ySp9kw.300x300.jpg",
      "is_claimed": false,
      "description": "\n      Pat Flynn from The Smart Passive Income Blog reveals all of his online business and blogging strategies, income sources and killer marketing tips and tricks so you can be ahead of the curve with your online business or blog. Discover how you can create multiple passive income streams that work for you so that you can have the time and freedom to do what you love, whether it's traveling the world, or just living comfortably at home. Since 2008, he's been supporting his family with his many online businesses, and he's been openly sharing his wins, his losses, and all the lessons in between with the community of energetic but humble entrepreneurs who follow him. Self-proclaimed \"crash test dummy of online business\", you'll learn about building authority online, email marketing, building a team and outsourcing, content marketing, podcasting, search engine optimization, niche sites, social media strategies, how to get more traffic, creating online courses, affiliate marketing, and productivity tips so that you create something amazing without burning yourself out. It's a mix of interviews, special co-hosts and solo shows from Pat you're not going to want to miss. Hit subscribe, and get ready to change your life.\n    ",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 72,
      "total_episodes": 530,
      "listennotes_url": "https://www.listennotes.com/c/499661f3589f42aaa1532673e0e0aedf/",
      "explicit_content": false,
      "latest_pub_date_ms": 1634886000000,
      "earliest_pub_date_ms": 1279551600523,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "cba6cf06a87140bc9226efc8d530ed4d",
      "rss": "http://joeroganexp.joerogan.libsynpro.com/rss",
      "type": "episodic",
      "email": "joe@joerogan.net",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cDovL2pvZXJvZ2FuZXhwLmpvZXJvZ2FuLmxpYnN5bnByby5jb20vcnNz",
        "spotify_url": "",
        "youtube_url": "https://www.youtube.com/channel/UCzQUP1qoWDoEbmsQxvdjxgQ",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "joerogan",
        "facebook_handle": "JOEROGAN",
        "instagram_handle": "joerogan"
      },
      "image": "https://production.listennotes.com/podcasts/the-joe-rogan-experience-joe-rogan-AoKEVuC8I2B-s_ML5QqPi0v.1400x1400.jpg",
      "title": "The Joe Rogan Experience",
      "country": "United States",
      "website": "https://www.joerogan.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        216,
        173,
        77,
        133,
        129,
        122,
        99,
        88,
        127,
        93
      ],
      "itunes_id": 360084272,
      "publisher": "Joe Rogan",
      "thumbnail": "https://production.listennotes.com/podcasts/the-joe-rogan-experience-joe-rogan-32ylAiemYgR-s_ML5QqPi0v.300x300.jpg",
      "is_claimed": false,
      "description": "Conduit to the Gaian Mind",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 98,
      "total_episodes": 1,
      "listennotes_url": "https://www.listennotes.com/c/cba6cf06a87140bc9226efc8d530ed4d/",
      "explicit_content": true,
      "latest_pub_date_ms": 1524695830000,
      "earliest_pub_date_ms": 1524695830000,
      "listen_score_global_rank": "0.01%"
    }
  ]
}
```   
</details>



<details>
  <summary>Click to see response schema</summary>
  
```json
{
  "type": "object",
  "required": [
    "recommendations"
  ],
  "properties": {
    "recommendations": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "example": "4d3fe717742d4963a85562e9f84d8c79",
            "description": "Podcast id."
          },
          "rss": {
            "type": "string",
            "example": "https://sw7x7.libsyn.com/rss",
            "description": "RSS url of this podcast. This field is available only in the PRO/ENTERPRISE plan."
          },
          "type": {
            "enum": [
              "episodic",
              "serial"
            ],
            "type": "string",
            "example": "episodic",
            "description": "The type of this podcast - episodic or serial."
          },
          "email": {
            "type": "string",
            "example": "hello@example.com",
            "description": "The email of this podcast's producer. This field is available only in the PRO/ENTERPRISE plan."
          },
          "extra": {
            "type": "object",
            "properties": {
              "url1": {
                "type": "string",
                "description": "Url affiliated with this podcast"
              },
              "url2": {
                "type": "string",
                "description": "Url affiliated with this podcast"
              },
              "url3": {
                "type": "string",
                "description": "Url affiliated with this podcast"
              },
              "google_url": {
                "type": "string",
                "example": "https://play.google.com/music/listen?u=0#/ps/I7gdcrqcmvhfnhh2cyqkcg32tkq",
                "description": "Google Podcasts url for this podcast"
              },
              "spotify_url": {
                "type": "string",
                "example": "https://open.spotify.com/show/2rQJUP9Y3HxemiW3JHt9WV",
                "description": "Spotify url for this podcast"
              },
              "youtube_url": {
                "type": "string",
                "example": "https://www.youtube.com/sw7x7",
                "description": "YouTube url affiliated with this podcast"
              },
              "linkedin_url": {
                "type": "string",
                "description": "LinkedIn url affiliated with this podcast"
              },
              "wechat_handle": {
                "type": "string",
                "description": "WeChat username affiliated with this podcast"
              },
              "patreon_handle": {
                "type": "string",
                "example": "sw7x7",
                "description": "Patreon username affiliated with this podcast"
              },
              "twitter_handle": {
                "type": "string",
                "example": "SW7x7podcast",
                "description": "Twitter username affiliated with this podcast"
              },
              "facebook_handle": {
                "type": "string",
                "example": "sw7x7",
                "description": "Facebook username affiliated with this podcast"
              },
              "instagram_handle": {
                "type": "string",
                "example": "sw7x7",
                "description": "Instagram username affiliated with this podcast"
              }
            }
          },
          "image": {
            "type": "string",
            "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
            "description": "Image url for this podcast's artwork. If you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
          },
          "title": {
            "type": "string",
            "example": "Star Wars 7x7 | Star Wars News, Interviews, and More!",
            "description": "Podcast name."
          },
          "country": {
            "type": "string",
            "example": "United States",
            "description": "The country where this podcast is produced."
          },
          "website": {
            "type": "string",
            "example": "http://sw7x7.com/",
            "description": "Website url of this podcast."
          },
          "language": {
            "type": "string",
            "example": "English",
            "description": "The language of this podcast. You can get all supported languages from `GET /languages`."
          },
          "genre_ids": {
            "type": "array",
            "items": {
              "type": "integer",
              "description": "Genre ids."
            },
            "example": [
              138,
              86,
              160,
              68,
              82,
              100,
              101
            ]
          },
          "itunes_id": {
            "type": "integer",
            "example": 896354638,
            "description": "iTunes id for this podcast."
          },
          "publisher": {
            "type": "string",
            "example": "Planet Broadcasting",
            "description": "Podcast publisher name."
          },
          "thumbnail": {
            "type": "string",
            "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
            "description": "Thumbnail image url for this podcast's artwork (300x300)."
          },
          "is_claimed": {
            "type": "boolean",
            "example": true,
            "description": "Whether this podcast is claimed by its producer on [ListenNotes.com](https://www.ListenNotes.com)."
          },
          "description": {
            "type": "string",
            "example": "<p>The Star Wars 7x7 Podcast is Rebel-rousing fun for everyday Jedi, between 7 and 14 minutes a day, 7 days a week. Join host Allen Voivod for Star Wars news, history, interviews, trivia, and deep dives into the Star Wars story as told in movies, books, comics, games, cartoons, and more. Subscribe now for your daily dose of Star Wars joy. It's destiny unleashed!</p>",
            "description": "Html of this episode's full description"
          },
          "looking_for": {
            "type": "object",
            "properties": {
              "guests": {
                "type": "boolean",
                "example": true,
                "description": "Whether this podcast is looking for guests."
              },
              "cohosts": {
                "type": "boolean",
                "example": true,
                "description": "Whether this podcast is looking for cohosts."
              },
              "sponsors": {
                "type": "boolean",
                "example": true,
                "description": "Whether this podcast is looking for sponsors."
              },
              "cross_promotion": {
                "type": "boolean",
                "example": true,
                "description": "Whether this podcast is looking for cross promotion opportunities with other podcasts."
              }
            }
          },
          "listen_score": {
            "type": "integer",
            "example": 81,
            "description": "The estimated popularity score of a podcast compared to all other rss-based public podcasts in the world on a scale from 0 to 100.\nIf the score is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
          },
          "total_episodes": {
            "type": "integer",
            "example": 324,
            "description": "Total number of episodes in this podcast."
          },
          "listennotes_url": {
            "type": "string",
            "example": "https://www.listennotes.com/c/4d3fe717742d4963a85562e9f84d8c79/",
            "description": "The url of this podcast on [ListenNotes.com](https://www.ListenNotes.com)."
          },
          "explicit_content": {
            "type": "boolean",
            "example": false,
            "description": "Whether this podcast contains explicit language."
          },
          "latest_pub_date_ms": {
            "type": "integer",
            "example": 1557499770000,
            "description": "The published date of the latest episode of this podcast. In milliseconds"
          },
          "earliest_pub_date_ms": {
            "type": "integer",
            "example": 1470667902000,
            "description": "The published date of the oldest episode of this podcast. In milliseconds"
          },
          "listen_score_global_rank": {
            "type": "string",
            "example": "0.5%",
            "description": "The estimated popularity ranking of a podcast compared to all other rss-based public podcasts in the world.\nFor example, if the value is 0.5%, then this podcast is one of the top 0.5% most popular shows out of all podcasts globally, ranked by Listen Score.\nIf the ranking is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
          }
        }
      }
    }
  }
}
```   
</details>




### Fetch recommendations for an episode

Function Name: **fetch_recommendations_for_episode**

Fetch up to 8 episode recommendations based on the given episode id.

Example:
```python

from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)      

response = client.fetch_recommendations_for_episode(id='914a9deafa5340eeaa2859c77f275799')
            
print(response.json())

```

See all available parameters on the [API Docs page](https://www.listennotes.com/api/docs/#get-api-v2-episodes-id-recommendations).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "recommendations": [
    {
      "id": "8c9fcee265fc4f54bbca6afafcb8c28c",
      "link": "https://anchor.fm/thefirstmint/episodes/Roham-e15g29r?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/8c9fcee265fc4f54bbca6afafcb8c28c/",
      "image": "https://production.listennotes.com/podcasts/the-first-mint-nba-top-shot-podcast-the-zRoEZJmAXaW-NuBwOlnV0bt.1400x1400.jpg",
      "title": "Roham",
      "podcast": {
        "id": "fbdf83bb46ac4e0b9e807991719e210f",
        "image": "https://production.listennotes.com/podcasts/the-first-mint-nba-top-shot-podcast-the-zRoEZJmAXaW-NuBwOlnV0bt.1400x1400.jpg",
        "title": "The First Mint :: NBA Top Shot Podcast",
        "publisher": "The First Mint",
        "thumbnail": "https://production.listennotes.com/podcasts/the-first-mint-nba-top-shot-podcast-the-NIObareEkDi-NuBwOlnV0bt.300x300.jpg",
        "listen_score": 45,
        "listennotes_url": "https://www.listennotes.com/c/fbdf83bb46ac4e0b9e807991719e210f/",
        "listen_score_global_rank": "1%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/the-first-mint-nba-top-shot-podcast-the-NIObareEkDi-NuBwOlnV0bt.300x300.jpg",
      "description": "<p>Episode 83 of The First Mint.</p>\n<p>Roham.</p>\n<p>To kick off First Mint Fest, LG Doucet sat down with Roham Gharegozlou, the Founder &amp; CEO of Dapper Labs, the company behind NBA Top Shot and the Flow Blockchain.&nbsp;</p>",
      "pub_date_ms": 1628143512029,
      "guid_from_rss": "f148e49b-dfbf-4a94-8e3a-19bcb4ff1c17",
      "listennotes_url": "https://www.listennotes.com/e/8c9fcee265fc4f54bbca6afafcb8c28c/",
      "audio_length_sec": 3738,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/8c9fcee265fc4f54bbca6afafcb8c28c/#edit"
    },
    {
      "id": "cf20d584931945e692e7c0b437649010",
      "link": "http://www.fastcompany.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/cf20d584931945e692e7c0b437649010/",
      "image": "https://production.listennotes.com/podcasts/the-new-way-we-work-fast-company-ycLq6sXxbTk-fy29Abn3q_V.1400x1400.jpg",
      "title": "How NBA Top Shot is Transforming Trading Cards into NFTs",
      "podcast": {
        "id": "c4bedc7408564225b59a01a08da2c84b",
        "image": "https://production.listennotes.com/podcasts/the-new-way-we-work-fast-company-ycLq6sXxbTk-fy29Abn3q_V.1400x1400.jpg",
        "title": "The New Way We Work",
        "publisher": "Fast Company",
        "thumbnail": "https://production.listennotes.com/podcasts/the-new-way-we-work-fast-company-i5zQwlC9JYk-fy29Abn3q_V.300x300.jpg",
        "listen_score": 42,
        "listennotes_url": "https://www.listennotes.com/c/c4bedc7408564225b59a01a08da2c84b/",
        "listen_score_global_rank": "1.5%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/the-new-way-we-work-fast-company-i5zQwlC9JYk-fy29Abn3q_V.300x300.jpg",
      "description": "<p>On this episode, we\u2019re going to talk about the gaming industry, which is worth more than 160 billion dollars globally. Over the past year and a half, as people have gone from sheltering at home to tentative re-engagement with the world to\u2026.whatever is in store for us this fall, games have taken on an outsized role in our lives.\u00a0</p><p>Amy sat down with Roham Gharegozlou, CEO of Dapper Labs, the company behind NBA Top Shot, to discuss why he wants to do far more than just digitize the age-old pastime of buying and selling trading cards.</p>",
      "pub_date_ms": 1629709200009,
      "guid_from_rss": "d4de1a7c-0676-11ec-bc6f-472448d528ba",
      "listennotes_url": "https://www.listennotes.com/e/cf20d584931945e692e7c0b437649010/",
      "audio_length_sec": 1851,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/cf20d584931945e692e7c0b437649010/#edit"
    },
    {
      "id": "ed3f744e76d34193a56ac49cebf8f68a",
      "link": "https://www.morningbrew.com/business-casual-podcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/ed3f744e76d34193a56ac49cebf8f68a/",
      "image": "https://production.listennotes.com/podcasts/business-casual/are-nfts-the-future-of-vmkO-CorWKe-1Go68uyRgDH.1400x1400.jpg",
      "title": "Are NFTs the future of ownership?",
      "podcast": {
        "id": "db08706b3de9432dacef9f68c5a62de1",
        "image": "https://production.listennotes.com/podcasts/business-casual-morning-brew-thG8J_x1PMH-jWaUcpQC1F4.1400x1400.jpg",
        "title": "Business Casual",
        "publisher": "Morning Brew",
        "thumbnail": "https://production.listennotes.com/podcasts/business-casual-morning-brew-CY_Ax4EfsOr-jWaUcpQC1F4.300x300.jpg",
        "listen_score": 62,
        "listennotes_url": "https://www.listennotes.com/c/db08706b3de9432dacef9f68c5a62de1/",
        "listen_score_global_rank": "0.1%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/business-casual/are-nfts-the-future-of-Tal2dWAjCyg-1Go68uyRgDH.300x300.jpg",
      "description": "<p>Right now, it feels like the entire world is talking about NFTs, or nonfungible tokens. I'm sure you've seen the tweets and the headlines about NFTs and wondered \u2014 what the heck are these?</p><p>We're finding out from Roham Gharegozlou, the CEO of Dapper Labs. Dapper Labs is the blockchain based entertainment company behind NBA Top Shot, which is one of the most popular and hyped NFT series out there.</p>",
      "pub_date_ms": 1617262200000,
      "guid_from_rss": "gid://art19-episode-locator/V0/5DzuDdH4Gr-LDItdX9UjAAh0LQ8uJh_E-oLZgyAvu2I",
      "listennotes_url": "https://www.listennotes.com/e/ed3f744e76d34193a56ac49cebf8f68a/",
      "audio_length_sec": 2181,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/ed3f744e76d34193a56ac49cebf8f68a/#edit"
    },
    {
      "id": "230acd3bf6774079a43fd56c9fca788d",
      "link": "https://fiftyonepercent.podbean.com/e/dapper-labs-paving-the-way-for-consumer-blockchain-%E2%80%94-metaverse-musings-ep-16/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/230acd3bf6774079a43fd56c9fca788d/",
      "image": "https://production.listennotes.com/podcasts/the-delphi-podcast-tom-shaughnessy-FdG8P0YJ15C-b8TnOVkhWJc.1400x1400.jpg",
      "title": "Dapper Labs: Paving The Way For Consumer Blockchain \u2014 Metaverse Musings Ep 16",
      "podcast": {
        "id": "f0c9c7bb86464ac888b99c595c17b058",
        "image": "https://production.listennotes.com/podcasts/the-delphi-podcast-tom-shaughnessy-FdG8P0YJ15C-b8TnOVkhWJc.1400x1400.jpg",
        "title": "The Delphi Podcast",
        "publisher": "Tom Shaughnessy",
        "thumbnail": "https://production.listennotes.com/podcasts/the-delphi-podcast-tom-shaughnessy-dXUbH7jYuAw-b8TnOVkhWJc.300x300.jpg",
        "listen_score": 41,
        "listennotes_url": "https://www.listennotes.com/c/f0c9c7bb86464ac888b99c595c17b058/",
        "listen_score_global_rank": "2%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/the-delphi-podcast-tom-shaughnessy-dXUbH7jYuAw-b8TnOVkhWJc.300x300.jpg",
      "description": "<p>Host <a href='https://twitter.com/pierskicks'>Piers Kicks</a> sits down for Episode 16 of Metaverse Musings with <a href='https://twitter.com/rohamg'>Roham Gharegozlou</a> the Founder & CEO of Dapper Labs who built Crypto Kitties and NBA Top Shot. Most recently, they launched a new chain built entirely from the ground up after being dissatisfied with the scaling solutions available. Roham and his team are perhaps best positioned to comment on taking blockchain mainstream after not one, but two breakout successes with even more ambitious plans ahead of them.</p>\n\n<p>-</p>\n\n<p>Resources:</p>\n\n<ul><li style=\"font-weight:400;\">Guests' Twitter: <a href='https://twitter.com/rohamg'>https://twitter.com/rohamg</a></li>\n\n<li style=\"font-weight:400;\">Piers' Twitter: <a href='https://twitter.com/xxstevelee'>https://twitter.com/pierskicks</a></li>\n\n<li style=\"font-weight:400;\">Delphi Podcast Twitter:<a href='https://twitter.com/PodcastDelphi'> https://twitter.com/PodcastDelphi</a></li>\n\n</ul>\n<p>\nMore</p>\n\n<ul><li style=\"font-weight:400;\">Our Video interviews Can Be Viewed Here: <a href='https://tinyurl.com/ycvsp75h'>https://tinyurl.com/ycvsp75h</a></li>\n\n<li style=\"font-weight:400;\">Access Delphi's Research Here: <a href='https://www.delphidigital.io/'>https://www.delphidigital.io/</a></li>\n\n</ul>\n<p>\nDisclosures: This podcast is strictly informational and educational and is not investment advice or a solicitation to buy or sell any tokens or securities or to make any financial decisions. Do not trade or invest in any project, tokens, or securities based upon this podcast episode. The host may personally own tokens that are mentioned on the podcast. Lets Talk Bitcoin is a distribution partner for The Delphi Podcast, and our current show features paid sponsorships which may be featured at the start, middle, and/or the end of the episode. These sponsorships are for informational purposes only and are not a solicitation to use any product or service.\u00a0</p>",
      "pub_date_ms": 1612472990053,
      "guid_from_rss": "fiftyonepercent.podbean.com/fa007238-ad5f-3597-b530-088e196871ae",
      "listennotes_url": "https://www.listennotes.com/e/230acd3bf6774079a43fd56c9fca788d/",
      "audio_length_sec": 3802,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/230acd3bf6774079a43fd56c9fca788d/#edit"
    },
    {
      "id": "9aaeb046a07042d09ca5214a94f999b4",
      "link": "https://www.coindesk.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/9aaeb046a07042d09ca5214a94f999b4/",
      "image": "https://production.listennotes.com/podcasts/coindesk-reports/money-reimagined-inside-what-iJhcYnat3KX-CHxWD0gME75.1400x1400.jpg",
      "title": "MONEY REIMAGINED: Inside What Could Be NFTs 'Mainstream Moment' with Dapper Labs CEO Roham Gharegozlou",
      "podcast": {
        "id": "188eb6965eb048469400414acb5749ae",
        "image": "https://production.listennotes.com/podcasts/coindesk-reports-coindeskcom-2ZC6ING-TrD-TElxWfYmVpQ.1400x1400.jpg",
        "title": "CoinDesk Reports",
        "publisher": "CoinDesk.com",
        "thumbnail": "https://production.listennotes.com/podcasts/coindesk-reports-coindeskcom-vcYaEq5G_Ox-TElxWfYmVpQ.300x300.jpg",
        "listen_score": 29,
        "listennotes_url": "https://www.listennotes.com/c/188eb6965eb048469400414acb5749ae/",
        "listen_score_global_rank": "10%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/coindesk-reports/money-reimagined-inside-what-ezmdK02jRlc-CHxWD0gME75.300x300.jpg",
      "description": "<p>At the end of a high-energy week in the burgeoning digital art world, \u201cMoney Reimagined\u201d brings you the third and (for now) final edition of our NFT series.&nbsp;</p><p>In between recording this episode and publishing it two days later, a non-fungible token attached to a piece of digital art sold for a whopping $69.3 million. The sale, orchestrated by Christie\u2019s, turned the digital creator known as Beeple into the third-highest paid living artist. It also represented a high point in the media attention now swirling around this new, crypto-based technology.&nbsp;</p><p>So, it\u2019s appropriate we end on a note that grounds things in the reality of the technology and its potential to transform the creator economy generally, rather than being caught up in the celebrity story and media sensations. To do so, we talk with Roham Gharegozlou, the CEO and founder of Dapper Labs, the startup that in many respects is responsible for kicking off the entire NFT phenomenon.&nbsp;</p><p>We talk about the early days when Dapper created the ERC-721 standard on Ethereum and launched the popular CryptoKitties program. We talk about why the team made the decision to build its own blockchain, known as Flow, and to migrate the business there away from Ethereum. And we talk about where this rapidly evolving industry, with its competing platforms and wild debates over rights and opportunities, is going.</p><p>Join us for the conversation.&nbsp;</p><p><br></p><p><em>Image credit:&nbsp;</em>&nbsp;<a href=\"https://unsplash.com/@benjaminjsuter?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText\" rel=\"noopener noreferrer\" target=\"_blank\">Benjamin Suter</a>&nbsp;on&nbsp;<a href=\"https://unsplash.com/s/photos/basketball?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText\" rel=\"noopener noreferrer\" target=\"_blank\">Unsplash</a>,&nbsp;<em>modified by CoinDesk</em></p><p><br></p><p><br></p>",
      "pub_date_ms": 1615573111029,
      "guid_from_rss": "gid://art19-episode-locator/V0/TIr9Oc1xT-lNsuHS68HF9xWQ3oPV6E8w41xzcI0Ebdg",
      "listennotes_url": "https://www.listennotes.com/e/9aaeb046a07042d09ca5214a94f999b4/",
      "audio_length_sec": 2692,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/9aaeb046a07042d09ca5214a94f999b4/#edit"
    },
    {
      "id": "9552f754e1cb48f2a806006cbc095fc3",
      "link": "https://www.vox.com/recode-media-podcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/9552f754e1cb48f2a806006cbc095fc3/",
      "image": "https://production.listennotes.com/podcasts/recode-media-recode-h9zPK_1UkdB-1iPwTajLXlS.1400x1400.jpg",
      "title": "How Hollywood and the NBA are betting on NFTs",
      "podcast": {
        "id": "2aba49dc3fc04e3e96fe89f79a261798",
        "image": "https://production.listennotes.com/podcasts/recode-media-recode-h9zPK_1UkdB-1iPwTajLXlS.1400x1400.jpg",
        "title": "Recode Media",
        "publisher": "Recode",
        "thumbnail": "https://production.listennotes.com/podcasts/recode-media-recode-eHTVnkiXyu9-1iPwTajLXlS.300x300.jpg",
        "listen_score": 55,
        "listennotes_url": "https://www.listennotes.com/c/2aba49dc3fc04e3e96fe89f79a261798/",
        "listen_score_global_rank": "0.5%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/recode-media-recode-eHTVnkiXyu9-1iPwTajLXlS.300x300.jpg",
      "description": "<p>NFT\u2019s have been rising in popularity in recent months with franchises like the NBA partnering with Roham Gharegozlou\u2019s Dapper Labs to create Top Shot, or UTA\u2019s Brent Weinstein assisting entertainers to take advantage of it as well. Recode\u2019s Peter Kafka speaks to both of them about their journey getting into NFT\u2019s and blockchain, as well as The Verge\u2019s Mitchell Clark who breaks down the industry as a whole.</p><p><br></p><p><strong>Featuring</strong>: Roham Gharegozlou (<a href=\"https://twitter.com/rohamg\">@rohamg</a>) , CEO of Dapper Labs</p><p>Mitchell Clark (<a href=\"https://twitter.com/strawberrywell\">@strawberrywell</a>), reporter for The Verge</p><p>Brent Weinstein (<a href=\"https://twitter.com/brentweinstein\">@brentweinstein</a>), Partner &amp; Chief Innovator Officer for UTA</p><p><strong>Host</strong>: Peter Kafka\u00a0(<a href=\"https://twitter.com/pkafka\">@pkafka</a>), Senior Editor at Recode</p><p><strong>More to explore</strong>: <a href=\"https://pod.link/1080467174\">Subscribe for free to Recode Media</a>, Peter Kafka, one of the media industry's most acclaimed reporters, talks to business titans, journalists, comedians, and more to get their take on today's media landscape.</p><p><strong>About Recode by Vox</strong>: Recode by Vox helps you understand how tech is changing the world \u2014 and changing us.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1618286400032,
      "guid_from_rss": "03fb741a-9888-11eb-bfa6-b39b748294d3",
      "listennotes_url": "https://www.listennotes.com/e/9552f754e1cb48f2a806006cbc095fc3/",
      "audio_length_sec": 4729,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/9552f754e1cb48f2a806006cbc095fc3/#edit"
    },
    {
      "id": "23edf77bbc8e458eae6b4a70763e909a",
      "link": "https://product-hunt-radio.simplecast.com/episodes/how-to-bounce-back-as-a-maker-with-josh-howarth-XbOKZ76t?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/23edf77bbc8e458eae6b4a70763e909a/",
      "image": "https://production.listennotes.com/podcasts/product-hunt-radio-product-hunt-GWVKjh-0kgs-4qPNklrZI93.1400x1400.jpg",
      "title": "How to bounce back as a maker with Josh Howarth",
      "podcast": {
        "id": "40426582e3cd4dd2bf931f880e7374aa",
        "image": "https://production.listennotes.com/podcasts/product-hunt-radio-product-hunt-GWVKjh-0kgs-4qPNklrZI93.1400x1400.jpg",
        "title": "Product Hunt Radio",
        "publisher": "Product Hunt",
        "thumbnail": "https://production.listennotes.com/podcasts/product-hunt-radio-product-hunt--QOpzec69YV-4qPNklrZI93.300x300.jpg",
        "listen_score": 46,
        "listennotes_url": "https://www.listennotes.com/c/40426582e3cd4dd2bf931f880e7374aa/",
        "listen_score_global_rank": "1%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/product-hunt-radio-product-hunt--QOpzec69YV-4qPNklrZI93.300x300.jpg",
      "description": "<p>On this episode Abadesi talks to <a href=\"https://www.producthunt.com/@joshahowarth\">Josh Howarth</a>, co-founder of <a href=\"https://www.producthunt.com/posts/exploding-topics\">Exploding Topics</a>.</p><p>In this episode they talk about...</p><h2>His early days as a maker and what he would change if he could do things over again</h2><blockquote><p>\u201cIt\u2019s not the case that you build it and they will come. It took me two months to build and then I was like, now what? I hadn\u2019t thought at all about marketing channels.\u201d</p></blockquote><p>Josh talks about one of the projects that he created at the start of his journey to becoming a maker. He worked on a website plugin that he had seen other people implement where you spun a wheel to see what kind of discount code you would get for entering your email.</p><p>He says that he didn\u2019t realize how difficult getting distribution for the plugin would be and spent a lot of his time after releasing it reaching out to different people trying to get business to sign up. He achieved some revenue from it but it seemed to quickly fizzle out.</p><blockquote><p>\u201cYou can usually tell pretty quickly whether it will work or not if you\u2019re putting it out there for people to see. I probably should have quit sooner, like after two months instead of six on my previous project.\u201d</p></blockquote><p>He realized that he didn\u2019t have any passion for the project and that it would have been better to work on something that he cared deeply about. In hindsight, he also realized that he spent too much time working on it when it was fairly clear that it would always be a slog to try to keep the revenue up.</p><blockquote><p>\u201cIf the goal is to run your own business, you should go for a space that you\u2019re interested in because someone else who is passionate about it will beat you in the end.\u201d</p></blockquote><h2>The genesis and evolution of Exploding Topics and the lessons he\u2019s learned through the process</h2><blockquote><p>\u201cIt\u2019s 100 times easier to bootstrap a profitable online business if you ride one of these big market trends. You will grow with the opportunity and the competition won\u2019t be too fierce either. That\u2019s when I started to build a project that would spot these trends, to scratch my own itch.\u201d</p></blockquote><p>His experience with his previous project led him to research emerging trends that he could potentially build an online business out of. He did a lot of research and turned his research project into a web app when he realized that the results might be of use to other people as well.</p><blockquote><p>\u201cI didn\u2019t intend for it to become a product in itself but I decided I had solved this problem for me, I may as well turn it into a web app and see if other people are interested in it.\u201d</p></blockquote><p>He started to post the project on the web with lists of the top trends that he was seeing at the time, which proved to be very interesting to people. One day his site was near the top of Hacker News when his database went down, leading him to scramble to upgrade to a paid solution before losing all the traffic that he was getting.</p><p>He explains what he learned and what he would have done differently with Exploding Topics if he was starting over again.</p><blockquote><p>\u201cYou can feel it when you have something that people like and that is taking off. With the with the previous SaaS app it felt like I was pushing like a boulder uphill, but this thing was like snowball, everywhere I posted it people loved it and it just kept growing and growing.\u201d</p></blockquote><h2>How writing updates kept him accountable as a solo founder and his advice for finding a co-founder you can work well with</h2><blockquote><p>\u201cMake sure there\u2019s a good co-founder fit, make sure that you know them and they\u2019re going to bring a lot.\u201d</p></blockquote><p>Josh says that it was very gratifying to see people use Exploding Topics to create their own sites based on emerging trends. This was what he had hoped to do with his original project with the web plugin.</p><p>He says that it was important as a solo founder to write updates on Medium for his users. This encouraged him to make sure that he was making progress consistently on the site, because he needed to show his users and readers that he was always working on it. He also heard a lot of useful feedback from users who would use the site and sometimes even from people who were simply following his journey.</p><p>He ended up taking on a co-founder for Exploding Topics via the sale of his site. He explains what the most important attributes in a co-founder are and why he and his co-founder work well together.</p><blockquote><p>\u201cWriting updates and keeping people updated on your progress is fantastic as a sole founder because it keeps you accountable. It also helps to clarify your thoughts and direction. It helps to get support from other people who reach out to offer support, advice and guidance.\u201d</p></blockquote><p>We\u2019ll be back next week so be sure to subscribe on <a href=\"https://itunes.apple.com/podcast/product-hunt-radio/id862714883\">Apple Podcasts</a>, <a href=\"https://www.google.com/podcasts?feed=aHR0cHM6Ly9yc3Muc2ltcGxlY2FzdC5jb20vcG9kY2FzdHMvNjI2MS9yc3M%3D\">Google Podcasts</a>, <a href=\"https://open.spotify.com/show/4Ak6HpbVkLKGacY3E0GHL8?si=N8xXCfscQPapPSFIF2rP3w\">Spotify</a>, <a href=\"https://www.breaker.audio/product-hunt\">Breaker</a>, <a href=\"https://overcast.fm/itunes862714883/product-hunt-radio\">Overcast</a>, or wherever you listen to your favorite podcasts. \ud83d\ude38</p>",
      "pub_date_ms": 1587528007000,
      "guid_from_rss": "f80ea223-1249-4624-8885-29dd649f43ea",
      "listennotes_url": "https://www.listennotes.com/e/23edf77bbc8e458eae6b4a70763e909a/",
      "audio_length_sec": 2933,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/23edf77bbc8e458eae6b4a70763e909a/#edit"
    },
    {
      "id": "3663e1ba8f944df7956378ab332bf12b",
      "link": "https://www.gimletmedia.com/startup?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/3663e1ba8f944df7956378ab332bf12b/",
      "image": "https://production.listennotes.com/podcasts/startup-podcast-gimlet-14zU0c_MOmv-n9PpCBTQvoJ.1400x1400.jpg",
      "title": "Introducing How to Save a Planet",
      "podcast": {
        "id": "0d362b13399240de97602ef614acdcbc",
        "image": "https://production.listennotes.com/podcasts/startup-podcast-gimlet-14zU0c_MOmv-n9PpCBTQvoJ.1400x1400.jpg",
        "title": "StartUp Podcast",
        "publisher": "Gimlet",
        "thumbnail": "https://production.listennotes.com/podcasts/startup-podcast-gimlet-8If7QBKU5jb-n9PpCBTQvoJ.300x300.jpg",
        "listen_score": 76,
        "listennotes_url": "https://www.listennotes.com/c/0d362b13399240de97602ef614acdcbc/",
        "listen_score_global_rank": "0.01%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/startup-podcast-gimlet-8If7QBKU5jb-n9PpCBTQvoJ.300x300.jpg",
      "description": "<p>Does climate change freak you out? Want to know what we, collectively, can do about it? Us too. How to Save a Planet is a podcast that asks the big questions: what do we need to do to solve the climate crisis, and how do we get it done? </p><p>Join us, journalist Alex Blumberg and scientist and policy nerd Dr. Ayana Elizabeth Johnson, as we scour the Earth for solutions, talk to people who are making a difference, ask hard questions, crack dumb jokes and \u2014 episode by episode \u2014 figure out how to build the future we want.</p>",
      "pub_date_ms": 1598004000000,
      "guid_from_rss": "25666464-e19c-11ea-bb5d-b3b5dc0bbdef",
      "listennotes_url": "https://www.listennotes.com/e/3663e1ba8f944df7956378ab332bf12b/",
      "audio_length_sec": 714,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/3663e1ba8f944df7956378ab332bf12b/#edit"
    }
  ]
}
```   
</details>



<details>
  <summary>Click to see response schema</summary>
  
```json
{
  "type": "object",
  "required": [
    "recommendations"
  ],
  "properties": {
    "recommendations": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "example": "4d82e50314174754a3b603912448e812",
            "description": "Episode id."
          },
          "link": {
            "type": "string",
            "example": "https://www.npr.org/2020/01/22/798532179/soleimanis-iran",
            "description": "Web link of this episode."
          },
          "audio": {
            "type": "string",
            "example": "https://www.listennotes.com/e/p/11b34041e804491b9704d11f283c74de/",
            "description": "Audio url of this episode, which can be played directly."
          },
          "image": {
            "type": "string",
            "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
            "description": "Image url for this episode.\nIf an episode doesn't have its own image, then this field would be the url of the podcast artwork image.\nIf you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
          },
          "title": {
            "type": "string",
            "example": "Celebration Recap, Jason Fry and Christian Blauvelt Interviews \u2013 SWBW #101",
            "description": "Episode name."
          },
          "podcast": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "example": "4d3fe717742d4963a85562e9f84d8c79",
                "description": "Podcast id."
              },
              "image": {
                "type": "string",
                "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
                "description": "Image url for this podcast's artwork. If you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
              },
              "title": {
                "type": "string",
                "example": "Star Wars 7x7 | Star Wars News, Interviews, and More!",
                "description": "Podcast name."
              },
              "publisher": {
                "type": "string",
                "example": "Planet Broadcasting",
                "description": "Podcast publisher name."
              },
              "thumbnail": {
                "type": "string",
                "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
                "description": "Thumbnail image url for this podcast's artwork (300x300)."
              },
              "listen_score": {
                "type": "integer",
                "example": 81,
                "description": "The estimated popularity score of a podcast compared to all other rss-based public podcasts in the world on a scale from 0 to 100.\nIf the score is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
              },
              "listennotes_url": {
                "type": "string",
                "example": "https://www.listennotes.com/c/4d3fe717742d4963a85562e9f84d8c79/",
                "description": "The url of this podcast on [ListenNotes.com](https://www.ListenNotes.com)."
              },
              "listen_score_global_rank": {
                "type": "string",
                "example": "0.5%",
                "description": "The estimated popularity ranking of a podcast compared to all other rss-based public podcasts in the world.\nFor example, if the value is 0.5%, then this podcast is one of the top 0.5% most popular shows out of all podcasts globally, ranked by Listen Score.\nIf the ranking is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
              }
            }
          },
          "thumbnail": {
            "type": "string",
            "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
            "description": "Thumbnail image (300x300) url for this episode.\nIf an episode doesn't have its own image, then this field would be the url of the podcast artwork thumbnail image.\n"
          },
          "description": {
            "type": "string",
            "example": "<p>Disney chief Bob Iger shared news about Star Wars movies in 2020 and beyond, but some media outlets gave conflicting reports about it. Here's the real scoop. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>\n",
            "description": "Html of this episode's full description"
          },
          "pub_date_ms": {
            "type": "integer",
            "example": 1474873200000,
            "description": "Published date for this episode. In millisecond."
          },
          "listennotes_url": {
            "type": "string",
            "example": "https://www.listennotes.com/e/4d82e50314174754a3b603912448e812/",
            "description": "The url of this episode on [ListenNotes.com](https://www.ListenNotes.com)."
          },
          "audio_length_sec": {
            "type": "integer",
            "example": 567,
            "description": "Audio length of this episode. In seconds."
          },
          "explicit_content": {
            "type": "boolean",
            "example": false,
            "description": "Whether this podcast contains explicit language."
          },
          "maybe_audio_invalid": {
            "type": "boolean",
            "example": false,
            "description": "Whether or not this episode's audio is invalid. Podcasters may delete the original audio."
          },
          "listennotes_edit_url": {
            "type": "string",
            "example": "https://www.listennotes.com/e/11b34041e804491b9704d11f283c74de/#edit",
            "description": "Edit url of this episode where you can update the audio url if you find the audio is broken."
          }
        }
      }
    }
  }
}
```   
</details>




### Batch fetch basic meta data for episodes

Function Name: **batch_fetch_episodes**

Batch fetch basic meta data for up to 10 episodes. This endpoint could be used to implement custom playlists for individual episodes. For detailed meta data of an individual episode, you need to use `GET /episodes/{id}`. This endpoint is available only in the PRO/ENTERPRISE plan.


Example:
```python

from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)      

response = client.batch_fetch_episodes(
    ids='c577d55b2b2b483c969fae3ceb58e362,0f34a9099579490993eec9e8c8cebb82')
            
print(response.json())

```

See all available parameters on the [API Docs page](https://www.listennotes.com/api/docs/#post-api-v2-episodes).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "episodes": [
    {
      "id": "c577d55b2b2b483c969fae3ceb58e362",
      "link": "https://www.listenmoneymatters.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/c577d55b2b2b483c969fae3ceb58e362/",
      "image": "https://production.listennotes.com/podcasts/listen-money-matters-free-your-inner-lPXW7V_6n0C-SJEHNr84kVg.1400x1400.jpg",
      "title": "Do Things That Scale: Starting a Business That Will Take Off",
      "podcast": {
        "id": "3302bc71139541baa46ecb27dbf6071a",
        "image": "https://production.listennotes.com/podcasts/listen-money-matters-free-your-inner-lPXW7V_6n0C-SJEHNr84kVg.1400x1400.jpg",
        "title": "Listen Money Matters - Free your inner financial badass. All the stuff you should know about personal finance.",
        "publisher": "ListenMoneyMatters.com | Andrew Fiebert and Matt Giovanisci",
        "thumbnail": "https://production.listennotes.com/podcasts/listen-money-matters-free-your-inner-d5If074qkhz-SJEHNr84kVg.300x300.jpg",
        "listen_score": 66,
        "listennotes_url": "https://www.listennotes.com/c/3302bc71139541baa46ecb27dbf6071a/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/listen-money-matters-free-your-inner-d5If074qkhz-SJEHNr84kVg.300x300.jpg",
      "description": "<p>There are only so many hours in a day so you need to build a business that can grow while you\u2019re sleeping, on vacation, or working on your next business. You have to do things that scale when starting a business that will take off. While we are discussing scaling a business, there are plenty of other areas of life that you can scale including investing and video games. To scale a business means to create a system, product, or service that can generate more money through some resource that isn\u2019t your time. Scale is a concept that is meant to support infinite growth. When starting a business, you want to find ways to apply your time and money that are scalable and to shift your focus from things with a hard maximum return to things that have the potential to be infinitely scalable.</p><p>\u00a0</p><p><a href=\"https://www.listenmoneymatters.com/starting-a-business-that-scales/%20%E2%80%8E\">Full Article Here</a></p><p><strong></p><p>Show Notes</p><p></strong></p><p><a href=\"http://portbrewing.com/beer/board-meeting/\"><strong>Board Meeting:</strong></a> A coffee flavored brown ale.</p><p><a href=\"https://www.listenmoneymatters.com/toolbox/\"><strong>Tool Box:</strong></a> All the best stuff to manage your money.</p><p><a href=\"http://paulgraham.com/ds.html\"><strong>Do Things That Don't Scale:</strong></a> The essay Andrew mentioned by Paul Graham.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://megaphone.fm/adchoices\">megaphone.fm/adchoices</a></p>",
      "pub_date_ms": 1528088400089,
      "guid_from_rss": "https://www.listenmoneymatters.com/?p=46659",
      "listennotes_url": "https://www.listennotes.com/e/c577d55b2b2b483c969fae3ceb58e362/",
      "audio_length_sec": 3683,
      "explicit_content": true,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/c577d55b2b2b483c969fae3ceb58e362/#edit"
    },
    {
      "id": "0f34a9099579490993eec9e8c8cebb82",
      "link": "https://cms.megaphone.fm/channel/business-unusual-with-barbara-corcoran?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/0f34a9099579490993eec9e8c8cebb82/",
      "image": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-MDXGCRbYJ2z-aZPn3Ic47rx.1400x1400.jpg",
      "title": "35: Don\u2019t Make Your Landlord Rich",
      "podcast": {
        "id": "68faf62be97149c280ebcc25178aa731",
        "image": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-MDXGCRbYJ2z-aZPn3Ic47rx.1400x1400.jpg",
        "title": "Business Unusual with Barbara Corcoran",
        "publisher": "Barbara Corcoran",
        "thumbnail": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-Oqs7L9Yfpci-aZPn3Ic47rx.300x300.jpg",
        "listen_score": 57,
        "listennotes_url": "https://www.listennotes.com/c/68faf62be97149c280ebcc25178aa731/",
        "listen_score_global_rank": "0.5%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-Oqs7L9Yfpci-aZPn3Ic47rx.300x300.jpg",
      "description": "<p>If you\u2019re starting a new business, you need to keep costs low \u2013 so renting is the way to go, right?\n\nI say no! I\u2019ll tell you why you should scrape together the cash to buy your business headquarters from the get-go.\u00a0\n\nAlso, I\u2019ll answer some more of your great questions about how to get the press to pay attention to your little mom and pop shop and what to do about a toxic work environment.\n\nGot a business question you want to ask me? Tweet it @BarbaraCorcoran and I may just answer it on a future episode!\n\nFollow Business Unusual with Barbara Corcoran on iHeartRadio, or subscribe wherever you listen to podcasts.\n\nThis episode of Business Unusual with Barbara Corcoran is presented by\u00a0On Deck Business Loans\u00a0(http://www.ondeck.com/barbara).\u00a0\u00a0\u00a0</p>",
      "pub_date_ms": 1546232460080,
      "guid_from_rss": "gid://art19-episode-locator/V0/Q3wpi1LpU7b7vFqc3_T1BsaIqZJruq-YWy3Ud4sJnJo",
      "listennotes_url": "https://www.listennotes.com/e/0f34a9099579490993eec9e8c8cebb82/",
      "audio_length_sec": 486,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/0f34a9099579490993eec9e8c8cebb82/#edit"
    }
  ]
}
```   
</details>



<details>
  <summary>Click to see response schema</summary>
  
```json
{
  "type": "object",
  "required": [
    "episodes"
  ],
  "properties": {
    "episodes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "example": "4d82e50314174754a3b603912448e812",
            "description": "Episode id."
          },
          "link": {
            "type": "string",
            "example": "https://www.npr.org/2020/01/22/798532179/soleimanis-iran",
            "description": "Web link of this episode."
          },
          "audio": {
            "type": "string",
            "example": "https://www.listennotes.com/e/p/11b34041e804491b9704d11f283c74de/",
            "description": "Audio url of this episode, which can be played directly."
          },
          "image": {
            "type": "string",
            "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
            "description": "Image url for this episode.\nIf an episode doesn't have its own image, then this field would be the url of the podcast artwork image.\nIf you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
          },
          "title": {
            "type": "string",
            "example": "Celebration Recap, Jason Fry and Christian Blauvelt Interviews \u2013 SWBW #101",
            "description": "Episode name."
          },
          "podcast": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "example": "4d3fe717742d4963a85562e9f84d8c79",
                "description": "Podcast id."
              },
              "image": {
                "type": "string",
                "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
                "description": "Image url for this podcast's artwork. If you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
              },
              "title": {
                "type": "string",
                "example": "Star Wars 7x7 | Star Wars News, Interviews, and More!",
                "description": "Podcast name."
              },
              "publisher": {
                "type": "string",
                "example": "Planet Broadcasting",
                "description": "Podcast publisher name."
              },
              "thumbnail": {
                "type": "string",
                "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
                "description": "Thumbnail image url for this podcast's artwork (300x300)."
              },
              "listen_score": {
                "type": "integer",
                "example": 81,
                "description": "The estimated popularity score of a podcast compared to all other rss-based public podcasts in the world on a scale from 0 to 100.\nIf the score is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
              },
              "listennotes_url": {
                "type": "string",
                "example": "https://www.listennotes.com/c/4d3fe717742d4963a85562e9f84d8c79/",
                "description": "The url of this podcast on [ListenNotes.com](https://www.ListenNotes.com)."
              },
              "listen_score_global_rank": {
                "type": "string",
                "example": "0.5%",
                "description": "The estimated popularity ranking of a podcast compared to all other rss-based public podcasts in the world.\nFor example, if the value is 0.5%, then this podcast is one of the top 0.5% most popular shows out of all podcasts globally, ranked by Listen Score.\nIf the ranking is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
              }
            }
          },
          "thumbnail": {
            "type": "string",
            "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
            "description": "Thumbnail image (300x300) url for this episode.\nIf an episode doesn't have its own image, then this field would be the url of the podcast artwork thumbnail image.\n"
          },
          "description": {
            "type": "string",
            "example": "<p>Disney chief Bob Iger shared news about Star Wars movies in 2020 and beyond, but some media outlets gave conflicting reports about it. Here's the real scoop. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>\n",
            "description": "Html of this episode's full description"
          },
          "pub_date_ms": {
            "type": "integer",
            "example": 1474873200000,
            "description": "Published date for this episode. In millisecond."
          },
          "listennotes_url": {
            "type": "string",
            "example": "https://www.listennotes.com/e/4d82e50314174754a3b603912448e812/",
            "description": "The url of this episode on [ListenNotes.com](https://www.ListenNotes.com)."
          },
          "audio_length_sec": {
            "type": "integer",
            "example": 567,
            "description": "Audio length of this episode. In seconds."
          },
          "explicit_content": {
            "type": "boolean",
            "example": false,
            "description": "Whether this podcast contains explicit language."
          },
          "maybe_audio_invalid": {
            "type": "boolean",
            "example": false,
            "description": "Whether or not this episode's audio is invalid. Podcasters may delete the original audio."
          },
          "listennotes_edit_url": {
            "type": "string",
            "example": "https://www.listennotes.com/e/11b34041e804491b9704d11f283c74de/#edit",
            "description": "Edit url of this episode where you can update the audio url if you find the audio is broken."
          }
        }
      }
    }
  }
}
```   
</details>




### Batch fetch basic meta data for podcasts

Function Name: **batch_fetch_podcasts**

Batch fetch basic meta data for up to 10 podcasts.
This endpoint could be used to build something like OPML import,
allowing users to import a bunch of podcasts via rss urls.
For detailed meta data (including episodes) of an individual podcast, you need to use `GET /podcasts/{id}`. This endpoint is available only in the PRO/ENTERPRISE plan.


Example:
```python

from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)      

response = client.batch_fetch_podcasts(
    ids='3302bc71139541baa46ecb27dbf6071a,68faf62be97149c280ebcc25178aa731,9cf19c590ff0484d97b18b329fed0c6a',
    itunes_ids='1457514703,1386234384,659155419', show_latest_episodes=1)
            
print(response.json())

```

See all available parameters on the [API Docs page](https://www.listennotes.com/api/docs/#post-api-v2-podcasts).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "podcasts": [
    {
      "id": "37589a3e121e40debe4cef3d9638932a",
      "rss": "http://exponent.fm/feed/",
      "type": "episodic",
      "email": "bjthompson@mac.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cDovL2V4cG9uZW50LmZtL2ZlZWQv",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "exponentfm",
        "facebook_handle": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-4-khvom1d3W-OaJSjb4xQv3.1400x1400.jpg",
      "title": "Exponent",
      "country": "United States",
      "website": "http://exponent.fm?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        127,
        67,
        129,
        93,
        157,
        149
      ],
      "itunes_id": 826420969,
      "publisher": "Ben Thompson / James Allworth",
      "thumbnail": "https://production.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-lRYU3p4xQ-m-OaJSjb4xQv3.300x300.jpg",
      "is_claimed": false,
      "description": "A podcast about tech and society, hosted by Ben Thompson and James Allworth",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 61,
      "total_episodes": 196,
      "listennotes_url": "https://www.listennotes.com/c/37589a3e121e40debe4cef3d9638932a/",
      "explicit_content": false,
      "latest_pub_date_ms": 1634548480000,
      "earliest_pub_date_ms": 1392899826195,
      "listen_score_global_rank": "0.1%"
    },
    {
      "id": "68faf62be97149c280ebcc25178aa731",
      "rss": "https://feeds.megaphone.fm/business-unusual-with-barbara-corcoran",
      "type": "episodic",
      "email": "businessunusual@barbaracorcoran.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5tZWdhcGhvbmUuZm0vYnVzaW5lc3MtdW51c3VhbC13aXRoLWJhcmJhcmEtY29yY29yYW4=",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "BarbaraCorcoran",
        "facebook_handle": "TheBarbaraCorcoran",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-MDXGCRbYJ2z-aZPn3Ic47rx.1400x1400.jpg",
      "title": "Business Unusual with Barbara Corcoran",
      "country": "United States",
      "website": "https://cms.megaphone.fm/channel/business-unusual-with-barbara-corcoran?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        157,
        98,
        94,
        93,
        67
      ],
      "itunes_id": 1378685290,
      "publisher": "Barbara Corcoran",
      "thumbnail": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-Oqs7L9Yfpci-aZPn3Ic47rx.300x300.jpg",
      "is_claimed": false,
      "description": "I\u2019m smart at getting to where I want to go, and I can teach you how to do it! I had 22 jobs before starting my real estate company with a $1000 loan and built it into a $5 billion business. Today I\u2019m a \u2019Shark\u2019 on ABC\u2019s hit show \"Shark Tank.\" It didn\u2019t take a fancy degree to get here but took street smarts and a lot of courage. Life is too short to waste your time practicing someone else\u2019s fancy theory on success. I give you the straight talk and the confidence to get there. Got a question? Call me at 888-BARBARA. Subscribe to Business Unusual with Barbara Corcoran wherever you listen to podcasts.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 57,
      "total_episodes": 122,
      "listennotes_url": "https://www.listennotes.com/c/68faf62be97149c280ebcc25178aa731/",
      "explicit_content": false,
      "latest_pub_date_ms": 1634647424000,
      "earliest_pub_date_ms": 1525202794115,
      "listen_score_global_rank": "0.5%"
    },
    {
      "id": "9cf19c590ff0484d97b18b329fed0c6a",
      "rss": "https://feeds.megaphone.fm/binge-mode",
      "type": "serial",
      "email": "info@theringer.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5tZWdhcGhvbmUuZm0vYmluZ2UtbW9kZQ==",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "binge_mode",
        "facebook_handle": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/binge-mode-marvel-the-ringer-QZoDCyP6hev-BdPpshCaFDu.1400x1400.jpg",
      "title": "Binge Mode: Marvel",
      "country": "United States",
      "website": "https://art19.com/shows/binge-mode-game-of-thrones?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        122,
        162,
        67,
        68
      ],
      "itunes_id": 1243247464,
      "publisher": "The Ringer",
      "thumbnail": "https://production.listennotes.com/podcasts/binge-mode-marvel-the-ringer-bqVntBmw3ij-BdPpshCaFDu.300x300.jpg",
      "is_claimed": false,
      "description": "The Ringer\u2019s Mallory Rubin and Jason Concepcion return to take their signature deep dives into the Marvel Cinematic Universe, covering all 23 films!",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 79,
      "total_episodes": 41,
      "listennotes_url": "https://www.listennotes.com/c/9cf19c590ff0484d97b18b329fed0c6a/",
      "explicit_content": true,
      "latest_pub_date_ms": 1616634382000,
      "earliest_pub_date_ms": 1496277060040,
      "listen_score_global_rank": "0.01%"
    },
    {
      "id": "3302bc71139541baa46ecb27dbf6071a",
      "rss": "https://feeds.megaphone.fm/listen-money-matters",
      "type": "episodic",
      "email": "listenmoneymatters@gmail.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5tZWdhcGhvbmUuZm0vbGlzdGVuLW1vbmV5LW1hdHRlcnM=",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "MoneyMattersMan",
        "facebook_handle": "ListenMoneyMatters",
        "instagram_handle": "listenmoneymatters"
      },
      "image": "https://production.listennotes.com/podcasts/listen-money-matters-free-your-inner-lPXW7V_6n0C-SJEHNr84kVg.1400x1400.jpg",
      "title": "Listen Money Matters - Free your inner financial badass. All the stuff you should know about personal finance.",
      "country": "United States",
      "website": "https://www.listenmoneymatters.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        98,
        144,
        111,
        67,
        93,
        127,
        128
      ],
      "itunes_id": 736826307,
      "publisher": "ListenMoneyMatters.com | Andrew Fiebert and Matt Giovanisci",
      "thumbnail": "https://production.listennotes.com/podcasts/listen-money-matters-free-your-inner-d5If074qkhz-SJEHNr84kVg.300x300.jpg",
      "is_claimed": false,
      "description": "Honest and uncensored - this is not your father\u2019s boring finance show. This show brings much needed ACTIONABLE advice to a people who hate being lectured about personal finance from the out-of-touch one percent. Andrew and Matt are relatable, funny, and brash. Their down-to-earth discussions about money are entertaining whether you\u2019re a financial whiz or just starting out. To be a part of the show and get your financial questions answered, send an email to listenmoneymatters@gmail.com.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 66,
      "total_episodes": 505,
      "listennotes_url": "https://www.listennotes.com/c/3302bc71139541baa46ecb27dbf6071a/",
      "explicit_content": true,
      "latest_pub_date_ms": 1589169600000,
      "earliest_pub_date_ms": 1383138000504,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "613aa80ec729409ea0db4265cf3e3899",
      "rss": "https://www.npr.org/rss/podcast.php?id=510331",
      "type": "serial",
      "email": "podcasts@npr.org",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "nprlifekit",
        "facebook_handle": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/find-money-you-didnt-know-you-had-npr-WuHnh0Poiyb-IDT1XPkq4rb.1400x1400.jpg",
      "title": "Find Money You Didn't Know You Had",
      "country": "United States",
      "website": "https://www.npr.org/lifekit?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        67
      ],
      "itunes_id": 1446899299,
      "publisher": "NPR",
      "thumbnail": "https://production.listennotes.com/podcasts/find-money-you-didnt-know-you-had-npr-Dl7VZ86KyNA-IDT1XPkq4rb.300x300.jpg",
      "is_claimed": false,
      "description": "Don't let your money disappear into a whirlpool of bank fees, takeout orders, and lattes! We'll learn how to free up more money so you can spend it on \u2014 and save it for \u2014 the things you value most.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": null,
      "total_episodes": 8,
      "listennotes_url": "https://www.listennotes.com/c/613aa80ec729409ea0db4265cf3e3899/",
      "explicit_content": false,
      "latest_pub_date_ms": 1574665259000,
      "earliest_pub_date_ms": 1544800017000,
      "listen_score_global_rank": null
    },
    {
      "id": "c5ce6c02cbf1486496206829f7d42e8e",
      "rss": "https://feeds.megaphone.fm/marketsnacks-daily",
      "type": "episodic",
      "email": "podcasts@cadence13.com",
      "extra": {
        "url1": "http://www.marketsnacks.com/",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5tZWdhcGhvbmUuZm0vbWFya2V0c25hY2tzLWRhaWx5",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "marketsnacks",
        "facebook_handle": "MarketSnacks",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-F_0RTie7PzG-kmx0XIZTAys.1400x1400.jpg",
      "title": "Snacks Daily",
      "country": "United States",
      "website": "https://snacks.robinhood.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        67,
        99,
        98,
        95
      ],
      "itunes_id": 1386234384,
      "publisher": "Robinhood Financial, LLC",
      "thumbnail": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-Yp5jkwN1GKi-kmx0XIZTAys.300x300.jpg",
      "is_claimed": false,
      "description": "Digestible financial news. Get smarter fast with an entertaining breakdown of our top 3 business stories in 15 minutes. Pairs perfectly with your commute, workout, or morning oatmeal ritual. Hosted by Jack Kramer and Nick Martell.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 72,
      "total_episodes": 609,
      "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
      "explicit_content": false,
      "latest_pub_date_ms": 1635152400000,
      "earliest_pub_date_ms": 1553519100604,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "3a2a6ddd549f4df0b876e7315fa1a319",
      "rss": "https://philosophizethis.libsyn.com/rss",
      "type": "episodic",
      "email": "steve@stephenwestshow.com",
      "extra": {
        "url1": "http://philosophizethis.org/",
        "url2": "",
        "url3": "",
        "google_url": "https://play.google.com/music/listen?u=0&gclid=COmlsNrWmc0CFcimfgodxAYFGw&gclsrc=ds#/ps/Iszi3nzoe3p22hsxpoe3i2jmxxy",
        "spotify_url": "https://open.spotify.com/show/2Shpxw7dPoxRJCdfFXTWLE",
        "youtube_url": "https://www.youtube.com/channel/UCjnpuIGovFFUBLG5BeHzTag",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "philosophizethis",
        "twitter_handle": "iamstephenwest",
        "facebook_handle": "Philosophizethisshow",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/philosophize-this-stephen-west-Y2PvRelyrIN-ivQCfmkqM_h.1400x1400.jpg",
      "title": "Philosophize This!",
      "country": "United States",
      "website": "http://www.philosophizethis.org?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        111,
        125,
        126,
        67,
        122,
        133
      ],
      "itunes_id": 659155419,
      "publisher": "Stephen West",
      "thumbnail": "https://production.listennotes.com/podcasts/philosophize-this-stephen-west-oSuiCW7Bz8T-ivQCfmkqM_h.300x300.jpg",
      "is_claimed": false,
      "description": "Beginner friendly if listened to in order! For anyone interested in an educational podcast about philosophy where you don't need to be a graduate-level philosopher to understand it. In chronological order, the thinkers and ideas that forged the world we live in are broken down and explained.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 79,
      "total_episodes": 158,
      "listennotes_url": "https://www.listennotes.com/c/3a2a6ddd549f4df0b876e7315fa1a319/",
      "explicit_content": false,
      "latest_pub_date_ms": 1633469847000,
      "earliest_pub_date_ms": 1370556600155,
      "listen_score_global_rank": "0.01%"
    },
    {
      "id": "bacb2f7ca7a04ed0b21efd21192f5014",
      "rss": "https://feeds.megaphone.fm/espionage",
      "type": "episodic",
      "email": "support@parcast.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "ParcastNetwork",
        "facebook_handle": "parcast",
        "instagram_handle": "parcast"
      },
      "image": "https://production.listennotes.com/podcasts/espionage-parcast-network-X9AT-uYo8Nq-ReK0QUN-VP_.1400x1400.jpg",
      "title": "Espionage",
      "country": "United States",
      "website": "https://www.parcast.com/espionage?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        99,
        67
      ],
      "itunes_id": 1457514703,
      "publisher": "Parcast Network",
      "thumbnail": "https://production.listennotes.com/podcasts/espionage-parcast-network-j-WLEmNQ4PB-ReK0QUN-VP_.300x300.jpg",
      "is_claimed": false,
      "description": "Not all spies look like James Bond and Ethan Hunt. Most of them look like ordinary people, which makes them all the more dangerous... So what does it really take to be a spy? Every week, we cover a real-life spy mission: the stakes, the deception, the gadgets, and how it changed the course of history. Each two-part series follows one mission of a historic spy, and if they made it out alive. Espionage is a production of Cutler Media and part of the Parcast Network.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 64,
      "total_episodes": 85,
      "listennotes_url": "https://www.listennotes.com/c/bacb2f7ca7a04ed0b21efd21192f5014/",
      "explicit_content": false,
      "latest_pub_date_ms": 1623049260000,
      "earliest_pub_date_ms": 1553471173023,
      "listen_score_global_rank": "0.1%"
    }
  ],
  "latest_episodes": [
    {
      "id": "9447ce07dd2345618054b04b733e4ad5",
      "link": "https://snacks.robinhood.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/9447ce07dd2345618054b04b733e4ad5/",
      "image": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-F_0RTie7PzG-kmx0XIZTAys.1400x1400.jpg",
      "title": "Google\u2019s $399 smartphone, Crocs\u2019 comeback, and GM\u2019s robotaxi Cruise snags $1B",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-F_0RTie7PzG-kmx0XIZTAys.1400x1400.jpg",
        "title": "Snacks Daily",
        "publisher": "Robinhood Financial, LLC",
        "thumbnail": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-Yp5jkwN1GKi-kmx0XIZTAys.300x300.jpg",
        "listen_score": 72,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-Yp5jkwN1GKi-kmx0XIZTAys.300x300.jpg",
      "description": "<p>Google\u2019s I/O event day enjoyed protests, AI tech to screen fake\u00a0calls, and a $399 Pixel phone. General Motors acquired self-driving car startup Cruise when it was worth $1B \u2014 Now it\u2019s worth $19B, and wants robotaxis on streets this year. And Crocs shares have nearly doubled in the past year, so we look at why.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1557309360573,
      "guid_from_rss": "cc706928-7143-11e9-94ec-bf6cee57c71d",
      "listennotes_url": "https://www.listennotes.com/e/9447ce07dd2345618054b04b733e4ad5/",
      "audio_length_sec": 916,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/9447ce07dd2345618054b04b733e4ad5/#edit"
    },
    {
      "id": "68d378e5b029431dbaca6acf7ce396f2",
      "link": "https://snacks.robinhood.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/68d378e5b029431dbaca6acf7ce396f2/",
      "image": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-F_0RTie7PzG-kmx0XIZTAys.1400x1400.jpg",
      "title": "Big Trade War update, Apple\u2019s bought 20+ companies in 6 months, and the largest VC investment in Latin America ever",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-F_0RTie7PzG-kmx0XIZTAys.1400x1400.jpg",
        "title": "Snacks Daily",
        "publisher": "Robinhood Financial, LLC",
        "thumbnail": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-Yp5jkwN1GKi-kmx0XIZTAys.300x300.jpg",
        "listen_score": 72,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-Yp5jkwN1GKi-kmx0XIZTAys.300x300.jpg",
      "description": "<p>The Trade War was supposed to end this week with a peace\u00a0deal. That\u2019s not looking likely, and we\u2019ll tell you why. Apple\u2019s CEO casually dropped that the company\u2019s bought over 20 startups over the last six months. And super delivery app Rappi just raised $1B from Softbank, making it the biggest Latin American venture\u00a0investment ever.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1557222960574,
      "guid_from_rss": "e46adbce-705f-11e9-baa5-1779edf441e3",
      "listennotes_url": "https://www.listennotes.com/e/68d378e5b029431dbaca6acf7ce396f2/",
      "audio_length_sec": 1039,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/68d378e5b029431dbaca6acf7ce396f2/#edit"
    },
    {
      "id": "402e67e65e2a4575ab2704a977a2b4b5",
      "link": "https://cms.megaphone.fm/channel/business-unusual-with-barbara-corcoran?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/402e67e65e2a4575ab2704a977a2b4b5/",
      "image": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-MDXGCRbYJ2z-aZPn3Ic47rx.1400x1400.jpg",
      "title": "53: Something About Mary",
      "podcast": {
        "id": "68faf62be97149c280ebcc25178aa731",
        "image": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-MDXGCRbYJ2z-aZPn3Ic47rx.1400x1400.jpg",
        "title": "Business Unusual with Barbara Corcoran",
        "publisher": "Barbara Corcoran",
        "thumbnail": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-Oqs7L9Yfpci-aZPn3Ic47rx.300x300.jpg",
        "listen_score": 57,
        "listennotes_url": "https://www.listennotes.com/c/68faf62be97149c280ebcc25178aa731/",
        "listen_score_global_rank": "0.5%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-Oqs7L9Yfpci-aZPn3Ic47rx.300x300.jpg",
      "description": "<p><strong>CNBC Producer Mary Hanan has the TV business dream job. I met Mary when she interviewed me for CNBC's \"The Brave Ones\" and I knew immediately I had to have her on the show. So I turned the tables on Mary and put her in the hot seat to learn how she worked her way up to the top, and she shared many of the interesting situations she found herself in along the way.Got a question for me? Call me at 888-BARBARA to ask a question for a future episode. Follow Business Unusual with Barbara Corcoran on iHeartRadio, or subscribe wherever you listen to podcasts. </strong>\u00a0<strong>This episode of Business Unusual with Barbara Corcoran is presented by OnDeck Business Loans (</strong><a href=\"https://urldefense.proofpoint.com/v2/url?u=http-3A__www.ondeck.com_Barbara&amp;d=DwMFaQ&amp;c=GC0NZZhaEw6GOQSjMHI2g15k_drElRoPmOYiK2k0eZ8&amp;r=xy9pRdG6lpZ6ogtRUMNvODnG4DdmLUxjZ2d9xbUZdbU5UshE20nENw68An-bhaS4&amp;m=b7G5z-S4fY6jYnVJoDD0IxLhdkIPrFOrNN2yLnt3Odc&amp;s=ecKEHfTJ9QtY2QfvkGL3kNIB-ZJ848-poG_hR6akhwQ&amp;e=\"><strong>http://www.ondeck.com/Barbara</strong></a><strong>)</strong></p>",
      "pub_date_ms": 1557201660062,
      "guid_from_rss": "b3ac56b2-2342-11e9-8178-17dec3a673e9",
      "listennotes_url": "https://www.listennotes.com/e/402e67e65e2a4575ab2704a977a2b4b5/",
      "audio_length_sec": 2188,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/402e67e65e2a4575ab2704a977a2b4b5/#edit"
    },
    {
      "id": "d6ff153d632f428195dfd54f002b0990",
      "link": "https://snacks.robinhood.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/d6ff153d632f428195dfd54f002b0990/",
      "image": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-F_0RTie7PzG-kmx0XIZTAys.1400x1400.jpg",
      "title": "Warren Buffett\u2019s epic annual event, Planet Fitness\u2019 innovative real estate strategy, and almond milk vs. Dean Foods dairy",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-F_0RTie7PzG-kmx0XIZTAys.1400x1400.jpg",
        "title": "Snacks Daily",
        "publisher": "Robinhood Financial, LLC",
        "thumbnail": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-Yp5jkwN1GKi-kmx0XIZTAys.300x300.jpg",
        "listen_score": 72,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-Yp5jkwN1GKi-kmx0XIZTAys.300x300.jpg",
      "description": "<p>The annual Berkshire Hathaway shareholder meeting showcased\u00a088-year-old legendary investor Warren Buffett, so we broke down his 6 hours of one-liner business takeaways. Planet Fitness shares are up 75% in the last year, so we\u2019re focused on its innovative real estate strategy that feeds off the retail-pocalypse. And Dean Foods is America\u2019s biggest dairy company, but the stock is down 62% in 2019 because of alt-milk.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1557136560575,
      "guid_from_rss": "de6a8f92-6f94-11e9-a2be-2bb85bb3ed24",
      "listennotes_url": "https://www.listennotes.com/e/d6ff153d632f428195dfd54f002b0990/",
      "audio_length_sec": 986,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/d6ff153d632f428195dfd54f002b0990/#edit"
    },
    {
      "id": "5ad170a60e76467e9d6b2453bd44fda6",
      "link": "https://www.listenmoneymatters.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/5ad170a60e76467e9d6b2453bd44fda6/",
      "image": "https://production.listennotes.com/podcasts/listen-money-matters-free-your-inner-lPXW7V_6n0C-SJEHNr84kVg.1400x1400.jpg",
      "title": "All Things Gold",
      "podcast": {
        "id": "3302bc71139541baa46ecb27dbf6071a",
        "image": "https://production.listennotes.com/podcasts/listen-money-matters-free-your-inner-lPXW7V_6n0C-SJEHNr84kVg.1400x1400.jpg",
        "title": "Listen Money Matters - Free your inner financial badass. All the stuff you should know about personal finance.",
        "publisher": "ListenMoneyMatters.com | Andrew Fiebert and Matt Giovanisci",
        "thumbnail": "https://production.listennotes.com/podcasts/listen-money-matters-free-your-inner-d5If074qkhz-SJEHNr84kVg.300x300.jpg",
        "listen_score": 66,
        "listennotes_url": "https://www.listennotes.com/c/3302bc71139541baa46ecb27dbf6071a/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/listen-money-matters-free-your-inner-d5If074qkhz-SJEHNr84kVg.300x300.jpg",
      "description": "<p>Some people who are hesitant to invest in the stock market are willing to invest in gold. Why? Gold is tangible, you can see it, hold it, and keep it right in your own house (or bunker). You can buy it from some guy in a late night infomercial. You can buy it with images of the fallen Twin Towers on it. Or an American eagle.<strong></p><p></strong></p><p><strong>You can\u2019t say any of that about investing in the stock market!</strong> When you own stock, you don\u2019t own a tangible thing. You have to deal with some slick stockbroker if you want to buy and sell it (you don\u2019t). And stocks don\u2019t come in a limited edition collector\u2019s box.</p><p>LMM hasn\u2019t discussed gold very much in the past and like a lot of you, thought it was something only Doomsday preppers were interested in so not really relevant to us or our audience. But while doing research for the <a href=\"https://www.listenmoneymatters.com/ray-dalio-all-weather-portfolio/\">Golden Butterfly episode,</a> we learned some legitimate reasons for investing in gold and <strong><em>none</em></strong> of them are related to the zombie apocalypse that is surely coming.</p><p>Many of our listeners wanted to know more about it too, why and how to invest in gold. We got a lot of emails asking questions. You asked and we answered. This is all things gold.<strong></p><p></strong><a href=\"https://www.listenmoneymatters.com/all-things-gold/\">Full Article Here</a><strong></p><p></strong></p><p><strong>Show Notes</p><p></strong></p><p><a href=\"http://SPS.NORTHWESTERN.EDU/CFP\">Northwestern University CFP Program</a> - Prepare for a career as a financial planner\u00a0</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://megaphone.fm/adchoices\">megaphone.fm/adchoices</a></p>",
      "pub_date_ms": 1557115200044,
      "guid_from_rss": "ca27ef12-d240-11e8-8c50-ab85da8ff643",
      "listennotes_url": "https://www.listennotes.com/e/5ad170a60e76467e9d6b2453bd44fda6/",
      "audio_length_sec": 2677,
      "explicit_content": true,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/5ad170a60e76467e9d6b2453bd44fda6/#edit"
    },
    {
      "id": "e2e15dc3f99745818872e71f7c828f89",
      "link": "https://snacks.robinhood.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/e2e15dc3f99745818872e71f7c828f89/",
      "image": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-F_0RTie7PzG-kmx0XIZTAys.1400x1400.jpg",
      "title": "The Taser CEO gets $246M in stock comp, Beyond Meat surges 163%, and Wayfair drops 7% because you\u2019re expensive",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-F_0RTie7PzG-kmx0XIZTAys.1400x1400.jpg",
        "title": "Snacks Daily",
        "publisher": "Robinhood Financial, LLC",
        "thumbnail": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-Yp5jkwN1GKi-kmx0XIZTAys.300x300.jpg",
        "listen_score": 72,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-Yp5jkwN1GKi-kmx0XIZTAys.300x300.jpg",
      "description": "<p>Axon Enterprises is the company behind the taser, and it just awarded its CEO $246M in compensation \u2014 So we look in to how it\u2019s set up to incentivize him. Beyond Meat surged 163% on its IPO day. And Wayfair is the biggest online furniture platform whose stock fell 7%, but it\u2019s got a fascinating relationship with 80 \u201chouse brands.\u201d</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1556877360576,
      "guid_from_rss": "fee4b324-6d3c-11e9-a4bf-c3f62ea29894",
      "listennotes_url": "https://www.listennotes.com/e/e2e15dc3f99745818872e71f7c828f89/",
      "audio_length_sec": 893,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/e2e15dc3f99745818872e71f7c828f89/#edit"
    },
    {
      "id": "2bc29c5d8ceb405c942bc13049784703",
      "link": "https://www.parcast.com/espionage?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/2bc29c5d8ceb405c942bc13049784703/",
      "image": "https://production.listennotes.com/podcasts/espionage-parcast-network-X9AT-uYo8Nq-ReK0QUN-VP_.1400x1400.jpg",
      "title": "Henri D\u00e9ricourt Pt. 2: Triple Agent",
      "podcast": {
        "id": "bacb2f7ca7a04ed0b21efd21192f5014",
        "image": "https://production.listennotes.com/podcasts/espionage-parcast-network-X9AT-uYo8Nq-ReK0QUN-VP_.1400x1400.jpg",
        "title": "Espionage",
        "publisher": "Parcast Network",
        "thumbnail": "https://production.listennotes.com/podcasts/espionage-parcast-network-j-WLEmNQ4PB-ReK0QUN-VP_.300x300.jpg",
        "listen_score": 64,
        "listennotes_url": "https://www.listennotes.com/c/bacb2f7ca7a04ed0b21efd21192f5014/",
        "listen_score_global_rank": "0.1%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/espionage-parcast-network-j-WLEmNQ4PB-ReK0QUN-VP_.300x300.jpg",
      "description": "Paris, 1943. World War II was in full swing, and triple-agent Henri D\u00e9ricourt was right in the middle of it. His mission: secure an Allied victory before his carefully-spun web of lies comes unraveled.<br><br>Parcasters - When it comes to transporting drugs, you can't do much better than a jetliner flying across international boundaries. Amado Carrillo Fuentes figured that out, earning his title as \"Lord of the Skies\" - learn his story on this week's episode of Kingpins at parcast.com/kingpins<br>",
      "pub_date_ms": 1556866860019,
      "guid_from_rss": "d8310352-3a17-11e9-acdb-535fa62c91fa",
      "listennotes_url": "https://www.listennotes.com/e/2bc29c5d8ceb405c942bc13049784703/",
      "audio_length_sec": 3218,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/2bc29c5d8ceb405c942bc13049784703/#edit"
    },
    {
      "id": "f0f2cc1d772c4ae4aef5bd1d1c8fb834",
      "link": "https://snacks.robinhood.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/f0f2cc1d772c4ae4aef5bd1d1c8fb834/",
      "image": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-F_0RTie7PzG-kmx0XIZTAys.1400x1400.jpg",
      "title": "Molson Coors falls 8% on mid-beer crisis, Royal Caribbean becomes pricing power superhero, and Fitbit is our \u201cSurvivor of the Day\u201d",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-F_0RTie7PzG-kmx0XIZTAys.1400x1400.jpg",
        "title": "Snacks Daily",
        "publisher": "Robinhood Financial, LLC",
        "thumbnail": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-Yp5jkwN1GKi-kmx0XIZTAys.300x300.jpg",
        "listen_score": 72,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-Yp5jkwN1GKi-kmx0XIZTAys.300x300.jpg",
      "description": "<p>With beer sales slowing, Molson Coors is desperately\u00a0focused on innovation (aka non-alcohol drinks), but shares fell because of its beer battles. Fitbit used to be profitable, now it\u2019s using partnerships to survive. And Royal Caribbean jumped 7% as it realizes it can charge a lot more for cruises.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1556790960577,
      "guid_from_rss": "ae282d24-6c71-11e9-a7ab-eff35f170a02",
      "listennotes_url": "https://www.listennotes.com/e/f0f2cc1d772c4ae4aef5bd1d1c8fb834/",
      "audio_length_sec": 1000,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/f0f2cc1d772c4ae4aef5bd1d1c8fb834/#edit"
    },
    {
      "id": "79811cc9a5704e32881699b0b93356ab",
      "link": "https://snacks.robinhood.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/79811cc9a5704e32881699b0b93356ab/",
      "image": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-F_0RTie7PzG-kmx0XIZTAys.1400x1400.jpg",
      "title": "Facebook\u2019s new \u201cFB5\u201d redesign (and dating feature), Apple\u2019s past-dependent business model, and Merck\u2019s profits quadruple",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-F_0RTie7PzG-kmx0XIZTAys.1400x1400.jpg",
        "title": "Snacks Daily",
        "publisher": "Robinhood Financial, LLC",
        "thumbnail": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-Yp5jkwN1GKi-kmx0XIZTAys.300x300.jpg",
        "listen_score": 72,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-Yp5jkwN1GKi-kmx0XIZTAys.300x300.jpg",
      "description": "<p>Apple\u2019s earnings report was critical for what it didn\u2019t say, just as much as what it did \u2014 And it reveals that Apple\u2019s transformation. Facebook\u2019s F8 event revealed new features (dating and crushes), but the big focus was its app redesign. And Merck\u2019s profits quadrupled because a measles vaccine and a new cancer drug have become its profit puppies.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1556704560578,
      "guid_from_rss": "ad35b722-6bb0-11e9-8988-bfa74a4a2234",
      "listennotes_url": "https://www.listennotes.com/e/79811cc9a5704e32881699b0b93356ab/",
      "audio_length_sec": 888,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/79811cc9a5704e32881699b0b93356ab/#edit"
    },
    {
      "id": "6f4b561b98c4489f94673bd709fa0c85",
      "link": "https://snacks.robinhood.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/6f4b561b98c4489f94673bd709fa0c85/",
      "image": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-F_0RTie7PzG-kmx0XIZTAys.1400x1400.jpg",
      "title": "Spotify hits 217M profitless users, Airbnb & Marriott\u2019s twin announcements, and Chewy.com\u2019s \u201cpet humanization\u201d IPO",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-F_0RTie7PzG-kmx0XIZTAys.1400x1400.jpg",
        "title": "Snacks Daily",
        "publisher": "Robinhood Financial, LLC",
        "thumbnail": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-Yp5jkwN1GKi-kmx0XIZTAys.300x300.jpg",
        "listen_score": 72,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-Yp5jkwN1GKi-kmx0XIZTAys.300x300.jpg",
      "description": "<p>Spotify now boasts 100M paying subscribers, so we looked\u00a0into why it\u2019s still losing so much money (hint: It\u2019s betting on podcasts). Airbnb and Marriott both revealed new services that look a lot like each other (awkward). And PetSmart\u2019s digital brand Chewy.com will IPO thanks to \u201cpet humanization\u201d trends.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1556618160579,
      "guid_from_rss": "6499bd3a-6aeb-11e9-a4ca-1b74330fa7a7",
      "listennotes_url": "https://www.listennotes.com/e/6f4b561b98c4489f94673bd709fa0c85/",
      "audio_length_sec": 1025,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/6f4b561b98c4489f94673bd709fa0c85/#edit"
    },
    {
      "id": "94bc56fb18cf4ef28a4e6cef6db1000d",
      "link": "https://cms.megaphone.fm/channel/business-unusual-with-barbara-corcoran?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/94bc56fb18cf4ef28a4e6cef6db1000d/",
      "image": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-MDXGCRbYJ2z-aZPn3Ic47rx.1400x1400.jpg",
      "title": "52: What I Learned From Bad Bosses",
      "podcast": {
        "id": "68faf62be97149c280ebcc25178aa731",
        "image": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-MDXGCRbYJ2z-aZPn3Ic47rx.1400x1400.jpg",
        "title": "Business Unusual with Barbara Corcoran",
        "publisher": "Barbara Corcoran",
        "thumbnail": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-Oqs7L9Yfpci-aZPn3Ic47rx.300x300.jpg",
        "listen_score": 57,
        "listennotes_url": "https://www.listennotes.com/c/68faf62be97149c280ebcc25178aa731/",
        "listen_score_global_rank": "0.5%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-Oqs7L9Yfpci-aZPn3Ic47rx.300x300.jpg",
      "description": "<p><strong>I had 23 bosses before starting my business and I know that a bad one is sure to kill your confidence. So what do you do when you don't see eye to eye? I answer your questions about dealing with a bad boss and becoming a better leader. </strong>\u00a0<strong>Want to hear your question on Business Unusual? Call me at 888-BARBARA or tweet at @barbaracorcoran to ask a question for a future episode. Follow Business Unusual with Barbara Corcoran on iHeartRadio, or subscribe wherever you listen to podcasts. </strong>\u00a0<strong>This episode of Business Unusual with Barbara Corcoran is presented by OnDeck Business Loans (</strong><a href=\"https://urldefense.proofpoint.com/v2/url?u=http-3A__www.ondeck.com_Barbara&amp;d=DwMFaQ&amp;c=GC0NZZhaEw6GOQSjMHI2g15k_drElRoPmOYiK2k0eZ8&amp;r=xy9pRdG6lpZ6ogtRUMNvODnG4DdmLUxjZ2d9xbUZdbU5UshE20nENw68An-bhaS4&amp;m=iyzCy3KkByFDhAZKPNnXfRZDwVi9wa4vgtkjqAegOYo&amp;s=AR-0E6fCOSktW28rNgQpCe-kEyu1odFgovlqPFyavSA&amp;e=\"><strong>http://www.ondeck.com/Barbara</strong></a><strong>)</strong>\u00a0</p>",
      "pub_date_ms": 1556596860063,
      "guid_from_rss": "b3a725ac-2342-11e9-8178-7fb1e262e428",
      "listennotes_url": "https://www.listennotes.com/e/94bc56fb18cf4ef28a4e6cef6db1000d/",
      "audio_length_sec": 972,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/94bc56fb18cf4ef28a4e6cef6db1000d/#edit"
    },
    {
      "id": "8823f69978ac40899d4e7264206db89f",
      "link": "https://philosophizethis.libsyn.com/episode-130-dewey-and-lippman-on-democracy?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/8823f69978ac40899d4e7264206db89f/",
      "image": "https://production.listennotes.com/podcasts/philosophize-this-stephen-west-Y2PvRelyrIN-ivQCfmkqM_h.1400x1400.jpg",
      "title": "Episode #130 ... Dewey and Lippman on Democracy",
      "podcast": {
        "id": "3a2a6ddd549f4df0b876e7315fa1a319",
        "image": "https://production.listennotes.com/podcasts/philosophize-this-stephen-west-Y2PvRelyrIN-ivQCfmkqM_h.1400x1400.jpg",
        "title": "Philosophize This!",
        "publisher": "Stephen West",
        "thumbnail": "https://production.listennotes.com/podcasts/philosophize-this-stephen-west-oSuiCW7Bz8T-ivQCfmkqM_h.300x300.jpg",
        "listen_score": 79,
        "listennotes_url": "https://www.listennotes.com/c/3a2a6ddd549f4df0b876e7315fa1a319/",
        "listen_score_global_rank": "0.01%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/philosophize-this-stephen-west-oSuiCW7Bz8T-ivQCfmkqM_h.300x300.jpg",
      "description": "<p>Today we talk about a famous debate from the early 20th century.\u00a0</p>",
      "pub_date_ms": 1556594432026,
      "guid_from_rss": "09cea1e8a32c49b383f85fff0f172a2e",
      "listennotes_url": "https://www.listennotes.com/e/8823f69978ac40899d4e7264206db89f/",
      "audio_length_sec": 1298,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/8823f69978ac40899d4e7264206db89f/#edit"
    },
    {
      "id": "d8ad1f1994654319a041e23d76d6b599",
      "link": "https://snacks.robinhood.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/d8ad1f1994654319a041e23d76d6b599/",
      "image": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-F_0RTie7PzG-kmx0XIZTAys.1400x1400.jpg",
      "title": "Beyond Meat boots its meat-focused investor, Comcast (shockingly) hits record high, and one startup\u2019s worst 1st week",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-F_0RTie7PzG-kmx0XIZTAys.1400x1400.jpg",
        "title": "Snacks Daily",
        "publisher": "Robinhood Financial, LLC",
        "thumbnail": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-Yp5jkwN1GKi-kmx0XIZTAys.300x300.jpg",
        "listen_score": 72,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-Yp5jkwN1GKi-kmx0XIZTAys.300x300.jpg",
      "description": "<p>Plant-based meat innovator Beyond Meat had an awkward investor: The world\u2019s 2nd biggest meat producer, Tyson Foods -- So Beyond Meat kicked it out before its upcoming IPO. Old school cable throwback Comcast is winning even though you cut the cord. And Luminary was supposed to be the future of podcasting, but its 1st week went really badly.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1556531760580,
      "guid_from_rss": "76ae24a6-6a24-11e9-a711-dbdc65a73778",
      "listennotes_url": "https://www.listennotes.com/e/d8ad1f1994654319a041e23d76d6b599/",
      "audio_length_sec": 803,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/d8ad1f1994654319a041e23d76d6b599/#edit"
    },
    {
      "id": "117e3b5027f14fb9842591aaa4b794eb",
      "link": "https://www.npr.org/2019/04/25/717075560/special-announcement-from-life-kit?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/117e3b5027f14fb9842591aaa4b794eb/",
      "image": "https://production.listennotes.com/podcasts/find-money-you-didnt-know-you-had-npr-WuHnh0Poiyb-IDT1XPkq4rb.1400x1400.jpg",
      "title": "Special Announcement From Life Kit",
      "podcast": {
        "id": "613aa80ec729409ea0db4265cf3e3899",
        "image": "https://production.listennotes.com/podcasts/find-money-you-didnt-know-you-had-npr-WuHnh0Poiyb-IDT1XPkq4rb.1400x1400.jpg",
        "title": "Find Money You Didn't Know You Had",
        "publisher": "NPR",
        "thumbnail": "https://production.listennotes.com/podcasts/find-money-you-didnt-know-you-had-npr-Dl7VZ86KyNA-IDT1XPkq4rb.300x300.jpg",
        "listen_score": null,
        "listennotes_url": "https://www.listennotes.com/c/613aa80ec729409ea0db4265cf3e3899/",
        "listen_score_global_rank": null
      },
      "thumbnail": "https://production.listennotes.com/podcasts/find-money-you-didnt-know-you-had-npr-Dl7VZ86KyNA-IDT1XPkq4rb.300x300.jpg",
      "description": "Based on your feedback, we've created new ways to listen to Life Kit. If you never want to miss an episode, subscribe to Life Kit: All Guides. We also divided our guides by subject \u2014 health, money and parenting - and more to come in the future \u2014 so you can subscribe to only the topics you want to learn about.",
      "pub_date_ms": 1556519451000,
      "guid_from_rss": "f0925b4c-fc2f-494d-acf1-0c2fb96627ff",
      "listennotes_url": "https://www.listennotes.com/e/117e3b5027f14fb9842591aaa4b794eb/",
      "audio_length_sec": 53,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/117e3b5027f14fb9842591aaa4b794eb/#edit"
    },
    {
      "id": "99ae9284a95948208170457bd4a0a141",
      "link": "https://www.listenmoneymatters.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/99ae9284a95948208170457bd4a0a141/",
      "image": "https://production.listennotes.com/podcasts/listen-money-matters-free-your-inner-lPXW7V_6n0C-SJEHNr84kVg.1400x1400.jpg",
      "title": "How Wills and Trusts Work, and Where to Start",
      "podcast": {
        "id": "3302bc71139541baa46ecb27dbf6071a",
        "image": "https://production.listennotes.com/podcasts/listen-money-matters-free-your-inner-lPXW7V_6n0C-SJEHNr84kVg.1400x1400.jpg",
        "title": "Listen Money Matters - Free your inner financial badass. All the stuff you should know about personal finance.",
        "publisher": "ListenMoneyMatters.com | Andrew Fiebert and Matt Giovanisci",
        "thumbnail": "https://production.listennotes.com/podcasts/listen-money-matters-free-your-inner-d5If074qkhz-SJEHNr84kVg.300x300.jpg",
        "listen_score": 66,
        "listennotes_url": "https://www.listennotes.com/c/3302bc71139541baa46ecb27dbf6071a/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/listen-money-matters-free-your-inner-d5If074qkhz-SJEHNr84kVg.300x300.jpg",
      "description": "<p>We know that none of you likes to think about death, but it\u2019s inevitable, and you have no idea when. </p><p>For the majority of us, the most important thing in our life is the well being of our family. We work hard for them; we take care of them. But how can you do that when you\u2019re no longer here? <strong>By establishing a trust fund and a will. </p><p></strong></p><p>Don\u2019t wait; there\u2019s no reason to. You can finish reading this, spend a few minutes and a few hundred dollars and make sure your family is taken care of. Because what else is there?</p><p><a href=\"https://www.listenmoneymatters.com/what-is-a-trust-fund/%20\">Full Article Here</a></p><p><strong></p><p>Show Notes</p><p></strong></p><p><a href=\"https://www.beeradvocate.com/beer/profile/30452/91759/\"><strong>18 Watt Session IPA:</strong></a> An IPA from SingleCut. </p><p><a href=\"https://www.beeradvocate.com/beer/profile/1450/6356/\"><strong>Fruh Kolsch:</strong></a> A German-style beer</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://megaphone.fm/adchoices\">megaphone.fm/adchoices</a></p>",
      "pub_date_ms": 1556510400045,
      "guid_from_rss": "ca235006-d240-11e8-8c50-03fa7e64a82c",
      "listennotes_url": "https://www.listennotes.com/e/99ae9284a95948208170457bd4a0a141/",
      "audio_length_sec": 3078,
      "explicit_content": true,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/99ae9284a95948208170457bd4a0a141/#edit"
    }
  ],
  "next_episode_pub_date": 1556510400045
}
```   
</details>



<details>
  <summary>Click to see response schema</summary>
  
```json
{
  "type": "object",
  "required": [
    "podcasts"
  ],
  "properties": {
    "podcasts": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "example": "4d3fe717742d4963a85562e9f84d8c79",
            "description": "Podcast id."
          },
          "rss": {
            "type": "string",
            "example": "https://sw7x7.libsyn.com/rss",
            "description": "RSS url of this podcast. This field is available only in the PRO/ENTERPRISE plan."
          },
          "type": {
            "enum": [
              "episodic",
              "serial"
            ],
            "type": "string",
            "example": "episodic",
            "description": "The type of this podcast - episodic or serial."
          },
          "email": {
            "type": "string",
            "example": "hello@example.com",
            "description": "The email of this podcast's producer. This field is available only in the PRO/ENTERPRISE plan."
          },
          "extra": {
            "type": "object",
            "properties": {
              "url1": {
                "type": "string",
                "description": "Url affiliated with this podcast"
              },
              "url2": {
                "type": "string",
                "description": "Url affiliated with this podcast"
              },
              "url3": {
                "type": "string",
                "description": "Url affiliated with this podcast"
              },
              "google_url": {
                "type": "string",
                "example": "https://play.google.com/music/listen?u=0#/ps/I7gdcrqcmvhfnhh2cyqkcg32tkq",
                "description": "Google Podcasts url for this podcast"
              },
              "spotify_url": {
                "type": "string",
                "example": "https://open.spotify.com/show/2rQJUP9Y3HxemiW3JHt9WV",
                "description": "Spotify url for this podcast"
              },
              "youtube_url": {
                "type": "string",
                "example": "https://www.youtube.com/sw7x7",
                "description": "YouTube url affiliated with this podcast"
              },
              "linkedin_url": {
                "type": "string",
                "description": "LinkedIn url affiliated with this podcast"
              },
              "wechat_handle": {
                "type": "string",
                "description": "WeChat username affiliated with this podcast"
              },
              "patreon_handle": {
                "type": "string",
                "example": "sw7x7",
                "description": "Patreon username affiliated with this podcast"
              },
              "twitter_handle": {
                "type": "string",
                "example": "SW7x7podcast",
                "description": "Twitter username affiliated with this podcast"
              },
              "facebook_handle": {
                "type": "string",
                "example": "sw7x7",
                "description": "Facebook username affiliated with this podcast"
              },
              "instagram_handle": {
                "type": "string",
                "example": "sw7x7",
                "description": "Instagram username affiliated with this podcast"
              }
            }
          },
          "image": {
            "type": "string",
            "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
            "description": "Image url for this podcast's artwork. If you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
          },
          "title": {
            "type": "string",
            "example": "Star Wars 7x7 | Star Wars News, Interviews, and More!",
            "description": "Podcast name."
          },
          "country": {
            "type": "string",
            "example": "United States",
            "description": "The country where this podcast is produced."
          },
          "website": {
            "type": "string",
            "example": "http://sw7x7.com/",
            "description": "Website url of this podcast."
          },
          "language": {
            "type": "string",
            "example": "English",
            "description": "The language of this podcast. You can get all supported languages from `GET /languages`."
          },
          "genre_ids": {
            "type": "array",
            "items": {
              "type": "integer",
              "description": "Genre ids."
            },
            "example": [
              138,
              86,
              160,
              68,
              82,
              100,
              101
            ]
          },
          "itunes_id": {
            "type": "integer",
            "example": 896354638,
            "description": "iTunes id for this podcast."
          },
          "publisher": {
            "type": "string",
            "example": "Planet Broadcasting",
            "description": "Podcast publisher name."
          },
          "thumbnail": {
            "type": "string",
            "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
            "description": "Thumbnail image url for this podcast's artwork (300x300)."
          },
          "is_claimed": {
            "type": "boolean",
            "example": true,
            "description": "Whether this podcast is claimed by its producer on [ListenNotes.com](https://www.ListenNotes.com)."
          },
          "description": {
            "type": "string",
            "example": "<p>The Star Wars 7x7 Podcast is Rebel-rousing fun for everyday Jedi, between 7 and 14 minutes a day, 7 days a week. Join host Allen Voivod for Star Wars news, history, interviews, trivia, and deep dives into the Star Wars story as told in movies, books, comics, games, cartoons, and more. Subscribe now for your daily dose of Star Wars joy. It's destiny unleashed!</p>",
            "description": "Html of this episode's full description"
          },
          "looking_for": {
            "type": "object",
            "properties": {
              "guests": {
                "type": "boolean",
                "example": true,
                "description": "Whether this podcast is looking for guests."
              },
              "cohosts": {
                "type": "boolean",
                "example": true,
                "description": "Whether this podcast is looking for cohosts."
              },
              "sponsors": {
                "type": "boolean",
                "example": true,
                "description": "Whether this podcast is looking for sponsors."
              },
              "cross_promotion": {
                "type": "boolean",
                "example": true,
                "description": "Whether this podcast is looking for cross promotion opportunities with other podcasts."
              }
            }
          },
          "listen_score": {
            "type": "integer",
            "example": 81,
            "description": "The estimated popularity score of a podcast compared to all other rss-based public podcasts in the world on a scale from 0 to 100.\nIf the score is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
          },
          "total_episodes": {
            "type": "integer",
            "example": 324,
            "description": "Total number of episodes in this podcast."
          },
          "listennotes_url": {
            "type": "string",
            "example": "https://www.listennotes.com/c/4d3fe717742d4963a85562e9f84d8c79/",
            "description": "The url of this podcast on [ListenNotes.com](https://www.ListenNotes.com)."
          },
          "explicit_content": {
            "type": "boolean",
            "example": false,
            "description": "Whether this podcast contains explicit language."
          },
          "latest_pub_date_ms": {
            "type": "integer",
            "example": 1557499770000,
            "description": "The published date of the latest episode of this podcast. In milliseconds"
          },
          "earliest_pub_date_ms": {
            "type": "integer",
            "example": 1470667902000,
            "description": "The published date of the oldest episode of this podcast. In milliseconds"
          },
          "listen_score_global_rank": {
            "type": "string",
            "example": "0.5%",
            "description": "The estimated popularity ranking of a podcast compared to all other rss-based public podcasts in the world.\nFor example, if the value is 0.5%, then this podcast is one of the top 0.5% most popular shows out of all podcasts globally, ranked by Listen Score.\nIf the ranking is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
          }
        }
      }
    },
    "latest_episodes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "example": "4d82e50314174754a3b603912448e812",
            "description": "Episode id."
          },
          "link": {
            "type": "string",
            "example": "https://www.npr.org/2020/01/22/798532179/soleimanis-iran",
            "description": "Web link of this episode."
          },
          "audio": {
            "type": "string",
            "example": "https://www.listennotes.com/e/p/11b34041e804491b9704d11f283c74de/",
            "description": "Audio url of this episode, which can be played directly."
          },
          "image": {
            "type": "string",
            "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
            "description": "Image url for this episode.\nIf an episode doesn't have its own image, then this field would be the url of the podcast artwork image.\nIf you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
          },
          "title": {
            "type": "string",
            "example": "Celebration Recap, Jason Fry and Christian Blauvelt Interviews \u2013 SWBW #101",
            "description": "Episode name."
          },
          "podcast": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "example": "4d3fe717742d4963a85562e9f84d8c79",
                "description": "Podcast id."
              },
              "image": {
                "type": "string",
                "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
                "description": "Image url for this podcast's artwork. If you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
              },
              "title": {
                "type": "string",
                "example": "Star Wars 7x7 | Star Wars News, Interviews, and More!",
                "description": "Podcast name."
              },
              "publisher": {
                "type": "string",
                "example": "Planet Broadcasting",
                "description": "Podcast publisher name."
              },
              "thumbnail": {
                "type": "string",
                "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
                "description": "Thumbnail image url for this podcast's artwork (300x300)."
              },
              "listen_score": {
                "type": "integer",
                "example": 81,
                "description": "The estimated popularity score of a podcast compared to all other rss-based public podcasts in the world on a scale from 0 to 100.\nIf the score is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
              },
              "listennotes_url": {
                "type": "string",
                "example": "https://www.listennotes.com/c/4d3fe717742d4963a85562e9f84d8c79/",
                "description": "The url of this podcast on [ListenNotes.com](https://www.ListenNotes.com)."
              },
              "listen_score_global_rank": {
                "type": "string",
                "example": "0.5%",
                "description": "The estimated popularity ranking of a podcast compared to all other rss-based public podcasts in the world.\nFor example, if the value is 0.5%, then this podcast is one of the top 0.5% most popular shows out of all podcasts globally, ranked by Listen Score.\nIf the ranking is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
              }
            }
          },
          "thumbnail": {
            "type": "string",
            "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
            "description": "Thumbnail image (300x300) url for this episode.\nIf an episode doesn't have its own image, then this field would be the url of the podcast artwork thumbnail image.\n"
          },
          "description": {
            "type": "string",
            "example": "<p>Disney chief Bob Iger shared news about Star Wars movies in 2020 and beyond, but some media outlets gave conflicting reports about it. Here's the real scoop. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>\n",
            "description": "Html of this episode's full description"
          },
          "pub_date_ms": {
            "type": "integer",
            "example": 1474873200000,
            "description": "Published date for this episode. In millisecond."
          },
          "listennotes_url": {
            "type": "string",
            "example": "https://www.listennotes.com/e/4d82e50314174754a3b603912448e812/",
            "description": "The url of this episode on [ListenNotes.com](https://www.ListenNotes.com)."
          },
          "audio_length_sec": {
            "type": "integer",
            "example": 567,
            "description": "Audio length of this episode. In seconds."
          },
          "explicit_content": {
            "type": "boolean",
            "example": false,
            "description": "Whether this podcast contains explicit language."
          },
          "maybe_audio_invalid": {
            "type": "boolean",
            "example": false,
            "description": "Whether or not this episode's audio is invalid. Podcasters may delete the original audio."
          },
          "listennotes_edit_url": {
            "type": "string",
            "example": "https://www.listennotes.com/e/11b34041e804491b9704d11f283c74de/#edit",
            "description": "Edit url of this episode where you can update the audio url if you find the audio is broken."
          }
        }
      },
      "description": "Up to 10 latest episodes from these podcasts, sorted by **pub_date**. This field shows up only when **show_latest_episodes** is 1.\n"
    }
  }
}
```   
</details>




### Fetch a random podcast episode

Function Name: **just_listen**

Recently published episodes are more likely to be fetched. Good luck!

Example:
```python

from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)      

response = client.just_listen()
            
print(response.json())

```

See all available parameters on the [API Docs page](https://www.listennotes.com/api/docs/#get-api-v2-just_listen).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "id": "e6d32d2049a24edaaeaf0adb6a98ffb9",
  "link": "http://www.sermonaudio.com/sermoninfo.asp?SID=10252117542523&utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
  "audio": "https://www.listennotes.com/e/p/e6d32d2049a24edaaeaf0adb6a98ffb9/",
  "image": "https://production.listennotes.com/podcasts/sermonaudio-mp3-infosermonaudiocom-QbhBH7VtCOF-v31NbnyI_Dm.1400x1400.jpg",
  "title": "Who do you say Jesus is?",
  "podcast": {
    "id": "a9d8880842f3464eb6621f8d850b7eb6",
    "image": "https://production.listennotes.com/podcasts/sermonaudio-mp3-infosermonaudiocom-QbhBH7VtCOF-v31NbnyI_Dm.1400x1400.jpg",
    "title": "SermonAudio: MP3",
    "publisher": "info@sermonaudio.com",
    "thumbnail": "https://production.listennotes.com/podcasts/sermonaudio-mp3-infosermonaudiocom-kqnxPW6mgVb-v31NbnyI_Dm.300x300.jpg",
    "listen_score": null,
    "listennotes_url": "https://www.listennotes.com/c/a9d8880842f3464eb6621f8d850b7eb6/",
    "listen_score_global_rank": null
  },
  "thumbnail": "https://production.listennotes.com/podcasts/sermonaudio-mp3-infosermonaudiocom-kqnxPW6mgVb-v31NbnyI_Dm.300x300.jpg",
  "description": "Craig Gillenwater",
  "pub_date_ms": 1635222720000,
  "guid_from_rss": "http://www.sermonaudio.com/sermoninfo.asp?SID=10252117542523",
  "listennotes_url": "https://www.listennotes.com/e/e6d32d2049a24edaaeaf0adb6a98ffb9/",
  "audio_length_sec": 2520,
  "explicit_content": false,
  "maybe_audio_invalid": false,
  "listennotes_edit_url": "https://www.listennotes.com/e/e6d32d2049a24edaaeaf0adb6a98ffb9/#edit"
}
```   
</details>



<details>
  <summary>Click to see response schema</summary>
  
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "example": "4d82e50314174754a3b603912448e812",
      "description": "Episode id."
    },
    "link": {
      "type": "string",
      "example": "https://www.npr.org/2020/01/22/798532179/soleimanis-iran",
      "description": "Web link of this episode."
    },
    "audio": {
      "type": "string",
      "example": "https://www.listennotes.com/e/p/11b34041e804491b9704d11f283c74de/",
      "description": "Audio url of this episode, which can be played directly."
    },
    "image": {
      "type": "string",
      "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
      "description": "Image url for this episode.\nIf an episode doesn't have its own image, then this field would be the url of the podcast artwork image.\nIf you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
    },
    "title": {
      "type": "string",
      "example": "Celebration Recap, Jason Fry and Christian Blauvelt Interviews \u2013 SWBW #101",
      "description": "Episode name."
    },
    "podcast": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "example": "4d3fe717742d4963a85562e9f84d8c79",
          "description": "Podcast id."
        },
        "image": {
          "type": "string",
          "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
          "description": "Image url for this podcast's artwork. If you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
        },
        "title": {
          "type": "string",
          "example": "Star Wars 7x7 | Star Wars News, Interviews, and More!",
          "description": "Podcast name."
        },
        "publisher": {
          "type": "string",
          "example": "Planet Broadcasting",
          "description": "Podcast publisher name."
        },
        "thumbnail": {
          "type": "string",
          "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
          "description": "Thumbnail image url for this podcast's artwork (300x300)."
        },
        "listen_score": {
          "type": "integer",
          "example": 81,
          "description": "The estimated popularity score of a podcast compared to all other rss-based public podcasts in the world on a scale from 0 to 100.\nIf the score is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
        },
        "listennotes_url": {
          "type": "string",
          "example": "https://www.listennotes.com/c/4d3fe717742d4963a85562e9f84d8c79/",
          "description": "The url of this podcast on [ListenNotes.com](https://www.ListenNotes.com)."
        },
        "listen_score_global_rank": {
          "type": "string",
          "example": "0.5%",
          "description": "The estimated popularity ranking of a podcast compared to all other rss-based public podcasts in the world.\nFor example, if the value is 0.5%, then this podcast is one of the top 0.5% most popular shows out of all podcasts globally, ranked by Listen Score.\nIf the ranking is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
        }
      }
    },
    "thumbnail": {
      "type": "string",
      "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
      "description": "Thumbnail image (300x300) url for this episode.\nIf an episode doesn't have its own image, then this field would be the url of the podcast artwork thumbnail image.\n"
    },
    "description": {
      "type": "string",
      "example": "<p>Disney chief Bob Iger shared news about Star Wars movies in 2020 and beyond, but some media outlets gave conflicting reports about it. Here's the real scoop. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>\n",
      "description": "Html of this episode's full description"
    },
    "pub_date_ms": {
      "type": "integer",
      "example": 1474873200000,
      "description": "Published date for this episode. In millisecond."
    },
    "listennotes_url": {
      "type": "string",
      "example": "https://www.listennotes.com/e/4d82e50314174754a3b603912448e812/",
      "description": "The url of this episode on [ListenNotes.com](https://www.ListenNotes.com)."
    },
    "audio_length_sec": {
      "type": "integer",
      "example": 567,
      "description": "Audio length of this episode. In seconds."
    },
    "explicit_content": {
      "type": "boolean",
      "example": false,
      "description": "Whether this podcast contains explicit language."
    },
    "maybe_audio_invalid": {
      "type": "boolean",
      "example": false,
      "description": "Whether or not this episode's audio is invalid. Podcasters may delete the original audio."
    },
    "listennotes_edit_url": {
      "type": "string",
      "example": "https://www.listennotes.com/e/11b34041e804491b9704d11f283c74de/#edit",
      "description": "Edit url of this episode where you can update the audio url if you find the audio is broken."
    }
  }
}
```   
</details>




### Fetch a curated list of podcasts by id

Function Name: **fetch_curated_podcasts_list_by_id**

Get detailed meta data of all podcasts in a specific curated list.
This endpoint returns same data as https://www.listennotes.com/curated-podcasts/


Example:
```python

from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)      

response = client.fetch_curated_podcasts_list_by_id(id='SDFKduyJ47r')
            
print(response.json())

```

See all available parameters on the [API Docs page](https://www.listennotes.com/api/docs/#get-api-v2-curated_podcasts-id).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "id": "SDFKduyJ47r",
  "title": "16 Brilliant Indian Podcasts That'll Make You A Funner, Smarter, Better Informed Person",
  "total": 16,
  "podcasts": [
    {
      "id": "c463d5980b8e480fb78db6b3ed6be115",
      "rss": "https://maedinindia.libsyn.com/maedinindia",
      "type": "episodic",
      "email": "maedinindia@gmail.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9tYWVkaW5pbmRpYS5saWJzeW4uY29tL21hZWRpbmluZGlh",
        "spotify_url": "https://open.spotify.com/show/0QhzjA2zKdKgIQsd2ltHtp?si=1G6nu1YnRKiM9XPgjs3fyw",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "maedinindia",
        "facebook_handle": "maedinindia",
        "instagram_handle": "maedinindia"
      },
      "image": "https://production.listennotes.com/podcasts/maed-in-india-maed-in-india-7fgzAQsCRmy-y2oQTwMN73p.1400x1400.jpg",
      "title": "Maed in India",
      "country": "India",
      "website": "https://www.maedinindia.in/maed-in-india?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        100,
        101,
        134
      ],
      "itunes_id": 1009197596,
      "publisher": "Maed in India",
      "thumbnail": "https://production.listennotes.com/podcasts/maed-in-india-maed-in-india-p9P2YIfeQl3-y2oQTwMN73p.300x300.jpg",
      "is_claimed": true,
      "description": "Maed in India - India's first indie music podcast that showcases the best Indian independent musicians from India and abroad. Each episode presents an interview with an artist/band along with an exclusive stripped down session or acoustic renditions of their original music. The weekly show prides itself on being the destination for new music, little known stories, and unreleased music never heard before.\n\nIt features all kinds of artists from new-comers to veterans and under a variety of genres from hip hop, blues, soul, to folk, punk, rock, and everything in between.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 44,
      "total_episodes": 269,
      "listennotes_url": "https://www.listennotes.com/c/c463d5980b8e480fb78db6b3ed6be115/",
      "explicit_content": false,
      "latest_pub_date_ms": 1632695400000,
      "earliest_pub_date_ms": 1434346200260,
      "listen_score_global_rank": "1%"
    },
    {
      "id": "f8752dd03e3a4f8d838fc07cab953c0b",
      "rss": "http://feeds.feedburner.com/theintersectionIN",
      "type": "episodic",
      "email": "theintersection@audiomatic.in",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/web/image/b3ec0cfa324e40c5b6fea08c16023669.jpg",
      "title": "The Intersection",
      "country": "United States",
      "website": "http://soundcloud.com/user-495845543?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        122,
        125
      ],
      "itunes_id": 981456156,
      "publisher": "The Intersection",
      "thumbnail": "https://production.listennotes.com/channel/image/b956ac6715da4f5bb57a3f770824a061.jpg",
      "is_claimed": false,
      "description": "Podcast by The Intersection",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": null,
      "total_episodes": 59,
      "listennotes_url": "https://www.listennotes.com/c/f8752dd03e3a4f8d838fc07cab953c0b/",
      "explicit_content": false,
      "latest_pub_date_ms": 1545121747000,
      "earliest_pub_date_ms": 1427975825000,
      "listen_score_global_rank": null
    },
    {
      "id": "10a1ff15904548978355ff69166b2578",
      "rss": "https://www.arre.co.in/apple-podcast-rss/",
      "type": "serial",
      "email": "trialbyerror@arre.co.in",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly93d3cuYXJyZS5jby5pbi9hcHBsZS1wb2RjYXN0LXJzcy8=",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/trial-by-error-the-aarushi-files-arre-HW5-PMrpJ6g--hleb0zIEPC.1400x1400.jpg",
      "title": "Trial by Error | The Aarushi Files",
      "country": "United States",
      "website": "https://www.arre.co.in/series/aarushi?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        122,
        67
      ],
      "itunes_id": 1437504601,
      "publisher": "Arre",
      "thumbnail": "https://production.listennotes.com/podcasts/trial-by-error-the-aarushi-files-arre-PdHUYLlQq1T--hleb0zIEPC.300x300.jpg",
      "is_claimed": false,
      "description": "Trial by Error, An Arr\u00e9-Saavn Original, produced by Jamun, is adapted from Avirook Sen\u2019s haunting book Aarushi, is an eight-part investigative audio series that narrates the story of the Noida double murder, and the controversial trial that convicted the Talwars. Follow investigative journalist Nishita Jha as she turns a lens on the murky details of the case to see whether justice truly has been served. \n\n",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 42,
      "total_episodes": 16,
      "listennotes_url": "https://www.listennotes.com/c/10a1ff15904548978355ff69166b2578/",
      "explicit_content": false,
      "latest_pub_date_ms": 1468183671000,
      "earliest_pub_date_ms": 1462135535000,
      "listen_score_global_rank": "1.5%"
    },
    {
      "id": "00c5d061be3d42bb954b7a05dc044166",
      "rss": "https://feeds.soundcloud.com/users/soundcloud:users:152973991/sounds.rss",
      "type": "episodic",
      "email": null,
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5zb3VuZGNsb3VkLmNvbS91c2Vycy9zb3VuZGNsb3VkOnVzZXJzOjE1Mjk3Mzk5MS9zb3VuZHMucnNz",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "cheapadventures",
        "facebook_handle": "theadventuresofcheapbeer",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/adventures-of-cheap-beer-adventures-of-_JAB4btwguP-vkZfSh-TJCt.1400x1400.jpg",
      "title": "Adventures of Cheap Beer",
      "country": "India",
      "website": "http://www.adventuresofcheapbeer.in?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        100,
        102,
        122,
        133
      ],
      "itunes_id": 1035169168,
      "publisher": "Adventures of Cheap Beer",
      "thumbnail": "https://production.listennotes.com/podcasts/adventures-of-cheap-beer-adventures-of-tszxiBTflqc-vkZfSh-TJCt.300x300.jpg",
      "is_claimed": false,
      "description": "Welcome to a podcast where Siddhant Mehta, Karan Agarwal and Suyash Barve head out into the city of Mumbai and review some awesome cheap bars | Hosts: Siddhant Mehta, Karan Agarwal and Suyash Barve | Opening Theme: Fog + Strobe by Blek | Music: Aman Agarwal | Produced by Hit, Kitanu & Sandwich",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": null,
      "total_episodes": 5,
      "listennotes_url": "https://www.listennotes.com/c/00c5d061be3d42bb954b7a05dc044166/",
      "explicit_content": true,
      "latest_pub_date_ms": 1515393130000,
      "earliest_pub_date_ms": 1504590119004,
      "listen_score_global_rank": null
    },
    {
      "id": "ff180c271be249e9b94a8bc3d80bb094",
      "rss": "https://static.adorilabs.com/feed/watcha.xml",
      "type": "episodic",
      "email": "shows@indusvox.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9zdGF0aWMuYWRvcmlsYWJzLmNvbS9mZWVkL3dhdGNoYS54bWw=",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/watcha-ivm-podcasts-Qv2WOYNyz5V-HEvn-LS7uyo.1400x1400.jpg",
      "title": "Watcha!",
      "country": "United States",
      "website": "http://ivmpodcasts.com/watcha?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        68,
        100,
        101,
        103
      ],
      "itunes_id": 1076223958,
      "publisher": "IVM Podcasts",
      "thumbnail": "https://production.listennotes.com/podcasts/watcha-ivm-podcasts-wSHZVq-i_TJ-HEvn-LS7uyo.300x300.jpg",
      "is_claimed": true,
      "description": "Film critic and writer Aniruddha Guha talks about the films and TV shows currently on his playlist, and recommends the best of them. Feature films, documentaries, television shows, web series, YouTube videos; come, Watcha! with @AniGuha.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": null,
      "total_episodes": 10,
      "listennotes_url": "https://www.listennotes.com/c/ff180c271be249e9b94a8bc3d80bb094/",
      "explicit_content": false,
      "latest_pub_date_ms": 1459143000000,
      "earliest_pub_date_ms": 1453095676009,
      "listen_score_global_rank": null
    },
    {
      "id": "c40188a1a51249a3bafb11793a011359",
      "rss": "https://feeds.soundcloud.com/users/soundcloud:users:90732272/sounds.rss",
      "type": "episodic",
      "email": "synthesistalk@gmail.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5zb3VuZGNsb3VkLmNvbS91c2Vycy9zb3VuZGNsb3VkOnVzZXJzOjkwNzMyMjcyL3NvdW5kcy5yc3M=",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/syntalk-syntalk-O_8qKgy0eWd-j2nFBUVDzq_.1006x1006.jpg",
      "title": "SynTalk",
      "country": "United States",
      "website": "https://appsto.re/in/sb7rlb.i?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        122,
        126
      ],
      "itunes_id": 898573870,
      "publisher": "SynTalk",
      "thumbnail": "https://production.listennotes.com/podcasts/syntalk-syntalk-AscbMPzh92d-j2nFBUVDzq_.300x300.jpg",
      "is_claimed": false,
      "description": "f(q) = Is everything moving? (#TSAM)\n\nSynTalk is a freewheeling interdisciplinary talk show with a philosophical approach to understanding the world from a long term perspective.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 33,
      "total_episodes": 172,
      "listennotes_url": "https://www.listennotes.com/c/c40188a1a51249a3bafb11793a011359/",
      "explicit_content": false,
      "latest_pub_date_ms": 1626048000000,
      "earliest_pub_date_ms": 1405191856171,
      "listen_score_global_rank": "5%"
    },
    {
      "id": "24ece1d0922d4d9a9659e9e6cb2b241e",
      "rss": "https://feeds.simplecast.com/6dj1W8C2",
      "type": "episodic",
      "email": "hello@neilpatel.co",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5zaW1wbGVjYXN0LmNvbS82ZGoxVzhDMg==",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "Indianstartupsh",
        "facebook_handle": "indianstartupshow",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-indian-startup-show-neil-patel-QWdjyCBTwPr-9574y1CKU8j.1400x1400.jpg",
      "title": "The Indian Startup Show",
      "country": "United States",
      "website": "http://www.indianstartupshow.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        93,
        95,
        127,
        129,
        131
      ],
      "itunes_id": 1031590716,
      "publisher": "Neil Patel",
      "thumbnail": "https://production.listennotes.com/podcasts/the-indian-startup-show-neil-patel-etrHT24KoXq-9574y1CKU8j.300x300.jpg",
      "is_claimed": false,
      "description": "A Weekly Podcast Show About Indian Startups\nEntrepreneurs & More !\nHosted by Neil Patel & Friends\n",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 42,
      "total_episodes": 178,
      "listennotes_url": "https://www.listennotes.com/c/24ece1d0922d4d9a9659e9e6cb2b241e/",
      "explicit_content": false,
      "latest_pub_date_ms": 1630710300000,
      "earliest_pub_date_ms": 1439366880177,
      "listen_score_global_rank": "1.5%"
    },
    {
      "id": "b9aa8bbb9e3c426980275b8b052a1215",
      "rss": "http://ishaanlalit.com/sixthworldradio/?feed=podcast",
      "type": "episodic",
      "email": null,
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/sixth-world-radio-TofYFXxGOKn.600x600.jpg",
      "title": "Sixth World Radio",
      "country": null,
      "website": "http://ishaanlalit.com/sixthworldradio?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        99,
        127,
        131,
        133
      ],
      "itunes_id": 942966985,
      "publisher": null,
      "thumbnail": "https://production.listennotes.com/podcasts/sixth-world-radio-TofYFXxGOKn.300x300.jpg",
      "is_claimed": false,
      "description": "<html><body><iframe allowtransparency=\"true\" marginwidth=\"0\" width=\"100%\" frameborder=\"0\" src=\"http://mcc.godaddy.com/park/qzM1oz5urJ55qzphpTW6\" marginheight=\"0\" style=\"visibility: visible;height: 100%; position:absolute\"></iframe>",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": null,
      "total_episodes": 30,
      "listennotes_url": "https://www.listennotes.com/c/b9aa8bbb9e3c426980275b8b052a1215/",
      "explicit_content": false,
      "latest_pub_date_ms": 1481272467000,
      "earliest_pub_date_ms": 1446055111000,
      "listen_score_global_rank": null
    },
    {
      "id": "4151ce9377a6435c8aac7d23f306243d",
      "rss": "https://static.adorilabs.com/feed/geek-fruit-podcast.xml",
      "type": "episodic",
      "email": "shows@indusvox.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9zdGF0aWMuYWRvcmlsYWJzLmNvbS9mZWVkL2dlZWstZnJ1aXQtcG9kY2FzdC54bWw=",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "GeekFruitHQ",
        "facebook_handle": "ivmpodcasts",
        "instagram_handle": "ivmpodcasts"
      },
      "image": "https://production.listennotes.com/podcasts/geek-fruit-podcast-ivm-podcasts-eLbAdx-J8yq-hNgR81AbBO4.1400x1400.jpg",
      "title": "Geek Fruit Podcast",
      "country": "United States",
      "website": "http://ivmpodcasts.com/geekfruit?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        68,
        100,
        103,
        122
      ],
      "itunes_id": 1070891121,
      "publisher": "IVM Podcasts",
      "thumbnail": "https://production.listennotes.com/podcasts/geek-fruit-podcast-ivm-podcasts-lS_yLej9CAr-hNgR81AbBO4.300x300.jpg",
      "is_claimed": true,
      "description": "We spend way too much time discussing minuscule facts, character dynamics, story arcs and unique concepts in the wonderful world of science-fiction and overall nerd culture. Think you do that too? Find us and become one with the geeks! And believe it; the Force is totally strong with us.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 35,
      "total_episodes": 342,
      "listennotes_url": "https://www.listennotes.com/c/4151ce9377a6435c8aac7d23f306243d/",
      "explicit_content": false,
      "latest_pub_date_ms": 1595810106000,
      "earliest_pub_date_ms": 1450868870327,
      "listen_score_global_rank": "3%"
    },
    {
      "id": "2641ed2ce5524b3da43b8f19fe0f5ae9",
      "rss": "https://static.adorilabs.com/feed/cyrus-says.xml",
      "type": "episodic",
      "email": "ivmshows@pratilipi.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9zdGF0aWMuYWRvcmlsYWJzLmNvbS9mZWVkL2N5cnVzLXNheXMueG1s",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "cyrussaysin",
        "facebook_handle": "ivmpodcasts",
        "instagram_handle": "ivmpodcasts"
      },
      "image": "https://production.listennotes.com/podcasts/cyrus-says-ivm-podcasts-IzSsTaoOHZP-1q2UDTO6ztZ.1400x1400.jpg",
      "title": "Cyrus Says",
      "country": "United States",
      "website": "http://ivmpodcasts.com/cyrussays?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        77,
        99,
        133
      ],
      "itunes_id": 979118845,
      "publisher": "IVM Podcasts",
      "thumbnail": "https://production.listennotes.com/podcasts/cyrus-says-ivm-podcasts-GBqMfp5-STP-1q2UDTO6ztZ.300x300.jpg",
      "is_claimed": true,
      "description": "<p>Broadcasting through the week with a rotating panel of guests, Cyrus Says is the definitive show on life in urban India, politics, sports, civic sense, traffic, kids, food, and everything that matters. Mostly.</p>",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 53,
      "total_episodes": 817,
      "listennotes_url": "https://www.listennotes.com/c/2641ed2ce5524b3da43b8f19fe0f5ae9/",
      "explicit_content": false,
      "latest_pub_date_ms": 1635165313000,
      "earliest_pub_date_ms": 1426829400714,
      "listen_score_global_rank": "0.5%"
    },
    {
      "id": "b25da297f2cc434097773ac1da57b1ea",
      "rss": "http://feeds.feedburner.com/therealfoodpodcast",
      "type": "episodic",
      "email": "realfood@audiomatic.in",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-real-food-podcast-audiomatic-Kb91aMGW8JA.1400x1400.jpg",
      "title": "The Real Food Podcast",
      "country": "United States",
      "website": "http://soundcloud.com/the-real-food-podcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        100,
        102
      ],
      "itunes_id": 986251025,
      "publisher": "Audiomatic",
      "thumbnail": "https://production.listennotes.com/podcasts/the-real-food-podcast-audiomatic-Kb91aMGW8JA.300x300.jpg",
      "is_claimed": false,
      "description": "If you have an adventurous palate, join Vikram Doctor every fortnight as he indulges in his appetite for the stories of food. Taste the origins, legends and practical magic of ingredients and recipes that range from the everyday to the extraordinary.\nThrough ancestral kitchens, gourmet restaurants, exotic vegetable farms, modern agriculturists, heirloom aficionados... One of India\u2019s most respected food writers has been there, eaten that and knows that there is no love more sincere than the love of food.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": null,
      "total_episodes": 44,
      "listennotes_url": "https://www.listennotes.com/c/b25da297f2cc434097773ac1da57b1ea/",
      "explicit_content": false,
      "latest_pub_date_ms": 1485346229000,
      "earliest_pub_date_ms": 1429793450000,
      "listen_score_global_rank": null
    },
    {
      "id": "bdeb94c7f7164b14837dcd0449f4a5ee",
      "rss": "http://feeds.feedburner.com/Allindiabakchod",
      "type": "episodic",
      "email": "Allindiabakchod@gmail.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cDovL2ZlZWRzLmZlZWRidXJuZXIuY29tL0FsbGluZGlhYmFrY2hvZA==",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/all-india-bakchod-all-india-bakchod-wx3rMv6WfdH-kgcdJ-xKmAL.1023x990.jpg",
      "title": "All India Bakchod",
      "country": "United States",
      "website": "http://www.allindiabakchod.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        133
      ],
      "itunes_id": 533140007,
      "publisher": "All India Bakchod",
      "thumbnail": "https://production.listennotes.com/podcasts/all-india-bakchod-all-india-bakchod-4kPM70-W_Ue-kgcdJ-xKmAL.300x290.jpg",
      "is_claimed": false,
      "description": "All India Bakchod is India's most widely heard, edgiest, comedy podcast - run by comedians Tanmay Bhat (www.tanmaybhat.com) and Gursimranjeet Khamba (www.gkhamba.com) - It's their take on everything that made it to the news. It's your fortnightly dose of entirely uncensored bakchod. Subscribe away! ",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 44,
      "total_episodes": 8,
      "listennotes_url": "https://www.listennotes.com/c/bdeb94c7f7164b14837dcd0449f4a5ee/",
      "explicit_content": true,
      "latest_pub_date_ms": 1506436886000,
      "earliest_pub_date_ms": 1488805724007,
      "listen_score_global_rank": "1.5%"
    },
    {
      "id": "d203864a67fb43b1a98b7107cabeaa4b",
      "rss": "http://feeds.feedburner.com/OurLastWeek",
      "type": "episodic",
      "email": "ourlastweek@audiomatic.in",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cDovL2ZlZWRzLmZlZWRidXJuZXIuY29tL091ckxhc3RXZWVr",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/our-last-week-audiomatic-ed96Q4pHgsE.1400x1400.jpg",
      "title": "Our Last Week",
      "country": "India",
      "website": "http://soundcloud.com/our-last-week?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        133
      ],
      "itunes_id": 992068781,
      "publisher": "Audiomatic",
      "thumbnail": "https://production.listennotes.com/podcasts/our-last-week-audiomatic-ed96Q4pHgsE.300x300.jpg",
      "is_claimed": false,
      "description": "Podcast by Our Last Week",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 37,
      "total_episodes": 45,
      "listennotes_url": "https://www.listennotes.com/c/d203864a67fb43b1a98b7107cabeaa4b/",
      "explicit_content": false,
      "latest_pub_date_ms": 1579417200000,
      "earliest_pub_date_ms": 1431062738044,
      "listen_score_global_rank": "2.5%"
    },
    {
      "id": "83907f1577724ac1b2c6ab154f8e0566",
      "rss": "https://historyofindiapodcast.libsyn.com/rss",
      "type": "episodic",
      "email": "thehistoryofindiapodcasts@gmail.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9oaXN0b3J5b2ZpbmRpYXBvZGNhc3QubGlic3luLmNvbS9yc3M=",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "historyofindiapodcast",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-history-of-india-podcast-kit-patrick-rpU53uF0ckj-lE64kqFsTHC.1400x1400.jpg",
      "title": "The History of India Podcast",
      "country": "United States",
      "website": "http://www.historyofindiapodcast.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        111,
        113,
        122,
        125
      ],
      "itunes_id": 1041684187,
      "publisher": "Kit Patrick",
      "thumbnail": "https://production.listennotes.com/podcasts/the-history-of-india-podcast-kit-patrick-kCpZW6V-tnP-lE64kqFsTHC.300x300.jpg",
      "is_claimed": false,
      "description": "A light weekly podcast covering the history of India, from 6th century B.C.  Enjoying the podcast? Please consider donating to the Snehal Sidhu Memorial Fund (http://tinyurl.com/prkvwll)",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 57,
      "total_episodes": 142,
      "listennotes_url": "https://www.listennotes.com/c/83907f1577724ac1b2c6ab154f8e0566/",
      "explicit_content": false,
      "latest_pub_date_ms": 1610564400000,
      "earliest_pub_date_ms": 1437820995140,
      "listen_score_global_rank": "0.5%"
    },
    {
      "id": "ff7abc5c7a4d4d01913760375058dead",
      "rss": "http://feeds.feedburner.com/KaanMasti",
      "type": "episodic",
      "email": null,
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/kaanmasti-hoezaay-flIyRD8c4VU.600x600.jpg",
      "title": "KaanMasti",
      "country": null,
      "website": null,
      "language": "English",
      "genre_ids": [
        67,
        133
      ],
      "itunes_id": 524560373,
      "publisher": "Hoezaay",
      "thumbnail": "https://production.listennotes.com/podcasts/kaanmasti-hoezaay-flIyRD8c4VU.300x300.jpg",
      "is_claimed": false,
      "description": "<html><body><iframe marginheight=\"0\" marginwidth=\"0\" allowtransparency=\"true\" style=\"visibility: visible;height: 100%; position:absolute\" src=\"http://mcc.godaddy.com/park/rT5hLKchMzq2YaOvrt==\" width=\"100%\" frameborder=\"0\"></iframe>",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": null,
      "total_episodes": 33,
      "listennotes_url": "https://www.listennotes.com/c/ff7abc5c7a4d4d01913760375058dead/",
      "explicit_content": false,
      "latest_pub_date_ms": 1495259445000,
      "earliest_pub_date_ms": 1337444762000,
      "listen_score_global_rank": null
    },
    {
      "id": "1daa2a04171f44f58f4fba42b77a8203",
      "rss": "https://static.adorilabs.com/feed/tfg-sports-podcast.xml",
      "type": "episodic",
      "email": "shows@indusvox.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9zdGF0aWMuYWRvcmlsYWJzLmNvbS9mZWVkL3RmZy1zcG9ydHMtcG9kY2FzdC54bWw=",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/tfg-sports-podcast-ivm-podcasts-TnJ7PSoMCbA-5Mq0usV3E84.1400x1400.jpg",
      "title": "TFG Sports Podcast",
      "country": "United States",
      "website": "http://ivmpodcasts.com/tfgsportspodcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        77,
        78,
        81
      ],
      "itunes_id": 1062166975,
      "publisher": "IVM Podcasts",
      "thumbnail": "https://production.listennotes.com/podcasts/tfg-sports-podcast-ivm-podcasts-HjVfPrghzdy-5Mq0usV3E84.300x300.jpg",
      "is_claimed": true,
      "description": "TFG Sports podcast is the place to check in for discussion on Indian sports. We talk about Cricket, Football, Kabaddi, Hockey, Athletics and more with a variety of guests and regular contributors.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": null,
      "total_episodes": 565,
      "listennotes_url": "https://www.listennotes.com/c/1daa2a04171f44f58f4fba42b77a8203/",
      "explicit_content": false,
      "latest_pub_date_ms": 1560299400000,
      "earliest_pub_date_ms": 1448286726564,
      "listen_score_global_rank": null
    }
  ],
  "source_url": "https://www.buzzfeed.com/andreborges/17-brilliant-indian-podcasts-thatll-make-you-a-funner-smarte?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
  "description": "\"Think about how much you can soak in on those long commutes.\"",
  "pub_date_ms": 1556561928161,
  "source_domain": "www.buzzfeed.com",
  "listennotes_url": "https://www.listennotes.com/curated-podcasts/16-brilliant-indian-podcasts-thatll-SDFKduyJ47r/"
}
```   
</details>



<details>
  <summary>Click to see response schema</summary>
  
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "example": "Vb017Sx3l8F",
      "description": "Curated list id."
    },
    "title": {
      "type": "string",
      "example": "7 Bookish Podcasts for Avid Readers On the Go",
      "description": "Curated list name."
    },
    "total": {
      "type": "integer",
      "example": 25,
      "description": "The total number of podcasts in this curated list."
    },
    "podcasts": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "example": "4d3fe717742d4963a85562e9f84d8c79",
            "description": "Podcast id."
          },
          "rss": {
            "type": "string",
            "example": "https://sw7x7.libsyn.com/rss",
            "description": "RSS url of this podcast. This field is available only in the PRO/ENTERPRISE plan."
          },
          "type": {
            "enum": [
              "episodic",
              "serial"
            ],
            "type": "string",
            "example": "episodic",
            "description": "The type of this podcast - episodic or serial."
          },
          "email": {
            "type": "string",
            "example": "hello@example.com",
            "description": "The email of this podcast's producer. This field is available only in the PRO/ENTERPRISE plan."
          },
          "extra": {
            "type": "object",
            "properties": {
              "url1": {
                "type": "string",
                "description": "Url affiliated with this podcast"
              },
              "url2": {
                "type": "string",
                "description": "Url affiliated with this podcast"
              },
              "url3": {
                "type": "string",
                "description": "Url affiliated with this podcast"
              },
              "google_url": {
                "type": "string",
                "example": "https://play.google.com/music/listen?u=0#/ps/I7gdcrqcmvhfnhh2cyqkcg32tkq",
                "description": "Google Podcasts url for this podcast"
              },
              "spotify_url": {
                "type": "string",
                "example": "https://open.spotify.com/show/2rQJUP9Y3HxemiW3JHt9WV",
                "description": "Spotify url for this podcast"
              },
              "youtube_url": {
                "type": "string",
                "example": "https://www.youtube.com/sw7x7",
                "description": "YouTube url affiliated with this podcast"
              },
              "linkedin_url": {
                "type": "string",
                "description": "LinkedIn url affiliated with this podcast"
              },
              "wechat_handle": {
                "type": "string",
                "description": "WeChat username affiliated with this podcast"
              },
              "patreon_handle": {
                "type": "string",
                "example": "sw7x7",
                "description": "Patreon username affiliated with this podcast"
              },
              "twitter_handle": {
                "type": "string",
                "example": "SW7x7podcast",
                "description": "Twitter username affiliated with this podcast"
              },
              "facebook_handle": {
                "type": "string",
                "example": "sw7x7",
                "description": "Facebook username affiliated with this podcast"
              },
              "instagram_handle": {
                "type": "string",
                "example": "sw7x7",
                "description": "Instagram username affiliated with this podcast"
              }
            }
          },
          "image": {
            "type": "string",
            "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
            "description": "Image url for this podcast's artwork. If you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
          },
          "title": {
            "type": "string",
            "example": "Star Wars 7x7 | Star Wars News, Interviews, and More!",
            "description": "Podcast name."
          },
          "country": {
            "type": "string",
            "example": "United States",
            "description": "The country where this podcast is produced."
          },
          "website": {
            "type": "string",
            "example": "http://sw7x7.com/",
            "description": "Website url of this podcast."
          },
          "language": {
            "type": "string",
            "example": "English",
            "description": "The language of this podcast. You can get all supported languages from `GET /languages`."
          },
          "genre_ids": {
            "type": "array",
            "items": {
              "type": "integer",
              "description": "Genre ids."
            },
            "example": [
              138,
              86,
              160,
              68,
              82,
              100,
              101
            ]
          },
          "itunes_id": {
            "type": "integer",
            "example": 896354638,
            "description": "iTunes id for this podcast."
          },
          "publisher": {
            "type": "string",
            "example": "Planet Broadcasting",
            "description": "Podcast publisher name."
          },
          "thumbnail": {
            "type": "string",
            "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
            "description": "Thumbnail image url for this podcast's artwork (300x300)."
          },
          "is_claimed": {
            "type": "boolean",
            "example": true,
            "description": "Whether this podcast is claimed by its producer on [ListenNotes.com](https://www.ListenNotes.com)."
          },
          "description": {
            "type": "string",
            "example": "<p>The Star Wars 7x7 Podcast is Rebel-rousing fun for everyday Jedi, between 7 and 14 minutes a day, 7 days a week. Join host Allen Voivod for Star Wars news, history, interviews, trivia, and deep dives into the Star Wars story as told in movies, books, comics, games, cartoons, and more. Subscribe now for your daily dose of Star Wars joy. It's destiny unleashed!</p>",
            "description": "Html of this episode's full description"
          },
          "looking_for": {
            "type": "object",
            "properties": {
              "guests": {
                "type": "boolean",
                "example": true,
                "description": "Whether this podcast is looking for guests."
              },
              "cohosts": {
                "type": "boolean",
                "example": true,
                "description": "Whether this podcast is looking for cohosts."
              },
              "sponsors": {
                "type": "boolean",
                "example": true,
                "description": "Whether this podcast is looking for sponsors."
              },
              "cross_promotion": {
                "type": "boolean",
                "example": true,
                "description": "Whether this podcast is looking for cross promotion opportunities with other podcasts."
              }
            }
          },
          "listen_score": {
            "type": "integer",
            "example": 81,
            "description": "The estimated popularity score of a podcast compared to all other rss-based public podcasts in the world on a scale from 0 to 100.\nIf the score is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
          },
          "total_episodes": {
            "type": "integer",
            "example": 324,
            "description": "Total number of episodes in this podcast."
          },
          "listennotes_url": {
            "type": "string",
            "example": "https://www.listennotes.com/c/4d3fe717742d4963a85562e9f84d8c79/",
            "description": "The url of this podcast on [ListenNotes.com](https://www.ListenNotes.com)."
          },
          "explicit_content": {
            "type": "boolean",
            "example": false,
            "description": "Whether this podcast contains explicit language."
          },
          "latest_pub_date_ms": {
            "type": "integer",
            "example": 1557499770000,
            "description": "The published date of the latest episode of this podcast. In milliseconds"
          },
          "earliest_pub_date_ms": {
            "type": "integer",
            "example": 1470667902000,
            "description": "The published date of the oldest episode of this podcast. In milliseconds"
          },
          "listen_score_global_rank": {
            "type": "string",
            "example": "0.5%",
            "description": "The estimated popularity ranking of a podcast compared to all other rss-based public podcasts in the world.\nFor example, if the value is 0.5%, then this podcast is one of the top 0.5% most popular shows out of all podcasts globally, ranked by Listen Score.\nIf the ranking is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
          }
        }
      },
      "description": "Complete meta data of all podcasts in this curated list."
    },
    "source_url": {
      "type": "string",
      "example": "https://parade.com/718913/ashley_johnson/7-bookish-podcasts-for-avid-readers-on-the-go/",
      "description": "Url of the source of this curated list."
    },
    "description": {
      "type": "string",
      "example": "Commuting to work is always better when you have a great new podcast to listen to, and this year, we have discovered some of our favorite podcasts yet for readers and book-lovers. These podcasts for readers entertain us and provide no shortage of new book recommendations too.",
      "description": "This curated list's description."
    },
    "pub_date_ms": {
      "type": "integer",
      "example": 1556843484301,
      "description": "Published date of this curated list. In milliseconds."
    },
    "source_domain": {
      "type": "string",
      "example": "parade.com",
      "description": "The domain name of the source of this curated list."
    },
    "listennotes_url": {
      "type": "string",
      "example": "https://www.listennotes.com/curated-podcasts/7-bookish-podcasts-for-avid-readers-on-H2r-TCWai8K/",
      "description": "The url of this curated list on [ListenNotes.com](https://www.ListenNotes.com)."
    }
  }
}
```   
</details>




### Fetch curated lists of podcasts

Function Name: **fetch_curated_podcasts_lists**

A bunch of curated lists from online media. For each list, you&#x27;ll get basic info of up to 5 podcasts. To get detailed meta data of all podcasts in a specific list, you need to use `GET /curated_podcasts/{id}`. We add new curated lists to the database on a daily basis.


Example:
```python

from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)      

response = client.fetch_curated_podcasts_lists(page=2)
            
print(response.json())

```

See all available parameters on the [API Docs page](https://www.listennotes.com/api/docs/#get-api-v2-curated_podcasts).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "total": 3771,
  "has_next": true,
  "page_number": 2,
  "has_previous": true,
  "curated_lists": [
    {
      "id": "bG5rTvdxsES",
      "title": "Cebuano podcasts you should listen to",
      "total": 3,
      "podcasts": [
        {
          "id": "4f8461c536444856867c8c24fbce3d7f",
          "image": "https://production.listennotes.com/podcasts/skypodcast-kryz-and-slater-3gBJ7KYV8an-2PwgxC76j9S.1400x1400.jpg",
          "title": "skypodcast",
          "publisher": "Kryz and Slater",
          "thumbnail": "https://production.listennotes.com/podcasts/skypodcast-kryz-and-slater-pxXF_TDltVh-2PwgxC76j9S.300x300.jpg",
          "listen_score": 39,
          "listennotes_url": "https://www.listennotes.com/c/4f8461c536444856867c8c24fbce3d7f/",
          "listen_score_global_rank": "2%"
        },
        {
          "id": "da0848364d54445584c01310c4f1a40f",
          "image": "https://production.listennotes.com/podcasts/basabalak-kanunay-cindy-velasquez-58bix0uIB6t-mLW2HxGfYj0.1400x1400.jpg",
          "title": "Basabalak Kanunay",
          "publisher": "Cindy Velasquez",
          "thumbnail": "https://production.listennotes.com/podcasts/basabalak-kanunay-cindy-velasquez-uVDznFr4bpo-mLW2HxGfYj0.300x300.jpg",
          "listen_score": null,
          "listennotes_url": "https://www.listennotes.com/c/da0848364d54445584c01310c4f1a40f/",
          "listen_score_global_rank": null
        },
        {
          "id": "2f1be988113f4e888be7324195fe0404",
          "image": "https://production.listennotes.com/podcasts/the-big-picture-philippines-dave-visaya-and-Eb7CJfWcAPh-S0MDNIdo4sA.1400x1400.jpg",
          "title": "The Big Picture Philippines",
          "publisher": "Dave Visaya and Joseph Librero",
          "thumbnail": "https://production.listennotes.com/podcasts/the-big-picture-philippines-dave-visaya-and-9s8Pi3ehIcb-S0MDNIdo4sA.300x300.jpg",
          "listen_score": null,
          "listennotes_url": "https://www.listennotes.com/c/2f1be988113f4e888be7324195fe0404/",
          "listen_score_global_rank": null
        }
      ],
      "source_url": "https://ph.news.yahoo.com/cebuano-podcasts-listen-124400380.html?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"Here are some of the Cebuano podcasts to listen to right now:\"",
      "pub_date_ms": 1633832483263,
      "source_domain": "ph.news.yahoo.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/cebuano-podcasts-you-should-listen-to-bG5rTvdxsES/"
    },
    {
      "id": "M24KBZnqXJt",
      "title": "Vaccine Scammers, Scream Queens, and 4 More Podcasts Worth Trying",
      "total": 5,
      "podcasts": [
        {
          "id": "ab6b3988fc994ea697d377b3795174a2",
          "image": "https://production.listennotes.com/podcasts/half-vaxxed-bJ8Im2pcveq-Fc4VgSy7DeJ.1400x1400.jpg",
          "title": "Half Vaxxed: The Rise and Fall of Philly Fighting COVID",
          "publisher": "WHYY",
          "thumbnail": "https://production.listennotes.com/podcasts/half-vaxxed-2U41z0eE8ix-Fc4VgSy7DeJ.300x300.jpg",
          "listen_score": 39,
          "listennotes_url": "https://www.listennotes.com/c/ab6b3988fc994ea697d377b3795174a2/",
          "listen_score_global_rank": "2%"
        },
        {
          "id": "776efe7ea84d4872ac6ff910b5ea83af",
          "image": "https://production.listennotes.com/podcasts/the-just-enough-family-DfPWMjZm1R2-7y8GMl0VqfT.1400x1400.jpg",
          "title": "The Just Enough Family",
          "publisher": "Three Uncanny Four",
          "thumbnail": "https://production.listennotes.com/podcasts/the-just-enough-family-fHGtOVvcmn_-7y8GMl0VqfT.300x300.jpg",
          "listen_score": 49,
          "listennotes_url": "https://www.listennotes.com/c/776efe7ea84d4872ac6ff910b5ea83af/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "c271aec8150149599f8cb7c387a8dad1",
          "image": "https://production.listennotes.com/podcasts/scream-queen-domino-sound-tmaBNqjxiz8-Yhb2fV697tv.1400x1400.jpg",
          "title": "Scream, Queen!",
          "publisher": "Domino Sound",
          "thumbnail": "https://production.listennotes.com/podcasts/scream-queen-domino-sound-ZdfMn6WN_29-Yhb2fV697tv.300x300.jpg",
          "listen_score": 40,
          "listennotes_url": "https://www.listennotes.com/c/c271aec8150149599f8cb7c387a8dad1/",
          "listen_score_global_rank": "2%"
        },
        {
          "id": "81ab79ffad794edab15e5b616d196650",
          "image": "https://production.listennotes.com/podcasts/straightiolab-sam-taggart-and-george-civeris-GCb617eoKvT-vnYD5R87bPe.1400x1400.jpg",
          "title": "StraightioLab",
          "publisher": "Sam Taggart and George Civeris",
          "thumbnail": "https://production.listennotes.com/podcasts/straightiolab-sam-taggart-and-george-civeris-uk09sbOLSio-vnYD5R87bPe.300x300.jpg",
          "listen_score": 52,
          "listennotes_url": "https://www.listennotes.com/c/81ab79ffad794edab15e5b616d196650/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "4bc70cf520544a798e158da781443e43",
          "image": "https://production.listennotes.com/podcasts/heavyweight-gimlet-4r3EXglpIbt-8mLFsBqwvMR.1400x1400.jpg",
          "title": "Heavyweight",
          "publisher": "Gimlet",
          "thumbnail": "https://production.listennotes.com/podcasts/heavyweight-gimlet-uFmNXP4xgqD-8mLFsBqwvMR.300x300.jpg",
          "listen_score": 79,
          "listennotes_url": "https://www.listennotes.com/c/4bc70cf520544a798e158da781443e43/",
          "listen_score_global_rank": "0.01%"
        }
      ],
      "source_url": "https://www.vulture.com/2021/10/best-podcasts-newsletter-half-vaxxed.html?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"Am I a bad art friend? Hey, I\u2019m your bad art friend. This is 1.5x Speed, your listening guide to the podcast world, plus some other things, too.\"",
      "pub_date_ms": 1633627010087,
      "source_domain": "www.vulture.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/vaccine-scammers-scream-queens-and-4-M24KBZnqXJt/"
    },
    {
      "id": "DPIYGmOFxCs",
      "title": "27 Marketing Podcasts That Inspire HubSpot's Content Team",
      "total": 27,
      "podcasts": [
        {
          "id": "8da6f9f6c1224d08be575d5371c62089",
          "image": "https://production.listennotes.com/podcasts/the-shake-up-fGwiyMBhTZ9-sYbOwiBvPfX.1400x1400.jpg",
          "title": "The Shake Up",
          "publisher": "HubSpot",
          "thumbnail": "https://production.listennotes.com/podcasts/the-shake-up-JE5LPpMk0Hm-sYbOwiBvPfX.300x300.jpg",
          "listen_score": 38,
          "listennotes_url": "https://www.listennotes.com/c/8da6f9f6c1224d08be575d5371c62089/",
          "listen_score_global_rank": "2.5%"
        },
        {
          "id": "72da7d9bd0474055a7f3fe523c6def1d",
          "image": "https://production.listennotes.com/podcasts/my-first-million-the-hustle-shaan-puri-qS_m1a9UOg7-Vmz8LP7xJOS.1400x1400.jpg",
          "title": "My First Million",
          "publisher": "The Hustle & Shaan Puri",
          "thumbnail": "https://production.listennotes.com/podcasts/my-first-million-the-hustle-shaan-puri-lt8LUG0i2zZ-Vmz8LP7xJOS.300x300.jpg",
          "listen_score": 63,
          "listennotes_url": "https://www.listennotes.com/c/72da7d9bd0474055a7f3fe523c6def1d/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "e1543ac1250743729269e9e19155dae0",
          "image": "https://production.listennotes.com/podcasts/idigress-with-troy-sandidge-troy-sandidge-sMRI-bTlDjJ-mVsarlHcPNJ.1400x1400.jpg",
          "title": "iDigress with Troy Sandidge",
          "publisher": "Troy Sandidge",
          "thumbnail": "https://production.listennotes.com/podcasts/idigress-with-troy-sandidge-troy-sandidge-EJTiC-sSyH6-mVsarlHcPNJ.300x300.jpg",
          "listen_score": 52,
          "listennotes_url": "https://www.listennotes.com/c/e1543ac1250743729269e9e19155dae0/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "2c8a37b61cb84202a2f7bee3822bb6d6",
          "image": "https://production.listennotes.com/podcasts/podcast-duct-tape-marketing-consultant-8olwsO3V9CW-OMh1aXmdzWf.1400x1400.jpg",
          "title": "Podcast \u2013 Duct Tape Marketing Consultant",
          "publisher": "Podcast \u2013 Duct Tape Marketing Consultant",
          "thumbnail": "https://production.listennotes.com/podcasts/podcast-duct-tape-marketing-consultant-I0sGgi-LmZJ-OMh1aXmdzWf.300x300.jpg",
          "listen_score": null,
          "listennotes_url": "https://www.listennotes.com/c/2c8a37b61cb84202a2f7bee3822bb6d6/",
          "listen_score_global_rank": null
        },
        {
          "id": "e34fd9c29d574972965bb5f013ddb4c1",
          "image": "https://production.listennotes.com/podcasts/marketing-made-simple-powered-by-storybrand-GYPbQ5Ozi20-udlEHL-0Vr1.1400x1400.jpg",
          "title": "Marketing Made Simple",
          "publisher": "Powered by StoryBrand",
          "thumbnail": "https://production.listennotes.com/podcasts/marketing-made-simple-powered-by-storybrand-N3dFgDf-Gvb-udlEHL-0Vr1.300x300.jpg",
          "listen_score": 44,
          "listennotes_url": "https://www.listennotes.com/c/e34fd9c29d574972965bb5f013ddb4c1/",
          "listen_score_global_rank": "1.5%"
        }
      ],
      "source_url": "https://www.marketscreener.com/quote/stock/HUBSPOT-INC-45166580/news/HubSpot-27-Marketing-Podcasts-That-Inspire-HubSpot-s-Content-Team-36598802/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\u201cPodcasts offer knowledge and inspiration in an easy-to-digest format for a variety of topics. If sharpening your skills as a marketer is on your list of priorities, then tuning into marketing-focused podcasts can be a great way to prioritize your professional development.\u201d",
      "pub_date_ms": 1633393182444,
      "source_domain": "www.marketscreener.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/27-marketing-podcasts-that-inspire-DPIYGmOFxCs/"
    },
    {
      "id": "I4jtDr103ga",
      "title": "The 15 Best True Crime Podcasts of All-Time",
      "total": 17,
      "podcasts": [
        {
          "id": "02e194651c6240e6b95c8e38729af63b",
          "image": "https://production.listennotes.com/podcasts/casefile-true-crime-casefile-presents-AqHXPmVQEB9-DG5lH8yuLgi.1400x1400.jpg",
          "title": "Casefile True Crime",
          "publisher": "Casefile Presents",
          "thumbnail": "https://production.listennotes.com/podcasts/casefile-true-crime-casefile-presents-gpCUoc9A4Jl-DG5lH8yuLgi.300x300.jpg",
          "listen_score": 88,
          "listennotes_url": "https://www.listennotes.com/c/02e194651c6240e6b95c8e38729af63b/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "44d2110a792b4e2b85f2303abaef75e9",
          "image": "https://production.listennotes.com/podcasts/crime-junkie-audiochuck-NRFDTn54WYh-BWDcryRL6xl.1400x1400.jpg",
          "title": "Crime Junkie",
          "publisher": "audiochuck",
          "thumbnail": "https://production.listennotes.com/podcasts/crime-junkie-audiochuck-5yH6plhgjR2-BWDcryRL6xl.300x300.jpg",
          "listen_score": 98,
          "listennotes_url": "https://www.listennotes.com/c/44d2110a792b4e2b85f2303abaef75e9/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "a4488ab6af7b418b874a9d9f5b6870b6",
          "image": "https://production.listennotes.com/podcasts/true-crime-all-the-time-unsolved-podcastone-ZGn12FvNj58-h9FuPAj-op3.1400x1400.jpg",
          "title": "True Crime All The Time Unsolved",
          "publisher": "PodcastOne",
          "thumbnail": "https://production.listennotes.com/podcasts/true-crime-all-the-time-unsolved-podcastone-lepS8kKTv9o-h9FuPAj-op3.300x300.jpg",
          "listen_score": 69,
          "listennotes_url": "https://www.listennotes.com/c/a4488ab6af7b418b874a9d9f5b6870b6/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "34c89da1490948a484f1f954600e3d0e",
          "image": "https://production.listennotes.com/podcasts/criminology-emash-digital-mike-ferguson-Zs3N_KljkBO--Fjr1L5sf4_.1400x1400.jpg",
          "title": "Criminology",
          "publisher": "Emash Digital & Mike Ferguson, Mike Morford",
          "thumbnail": "https://production.listennotes.com/podcasts/criminology-emash-digital-mike-ferguson-WeDsZK0nzFd--Fjr1L5sf4_.300x300.jpg",
          "listen_score": 71,
          "listennotes_url": "https://www.listennotes.com/c/34c89da1490948a484f1f954600e3d0e/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "08e7e64e80ac456a8ce0027f07dc40d0",
          "image": "https://production.listennotes.com/podcasts/morbid-a-true-crime-podcast-morbid-a-true-owJCuTLqdkf-krRXUPe1dbC.1400x1400.jpg",
          "title": "Morbid: A True Crime Podcast",
          "publisher": "Morbid: A True Crime Podcast",
          "thumbnail": "https://production.listennotes.com/podcasts/morbid-a-true-crime-podcast-morbid-a-true-Jc0iPX8x5KS-krRXUPe1dbC.300x300.jpg",
          "listen_score": 84,
          "listennotes_url": "https://www.listennotes.com/c/08e7e64e80ac456a8ce0027f07dc40d0/",
          "listen_score_global_rank": "0.01%"
        }
      ],
      "source_url": "https://www.tvovermind.com/best-true-crime-podcasts-of-all-time/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"No matter what kinds of cases you like to learn about and/or research, this list will have something for you.  Keep reading to see our list of the 15 best true crime podcasts of all time.\"",
      "pub_date_ms": 1633238495652,
      "source_domain": "www.tvovermind.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/the-15-best-true-crime-podcasts-of-all-I4jtDr103ga/"
    },
    {
      "id": "5mbhZYnQAez",
      "title": "3 Must-Hear Climate Podcasts",
      "total": 3,
      "podcasts": [
        {
          "id": "3a076288ad90457396a34a3035429f88",
          "image": "https://production.listennotes.com/podcasts/threshold-auricle-productions-PkW76tp4a5Z-Sw1ZNvFBk8R.1400x1400.jpg",
          "title": "Threshold",
          "publisher": "Auricle Productions",
          "thumbnail": "https://production.listennotes.com/podcasts/threshold-auricle-productions-qHLcK1uSe3X-Sw1ZNvFBk8R.300x300.jpg",
          "listen_score": 51,
          "listennotes_url": "https://www.listennotes.com/c/3a076288ad90457396a34a3035429f88/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "ff08bfe7e4204ed792fbf2123db47dcd",
          "image": "https://production.listennotes.com/podcasts/generation-anthropocene-generation-i2duwJhbKqZ-y1NwBnxK8LW.1400x1400.jpg",
          "title": "Generation Anthropocene",
          "publisher": "Generation Anthropocene",
          "thumbnail": "https://production.listennotes.com/podcasts/generation-anthropocene-generation-6Z0IyYjHn8Q-y1NwBnxK8LW.300x300.jpg",
          "listen_score": 45,
          "listennotes_url": "https://www.listennotes.com/c/ff08bfe7e4204ed792fbf2123db47dcd/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "b2954aa1f9bc420fa48f657874efa447",
          "image": "https://production.listennotes.com/podcasts/outsidein-new-hampshire-public-radio-panoply-hecNriGHZu1-4iRcI1mTS6M.1400x1400.jpg",
          "title": "Outside/In",
          "publisher": "New Hampshire Public Radio / Panoply",
          "thumbnail": "https://production.listennotes.com/podcasts/outsidein-new-hampshire-public-radio-panoply-HKt3BgJcpYw-4iRcI1mTS6M.300x300.jpg",
          "listen_score": 61,
          "listennotes_url": "https://www.listennotes.com/c/b2954aa1f9bc420fa48f657874efa447/",
          "listen_score_global_rank": "0.5%"
        }
      ],
      "source_url": "https://www.sierraclub.org/sierra/2021-4-fall/critic-s-notebook/3-must-hear-climate-podcasts?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"These podcasts take climate storytelling to new heights.\"",
      "pub_date_ms": 1633237996380,
      "source_domain": "www.sierraclub.org",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/3-must-hear-climate-podcasts-5mbhZYnQAez/"
    },
    {
      "id": "LZU_hDcGVT4",
      "title": "New Beer Podcasts Are Giving Voice to Diversity and Inclusion",
      "total": 10,
      "podcasts": [
        {
          "id": "e8451477e09e4a6397e997ec53254b99",
          "image": "https://production.listennotes.com/podcasts/bitch-beer-podcast-bitch-beer-podcast-yhOFg1b4jCA-Ue1GL3XB5yv.645x645.jpg",
          "title": "Bitch Beer Podcast",
          "publisher": "Bitch Beer Podcast",
          "thumbnail": "https://production.listennotes.com/podcasts/bitch-beer-podcast-bitch-beer-podcast-1lO5yufzZ2b-Ue1GL3XB5yv.300x300.jpg",
          "listen_score": 32,
          "listennotes_url": "https://www.listennotes.com/c/e8451477e09e4a6397e997ec53254b99/",
          "listen_score_global_rank": "5%"
        },
        {
          "id": "98701bbe12c74faf9cd9c3b9f58baea2",
          "image": "https://production.listennotes.com/podcasts/brewing-after-hours-with-sarah-flora-X2DSQc6MJYF-xIOgou7F94v.1400x1400.jpg",
          "title": "Brewing After Hours with Sarah Flora",
          "publisher": "Sarah Flora | Bleav Podcast Network",
          "thumbnail": "https://production.listennotes.com/podcasts/brewing-after-hours-with-sarah-flora-6aWINRquCFn-xIOgou7F94v.300x300.jpg",
          "listen_score": 30,
          "listennotes_url": "https://www.listennotes.com/c/98701bbe12c74faf9cd9c3b9f58baea2/",
          "listen_score_global_rank": "5%"
        },
        {
          "id": "e56ef01047484243a3da92b83c66c358",
          "image": "https://production.listennotes.com/podcasts/false-bottomed-girls-jen-blair-fTsaXHy10LV-UI8fv2YmJeM.1400x1400.jpg",
          "title": "False Bottomed Girls",
          "publisher": "Jen Blair & Rachael Hudson",
          "thumbnail": "https://production.listennotes.com/podcasts/false-bottomed-girls-jen-blair-cfPAKuSJT-3-UI8fv2YmJeM.300x300.jpg",
          "listen_score": 30,
          "listennotes_url": "https://www.listennotes.com/c/e56ef01047484243a3da92b83c66c358/",
          "listen_score_global_rank": "5%"
        },
        {
          "id": "e1cb74a95d6a45f581c7a9b6c0c7bd06",
          "image": "https://production.listennotes.com/podcasts/beer-with-nat-natalya-watson-1Zw9-VEnv0X.1400x1400.jpg",
          "title": "Beer with Nat",
          "publisher": "Natalya Watson",
          "thumbnail": "https://production.listennotes.com/podcasts/beer-with-nat-natalya-watson-1Zw9-VEnv0X.300x300.jpg",
          "listen_score": 32,
          "listennotes_url": "https://www.listennotes.com/c/e1cb74a95d6a45f581c7a9b6c0c7bd06/",
          "listen_score_global_rank": "5%"
        },
        {
          "id": "4069145bb7434103824e5062c0cbeb00",
          "image": "https://production.listennotes.com/podcasts/the-beer-wax-society-chris-maestro-knjPwetLVE_-w5Nm2_KlHb6.1400x1400.jpg",
          "title": "The Beer & Wax Society ",
          "publisher": "Chris Maestro ",
          "thumbnail": "https://production.listennotes.com/podcasts/the-beer-wax-society-chris-maestro-kqnrA8HYt21-w5Nm2_KlHb6.300x300.jpg",
          "listen_score": null,
          "listennotes_url": "https://www.listennotes.com/c/4069145bb7434103824e5062c0cbeb00/",
          "listen_score_global_rank": null
        }
      ],
      "source_url": "https://vinepair.com/articles/new-beer-podcasts-diversity-inclusion/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"Last year\u2019s pandemic lockdowns left many of us with a lot more time on our hands than we\u2019re used to. Some of us picked up a new hobby; some learned a new skill; some rebelled against the idea that we were expected to be productive. And in the midst of our collective trauma and anxiety, some of us created podcasts.\"",
      "pub_date_ms": 1633134497363,
      "source_domain": "vinepair.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/new-beer-podcasts-are-giving-voice-to-LZU_hDcGVT4/"
    },
    {
      "id": "i0p9h3FJXSH",
      "title": "10 Podcasts That Should Be On Every Astrology Lover\u2019s Radar",
      "total": 10,
      "podcasts": [
        {
          "id": "715c9f40b6a34f4e9fa81e6d0a7238eb",
          "image": "https://production.listennotes.com/podcasts/allegedly-astrology-dana-defranco-elyse-dTKFVtCoAUE-0pWu-HCvlx1.1400x1400.jpg",
          "title": "Allegedly Astrology",
          "publisher": "Dana DeFranco, Elyse Carlucci, Sarah Dembkowski",
          "thumbnail": "https://production.listennotes.com/podcasts/allegedly-astrology-dana-defranco-elyse-Xnz7lUas-r8-0pWu-HCvlx1.300x300.jpg",
          "listen_score": 41,
          "listennotes_url": "https://www.listennotes.com/c/715c9f40b6a34f4e9fa81e6d0a7238eb/",
          "listen_score_global_rank": "1.5%"
        },
        {
          "id": "a8200cf37cd6415aaaf00aecb48fa13e",
          "image": "https://production.listennotes.com/podcasts/astrotwins-radio-astrotwins-9kDltjSI4pE-YFTZua1-mO2.1400x1400.jpg",
          "title": "AstroTwins Radio",
          "publisher": "AstroTwins",
          "thumbnail": "https://production.listennotes.com/podcasts/astrotwins-radio-astrotwins-kUEjvpuaRf6-YFTZua1-mO2.300x300.jpg",
          "listen_score": 36,
          "listennotes_url": "https://www.listennotes.com/c/a8200cf37cd6415aaaf00aecb48fa13e/",
          "listen_score_global_rank": "3%"
        },
        {
          "id": "355d83c2296742f7a04ba0e6c1ce51ae",
          "image": "https://production.listennotes.com/podcasts/the-astrology-podcast-chris-brennan-bPA1vUkXMdL-_ou-KUHdDzI.1400x1400.jpg",
          "title": "The Astrology Podcast",
          "publisher": "Chris Brennan",
          "thumbnail": "https://production.listennotes.com/podcasts/the-astrology-podcast-chris-brennan-amWp7rAkPoi-_ou-KUHdDzI.300x300.jpg",
          "listen_score": 60,
          "listennotes_url": "https://www.listennotes.com/c/355d83c2296742f7a04ba0e6c1ce51ae/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "6a664e5f73c345f9be44c0fe42f804eb",
          "image": "https://production.listennotes.com/podcasts/moon-matters-astrology-podcast-dalanah-cpEyWIrTkOG-FtRnMv1I6zl.1400x1400.jpg",
          "title": "Moon Matters Podcast",
          "publisher": "Dalanah",
          "thumbnail": "https://production.listennotes.com/podcasts/moon-matters-astrology-podcast-dalanah-qcUFXK92Ny8-FtRnMv1I6zl.300x300.jpg",
          "listen_score": 36,
          "listennotes_url": "https://www.listennotes.com/c/6a664e5f73c345f9be44c0fe42f804eb/",
          "listen_score_global_rank": "3%"
        },
        {
          "id": "471590d102164a2fb2dbb07dd9c924bc",
          "image": "https://production.listennotes.com/podcasts/astrology-and-you-alice-bell-maxine-luz\u00eda-VWs0HfJAzBT-XxiwdjUy-lG.1400x1400.jpg",
          "title": "Astrology and You",
          "publisher": "Alice Bell, Maxine Luz\u00eda",
          "thumbnail": "https://production.listennotes.com/podcasts/astrology-and-you-alice-bell-maxine-luz\u00eda-AU_dHQJr-5p-XxiwdjUy-lG.300x300.jpg",
          "listen_score": 43,
          "listennotes_url": "https://www.listennotes.com/c/471590d102164a2fb2dbb07dd9c924bc/",
          "listen_score_global_rank": "1.5%"
        }
      ],
      "source_url": "https://www.bustle.com/life/best-astrology-podcasts?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"So, if you\u2019re looking to dive deeper into the specific details of your birth chart \u2014 knowing the energies in your houses and learning more about your Saturn return \u2014 these 10 astrology podcasts are some of the best guides.\"",
      "pub_date_ms": 1633134346929,
      "source_domain": "www.bustle.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/10-podcasts-that-should-be-on-every-i0p9h3FJXSH/"
    },
    {
      "id": "R0mblKeiH62",
      "title": "10 BEST podcasts for Russian language students of ALL levels",
      "total": 10,
      "podcasts": [
        {
          "id": "dd0657fbb5bf470c8188ac3aef9cc1f9",
          "image": "https://production.listennotes.com/podcasts/learn-beginner-russian-fluentli-language-s2Vxw4fdlSv.600x600.jpg",
          "title": "Learn Beginner Russian",
          "publisher": "Fluentli | Language Learning Q&A",
          "thumbnail": "https://production.listennotes.com/podcasts/learn-beginner-russian-fluentli-language-s2Vxw4fdlSv.300x300.jpg",
          "listen_score": null,
          "listennotes_url": "https://www.listennotes.com/c/dd0657fbb5bf470c8188ac3aef9cc1f9/",
          "listen_score_global_rank": null
        },
        {
          "id": "eaecef4c24c544e6861d7c1f08e25df7",
          "image": "https://production.listennotes.com/podcasts/one-minute-russian-radio-lingua-network-Q5t4WZ1I_SO-1PobCwK9J3r.1400x1400.jpg",
          "title": "One Minute Russian",
          "publisher": "Radio Lingua Network",
          "thumbnail": "https://production.listennotes.com/podcasts/one-minute-russian-radio-lingua-network-olGFbnWAZM3-1PobCwK9J3r.300x300.jpg",
          "listen_score": 39,
          "listennotes_url": "https://www.listennotes.com/c/eaecef4c24c544e6861d7c1f08e25df7/",
          "listen_score_global_rank": "2%"
        },
        {
          "id": "85013b9931214cfc890d45b4f00fa4dc",
          "image": "https://production.listennotes.com/podcasts/russian-made-easy-learn-russian-quickly-and-c65CzmfaJo1.1400x1400.jpg",
          "title": "Russian Made Easy: Learn Russian Quickly and Easily",
          "publisher": "Russian Made Easy: Learn Russian Quickly and Easily",
          "thumbnail": "https://production.listennotes.com/podcasts/russian-made-easy-learn-russian-quickly-and-c65CzmfaJo1.300x300.jpg",
          "listen_score": 48,
          "listennotes_url": "https://www.listennotes.com/c/85013b9931214cfc890d45b4f00fa4dc/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "9f294276af994751993f2c2cf1e6f26f",
          "image": "https://production.listennotes.com/podcasts/slow-russian-daria-molchanova-hK98V_FepCu-oDOR4fZc6HK.1400x1400.jpg",
          "title": "Slow Russian",
          "publisher": "Daria Molchanova",
          "thumbnail": "https://production.listennotes.com/podcasts/slow-russian-daria-molchanova-6lMTwRDqIQB-oDOR4fZc6HK.300x300.jpg",
          "listen_score": 52,
          "listennotes_url": "https://www.listennotes.com/c/9f294276af994751993f2c2cf1e6f26f/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "f0925a3ec6fd4c6ea1c1a93a93bb4f70",
          "image": "https://production.listennotes.com/podcasts/the-words-worth-the-moscow-times-7isWZFf5N9S-mQ6Mre0kLyI.1400x1400.jpg",
          "title": "The Word's Worth",
          "publisher": "The Moscow Times",
          "thumbnail": "https://production.listennotes.com/podcasts/the-words-worth-the-moscow-times-HVy5fo-O0Ln-mQ6Mre0kLyI.300x300.jpg",
          "listen_score": 39,
          "listennotes_url": "https://www.listennotes.com/c/f0925a3ec6fd4c6ea1c1a93a93bb4f70/",
          "listen_score_global_rank": "2%"
        }
      ],
      "source_url": "https://www.rbth.com/lifestyle/334243-best-podcasts-to-learn-russian?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"From beginner to advanced, pick your course and hone your skills. Davai!\"",
      "pub_date_ms": 1633043172093,
      "source_domain": "www.rbth.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/10-best-podcasts-for-russian-language-R0mblKeiH62/"
    },
    {
      "id": "Nu_GgVazPDJ",
      "title": "Five of the best podcasts: laugh-out-loud fictional comedies",
      "total": 4,
      "podcasts": [
        {
          "id": "38c3db933bb74a7a8ec41163833e2f2a",
          "image": "https://production.listennotes.com/podcasts/dear-joan-and-jericha-julia-davis-and-vicki-6oCMwgYkmzB-GFo8kHtvNBf.1400x1400.jpg",
          "title": "Dear Joan and Jericha (Julia Davis and Vicki Pepperdine)",
          "publisher": "Hush Ho and Pepperdine Productions.",
          "thumbnail": "https://production.listennotes.com/podcasts/dear-joan-and-jericha-julia-davis-and-vicki-l4Ts1gWMjGL-GFo8kHtvNBf.300x300.jpg",
          "listen_score": 70,
          "listennotes_url": "https://www.listennotes.com/c/38c3db933bb74a7a8ec41163833e2f2a/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "10ee196a6fb248a08f57cd2c55c5f648",
          "image": "https://production.listennotes.com/podcasts/microscope-nY4ts9XwUgq-4_wlYLr-pEa.1400x1400.jpg",
          "title": "Microscope",
          "publisher": "Plosive",
          "thumbnail": "https://production.listennotes.com/podcasts/microscope-0-uH6DX1sch-4_wlYLr-pEa.300x300.jpg",
          "listen_score": 39,
          "listennotes_url": "https://www.listennotes.com/c/10ee196a6fb248a08f57cd2c55c5f648/",
          "listen_score_global_rank": "2%"
        },
        {
          "id": "f98f0f37356e47ff9731fab0fca2ab46",
          "image": "https://production.listennotes.com/podcasts/capital-an-improvised-comedy-about-sczVBvAWHOE.1400x1400.jpg",
          "title": "Capital",
          "publisher": "An improvised comedy about executing an execution.",
          "thumbnail": "https://production.listennotes.com/podcasts/capital-an-improvised-comedy-about-sczVBvAWHOE.300x300.jpg",
          "listen_score": 56,
          "listennotes_url": "https://www.listennotes.com/c/f98f0f37356e47ff9731fab0fca2ab46/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "b22e21db22764ba3a65120b34a044d5f",
          "image": "https://production.listennotes.com/podcasts/sound-heap-Zd8XaNmKopJ-8a3q6zxfBQI.1400x1400.jpg",
          "title": "Sound Heap",
          "publisher": "Auddy",
          "thumbnail": "https://production.listennotes.com/podcasts/sound-heap-MFzGyHL6mgr-8a3q6zxfBQI.300x300.jpg",
          "listen_score": 36,
          "listennotes_url": "https://www.listennotes.com/c/b22e21db22764ba3a65120b34a044d5f/",
          "listen_score_global_rank": "3%"
        }
      ],
      "source_url": "https://www.theguardian.com/tv-and-radio/2021/sep/28/five-of-the-best-podcasts-laugh-out-loud-fictional-comedies?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"From the world\u2019s rudest agony aunts to pirate radio DJs and mock-celeb chat, if it\u2019s comedy you\u2019re after, there\u2019s a podcast for that.\"",
      "pub_date_ms": 1632892161490,
      "source_domain": "www.theguardian.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/five-of-the-best-podcasts-laugh-out-Nu_GgVazPDJ/"
    },
    {
      "id": "obpZVyEufxD",
      "title": "This is the best true-crime podcast, according to Boston.com readers",
      "total": 12,
      "podcasts": [
        {
          "id": "25ba0ee509544677acbcda769745963e",
          "image": "https://production.listennotes.com/podcasts/wine-crime-wine-crime-podcast-q0Z7SHhP4N_-WMgqCDGRI8s.1400x1400.jpg",
          "title": "Wine & Crime",
          "publisher": "Wine & Crime Podcast",
          "thumbnail": "https://production.listennotes.com/podcasts/wine-crime-wine-crime-podcast-1Y5_-DZQqiV-WMgqCDGRI8s.300x300.jpg",
          "listen_score": 76,
          "listennotes_url": "https://www.listennotes.com/c/25ba0ee509544677acbcda769745963e/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "873414cf0efe4efebb20f467aa0f28b2",
          "image": "https://production.listennotes.com/podcasts/my-favorite-murder-with-karen-kilgariff-and-9Z3Xvpts8AR-nUHfdZot1PQ.1400x1400.jpg",
          "title": "My Favorite Murder with Karen Kilgariff and Georgia Hardstark",
          "publisher": "Exactly Right",
          "thumbnail": "https://production.listennotes.com/podcasts/my-favorite-murder-with-karen-kilgariff-and-SDOFYaQWsIb-nUHfdZot1PQ.300x300.jpg",
          "listen_score": 95,
          "listennotes_url": "https://www.listennotes.com/c/873414cf0efe4efebb20f467aa0f28b2/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "08e7e64e80ac456a8ce0027f07dc40d0",
          "image": "https://production.listennotes.com/podcasts/morbid-a-true-crime-podcast-morbid-a-true-owJCuTLqdkf-krRXUPe1dbC.1400x1400.jpg",
          "title": "Morbid: A True Crime Podcast",
          "publisher": "Morbid: A True Crime Podcast",
          "thumbnail": "https://production.listennotes.com/podcasts/morbid-a-true-crime-podcast-morbid-a-true-Jc0iPX8x5KS-krRXUPe1dbC.300x300.jpg",
          "listen_score": 84,
          "listennotes_url": "https://www.listennotes.com/c/08e7e64e80ac456a8ce0027f07dc40d0/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "44d2110a792b4e2b85f2303abaef75e9",
          "image": "https://production.listennotes.com/podcasts/crime-junkie-audiochuck-NRFDTn54WYh-BWDcryRL6xl.1400x1400.jpg",
          "title": "Crime Junkie",
          "publisher": "audiochuck",
          "thumbnail": "https://production.listennotes.com/podcasts/crime-junkie-audiochuck-5yH6plhgjR2-BWDcryRL6xl.300x300.jpg",
          "listen_score": 98,
          "listennotes_url": "https://www.listennotes.com/c/44d2110a792b4e2b85f2303abaef75e9/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "b9865c83d0a44c16b125e90c152470dc",
          "image": "https://production.listennotes.com/podcasts/anatomy-of-murder-audiochuck-Rp64qNMI71F-JKw-WyF3BnM.1400x1400.jpg",
          "title": "Anatomy of Murder",
          "publisher": "audiochuck",
          "thumbnail": "https://production.listennotes.com/podcasts/anatomy-of-murder-audiochuck-ihrB1CEPYjd-JKw-WyF3BnM.300x300.jpg",
          "listen_score": 74,
          "listennotes_url": "https://www.listennotes.com/c/b9865c83d0a44c16b125e90c152470dc/",
          "listen_score_global_rank": "0.05%"
        }
      ],
      "source_url": "https://www.boston.com/culture/community/2021/09/28/readers-vote-best-true-crime-podcast/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "'\"Smart, funny women getting drunk and talking true crime.\u201d'",
      "pub_date_ms": 1632891377027,
      "source_domain": "www.boston.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/this-is-the-best-true-crime-podcast-obpZVyEufxD/"
    },
    {
      "id": "IOhyKYv1ATk",
      "title": "The Best True Crime Podcasts",
      "total": 9,
      "podcasts": [
        {
          "id": "e62745c909384ff3b70616e9746a6158",
          "image": "https://production.listennotes.com/podcasts/suspect-1qVUJ3hKQuN-LilRr6M_Np1.1400x1400.jpg",
          "title": "Suspect",
          "publisher": "Wondery | Campside",
          "thumbnail": "https://production.listennotes.com/podcasts/suspect-WvUAoCw8H3c-LilRr6M_Np1.300x300.jpg",
          "listen_score": 58,
          "listennotes_url": "https://www.listennotes.com/c/e62745c909384ff3b70616e9746a6158/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "b426b492c1d4458b86012f95131e01e4",
          "image": "https://production.listennotes.com/podcasts/gangster-capitalism-c13originals-cZPmAqyloKp-etZ0EfNABP8.1400x1400.jpg",
          "title": "Gangster Capitalism",
          "publisher": "C13Originals",
          "thumbnail": "https://production.listennotes.com/podcasts/gangster-capitalism-c13originals-4R6u8UtD5Kx-etZ0EfNABP8.300x300.jpg",
          "listen_score": 67,
          "listennotes_url": "https://www.listennotes.com/c/b426b492c1d4458b86012f95131e01e4/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "9966922dce8f41f89af294f2354f07a6",
          "image": "https://production.listennotes.com/podcasts/dr-death-season-3-miracle-man-l2TibAZh4-m-QEw_vsYlRPN.1400x1400.jpg",
          "title": "Dr. Death | S3: Miracle Man",
          "publisher": "Wondery",
          "thumbnail": "https://production.listennotes.com/podcasts/dr-death-season-3-miracle-man-UnPdkE6GJHB-QEw_vsYlRPN.300x300.jpg",
          "listen_score": 66,
          "listennotes_url": "https://www.listennotes.com/c/9966922dce8f41f89af294f2354f07a6/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "8063db4878224449b0588bfb0a22ba5f",
          "image": "https://production.listennotes.com/podcasts/bad-blood-the-final-chapter-p2nXWTEZGtr-vMTrJ6L2Bic.1400x1400.jpg",
          "title": "Bad Blood: The Final Chapter",
          "publisher": "Three Uncanny Four",
          "thumbnail": "https://production.listennotes.com/podcasts/bad-blood-the-final-chapter-kzne2mZ-4_K-vMTrJ6L2Bic.300x300.jpg",
          "listen_score": 61,
          "listennotes_url": "https://www.listennotes.com/c/8063db4878224449b0588bfb0a22ba5f/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "ce8a8a1439c54b07bcaf49cf6640cf7a",
          "image": "https://production.listennotes.com/podcasts/up-against-the-mob-MlkA1Rq90zg-uk_HTAI9yDq.1400x1400.jpg",
          "title": "Up Against The Mob",
          "publisher": "CAFE",
          "thumbnail": "https://production.listennotes.com/podcasts/up-against-the-mob-r2pmksKAX0w-uk_HTAI9yDq.300x300.jpg",
          "listen_score": 49,
          "listennotes_url": "https://www.listennotes.com/c/ce8a8a1439c54b07bcaf49cf6640cf7a/",
          "listen_score_global_rank": "1%"
        }
      ],
      "source_url": "https://www.pastemagazine.com/media/podcasts/the-best-true-crime-podcasts/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"More than just guilty pleasures, true crime podcasts can reveal both the worst and the best humanity has to offer, inspiring us to speak out for truth or find redemption in helping others. Here are some of the best recent true-crime podcasts for your next listening binge.\"",
      "pub_date_ms": 1632890570130,
      "source_domain": "www.pastemagazine.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/the-best-true-crime-podcasts-IOhyKYv1ATk/"
    },
    {
      "id": "LOuIz-y8DAq",
      "title": "10 Podcasts to Help with Depression",
      "total": 10,
      "podcasts": [
        {
          "id": "f9f6bd3c0020485ab135b7e5e7dd97c3",
          "image": "https://production.listennotes.com/podcasts/the-selfwork-podcast-margaret-robinson-f2BEzVACbHo-oC7waQM3dvi.1400x1400.jpg",
          "title": "The SelfWork Podcast",
          "publisher": "Margaret Robinson Rutherford PhD",
          "thumbnail": "https://production.listennotes.com/podcasts/the-selfwork-podcast-margaret-robinson-rAxuKVkRoJq-oC7waQM3dvi.300x300.jpg",
          "listen_score": 59,
          "listennotes_url": "https://www.listennotes.com/c/f9f6bd3c0020485ab135b7e5e7dd97c3/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "795d876d4f114f368630aec49aab03a0",
          "image": "https://production.listennotes.com/podcasts/on-purpose-with-jay-shetty-jay-shetty-nEIGu8q3vaV-gnyHELJ0usD.1400x1400.jpg",
          "title": "On Purpose with Jay Shetty",
          "publisher": "Jay Shetty",
          "thumbnail": "https://production.listennotes.com/podcasts/on-purpose-with-jay-shetty-jay-shetty-GtygfvBH9Km-gnyHELJ0usD.300x300.jpg",
          "listen_score": 82,
          "listennotes_url": "https://www.listennotes.com/c/795d876d4f114f368630aec49aab03a0/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "9477e109d17b40188088aa7e4d35e8a9",
          "image": "https://production.listennotes.com/podcasts/owning-it-the-anxiety-podcast-caroline-foran-dL9usnrNKic.1400x1400.jpg",
          "title": "Owning It: The Anxiety Podcast",
          "publisher": "Caroline Foran",
          "thumbnail": "https://production.listennotes.com/podcasts/owning-it-the-anxiety-podcast-caroline-foran-dL9usnrNKic.300x300.jpg",
          "listen_score": 54,
          "listennotes_url": "https://www.listennotes.com/c/9477e109d17b40188088aa7e4d35e8a9/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "0aa41a23b40e4306be2f798d62ecec14",
          "image": "https://production.listennotes.com/podcasts/the-hilarious-world-of-depression-american-CWb62Vdx8Il.1400x1400.jpg",
          "title": "The Hilarious World of Depression",
          "publisher": "American Public Media",
          "thumbnail": "https://production.listennotes.com/podcasts/the-hilarious-world-of-depression-american-CWb62Vdx8Il.300x300.jpg",
          "listen_score": 70,
          "listennotes_url": "https://www.listennotes.com/c/0aa41a23b40e4306be2f798d62ecec14/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "b16a7d807ccb434184d866c2ffb2084e",
          "image": "https://production.listennotes.com/podcasts/feeling-good-podcast-team-cbt-the-new-mood-PzemW-CsO_4-J19oweM6jk0.1400x1400.jpg",
          "title": "Feeling Good Podcast | TEAM-CBT - The New Mood Therapy",
          "publisher": "David Burns, MD",
          "thumbnail": "https://production.listennotes.com/podcasts/feeling-good-podcast-team-cbt-the-new-mood-6vE7q8PlGJk-J19oweM6jk0.300x300.jpg",
          "listen_score": 56,
          "listennotes_url": "https://www.listennotes.com/c/b16a7d807ccb434184d866c2ffb2084e/",
          "listen_score_global_rank": "0.5%"
        }
      ],
      "source_url": "https://www.healthline.com/health/mental-health/depression-podcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"Although self-help podcasts are not a substitute for professional help, they can be a very helpful tool to use alongside seeing someone regularly. If you think you might have depression, please make sure to consult a mental health professional.\"",
      "pub_date_ms": 1632890429616,
      "source_domain": "www.healthline.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/10-podcasts-to-help-with-depression-LOuIz-y8DAq/"
    },
    {
      "id": "zUxQiaRn8eB",
      "title": "The best technology and innovation podcasts in Spanish",
      "total": 10,
      "podcasts": [
        {
          "id": "3bb8ae230a29400eac9cea19b3b93059",
          "image": "https://production.listennotes.com/podcasts/mixxio-podcast-diario-de-tecnolog\u00eda-\u00e1lex-xDwqocEjbi9-aOEWo5wSl-K.1400x1400.jpg",
          "title": "mixxio \u2014 podcast diario de tecnolog\u00eda",
          "publisher": "\u00c1lex Barredo",
          "thumbnail": "https://production.listennotes.com/podcasts/mixxio-podcast-diario-de-tecnolog\u00eda-\u00e1lex-oM71sI6bJKG-aOEWo5wSl-K.300x300.jpg",
          "listen_score": 54,
          "listennotes_url": "https://www.listennotes.com/c/3bb8ae230a29400eac9cea19b3b93059/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "0085ec8c83d1418882d2f469ed4ccb63",
          "image": "https://production.listennotes.com/podcasts/despeja-la-x-by-xataka-xataka-kQ6Nsph5Ud7-CchIrHT_yoX.1400x1400.jpg",
          "title": "Despeja la X (by Xataka)",
          "publisher": "Xataka",
          "thumbnail": "https://production.listennotes.com/podcasts/despeja-la-x-by-xataka-xataka-vgPCqaT-Aot-CchIrHT_yoX.300x300.jpg",
          "listen_score": 33,
          "listennotes_url": "https://www.listennotes.com/c/0085ec8c83d1418882d2f469ed4ccb63/",
          "listen_score_global_rank": "5%"
        },
        {
          "id": "b43482c145a6424db7fd61ad9557d676",
          "image": "https://production.listennotes.com/podcasts/archives-futures-_gYRmDlTvbS-5Gds43iRuCW.1400x1400.jpg",
          "title": "Archives + Futures",
          "publisher": "Ivan LOZANO",
          "thumbnail": "https://production.listennotes.com/podcasts/archives-futures-djiSW1hCo4y-5Gds43iRuCW.300x300.jpg",
          "listen_score": null,
          "listennotes_url": "https://www.listennotes.com/c/b43482c145a6424db7fd61ad9557d676/",
          "listen_score_global_rank": null
        },
        {
          "id": "3932593c8c9f485a8c397ed36c0b8993",
          "image": "https://production.listennotes.com/podcasts/aurospace-podcast-edrick-uribe-_M1twR2D5JZ-KYEkebP6GZ-.1400x1400.jpg",
          "title": "Aurospace Podcast",
          "publisher": "Edrick Uribe",
          "thumbnail": "https://production.listennotes.com/podcasts/aurospace-podcast-edrick-uribe-LZOpJGYPTMo-KYEkebP6GZ-.300x300.jpg",
          "listen_score": null,
          "listennotes_url": "https://www.listennotes.com/c/3932593c8c9f485a8c397ed36c0b8993/",
          "listen_score_global_rank": null
        },
        {
          "id": "cf122fcf65a2474988d3e0eef8351f69",
          "image": "https://production.listennotes.com/podcasts/gran-invento-con-chris-becerra-chris-ANDWXu-YUkS-gWkvB5TyUoI.1400x1400.jpg",
          "title": "Gran Invento \ud83d\udca1con Chris Becerra",
          "publisher": "Chris Becerra Piquinotti",
          "thumbnail": "https://production.listennotes.com/podcasts/gran-invento-con-chris-becerra-chris-NakwpyHMgSX-gWkvB5TyUoI.300x300.jpg",
          "listen_score": null,
          "listennotes_url": "https://www.listennotes.com/c/cf122fcf65a2474988d3e0eef8351f69/",
          "listen_score_global_rank": null
        }
      ],
      "source_url": "https://www.entrepreneur.com/article/387839?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"So, if you are passionate about science, or you simply like to keep up to date with the latest news, this time I am going to share the best technology and innovation podcasts in Spanish . With each of them you will learn a lot, and they will inspire you to exploit your capabilities and your most creative side for innovation.\"",
      "pub_date_ms": 1632890354026,
      "source_domain": "www.entrepreneur.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/the-best-technology-and-innovation-zUxQiaRn8eB/"
    },
    {
      "id": "8er3C0wGDjW",
      "title": "The Podcasts Opera Pros Tune To",
      "total": 20,
      "podcasts": [
        {
          "id": "6dcf95419c2a4a8e927d213a8ee821f8",
          "image": "https://production.listennotes.com/podcasts/aria-code-wqxr-the-metropolitan-opera-b6iTY75vaJe-eSEgM9KnlVG.1400x1400.jpg",
          "title": "Aria Code",
          "publisher": "WQXR & The Metropolitan Opera ",
          "thumbnail": "https://production.listennotes.com/podcasts/aria-code-wqxr-the-metropolitan-opera-8NeKnPTv0cE-eSEgM9KnlVG.300x300.jpg",
          "listen_score": 64,
          "listennotes_url": "https://www.listennotes.com/c/6dcf95419c2a4a8e927d213a8ee821f8/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "f9b5a0aec14a46dcb7f65990442dc755",
          "image": "https://production.listennotes.com/podcasts/north-stage-door-san-francisco-opera-s47GBKAMFHR-quRv7iLs_eh.1400x1400.jpg",
          "title": "North Stage Door",
          "publisher": "San Francisco Opera",
          "thumbnail": "https://production.listennotes.com/podcasts/north-stage-door-san-francisco-opera-4aBVKHEWsuj-quRv7iLs_eh.300x300.jpg",
          "listen_score": 24,
          "listennotes_url": "https://www.listennotes.com/c/f9b5a0aec14a46dcb7f65990442dc755/",
          "listen_score_global_rank": "10%"
        },
        {
          "id": "e31415a7fb794faea9697163a39926a7",
          "image": "https://production.listennotes.com/podcasts/the-met-in-focus-the-metropolitan-opera-r4BpDX3OqfM.1400x1400.jpg",
          "title": "The Met: In Focus",
          "publisher": "The Metropolitan Opera",
          "thumbnail": "https://production.listennotes.com/podcasts/the-met-in-focus-the-metropolitan-opera-r4BpDX3OqfM.300x300.jpg",
          "listen_score": 42,
          "listennotes_url": "https://www.listennotes.com/c/e31415a7fb794faea9697163a39926a7/",
          "listen_score_global_rank": "1.5%"
        },
        {
          "id": "6c2af68f6c354b6b901cb6bff846b9ef",
          "image": "https://production.listennotes.com/podcasts/soul-music-bbc-radio-4-CikSh7F93NT.1400x1400.jpg",
          "title": "Soul Music",
          "publisher": "BBC Radio 4",
          "thumbnail": "https://production.listennotes.com/podcasts/soul-music-bbc-radio-4-CikSh7F93NT.300x300.jpg",
          "listen_score": 57,
          "listennotes_url": "https://www.listennotes.com/c/6c2af68f6c354b6b901cb6bff846b9ef/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "f3c1470428ce4cafa8c2a8f2b4ad8be0",
          "image": "https://production.listennotes.com/podcasts/this-classical-life-bbc-radio-3-nXjYUib3hCa-ydtG340ZUHP.1400x1400.jpg",
          "title": "This Classical Life",
          "publisher": "BBC Radio 3",
          "thumbnail": "https://production.listennotes.com/podcasts/this-classical-life-bbc-radio-3-KpG-ykTHVdc-ydtG340ZUHP.300x300.jpg",
          "listen_score": 43,
          "listennotes_url": "https://www.listennotes.com/c/f3c1470428ce4cafa8c2a8f2b4ad8be0/",
          "listen_score_global_rank": "1.5%"
        }
      ],
      "source_url": "https://www.nytimes.com/2021/09/25/arts/music/podcasts-opera-pros-tune-to.html?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "'\u201cAria Code\u201d is an increasingly popular podcast. But what else do opera professionals listen to? Here are some recommendations.'",
      "pub_date_ms": 1632616271535,
      "source_domain": "www.nytimes.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/the-podcasts-opera-pros-tune-to-8er3C0wGDjW/"
    },
    {
      "id": "c1qiIkjsLFZ",
      "title": "The 15 Best Meditation Podcasts of 2021",
      "total": 15,
      "podcasts": [
        {
          "id": "eeed8f359d5344b7aa421d174a1c4481",
          "image": "https://production.listennotes.com/podcasts/natural-meditation-podcast-stephan-pende-V9r7R20t1Dl-cSjK7bZzRF8.1400x1050.jpg",
          "title": "Natural Meditation podcast",
          "publisher": "Stephan Pende Wormland",
          "thumbnail": "https://production.listennotes.com/podcasts/natural-meditation-podcast-stephan-pende-BIeqQ_RSzm3-cSjK7bZzRF8.300x225.jpg",
          "listen_score": 34,
          "listennotes_url": "https://www.listennotes.com/c/eeed8f359d5344b7aa421d174a1c4481/",
          "listen_score_global_rank": "5%"
        },
        {
          "id": "0b90084973dd40afbe26841ce87de3f8",
          "image": "https://production.listennotes.com/podcasts/meditation-minis-podcast-meditation-minis-1Lo56mdkGIA-8iYFA4Tcas6.1400x1400.jpg",
          "title": "Meditation Minis Podcast",
          "publisher": "Meditation Minis Podcast",
          "thumbnail": "https://production.listennotes.com/podcasts/meditation-minis-podcast-meditation-minis-oD9JH2-VLpM-8iYFA4Tcas6.300x300.jpg",
          "listen_score": 69,
          "listennotes_url": "https://www.listennotes.com/c/0b90084973dd40afbe26841ce87de3f8/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "327fe219dedd4b1d87207a8b3bfbec65",
          "image": "https://production.listennotes.com/podcasts/tara-brach-tara-brach-Un1vfpKxBm4-n8rbXotsLFv.1400x1400.jpg",
          "title": "Tara Brach",
          "publisher": "Tara Brach",
          "thumbnail": "https://production.listennotes.com/podcasts/tara-brach-tara-brach-kvpKY5PjoSi-n8rbXotsLFv.300x300.jpg",
          "listen_score": 76,
          "listennotes_url": "https://www.listennotes.com/c/327fe219dedd4b1d87207a8b3bfbec65/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "464433fd3bbe44febc4f7a0fe896316c",
          "image": "https://production.listennotes.com/podcasts/ten-percent-happier-with-dan-harris-ten-UdtGi5Cwg_z-OoJzEl98cRU.1400x1400.jpg",
          "title": "Ten Percent Happier with Dan Harris",
          "publisher": "Ten Percent Happier",
          "thumbnail": "https://production.listennotes.com/podcasts/ten-percent-happier-with-dan-harris-ten-p_41FwAO6ag-OoJzEl98cRU.300x300.jpg",
          "listen_score": 76,
          "listennotes_url": "https://www.listennotes.com/c/464433fd3bbe44febc4f7a0fe896316c/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "f08da0b5713a42e8b0a0afd232cb1554",
          "image": "https://production.listennotes.com/podcasts/the-mindful-minute-meryl-arnett-pnd7Tw5Glh_-VQhqNEHXsDb.1400x1400.jpg",
          "title": "The Mindful Minute",
          "publisher": "Meryl Arnett",
          "thumbnail": "https://production.listennotes.com/podcasts/the-mindful-minute-meryl-arnett-UA_bcY8NBKT-VQhqNEHXsDb.300x300.jpg",
          "listen_score": 47,
          "listennotes_url": "https://www.listennotes.com/c/f08da0b5713a42e8b0a0afd232cb1554/",
          "listen_score_global_rank": "1%"
        }
      ],
      "source_url": "https://www.healthline.com/health/mental-health/best-meditation-podcasts?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"There are a variety of meditation podcasts out there that can help inform and enlighten you on the practice.\"",
      "pub_date_ms": 1632615895552,
      "source_domain": "www.healthline.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/the-15-best-meditation-podcasts-of-2021-c1qiIkjsLFZ/"
    },
    {
      "id": "VUBHje2gIY7",
      "title": "Top Podcasts for Women Interested in the Outdoors",
      "total": 5,
      "podcasts": [
        {
          "id": "eb5fc37b4f6949318f13f05016784fff",
          "image": "https://production.listennotes.com/podcasts/she-explores-ravel-media-J4jkZbpthLV-17DuRzUJrmh.1400x1400.jpg",
          "title": "She Explores",
          "publisher": "Ravel Media",
          "thumbnail": "https://production.listennotes.com/podcasts/she-explores-ravel-media-kINRhFA8Q_1-17DuRzUJrmh.300x300.jpg",
          "listen_score": 60,
          "listennotes_url": "https://www.listennotes.com/c/eb5fc37b4f6949318f13f05016784fff/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "c26bf7ebef47411d93772db1a67c9240",
          "image": "https://production.listennotes.com/podcasts/tough-girl-podcast-sarah-williams-QHMulgn1GPJ-pbj1d-9P0Jt.1400x1400.jpg",
          "title": "Tough Girl Podcast",
          "publisher": "Sarah Williams",
          "thumbnail": "https://production.listennotes.com/podcasts/tough-girl-podcast-sarah-williams-hK1juxvH3zQ-pbj1d-9P0Jt.300x300.jpg",
          "listen_score": 45,
          "listennotes_url": "https://www.listennotes.com/c/c26bf7ebef47411d93772db1a67c9240/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "e20cac0d0be8449592c86f86dd940594",
          "image": "https://production.listennotes.com/podcasts/outside-podcast-outside-podcast-WJt6V054EqP.1400x1400.jpg",
          "title": "Outside Podcast",
          "publisher": "Outside Podcast",
          "thumbnail": "https://production.listennotes.com/podcasts/outside-podcast-outside-podcast-WJt6V054EqP.300x300.jpg",
          "listen_score": 63,
          "listennotes_url": "https://www.listennotes.com/c/e20cac0d0be8449592c86f86dd940594/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "5555bb00695a4207a7629aa0dcf3f7dd",
          "image": "https://production.listennotes.com/podcasts/the-dirtbag-diaries-duct-tape-then-beer-Tgi2V3yYU_N-0qD-daWIxYn.1400x1400.jpg",
          "title": "The Dirtbag Diaries",
          "publisher": "Duct Tape Then Beer",
          "thumbnail": "https://production.listennotes.com/podcasts/the-dirtbag-diaries-duct-tape-then-beer-cdVK3ZTzFyO-0qD-daWIxYn.300x300.jpg",
          "listen_score": 66,
          "listennotes_url": "https://www.listennotes.com/c/5555bb00695a4207a7629aa0dcf3f7dd/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "d219cbc2fed14e0f8a9c8ce4af97016f",
          "image": "https://production.listennotes.com/podcasts/anchored-with-april-vokey-anchored-outdoors-rXy2ZkPSlNJ-vChzSktpYAI.480x480.jpg",
          "title": "Anchored with April Vokey",
          "publisher": "April Vokey",
          "thumbnail": "https://production.listennotes.com/podcasts/anchored-with-april-vokey-anchored-outdoors-bXJMqILB091-vChzSktpYAI.300x300.jpg",
          "listen_score": 60,
          "listennotes_url": "https://www.listennotes.com/c/d219cbc2fed14e0f8a9c8ce4af97016f/",
          "listen_score_global_rank": "0.5%"
        }
      ],
      "source_url": "https://www.wideopenspaces.com/outdoor-podcasts-for-women/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"With every novice picking up a mic and claiming to be an expert, it's tough to sift through all the wannabe podcasts and find one that's truly informative, interesting, and worth your time. But these five picks are some of the best outdoor podcasts out there for women who love the wild.\"",
      "pub_date_ms": 1632615716937,
      "source_domain": "www.wideopenspaces.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/top-podcasts-for-women-interested-in-VUBHje2gIY7/"
    },
    {
      "id": "CNzI_3uZdRD",
      "title": "Best self-help podcasts to listen to now",
      "total": 10,
      "podcasts": [
        {
          "id": "9a08629f7a8f4251a56c0c41f8f8a92a",
          "image": "https://production.listennotes.com/podcasts/happier-with-gretchen-rubin-gretchen-rubin-aGPeTKFY-MS-NBPDw-ZbzAC.1400x1400.jpg",
          "title": "Happier with Gretchen Rubin",
          "publisher": "Gretchen Rubin / The Onward Project",
          "thumbnail": "https://production.listennotes.com/podcasts/happier-with-gretchen-rubin-gretchen-rubin-GUPlNH0t7no-NBPDw-ZbzAC.300x300.jpg",
          "listen_score": 79,
          "listennotes_url": "https://www.listennotes.com/c/9a08629f7a8f4251a56c0c41f8f8a92a/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "3af4d2a1f88d461592f6b6e4cfcab721",
          "image": "https://production.listennotes.com/podcasts/optimal-living-daily-personal-development-JLehEXybiKO-0X_sCuTiJfB.1400x1400.jpg",
          "title": "Optimal Living Daily: Personal Development & Minimalism",
          "publisher": "Justin Malik | Optimal Living Daily",
          "thumbnail": "https://production.listennotes.com/podcasts/optimal-living-daily-personal-development-j1V_ptmEr3l-0X_sCuTiJfB.300x300.jpg",
          "listen_score": 68,
          "listennotes_url": "https://www.listennotes.com/c/3af4d2a1f88d461592f6b6e4cfcab721/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "9dc9fdd724c24ac4a497788b19064f1e",
          "image": "https://production.listennotes.com/podcasts/unlocking-us-with-bren\u00e9-brown-parcast-network-w4qKzY5OpyB-3BLhH_1OXfZ.1400x1400.jpg",
          "title": "Unlocking Us with Bren\u00e9 Brown",
          "publisher": "Parcast Network",
          "thumbnail": "https://production.listennotes.com/podcasts/unlocking-us-with-bren\u00e9-brown-parcast-network-e-UfCqLn2yi-3BLhH_1OXfZ.300x300.jpg",
          "listen_score": 81,
          "listennotes_url": "https://www.listennotes.com/c/9dc9fdd724c24ac4a497788b19064f1e/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "78574497404347fc874d1744b69ce6d6",
          "image": "https://production.listennotes.com/podcasts/the-one-you-feed-eric-zimmer-fAsW_HKvMn6-bzpAeNxUqf3.1400x1400.jpg",
          "title": "The One You Feed",
          "publisher": "Eric Zimmer|Wondery ",
          "thumbnail": "https://production.listennotes.com/podcasts/the-one-you-feed-eric-zimmer-koFcVhnazUv-bzpAeNxUqf3.300x300.jpg",
          "listen_score": 66,
          "listennotes_url": "https://www.listennotes.com/c/78574497404347fc874d1744b69ce6d6/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "fc6d33e22b7f4db38df3bb64a9a8c227",
          "image": "https://production.listennotes.com/podcasts/the-tony-robbins-podcast-tony-robbins-eh9wNFJcP1W.1400x1400.jpg",
          "title": "The Tony Robbins Podcast",
          "publisher": "Tony Robbins",
          "thumbnail": "https://production.listennotes.com/podcasts/the-tony-robbins-podcast-tony-robbins-eh9wNFJcP1W.300x300.jpg",
          "listen_score": 74,
          "listennotes_url": "https://www.listennotes.com/c/fc6d33e22b7f4db38df3bb64a9a8c227/",
          "listen_score_global_rank": "0.05%"
        }
      ],
      "source_url": "https://theoklahoma100.com/lifestyle/living-wellness/2021/09/21/best-self-help-podcasts-to-listen-to-now/18098?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"With September being National Self-Improvement Month and Podcast Day hitting on Sept. 30, it\u2019s the perfect time to focus on YOU and indulge in a little self-help therapy with these top 10 self-help podcasts.\"",
      "pub_date_ms": 1632615600486,
      "source_domain": "theoklahoma100.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/best-self-help-podcasts-to-listen-to-now-CNzI_3uZdRD/"
    },
    {
      "id": "jntERKsu6YU",
      "title": "10 Mental Health Podcasts That Will Help You Feel Seen (and Teach You Something, Too)",
      "total": 10,
      "podcasts": [
        {
          "id": "1997df5fa44846ec93ebe96676ca9b44",
          "image": "https://production.listennotes.com/podcasts/unfck-your-brain-kara-loewentheil-FqR_JpIlUHW-1RcasTFpNBu.1400x1400.jpg",
          "title": "UnF*ck Your Brain",
          "publisher": "Kara Loewentheil",
          "thumbnail": "https://production.listennotes.com/podcasts/unfck-your-brain-kara-loewentheil-0xredGP3vsc-1RcasTFpNBu.300x300.jpg",
          "listen_score": 70,
          "listennotes_url": "https://www.listennotes.com/c/1997df5fa44846ec93ebe96676ca9b44/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "6d01c4e63c5349099ea5c6e617c646e6",
          "image": "https://production.listennotes.com/podcasts/therapy-for-black-girls-joy-harden-bradford-f0RMwG6g3Qt-Jw_CUaBj1GI.1400x1400.jpg",
          "title": "Therapy for Black Girls",
          "publisher": "Joy Harden Bradford, Ph.D. and iHeartRadio",
          "thumbnail": "https://production.listennotes.com/podcasts/therapy-for-black-girls-joy-harden-bradford-uMQl_Zbai8z-Jw_CUaBj1GI.300x300.jpg",
          "listen_score": 70,
          "listennotes_url": "https://www.listennotes.com/c/6d01c4e63c5349099ea5c6e617c646e6/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "6b8c4e1b888c4c94a795c75b76707c3f",
          "image": "https://production.listennotes.com/podcasts/cleaning-up-the-mental-mess-with-dr-mvstdpuGzH0-rE42WDNG-gq.1400x1400.jpg",
          "title": "CLEANING UP THE MENTAL MESS with Dr. Caroline Leaf",
          "publisher": "Dr. Caroline Leaf",
          "thumbnail": "https://production.listennotes.com/podcasts/cleaning-up-the-mental-mess-with-dr-NX4nCDgdzrW-rE42WDNG-gq.300x300.jpg",
          "listen_score": 66,
          "listennotes_url": "https://www.listennotes.com/c/6b8c4e1b888c4c94a795c75b76707c3f/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "9f4afed37cfe4e1c8caaebf884e024be",
          "image": "https://production.listennotes.com/podcasts/anxiety-slayertm-with-shann-and-ananga-jD7YuGVz40K-91f8OKs-Hhw.1400x1400.jpg",
          "title": "Anxiety Slayer\u2122 with Shann and Ananga",
          "publisher": "Shann Vander Leek & Ananga Sivyer",
          "thumbnail": "https://production.listennotes.com/podcasts/anxiety-slayertm-with-shann-and-ananga-yu-0vrgcA54-91f8OKs-Hhw.300x300.jpg",
          "listen_score": 57,
          "listennotes_url": "https://www.listennotes.com/c/9f4afed37cfe4e1c8caaebf884e024be/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "6e05ef7396944ae1ae553b8d3ac90c6b",
          "image": "https://production.listennotes.com/podcasts/inside-mental-health-a-psych-central-bYr2TjCBiPs-dg-z4f8S5_C.1400x1400.jpg",
          "title": "Inside Mental Health: A Psych Central Podcast",
          "publisher": "Healthline Media",
          "thumbnail": "https://production.listennotes.com/podcasts/inside-mental-health-a-psych-central-j2q-KwUIGyF-dg-z4f8S5_C.300x300.jpg",
          "listen_score": 54,
          "listennotes_url": "https://www.listennotes.com/c/6e05ef7396944ae1ae553b8d3ac90c6b/",
          "listen_score_global_rank": "0.5%"
        }
      ],
      "source_url": "https://www.popsugar.com/fitness/best-mental-health-podcasts-48510801?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"These awesome podcasts feature psychologists, experts, and people who struggle with anxiety, depression, or other mental health issues, as they share insights, information, and ideas to help you live your best life. Some of them cover breathing techniques, others offer insights into why you may be feeling a certain way, and all of them are entertaining and easy to listen to, either weekly or biweekly. Check out 10 favorites in the slides ahead.\"",
      "pub_date_ms": 1632325034220,
      "source_domain": "www.popsugar.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/10-mental-health-podcasts-that-will-jntERKsu6YU/"
    },
    {
      "id": "mD_lkpYHLdS",
      "title": "Top 10 Great Podcasts That Are Worth a Listen",
      "total": 10,
      "podcasts": [
        {
          "id": "83e5d2405a42452e8e820c2cd705043c",
          "image": "https://production.listennotes.com/podcasts/the-heart-mermaid-palace-radiotopia-kaitlin-KxTJc3FqWOu-D4JkP-O2Vm0.1400x1400.jpg",
          "title": "The Heart",
          "publisher": "Mermaid Palace, Radiotopia & Kaitlin Prest",
          "thumbnail": "https://production.listennotes.com/podcasts/the-heart-mermaid-palace-radiotopia-kaitlin-sOYv950hmz_-D4JkP-O2Vm0.300x300.jpg",
          "listen_score": 66,
          "listennotes_url": "https://www.listennotes.com/c/83e5d2405a42452e8e820c2cd705043c/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "4b5959f8e497489c86b267ec235bd21d",
          "image": "https://production.listennotes.com/podcasts/the-read-loud-speakers-network-FHepldtPUns-Kp-FswfTCg3.1400x1400.jpg",
          "title": "The Read",
          "publisher": "Loud Speakers Network",
          "thumbnail": "https://production.listennotes.com/podcasts/the-read-loud-speakers-network-BeqTgutw-SW-Kp-FswfTCg3.300x300.jpg",
          "listen_score": 83,
          "listennotes_url": "https://www.listennotes.com/c/4b5959f8e497489c86b267ec235bd21d/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "77035c0ef3d24d31b7c237cf8029d705",
          "image": "https://production.listennotes.com/podcasts/sex-with-emily-dr-emily-morse-1cil3xJpNeg-Fme6uI7NoHQ.1400x1400.jpg",
          "title": "Sex With Emily",
          "publisher": "Dr. Emily Morse",
          "thumbnail": "https://production.listennotes.com/podcasts/sex-with-emily-dr-emily-morse-XRvnAM9GPEy-Fme6uI7NoHQ.300x300.jpg",
          "listen_score": 71,
          "listennotes_url": "https://www.listennotes.com/c/77035c0ef3d24d31b7c237cf8029d705/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "3c5f1fed1d5147b084d8be4f607cd4c4",
          "image": "https://production.listennotes.com/podcasts/tifo-football-podcast-the-athletic-mlpQ_hey8gw-hvrXqC8RyNJ.1400x1400.jpg",
          "title": "Tifo Football Podcast",
          "publisher": "The Athletic",
          "thumbnail": "https://production.listennotes.com/podcasts/tifo-football-podcast-the-athletic-WHadumMUqSk-hvrXqC8RyNJ.300x300.jpg",
          "listen_score": 59,
          "listennotes_url": "https://www.listennotes.com/c/3c5f1fed1d5147b084d8be4f607cd4c4/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "f2eb196b20884b0490cc60a58b05bbb6",
          "image": "https://production.listennotes.com/podcasts/the-daily-the-new-york-times-wLJZBNmd5_Y-xp7nhsmSkX2.1400x1400.jpg",
          "title": "The Daily",
          "publisher": "The New York Times",
          "thumbnail": "https://production.listennotes.com/podcasts/the-daily-the-new-york-times-lDnVGaIf7Ks-xp7nhsmSkX2.300x300.jpg",
          "listen_score": 91,
          "listennotes_url": "https://www.listennotes.com/c/f2eb196b20884b0490cc60a58b05bbb6/",
          "listen_score_global_rank": "0.01%"
        }
      ],
      "source_url": "https://oracle.newpaltz.edu/top-10-great-podcasts-that-are-worth-a-listen/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"Whether you\u2019re on the green taking in the pleasant weather or people-watching from a desk, there\u2019s nothing like the sound of folks jabbering away on a podcast that makes the day fly by or your study session go faster.\"",
      "pub_date_ms": 1632325128925,
      "source_domain": "oracle.newpaltz.edu",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/top-10-great-podcasts-that-are-worth-a-mD_lkpYHLdS/"
    },
    {
      "id": "U_2u4VHvyNm",
      "title": "The 5 Best Podcasts for Personal Finance",
      "total": 5,
      "podcasts": [
        {
          "id": "b925a2e959e14ee79b4f5294ea6f5a37",
          "image": "https://production.listennotes.com/podcasts/brown-ambition-mandi-woodruff-and-tiffany-secNJmwBkpo-f39F1YXI-8r.1400x1400.jpg",
          "title": "Brown Ambition",
          "publisher": "Mandi Woodruff & Tiffany Aliche | Cumulus Podcast Network",
          "thumbnail": "https://production.listennotes.com/podcasts/brown-ambition-mandi-woodruff-and-tiffany-nH1Z_NtfE4k-f39F1YXI-8r.300x300.jpg",
          "listen_score": 63,
          "listennotes_url": "https://www.listennotes.com/c/b925a2e959e14ee79b4f5294ea6f5a37/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "d03a0a1a00494809a77efc6f51273b9b",
          "image": "https://production.listennotes.com/podcasts/real-estate-financial-independence-podcast-3IN9E_LzGx0-cK3_FBy0Yh1.1200x1200.jpg",
          "title": "Real Estate & Financial Independence Podcast",
          "publisher": "Chad Coach Carson",
          "thumbnail": "https://production.listennotes.com/podcasts/real-estate-financial-independence-podcast-5VNBvx2hodL-cK3_FBy0Yh1.300x300.jpg",
          "listen_score": 52,
          "listennotes_url": "https://www.listennotes.com/c/d03a0a1a00494809a77efc6f51273b9b/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "61eb6cf4b84d493b8ad512e01f72e2ef",
          "image": "https://production.listennotes.com/podcasts/freakonomics-radio-freakonomics-radio-0FeHYosOrvQ-LIxRmU8oGZq.1400x1400.jpg",
          "title": "Freakonomics Radio",
          "publisher": "Freakonomics Radio + Stitcher",
          "thumbnail": "https://production.listennotes.com/podcasts/freakonomics-radio-freakonomics-radio-CGYyPl1dehH-LIxRmU8oGZq.300x300.jpg",
          "listen_score": 85,
          "listennotes_url": "https://www.listennotes.com/c/61eb6cf4b84d493b8ad512e01f72e2ef/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "3ccfee508f70416b998513bc3afabb76",
          "image": "https://production.listennotes.com/podcasts/go-out-and-live-mike-policar-fiduciary-6qf_0jSXkDs-C6VdItYlyDw.1400x1400.jpg",
          "title": "Go Out And Live!",
          "publisher": "Michael Policar - Fiduciary",
          "thumbnail": "https://production.listennotes.com/podcasts/go-out-and-live-mike-policar-fiduciary-XEbc5x3fjiw-C6VdItYlyDw.300x300.jpg",
          "listen_score": 42,
          "listennotes_url": "https://www.listennotes.com/c/3ccfee508f70416b998513bc3afabb76/",
          "listen_score_global_rank": "1.5%"
        },
        {
          "id": "0da3baee05cc47e4b3222da775573efe",
          "image": "https://production.listennotes.com/podcasts/we-study-billionaires-the-investors-podcast-6FOudx8NlcK-ZuO23m60ePb.1400x1400.jpg",
          "title": "We Study Billionaires - The Investor\u2019s Podcast Network",
          "publisher": "The Investor's Podcast Network",
          "thumbnail": "https://production.listennotes.com/podcasts/we-study-billionaires-the-investors-podcast-hDr7pRB9Ku8-ZuO23m60ePb.300x300.jpg",
          "listen_score": 70,
          "listennotes_url": "https://www.listennotes.com/c/0da3baee05cc47e4b3222da775573efe/",
          "listen_score_global_rank": "0.05%"
        }
      ],
      "source_url": "https://www.gobankingrates.com/money/financial-planning/the-5-best-podcasts-for-personal-finance/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"GOBankingRates found five personal finance podcasts that cover everything from student loan debt to real estate investing to retirement planning (and more). Hosted by experts, if you\u2019re into all things personal finance you should definitely give a listen.\"",
      "pub_date_ms": 1632325224449,
      "source_domain": "www.gobankingrates.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/the-5-best-podcasts-for-personal-finance-U_2u4VHvyNm/"
    }
  ],
  "next_page_number": 3,
  "previous_page_number": 1
}
```   
</details>



<details>
  <summary>Click to see response schema</summary>
  
```json
{
  "type": "object",
  "required": [
    "curated_lists",
    "has_next",
    "has_previous",
    "next_page_number",
    "page_number",
    "previous_page_number",
    "total"
  ],
  "properties": {
    "total": {
      "type": "integer",
      "example": 25
    },
    "has_next": {
      "type": "boolean",
      "example": true
    },
    "page_number": {
      "type": "integer",
      "example": 2
    },
    "has_previous": {
      "type": "boolean",
      "example": true
    },
    "curated_lists": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "example": "Vb017Sx3l8F",
            "description": "Curated list id."
          },
          "title": {
            "type": "string",
            "example": "7 Bookish Podcasts for Avid Readers On the Go",
            "description": "Curated list name."
          },
          "total": {
            "type": "integer",
            "example": 25,
            "description": "The total number of podcasts in this curated list."
          },
          "podcasts": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "string",
                  "example": "4d3fe717742d4963a85562e9f84d8c79",
                  "description": "Podcast id."
                },
                "image": {
                  "type": "string",
                  "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
                  "description": "Image url for this podcast's artwork. If you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
                },
                "title": {
                  "type": "string",
                  "example": "Star Wars 7x7 | Star Wars News, Interviews, and More!",
                  "description": "Podcast name."
                },
                "publisher": {
                  "type": "string",
                  "example": "Planet Broadcasting",
                  "description": "Podcast publisher name."
                },
                "thumbnail": {
                  "type": "string",
                  "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
                  "description": "Thumbnail image url for this podcast's artwork (300x300)."
                },
                "listen_score": {
                  "type": "integer",
                  "example": 81,
                  "description": "The estimated popularity score of a podcast compared to all other rss-based public podcasts in the world on a scale from 0 to 100.\nIf the score is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
                },
                "listennotes_url": {
                  "type": "string",
                  "example": "https://www.listennotes.com/c/4d3fe717742d4963a85562e9f84d8c79/",
                  "description": "The url of this podcast on [ListenNotes.com](https://www.ListenNotes.com)."
                },
                "listen_score_global_rank": {
                  "type": "string",
                  "example": "0.5%",
                  "description": "The estimated popularity ranking of a podcast compared to all other rss-based public podcasts in the world.\nFor example, if the value is 0.5%, then this podcast is one of the top 0.5% most popular shows out of all podcasts globally, ranked by Listen Score.\nIf the ranking is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
                }
              }
            },
            "description": "Minimum meta data of up to 5 podcasts in this curated list."
          },
          "source_url": {
            "type": "string",
            "example": "https://parade.com/718913/ashley_johnson/7-bookish-podcasts-for-avid-readers-on-the-go/",
            "description": "Url of the source of this curated list."
          },
          "description": {
            "type": "string",
            "example": "Commuting to work is always better when you have a great new podcast to listen to, and this year, we have discovered some of our favorite podcasts yet for readers and book-lovers. These podcasts for readers entertain us and provide no shortage of new book recommendations too.",
            "description": "This curated list's description."
          },
          "pub_date_ms": {
            "type": "integer",
            "example": 1556843484301,
            "description": "Published date of this curated list. In milliseconds."
          },
          "source_domain": {
            "type": "string",
            "example": "parade.com",
            "description": "The domain name of the source of this curated list."
          },
          "listennotes_url": {
            "type": "string",
            "example": "https://www.listennotes.com/curated-podcasts/7-bookish-podcasts-for-avid-readers-on-H2r-TCWai8K/",
            "description": "The url of this curated list on [ListenNotes.com](https://www.ListenNotes.com)."
          }
        }
      }
    },
    "next_page_number": {
      "type": "integer",
      "example": 3
    },
    "previous_page_number": {
      "type": "integer",
      "example": 1
    }
  }
}
```   
</details>




### Submit a podcast to Listen Notes database

Function Name: **submit_podcast**

Podcast hosting services can use this endpoint to help your users directly submit a new podcast to Listen Notes database. If the podcast doesn&#x27;t exist in the database, &quot;status&quot; in the response will be &quot;in review&quot;, and we&#x27;ll review it within 12 hours. If the podcast exists, &quot;status&quot; in the response will be &quot;found&quot;. You can use `POST /podcasts` to check if multiple podcasts exist in the database. If you want to get a notification once the podcast is accepted, you can either specify the &quot;email&quot; parameter or configure a webhook url in the dashboard: listennotes.com/api/dashboard/#webhooks


Example:
```python

from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)      

response = client.submit_podcast(rss='https://feeds.megaphone.fm/committed')
            
print(response.json())

```

See all available parameters on the [API Docs page](https://www.listennotes.com/api/docs/#post-api-v2-podcasts-submit).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "status": "found",
  "podcast": {
    "id": "bc9546c04f7445e48d611112ec6438ca",
    "image": "https://production.listennotes.com/podcasts/committed-iheartradio-YopuPrlDIsU-Lvh5Xq29dtK.1400x1400.jpg",
    "title": "Committed",
    "publisher": "iHeartRadio",
    "thumbnail": "https://production.listennotes.com/podcasts/committed-iheartradio-jhFwq85cm3e-Lvh5Xq29dtK.300x300.jpg",
    "listen_score": 62,
    "listennotes_url": "https://www.listennotes.com/c/bc9546c04f7445e48d611112ec6438ca/",
    "listen_score_global_rank": "0.1%"
  }
}
```   
</details>



<details>
  <summary>Click to see response schema</summary>
  
```json
{
  "type": "object",
  "required": [
    "podcast",
    "status"
  ],
  "properties": {
    "status": {
      "enum": [
        "found",
        "in review"
      ],
      "type": "string",
      "example": "found",
      "description": "The status of this submission."
    },
    "podcast": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "example": "4d3fe717742d4963a85562e9f84d8c79",
          "description": "Podcast id."
        },
        "image": {
          "type": "string",
          "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
          "description": "Image url for this podcast's artwork. If you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
        },
        "title": {
          "type": "string",
          "example": "Star Wars 7x7 | Star Wars News, Interviews, and More!",
          "description": "Podcast name."
        },
        "publisher": {
          "type": "string",
          "example": "Planet Broadcasting",
          "description": "Podcast publisher name."
        },
        "thumbnail": {
          "type": "string",
          "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
          "description": "Thumbnail image url for this podcast's artwork (300x300)."
        },
        "listen_score": {
          "type": "integer",
          "example": 81,
          "description": "The estimated popularity score of a podcast compared to all other rss-based public podcasts in the world on a scale from 0 to 100.\nIf the score is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
        },
        "listennotes_url": {
          "type": "string",
          "example": "https://www.listennotes.com/c/4d3fe717742d4963a85562e9f84d8c79/",
          "description": "The url of this podcast on [ListenNotes.com](https://www.ListenNotes.com)."
        },
        "listen_score_global_rank": {
          "type": "string",
          "example": "0.5%",
          "description": "The estimated popularity ranking of a podcast compared to all other rss-based public podcasts in the world.\nFor example, if the value is 0.5%, then this podcast is one of the top 0.5% most popular shows out of all podcasts globally, ranked by Listen Score.\nIf the ranking is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
        }
      }
    }
  }
}
```   
</details>




### Request to delete a podcast

Function Name: **delete_podcast**

Podcast hosting services can use this endpoint to streamline the process of podcast deletion on behave of their users (podcasters). We will review the deletion request within 12 hours. If the podcast is already deleted, the &quot;status&quot; field in the response will be &quot;deleted&quot;. Otherwise, the status field will be &quot;in review&quot;. If you want to get a notification once the podcast is deleted, you can configure a webhook url in the dashboard: listennotes.com/api/dashboard/#webhooks


Example:
```python

from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)      

response = client.delete_podcast(
    id='4d3fe717742d4963a85562e9f84d8c79',
    reason='Just delete it')
            
print(response.json())

```

See all available parameters on the [API Docs page](https://www.listennotes.com/api/docs/#delete-api-v2-podcasts-id).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "status": "in review"
}
```   
</details>



<details>
  <summary>Click to see response schema</summary>
  
```json
{
  "type": "object",
  "required": [
    "status"
  ],
  "properties": {
    "status": {
      "enum": [
        "deleted",
        "in review"
      ],
      "type": "string",
      "example": "deleted",
      "description": "The status of this podcast deletion request."
    }
  }
}
```   
</details>




### Fetch a playlist&#x27;s info and items (i.e., episodes or podcasts).

Function Name: **fetch_playlist_by_id**

A playlist can be an episode list (i.e., all items are episodes) or a podcast list (i.e., all items are podcasts),
which is essentially the same as those created via listennotes.com/listen/.
This endpoint fetches a list of items (i.e., episodes or podcasts) in the playlist.
You can use the **last_pub_date_ms** parameter to do pagination and fetch more items.
A playlist can be **public** (discoverable on ListenNotes.com),
**unlisted** (accessible to anyone who knows the playlist id),
or **private** (accessible to its owner).
You can fetch all playlists created by you, and **public** / **unlisted** playlists created by others.


Example:
```python

from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)      

response = client.fetch_playlist_by_id(
    id='m1pe7z60bsw', type='episode_list', sort='recent_published_first')
            
print(response.json())

```

See all available parameters on the [API Docs page](https://www.listennotes.com/api/docs/#get-api-v2-playlists-id).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "id": "m1pe7z60bsw",
  "name": "Podcasts about podcasting",
  "type": "episode_list",
  "image": "https://production.listennotes.com/playlist/image/6907e8ff6b6c45df94cc059753f369cc.JPEG",
  "items": [
    {
      "id": 678931,
      "data": {
        "id": "af19ceda98d84d3c92eafe7e7f63b6dd",
        "link": "https://tim.blog/podcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/af19ceda98d84d3c92eafe7e7f63b6dd/",
        "image": "https://production.listennotes.com/podcasts/the-tim-ferriss-show-tim-ferriss-7NwMpUz5o0S.1400x1400.jpg",
        "title": "#538: How I Built The Tim Ferriss Show to 700+ Million Downloads \u2014 An Immersive Explanation of All Aspects and Key Decisions (Featuring Chris Hutchins)",
        "podcast": {
          "id": "25212ac3c53240a880dd5032e547047b",
          "image": "https://production.listennotes.com/podcasts/the-tim-ferriss-show-tim-ferriss-7NwMpUz5o0S.1400x1400.jpg",
          "title": "The Tim Ferriss Show",
          "publisher": "Tim Ferriss: Bestselling Author, Human Guinea Pig",
          "thumbnail": "https://production.listennotes.com/podcasts/the-tim-ferriss-show-tim-ferriss-7NwMpUz5o0S.300x300.jpg",
          "listen_score": 81,
          "listennotes_url": "https://www.listennotes.com/c/25212ac3c53240a880dd5032e547047b/",
          "listen_score_global_rank": "0.01%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/the-tim-ferriss-show-tim-ferriss-7NwMpUz5o0S.300x300.jpg",
        "description": "<p><strong>How I Built The Tim Ferriss Show to 700+ Million Downloads \u2014 An Immersive Explanation of All Aspects and Key Decisions (Featuring Chris Hutchins) | Brought to you by </strong><a href=\"http://linkedin.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>LinkedIn Jobs</strong></a><strong>&nbsp;recruitment platform with 770M+ users</strong>, <a href=\"http://athleticgreens.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>Athletic Greens</strong></a><strong>&nbsp;all-in-one nutritional supplement,&nbsp;and </strong><a href=\"http://helixsleep.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>Helix Sleep</strong></a><strong>&nbsp;premium mattresses. More on all three below.</strong></p><p><strong>Chris Hutchins</strong>&nbsp;(<a href=\"https://twitter.com/hutchins\" rel=\"noopener noreferrer\" target=\"_blank\">@hutchins</a>) is an avid life hacker and financial optimizer. He\u2019s the host of&nbsp;<a href=\"https://www.allthehacks.com/\" rel=\"noopener noreferrer\" target=\"_blank\"><strong><em>All the Hacks</em></strong>&nbsp;</a>podcast and the Head of New Product Strategy at&nbsp;<a href=\"https://www.wealthfront.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\">Wealthfront</a>.</p><p>Previously, Chris was co-founder and CEO of Grove (acquired by&nbsp;<a href=\"https://www.wealthfront.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\">Wealthfront</a>), co-founder of Milk (acquired by Google), and a partner at&nbsp;<a href=\"https://www.gv.com/\" rel=\"noopener noreferrer\" target=\"_blank\">Google Ventures</a>, where he focused on seed and early stage investments.</p><p>Chris reached out with many questions about podcasting. He had already read much of&nbsp;<a href=\"https://tim.blog/2016/04/11/tim-ferriss-podcast-business/\" rel=\"noopener noreferrer\" target=\"_blank\">what I had written</a>,&nbsp;<a href=\"https://rolfpotts.com/podcast/tim-ferriss/\" rel=\"noopener noreferrer\" target=\"_blank\">listened to several interviews</a>, and this is intended to be an updated guide to all things podcasting.</p><p>Please enjoy!</p><p><strong>This episode is brought to you by&nbsp;</strong><a href=\"https://www.athleticgreens.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>Athletic Greens</strong></a><strong>.</strong>&nbsp;I get asked all the time, \u201cIf you could only use one supplement, what would it be?\u201d My answer is usually&nbsp;<a href=\"https://www.athleticgreens.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\">Athletic&nbsp;Greens</a>, my all-in-one nutritional insurance. I recommended it in&nbsp;<em>The 4-Hour Body</em>&nbsp;in 2010 and did not get paid to do so. I do my best with nutrient-dense meals, of course, but&nbsp;<a href=\"https://www.athleticgreens.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\">AG</a>&nbsp;further covers my bases with vitamins, minerals, and whole-food-sourced micronutrients that support gut health and the immune system.&nbsp;</p><p><strong>Right now,&nbsp;</strong><a href=\"https://www.athleticgreens.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>Athletic Greens</strong></a><strong>&nbsp;is offering you their Vitamin D Liquid Formula free with your first subscription purchase</strong>\u2014a vital nutrient for a strong immune system and strong bones.&nbsp;<strong>Visit&nbsp;</strong><a href=\"https://www.athleticgreens.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>AthleticGreens.com/Tim</strong></a><strong>&nbsp;to claim this special offer today and receive the free Vitamin D Liquid Formula (and five free travel packs) with your first subscription purchase!&nbsp;</strong>That\u2019s up to a one-year supply of Vitamin D as added value when you try their delicious and comprehensive all-in-one daily greens product.</p><p>*</p><p><strong>This episode is also brought to you by&nbsp;</strong><a href=\"http://helixsleep.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>Helix Sleep</strong></a><strong>!&nbsp;</strong>Helix was selected as the #1 overall mattress of 2020 by&nbsp;<em>GQ&nbsp;</em>magazine<em>, Wired,&nbsp;</em>Apartment Therapy, and many others. With&nbsp;<a href=\"http://helixsleep.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\">Helix</a>, there\u2019s a specific mattress to meet each and every body\u2019s unique comfort needs. Just take their quiz\u2014<a href=\"http://helixsleep.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\">only two minutes to complete</a>\u2014that matches your body type and sleep preferences to the perfect mattress for you. They have a 10-year warranty, and you get to try it out for a hundred nights, risk free. They\u2019ll even pick it up from you if you don\u2019t love it.&nbsp;</p><p><strong>And now, to my dear listeners, Helix is offering up to 200 dollars off all mattress orders plus two free pillows at&nbsp;</strong><a href=\"http://helixsleep.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>HelixSleep.com/Tim</strong></a><strong>.</strong></p><p><strong>*</strong></p><p><strong>This episode is also brought to you by&nbsp;</strong><a href=\"https://linkedin.com/Tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>LinkedIn Jobs</strong></a><strong>.</strong>&nbsp;Whether you are looking to hire now for a critical role or thinking about needs that you may have in the future,&nbsp;<a href=\"https://linkedin.com/Tim\" rel=\"noopener noreferrer\" target=\"_blank\">LinkedIn Jobs</a>&nbsp;can help. LinkedIn screens candidates for the hard and soft skills you\u2019re looking for and puts your job in front of candidates looking for job opportunities that match what you have to offer.</p><p>Using LinkedIn\u2019s active community of more than 770 million professionals worldwide,&nbsp;<a href=\"https://linkedin.com/Tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>LinkedIn Jobs</strong></a>&nbsp;can help you find and hire the right person faster.&nbsp;<strong>When your business is ready to make that next hire, find the right person with LinkedIn Jobs. And now, you can post a job for free.</strong>&nbsp;<a href=\"https://linkedin.com/Tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>Just visit LinkedIn.com/Tim</strong></a><strong>.</strong></p><p><strong>*</strong></p><p><strong>If you enjoy the podcast, would you please consider&nbsp;</strong><a href=\"https://podcasts.apple.com/us/podcast/the-tim-ferriss-show/id863897795?mt=2\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>leaving a short&nbsp;review&nbsp;on Apple Podcasts</strong></a><strong>?</strong>&nbsp;It takes less than 60 seconds, and it really makes a difference in helping to convince hard-to-get guests. I also love reading the&nbsp;reviews!</p><p><strong>For show notes and past guests, please visit</strong>&nbsp;<a href=\"https://tim.blog/podcast/?utm_source=podcast&amp;utm_medium=podcast&amp;utm_campaign=podcast-description\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>tim.blog/podcast</strong></a><strong>.</strong></p><p><strong>Sign up for Tim\u2019s email newsletter (\u201c5-Bullet Friday\u201d) at&nbsp;</strong><a href=\"https://go.tim.blog/5-bullet-friday-1/\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>tim.blog/friday</strong></a><strong>.</strong></p><p><strong>For transcripts of episodes, go to&nbsp;</strong><a href=\"http://tim.blog/transcripts\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>tim.blog/transcripts</strong></a><strong>.</strong></p><p><strong>Discover Tim\u2019s books:&nbsp;</strong><a href=\"http://tim.blog/books\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>tim.blog/books</strong></a><strong>.</strong></p><p><strong>Follow Tim:</strong></p><p><strong>Twitter</strong>:&nbsp;<a href=\"https://twitter.com/tferriss\" rel=\"noopener noreferrer\" target=\"_blank\">twitter.com/tferriss</a>&nbsp;</p><p><strong>Instagram</strong>:&nbsp;<a href=\"https://instagram.com/timferriss/\" rel=\"noopener noreferrer\" target=\"_blank\">instagram.com/timferriss</a></p><p><strong>Facebook</strong>:&nbsp;<a href=\"https://www.facebook.com/TimFerriss/\" rel=\"noopener noreferrer\" target=\"_blank\">facebook.com/timferriss</a>&nbsp;</p><p><strong>YouTube</strong>:&nbsp;<a href=\"https://www.youtube.com/timferriss\" rel=\"noopener noreferrer\" target=\"_blank\">youtube.com/timferriss</a></p><p>Past guests on&nbsp;<a href=\"http://tim.blog/podcast\" rel=\"noopener noreferrer\" target=\"_blank\"><strong><em>The Tim Ferriss Show</em></strong></a>&nbsp;include&nbsp;<a href=\"https://tim.blog/2020/12/08/jerry-seinfeld/\" rel=\"noopener noreferrer\" target=\"_blank\">Jerry Seinfeld</a>,&nbsp;<a href=\"https://tim.blog/2020/06/26/hugh-jackman/\" rel=\"noopener noreferrer\" target=\"_blank\">Hugh Jackman</a>,&nbsp;<a href=\"https://tim.blog/2020/04/16/jane-goodall/\" rel=\"noopener noreferrer\" target=\"_blank\">Dr. Jane Goodall</a>,&nbsp;<a href=\"https://tim.blog/2018/11/27/lebron-james-mike-mancias/\" rel=\"noopener noreferrer\" target=\"_blank\">LeBron James</a>,&nbsp;<a href=\"https://tim.blog/2020/05/20/kevin-hart/\" rel=\"noopener noreferrer\" target=\"_blank\">Kevin Hart</a>,&nbsp;<a href=\"https://tim.blog/2018/09/07/doris-kearns-goodwin-leadership/\" rel=\"noopener noreferrer\" target=\"_blank\">Doris Kearns Goodwin</a>,&nbsp;<a href=\"https://tim.blog/2015/12/06/jamie-foxx/\" rel=\"noopener noreferrer\" target=\"_blank\">Jamie Foxx</a>,&nbsp;<a href=\"https://tim.blog/2020/10/19/matthew-mcconaughey/\" rel=\"noopener noreferrer\" target=\"_blank\">Matthew McConaughey</a>,&nbsp;<a href=\"https://tim.blog/2017/05/21/esther-perel/\" rel=\"noopener noreferrer\" target=\"_blank\">Esther Perel</a>,&nbsp;<a href=\"https://tim.blog/2020/05/08/elizabeth-gilbert/\" rel=\"noopener noreferrer\" target=\"_blank\">Elizabeth Gilbert</a>,&nbsp;<a href=\"https://tim.blog/2017/12/20/terry-crews-how-to-have-do-and-be-all-you-want/\" rel=\"noopener noreferrer\" target=\"_blank\">Terry Crews</a>,&nbsp;<a href=\"https://tim.blog/2020/08/12/sia/\" rel=\"noopener noreferrer\" target=\"_blank\">Sia</a>,&nbsp;<a href=\"https://tim.blog/2020/10/27/yuval-noah-harari/\" rel=\"noopener noreferrer\" target=\"_blank\">Yuval Noah Harari</a>,&nbsp;<a href=\"https://tim.blog/2016/06/21/malcolm-gladwell/\" rel=\"noopener noreferrer\" target=\"_blank\">Malcolm Gladwell</a>,&nbsp;<a href=\"https://tim.blog/2020/05/27/secretary-madeleine-albright/\" rel=\"noopener noreferrer\" target=\"_blank\">Madeleine Albright</a>,&nbsp;<a href=\"https://tim.blog/2017/03/30/cheryl-strayed/\" rel=\"noopener noreferrer\" target=\"_blank\">Cheryl Strayed</a>,&nbsp;<a href=\"https://tim.blog/2019/02/18/jim-collins/\" rel=\"noopener noreferrer\" target=\"_blank\">Jim Collins</a>,&nbsp;<a href=\"https://tim.blog/2020/11/11/mary-karr/\" rel=\"noopener noreferrer\" target=\"_blank\">Mary Karr,</a>&nbsp;<a href=\"https://tim.blog/2014/10/21/brain-pickings/\" rel=\"noopener noreferrer\" target=\"_blank\">Maria Popova</a>,&nbsp;<a href=\"https://tim.blog/2020/05/15/sam-harris-2/\" rel=\"noopener noreferrer\" target=\"_blank\">Sam Harris</a>,&nbsp;<a href=\"https://tim.blog/2021/01/21/michael-phelps-grant-hackett/\" rel=\"noopener noreferrer\" target=\"_blank\">Michael Phelps</a>,&nbsp;<a href=\"https://tim.blog/2020/01/16/bob-iger/\" rel=\"noopener noreferrer\" target=\"_blank\">Bob Iger</a>,&nbsp;<a href=\"https://tim.blog/2019/10/31/edward-norton-motherless-brooklyn/\" rel=\"noopener noreferrer\" target=\"_blank\">Edward Norton</a>,&nbsp;<a href=\"https://tim.blog/2015/02/02/arnold-schwarzenegger/\" rel=\"noopener noreferrer\" target=\"_blank\">Arnold Schwarzenegger</a>,&nbsp;<a href=\"https://tim.blog/2014/06/24/neil-strauss/\" rel=\"noopener noreferrer\" target=\"_blank\">Neil Strauss</a>,&nbsp;<a href=\"https://tim.blog/2019/09/12/ken-burns/\" rel=\"noopener noreferrer\" target=\"_blank\">Ken Burns</a>,&nbsp;<a href=\"https://tim.blog/2017/08/26/maria-sharapova/\" rel=\"noopener noreferrer\" target=\"_blank\">Maria Sharapova</a>,&nbsp;<a href=\"https://tim.blog/2016/05/29/marc-andreessen/\" rel=\"noopener noreferrer\" target=\"_blank\">Marc Andreessen</a>,&nbsp;<a href=\"https://tim.blog/2019/03/28/neil-gaiman/\" rel=\"noopener noreferrer\" target=\"_blank\">Neil Gaiman</a>,&nbsp;<a href=\"https://tim.blog/2019/10/03/neil-degrasse-tyson/\" rel=\"noopener noreferrer\" target=\"_blank\">Neil de Grasse Tyson</a>,&nbsp;<a href=\"https://tim.blog/2016/09/21/jocko-willink-on-discipline-leadership-and-overcoming-doubt/\" rel=\"noopener noreferrer\" target=\"_blank\">Jocko Willink</a>,&nbsp;<a href=\"https://tim.blog/2020/12/03/daniel-ek/\" rel=\"noopener noreferrer\" target=\"_blank\">Daniel Ek</a>,&nbsp;<a href=\"https://tim.blog/2020/09/08/kelly-slater/\" rel=\"noopener noreferrer\" target=\"_blank\">Kelly Slater</a>,&nbsp;<a href=\"https://tim.blog/2019/11/27/peter-attia-fasting-metformin-longevity/\" rel=\"noopener noreferrer\" target=\"_blank\">Dr. Peter Attia</a>,&nbsp;<a href=\"https://tim.blog/2016/02/10/seth-godin/\" rel=\"noopener noreferrer\" target=\"_blank\">Seth Godin</a>,&nbsp;<a href=\"https://tim.blog/2018/09/25/howard-marks/\" rel=\"noopener noreferrer\" target=\"_blank\">Howard Marks</a>,&nbsp;<a href=\"https://tim.blog/2020/02/06/brene-brown-striving-self-acceptance-saving-marriages/\" rel=\"noopener noreferrer\" target=\"_blank\">Dr. Bren\u00e9 Brown</a>,&nbsp;<a href=\"https://tim.blog/2019/04/09/eric-schmidt/\" rel=\"noopener noreferrer\" target=\"_blank\">Eric Schmidt</a>,&nbsp;<a href=\"https://tim.blog/2020/05/01/michael-lewis/\" rel=\"noopener noreferrer\" target=\"_blank\">Michael Lewis</a>,&nbsp;<a href=\"https://tim.blog/2018/03/08/joe-gebbia-co-founder-of-airbnb/\" rel=\"noopener noreferrer\" target=\"_blank\">Joe Gebbia</a>,&nbsp;<a href=\"https://tim.blog/2018/05/06/michael-pollan-how-to-change-your-mind/\" rel=\"noopener noreferrer\" target=\"_blank\">Michael Pollan</a>,&nbsp;<a href=\"https://tim.blog/2021/03/01/jordan-peterson/\" rel=\"noopener noreferrer\" target=\"_blank\">Dr. Jordan Peterson</a>,&nbsp;<a href=\"https://tim.blog/2017/05/31/vince-vaughn/\" rel=\"noopener noreferrer\" target=\"_blank\">Vince Vaughn</a>,&nbsp;<a href=\"https://tim.blog/2020/04/23/brian-koppelman/\" rel=\"noopener noreferrer\" target=\"_blank\">Brian Koppelman</a>,&nbsp;<a href=\"https://tim.blog/2019/05/07/ramit-sethi/\" rel=\"noopener noreferrer\" target=\"_blank\">Ramit Sethi</a>,&nbsp;<a href=\"https://tim.blog/2020/11/18/dax-shepard/\" rel=\"noopener noreferrer\" target=\"_blank\">Dax Shepard</a>,&nbsp;<a href=\"https://tim.blog/2014/10/15/money-master-the-game/\" rel=\"noopener noreferrer\" target=\"_blank\">Tony Robbins</a>,&nbsp;<a href=\"https://tim.blog/2020/05/18/jim-dethmer/\" rel=\"noopener noreferrer\" target=\"_blank\">Jim Dethmer</a>,&nbsp;<a href=\"https://tim.blog/2020/11/19/dan-harris/\" rel=\"noopener noreferrer\" target=\"_blank\">Dan Harris</a>,&nbsp;<a href=\"https://tim.blog/2017/09/13/ray-dalio/\" rel=\"noopener noreferrer\" target=\"_blank\">Ray Dalio</a>,&nbsp;<a href=\"https://tim.blog/2015/08/18/the-evolutionary-angel-naval-ravikant/\" rel=\"noopener noreferrer\" target=\"_blank\">Naval Ravikant</a>,&nbsp;<a href=\"https://tim.blog/2021/03/08/vitalik-buterin-naval-ravikant/\" rel=\"noopener noreferrer\" target=\"_blank\">Vitalik Buterin</a>,&nbsp;<a href=\"https://tim.blog/2021/03/16/elizabeth-lesser/\" rel=\"noopener noreferrer\" target=\"_blank\">Elizabeth Lesser</a>,&nbsp;<a href=\"https://tim.blog/2019/04/18/amanda-palmer-2/\" rel=\"noopener noreferrer\" target=\"_blank\">Amanda Palmer</a>,&nbsp;<a href=\"https://tim.blog/2021/02/18/katie-haun/\" rel=\"noopener noreferrer\" target=\"_blank\">Katie Haun</a>,&nbsp;<a href=\"https://tim.blog/2017/10/09/richard-branson/\" rel=\"noopener noreferrer\" target=\"_blank\">Sir Richard Branson</a>,&nbsp;<a href=\"https://tim.blog/2020/09/02/chuck-palahniuk/\" rel=\"noopener noreferrer\" target=\"_blank\">Chuck Palahniuk</a>,&nbsp;<a href=\"https://tim.blog/2017/10/18/arianna-huffington/\" rel=\"noopener noreferrer\" target=\"_blank\">Arianna Huffington</a>,&nbsp;<a href=\"https://tim.blog/2015/08/31/the-oracle-of-silicon-valley-reid-hoffman-plus-michael-mccullough/\" rel=\"noopener noreferrer\" target=\"_blank\">Reid Hoffman</a>,&nbsp;<a href=\"https://tim.blog/2017/09/17/bill-burr/\" rel=\"noopener noreferrer\" target=\"_blank\">Bill Burr</a>,&nbsp;<a href=\"https://tim.blog/2015/06/26/whitney-cummings/\" rel=\"noopener noreferrer\" target=\"_blank\">Whitney Cummings</a>,&nbsp;<a href=\"https://tim.blog/2015/05/15/rick-rubin/\" rel=\"noopener noreferrer\" target=\"_blank\">Rick Rubin</a>,&nbsp;<a href=\"https://tim.blog/2020/03/26/vivek-murthy/\" rel=\"noopener noreferrer\" target=\"_blank\">Dr. Vivek Murthy</a>,&nbsp;<a href=\"https://tim.blog/2017/09/09/darren-aronofsky/\" rel=\"noopener noreferrer\" target=\"_blank\">Darren Aronofsky</a>, and many more.</p><p>See Privacy Policy at <a href=\"https://art19.com/privacy\" rel=\"noopener noreferrer\" target=\"_blank\">https://art19.com/privacy</a> and California Privacy Notice at <a href=\"https://art19.com/privacy#do-not-sell-my-info\" rel=\"noopener noreferrer\" target=\"_blank\">https://art19.com/privacy#do-not-sell-my-info</a>.</p>",
        "pub_date_ms": 1634222633000,
        "guid_from_rss": "gid://art19-episode-locator/V0/BtqNd8i7Fya-HhzGx_0SKu-ZiX1V8AB2Te4M0bCkakQ",
        "listennotes_url": "https://www.listennotes.com/e/af19ceda98d84d3c92eafe7e7f63b6dd/",
        "audio_length_sec": 10927,
        "explicit_content": false,
        "maybe_audio_invalid": false,
        "listennotes_edit_url": "https://www.listennotes.com/e/af19ceda98d84d3c92eafe7e7f63b6dd/#edit"
      },
      "type": "episode",
      "notes": "",
      "added_at_ms": 1634779096596
    },
    {
      "id": 580202,
      "data": {
        "id": "463b7db874c04c3ca66cefda3e9d4679",
        "link": "http://exponent.fm/episode-194-back-on-spotify/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/463b7db874c04c3ca66cefda3e9d4679/",
        "image": "https://production.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-4-khvom1d3W-OaJSjb4xQv3.1400x1400.jpg",
        "title": "Episode 194 \u2014 Back on Spotify",
        "podcast": {
          "id": "37589a3e121e40debe4cef3d9638932a",
          "image": "https://production.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-4-khvom1d3W-OaJSjb4xQv3.1400x1400.jpg",
          "title": "Exponent",
          "publisher": "Ben Thompson / James Allworth",
          "thumbnail": "https://production.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-lRYU3p4xQ-m-OaJSjb4xQv3.300x300.jpg",
          "listen_score": 61,
          "listennotes_url": "https://www.listennotes.com/c/37589a3e121e40debe4cef3d9638932a/",
          "listen_score_global_rank": "0.1%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-lRYU3p4xQ-m-OaJSjb4xQv3.300x300.jpg",
        "description": "<p>Ben and James discuss the history of podcasts and why Spotify&#8217;s recent announcements are so compelling for creators.</p>\n<p><strong>Links</strong></p>\n<ul>\n<li>Ben Thompson: Spotify&#8217;s Surprise \u2014 <a href=\"https://stratechery.com/2021/spotifys-surprise/\">Stratechery</a></li>\n<li>Episode 185 \u2014 Open, Free, and Spotify \u2014 <a href=\"https://exponent.fm/episode-185-open-free-and-spotify/\">Exponent</a></li>\n<li>Ben Thompson: Podcasts, Analytics, and Centralization \u2014 <a href=\"https://stratechery.com/2017/podcasts-analytics-and-centralization/\">Stratechery</a></li>\n<li>Ben Thompson: Spotify\u2019s Podcast Aggregation Play \u2014 <a href=\"https://stratechery.com/2019/spotifys-podcast-aggregation-play/\">Stratechery</a></li>\n<li>Ben Thompson: Dithering and Open Versus Free \u2014 <a href=\"https://stratechery.com/2020/dithering-and-the-open-web/\">Stratechery</a></li>\n<li>Ben Thompson: Spotify Earnings, Podcasts and Lifetime Value, The Ringer Acquisition \u2014 <a href=\"https://stratechery.com/2020/spotifys-earnings-podcasts-and-lifetime-value-the-ringer-acquisition/\">Stratechery</a></li>\n<li>Ben Thompson: The European Super League, Apple Music\u2019s Letter to Artists \u2014 <a href=\"https://stratechery.com/2021/the-european-super-league-apple-musics-letter-to-artists/\">Stratechery</a></li>\n<li>Ben Thompson: Podcast Subscriptions vs. the App Store \u2014 <a href=\"https://stratechery.com/2021/podcast-subscriptions-vs-the-app-store/\">Stratechery</a></li>\n<li>Ben Thompson: Fearing Spotify?, Apple\u2019s Earnings, Margins and Chips \u2014 <a href=\"https://stratechery.com/2021/fearing-spotify-apples-earnings-margins-and-chips/\">Stratechery</a></li>\n</ul>\n<p><strong>Hosts</strong></p>\n<p>\u00a0</p>\n<ul>\n<li>Ben Thompson, <a href=\"http://twitter.com/benthompson\">@benthompson</a>, <a href=\"http://stratechery.com\">Stratechery</a></li>\n<li>James Allworth, <a href=\"http://twitter.com/jamesallworth\">@jamesallworth</a>, <a href=\"https://hbr.org/search?term=James+Allworth&#038;sort=popularity_score\">Harvard Business Review</a></li>\n</ul>\n<p>\u00a0</p>\n<p><strong>Podcast Information</strong></p>\n<p>\u00a0</p>\n<ul>\n<li><a href=\"http://exponent.fm/feed/\">Feed</a></li>\n<li><a href=\"https://itunes.apple.com/us/podcast/exponent/id826420969\">iTunes</a></li>\n<li><a href=\"https://soundcloud.com/exponentfm\">SoundCloud</a></li>\n<li><a href=\"http://twitter.com/exponentfm\">Twitter</a></li>\n<li><a href=\"http://stratechery.com/exponent-feedback/\">Feedback</a></h2>\n</li>\n</ul>",
        "pub_date_ms": 1619771580000,
        "guid_from_rss": "https://exponent.fm/?p=429",
        "listennotes_url": "https://www.listennotes.com/e/463b7db874c04c3ca66cefda3e9d4679/",
        "audio_length_sec": 3978,
        "explicit_content": false,
        "maybe_audio_invalid": false,
        "listennotes_edit_url": "https://www.listennotes.com/e/463b7db874c04c3ca66cefda3e9d4679/#edit"
      },
      "type": "episode",
      "notes": "",
      "added_at_ms": 1619799889806
    },
    {
      "id": 524059,
      "data": {
        "id": "5810e500db4c472aa03a6a5685bf8fbd",
        "error": "This episode has been deleted from the podcast database. Possible reasons: 1) Podcast producers sometimes delete their old episodes. 2) Copyright issues.",
        "title": "Spotify Betting Big on Podcasts",
        "status": "deleted"
      },
      "type": "episode",
      "notes": "",
      "added_at_ms": 1610639628046
    },
    {
      "id": 475797,
      "data": {
        "id": "4c72c4dfac004ffca0867a70361f77ab",
        "link": "https://omny.fm/shows/the-james-altucher-show/side-hustle-friday-podcast-monetization?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/4c72c4dfac004ffca0867a70361f77ab/",
        "image": "https://production.listennotes.com/podcasts/the-james-altucher/side-hustle-friday-monetize-LncxE9KjCgt-jDmTs6Nl-tr.1400x1400.jpg",
        "title": "Side Hustle Friday: Why should you START a podcast and MONETIZE your podcast through Ads and Patreon!",
        "podcast": {
          "id": "6dabf2f65c384e1f897bb606859309f4",
          "image": "https://production.listennotes.com/podcasts/the-james-altucher-show-james-altucher-ydcMlwOz5W7-sSHocv8YjIe.1400x1400.jpg",
          "title": "The James Altucher Show",
          "publisher": "James Altucher",
          "thumbnail": "https://production.listennotes.com/podcasts/the-james-altucher-show-james-altucher-Hnzt-457Amb-sSHocv8YjIe.300x300.jpg",
          "listen_score": 68,
          "listennotes_url": "https://www.listennotes.com/c/6dabf2f65c384e1f897bb606859309f4/",
          "listen_score_global_rank": "0.05%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/the-james-altucher/side-hustle-friday-monetize-qtbDBvrK5Ii-jDmTs6Nl-tr.300x300.jpg",
        "description": "<p>Another Side Hustle Friday! I sat down with Jay Yow, the Sound Engineer/ Producer of The James Altucher, to discuss ways to monetize a podcast, we spoke about why this is the best time to launch a podcast and our equipment set up for remote recording and interview. In this episode, we break down that's the different ways you can monetize through Ads, sponsors, affiliate deals, and Patreon! Part 2 will be coming soon Monday!</p>\n<hr>\n<p><strong>I write about all my podcasts! Check out the full post and learn what I learned at&nbsp;<a href=\"https://www.jamesaltucher.com/podcast\">jamesaltucher.com/podcast</a>.</strong></p>\n<p><strong>Thanks so much for listening! If you like this episode, please subscribe to &ldquo;The James Altucher Show&rdquo; and rate and review wherever you get your podcasts:</strong></p>\n<p><a href=\"https://itunes.apple.com/us/podcast/the-james-altucher-show/id794030859?mt=2\">Apple Podcasts</a></p>\n<p><a href=\"https://www.stitcher.com/podcast/stansberry-radio-network/the-james-altucher-show/e/52735033\">Stitcher</a></p>\n<p><a href=\"https://www.iheart.com/podcast/232-The-James-Altucher-Show-27085086/episode/ep-298-ryan-holiday-competition-28789411/\">iHeart Radio</a></p>\n<p><a href=\"https://open.spotify.com/episode/0ABi9w3Qrb2EFNDeeXlHyz\">Spotify</a></p>\n<p>&nbsp;</p>\n<p><strong>Follow me on Social Media:</strong></p>\n<p><a href=\"https://www.youtube.com/channel/UCRQlx2klE_aNrPhz2OyKRdg\">YouTube</a></p>\n<p><a href=\"https://twitter.com/jaltucher\">Twitter</a></p>\n<p><a href=\"https://www.facebook.com/JAltucher.Blog/\">Facebook</a></p>\n<p><a href=\"https://www.linkedin.com/in/jamesaltucher\">Linkedin</a></p><p>See <a href=\"https://omnystudio.com/listener\">omnystudio.com/listener</a> for privacy information.</p>",
        "pub_date_ms": 1602831600169,
        "guid_from_rss": "fae163b1-dcc2-4600-b040-ac5600102349",
        "listennotes_url": "https://www.listennotes.com/e/4c72c4dfac004ffca0867a70361f77ab/",
        "audio_length_sec": 3007,
        "explicit_content": false,
        "maybe_audio_invalid": false,
        "listennotes_edit_url": "https://www.listennotes.com/e/4c72c4dfac004ffca0867a70361f77ab/#edit"
      },
      "type": "episode",
      "notes": "",
      "added_at_ms": 1603256538471
    },
    {
      "id": 475796,
      "data": {
        "id": "d5e2112643ac4d01baaa8eab6c7b7cae",
        "link": "https://omny.fm/shows/the-james-altucher-show/side-hustle-friday-podcast-monetization-pt-2?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/d5e2112643ac4d01baaa8eab6c7b7cae/",
        "image": "https://production.listennotes.com/podcasts/the-james-altucher/side-hustle-friday-monetize-OBljDR14EC3-vZt0gi5hoDN.1400x1400.jpg",
        "title": "Side Hustle Friday: Monetize your podcast right now!",
        "podcast": {
          "id": "6dabf2f65c384e1f897bb606859309f4",
          "image": "https://production.listennotes.com/podcasts/the-james-altucher-show-james-altucher-ydcMlwOz5W7-sSHocv8YjIe.1400x1400.jpg",
          "title": "The James Altucher Show",
          "publisher": "James Altucher",
          "thumbnail": "https://production.listennotes.com/podcasts/the-james-altucher-show-james-altucher-Hnzt-457Amb-sSHocv8YjIe.300x300.jpg",
          "listen_score": 68,
          "listennotes_url": "https://www.listennotes.com/c/6dabf2f65c384e1f897bb606859309f4/",
          "listen_score_global_rank": "0.05%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/the-james-altucher/side-hustle-friday-monetize-i4IhCZMzQTl-vZt0gi5hoDN.300x300.jpg",
        "description": "<p>Part 2 on monetizing your podcast! In this episode, we talked about ways to monetize your podcast via merchandising, getting hired as a consultant through your podcast, speaking gigs, on and on! Also, enjoy Jay's episodic debut on the podcast! (Technically a second since this is a part of Friday's podcast!)</p>\n<hr>\n<p><strong>I write about all my podcasts! Check out the full post and learn what I learned at&nbsp;<a href=\"https://www.jamesaltucher.com/podcast\">jamesaltucher.com/podcast</a>.</strong></p>\n<p><strong>Thanks so much for listening! If you like this episode, please subscribe to &ldquo;The James Altucher Show&rdquo; and rate and review wherever you get your podcasts:</strong></p>\n<p><a href=\"https://itunes.apple.com/us/podcast/the-james-altucher-show/id794030859?mt=2\">Apple Podcasts</a></p>\n<p><a href=\"https://www.stitcher.com/podcast/stansberry-radio-network/the-james-altucher-show/e/52735033\">Stitcher</a></p>\n<p><a href=\"https://www.iheart.com/podcast/232-The-James-Altucher-Show-27085086/episode/ep-298-ryan-holiday-competition-28789411/\">iHeart Radio</a></p>\n<p><a href=\"https://open.spotify.com/episode/0ABi9w3Qrb2EFNDeeXlHyz\">Spotify</a></p>\n<p>&nbsp;</p>\n<p><strong>Follow me on Social Media:</strong></p>\n<p><a href=\"https://www.youtube.com/channel/UCRQlx2klE_aNrPhz2OyKRdg\">YouTube</a></p>\n<p><a href=\"https://twitter.com/jaltucher\">Twitter</a></p>\n<p><a href=\"https://www.facebook.com/JAltucher.Blog/\">Facebook</a></p>\n<p><a href=\"https://www.linkedin.com/in/jamesaltucher\">Linkedin</a></p><p>See <a href=\"https://omnystudio.com/listener\">omnystudio.com/listener</a> for privacy information.</p>",
        "pub_date_ms": 1603090800167,
        "guid_from_rss": "7e70863f-ebf1-4641-b151-ac5800ea8773",
        "listennotes_url": "https://www.listennotes.com/e/d5e2112643ac4d01baaa8eab6c7b7cae/",
        "audio_length_sec": 2617,
        "explicit_content": false,
        "maybe_audio_invalid": false,
        "listennotes_edit_url": "https://www.listennotes.com/e/d5e2112643ac4d01baaa8eab6c7b7cae/#edit"
      },
      "type": "episode",
      "notes": "",
      "added_at_ms": 1603256526157
    },
    {
      "id": 434674,
      "data": {
        "id": "3c311c8cf83448dea0463c69bfe61c75",
        "link": "http://feedproxy.google.com/~r/twist-audio/~3/mpdJUZ2omI0/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/3c311c8cf83448dea0463c69bfe61c75/",
        "image": "https://production.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-rMEoeGBJqt1-EKckR36zrnA.1400x1400.jpg",
        "title": "E1096: Podcasting State of the Union featuring Overcast\u2019s Marco Arment & Oxford Road\u2019s Dan Granger",
        "podcast": {
          "id": "9a62e2581908415185dee35d2d19f9b5",
          "image": "https://production.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-rMEoeGBJqt1-EKckR36zrnA.1400x1400.jpg",
          "title": "This Week in Startups",
          "publisher": "Jason Calacanis",
          "thumbnail": "https://production.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-txh7pAS-Xsy-EKckR36zrnA.300x300.jpg",
          "listen_score": 63,
          "listennotes_url": "https://www.listennotes.com/c/9a62e2581908415185dee35d2d19f9b5/",
          "listen_score_global_rank": "0.1%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-txh7pAS-Xsy-EKckR36zrnA.300x300.jpg",
        "description": "<img src=\"http://feeds.feedburner.com/~r/twist-audio/~4/mpdJUZ2omI0\" height=\"1\" width=\"1\" alt=\"\"/>",
        "pub_date_ms": 1597416466256,
        "guid_from_rss": "https://thisweekinstartups.com/?p=41080",
        "listennotes_url": "https://www.listennotes.com/e/3c311c8cf83448dea0463c69bfe61c75/",
        "audio_length_sec": 5250,
        "explicit_content": false,
        "maybe_audio_invalid": false,
        "listennotes_edit_url": "https://www.listennotes.com/e/3c311c8cf83448dea0463c69bfe61c75/#edit"
      },
      "type": "episode",
      "notes": "",
      "added_at_ms": 1597421395248
    },
    {
      "id": 424141,
      "data": {
        "id": "50d0110bec79414eac61cb472c3c1de2",
        "link": "https://anchor.fm/caseyadams/episodes/Elise-Hu---Hosting-TED-Talks-Daily--The-Future-of-Podcasting-ecfp5b?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/50d0110bec79414eac61cb472c3c1de2/",
        "image": "https://production.listennotes.com/podcasts/rise-of-the-young-casey-adams-vxBJKELbzMn-YuarHs5lfDI.1400x1400.jpg",
        "title": "Elise Hu - Hosting \"TED Talks Daily\" & The Future of Podcasting",
        "podcast": {
          "id": "11362a0682e744b29ce5ea73c920132e",
          "image": "https://production.listennotes.com/podcasts/rise-of-the-young-casey-adams-vxBJKELbzMn-YuarHs5lfDI.1400x1400.jpg",
          "title": "Rise of The Young",
          "publisher": "Casey Adams",
          "thumbnail": "https://production.listennotes.com/podcasts/rise-of-the-young-casey-adams-3BL-j4KFIZq-YuarHs5lfDI.300x300.jpg",
          "listen_score": 55,
          "listennotes_url": "https://www.listennotes.com/c/11362a0682e744b29ce5ea73c920132e/",
          "listen_score_global_rank": "0.5%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/rise-of-the-young-casey-adams-3BL-j4KFIZq-YuarHs5lfDI.300x300.jpg",
        "description": "<p>Elise Hu is a host-at-large based at NPR West in Culver City, Calif. Previously, she explored the future with her video series, <a href=\"https://www.npr.org/2019/05/06/716414780/videos-future-you\"><em>Future You with Elise Hu</em></a>, and served as the founding bureau chief and International Correspondent for NPR's Seoul office. She was based in Seoul for nearly four years, responsible for the network's coverage of both Koreas and Japan, and filed from a dozen countries across Asia. Before joining NPR, she was one of the founding reporters at <a href=\"http://www.texastribune.org/\">The Texas Tribune</a>, a non-profit digital news startup devoted to politics and public policy. While at the Tribune, Hu oversaw television partnerships and multimedia projects, contributed to <em>The New York Times</em>' expanded Texas coverage, and pushed for editorial innovation across platforms.Her work at NPR has earned a DuPont-Columbia award and a Gracie Award from the Alliance for Women in Media for her video series, <em>Elise Tries</em>. Her previous work has earned a Gannett Foundation Award for Innovation in Watchdog Journalism, a National Edward R. Murrow award for best online video, and beat reporting awards from the Texas Associated Press. <em>The Austin Chronicle</em> once dubiously named her the \"<a href=\"http://www.austinchronicle.com/gyrobase/Awards/BestOfAustin?Award=660138\">Best TV Reporter Who Can Write</a>.\"</p>\n<p>Follow Elise Hu on Instagram: <a href=\"https://www.instagram.com/elisewho/?hl=en\">https://www.instagram.com/elisewho/?hl=en</a></p>\n<p>Learn more about Elise Hu: <a href=\"https://elisehu.com/\">https://elisehu.com/</a></p>\n<p>Listen to \"TED Talks Daily\" <a href=\"https://podcasts.apple.com/us/podcast/ted-talks-daily/id160904630\">https://podcasts.apple.com/us/podcast/ted-talks-daily/id160904630</a></p>",
        "pub_date_ms": 1586266731113,
        "guid_from_rss": "9aeee818-e72c-4928-8149-7cae42595d82",
        "listennotes_url": "https://www.listennotes.com/e/50d0110bec79414eac61cb472c3c1de2/",
        "audio_length_sec": 2445,
        "explicit_content": false,
        "maybe_audio_invalid": false,
        "listennotes_edit_url": "https://www.listennotes.com/e/50d0110bec79414eac61cb472c3c1de2/#edit"
      },
      "type": "episode",
      "notes": "",
      "added_at_ms": 1595791871517
    },
    {
      "id": 423865,
      "data": {
        "id": "8f51c8e8b19a4c638ecbce12f9322ba8",
        "link": "https://thefeed.libsyn.com/167-cleanfeed-with-a-side-of-google-podcasts?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/8f51c8e8b19a4c638ecbce12f9322ba8/",
        "image": "https://production.listennotes.com/podcasts/the-feed-the/167-cleanfeed-with-a-side-of-_HxANWiUlRk-OS-PBaQKcgl.1400x1400.jpg",
        "title": "167 Cleanfeed With A Side of Google Podcasts",
        "podcast": {
          "id": "ce3754058c7a44a0abd574f86ff5c719",
          "image": "https://production.listennotes.com/podcasts/the-feed-the-official-libsyn-podcast-elsie-vpSizOJdtuG-2kOexVdGJIv.1400x1400.jpg",
          "title": "The Feed The Official Libsyn Podcast",
          "publisher": "Elsie Escobar and Rob Walch",
          "thumbnail": "https://production.listennotes.com/podcasts/the-feed-the-official-libsyn-podcast-elsie-1gCfKIP5XVy-2kOexVdGJIv.300x300.jpg",
          "listen_score": 45,
          "listennotes_url": "https://www.listennotes.com/c/ce3754058c7a44a0abd574f86ff5c719/",
          "listen_score_global_rank": "1%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/the-feed-the/167-cleanfeed-with-a-side-of-KEMJ65zVY4x-OS-PBaQKcgl.300x300.jpg",
        "description": "<p>Tons of details on all things Google Podcasts Manager! It\u2019s like Apple Podcasts connect but of course Google. Then, we move on to jobs in podcasting, so much about feedback about Cleanfeed, some very interesting Facebook updates, Libsyn player automation, what if someone uses YOUR podcast name, a massive breakdown of the podfader types and of course we\u2019ve got a crazy amount of stats!</p> <p>Audience feedback drives the show. We\u2019d love for you to email us and keep the conversation going! Email thefeed@libsyn.com or call 412\u2013573\u20131934. We\u2019d love to hear from you!</p> Quick Episode Summary <ul> <li><em>:07</em> Intro!</li> <li><em>3:04 PROMO 1: Sailing in the Mediterranean and Beyond</em></li> <li><em>3:34</em> Rob and Elsie conversation</li> <li>Announcement of Google Podcasts Manager!</li> <li>What it is, what it gives you and how it it different than Apple Podcasts analytics</li> <li>9:46 Apple is hiring for all kinds of podcasting positions</li> <li>13:56 Cleanfeed audio feedback from Carey Green</li> <li>Emails about Cleanfeed</li> <li>18:08 Cleanfeed audio feedback from CG</li> <li>Thoughts and processes about remote recording</li> <li>There\u2019s a new kid in town</li> <li>27:35 Facebook updates about charging for online events and listening to Faceboook Lives</li> <li>30:58 PROMO 2: The Naturist Living Show</li> <li>New version of Podcast Addict now with reviews</li> <li>Custom automation for the libsyn players</li> <li>Face ID and masks</li> <li>39:55 What if someone is using the name of your show? How do you go about dealing with it?</li> <li>A show appearing twice on some apps</li> <li>49:43 Podfading - the key main groups</li> <li>UK data from Rajar on internet delivery audio services via Neil!</li> <li>57:38 PROMO 3: The Europe Desk</li> <li>Stats, stats, stats: mean and median</li> <li>59:52 COVID\u201319 libsyn stats</li> <li>Where have we been?</li> <li>Where are we going?</li> </ul> Featured Podcast Promos + Audio <ul> <li><a href=\"https://www.medsailor.com/\">PROMO 1: Sailing in the Mediterranean and Beyond</a></li> <li><a href=\"https://www.naturistlivingshow.com/\">PROMO 2: The Naturist Living Show</a></li> <li><a href=\"https://cges.georgetown.edu/research/podcast/\">PROMO 3: The Europe Desk</a></li> <li><a href=\"https://podcastfasttrack.com/\">Carey Green from Podcast Fast Track</a></li> <li><a href=\"https://www.therocketryshow.com/\">CB from the Rocketry Show</a></li> </ul> <p>Thank you to Nick from <a href= \"http://micme.com\">MicMe</a> for our awesome intro!</p>  <p><em>Podcasting Articles and Links mentioned by Rob and Elsie</em></p> <ul> <li><a href=\"http://speakpipe.com/thefeed\">Our SpeakPipe Feedback page!</a> Leave us feedback :)</li> <li><a href=\"http://podcastsmanager.google.com\">Google Podcasts Podcast Manager</a></li> <li><a href=\"https://podcasts.google.com/manager/about\">Google Podcasts Manager About Page</a></li> <li><a href= \"https://support.google.com/podcast-publishers/answer/9479755?hl=en&ref_topic=9476973&authuser=0\"> Adding new and existing podcasts</a></li> <li><a href=\"https://search.google.com/devtools/podcast/preview\">Is your show already in Google Podcasts? Check here</a></li> <li><a href= \"https://support.google.com/podcast-publishers/answer/9696727?hl=en&ref_topic=9476973&authuser=0\"> Manage users and permissions on Google Podcasts Manager</a></li> <li><a href= \"https://support.google.com/podcast-publishers?hl=en&authuser=0#topic=9476973\"> Google Podcasts Manager Support</a></li> <li><a href= \"https://jobs.apple.com/en-us/details/200164774/podcasts-operations-manager?team=MKTG\"> Podcasts Operations Manager</a></li> <li><a href= \"https://jobs.apple.com/en-us/details/200164287/program-manager-podcasts-apple-media-products?team=SFTWR\"> Program Manager, Podcasts, Apple Media Products</a></li> <li><a href= \"https://jobs.apple.com/en-us/details/200164774/podcasts-operations-manager?team=MKTG\"> UI Engineer, Apple Media Products (Podcasts)</a></li> <li><a href=\"https://youtu.be/DpRHSmJT_Vk\">Carey\u2019s Cleanfeed demo video</a></li> <li><a href= \"http://podcastification.com/in-search-of-the-best-way-to-record-an-interview-with-mark-hills-of-cleanfeed-ep-69\"> Carey\u2019s interview with Mark from Cleanfeed</a></li> <li><a href= \"https://podcastengineeringschool.com/marc-bakos-of-cleanfeed-pes-104/\"> Chris Curran\u2019s interview with Marc from Cleanfeed</a></li> <li><a href= \"https://www.reddit.com/r/podcasting/comments/flw9ae/services_and_applications_to_allow_remote/\"> Services and applications to allow remote recordings of remote guests and co-hosts. - Reddit</a></li> <li><a href=\"http://podcast411.com/mixer.pdf\">Rob\u2019s PDF</a></li> <li><a href= \"https://resonaterecordings.com/2020/04/voice-recorder\">Resonate Recordings new recorder</a></li> <li><a href= \"https://about.fb.com/news/2020/04/introducing-messenger-rooms/\">Facebook news</a></li> <li><a href= \"https://www.rajar.co.uk/docs/news/MIDAS_Spring_2020.pdf\">Rajar data for Measurement of Internet Delivery Audio Services</a></li> <li><a href= \"https://twitter.com/search?q=podcast411%20%23cmworld&src=typed_query&f=live\"> Rob\u2019s #CMWorld twitter chat</a></li> <li><a href= \"https://jacobsmedia.com/there-are-over-a-million-podcasts-in-apples-podcasts-app-what-does-it-mean/\"> There Are Over A Million Podcasts In Apple\u2019s Podcasts App, What Does It Mean?</a></li> <li><a href= \"http://www.insideradio.com/podcastnewsdaily/walch-podcast-downloads-aren-t-down-as-much-as-mobility-showing-medium-s-stickiness/article_394e057a-84ba-11ea-a6d0-a3defc713949.html\"> Walch: Proof Of Podcast \u2018Stickiness.\u2019</a></li> </ul>  <em>HELP US SPREAD THE WORD!</em> <p><em>We\u2019d love it if you could please share #TheFeed with your twitter followers. <a href= \"http://clicktotweet.com/9d2te\">Click here to post a tweet!</a></em></p> <p><em>If you dug this episode head on over to Apple Podcasts and kindly <a href= \"https://itunes.apple.com/us/podcast/feed-official-libsyn-podcast/id668413144\"> leave us a rating, a review and subscribe!</a></em></p> <em>Ways to subscribe to The Feed: The Official Libsyn Podcast</em> <ul> <li><em><a href= \"https://itunes.apple.com/us/podcast/feed-official-libsyn-podcast/id668413144\"> Click here to subscribe via Apple Podcasts</a></em></li> <li><em><a href=\"http://thefeed.libsyn.com/rss\">Click here to subscribe via RSS</a></em></li> <li><em><a href= \"http://www.stitcher.com/podcast/libsyn/the-feed\">You can also subscribe via Stitcher</a></em></li> </ul> FEEDBACK + PROMOTION <p><em>You can ask your questions, make comments and create a segment about podcasting for podcasters! Let your voice be heard.</em></p> <ul> <li>Download the FREE The Feed App for <a href= \"https://itunes.apple.com/us/app/the-feed-podcasting-tips-from-libsyn/id381787434?mt=8\"> iOS</a> and <a href= \"https://play.google.com/store/apps/details?id=com.libsyn.android.thefeed&hl=en\"> Android</a> (you can send feedback straight from within the app)</li> <li>Call 412 573 1934</li> <li>Email thefeed@libsyn.com</li> <li>Use our <a href=\"http://speakpipe.com/thefeed\">SpeakPipe Page</a>!</li> </ul>",
        "pub_date_ms": 1588694700035,
        "guid_from_rss": "7d758875-6443-4260-a57f-f31e35d21ec8",
        "listennotes_url": "https://www.listennotes.com/e/8f51c8e8b19a4c638ecbce12f9322ba8/",
        "audio_length_sec": 4337,
        "explicit_content": false,
        "maybe_audio_invalid": false,
        "listennotes_edit_url": "https://www.listennotes.com/e/8f51c8e8b19a4c638ecbce12f9322ba8/#edit"
      },
      "type": "episode",
      "notes": "",
      "added_at_ms": 1595731343450
    },
    {
      "id": 345601,
      "data": {
        "id": "dbd3d477dfc94128982b79e8152301b4",
        "link": "http://mschool.growtheverywhere.libsynpro.com/spotify-acquired-the-ringer-podcast-15m-in-revenues-heres-what-it-means-ep-1306?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/dbd3d477dfc94128982b79e8152301b4/",
        "image": "https://production.listennotes.com/podcasts/marketing-school-digital-marketing-and-knLzBPreqYx-pHyiIJT4Lxl.1400x1400.jpg",
        "title": "Spotify Acquired 'The Ringer' Podcast ($15M In Revenues) - Here's What It Means  | Ep. #1306",
        "podcast": {
          "id": "9a2abf6b68b54554a60a32a2932febcb",
          "image": "https://production.listennotes.com/podcasts/marketing-school-digital-marketing-and-knLzBPreqYx-pHyiIJT4Lxl.1400x1400.jpg",
          "title": "Marketing School - Digital Marketing and Online Marketing Tips",
          "publisher": "Eric Siu & Neil Patel",
          "thumbnail": "https://production.listennotes.com/podcasts/marketing-school-digital-marketing-and-9FS5Tsvab0Q-pHyiIJT4Lxl.300x300.jpg",
          "listen_score": 64,
          "listennotes_url": "https://www.listennotes.com/c/9a2abf6b68b54554a60a32a2932febcb/",
          "listen_score_global_rank": "0.1%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/marketing-school-digital-marketing-and-9FS5Tsvab0Q-pHyiIJT4Lxl.300x300.jpg",
        "description": "<p>In episode #1306, we discuss Spotify\u2019s acquisition of The Ringer. The podcasting industry is growing exponentially and Spotify wanted to make an aggressive move toward growing its market share. Tune in to hear why this was a super smart decision on their part!</p> <p>TIME-STAMPED SHOW NOTES:</p> <ul> <li>[00:25] Today\u2019s topic: How Spotify Acquired The Ringer.\u00a0\u00a0</li> <li>[00:42] The solid financial results for Spotify in Q4 of 2019.</li> <li>[00:56] How Spotify recognized exponential growth in podcast hours streamed.</li> <li>[01:24] Realizing that they needed to acquire a big podcast to double down on opportunities.\u00a0\u00a0\u00a0</li> <li>[01:53] The impressive retention rates of the Marketing School podcast.</li> <li>[02:09] Why Spotify\u2019s decision makes a lot of sense.\u00a0</li> <li>[02:39] Keep in mind that all good channels eventually become crowded.\u00a0\u00a0</li> <li>[03:09] Spotify\u2019s market share around podcasting and how they\u2019re more aggressive than Apple.\u00a0</li> <li>[03:48] The number of downloads The Ringer podcast is getting.\u00a0</li> <li>[04:07] Start comparing your Apple Podcast and Spotify analytics for your podcast.\u00a0</li> <li>[04:50] How our podcasts and Eric\u2019s own podcast are performing.\u00a0\u00a0</li> <li>[05:56] The proposed price for The Ringer stated by Bill Simmons: $100 million.\u00a0</li> <li>[06:25] That\u2019s it for today!</li> <li>[06:26] To stay updated with events and learn more about our mastermind, go to the <a href= \"https://marketingschool.io/growth-accelerator-mastermind\"> Marketing School</a> site for more information.</li> </ul> <p>Links Mentioned in Today\u2019s Episode:</p> <ul> <li><a href=\"https://www.spotify.com/\">Spotify</a>\u00a0</li> <li><a href=\"https://www.theringer.com\">The Ringer</a></li> <li><a href=\"https://www.apple.com\">Apple</a></li> <li><a href= \"https://growtheverywhere.com/podcast-player/\">Leveling Up Podcast</a></li> <li><a href=\"https://twitter.com/BillSimmons?ref_src\">Bill Simmons on Twitter</a></li> </ul> <p>Leave Some Feedback:</p> <p>\u00a0</p> <ul> <li>What should we talk about next?\u00a0Please let us know in the comments below</li> </ul> <ul> <li>Did you enjoy this episode?\u00a0If so, please leave a short review.</li> </ul> <p>\u00a0</p> <p>Connect with Us:\u00a0</p> <ul> <li style=\"font-weight: 400;\"><a href= \"http://neilpatel.com\">Neilpatel.com</a></li> <li style=\"font-weight: 400;\"><a href= \"https://www.quicksprout.com/\">Quick Sprout</a>\u00a0</li> <li style=\"font-weight: 400;\"><a href= \"https://growtheverywhere.com/\">Growth Everywhere</a></li> <li style=\"font-weight: 400;\"><a href= \"https://www.singlegrain.com/\">Single Grain</a></li> <li style=\"font-weight: 400;\"><a href= \"https://twitter.com/neilpatel\">Twitter @neilpatel</a>\u00a0</li> <li style=\"font-weight: 400;\"><a href= \"https://twitter.com/ericosiu\">Twitter @ericosiu</a></li> </ul>",
        "pub_date_ms": 1582812000575,
        "guid_from_rss": "bf073240-9680-42e7-89aa-82a2338840dc",
        "listennotes_url": "https://www.listennotes.com/e/dbd3d477dfc94128982b79e8152301b4/",
        "audio_length_sec": 434,
        "explicit_content": false,
        "maybe_audio_invalid": false,
        "listennotes_edit_url": "https://www.listennotes.com/e/dbd3d477dfc94128982b79e8152301b4/#edit"
      },
      "type": "episode",
      "notes": "",
      "added_at_ms": 1582824661788
    },
    {
      "id": 337223,
      "data": {
        "id": "5b8b9d5851ad4634812798d25553d8d7",
        "link": "https://www.vox.com/recode-media-podcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/5b8b9d5851ad4634812798d25553d8d7/",
        "image": "https://production.listennotes.com/podcasts/recode-media-recode-h9zPK_1UkdB-1iPwTajLXlS.1400x1400.jpg",
        "title": "Spotify, The Ringer and the future of podcasts",
        "podcast": {
          "id": "2aba49dc3fc04e3e96fe89f79a261798",
          "image": "https://production.listennotes.com/podcasts/recode-media-recode-h9zPK_1UkdB-1iPwTajLXlS.1400x1400.jpg",
          "title": "Recode Media",
          "publisher": "Recode",
          "thumbnail": "https://production.listennotes.com/podcasts/recode-media-recode-eHTVnkiXyu9-1iPwTajLXlS.300x300.jpg",
          "listen_score": 55,
          "listennotes_url": "https://www.listennotes.com/c/2aba49dc3fc04e3e96fe89f79a261798/",
          "listen_score_global_rank": "0.5%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/recode-media-recode-eHTVnkiXyu9-1iPwTajLXlS.300x300.jpg",
        "description": "<p>Spotify is buying Bill Simmons\u2019 sports and pop culture website and podcast network, The Ringer. It\u2019s Spotify\u2019s fourth podcast acquisition in a year. Recode\u2019s Peter Kafka (who broke the story) sits down with Vox Media Podcast Network producer and former Ringer staff member Zach Mack to discuss what this deal means for Spotify, The Ringer and the future of podcasts.</p><p><br></p><p><strong>Featuring</strong>: Zach Mack (<a href=\"https://twitter.com/zachthemack\">@zachthemack</a>), Senior Podcast Producer at Vox Media Podcast Network</p><p><strong>Host</strong>: Peter Kafka\u00a0(<a href=\"https://twitter.com/pkafka\">@pkafka</a>), Senior Editor at Recode</p><p><strong>More to explore</strong>: <a href=\"https://pod.link/1080467174\">Subscribe for free to Recode Media</a>, Peter Kafka, one of the media industry's most acclaimed reporters, talks to business titans, journalists, comedians, and more to get their take on today's media landscape.</p><p><strong>About Recode by Vox</strong>: Recode by Vox helps you understand how tech is changing the world \u2014 and changing us.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
        "pub_date_ms": 1581021870102,
        "guid_from_rss": "984d87fe-491d-11ea-a150-ab286b86e563",
        "listennotes_url": "https://www.listennotes.com/e/5b8b9d5851ad4634812798d25553d8d7/",
        "audio_length_sec": 1216,
        "explicit_content": false,
        "maybe_audio_invalid": false,
        "listennotes_edit_url": "https://www.listennotes.com/e/5b8b9d5851ad4634812798d25553d8d7/#edit"
      },
      "type": "episode",
      "notes": "",
      "added_at_ms": 1581032059508
    },
    {
      "id": 312262,
      "data": {
        "id": "eaa81f7bba344ae78bcf228b88e102a7",
        "link": "https://a16z.simplecast.com/episodes/a16z-podcast-how-what-why-500th-episode-behind-the-scenes-XgOK8aBT?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/eaa81f7bba344ae78bcf228b88e102a7/",
        "image": "https://production.listennotes.com/podcasts/a16z-podcast-andreessen-horowitz-sBmS7T_86qH-IWF2alEr-9h.1400x1400.jpg",
        "title": "How We Podcast",
        "podcast": {
          "id": "7c20388d8d7e45d6ae4b770c1fe36b6f",
          "image": "https://production.listennotes.com/podcasts/a16z-podcast-andreessen-horowitz-sBmS7T_86qH-IWF2alEr-9h.1400x1400.jpg",
          "title": "a16z Podcast",
          "publisher": "Andreessen Horowitz",
          "thumbnail": "https://production.listennotes.com/podcasts/a16z-podcast-andreessen-horowitz-3bPEYm06XuR-IWF2alEr-9h.300x300.jpg",
          "listen_score": 62,
          "listennotes_url": "https://www.listennotes.com/c/7c20388d8d7e45d6ae4b770c1fe36b6f/",
          "listen_score_global_rank": "0.1%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/a16z-podcast-andreessen-horowitz-3bPEYm06XuR-IWF2alEr-9h.300x300.jpg",
        "description": "<p>\"Hi everyone, welcome to the a16z Podcast...\" ... and welcome to our 500th episode, where, for the first time, we reveal behind-the-scenes details and the backstory of how we built this show, and the broader editorial operation. [You can also listen to episode 499, with head of marketing Margit Wennmachers, on building the a16z brand, <a href=\"https://a16z.com/2019/11/20/brand-building-a16z-ideas-people-marketing/\" target=\"_blank\">here</a>.]</p><p>We've talked a lot about the podcasting industry, and even done podcasts about podcasting, so for this special episode, editor-in-chief and showrunner Sonal Chokshi reveals the how, what, and why in conversation with a16z general partner (and guest-host for this special episode) <a href=\"https://a16z.com/2019/10/01/knowable-audio-startups/\" target=\"_blank\">podcasting</a> fan Connie Chan. We also answer some frequently asked questions that we often get (and recently <a href=\"https://twitter.com/smc90/status/1198026729421324289\" target=\"_blank\">got</a> via Twitter), such as:</p><ul><li>how we program podcasts</li><li>what's the process, from ideas to publishing</li><li>do we edit them and how!</li><li>do guests prep, do we have a script</li><li>technical stack</li></ul><p>...and much more. In fact, much of the conversation goes beyond the a16z Podcast and towards Sonal's broader principles of 'editorial content marketing', which hopefully helps those thinking about their own content operations and podcasts, too. Including where podcasting may be going.</p><p>Finally, we share some unexpected moments, and lessons learned along the way; our positions on \"tics\", swear-words, and talking too fast; failed experiments, and new directions. But most importantly, we share some of the people behind the scenes who help make the a16z Podcast what it was, is, and can be... with thanks most of all to *you*, our wonderful fans!</p>",
        "pub_date_ms": 1574838000136,
        "guid_from_rss": "2307c44b-8b88-4348-b4f5-3deaa204135e",
        "listennotes_url": "https://www.listennotes.com/e/eaa81f7bba344ae78bcf228b88e102a7/",
        "audio_length_sec": 2860,
        "explicit_content": false,
        "maybe_audio_invalid": false,
        "listennotes_edit_url": "https://www.listennotes.com/e/eaa81f7bba344ae78bcf228b88e102a7/#edit"
      },
      "type": "episode",
      "notes": "",
      "added_at_ms": 1574917254490
    },
    {
      "id": 312259,
      "data": {
        "id": "1ca5d330311d4808a4dbc668680f565b",
        "link": "https://snacks.robinhood.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/1ca5d330311d4808a4dbc668680f565b/",
        "image": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-F_0RTie7PzG-kmx0XIZTAys.1400x1400.jpg",
        "title": "*Live* at Spotify - Part II: Why Spotify is doing podcasts \u2014 Our interview with Max Cutler,  Founder & MD of podcasts at Spotify",
        "podcast": {
          "id": "c5ce6c02cbf1486496206829f7d42e8e",
          "image": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-F_0RTie7PzG-kmx0XIZTAys.1400x1400.jpg",
          "title": "Snacks Daily",
          "publisher": "Robinhood Financial, LLC",
          "thumbnail": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-Yp5jkwN1GKi-kmx0XIZTAys.300x300.jpg",
          "listen_score": 72,
          "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
          "listen_score_global_rank": "0.05%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-Yp5jkwN1GKi-kmx0XIZTAys.300x300.jpg",
        "description": "<p>The 2nd half of our Snacks recording live from Spotify. We sit down with Max Cutler, the Founder &amp; MD of Parcast Studios at Spotify \u2014 his startup was acquired by Spotify earlier this year. We\u2019re asking about how he first pitched his company, whether podcasts will follow the Netflix strategy, and what his favorite pod is. Ever.</p><p><br></p><p><br></p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
        "pub_date_ms": 1574852400438,
        "guid_from_rss": "b1210966-10a8-11ea-a5b5-6fb6124a64cd",
        "listennotes_url": "https://www.listennotes.com/e/1ca5d330311d4808a4dbc668680f565b/",
        "audio_length_sec": 1020,
        "explicit_content": false,
        "maybe_audio_invalid": false,
        "listennotes_edit_url": "https://www.listennotes.com/e/1ca5d330311d4808a4dbc668680f565b/#edit"
      },
      "type": "episode",
      "notes": "",
      "added_at_ms": 1574917188846
    },
    {
      "id": 310664,
      "data": {
        "id": "df11c9fde8234140a705c4aedff2561e",
        "link": "https://snacks.robinhood.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/df11c9fde8234140a705c4aedff2561e/",
        "image": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-F_0RTie7PzG-kmx0XIZTAys.1400x1400.jpg",
        "title": "*Live* at Spotify - Part I: How we build this (every day)",
        "podcast": {
          "id": "c5ce6c02cbf1486496206829f7d42e8e",
          "image": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-F_0RTie7PzG-kmx0XIZTAys.1400x1400.jpg",
          "title": "Snacks Daily",
          "publisher": "Robinhood Financial, LLC",
          "thumbnail": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-Yp5jkwN1GKi-kmx0XIZTAys.300x300.jpg",
          "listen_score": 72,
          "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
          "listen_score_global_rank": "0.05%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-Yp5jkwN1GKi-kmx0XIZTAys.300x300.jpg",
        "description": "<p>Spotify invited us to their NYC offices to record a live podcast \u2014 it\u2019s a podcast about podcasts for our podcast listening Snackers. We introduce to the Snackers how we got into podcasting, how we built this podcast (every day), and the 5 ingredients for a podcast that people will actually listen to.\u00a0</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
        "pub_date_ms": 1574420400441,
        "guid_from_rss": "b1632e3a-0ccb-11ea-82ce-6fd47d59f86e",
        "listennotes_url": "https://www.listennotes.com/e/df11c9fde8234140a705c4aedff2561e/",
        "audio_length_sec": 1226,
        "explicit_content": false,
        "maybe_audio_invalid": false,
        "listennotes_edit_url": "https://www.listennotes.com/e/df11c9fde8234140a705c4aedff2561e/#edit"
      },
      "type": "episode",
      "notes": "",
      "added_at_ms": 1574445406609
    },
    {
      "id": 309738,
      "data": {
        "id": "756203eef51f488fa990fda9daa3c54b",
        "link": "https://product-hunt-radio.simplecast.com/episodes/the-future-of-podcasting-with-andrew-mason-trD3wUwe?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/756203eef51f488fa990fda9daa3c54b/",
        "image": "https://production.listennotes.com/podcasts/product-hunt-radio-product-hunt-GWVKjh-0kgs-4qPNklrZI93.1400x1400.jpg",
        "title": "The future of podcasting with Andrew Mason",
        "podcast": {
          "id": "40426582e3cd4dd2bf931f880e7374aa",
          "image": "https://production.listennotes.com/podcasts/product-hunt-radio-product-hunt-GWVKjh-0kgs-4qPNklrZI93.1400x1400.jpg",
          "title": "Product Hunt Radio",
          "publisher": "Product Hunt",
          "thumbnail": "https://production.listennotes.com/podcasts/product-hunt-radio-product-hunt--QOpzec69YV-4qPNklrZI93.300x300.jpg",
          "listen_score": 46,
          "listennotes_url": "https://www.listennotes.com/c/40426582e3cd4dd2bf931f880e7374aa/",
          "listen_score_global_rank": "1%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/product-hunt-radio-product-hunt--QOpzec69YV-4qPNklrZI93.300x300.jpg",
        "description": "<p>On this episode Abadesi talks to <a href=\"https://www.producthunt.com/@andrewmason\">Andrew Mason</a>, founder and CEO of <a href=\"https://www.producthunt.com/posts/descript-podcast-studio\">Descript</a>. He was formerly founder of Detour, which Descript emerged within before it was spun out into its own company when Bose bought the technology behind Detour. Andrew was also founder of Groupon.</p><p>In this episode they talk about...</p><h2>Descript\u2019s origin as part of Detour, and how to know when it\u2019s the right time to pivot from your original idea</h2><blockquote><p>\u201cWe would have been over-investing in Descript if all we were using it for was for Detour, but we knew there was a potential business there and were treating it like a kind of a backup plan when you\u2019re pre-product-market fit, like we were. You\u2019re staying open to different paths.\u201d</p></blockquote><p>Descript actually emerged as a part of Detour, the company Andrew founded to create local audio tours. The team built themselves a better workflow for editing audio and realized that the internal product they had created could be much larger than Detour itself. They also recognized that a confluence of factors in tech were going to allow them to create the next generation of audio editing tools. Andrew explains how he went through the process of figuring out when to \u201ccut bait\u201d on Detour. He previously had pivoted The Point into Groupon, so he has some insightful things to say about when and how to pivot.</p><blockquote><p>\u201cWe tried every last possible approach that we could think of and eventually it was like, it\u2019s not supposed to be this hard. Having been through this before, it felt like we were doing the most elaborate things to market the product and reach customers, and at some point it just clicked that it\u2019s not supposed to be this hard and we should move on.\u201d</p></blockquote><h2>Andrew\u2019s advice on managing people and scaling a company</h2><blockquote><p>\u201cIn a lot of companies the way that people get into management is they'll be individual contributors who have great ideas and nobody wants to listen to their ideas because it's the people in management that get to have those conversations. So people say 'okay, I guess I'll become a manager' and then they become a manager for completely the wrong reasons \u2014 not because they care about people or unlocking the best possible incarnation of their teams, but because they care about having their ideas listened to.\u201d</p></blockquote><p>He gives a rundown of the history of the company and where they are at now, after having raised a large Series A round and made the acquisition of Lyrebird. He talks about what the next stage of growth will hold for them, and how he is managing the scaling process by putting into place processes and protocols that will provide structure for the company as it grows. He also talks about the importance of delegating the work that the founder has been doing in a growing company.</p><h2>Personal development as a leader and helping your team grow</h2><p>Andrew explains what a typical day looks like for the team at Descript. He explains how they manage internal tools and how he tries to create an environment where feedback can flow freely among the team members. He talks about some of the best ways to grow as a leader, including some of the events that he attends and why he reads a lot. He also says that they have created an internal podcast for the team, a cool idea which you might expect from the company given what Descript is typically used for!</p><p>Andrew also tells us about one of his favorite products that he uses to build tools for the team.</p><p>We\u2019ll be back next week so be sure to subscribe on <a href=\"https://itunes.apple.com/podcast/product-hunt-radio/id862714883\">Apple Podcasts</a>, <a href=\"https://www.google.com/podcasts?feed=aHR0cHM6Ly9yc3Muc2ltcGxlY2FzdC5jb20vcG9kY2FzdHMvNjI2MS9yc3M%3D\">Google Podcasts</a>, <a href=\"https://open.spotify.com/show/4Ak6HpbVkLKGacY3E0GHL8?si=N8xXCfscQPapPSFIF2rP3w\">Spotify</a>, <a href=\"https://www.breaker.audio/product-hunt\">Breaker</a>, <a href=\"https://overcast.fm/itunes862714883/product-hunt-radio\">Overcast</a>, or wherever you listen to your favorite podcasts. \ud83d\ude38</p><h3>Companies and Products Mentioned In This Episode</h3><p><a href=\"https://www.producthunt.com/posts/retool-2\">Retool</a> \u2014 Customized internal tools in minutes.</p>",
        "pub_date_ms": 1574226009020,
        "guid_from_rss": "30b4169f-c117-4530-b416-e057e16c3f30",
        "listennotes_url": "https://www.listennotes.com/e/756203eef51f488fa990fda9daa3c54b/",
        "audio_length_sec": 1816,
        "explicit_content": false,
        "maybe_audio_invalid": false,
        "listennotes_edit_url": "https://www.listennotes.com/e/756203eef51f488fa990fda9daa3c54b/#edit"
      },
      "type": "episode",
      "notes": "",
      "added_at_ms": 1574273649602
    },
    {
      "id": 294620,
      "data": {
        "id": "44017cd438a24139a913a3e288a518fe",
        "link": "http://demandgenradio.com/e/129-how-to-build-your-brand-with-podcasting/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/44017cd438a24139a913a3e288a518fe/",
        "image": "https://production.listennotes.com/podcasts/demandgen-radio-demandgen-international-inc-XCuYoBd-czH-oVByO3tuFwR.1400x1400.jpg",
        "title": "#129 How to Build your Brand with Podcasting",
        "podcast": {
          "id": "f446a0eaac2e481991e36467e4a4f96f",
          "image": "https://production.listennotes.com/podcasts/demandgen-radio-demandgen-international-inc-XCuYoBd-czH-oVByO3tuFwR.1400x1400.jpg",
          "title": "DemandGen Radio",
          "publisher": "DemandGen International, Inc.",
          "thumbnail": "https://production.listennotes.com/podcasts/demandgen-radio-demandgen-international-inc-ugejYpvaH7O-oVByO3tuFwR.300x300.jpg",
          "listen_score": 37,
          "listennotes_url": "https://www.listennotes.com/c/f446a0eaac2e481991e36467e4a4f96f/",
          "listen_score_global_rank": "2.5%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/demandgen-radio-demandgen-international-inc-ugejYpvaH7O-oVByO3tuFwR.300x300.jpg",
        "description": "<p></p>\n\n<p>Jordan Paris is a 21-year-old entrepreneur who runs a wildly successful podcast. In this episode, he shares how and why he started his podcast and how podcasting propelled the growth of his business and personal brand. Tune in as Jordan shares how he remains so driven and accomplished at an early age, what lessons he\u2019s learned from starting his podcast, and how you can benefit from starting your own podcast.</p>",
        "pub_date_ms": 1569146400097,
        "guid_from_rss": "demandgen.podbean.com/129-how-to-build-your-brand-with-podcasting-b3619189abc76e1d857a35d5ff3062d9",
        "listennotes_url": "https://www.listennotes.com/e/44017cd438a24139a913a3e288a518fe/",
        "audio_length_sec": 2329,
        "explicit_content": false,
        "maybe_audio_invalid": false,
        "listennotes_edit_url": "https://www.listennotes.com/e/44017cd438a24139a913a3e288a518fe/#edit"
      },
      "type": "episode",
      "notes": "",
      "added_at_ms": 1570177564050
    },
    {
      "id": 293809,
      "data": {
        "id": "9df23a4053c940fa8762cc94d08c4836",
        "link": "https://hbr.org/podcast/2019/10/can-gimlet-turn-a-podcast-network-into-a-disruptive-platform?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/9df23a4053c940fa8762cc94d08c4836/",
        "image": "https://production.listennotes.com/podcasts/cold-call-hbr-presents-brian-kenny-UepvPhNmMFV-sC2kfX7gM0D.1400x1400.jpg",
        "title": "Can Gimlet Turn a Podcast Network Into a Disruptive Platform?",
        "podcast": {
          "id": "841eca7a25c64420b2bd0b536d35108d",
          "image": "https://production.listennotes.com/podcasts/cold-call-hbr-presents-brian-kenny-UepvPhNmMFV-sC2kfX7gM0D.1400x1400.jpg",
          "title": "Cold Call",
          "publisher": "HBR Presents / Brian Kenny",
          "thumbnail": "https://production.listennotes.com/podcasts/cold-call-hbr-presents-brian-kenny-egRtK2b1Odo-sC2kfX7gM0D.300x300.jpg",
          "listen_score": 48,
          "listennotes_url": "https://www.listennotes.com/c/841eca7a25c64420b2bd0b536d35108d/",
          "listen_score_global_rank": "1%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/cold-call-hbr-presents-brian-kenny-egRtK2b1Odo-sC2kfX7gM0D.300x300.jpg",
        "description": "<p>Harvard Business School professors <strong><a href=\"https://www.hbs.edu/faculty/Pages/profile.aspx?facId=6446\" target=\"_blank\" rel=\"noopener\">John Deighton</a></strong> and <strong><a href=\"https://www.hbs.edu/faculty/Pages/profile.aspx?facId=6536\" target=\"_blank\" rel=\"noopener\">Jeffrey Rayport</a></strong> discuss their case, &#8220;<a href=\"https://store.hbr.org/product/gimlet-media-a-podcasting-startup/918413?sku=918413-PDF-ENG\" target=\"_blank\" rel=\"noopener\">Gimlet Media: A Podcasting Startup</a>,&#8221; and how two former public radio producers launch a podcast network, entering the last frontier of digital media. Can they turn a content supplier into a disruptive platform?</p>",
        "pub_date_ms": 1569948476053,
        "guid_from_rss": "tag:audio.hbr.org,2016-09-16:cold-call.0104",
        "listennotes_url": "https://www.listennotes.com/e/9df23a4053c940fa8762cc94d08c4836/",
        "audio_length_sec": 1584,
        "explicit_content": false,
        "maybe_audio_invalid": false,
        "listennotes_edit_url": "https://www.listennotes.com/e/9df23a4053c940fa8762cc94d08c4836/#edit"
      },
      "type": "episode",
      "notes": "",
      "added_at_ms": 1569971844390
    },
    {
      "id": 274212,
      "data": {
        "id": "00d8c43df3f94eb7b409135fcba6a083",
        "link": "https://glitch.com/culture/function-episode-6/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/00d8c43df3f94eb7b409135fcba6a083/",
        "image": "https://production.listennotes.com/episode/image/e816164a99cb4339bb248b7218d8c9d5.jpg",
        "title": "The Wild World of Podcast Ads",
        "podcast": {
          "id": "3b7c6c851ec14f40bb062b918942aa15",
          "image": "https://production.listennotes.com/podcasts/function-with-anil-dash-vox-media-3DjNoAIGtV_-pfqIzGD4odn.1400x1400.jpg",
          "title": "Function with Anil Dash",
          "publisher": "Vox Media",
          "thumbnail": "https://production.listennotes.com/podcasts/function-with-anil-dash-vox-media-yYP_8KQFk06-pfqIzGD4odn.300x300.jpg",
          "listen_score": 45,
          "listennotes_url": "https://www.listennotes.com/c/3b7c6c851ec14f40bb062b918942aa15/",
          "listen_score_global_rank": "1%"
        },
        "thumbnail": "https://production.listennotes.com/episode/image/c76197bdbdc4438e85fc13a05637a420.jpg",
        "description": "<p>Squarespace. Mailchimp. Casper. Blue Apron. If you're a regular podcast listener, then there's no doubt you've heard ads from these companies, among many others. Podcasting's reach has grown exponentially over the past few years, and companies like these are spending millions of dollars to reach listeners whenever, wherever and however they tune in. But is this truly effective? What type of ads work best? And if you're not a podcast from a big media organization, how can\u00a0<em>you</em>\u00a0can get a piece of the pie?</p><p>This week on Function, we examine the world of podcast advertising. Anil sits down with\u00a0<strong>Francesco Baschieri</strong>, president of Voxnest, and talks about some of the trends and technology behind podcast ads. We also hear from New York City podcasting duo\u00a0<strong>Jade + XD</strong>\u00a0and pull back the curtain on advertising and monetization from an independent media perspective.</p><p>How does podcast advertising stay ahead of tech like adblockers? What happens when an ad is automatically placed in your podcast by the network that goes against both the host and the audience? You'll find out the answers to all this and more on this week's episode!</p><p>But first, a word from our sponsors....</p><p><strong>Guests</strong></p><ul>\n<li><a href=\"https://twitter.com/thebask\">Francesco Baschieri</a></li>\n<li><a href=\"https://twitter.com/JadeAndXD\">Jade + XD</a></li>\n</ul><p></p><p><strong>Other Links</strong></p><ul>\n<li><a href=\"https://voxnest.com/\">Voxnest</a></li>\n<li><a href=\"https://jadeandxd.com/\">Jade + XD's Website</a></li>\n<li>\n<a href=\"https://blog.voxnest.com/dynamic-ad-insertion-what-it-is-why-use-it/\"><em>Dynamic Ad Insertion \u2014 What it is and Why You Should Be Utilising It</em></a>\u00a0(Voxnest)</li>\n<li>\n<a href=\"https://stratechery.com/2017/podcasts-analytics-and-centralization/\"><em>Podcasts, Analytics, and Centralization</em></a>\u00a0(Stratechery)</li>\n<li>\n<a href=\"https://fivethirtyeight.com/features/but-first-a-word-from-100-podcast-sponsors/\"><em>But First, A Word From 100 Podcasts' Sponsors</em></a>\u00a0(FiveThirtyEight)</li>\n</ul><p></p>",
        "pub_date_ms": 1543834800017,
        "guid_from_rss": "gid://art19-episode-locator/V0/3NB2Qv5duR9Q5DGswnGa7R31to3M60gmiXhPD6Ou1Fk",
        "listennotes_url": "https://www.listennotes.com/e/00d8c43df3f94eb7b409135fcba6a083/",
        "audio_length_sec": 3338,
        "explicit_content": false,
        "maybe_audio_invalid": false,
        "listennotes_edit_url": "https://www.listennotes.com/e/00d8c43df3f94eb7b409135fcba6a083/#edit"
      },
      "type": "episode",
      "notes": "",
      "added_at_ms": 1565460047367
    },
    {
      "id": 270587,
      "data": {
        "id": "89765fa2bee24603a93b4098830c4efa",
        "link": "https://shows.acast.com/g/episodes/6105626a7c2a82001a79b7e8?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/89765fa2bee24603a93b4098830c4efa/",
        "image": "https://production.listennotes.com/podcasts/chinatalk/learning-to-listen-chinas-zbHvEJsnqZ2-LoO0UAa_G4e.1400x1400.jpg",
        "title": "Learning to listen: China's billion-dollar podcast industry",
        "podcast": {
          "id": "5cd3fe3fc0c04c8da9abf4a6fb897a31",
          "image": "https://production.listennotes.com/podcasts/chinatalk-jordan-schneider-_O9VLEIa6tx-Jz4DAyqm9ZV.1400x1400.jpg",
          "title": "ChinaTalk",
          "publisher": "Jordan Schneider",
          "thumbnail": "https://production.listennotes.com/podcasts/chinatalk-jordan-schneider-grzPNnKBX3i-Jz4DAyqm9ZV.300x300.jpg",
          "listen_score": 37,
          "listennotes_url": "https://www.listennotes.com/c/5cd3fe3fc0c04c8da9abf4a6fb897a31/",
          "listen_score_global_rank": "2.5%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/chinatalk/learning-to-listen-chinas-EZGSUdgywHp-LoO0UAa_G4e.300x300.jpg",
        "description": "While it may be a pipe dream for ChinaEconTalk to ever merit a billion-dollar price tag, in China, podcast \u201cunicorns\u201d are everywhere. Companies like Ximalaya and Yudao have multibillion-dollar valuations, but feature startlingly different content from what consumers expect in the West. What drives these differences, and what does the future hold for spoken audio in China? To answer these questions, Yi Yang, a young podcast host and founder of the Mandarin-language podcast startup JustPod \u64ad\u5ba2\u4e00\u4e0b, joins Jordan to explain how, after the advent of podcasts in China, people are finally \u201clearning to listen.\u201d Yi Yang's original podcast is called LeftRight\u00a0\u5ffd\u5de6\u5ffd\u53f3. His two branded podcasts are\u00a0Startup Insider\u00a0\u521b\u4e1a\u5185\u5e55 and Bessie\u2019s Notes\u00a0\u8d1d\u671b\u5f55. ChinaEconTalk's newsletter is dope. Sign up here at\u00a0www.chinaecontalk.substack.com. The latest issues include an analysis of why Amazon lost in China and learn about the bane of China\u2019s automobile industry. <a target='_blank' rel='noopener noreferrer' href=\"https://open.acast.com/public/patreon/fanSubscribe/1959352\">Get bonus content on Patreon</a><br /><hr><p style='color:grey; font-size:0.75em;'> See <a style='color:grey;' target='_blank' rel='noopener noreferrer' href='https://acast.com/privacy'>acast.com/privacy</a> for privacy and opt-out information.</p>",
        "pub_date_ms": 1562795773124,
        "guid_from_rss": "807301962fd14ffdbd8392824f6f1e5f",
        "listennotes_url": "https://www.listennotes.com/e/89765fa2bee24603a93b4098830c4efa/",
        "audio_length_sec": 2909,
        "explicit_content": false,
        "maybe_audio_invalid": false,
        "listennotes_edit_url": "https://www.listennotes.com/e/89765fa2bee24603a93b4098830c4efa/#edit"
      },
      "type": "episode",
      "notes": "",
      "added_at_ms": 1564614350360
    },
    {
      "id": 263794,
      "data": {
        "id": "3e4b4e2bfa32403ab90bf7f8d3db1329",
        "link": "http://acquired.libsyn.com/season-2-episode-6spotifys-direct-listing?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/3e4b4e2bfa32403ab90bf7f8d3db1329/",
        "image": "https://production.listennotes.com/episode/image/96fb8e1ea1ba4d69ab5164c6d0499003.jpg",
        "title": "Season 2, Episode 6:\u00a0Spotify\u2019s Direct Listing",
        "podcast": {
          "id": "50d02b7d32b246a5a6b43e3ca1676657",
          "image": "https://production.listennotes.com/podcasts/acquired-ben-gilbert-and-david-rosenthal-QGBvwyLxDCe-9pne_5jCY2u.1400x1400.jpg",
          "title": "Acquired",
          "publisher": "Ben Gilbert and David Rosenthal",
          "thumbnail": "https://production.listennotes.com/podcasts/acquired-ben-gilbert-and-david-rosenthal-FAHOSj_1WC0-9pne_5jCY2u.300x300.jpg",
          "listen_score": 62,
          "listennotes_url": "https://www.listennotes.com/c/50d02b7d32b246a5a6b43e3ca1676657/",
          "listen_score_global_rank": "0.1%"
        },
        "thumbnail": "https://production.listennotes.com/episode/image/6dc6933a8143463a89449a846cfe0c24.jpg",
        "description": "<p>Join the Acquired Limited Partner program! <a href= \"https://kimberlite.fm/acquired/\">https://kimberlite.fm/acquired/</a> (works best on mobile)</p> <p>Acquired wraps up a big few weeks of coverage with not an IPO or an M&A or a fundraising round, but what\u2019s still the largest tech exit in recent memory: Spotify\u2019s $30B direct public listing. We dive into what it all means and how we got here: from Napster to iTunes to Facebook (and even some Justin Timberlake thrown in for good measure). Acquired FM is on the scene and spinning all the hits from this new wave music industry titan!\u00a0</p> <p>\u00a0</p> <p><em>Note: We incorrectly described Spotify CEO Daniel Ek\u2019s ownership stake in Spotify as 25%+; that is actually his voting control. His economic ownership is 9.3%, and cofounder Martin Lorentzon\u2019s is 12.4%. We apologize for the error!</em></p> <p>\u00a0</p> <p>Links:</p> <ul> <li><a href= \"http://www.internethistorypodcast.com/2017/04/the-napster-story-with-jordan-ritter/\"> Internet History Podcast on the Napster Story with Jordan Ritter</a></li> <li><a href= \"https://www.scribd.com/doc/67465758/Sean-Parker-s-Email-to-Spotify-s-Daniel-Ek\"> Sean Parker\u2019s email to Daniel Ek</a></li> </ul> <p>\u00a0</p> <p>Carve Outs:</p> <ul> <li>Ben: <a href=\"http://www.imdb.com/title/tt1825683/\">Black Panther</a> (and <a href= \"https://open.spotify.com/user/g0u1d1e1/playlist/4Vaus6GcI1TAMGmepUK3WO\"> soundtrack on Spotify</a>!)</li> <li>David: <a href=\"https://www.sfballet.org/boundless\">\u201cSilicon Ballet\u201d panel at San Francisco Ballet on Saturday, April 28</a></li> </ul> <p>\u00a0</p> <p>Sponsor:</p> <ul> <li>Thanks to <a href=\"https://www.perkinscoie.com/\">Perkins Coie</a>, Counsel to Great Companies, for sponsoring Acquired Season 2. You can get in touch with Lee Schindler, who you heard at the beginning of this podcast, <a href= \"https://www.perkinscoie.com/en/professionals/r-lee-schindler.html\"> here</a>.</li> </ul>",
        "pub_date_ms": 1522992660081,
        "guid_from_rss": "3f987c8a5468b2a8806dc70282791593",
        "listennotes_url": "https://www.listennotes.com/e/3e4b4e2bfa32403ab90bf7f8d3db1329/",
        "audio_length_sec": 6278,
        "explicit_content": false,
        "maybe_audio_invalid": false,
        "listennotes_edit_url": "https://www.listennotes.com/e/3e4b4e2bfa32403ab90bf7f8d3db1329/#edit"
      },
      "type": "episode",
      "notes": "",
      "added_at_ms": 1563257445808
    },
    {
      "id": 263793,
      "data": {
        "id": "aa929f517e4643c58249936a0e1dcdc2",
        "link": "https://www.theverge.com/the-vergecast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/aa929f517e4643c58249936a0e1dcdc2/",
        "image": "https://production.listennotes.com/podcasts/the-vergecast-the-verge-R-59MH_ksW6-n6zR1v83Ejt.1400x1400.jpg",
        "title": "Spotify\u2019s big audio play, plus a Palm tiny phone review",
        "podcast": {
          "id": "cfeaa7a758a94e069ba087f323ffa225",
          "image": "https://production.listennotes.com/podcasts/the-vergecast-the-verge-R-59MH_ksW6-n6zR1v83Ejt.1400x1400.jpg",
          "title": "The Vergecast",
          "publisher": "The Verge",
          "thumbnail": "https://production.listennotes.com/podcasts/the-vergecast-the-verge-YJnQVyw5j4L-n6zR1v83Ejt.300x300.jpg",
          "listen_score": 69,
          "listennotes_url": "https://www.listennotes.com/c/cfeaa7a758a94e069ba087f323ffa225/",
          "listen_score_global_rank": "0.05%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/the-vergecast-the-verge-YJnQVyw5j4L-n6zR1v83Ejt.300x300.jpg",
        "description": "<p>Spotify acquires Gimlet Media and Anchor in a play to further expand into audio beyond music streaming. Later, Nilay Patel, Dieter Bohn, and Paul Miller review the tiny new Palm phone, address Samsung Galaxy S10 rumors and finally, some Apple updates.</p><p>Links: </p><p>- <a href=\"https://www.theverge.com/2019/2/6/18213462/spotify-podcasts-gimlet-anchor-acquisition\">Spotify gets serious about podcasts with two acquisitions</p><p></a></p><p>- <a href=\"https://www.theverge.com/circuitbreaker/2019/2/6/18213597/samsung-galaxy-s10e-variant-smaller-screen-leak-name-pictures\">Latest leaks confirm cheaper and smaller Samsung Galaxy S10e</p><p></a></p><p>- <a href=\"https://www.theverge.com/2019/2/4/18210291/samsung-galaxy-s10-wifi-6-leak\">Samsung\u2019s Galaxy S10 will be one of the first Wi-Fi 6 phones</p><p></a></p><p>- <a href=\"https://www.theverge.com/2019/2/6/18213974/samsung-true-wireless-galaxy-buds-earphones-promotional-image-leak\">New Samsung true wireless earbuds appear in leaked promotional \u2026</p><p></a></p><p>- <a href=\"https://www.theverge.com/2019/2/4/18211261/samsung-galaxy-sport-leak-shows-a-sleek-bezel-less-smartwatch\">Samsung Galaxy Sport leak shows a sleek bezel-less smartwatch \u2026</p><p></a></p><p>- <a href=\"https://www.theverge.com/2019/2/6/18212311/palm-phone-review-time-well-spent-life-mode-lite-verizon\">Palm phone review: it won\u2019t save you from your phone</p><p></a></p><p>- <a href=\"https://www.theverge.com/2019/2/7/18203706/apple-ios-12-1-4-group-facetime-security-fix\">Apple releases iOS 12.1.4 to fix Group FaceTime security flaw</p><p></a></p><p>- <a href=\"https://www.theverge.com/2019/2/7/18215885/apple-group-facetime-security-bug-bounty-compensation\">Apple is compensating the 14-year-old who discovered major FaceTime security bug</p><p></a></p><p>- <a href=\"https://www.theverge.com/2019/2/5/18212657/apple-retail-chief-angela-ahrendts-leaving-replacement\">Apple retail chief Angela Ahrendts is leaving in April</p><p></a></p><p>- <a href=\"https://www.theverge.com/2019/2/4/18211044/apple-att-5g-e-network-icon-iphones-misleading-ios-software-update-beta\">Apple just endorsed AT&amp;T\u2019s fake 5G E network</p><p></a></p><p>- <a href=\"https://www.theverge.com/circuitbreaker/2019/2/4/18210866/belkin-ethernet-lightning-dongle-release-date-price-power\">Fine, here\u2019s a $100 Lightning to Ethernet dongle for iPads</p><p></a></p><p>- <a href=\"https://www.theverge.com/2019/2/7/18215639/net-neutrality-congress-hearing-energy-commerce-committee\">Net neutrality takes center stage at congressional hearing</p><p></a></p><p>Check out: <a href=\"http://www.azure.com/trial\">Azure.com/trial</a> to sign up for a trial today!</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
        "pub_date_ms": 1549623600247,
        "guid_from_rss": "fa873cfe-ff17-11e8-8004-eb3849e20cd6",
        "listennotes_url": "https://www.listennotes.com/e/aa929f517e4643c58249936a0e1dcdc2/",
        "audio_length_sec": 4322,
        "explicit_content": false,
        "maybe_audio_invalid": false,
        "listennotes_edit_url": "https://www.listennotes.com/e/aa929f517e4643c58249936a0e1dcdc2/#edit"
      },
      "type": "episode",
      "notes": "",
      "added_at_ms": 1563257433277
    }
  ],
  "total": 36,
  "thumbnail": "https://d3sv2eduhewoas.cloudfront.net/playlist/image/48477deae02649d7ab9d3f1b3966af38.JPEG",
  "visibility": "public",
  "description": "A curated playlist of podcasts by Wenbin Fang.",
  "listennotes_url": "https://www.listennotes.com/playlists/podcasts-about-podcasting-m1pe7z60bsw/episodes/",
  "last_timestamp_ms": 1563257433277
}
```   
</details>



<details>
  <summary>Click to see response schema</summary>
  
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "example": "m1pe7z60bsw",
      "description": "A 11-character playlist id."
    },
    "name": {
      "type": "string",
      "example": "My podcast playlist",
      "description": "Playlist name."
    },
    "type": {
      "enum": [
        "episode_list",
        "podcast_list"
      ],
      "type": "string",
      "example": "episode_list",
      "description": "The type of this playlist, which should be either **episode_list** or **podcast_list**.\n"
    },
    "image": {
      "type": "string",
      "example": "https://cdn-images-1.listennotes.com/playlist/image/6907e8ff6b6c45df94cc059753f369cc.JPEG",
      "description": "High resolution image url of the playlist."
    },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "example": 23,
            "description": "Playlist item id."
          },
          "data": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "string",
                    "example": "4d82e50314174754a3b603912448e812",
                    "description": "Episode id."
                  },
                  "link": {
                    "type": "string",
                    "example": "https://www.npr.org/2020/01/22/798532179/soleimanis-iran",
                    "description": "Web link of this episode."
                  },
                  "audio": {
                    "type": "string",
                    "example": "https://www.listennotes.com/e/p/11b34041e804491b9704d11f283c74de/",
                    "description": "Audio url of this episode, which can be played directly."
                  },
                  "image": {
                    "type": "string",
                    "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
                    "description": "Image url for this episode.\nIf an episode doesn't have its own image, then this field would be the url of the podcast artwork image.\nIf you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
                  },
                  "title": {
                    "type": "string",
                    "example": "Celebration Recap, Jason Fry and Christian Blauvelt Interviews \u2013 SWBW #101",
                    "description": "Episode name."
                  },
                  "podcast": {
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "string",
                        "example": "4d3fe717742d4963a85562e9f84d8c79",
                        "description": "Podcast id."
                      },
                      "image": {
                        "type": "string",
                        "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
                        "description": "Image url for this podcast's artwork. If you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
                      },
                      "title": {
                        "type": "string",
                        "example": "Star Wars 7x7 | Star Wars News, Interviews, and More!",
                        "description": "Podcast name."
                      },
                      "publisher": {
                        "type": "string",
                        "example": "Planet Broadcasting",
                        "description": "Podcast publisher name."
                      },
                      "thumbnail": {
                        "type": "string",
                        "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
                        "description": "Thumbnail image url for this podcast's artwork (300x300)."
                      },
                      "listen_score": {
                        "type": "integer",
                        "example": 81,
                        "description": "The estimated popularity score of a podcast compared to all other rss-based public podcasts in the world on a scale from 0 to 100.\nIf the score is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
                      },
                      "listennotes_url": {
                        "type": "string",
                        "example": "https://www.listennotes.com/c/4d3fe717742d4963a85562e9f84d8c79/",
                        "description": "The url of this podcast on [ListenNotes.com](https://www.ListenNotes.com)."
                      },
                      "listen_score_global_rank": {
                        "type": "string",
                        "example": "0.5%",
                        "description": "The estimated popularity ranking of a podcast compared to all other rss-based public podcasts in the world.\nFor example, if the value is 0.5%, then this podcast is one of the top 0.5% most popular shows out of all podcasts globally, ranked by Listen Score.\nIf the ranking is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
                      }
                    }
                  },
                  "thumbnail": {
                    "type": "string",
                    "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
                    "description": "Thumbnail image (300x300) url for this episode.\nIf an episode doesn't have its own image, then this field would be the url of the podcast artwork thumbnail image.\n"
                  },
                  "description": {
                    "type": "string",
                    "example": "<p>Disney chief Bob Iger shared news about Star Wars movies in 2020 and beyond, but some media outlets gave conflicting reports about it. Here's the real scoop. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>\n",
                    "description": "Html of this episode's full description"
                  },
                  "pub_date_ms": {
                    "type": "integer",
                    "example": 1474873200000,
                    "description": "Published date for this episode. In millisecond."
                  },
                  "listennotes_url": {
                    "type": "string",
                    "example": "https://www.listennotes.com/e/4d82e50314174754a3b603912448e812/",
                    "description": "The url of this episode on [ListenNotes.com](https://www.ListenNotes.com)."
                  },
                  "audio_length_sec": {
                    "type": "integer",
                    "example": 567,
                    "description": "Audio length of this episode. In seconds."
                  },
                  "explicit_content": {
                    "type": "boolean",
                    "example": false,
                    "description": "Whether this podcast contains explicit language."
                  },
                  "maybe_audio_invalid": {
                    "type": "boolean",
                    "example": false,
                    "description": "Whether or not this episode's audio is invalid. Podcasters may delete the original audio."
                  },
                  "listennotes_edit_url": {
                    "type": "string",
                    "example": "https://www.listennotes.com/e/11b34041e804491b9704d11f283c74de/#edit",
                    "description": "Edit url of this episode where you can update the audio url if you find the audio is broken."
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "string",
                    "example": "4d3fe717742d4963a85562e9f84d8c79",
                    "description": "Podcast id."
                  },
                  "rss": {
                    "type": "string",
                    "example": "https://sw7x7.libsyn.com/rss",
                    "description": "RSS url of this podcast. This field is available only in the PRO/ENTERPRISE plan."
                  },
                  "type": {
                    "enum": [
                      "episodic",
                      "serial"
                    ],
                    "type": "string",
                    "example": "episodic",
                    "description": "The type of this podcast - episodic or serial."
                  },
                  "email": {
                    "type": "string",
                    "example": "hello@example.com",
                    "description": "The email of this podcast's producer. This field is available only in the PRO/ENTERPRISE plan."
                  },
                  "extra": {
                    "type": "object",
                    "properties": {
                      "url1": {
                        "type": "string",
                        "description": "Url affiliated with this podcast"
                      },
                      "url2": {
                        "type": "string",
                        "description": "Url affiliated with this podcast"
                      },
                      "url3": {
                        "type": "string",
                        "description": "Url affiliated with this podcast"
                      },
                      "google_url": {
                        "type": "string",
                        "example": "https://play.google.com/music/listen?u=0#/ps/I7gdcrqcmvhfnhh2cyqkcg32tkq",
                        "description": "Google Podcasts url for this podcast"
                      },
                      "spotify_url": {
                        "type": "string",
                        "example": "https://open.spotify.com/show/2rQJUP9Y3HxemiW3JHt9WV",
                        "description": "Spotify url for this podcast"
                      },
                      "youtube_url": {
                        "type": "string",
                        "example": "https://www.youtube.com/sw7x7",
                        "description": "YouTube url affiliated with this podcast"
                      },
                      "linkedin_url": {
                        "type": "string",
                        "description": "LinkedIn url affiliated with this podcast"
                      },
                      "wechat_handle": {
                        "type": "string",
                        "description": "WeChat username affiliated with this podcast"
                      },
                      "patreon_handle": {
                        "type": "string",
                        "example": "sw7x7",
                        "description": "Patreon username affiliated with this podcast"
                      },
                      "twitter_handle": {
                        "type": "string",
                        "example": "SW7x7podcast",
                        "description": "Twitter username affiliated with this podcast"
                      },
                      "facebook_handle": {
                        "type": "string",
                        "example": "sw7x7",
                        "description": "Facebook username affiliated with this podcast"
                      },
                      "instagram_handle": {
                        "type": "string",
                        "example": "sw7x7",
                        "description": "Instagram username affiliated with this podcast"
                      }
                    }
                  },
                  "image": {
                    "type": "string",
                    "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.1400x1400.jpg",
                    "description": "Image url for this podcast's artwork. If you are using PRO/ENTERPRISE plan, then it's\na high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**,\nlow resolution image (300x300).\n"
                  },
                  "title": {
                    "type": "string",
                    "example": "Star Wars 7x7 | Star Wars News, Interviews, and More!",
                    "description": "Podcast name."
                  },
                  "country": {
                    "type": "string",
                    "example": "United States",
                    "description": "The country where this podcast is produced."
                  },
                  "website": {
                    "type": "string",
                    "example": "http://sw7x7.com/",
                    "description": "Website url of this podcast."
                  },
                  "language": {
                    "type": "string",
                    "example": "English",
                    "description": "The language of this podcast. You can get all supported languages from `GET /languages`."
                  },
                  "genre_ids": {
                    "type": "array",
                    "items": {
                      "type": "integer",
                      "description": "Genre ids."
                    },
                    "example": [
                      138,
                      86,
                      160,
                      68,
                      82,
                      100,
                      101
                    ]
                  },
                  "itunes_id": {
                    "type": "integer",
                    "example": 896354638,
                    "description": "iTunes id for this podcast."
                  },
                  "publisher": {
                    "type": "string",
                    "example": "Planet Broadcasting",
                    "description": "Podcast publisher name."
                  },
                  "thumbnail": {
                    "type": "string",
                    "example": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-OaJSjb4xQv3.300x300.jpg",
                    "description": "Thumbnail image url for this podcast's artwork (300x300)."
                  },
                  "is_claimed": {
                    "type": "boolean",
                    "example": true,
                    "description": "Whether this podcast is claimed by its producer on [ListenNotes.com](https://www.ListenNotes.com)."
                  },
                  "description": {
                    "type": "string",
                    "example": "<p>The Star Wars 7x7 Podcast is Rebel-rousing fun for everyday Jedi, between 7 and 14 minutes a day, 7 days a week. Join host Allen Voivod for Star Wars news, history, interviews, trivia, and deep dives into the Star Wars story as told in movies, books, comics, games, cartoons, and more. Subscribe now for your daily dose of Star Wars joy. It's destiny unleashed!</p>",
                    "description": "Html of this episode's full description"
                  },
                  "looking_for": {
                    "type": "object",
                    "properties": {
                      "guests": {
                        "type": "boolean",
                        "example": true,
                        "description": "Whether this podcast is looking for guests."
                      },
                      "cohosts": {
                        "type": "boolean",
                        "example": true,
                        "description": "Whether this podcast is looking for cohosts."
                      },
                      "sponsors": {
                        "type": "boolean",
                        "example": true,
                        "description": "Whether this podcast is looking for sponsors."
                      },
                      "cross_promotion": {
                        "type": "boolean",
                        "example": true,
                        "description": "Whether this podcast is looking for cross promotion opportunities with other podcasts."
                      }
                    }
                  },
                  "listen_score": {
                    "type": "integer",
                    "example": 81,
                    "description": "The estimated popularity score of a podcast compared to all other rss-based public podcasts in the world on a scale from 0 to 100.\nIf the score is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
                  },
                  "total_episodes": {
                    "type": "integer",
                    "example": 324,
                    "description": "Total number of episodes in this podcast."
                  },
                  "listennotes_url": {
                    "type": "string",
                    "example": "https://www.listennotes.com/c/4d3fe717742d4963a85562e9f84d8c79/",
                    "description": "The url of this podcast on [ListenNotes.com](https://www.ListenNotes.com)."
                  },
                  "explicit_content": {
                    "type": "boolean",
                    "example": false,
                    "description": "Whether this podcast contains explicit language."
                  },
                  "latest_pub_date_ms": {
                    "type": "integer",
                    "example": 1557499770000,
                    "description": "The published date of the latest episode of this podcast. In milliseconds"
                  },
                  "earliest_pub_date_ms": {
                    "type": "integer",
                    "example": 1470667902000,
                    "description": "The published date of the oldest episode of this podcast. In milliseconds"
                  },
                  "listen_score_global_rank": {
                    "type": "string",
                    "example": "0.5%",
                    "description": "The estimated popularity ranking of a podcast compared to all other rss-based public podcasts in the world.\nFor example, if the value is 0.5%, then this podcast is one of the top 0.5% most popular shows out of all podcasts globally, ranked by Listen Score.\nIf the ranking is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "audio": {
                    "type": "string",
                    "example": "https://example.com/audio.mp3",
                    "description": "Audio url, which can be played directly."
                  },
                  "image": {
                    "type": "string",
                    "example": "https://cdn-images-1.listennotes.com/playlist/image/6907e8ff6b6c45df94cc059753f369cc.JPEG",
                    "description": "High resolution image url of this custom audio."
                  },
                  "title": {
                    "type": "string",
                    "example": "An awesome audio to listen.",
                    "description": "Custom audio title."
                  },
                  "thumbnail": {
                    "type": "string",
                    "example": "https://d3sv2eduhewoas.cloudfront.net/playlist/image/48477deae02649d7ab9d3f1b3966af38.JPEG",
                    "description": "Low resolution image url of this custom audio."
                  },
                  "pub_date_ms": {
                    "type": "integer",
                    "example": 1595567028133,
                    "description": "Published date (in milliseconds) of this custom audio.\nFor now, it's the same as **added_at_ms** of this playlist item.\n"
                  },
                  "audio_length_sec": {
                    "type": "integer",
                    "example": 253,
                    "description": "Audio length in seconds."
                  }
                },
                "description": "A custom audio in a playlist, which is a type of playlist item."
              },
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "string",
                    "example": "96fc400171364e32897b25d84a8ed8ec",
                    "description": "Episode id or podcast id."
                  },
                  "error": {
                    "type": "string",
                    "example": "This episode is deleted from the podcast database, because...",
                    "description": "Why this episode or podcast is deleted?"
                  },
                  "title": {
                    "type": "string",
                    "example": "This is a test episode",
                    "description": "Episode title or podcast title."
                  },
                  "status": {
                    "type": "string",
                    "example": "deleted",
                    "description": "The status of this episode or podcast. For now, the only possible value is **deleted**."
                  }
                },
                "description": "A deleted episode or podcast.\nAn episode or a podcast could be deleted from our podcast database.\nPossible reasons: 1) Podcast producers sometimes delete their old episodes. 2) Copyright issues.\n"
              }
            ]
          },
          "type": {
            "enum": [
              "episode",
              "custom_audio",
              "podcast"
            ],
            "type": "string",
            "example": "episode",
            "description": "The type of this playlist item.\nIf a playlist is **episode_list**, then an item could be either **episode** or **custom_audio**.\nIf it's **podcast_list**, then an item can only be **podcast**.\n"
          },
          "notes": {
            "type": "string",
            "example": "This is a good episode.",
            "description": "Notes for this item."
          },
          "added_at_ms": {
            "type": "integer",
            "example": 1595567004958,
            "description": "Timestamp (in milliseconds) when this item is added."
          }
        },
        "description": "An item in a playlist"
      },
      "description": "A list of playlist items."
    },
    "total": {
      "type": "integer",
      "example": 325,
      "description": "Total number of items in this playlist."
    },
    "thumbnail": {
      "type": "string",
      "example": "https://d3sv2eduhewoas.cloudfront.net/playlist/image/48477deae02649d7ab9d3f1b3966af38.JPEG",
      "description": "Low resolution image url of the playlist."
    },
    "visibility": {
      "enum": [
        "public",
        "unlisted",
        "private"
      ],
      "type": "string",
      "example": "public",
      "description": "Visibility of this playlist."
    },
    "description": {
      "type": "string",
      "example": "A curated playlist of podcasts about podcasting.",
      "description": "Playlist description."
    },
    "listennotes_url": {
      "type": "string",
      "example": "https://www.listennotes.com/listen/podcasts-about-podcasting-m1pe7z60bsw/?display=episode",
      "description": "The url of this playlist on ListenNotes.com."
    },
    "last_timestamp_ms": {
      "type": "integer",
      "example": 1595641092907,
      "description": "Passed to the **last_timestamp_ms** parameter of `GET /playlists/{id}` to paginate through items of that playlist.\n"
    }
  }
}
```   
</details>




### Fetch a list of your playlists.

Function Name: **fetch_my_playlists**

This endpoint returns same data as listennotes.com/listen under your account.
You can use the **page** parameter to do pagination and fetch more playlists.


Example:
```python

from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)      

response = client.fetch_my_playlists(page=1, sort='name_a_to_z')
            
print(response.json())

```

See all available parameters on the [API Docs page](https://www.listennotes.com/api/docs/#get-api-v2-playlists).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "total": 3,
  "has_next": false,
  "playlists": [
    {
      "id": "kr3-ta28cJu",
      "name": "Wenbin Fang's Podcast Playlist",
      "image": "https://cdn-images-1.listennotes.com/playlist/image/42ab5b0d649d4fcea68249127f71f2b5.JPEG",
      "thumbnail": "https://cdn-images-1.listennotes.com/playlist/image/42ab5b0d649d4fcea68249127f71f2b5.JPEG",
      "visibility": "public",
      "description": "Wenbin Fang\u2019s master playlist. Just listen to individual episodes, rather than subscribing to tons of podcasts. How I listen to podcasts: https://lnns.co/6ArPszTwvDE",
      "episode_count": 4953,
      "podcast_count": 52,
      "listennotes_url": "https://www.listennotes.com/playlists/wenbin-fangs-podcast-playlist-kr3-ta28cJu/episodes/"
    },
    {
      "id": "m1pe7z60bsw",
      "name": "Podcasts about podcasting",
      "image": "https://production.listennotes.com/playlist/image/6907e8ff6b6c45df94cc059753f369cc.JPEG",
      "thumbnail": "https://d3sv2eduhewoas.cloudfront.net/playlist/image/48477deae02649d7ab9d3f1b3966af38.JPEG",
      "visibility": "public",
      "description": "A curated playlist of podcasts by Wenbin Fang.",
      "episode_count": 36,
      "podcast_count": 2,
      "listennotes_url": "https://www.listennotes.com/playlists/podcasts-about-podcasting-m1pe7z60bsw/episodes/"
    },
    {
      "id": "uIK85BM6EWJ",
      "name": "There's a podcast for that",
      "image": "https://production.listennotes.com/playlist/image/6e7c344a7a664320854a0677b57b3342.JPEG",
      "thumbnail": "https://production.listennotes.com/playlist/image/6e7c344a7a664320854a0677b57b3342.JPEG",
      "visibility": "public",
      "description": "Inspired by \"There's an app for that\". Email me if you want to become a contributor of this list: hello@listennotes.com",
      "episode_count": 0,
      "podcast_count": 128,
      "listennotes_url": "https://www.listennotes.com/playlists/theres-a-podcast-for-that-uIK85BM6EWJ/podcasts/"
    }
  ],
  "page_number": 1,
  "has_previous": false,
  "next_page_number": 2,
  "previous_page_number": 0
}
```   
</details>



<details>
  <summary>Click to see response schema</summary>
  
```json
{
  "type": "object",
  "properties": {
    "total": {
      "type": "integer",
      "example": 325
    },
    "has_next": {
      "type": "boolean",
      "example": true
    },
    "playlists": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "example": "m1pe7z60bsw",
            "description": "A 11-character playlist id."
          },
          "name": {
            "type": "string",
            "example": "My podcast playlist",
            "description": "Playlist name."
          },
          "image": {
            "type": "string",
            "example": "https://cdn-images-1.listennotes.com/playlist/image/6907e8ff6b6c45df94cc059753f369cc.JPEG",
            "description": "High resolution image url of the playlist."
          },
          "thumbnail": {
            "type": "string",
            "example": "https://d3sv2eduhewoas.cloudfront.net/playlist/image/48477deae02649d7ab9d3f1b3966af38.JPEG",
            "description": "Low resolution image url of the playlist."
          },
          "visibility": {
            "enum": [
              "public",
              "unlisted",
              "private"
            ],
            "type": "string",
            "example": "public",
            "description": "Visibility of this playlist."
          },
          "description": {
            "type": "string",
            "example": "A curated playlist of podcasts about podcasting.",
            "description": "Playlist description."
          },
          "episode_count": {
            "type": "integer",
            "example": 23,
            "description": "The number of episodes (including custom audio) in this playlist."
          },
          "podcast_count": {
            "type": "integer",
            "example": 10,
            "description": "The number of podcasts in this playlist."
          },
          "listennotes_url": {
            "type": "string",
            "example": "https://www.listennotes.com/listen/podcasts-about-podcasting-m1pe7z60bsw/?display=episode",
            "description": "The url of this playlist on ListenNotes.com."
          },
          "last_timestamp_ms": {
            "type": "integer",
            "example": 1595641092907,
            "description": "Passed to the **last_timestamp_ms** parameter of `GET /playlists/{id}` to paginate through items of that playlist.\n"
          }
        },
        "description": "A playlist"
      }
    },
    "page_number": {
      "type": "integer",
      "example": 2
    },
    "has_previous": {
      "type": "boolean",
      "example": true
    },
    "next_page_number": {
      "type": "integer",
      "example": 3
    },
    "previous_page_number": {
      "type": "integer",
      "example": 1
    }
  }
}
```   
</details>




### Fetch trending search terms

Function Name: **fetch_trending_searches**

Fetch up to 10 most recent trending search terms on the Listen Notes platform.

Example:
```python

from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)      

response = client.fetch_trending_searches()
            
print(response.json())

```

See all available parameters on the [API Docs page](https://www.listennotes.com/api/docs/#get-api-v2-trending_searches).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "terms": [
    "Ronan Farrow",
    "Frances Haugen",
    "Gary Gensler",
    "Evergrande",
    "Taliban",
    "\"Andrew Cuomo\"",
    "John McAfee",
    "\"Antonio Garc\u00eda Mart\u00ednez\"",
    "Bill Gates",
    "\"Brian Armstrong\""
  ]
}
```   
</details>



<details>
  <summary>Click to see response schema</summary>
  
```json
{
  "type": "object",
  "required": [
    "terms"
  ],
  "properties": {
    "terms": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "example": [
        "Taliban",
        "Andrew Cuomo",
        "john McAfee"
      ],
      "description": "Trending search terms"
    }
  }
}
```   
</details>




### Fetch related search terms

Function Name: **fetch_related_searches**

Suggest related search terms. The results are more comprehensive than from **GET /typeahead**. This endpoint is available only in the PRO/ENTERPRISE plan.

Example:
```python

from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)      

response = client.fetch_related_searches(q='evergrande')
            
print(response.json())

```

See all available parameters on the [API Docs page](https://www.listennotes.com/api/docs/#get-api-v2-related_searches).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "terms": [
    "evergrande stock",
    "evergrande china",
    "evergrande group",
    "evergrande bonds",
    "evergrande deadline",
    "evergrande contagion",
    "evergrande news",
    "evergrande default"
  ]
}
```   
</details>



<details>
  <summary>Click to see response schema</summary>
  
```json
{
  "type": "object",
  "required": [
    "terms"
  ],
  "properties": {
    "terms": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "example": [
        "evergrande stock",
        "evergrande china",
        "evergrande group",
        "evergrande news"
      ],
      "description": "Related search terms"
    }
  }
}
```   
</details>




### Spell check on a search term

Function Name: **spellcheck**

Suggest a list of words that correct the spelling errors of a search term. This endpoint is available only in the PRO/ENTERPRISE plan.

Example:
```python

from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)      

response = client.spellcheck(q='evergrand stok')
            
print(response.json())

```

See all available parameters on the [API Docs page](https://www.listennotes.com/api/docs/#get-api-v2-spellcheck).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "tokens": [
    {
      "token": "evergrand",
      "offset": 0,
      "suggestion": "evergrande"
    },
    {
      "token": "stok",
      "offset": 10,
      "suggestion": "stock"
    }
  ],
  "corrected_text_html": "<b><i>evergrande</i></b> <b><i>stock</i></b>"
}
```   
</details>



<details>
  <summary>Click to see response schema</summary>
  
```json
{
  "type": "object",
  "required": [
    "tokens",
    "corrected_text_html"
  ],
  "properties": {
    "tokens": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "token": {
            "type": "string",
            "example": "evergrand",
            "description": "The misspelled word"
          },
          "offset": {
            "type": "integer",
            "example": 5,
            "description": "The zero-based offset from the beginning of the text query string to the word that is misspelled"
          },
          "suggestion": {
            "type": "string",
            "example": "evergrande",
            "description": "A word that corrects the spelling error"
          }
        }
      },
      "description": "The word in the text query string that is not spelled correctly"
    },
    "corrected_text_html": {
      "type": "string",
      "example": "<b><i>evergrande</i></b> stock",
      "description": "The corrected text for the entire search term (multiple words/tokens), where misspelled tokens are replaced with the correct texts and html tags <b><i>"
    }
  }
}
```   
</details>



