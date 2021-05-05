# Podcast API Python Library

[![Build Status](https://travis-ci.com/ListenNotes/podcast-api-python.svg?branch=main)](https://travis-ci.com/ListenNotes/podcast-api-python)

The Podcast API Python library provides convenient access to the [Listen Notes Podcast API](https://www.listennotes.com/api/) from
applications written in the Python language.

Simple and no-nonsense podcast search & directory API. Search the meta data of all podcasts and episodes by people, places, or topics. It's the same API that powers [the best podcast search engine Listen Notes](https://www.listennotes.com/).

If you have any questions, please contact [hello@listennotes.com](hello@listennotes.com?subject=Questions+about+the+PHP+SDK+of+Listen+API)

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
  "took": 0.693,
  "count": 10,
  "total": 9499,
  "results": [
    {
      "id": "ea09b575d07341599d8d5b71f205517b",
      "rss": "https://theroughcut.libsyn.com/rss",
      "link": "http://theroughcutpod.com/?p=786&utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/ea09b575d07341599d8d5b71f205517b/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-rough-cut-PmR84dsqcbj-53MLh7NpAwm.1400x1400.jpg",
      "podcast": {
        "id": "8758da9be6c8452884a8cab6373b007c",
        "image": "https://cdn-images-1.listennotes.com/podcasts/the-rough-cut-PmR84dsqcbj-53MLh7NpAwm.1400x1400.jpg",
        "genre_ids": [
          68,
          264
        ],
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-rough-cut-AzKVtPeMOL4-53MLh7NpAwm.300x300.jpg",
        "listen_score": 37,
        "title_original": "The Rough Cut",
        "listennotes_url": "https://www.listennotes.com/c/8758da9be6c8452884a8cab6373b007c/",
        "title_highlighted": "The Rough Cut",
        "publisher_original": "Matt Feury",
        "publisher_highlighted": "Matt Feury",
        "listen_score_global_rank": "3%"
      },
      "itunes_id": 1471556007,
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-rough-cut-AzKVtPeMOL4-53MLh7NpAwm.300x300.jpg",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-vintage-rpg-podcast-vintage-rpg-V8MjvNnSRBt-eq8uGUY6vXN.1400x1400.jpg",
      "podcast": {
        "id": "f3094a0b14684300a3d6b69a1063e708",
        "image": "https://cdn-images-1.listennotes.com/podcasts/the-vintage-rpg-podcast-vintage-rpg-V8MjvNnSRBt-eq8uGUY6vXN.1400x1400.jpg",
        "genre_ids": [
          82,
          85,
          83
        ],
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-vintage-rpg-podcast-vintage-rpg-Mg-2ZYcmERT-eq8uGUY6vXN.300x300.jpg",
        "listen_score": 46,
        "title_original": "The Vintage RPG Podcast",
        "listennotes_url": "https://www.listennotes.com/c/f3094a0b14684300a3d6b69a1063e708/",
        "title_highlighted": "The Vintage RPG Podcast",
        "publisher_original": "Vintage RPG",
        "publisher_highlighted": "Vintage RPG",
        "listen_score_global_rank": "1%"
      },
      "itunes_id": 1409477830,
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-vintage-rpg-podcast-vintage-rpg-Mg-2ZYcmERT-eq8uGUY6vXN.300x300.jpg",
      "pub_date_ms": 1575867600060,
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
      "id": "abcc7a1ad1d14c8b81621458409bcbd8",
      "rss": "https://www.spreaker.com/show/4260636/episodes/feed",
      "link": "https://www.spreaker.com/user/scifitalk/craig-miller-star-wars-memories?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/abcc7a1ad1d14c8b81621458409bcbd8/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/sci-fi-talk-tony-tellado-c3pI562aqwD-pbWBl23qQhO.1400x1400.jpg",
      "podcast": {
        "id": "9c2c314ee8134f288745348df83dcafd",
        "image": "https://cdn-images-1.listennotes.com/podcasts/sci-fi-talk-tony-tellado-c3pI562aqwD-pbWBl23qQhO.1400x1400.jpg",
        "genre_ids": [
          68,
          100,
          101,
          122,
          126
        ],
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/sci-fi-talk-tony-tellado-FG3ti2BOQ7V-pbWBl23qQhO.300x300.jpg",
        "listen_score": 35,
        "title_original": "Sci-Fi Talk",
        "listennotes_url": "https://www.listennotes.com/c/9c2c314ee8134f288745348df83dcafd/",
        "title_highlighted": "Sci-Fi Talk",
        "publisher_original": "Tony Tellado",
        "publisher_highlighted": "Tony Tellado",
        "listen_score_global_rank": "5%"
      },
      "itunes_id": 73330406,
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/sci-fi-talk-tony-tellado-FG3ti2BOQ7V-pbWBl23qQhO.300x300.jpg",
      "pub_date_ms": 1576731600168,
      "guid_from_rss": "a7d8ab58-cff4-49a7-940e-0fbed1418239",
      "title_original": "Craig Miller Star Wars Memories",
      "listennotes_url": "https://www.listennotes.com/e/abcc7a1ad1d14c8b81621458409bcbd8/",
      "audio_length_sec": 1615,
      "explicit_content": false,
      "title_highlighted": "Craig Miller <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Memories",
      "description_original": "Interview with someone there at the start of Star Wars who started the official fan club. Some nice memories about Mark Hamill, Harrison Ford and Carrie Fisher.",
      "description_highlighted": "...Interview with someone there at the start of <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> who started the official fan club. Some nice memories about Mark Hamill, Harrison Ford and Carrie Fisher.",
      "transcripts_highlighted": []
    },
    {
      "id": "6280a11466dd407e99c66130f203167a",
      "rss": "https://snlafterparty.libsyn.com/rss",
      "link": "https://snlpodcast.com/episodes/2019/12/24/sample-star-wars-tv-talk-podcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/6280a11466dd407e99c66130f203167a/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/saturday-night-live-snl-afterparty-john-sEoTraLnKPB-_iOE4lLZ2pD.1400x1400.jpg",
      "podcast": {
        "id": "09b986e503d4448ab0b625f6233bdd65",
        "image": "https://cdn-images-1.listennotes.com/podcasts/saturday-night-live-snl-afterparty-john-sEoTraLnKPB-_iOE4lLZ2pD.1400x1400.jpg",
        "genre_ids": [
          68,
          133,
          134
        ],
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/saturday-night-live-snl-afterparty-john-wm1CtQVkRfy-_iOE4lLZ2pD.300x300.jpg",
        "listen_score": 44,
        "title_original": "Saturday Night Live (SNL) Afterparty",
        "listennotes_url": "https://www.listennotes.com/c/09b986e503d4448ab0b625f6233bdd65/",
        "title_highlighted": "Saturday Night Live (SNL) Afterparty",
        "publisher_original": "John Murray / Spry FM",
        "publisher_highlighted": "John Murray / Spry FM",
        "listen_score_global_rank": "1.5%"
      },
      "itunes_id": 1133381225,
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/saturday-night-live-snl-afterparty-john-wm1CtQVkRfy-_iOE4lLZ2pD.300x300.jpg",
      "pub_date_ms": 1576989000015,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/marvel-cinematic-universe-podcast-deRo7LDQBfn-aXR7VuG2z4p.1400x1400.jpg",
      "podcast": {
        "id": "593c42e343ba44e7b6f8634a946f0b52",
        "image": "https://cdn-images-1.listennotes.com/podcasts/marvel-cinematic-universe-podcast-deRo7LDQBfn-aXR7VuG2z4p.1400x1400.jpg",
        "genre_ids": [
          68,
          99,
          122
        ],
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/marvel-cinematic-universe-podcast-wVDeHrdxZJh-aXR7VuG2z4p.300x300.jpg",
        "listen_score": 57,
        "title_original": "Marvel Cinematic Universe Podcast: The Falcon and the Winter Soldier",
        "listennotes_url": "https://www.listennotes.com/c/593c42e343ba44e7b6f8634a946f0b52/",
        "title_highlighted": "Marvel Cinematic Universe Podcast: The Falcon and the Winter Soldier",
        "publisher_original": "Stranded Panda",
        "publisher_highlighted": "Stranded Panda",
        "listen_score_global_rank": "0.5%"
      },
      "itunes_id": 907175322,
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/marvel-cinematic-universe-podcast-wVDeHrdxZJh-aXR7VuG2z4p.300x300.jpg",
      "pub_date_ms": 1575521386130,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-2g5pFidDckm-BodDr7iIAR3.1400x1400.jpg",
      "podcast": {
        "id": "8bdbb906eef04e5d8b391e947998e9af",
        "image": "https://cdn-images-1.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-2g5pFidDckm-BodDr7iIAR3.1400x1400.jpg",
        "genre_ids": [
          68,
          214,
          265,
          99
        ],
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-ysANR-GCZQm-BodDr7iIAR3.300x300.jpg",
        "listen_score": 51,
        "title_original": "Super Carlin Brothers",
        "listennotes_url": "https://www.listennotes.com/c/8bdbb906eef04e5d8b391e947998e9af/",
        "title_highlighted": "Super Carlin Brothers",
        "publisher_original": "J and Ben Carlin",
        "publisher_highlighted": "J and Ben Carlin",
        "listen_score_global_rank": "1%"
      },
      "itunes_id": 1479112798,
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-ysANR-GCZQm-BodDr7iIAR3.300x300.jpg",
      "pub_date_ms": 1576602000111,
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
      "id": "8bb936149d2a4c8d9263b6683d09817e",
      "rss": "https://rss.art19.com/inside-star-wars",
      "link": "https://wondery.com/shows/inside-star-wars/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/8bb936149d2a4c8d9263b6683d09817e/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/inside-star-wars-wondery-MXsJ_pCNah3-e8ydUYnAOJv.1400x1400.jpg",
      "podcast": {
        "id": "8e90b8f0c9eb4c11b13f9dc331ed747c",
        "image": "https://cdn-images-1.listennotes.com/podcasts/inside-star-wars-wondery-MXsJ_pCNah3-e8ydUYnAOJv.1400x1400.jpg",
        "genre_ids": [
          122,
          68
        ],
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/inside-star-wars-wondery-5uMv-OJoUT9-e8ydUYnAOJv.300x300.jpg",
        "listen_score": 60,
        "title_original": "Inside Star Wars",
        "listennotes_url": "https://www.listennotes.com/c/8e90b8f0c9eb4c11b13f9dc331ed747c/",
        "title_highlighted": "Inside Star Wars",
        "publisher_original": "Wondery",
        "publisher_highlighted": "Wondery",
        "listen_score_global_rank": "0.5%"
      },
      "itunes_id": 1459899343,
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/inside-star-wars-wondery-5uMv-OJoUT9-e8ydUYnAOJv.300x300.jpg",
      "pub_date_ms": 1559114100010,
      "guid_from_rss": "gid://art19-episode-locator/V0/TLnNY6-JmrwBnSli6uy41rZXNQENnWNpfKaFewQocl8",
      "title_original": "Dreams of Star Wars  | 2",
      "listennotes_url": "https://www.listennotes.com/e/8bb936149d2a4c8d9263b6683d09817e/",
      "audio_length_sec": 1227,
      "explicit_content": false,
      "title_highlighted": "Dreams of <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span>  | 2",
      "description_original": "A young Carrie Fisher meets the paparazzi in the arms of her celebrity mother, Debbie Reynolds. It doesn\u2019t take Carrie long to decide that acting\u2019s not for her. So naturally, an actor is exactly what she becomes. Carrie models tops for Warren Beatty - with and without a bra. Meanwhile, George Lucas has decided to study film. Even though no film school graduate had ever gotten a job in the industry. He quickly becomes a star at USC, determined to make his movies his way, no matter what the rules are. He works day and night on a diet of coffee and chocolate bars. He graduates just as movie attendance is cratering and Hollywood is shutting down. He meets another young cinematic firebrand, Francis Coppola, and they join forces on his first movie, THX1138. Warner Brothers hates the movie and takes it back to cut it themselves. It limps into theaters where one young film buff is left awestruck. His name is Steven Spielberg. Meanwhile Lucas dreams of a movie with heroes and villains, ray guns and spaceships, thrills and adventure beyond the stars.Support us by supporting our sponsors!Wix - Go to Wix.com and enter code YODA for 10% off any premium plan!",
      "description_highlighted": "...He quickly becomes a <span class=\"ln-search-highlight\">star</span> at USC, determined to make his movies his way, no matter what the rules are. He works day and night on a diet of coffee and chocolate bars.",
      "transcripts_highlighted": []
    },
    {
      "id": "a34693ebf8b04a64b448208281965298",
      "rss": "https://feeds.megaphone.fm/ROOSTER7199250968",
      "link": "https://supercarlinbrothers.libsyn.com/star-wars-theory-was-han-solo-force-sensitive?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/a34693ebf8b04a64b448208281965298/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-2g5pFidDckm-BodDr7iIAR3.1400x1400.jpg",
      "podcast": {
        "id": "8bdbb906eef04e5d8b391e947998e9af",
        "image": "https://cdn-images-1.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-2g5pFidDckm-BodDr7iIAR3.1400x1400.jpg",
        "genre_ids": [
          68,
          214,
          265,
          99
        ],
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-ysANR-GCZQm-BodDr7iIAR3.300x300.jpg",
        "listen_score": 51,
        "title_original": "Super Carlin Brothers",
        "listennotes_url": "https://www.listennotes.com/c/8bdbb906eef04e5d8b391e947998e9af/",
        "title_highlighted": "Super Carlin Brothers",
        "publisher_original": "J and Ben Carlin",
        "publisher_highlighted": "J and Ben Carlin",
        "listen_score_global_rank": "1%"
      },
      "itunes_id": 1479112798,
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-ysANR-GCZQm-BodDr7iIAR3.300x300.jpg",
      "pub_date_ms": 1575997200113,
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
      "id": "7d10e4bf2c1446d8b095df043fb39d68",
      "rss": "https://www.omnycontent.com/d/playlist/b004fc18-3e73-404c-9a0a-aaa2001f4448/fdc7f23c-a55d-492f-8899-aaa40023fd0e/5879b0b2-04a5-45e2-9e20-aaa400241c06/podcast.rss",
      "link": "https://viewfinder.expedia.com/travel-podcast-bonus-return-to-star-wars-galaxys-edge/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/7d10e4bf2c1446d8b095df043fb39d68/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/out-travel-the-system-jaht9Wklq7e-1X9JaE0p7TV.1400x1400.jpg",
      "podcast": {
        "id": "84bc40c6aa2948edbf6fbb53cd73707c",
        "image": "https://cdn-images-1.listennotes.com/podcasts/out-travel-the-system-jaht9Wklq7e-1X9JaE0p7TV.1400x1400.jpg",
        "genre_ids": [
          123,
          82,
          122,
          244
        ],
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/out-travel-the-system-Zp48KSkJ2jo-1X9JaE0p7TV.300x300.jpg",
        "listen_score": 43,
        "title_original": "Out Travel The System",
        "listennotes_url": "https://www.listennotes.com/c/84bc40c6aa2948edbf6fbb53cd73707c/",
        "title_highlighted": "Out Travel The System",
        "publisher_original": "Expedia",
        "publisher_highlighted": "Expedia",
        "listen_score_global_rank": "1.5%"
      },
      "itunes_id": 1477909314,
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/out-travel-the-system-Zp48KSkJ2jo-1X9JaE0p7TV.300x300.jpg",
      "pub_date_ms": 1575586800030,
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
      "id": "3348a2918d8643aa8dfe3b8471846e2c",
      "rss": "https://feeds.buzzsprout.com/726630.rss",
      "link": "http://www.youtube.com/c/starwarsexplained?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/3348a2918d8643aa8dfe3b8471846e2c/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-explained-alex-mollie-c8Ju4l6grFQ-zuwl0R2DOjf.1400x1400.jpg",
      "podcast": {
        "id": "699701ca2479411f9c0bbf8dd85323e8",
        "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-explained-alex-mollie-c8Ju4l6grFQ-zuwl0R2DOjf.1400x1400.jpg",
        "genre_ids": [
          168,
          68,
          265,
          185
        ],
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-explained-alex-mollie-_li6TLEwgs2-zuwl0R2DOjf.300x300.jpg",
        "listen_score": 45,
        "title_original": "Star Wars Explained",
        "listennotes_url": "https://www.listennotes.com/c/699701ca2479411f9c0bbf8dd85323e8/",
        "title_highlighted": "Star Wars Explained",
        "publisher_original": "Alex & Mollie",
        "publisher_highlighted": "Alex & Mollie",
        "listen_score_global_rank": "1.5%"
      },
      "itunes_id": 1488511803,
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-explained-alex-mollie-_li6TLEwgs2-zuwl0R2DOjf.300x300.jpg",
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
    "star wars news"
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/rebel-force-radio-star-wars-podcast-star-wars-GSQTPOZCqAx-4v5pRaEg1Ub.1400x1400.jpg",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/rebel-force-radio-star-wars-podcast-star-wars-Na1ogntxKO_-4v5pRaEg1Ub.300x300.jpg",
      "title_original": "Rebel Force Radio: Star Wars Podcast",
      "explicit_content": false,
      "title_highlighted": "Rebel Force Radio: <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Podcast",
      "publisher_original": "Star Wars",
      "publisher_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span>"
    },
    {
      "id": "9af8a811286b4fffa82e4c083cf5e711",
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-minute-star-wars-minute-RCHpuilvzfZ-GJRN7_nAPOM.1400x1400.jpg",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-minute-star-wars-minute-dkYIhKa6oZB-GJRN7_nAPOM.300x300.jpg",
      "title_original": "Star Wars Minute",
      "explicit_content": false,
      "title_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Minute",
      "publisher_original": "Star Wars Minute",
      "publisher_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Minute"
    },
    {
      "id": "912f36444ea6475693ab3ab899cc3782",
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-theory-jigowatt-media-b768lGX-pno-FGYt8XM-sIK.1400x1400.jpg",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-theory-jigowatt-media-EzrLmUAqx-n-FGYt8XM-sIK.300x300.jpg",
      "title_original": "Star Wars Theory",
      "explicit_content": false,
      "title_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Theory",
      "publisher_original": "Jigowatt Media",
      "publisher_highlighted": "Jigowatt Media"
    },
    {
      "id": "8e90b8f0c9eb4c11b13f9dc331ed747c",
      "image": "https://cdn-images-1.listennotes.com/podcasts/inside-star-wars-wondery-MXsJ_pCNah3-e8ydUYnAOJv.1400x1400.jpg",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/inside-star-wars-wondery-5uMv-OJoUT9-e8ydUYnAOJv.300x300.jpg",
      "title_original": "Inside Star Wars",
      "explicit_content": false,
      "title_highlighted": "Inside <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span>",
      "publisher_original": "Wondery",
      "publisher_highlighted": "Wondery"
    },
    {
      "id": "ff1938a1747c4698976943bf5f685600",
      "image": "https://cdn-images-1.listennotes.com/podcasts/children-of-the-watch-a-star-wars-show-star-bo3n9eKzGFq-lt7yMQIx2fP.1400x1400.jpg",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/children-of-the-watch-a-star-wars-show-star-j1VyM2ioalk-lt7yMQIx2fP.300x300.jpg",
      "title_original": "Children of the Watch: A Star Wars Show",
      "explicit_content": false,
      "title_highlighted": "Children of the Watch: A <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Show",
      "publisher_original": "Star Wars",
      "publisher_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span>"
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
  "email": "fx7@sw7x7.com",
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
  "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-HN08OoDE7pc-AIg3cZVKCsL.1400x1400.jpg",
  "title": "Star Wars 7x7: The Daily Star Wars Podcast",
  "country": "United States",
  "website": "http://sw7x7.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
  "episodes": [
    {
      "id": "4e7c59e10e4640b98f2f3cb1777dbb43",
      "link": "https://sw7x7.libsyn.com/864-part-2-of-my-new-conversation-with-bobby-roberts?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/4e7c59e10e4640b98f2f3cb1777dbb43/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-HN08OoDE7pc-AIg3cZVKCsL.1400x1400.jpg",
      "title": "864: Part 2 of My (New) Conversation With Bobby Roberts",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-2LryqMj-sGP-AIg3cZVKCsL.300x300.jpg",
      "description": "<p>The second half of my latest conversation with Bobby Roberts, Podcast Emeritus from Full of Sith and now Star Wars \"Podcast Force Ghost at Large.\" Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1479110401387,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-HN08OoDE7pc-AIg3cZVKCsL.1400x1400.jpg",
      "title": "863: A (New) Conversation With Bobby Roberts, Part 1",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-2LryqMj-sGP-AIg3cZVKCsL.300x300.jpg",
      "description": "<p>An in-depth conversation about the Star Wars \"Story\" movies and so much more, featuring Bobby Roberts, Star Wars \"Podcast Force Ghost at Large.\" Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1479024001388,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-HN08OoDE7pc-AIg3cZVKCsL.1400x1400.jpg",
      "title": "862: \"Assassin\" - Clone Wars Briefing, Season 3, Episode 7",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-2LryqMj-sGP-AIg3cZVKCsL.300x300.jpg",
      "description": "<p>The beginnings of the true power of the Force, revealed in \"Assassin,\" season 3, episode 7 of the Star Wars: The Clone Wars cartoon series. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478937601389,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-HN08OoDE7pc-AIg3cZVKCsL.1400x1400.jpg",
      "title": "861: Rogue One International Trailer Breakdown",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-2LryqMj-sGP-AIg3cZVKCsL.300x300.jpg",
      "description": "<p>Surprise! An international trailer for Rogue One has dropped, and it includes new scenes, new dialogue, and some heavy foreshadowing about Jyn Erso's fate. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478851457390,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-HN08OoDE7pc-AIg3cZVKCsL.1400x1400.jpg",
      "title": "860: Will Jyn and Cassian Survive Rogue One?",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-2LryqMj-sGP-AIg3cZVKCsL.300x300.jpg",
      "description": "<p>Today I conclude a two-episode set looking at the odds of survival for major Rogue One characters. Today: Jyn Erso, Cassian Andor, Bodhi Rook, and K-2SO. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478764801391,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-HN08OoDE7pc-AIg3cZVKCsL.1400x1400.jpg",
      "title": "859: The Odds: Who Will Survive Rogue One?",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-2LryqMj-sGP-AIg3cZVKCsL.300x300.jpg",
      "description": "<p>Will Galen Erso, Lyra Erso, Saw Gerrera, and Orson Krennic survive the events of Rogue One: A Star Wars Story? Starting a mini-series to look at the odds... Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478678401392,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-HN08OoDE7pc-AIg3cZVKCsL.1400x1400.jpg",
      "title": "858: \"Together\" - New Rogue One Commercial Dialogue",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-2LryqMj-sGP-AIg3cZVKCsL.300x300.jpg",
      "description": "<p>A new Rogue One commercial dropped Sunday, with some new dialogue that hints at the relationship between Jyn Erso, Saw Gerrera, the Rebellion, and the Partisans. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478592001393,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-HN08OoDE7pc-AIg3cZVKCsL.1400x1400.jpg",
      "title": "857: \"Imperial Supercommandos\" - Star Wars Rebels Season 3, Episode 7",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-2LryqMj-sGP-AIg3cZVKCsL.300x300.jpg",
      "description": "<p>\"Imperial Supercommandos\" is Season 3, episode 7 of Star Wars Rebels, referring to Mandalorians serving the Empire. But can Fenn Rau be trusted, either? Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478505601394,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-HN08OoDE7pc-AIg3cZVKCsL.1400x1400.jpg",
      "title": "856: \"The Academy\" - Clone Wars Briefing, Season 3, Episode 6",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-2LryqMj-sGP-AIg3cZVKCsL.300x300.jpg",
      "description": "<p>\"The Academy,\" Season 3 Episode 6 of the Clone Wars cartoon series, is a quieter episode that highlights the importance of Mandalore to the Star Wars franchise. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478415601395,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-HN08OoDE7pc-AIg3cZVKCsL.1400x1400.jpg",
      "title": "855: Episode VIII and Han Solo Movie Updates",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-2LryqMj-sGP-AIg3cZVKCsL.300x300.jpg",
      "description": "<p>Daisy Ridley says wait for Episode VIII for answers about Rey's parents. Bradford Young says the Han Solo movie won't be what you expect. Updates here... Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478329201396,
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
  "publisher": "Star Wars",
  "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-2LryqMj-sGP-AIg3cZVKCsL.300x300.jpg",
  "is_claimed": false,
  "description": "The Star Wars 7x7 Podcast is Rebel-rousing fun for everyday Jedi, generally between 7 and 14 minutes a day, always 7 days a week. Join host Allen Voivod for Star Wars news, history, interviews, trivia, and deep dives into the Star Wars story as told in movies, books, comics, games, cartoons, and more. Follow now for your daily dose of Star Wars joy. It's destiny unleashed! #SW7x7",
  "looking_for": {
    "guests": false,
    "cohosts": false,
    "sponsors": false,
    "cross_promotion": false
  },
  "listen_score": 48,
  "total_episodes": 2550,
  "listennotes_url": "https://www.listennotes.com/c/4d3fe717742d4963a85562e9f84d8c79/",
  "explicit_content": false,
  "latest_pub_date_ms": 1619852400000,
  "earliest_pub_date_ms": 1404637200000,
  "next_episode_pub_date": 1478329201396,
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
  "image": "https://cdn-images-1.listennotes.com/podcasts/a-winning-mindset/16-arly-velasquez-on-xPbM1hpZqFK-c5khPVKzowB.1400x1400.jpg",
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
    "image": "https://cdn-images-1.listennotes.com/podcasts/a-winning-mindset-lessons-from-the-Llx63IkbdYJ-BktA4YUzNbu.1400x1400.jpg",
    "title": "A Winning Mindset: Lessons From The Paralympics",
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
    "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/a-winning-mindset-lessons-from-the-7lD8syETwzh-BktA4YUzNbu.300x300.jpg",
    "is_claimed": true,
    "description": "Nominated for Best Branded Podcast at the Webby Awards and shortlisted for Best Interview Podcast at the Ambies Awards, A Winning Mindset is a fascinating journey into the minds of Paralympians, as they share experiences that can benefit your own personal and professional life.\u00a0\n\nThis empowering weekly series is the official podcast of the International Paralympic Committee, in partnership with Allianz.\u00a0\n\nEach podcast will provide a platform for Para athletes to talk about their empowering and inspirational stories, sporting life and greatest achievement and enable them to showcase their personalities.\n\nThe episodes will go beyond Paralympic stories by covering a range of educational, confidence and self-improvement themes.\u00a0 Athletes will also tackle subjects that are close to their hearts and of interest to fans. Issues to be explored include activism, leadership, motivation, changing attitudes, overcoming failure, mental health, resilience, positivity, diversity and inclusion, body confidence, compassion, decision-making, communication, self-understanding, happiness, organisation and efficiency techniques, combining family with a sport career, parenting, the power of purpose and a personal vision, assertiveness, empathy, friendship and teamwork.\u00a0\n\nThe Podcast series will also explore the progress and transformational impact made by the Paralympic Movement so far in making for a more inclusive world. We\u2019ll understand how Para sport has helped to change attitudes, increase mobility and accessibility and create more opportunities for people with a disability whether to have an education, play sport, have access to healthcare or employment.\n\nThe Paralympic podcast series is presented by British broadcaster Andy Stevenson, who has reported on the Paralympic Games since 2012 for BBC and Channel 4.\n\nParalympic athletes that are set to feature on the show include Jonnie Peacock, Tatyana McFadden and Bebe Vio.\u00a0",
    "looking_for": {
      "guests": false,
      "cohosts": false,
      "sponsors": false,
      "cross_promotion": true
    },
    "listen_score": 34,
    "total_episodes": 22,
    "listennotes_url": "https://www.listennotes.com/c/073a66b496824a5d9e80d52621f372dc/",
    "explicit_content": false,
    "latest_pub_date_ms": 1610071860000,
    "earliest_pub_date_ms": 1598436120021,
    "listen_score_global_rank": "5%"
  },
  "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/a-winning-mindset/16-arly-velasquez-on-ftCxqnUg0Sr-c5khPVKzowB.300x300.jpg",
  "transcript": "\nA Paralympic skiier from Mexico isn\u2019t something you expect to see too often. But Arly Velasquez doesn\u2019t believe in expectations. Velasquez, one of a select few to ever represent Mexico at a Winter Paralympic Games, discusses the role of risk in his life - and how we can all learn to manage it.\u00a0\u201cI have developed because of taking decisions where I have no idea. It\u2019s a matter of 'does it feel right or not?'\" he said.\"I don't see it as a risk, I see that when I am in the mountain on a sit ski, I just feel the most free.\u201d\u00a0The former BMX champion also discusses the risks he took when leaving Mexico on the spur of a moment, building a new life on the ski slopes in Canada. \u00a0\u201c(Skiing) gave me the belief to go back to Mexico, sell all my stuff,\u00a0 sell my car and pretty much fly to the border,\" he said.\u00a0\"It's very, rare that there are moments in your life where you are feeling and your gut tells you that you are in the right place. That you are doing the right thing and that it's something that you want to keep doing in your life. That's what I felt for the first time.\u201d\u00a0Learning topics for this episode include managing risk, how to build a brand, self-understanding, defiance, thrill-seeking and exploration. \u00a0Allianz is a long-standing partner of the International Paralympic Committee. Together, we\u2019re proud to bring you A Winning Mindset: Lessons From The Paralympics. We aim to help you move forward in all aspects of your personal and professional life.\u00a0By hearing from Paralympic stars, you\u2019ll be introduced to stories that inspire and change the way you think. Stories of facing life\u2019s challenges with confidence, determination and excellence, and the true power of having the right team behind you.\u00a0",
  "description": "<div>\n<strong>A Paralympic skiier from Mexico isn\u2019t something you expect to see too often. But Arly Velasquez doesn\u2019t believe in expectations. </strong><br><br>Velasquez, one of a select few to ever represent Mexico at a Winter Paralympic Games, discusses the role of risk in his life - and how we can all learn to manage it.\u00a0<br><br>\u201cI have developed because of taking decisions where I have no idea. It\u2019s a matter of 'does it feel right or not?'\" he said.<br><br>\"I don't see it as a risk, I see that when I am in the mountain on a sit ski, I just feel the most free.\u201d\u00a0<br><br>The former BMX champion also discusses the risks he took when leaving Mexico on the spur of a moment, building a new life on the ski slopes in Canada. \u00a0<br><br>\u201c(Skiing) gave me the belief to go back to Mexico, sell all my stuff,\u00a0 sell my car and pretty much fly to the border,\" he said.\u00a0<br><br>\"It's very, rare that there are moments in your life where you are feeling and your gut tells you that you are in the right place. That you are doing the right thing and that it's something that you want to keep doing in your life. That's what I felt for the first time.\u201d\u00a0<br><br>Learning topics for this episode include managing risk, how to build a brand, self-understanding, defiance, thrill-seeking and exploration. \u00a0<br><br>Allianz is a long-standing partner of the International Paralympic Committee. Together, we\u2019re proud to bring you A Winning Mindset: Lessons From The Paralympics. We aim to help you move forward in all aspects of your personal and professional life.\u00a0<br><br>By hearing from Paralympic stars, you\u2019ll be introduced to stories that inspire and change the way you think. Stories of facing life\u2019s challenges with confidence, determination and excellence, and the true power of having the right team behind you.\u00a0</div>",
  "pub_date_ms": 1607054220005,
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
      "id": 125,
      "name": "History",
      "parent_id": 67
    },
    {
      "id": 151,
      "name": "Locally Focused",
      "parent_id": 67
    },
    {
      "id": 117,
      "name": "Government",
      "parent_id": 67
    },
    {
      "id": 93,
      "name": "Business",
      "parent_id": 67
    },
    {
      "id": 77,
      "name": "Sports",
      "parent_id": 67
    },
    {
      "id": 99,
      "name": "News",
      "parent_id": 67
    },
    {
      "id": 127,
      "name": "Technology",
      "parent_id": 67
    },
    {
      "id": 133,
      "name": "Comedy",
      "parent_id": 67
    },
    {
      "id": 88,
      "name": "Health & Fitness",
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
      "id": 135,
      "name": "True Crime",
      "parent_id": 67
    },
    {
      "id": 134,
      "name": "Music",
      "parent_id": 67
    },
    {
      "id": 100,
      "name": "Arts",
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
      "id": 68,
      "name": "TV & Film",
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

Get a list of curated best podcasts by genre. You can get the genre ids from `GET /genres` endpoint.
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
  "total": 607,
  "has_next": true,
  "podcasts": [
    {
      "id": "7872bb012fde45509079ddc8c4d573e2",
      "rss": "https://the-backpack-show.castos.com/feed",
      "type": "episodic",
      "email": "thebackpacktvshow@gmail.com",
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
        "twitter_handle": "chrisbrogan",
        "facebook_handle": "TheBackpackShowLIVE",
        "instagram_handle": ""
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-backpack-show-Qml8Ggiqw_j--E1BbUyfKi2.1400x1400.jpg",
      "title": "The Backpack Show",
      "country": "United States",
      "website": "https://thebackpackshow.online?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        67,
        173,
        171
      ],
      "itunes_id": 1552239939,
      "publisher": "Chris Brogan and Kerry Gorgone",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-backpack-show-ACpn4FHmKkR--E1BbUyfKi2.300x300.jpg",
      "is_claimed": false,
      "description": "Providing business insights from unusual places, the Backpack Show isn't your typical business podcast. We interview everyone from Sir Mix-A-Lot to Mexican Horror/Comedy Actors to nuns to give you great business insights. Chris Brogan and Kerry Gorgone deliver a daily live video (and now audio) experience for YOU!",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": null,
      "total_episodes": 61,
      "listennotes_url": "https://www.listennotes.com/c/7872bb012fde45509079ddc8c4d573e2/",
      "explicit_content": true,
      "latest_pub_date_ms": 1619794620000,
      "earliest_pub_date_ms": 1612270800011,
      "listen_score_global_rank": null
    },
    {
      "id": "8f83465e290941dd9023cefbce02c208",
      "rss": "https://feeds.captivate.fm/empire-building/",
      "type": "episodic",
      "email": "publishing@crate.media",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/empire-building-keller-williams-di6IxQZla2B-ziBkaZyUcsd.1400x1400.jpg",
      "title": "Empire Building",
      "country": "United States",
      "website": "https://empire-building.captivate.fm?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        181,
        111,
        67,
        93,
        94
      ],
      "itunes_id": 1513216353,
      "publisher": "Produktive",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/empire-building-keller-williams-ihOkNwbMB-e-ziBkaZyUcsd.300x300.jpg",
      "is_claimed": false,
      "description": "If you strive to grow a bigger business, find a bigger purpose, foster bigger relationships, and lead a bigger life, you are an Empire Builder\u2014and this show is for you!\n\nOn this podcast, your hosts Seychelle Van Poole, Sarah Reynolds, Vija Williams, and Wendy Papasan will discuss how to start and expand multi-million dollar businesses; smash through ceilings and barriers to unlock your fullest potential; foster amazing relationships, and become the best version of yourself.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 50,
      "total_episodes": 55,
      "listennotes_url": "https://www.listennotes.com/c/8f83465e290941dd9023cefbce02c208/",
      "explicit_content": false,
      "latest_pub_date_ms": 1619431200000,
      "earliest_pub_date_ms": 1589191200022,
      "listen_score_global_rank": "1%"
    },
    {
      "id": "e87ad18ee87a45319410c830afa5af75",
      "rss": "https://ark-invest.com/feed/podcast",
      "type": "episodic",
      "email": "info@ark-invest.com",
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
        "twitter_handle": "arkinvest",
        "facebook_handle": "ARKInvest",
        "instagram_handle": ""
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/fyi-for-your-innovation-ark-invest-F71XbnWfKHz-r_cwaPbSf5F.1400x1400.jpg",
      "title": "FYI - For Your Innovation",
      "country": "United States",
      "website": "https://ark-invest.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        93,
        98,
        111,
        127
      ],
      "itunes_id": 1271691895,
      "publisher": "ARK Invest",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/fyi-for-your-innovation-ark-invest-Jjk7c2xhY_Z-r_cwaPbSf5F.300x300.jpg",
      "is_claimed": false,
      "description": "The FYI \u2013 For Your Innovation Podcast offers an intellectual discussion on recent developments across disruptive innovation\u2014driven by research, news, controversies, companies, and technological breakthroughs.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 52,
      "total_episodes": 101,
      "listennotes_url": "https://www.listennotes.com/c/e87ad18ee87a45319410c830afa5af75/",
      "explicit_content": false,
      "latest_pub_date_ms": 1619819494000,
      "earliest_pub_date_ms": 1502443203000,
      "listen_score_global_rank": "0.5%"
    },
    {
      "id": "63517b0b5aa64fe2a7e47a5dff51357f",
      "rss": "https://anchor.fm/s/4afed8b0/podcast/rss",
      "type": "episodic",
      "email": "katscott310@gmail.com",
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
        "instagram_handle": "katrinascott"
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/live-beautifully-with-katrina-scott-0tfe4FODp3v--B3vMiGcqWO.1400x1400.jpg",
      "title": "Live Beautifully with Katrina Scott",
      "country": "United States",
      "website": "https://livebeautifully.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        67,
        171
      ],
      "itunes_id": 1552454666,
      "publisher": "Katrina Scott",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/live-beautifully-with-katrina-scott-RTvms3aCM9g--B3vMiGcqWO.300x300.jpg",
      "is_claimed": false,
      "description": "Welcome to the Live Beautifully Podcast! I\u2019m a mom, a passionate female founder, and a creative brand builder. \n\nThis podcast features advice and stories from female founders who have pioneered their space\u2014 brilliant entrepreneurs who started movements and built successful empires around their vision and dream. \n\nFrom personal stories to thoughtful conversations with the most empowering guests, and episodes answering your questions, this show will ignite your creative brilliance so you can flourish, succeed, and live beautifully. \nhttp://instagram.com/katrinascott\nhttp://LiveBeautifully.com\n",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 58,
      "total_episodes": 11,
      "listennotes_url": "https://www.listennotes.com/c/63517b0b5aa64fe2a7e47a5dff51357f/",
      "explicit_content": false,
      "latest_pub_date_ms": 1617947021000,
      "earliest_pub_date_ms": 1612543204002,
      "listen_score_global_rank": "0.5%"
    },
    {
      "id": "67f9f0a296144555834c28fcad3e1a7b",
      "rss": "https://mgntb.libsyn.com/rss",
      "type": "episodic",
      "email": "Podcast@McChrystalgroup.com",
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
        "twitter_handle": "mcchrystalgroup",
        "facebook_handle": "McChrystalGroup",
        "instagram_handle": ""
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/no-turning-back-stan-mcchrystal-EYBSkmK3lqb-4pnjwtcB1DH.1400x1400.jpg",
      "title": "No Turning Back",
      "country": "United States",
      "website": "http://mcchrystalgroup.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        97,
        67,
        93
      ],
      "itunes_id": 1527309309,
      "publisher": "Stan McChrystal",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/no-turning-back-stan-mcchrystal-S6nPRMTYJw9-4pnjwtcB1DH.300x300.jpg",
      "is_claimed": false,
      "description": "No Turning Back is a podcast by retired Army Four-Star General Stan McChrystal and former Navy SEAL Chris Fussell. In this series, they explore the future of leadership and teams with the world's most consequential leaders. From CEOs to political leaders to deep thinkers, Stan and Chris will bring you advice from the brightest minds about how to tackle the most pressing organizational and institutional challenges we face.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 44,
      "total_episodes": 37,
      "listennotes_url": "https://www.listennotes.com/c/67f9f0a296144555834c28fcad3e1a7b/",
      "explicit_content": false,
      "latest_pub_date_ms": 1619510400000,
      "earliest_pub_date_ms": 1597170248026,
      "listen_score_global_rank": "1.5%"
    },
    {
      "id": "eb0d7c4d258a4bf8b18f8224e770cc90",
      "rss": "http://feeds.soundcloud.com/users/soundcloud:users:634105539/sounds.rss",
      "type": "episodic",
      "email": "podcasts@asb.co.nz",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/asb-investment-podcast-syhpO_k6Pqj-8otAEespQO4.1400x1400.jpg",
      "title": "ASB Investment Podcast",
      "country": "New Zealand",
      "website": "http://soundcloud.com/asbinvestmentpodcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        67
      ],
      "itunes_id": 1465173590,
      "publisher": "ASB Bank",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/asb-investment-podcast-5YjugQo9fs2-8otAEespQO4.300x300.jpg",
      "is_claimed": false,
      "description": "A podcast that keeps you up to date on the market and helps you make smart choices with your investments.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": null,
      "total_episodes": 32,
      "listennotes_url": "https://www.listennotes.com/c/eb0d7c4d258a4bf8b18f8224e770cc90/",
      "explicit_content": false,
      "latest_pub_date_ms": 1619650690000,
      "earliest_pub_date_ms": 1558565902029,
      "listen_score_global_rank": null
    },
    {
      "id": "ee5a379e3041435a8ff2842e8c090da1",
      "rss": "https://www.spreaker.com/show/4104393/episodes/feed",
      "type": "episodic",
      "email": "podcasts@nzme.co.nz",
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
        "twitter_handle": "newstalkzb",
        "facebook_handle": "newstalkzb",
        "instagram_handle": ""
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/hp-business-class-newstalk-zb-r3dSWw4-e1v-SKIzVGLHr7_.1400x1399.jpg",
      "title": "HP Business Class",
      "country": "New Zealand",
      "website": "http://www.newstalkzb.co.nz?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        67
      ],
      "itunes_id": 1483427973,
      "publisher": "Newstalk ZB",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/hp-business-class-newstalk-zb-_JjN6VubXZL-SKIzVGLHr7_.300x299.jpg",
      "is_claimed": false,
      "description": "HP Business Class: The Story of New Zealand Business. The international award-winning podcast series from Newstalk ZB presented by Heather du Plessis-Allan. New Zealand has enjoyed an incredible level of business success given our population and proximity.  In this series we talk to some of New Zealand\u2019s key business leaders about their business journey\u2026 the wins, the losses, the learnings and more recently, adapting in a Covid-19 world.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": null,
      "total_episodes": 21,
      "listennotes_url": "https://www.listennotes.com/c/ee5a379e3041435a8ff2842e8c090da1/",
      "explicit_content": false,
      "latest_pub_date_ms": 1619586027000,
      "earliest_pub_date_ms": 1571037927015,
      "listen_score_global_rank": null
    },
    {
      "id": "385dc907b064492a8f70cf1b49b698a9",
      "rss": "https://www.rnz.co.nz/acast/businessnews.rss",
      "type": "episodic",
      "email": "webmaster@rnz.co.nz",
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
        "twitter_handle": "radionz",
        "facebook_handle": "RadioNewZealand",
        "instagram_handle": "radionewzealand"
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/rnz-business-news-rnz-ICU9Rp3QLeH-7K9al3F2bdt.1400x1400.jpg",
      "title": "RNZ: Business  News",
      "country": "New Zealand",
      "website": "https://www.rnz.co.nz/national/programmes/businessnews?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        93
      ],
      "itunes_id": 1455926997,
      "publisher": "RNZ",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/rnz-business-news-rnz-8PYmZ6XIpCE-7K9al3F2bdt.300x300.jpg",
      "is_claimed": false,
      "description": "The latest business news from RNZ News.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": null,
      "total_episodes": 1580,
      "listennotes_url": "https://www.listennotes.com/c/385dc907b064492a8f70cf1b49b698a9/",
      "explicit_content": false,
      "latest_pub_date_ms": 1619742000000,
      "earliest_pub_date_ms": 1574616060044,
      "listen_score_global_rank": null
    },
    {
      "id": "0f06e281c35c4f5ba7ccfdac5713fee5",
      "rss": "https://feeds.simplecast.com/hWY4QXG_",
      "type": "episodic",
      "email": "team@gorillahq.com",
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
        "twitter_handle": "nztechpodcast",
        "facebook_handle": "nztechpodcast",
        "instagram_handle": "paulspainnz"
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/nz-tech-podcast-podcasts-nz-aU8i6KhGcPV-Su6chZNq8bw.1400x1400.jpg",
      "title": "NZ Tech Podcast",
      "country": "United States",
      "website": "https://nztechpodcast.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        67,
        127,
        130,
        131,
        95
      ],
      "itunes_id": 421339518,
      "publisher": "Podcasts NZ / WorldPodcasts.com / Gorilla Voice Media",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/nz-tech-podcast-podcasts-nz-2IXl_Shu9RA-Su6chZNq8bw.300x300.jpg",
      "is_claimed": false,
      "description": "Each episode, Paul Spain and guests discuss what's happening in the world of technology, gadgets and telecommunications around the world and in New Zealand.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 27,
      "total_episodes": 535,
      "listennotes_url": "https://www.listennotes.com/c/0f06e281c35c4f5ba7ccfdac5713fee5/",
      "explicit_content": false,
      "latest_pub_date_ms": 1618450808000,
      "earliest_pub_date_ms": 1297944000533,
      "listen_score_global_rank": "10%"
    },
    {
      "id": "a007dfeeb40748fba8f98455860441ce",
      "rss": "https://rss.acast.com/business-is-boring",
      "type": "episodic",
      "email": "jane@thespinoff.co.nz",
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
        "twitter_handle": "TheSpinoffTV",
        "facebook_handle": "thespinofftv",
        "instagram_handle": "thespinofftv"
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/business-is-boring-the-spinoff-FW4hBpbEKRZ-Dv0ilbprJYS.1400x1400.jpg",
      "title": "Business Is Boring",
      "country": "New Zealand",
      "website": null,
      "language": "English",
      "genre_ids": [
        93,
        67
      ],
      "itunes_id": 1118188207,
      "publisher": "The Spinoff",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/business-is-boring-the-spinoff-G-W0nQvOLS1-Dv0ilbprJYS.300x300.jpg",
      "is_claimed": false,
      "description": "<p>Simon Pound speaks with innovators and commentators focused on the future of New Zealand. Presented by The Spinoff in association with Callaghan Innovation.</p>",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 29,
      "total_episodes": 206,
      "listennotes_url": "https://www.listennotes.com/c/a007dfeeb40748fba8f98455860441ce/",
      "explicit_content": false,
      "latest_pub_date_ms": 1619013600000,
      "earliest_pub_date_ms": 1489636777203,
      "listen_score_global_rank": "10%"
    },
    {
      "id": "c2a090b92bda49e4a01afd04828165f5",
      "rss": "https://feeds.simplecast.com/W225G50f",
      "type": "episodic",
      "email": "team@gorillahq.com",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/economy-watch-interestconz-podcasts-nz-E2jdumP64sb-m59D-F6TlQc.1400x1400.jpg",
      "title": "Economy Watch",
      "country": "United States",
      "website": "https://economywatch.simplecast.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        98,
        67
      ],
      "itunes_id": 1467130798,
      "publisher": "Interest.co.nz / Podcasts NZ, David Chaston",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/economy-watch-interestconz-podcasts-nz-i1wSqkjeJvg-m59D-F6TlQc.300x300.jpg",
      "is_claimed": false,
      "description": "We follow the economic events and trends that affect New Zealand.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": null,
      "total_episodes": 475,
      "listennotes_url": "https://www.listennotes.com/c/c2a090b92bda49e4a01afd04828165f5/",
      "explicit_content": false,
      "latest_pub_date_ms": 1619725353000,
      "earliest_pub_date_ms": 1559789236474,
      "listen_score_global_rank": null
    },
    {
      "id": "6d613b1f9aef4977a70ece537375b6b2",
      "rss": "https://feeds.megaphone.fm/clarkhoward",
      "type": "episodic",
      "email": "admin@clark.com",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-clark-howard-podcast-clark-howard-bmBjt_SynD5-KusgFWdArBl.1400x1400.jpg",
      "title": "The Clark Howard Podcast",
      "country": "United States",
      "website": "https://www.clark.com/podcasts?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        93,
        111,
        98,
        122,
        123,
        144
      ],
      "itunes_id": 207724573,
      "publisher": "Clark Howard",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-clark-howard-podcast-clark-howard-zl9MwbscV8F-KusgFWdArBl.300x300.jpg",
      "is_claimed": false,
      "description": "Save more and spend less is more than just a motto for money expert Clark Howard; it\u2019s a way of life. Clark and his crew \u2014 Team Clark \u2014 are on a mission to empower people to take control of their personal finances by providing money-saving tips, consumer advice, hot deals and economic news to help everyone achieve financial freedom. Clark is a nationally syndicated radio talk show host and a consumer reporter for television stations around the country. His podcast, The Clark Howard Show, receives more than one million downloads each month and is a hub for listeners to get valuable advice on-demand any time. Clark answers questions on the most popular business and consumer topics including; how to buy a cars, financing a home, retirement planning, shopping for insurance and getting the most out of your savings. Join the conversation and submit your question to www.clark.com/askclark . Clark spearheads two free resources \u2014 Clark.com and ClarkDeals.com \u2014 to encourage consumers to save more, spend less and avoid ripoffs.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 67,
      "total_episodes": 1109,
      "listennotes_url": "https://www.listennotes.com/c/6d613b1f9aef4977a70ece537375b6b2/",
      "explicit_content": false,
      "latest_pub_date_ms": 1619809200000,
      "earliest_pub_date_ms": 1486699261108,
      "listen_score_global_rank": "0.1%"
    },
    {
      "id": "f90e73f830774f698952fa39d0fba7ae",
      "rss": "https://rss.art19.com/business-movers",
      "type": "serial",
      "email": "iwonder@wondery.com",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/business-movers-wondery-kB_rebc8WYp-ALQ_sbGh428.1400x1400.jpg",
      "title": "Business Movers",
      "country": "United States",
      "website": "https://wondery.com/shows/business-movers/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        93,
        171
      ],
      "itunes_id": 1546027998,
      "publisher": "Wondery",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/business-movers-wondery-_aiFshgjHSX-ALQ_sbGh428.300x300.jpg",
      "is_claimed": false,
      "description": "\n      <p>Behind every successful business is a story. It starts with a vision and a leap of faith. Along the way, leaders make bold decisions, ride booms and busts, and sometimes, they reach new heights. From Wondery, the makers of the hit series&nbsp;<em>Business Wars</em>, and Lindsay Graham, the host of&nbsp;<em>American History Tellers</em>&nbsp;and&nbsp;<em>American Scandal</em>, comes a weekly podcast that brings you the true stories of the brilliant but all-too-human businesspeople who risked it all. From Walt Disney\u2019s creation of a theme park in Orlando, to the colossal failure of New Coke,&nbsp;<em>Business Movers&nbsp;</em>will explore the triumphs, failures and ideas that transformed our lives.</p>\n    ",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 54,
      "total_episodes": 21,
      "listennotes_url": "https://www.listennotes.com/c/f90e73f830774f698952fa39d0fba7ae/",
      "explicit_content": false,
      "latest_pub_date_ms": 1619686800000,
      "earliest_pub_date_ms": 1608315179012,
      "listen_score_global_rank": "0.5%"
    },
    {
      "id": "837e02f42c5649079d6cd3c5b5fa003f",
      "rss": "http://dontstopusnow.co/feed/podcast/",
      "type": "episodic",
      "email": "claire@dontstopusnow.co",
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
        "facebook_handle": "dontstopusnow",
        "instagram_handle": "dontstopusnowpodcast"
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/dont-stop-us-now-podcast-claire-hatton-LjpdZ216tyz-SHNq1LRiB-2.1400x1400.jpg",
      "title": "Don't Stop Us Now! Podcast",
      "country": "United States",
      "website": "https://dontstopusnow.co?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        97,
        94,
        90,
        88,
        67
      ],
      "itunes_id": 1389061373,
      "publisher": "Claire Hatton & Greta Thomas",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/dont-stop-us-now-podcast-claire-hatton-45xqKt0mVaB-SHNq1LRiB-2.300x300.jpg",
      "is_claimed": false,
      "description": "Authentic stories and practical advise from awesome, innovative women from around the globe.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 46,
      "total_episodes": 106,
      "listennotes_url": "https://www.listennotes.com/c/837e02f42c5649079d6cd3c5b5fa003f/",
      "explicit_content": true,
      "latest_pub_date_ms": 1619509367000,
      "earliest_pub_date_ms": 1526783763096,
      "listen_score_global_rank": "1%"
    },
    {
      "id": "ddb3978d555c43b28b95f05c9ff2f6aa",
      "rss": "https://rss.whooshkaa.com/rss/podcast/id/5927",
      "type": "episodic",
      "email": "philip@muscatello.com.au",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/shares-for-beginners-philip-muscatello-ekOYICL2-BQ-bZvPdjoUGkz.1400x1400.jpg",
      "title": "Shares for Beginners",
      "country": "Australia",
      "website": "https://player.whooshkaa.com/shows/shares-for-beginners?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        98,
        67
      ],
      "itunes_id": 1451778025,
      "publisher": "Philip Muscatello",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/shares-for-beginners-philip-muscatello-qYD-ZMrWSet-bZvPdjoUGkz.300x300.jpg",
      "is_claimed": true,
      "description": "I interview industry experts so you'll learn what to do, what to ask and - ideally - how not to lose money.\nI'm just like you I want to make money from the stock market but I find the terminology confusing. I want to be able to make informed decisions. Let's learn together on Shares for Beginners.\n\nShares for Beginners is for information and educational purposes only.  It isn\u2019t financial advice, and you shouldn\u2019t buy or sell any investment based on what you\u2019ve heard here. Any opinion or commentary is the view of the speaker only not Shares for Beginners.  This podcast doesn\u2019t replace professional advice regarding your personal financial needs, circumstances or current situation.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": null,
      "total_episodes": 50,
      "listennotes_url": "https://www.listennotes.com/c/ddb3978d555c43b28b95f05c9ff2f6aa/",
      "explicit_content": false,
      "latest_pub_date_ms": 1606262559000,
      "earliest_pub_date_ms": 1549829100042,
      "listen_score_global_rank": null
    },
    {
      "id": "bdaf74a01a0a4578b82f3d83475db8d1",
      "rss": "https://rss.acast.com/7am",
      "type": "episodic",
      "email": "team@7ampodcast.com.au",
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
        "twitter_handle": "7ampodcast",
        "facebook_handle": "7ampodcast",
        "instagram_handle": "7ampodcast"
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/7am-schwartz-media-HFRgYGK1ahE-i_1XqL7jHSt.1400x1400.jpg",
      "title": "7am",
      "country": "Australia",
      "website": "http://7ampodcast.com.au?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        99,
        67
      ],
      "itunes_id": 1461999702,
      "publisher": "Schwartz Media",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/7am-schwartz-media-43tzUbC-2Wm-i_1XqL7jHSt.300x300.jpg",
      "is_claimed": false,
      "description": "A daily news show from the publisher of The Monthly and The Saturday Paper. Hear from the country\u2019s best reporters, covering the news as it affects Australia. This is news with narrative, every weekday.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 61,
      "total_episodes": 484,
      "listennotes_url": "https://www.listennotes.com/c/bdaf74a01a0a4578b82f3d83475db8d1/",
      "explicit_content": false,
      "latest_pub_date_ms": 1619809200000,
      "earliest_pub_date_ms": 1556589009404,
      "listen_score_global_rank": "0.5%"
    },
    {
      "id": "b5da0338c2aa4519beb1b84f0fb6858f",
      "rss": "https://rss.acast.com/so-i-quit-my-day-job",
      "type": "serial",
      "email": "cath@rubyred.com.au",
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
        "twitter_handle": "whimn_au",
        "facebook_handle": "whimn.au",
        "instagram_handle": "whimn"
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/so-i-quit-my-day-job-whimncomau-_Q7jw9exPbl-va2U0AYDXiE.1400x1400.jpg",
      "title": "So, I Quit My Day Job",
      "country": "Australia",
      "website": "https://play.acast.com/s/so-i-quit-my-day-job?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        111,
        122,
        67,
        181,
        124
      ],
      "itunes_id": 1496517561,
      "publisher": "Cathrine Mahoney",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/so-i-quit-my-day-job-whimncomau-AeMZ6-8myR7-va2U0AYDXiE.300x300.jpg",
      "is_claimed": false,
      "description": "<p>A podcast that travels the bumpy road to achieving your dreams and speaks to those who have successfully made the leap.</p><p>Have you ever wanted to quit your day job and follow your dream career? Cathrine Mahoney did it. It wasn't easy, but she gave up a cushy job as a celebrity publicist and decided to try and make it as an author. But she's going to need some help! Every week Cathrine will be speaking to a different person who has quit their jobs and followed their heart and getting their advice.</p><p>From overcoming doubt, to coping with rejection  \u2013 Cathrine will cover it all.&nbsp;</p>",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 47,
      "total_episodes": 111,
      "listennotes_url": "https://www.listennotes.com/c/b5da0338c2aa4519beb1b84f0fb6858f/",
      "explicit_content": false,
      "latest_pub_date_ms": 1619463600000,
      "earliest_pub_date_ms": 1579236754092,
      "listen_score_global_rank": "1%"
    },
    {
      "id": "96bee96368124ca8b001e9263be0aa07",
      "rss": "https://rss.acast.com/funny-business",
      "type": "episodic",
      "email": "lachyshoots@gmail.com",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/funny-business-lachlan-bradford-robbie-hicks-2qGQevW5mlM-qxrEytR-kjM.1400x1400.jpg",
      "title": "Funny Business",
      "country": "United States",
      "website": "https://play.acast.com/s/funny-business?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        122,
        67
      ],
      "itunes_id": 1508669714,
      "publisher": "Lachlan Bradford, Robbie Hicks",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/funny-business-lachlan-bradford-robbie-hicks-VYy7kfFQh0x-qxrEytR-kjM.300x300.jpg",
      "is_claimed": false,
      "description": "<p>A podcast for free thinkers and creators exploring business culture and performance in Australia and abroad. Hosted by Robbie Hicks and Lachlan Bradford.</p>",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 42,
      "total_episodes": 185,
      "listennotes_url": "https://www.listennotes.com/c/96bee96368124ca8b001e9263be0aa07/",
      "explicit_content": true,
      "latest_pub_date_ms": 1619738288000,
      "earliest_pub_date_ms": 1587270600113,
      "listen_score_global_rank": "2%"
    },
    {
      "id": "e8073ec696a84e73bb7d29452f8708eb",
      "rss": "https://rss.acast.com/the-helpdesk",
      "type": "episodic",
      "email": "fulltimecasual@gmail.com",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-helpdesk-a-tech-podcast-for-the-rest-of-2AuLX-vlVWp-7YXWiJD-h1G.1400x1400.jpg",
      "title": "The Helpdesk",
      "country": "Australia",
      "website": "https://thehelpdesk.com.au/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        67,
        127,
        131,
        99
      ],
      "itunes_id": 1534830303,
      "publisher": "Peter Wells",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-helpdesk-a-tech-podcast-for-the-rest-of-nzqedtCgS7u-7YXWiJD-h1G.300x300.jpg",
      "is_claimed": false,
      "description": "<p>A daily tech podcast from Australian journalists Peter Wells and Tess Bennett</p>",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 33,
      "total_episodes": 104,
      "listennotes_url": "https://www.listennotes.com/c/e8073ec696a84e73bb7d29452f8708eb/",
      "explicit_content": false,
      "latest_pub_date_ms": 1618014574000,
      "earliest_pub_date_ms": 1602041759043,
      "listen_score_global_rank": "5%"
    },
    {
      "id": "5fc30358c0d34e73937661f7c35aa88a",
      "rss": "https://rss.acast.com/no-bullsht-leadership",
      "type": "episodic",
      "email": "hello@yourceomentor.com",
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
        "facebook_handle": "yourceomentor",
        "instagram_handle": "yourceomentor"
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/no-bullsht-leadership-martin-moore-BJyps-Ghxj7-34I1mfTDVwB.1400x1400.jpg",
      "title": "No Bullsh!t Leadership",
      "country": "United States",
      "website": "http://www.yourceomentor.com/podcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        181,
        111,
        97,
        94,
        67,
        173,
        78,
        77
      ],
      "itunes_id": 1434654553,
      "publisher": "Martin G Moore",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/no-bullsht-leadership-martin-moore-Ww7e1zXJEqf-34I1mfTDVwB.300x300.jpg",
      "is_claimed": false,
      "description": "<p>No Bullsh!t Leadership is a podcast for leaders who want to become truly exceptional. Each week, your host Martin Moore shares the secrets of high performance leadership; the career accelerators that you can\u2019t learn in business school, and your boss is unlikely to share with you. Step away from the theoretical view on leadership, and learn from a successful CEO who\u2019s already walked the path.</p>",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 52,
      "total_episodes": 140,
      "listennotes_url": "https://www.listennotes.com/c/5fc30358c0d34e73937661f7c35aa88a/",
      "explicit_content": false,
      "latest_pub_date_ms": 1619551500000,
      "earliest_pub_date_ms": 1535610300113,
      "listen_score_global_rank": "0.5%"
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
    "hu": "Hungaria",
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
      "rss": "http://bryankramer.libsyn.com/rss",
      "type": "episodic",
      "email": "bryan.kramer@purematter.com",
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
        "twitter_handle": "bryankramer",
        "facebook_handle": "",
        "instagram_handle": ""
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-bryan-kramer-show-bryan-kramer-Br0M_IayKc3-0SCl91ZT-bU.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-bryan-kramer-show-bryan-kramer-E7o80typv_b-0SCl91ZT-bU.300x300.jpg",
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
      "id": "99a8f88389c54382a300a363c74e9f26",
      "rss": "http://goaldiggerpodcast.libsyn.com/rss",
      "type": "episodic",
      "email": "Hello@JennaKutcher.com",
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
        "twitter_handle": "jennakutcher",
        "facebook_handle": "jenna.kutcher",
        "instagram_handle": "jennakutcher"
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-goal-digger-podcast-jenna-kutcher-YtWU_lEBuPM-BZgM5JWRnhY.1400x1400.jpg",
      "title": "The Goal Digger Podcast",
      "country": "United States",
      "website": "http://www.goaldiggerpodcast.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        94,
        173,
        93,
        171,
        67,
        97
      ],
      "itunes_id": 1178704872,
      "publisher": "Jenna Kutcher",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-goal-digger-podcast-jenna-kutcher-2rzxJY6oM0t-BZgM5JWRnhY.300x300.jpg",
      "is_claimed": false,
      "description": "How do I build my dream job? How do I make money online? Am I ready to leave my 9 to 5? How can I create passive income? How can I grow my Instagram following? And the biggest question of all, can I *really* turn my passion into profits? \n\nWelcome to the Goal Digger Podcast where we will answer ALL of these questions and so much more! Week after week, host Jenna Kutcher brings you the the productivity tips, social media strategies, business hacks,, and inspirational stories that can help YOU design your dream career. Jenna shares tangible tips and hacks that she used to become a self-made millionaire in photography, online courses, Instagram sponsorships, and navigating the world of being a #girlboss social media influencer. Along with sharing her best kept secrets, she interviews the best in the industry (Amy Porterfield, Jamie Ivey, Melyssa Griffin, Lori Harder, Cathy Heller and so much more) who will share their secrets to ensure you are seen, heard, (and hired!) \n\nWith millions of downloads and counting, the Goal Digger Movement is growing every day and now it\u2019s YOUR TURN to hear from the experts, get inspired, and tackle your biggest goals along the way.  \n\nWhat do you say? Are you in?  Because we believe that work doesn\u2019t have to feel like work.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 77,
      "total_episodes": 484,
      "listennotes_url": "https://www.listennotes.com/c/99a8f88389c54382a300a363c74e9f26/",
      "explicit_content": false,
      "latest_pub_date_ms": 1619598600000,
      "earliest_pub_date_ms": 1479465760438,
      "listen_score_global_rank": "0.01%"
    },
    {
      "id": "10954ad3114841e18abad343b3a9156f",
      "rss": "http://feeds.bloomberg.fm/BLM6442452948",
      "type": "episodic",
      "email": "podcasts@bloomberg.net",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/bloomberg-businessweek-bloomberg-radio-Ft6c9ksGVJ_-yn5Mm7jSGBe.1400x1400.jpg",
      "title": "Bloomberg Businessweek",
      "country": "United States",
      "website": "https://bloomberg.com/podcasts/advantage?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        93,
        95,
        98
      ],
      "itunes_id": 393107187,
      "publisher": "Bloomberg Radio",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/bloomberg-businessweek-bloomberg-radio-hOqQSF4gxpa-yn5Mm7jSGBe.300x300.jpg",
      "is_claimed": false,
      "description": "Carol Massar and Tim Stenovec bring together the latest news from the world of business and finance and the interesting stories of global technology, politics, economics and more by harnessing the power of Bloomberg Businessweek reporters and editors.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 49,
      "total_episodes": 2461,
      "listennotes_url": "https://www.listennotes.com/c/10954ad3114841e18abad343b3a9156f/",
      "explicit_content": false,
      "latest_pub_date_ms": 1619859600000,
      "earliest_pub_date_ms": 1493922948347,
      "listen_score_global_rank": "1%"
    },
    {
      "id": "27a163c3bbe64ff89036c1a328fc5c7e",
      "rss": "https://mindyourbusiness.libsyn.com/rss",
      "type": "episodic",
      "email": "support@jameswedmore.com",
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
        "instagram_handle": "jameswedmore"
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-mind-your-business-podcast-james-wedmore-E-iYI8LufOC-s4mokaucvUK.1400x1400.jpg",
      "title": "The Mind Your Business Podcast",
      "country": "United States",
      "website": "http://www.mindyourbusinesspodcast.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        93,
        97
      ],
      "itunes_id": 1074394632,
      "publisher": "James Wedmore",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-mind-your-business-podcast-james-wedmore-aO78F2dHgre-s4mokaucvUK.300x300.jpg",
      "is_claimed": false,
      "description": "All entrepreneurs want to know the secret to success. James Wedmore, a seven-figure online entrepreneur, believes success is created by mindset over strategy, magic over metrics, and attitude over action. In this podcast, James untangles the common misconception that hustle and hard work are all it takes to be successful.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 63,
      "total_episodes": 376,
      "listennotes_url": "https://www.listennotes.com/c/27a163c3bbe64ff89036c1a328fc5c7e/",
      "explicit_content": false,
      "latest_pub_date_ms": 1619685000000,
      "earliest_pub_date_ms": 1452591000374,
      "listen_score_global_rank": "0.1%"
    },
    {
      "id": "7ad1e45c655244298e9806c7a0bdccbf",
      "rss": "https://www.omnycontent.com/d/playlist/aaea4e69-af51-495e-afc9-a9760146922b/04343ddf-4cf2-4c01-900c-ab580181221a/fa85f081-7e46-4157-bc94-ab58018153d2/podcast.rss",
      "type": "episodic",
      "email": "podcasts@own.oprah.com",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-oprah-winfrey-show-the-podcast-the-pAdnyh582S7-NYPIE8gGpVd.1400x1400.jpg",
      "title": "The Oprah Winfrey Show: The Podcast",
      "country": "United States",
      "website": "http://www.oprah.com/app/the-oprah-winfrey-show.html?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        122
      ],
      "itunes_id": 1499860465,
      "publisher": "The Oprah Winfrey Show: The Podcast",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-oprah-winfrey-show-the-podcast-the-f4rv_H7w9QE-NYPIE8gGpVd.300x300.jpg",
      "is_claimed": false,
      "description": "<p>Oprah is opening the vault of The Oprah Winfrey Show with 25 years of hand-picked legendary interviews, a-ha moments, ugly cries and unforgettable surprises. A lot has changed since she ended the show, but many of our personal struggles have stayed the same. We&rsquo;re all still looking to connect, to be seen and to know that we&rsquo;re not alone. We&rsquo;re also looking for some joy, some laughs and some much-needed inspiration. As we head into this new decade, what better time to look back and reflect, to take stock of how we&rsquo;ve grown and to be reminded that we&rsquo;re all in this together. The Oprah Winfrey Show aired from September 8th, 1986 to May 25, 2011 with 4,561 episodes. The show remains the highest-rated daytime talk show in American television history, averaging between 10 to 20 million viewers a day.</p>\n<p><br><br><br></p>",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 58,
      "total_episodes": 72,
      "listennotes_url": "https://www.listennotes.com/c/7ad1e45c655244298e9806c7a0bdccbf/",
      "explicit_content": false,
      "latest_pub_date_ms": 1619499600000,
      "earliest_pub_date_ms": 1582217175059,
      "listen_score_global_rank": "0.5%"
    },
    {
      "id": "85c0e9f89f7c41aaa7420cd3b2424a26",
      "rss": "https://feeds.megaphone.fm/happinesslab",
      "type": "episodic",
      "email": "marketing@pushkin.fm",
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
        "twitter_handle": "pushkinpods",
        "facebook_handle": "pushkinpods",
        "instagram_handle": "pushkinpods"
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-happiness-lab-with-dr-laurie-santos-w8a0fegkMVJ-hB3PAqrH5Eu.1400x1400.jpg",
      "title": "The Happiness Lab with Dr. Laurie Santos",
      "country": "United States",
      "website": "https://www.pushkin.fm?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        90,
        191,
        67,
        122,
        111
      ],
      "itunes_id": 1474245040,
      "publisher": "Pushkin Industries ",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-happiness-lab-with-dr-laurie-santos-gVb_zWf7Xsc-hB3PAqrH5Eu.300x300.jpg",
      "is_claimed": false,
      "description": "You might think you know what it takes to lead a happier life\u2026 more money, a better job, or Instagram-worthy vacations. You\u2019re dead wrong. Yale professor Dr. Laurie Santos has studied the science of happiness and found that many of us do the exact opposite of what will truly make our lives better. Based on the psychology course she teaches at Yale--the most popular class in the university\u2019s 300-year history--Laurie will take you through the latest scientific research and share some surprising and inspiring stories that will change the way you think about happiness. For an even deeper dive into the research we talk about in the show and to sign up to our newsletter visit: happinesslab.fmiHeartMedia is the exclusive podcast partner of Pushkin Industries.\u00a0",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 78,
      "total_episodes": 56,
      "listennotes_url": "https://www.listennotes.com/c/85c0e9f89f7c41aaa7420cd3b2424a26/",
      "explicit_content": false,
      "latest_pub_date_ms": 1619409900000,
      "earliest_pub_date_ms": 1564005721051,
      "listen_score_global_rank": "0.01%"
    },
    {
      "id": "499661f3589f42aaa1532673e0e0aedf",
      "rss": "http://feeds.feedburner.com/spipodcast",
      "type": "episodic",
      "email": "podcasts@teamspi.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "",
        "spotify_url": "",
        "youtube_url": "https://www.youtube.com/user/smartpassiveincome",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "patflynn",
        "facebook_handle": "smartpassiveincome",
        "instagram_handle": "patflynn"
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-smart-passive-income-online-business-E0q3g-kJn7S-NDa6-ySp9kw.1400x1400.jpg",
      "title": "The Smart Passive Income Online Business and Blogging Podcast",
      "country": "United States",
      "website": "https://art19.com/shows/smart-passive-income-podcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        171,
        93,
        173,
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-smart-passive-income-online-business-GMDAkxml0VU-NDa6-ySp9kw.300x300.jpg",
      "is_claimed": false,
      "description": "\n      Pat Flynn from The Smart Passive Income Blog reveals all of his online business and blogging strategies, income sources and killer marketing tips and tricks so you can be ahead of the curve with your online business or blog. Discover how you can create multiple passive income streams that work for you so that you can have the time and freedom to do what you love, whether it's traveling the world, or just living comfortably at home. Since 2008, he's been supporting his family with his many online businesses, and he's been openly sharing his wins, his losses, and all the lessons in between with the community of energetic but humble entrepreneurs who follow him. Self-proclaimed \"crash test dummy of online business\", you'll learn about building authority online, email marketing, building a team and outsourcing, content marketing, podcasting, search engine optimization, niche sites, social media strategies, how to get more traffic, creating online courses, affiliate marketing, and productivity tips so that you create something amazing without burning yourself out. It's a mix of interviews, special co-hosts and solo shows from Pat you're not going to want to miss. Hit subscribe, and get ready to change your life.\n    ",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 72,
      "total_episodes": 632,
      "listennotes_url": "https://www.listennotes.com/c/499661f3589f42aaa1532673e0e0aedf/",
      "explicit_content": false,
      "latest_pub_date_ms": 1619766000000,
      "earliest_pub_date_ms": 1279551600475,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "10f6132cd44042ecbb693973a7f9fdbf",
      "rss": "https://feed.pippa.io/public/shows/5aecaca3a15c2dd12887881a",
      "type": "episodic",
      "email": "info+5aecaca3a15c2dd12887881a@mg.pippa.io",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "",
        "spotify_url": "",
        "youtube_url": "https://www.youtube.com/user/ultrawellness",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "drmarkhyman",
        "instagram_handle": "markhymanmd"
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-doctors-farmacy-with-mark-hyman-md-dr-zw67GgQIqY2.1400x1400.jpg",
      "title": "The Doctor's Farmacy with Mark Hyman, M.D.",
      "country": "United States",
      "website": "http://drhyman.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        91,
        89,
        88,
        67
      ],
      "itunes_id": 1382804627,
      "publisher": "Dr. Mark Hyman",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-doctors-farmacy-with-mark-hyman-md-dr-zw67GgQIqY2.300x300.jpg",
      "is_claimed": false,
      "description": "We are seeing an ever-increasing burden of chronic disease, primarily driven by our food and food system. This is perpetuated by agricultural, food and health care policies that don\u2019t support health. We need to rethink disease and reimagine a food system and a health care system the protects health, unburdens the economy from the weight of obesity and chronic disease, protects the environment, helps reverse climate change and creates a nation of healthy children and citizens. This podcast is a place for deep conversations about the critical issues of our time in the space of health, wellness, food and politics. New episodes are released every Monday, Wednesday, and Friday morning. I hope you'll join me.<br /><hr><p style='color:grey; font-size:0.75em;'> See <a style='color:grey;' target='_blank' rel='noopener noreferrer' href='https://acast.com/privacy'>acast.com/privacy</a> for privacy and opt-out information.</p>",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 71,
      "total_episodes": 349,
      "listennotes_url": "https://www.listennotes.com/c/10f6132cd44042ecbb693973a7f9fdbf/",
      "explicit_content": false,
      "latest_pub_date_ms": 1619776835000,
      "earliest_pub_date_ms": 1525798147259,
      "listen_score_global_rank": "0.05%"
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
      "id": "6bbdd8cf36894d27b52c778db363319a",
      "link": "https://lexfridman.com/jason-calacanis/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/6bbdd8cf36894d27b52c778db363319a/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/lex-fridman-podcast-ai-lex-fridman-mH9GfIiTzSb-YRs7Zkd0n4l.1400x1400.jpg",
      "title": "#161 \u2013 Jason Calacanis: Startups, Angel Investing, Capitalism, and Friendship",
      "podcast": {
        "id": "23e2be3c56e64dcdbb0cff3cedca4c95",
        "image": "https://cdn-images-1.listennotes.com/podcasts/lex-fridman-podcast-ai-lex-fridman-mH9GfIiTzSb-YRs7Zkd0n4l.1400x1400.jpg",
        "title": "Lex Fridman Podcast",
        "publisher": "Lex Fridman",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/lex-fridman-podcast-ai-lex-fridman-jiYnRwU6vdz-YRs7Zkd0n4l.300x300.jpg",
        "listen_score": 72,
        "listennotes_url": "https://www.listennotes.com/c/23e2be3c56e64dcdbb0cff3cedca4c95/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/lex-fridman-podcast-ai-lex-fridman-jiYnRwU6vdz-YRs7Zkd0n4l.300x300.jpg",
      "description": "Jason Calacanis is an angel investor, entrepreneur, and co-host of All-In Podcast and This Week in Startups. Please support this podcast by checking out our sponsors: \u2013 Brave: https://brave.com/lex \u2013 Linode: https://linode.com/lex to get $100 free credit \u2013 Four Sigmatic: https://foursigmatic.com/lex and use code LexPod to get up to 60% off \u2013 Rev: https://rev.ai/lex to get 7-day free trial EPISODE LINKS: Jason\u2019s Twitter: https://twitter.com/Jason Jason\u2019s Website: https://calacanis.com/ Jason\u2019s YouTube: https://www.youtube.com/user/ThisWeekIn Jason\u2019s Link Tree: https://linktr.ee/calacanis All-In Podcast: https://linktr.ee/allinpodcast This Week in Startups Podcast: https://thisweekinstartups.com/about/ PODCAST INFO: Podcast website: https://lexfridman.com/podcast Apple Podcasts: https://apple.co/2lwqZIr Spotify: https://spoti.fi/2nEwCF8 RSS: https://lexfridman.com/feed/podcast/ YouTube Full Episodes: https://youtube.com/lexfridman YouTube",
      "pub_date_ms": 1613398049012,
      "guid_from_rss": "https://lexfridman.com/?p=4530",
      "listennotes_url": "https://www.listennotes.com/e/6bbdd8cf36894d27b52c778db363319a/",
      "audio_length_sec": 8190,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/6bbdd8cf36894d27b52c778db363319a/#edit"
    },
    {
      "id": "b9d13637a7074a3c990f9f166b728e1e",
      "link": "https://allinchamathjason.libsyn.com/e16-reflecting-on-the-riots-at-the-us-capitol-plus-georgia-runoff-elections-vaccine-distribution-more?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/b9d13637a7074a3c990f9f166b728e1e/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/all-in-with-chamath-jason-sacks-friedberg-NpyF_7WBYua-0eWaLuirNTJ.1400x1400.jpg",
      "title": "E16: Reflecting on the riots at the US Capitol, plus: Georgia runoff elections, vaccine distribution & more",
      "podcast": {
        "id": "40b72ce8610649529542575dedf06c86",
        "image": "https://cdn-images-1.listennotes.com/podcasts/all-in-with-chamath-jason-sacks-friedberg-NpyF_7WBYua-0eWaLuirNTJ.1400x1400.jpg",
        "title": "All-In with Chamath, Jason, Sacks & Friedberg",
        "publisher": "Jason Calacanis",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/all-in-with-chamath-jason-sacks-friedberg-yCpUza38HRh-0eWaLuirNTJ.300x300.jpg",
        "listen_score": 63,
        "listennotes_url": "https://www.listennotes.com/c/40b72ce8610649529542575dedf06c86/",
        "listen_score_global_rank": "0.1%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/all-in-with-chamath-jason-sacks-friedberg-yCpUza38HRh-0eWaLuirNTJ.300x300.jpg",
      "description": "<p>Follow the crew:</p> <p><a href= \"https://twitter.com/chamath\">https://twitter.com/chamath</a></p> <p><a href= \"https://linktr.ee/calacanis\">https://linktr.ee/calacanis</a></p> <p><a href= \"https://twitter.com/DavidSacks\">https://twitter.com/DavidSacks</a></p> <p><a href= \"https://twitter.com/friedberg\">https://twitter.com/friedberg</a></p> <p>Follow the pod:</p> <p><a href= \"https://twitter.com/theallinpod\">https://twitter.com/theallinpod</a></p> <p><a href= \"https://linktr.ee/allinpodcast\">https://linktr.ee/allinpodcast</a></p> <p>Intro Music Credit:</p> <p><a href=\"https://rb.gy/aizgdm\">https://rb.gy/aizgdm</a></p> <p>Intro Video Credit:</p> <p><a href= \"https://twitter.com/MikeSylvan\">https://twitter.com/MikeSylvan</a></p> <p>Referenced in the show:</p> <p>The Killer D.A. by David Sacks</p> <p><a href=\"https://rb.gy/k5rz0k\">https://rb.gy/k5rz0k</a></p> <p>Show Notes:</p> <p>0:00 New intro for the besties - listen here: <a href= \"https://rb.gy/aizgdm\">https://rb.gy/aizgdm</a></p> <p>2:14 Sacks' trip to Miami</p> <p>6:01 Reflecting on the riot at the US Capitol: police response, double standard with BLM protest, big picture, prosecuting Trump & healing the nation post-Trump</p> <p>29:43 2016 Election interference, reasons for unrest & polarization, Trump's culpability</p> <p>44:19 Should the 25th Amendment be invoked?</p> <p>49:51 Democrats win Georgia runoff elections, did Trump's implosion lose Georgia for the GOP?</p> <p>56:23 How Friedberg would handle vaccine distribution</p> <p>1:07:45 San Francisco's Killer D.A., recalling Gavin Newsom, Kim Kardashian for Governor of CA</p>",
      "pub_date_ms": 1610088436000,
      "guid_from_rss": "79029f1c-824a-424d-a8d2-1ebd29506c6e",
      "listennotes_url": "https://www.listennotes.com/e/b9d13637a7074a3c990f9f166b728e1e/",
      "audio_length_sec": 4979,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/b9d13637a7074a3c990f9f166b728e1e/#edit"
    },
    {
      "id": "f899c0d4d8cd448ca91b6821c0e18f0f",
      "link": "https://share.transistor.fm/s/353d5b5b?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/f899c0d4d8cd448ca91b6821c0e18f0f/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/rework-basecamp-Ah8QgG7fNp9-rQRTM0OpCAo.1400x1400.jpg",
      "title": "Extreme Capitalism with Jason Calacanis",
      "podcast": {
        "id": "bde518d2cb22433d8f7a1e16e18aa1b7",
        "image": "https://cdn-images-1.listennotes.com/podcasts/rework-basecamp-Ah8QgG7fNp9-rQRTM0OpCAo.1400x1400.jpg",
        "title": "Rework",
        "publisher": "Basecamp",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/rework-basecamp-Dq6sV2huSAe-rQRTM0OpCAo.300x300.jpg",
        "listen_score": 50,
        "listennotes_url": "https://www.listennotes.com/c/bde518d2cb22433d8f7a1e16e18aa1b7/",
        "listen_score_global_rank": "1%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/rework-basecamp-Dq6sV2huSAe-rQRTM0OpCAo.300x300.jpg",
      "description": "Basecamp co-founder and CTO David Heinemeier Hansson and entrepreneur and angel investor Jason Calacanis debate the gig economy, democratic socialism, and whether the American dream is dead. The conversation in this episode is adapted from a longer interview that can be found in full at <a href=\"https://thisweekinstartups.com/e1029-basecamp-co-founder-author-david-heinemeier-hansson-dhh-debates-jason-on-reining-in-capitalism-benefits-of-state-run-education-healthcare-big-tech-disappointments-work-from-home-parad/\">This Week in Startups</a>.",
      "pub_date_ms": 1582203600033,
      "guid_from_rss": "b8af76cb-4f92-44b1-aa47-ac469a043b64",
      "listennotes_url": "https://www.listennotes.com/e/f899c0d4d8cd448ca91b6821c0e18f0f/",
      "audio_length_sec": 3582,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/f899c0d4d8cd448ca91b6821c0e18f0f/#edit"
    },
    {
      "id": "512830b5fdfb43569f0019b854c5d67f",
      "link": "https://allinchamathjason.libsyn.com/e18-inauguration-talk-breaking-down-the-19t-stimulus-the-case-for-recalling-gavin-newsom-more?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/512830b5fdfb43569f0019b854c5d67f/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/all-in-with-chamath-jason-sacks-friedberg-NpyF_7WBYua-0eWaLuirNTJ.1400x1400.jpg",
      "title": "E18: Inauguration talk, breaking down the $1.9T stimulus, the case for recalling Gavin Newsom & more",
      "podcast": {
        "id": "40b72ce8610649529542575dedf06c86",
        "image": "https://cdn-images-1.listennotes.com/podcasts/all-in-with-chamath-jason-sacks-friedberg-NpyF_7WBYua-0eWaLuirNTJ.1400x1400.jpg",
        "title": "All-In with Chamath, Jason, Sacks & Friedberg",
        "publisher": "Jason Calacanis",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/all-in-with-chamath-jason-sacks-friedberg-yCpUza38HRh-0eWaLuirNTJ.300x300.jpg",
        "listen_score": 63,
        "listennotes_url": "https://www.listennotes.com/c/40b72ce8610649529542575dedf06c86/",
        "listen_score_global_rank": "0.1%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/all-in-with-chamath-jason-sacks-friedberg-yCpUza38HRh-0eWaLuirNTJ.300x300.jpg",
      "description": "<p>Follow the crew:</p> <p><a href= \"https://twitter.com/chamath\">https://twitter.com/chamath</a></p> <p><a href= \"https://linktr.ee/calacanis\">https://linktr.ee/calacanis</a></p> <p><a href= \"https://twitter.com/DavidSacks\">https://twitter.com/DavidSacks</a></p> <p><a href= \"https://twitter.com/friedberg\">https://twitter.com/friedberg</a></p> <p>Follow the pod:</p> <p><a href= \"https://twitter.com/theallinpod\">https://twitter.com/theallinpod</a></p> <p><a href= \"https://linktr.ee/allinpodcast\">https://linktr.ee/allinpodcast</a></p> <p>Intro Music Credit:</p> <p><a href=\"https://rb.gy/tppkzl\">https://rb.gy/tppkzl</a></p> <p><a href= \"https://twitter.com/yung_spielburg\">https://twitter.com/yung_spielburg</a></p> <p>Intro Video Credit:</p> <p><a href= \"https://twitter.com/MikeSylvan\">https://twitter.com/MikeSylvan</a></p> <p>Referenced in the show:</p> <p>M1 Money Stock</p> <p><a href= \"https://fred.stlouisfed.org/series/M1\">https://fred.stlouisfed.org/series/M1</a></p> <p>Friedberg's Spy Situation</p> <p><a href= \"https://www.justice.gov/opa/pr/chinese-national-who-worked-monsanto-indicted-economic-espionage-charges\"> https://www.justice.gov/opa/pr/chinese-national-who-worked-monsanto-indicted-economic-espionage-charges</a></p> <p>Sacks' thoughts on Wilkinson cancellation</p> <p><a href= \"https://twitter.com/DavidSacks/status/1352432977460957185\">https://twitter.com/DavidSacks/status/1352432977460957185</a></p> <p>Show Notes:</p> <p>0:00 Bestie intro, Inauguration talk, Impeachment implications</p> <p>20:22 Trump as a successful change agent, Facebook's Oversight Board overseeing Trump's appeal</p> <p>34:07 Will Big Tech be regulated like utilities? Friedberg tells a spy story</p> <p>44:15 Breaking down the $1.9T Stimulus package, needs for infrastructure bill, worst-case scenarios</p> <p>55:06 How the tech ecosystem plays into inequality & how to fix it</p> <p>1:04:00 Recalling California Governor Gavin Newsom, California's lockdown incompetence</p> <p>1:17:32 Sacks rebukes cancel culture, this time from the right-wing mob</p>",
      "pub_date_ms": 1611365210000,
      "guid_from_rss": "feece5c1-dbc4-42ba-af91-52f4c3fa6401",
      "listennotes_url": "https://www.listennotes.com/e/512830b5fdfb43569f0019b854c5d67f/",
      "audio_length_sec": 5009,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/512830b5fdfb43569f0019b854c5d67f/#edit"
    },
    {
      "id": "55828aaa81ee4153a6f37c1af1fdccff",
      "link": "https://allinchamathjason.libsyn.com/e21-media-misalignment-subjects-controlling-narratives-more-with-bestie-guestie-draymond-green?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/55828aaa81ee4153a6f37c1af1fdccff/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/all-in-with-chamath-jason-sacks-friedberg-NpyF_7WBYua-0eWaLuirNTJ.1400x1400.jpg",
      "title": "E21: Media misalignment, subjects controlling narratives & more with bestie guestie Draymond Green",
      "podcast": {
        "id": "40b72ce8610649529542575dedf06c86",
        "image": "https://cdn-images-1.listennotes.com/podcasts/all-in-with-chamath-jason-sacks-friedberg-NpyF_7WBYua-0eWaLuirNTJ.1400x1400.jpg",
        "title": "All-In with Chamath, Jason, Sacks & Friedberg",
        "publisher": "Jason Calacanis",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/all-in-with-chamath-jason-sacks-friedberg-yCpUza38HRh-0eWaLuirNTJ.300x300.jpg",
        "listen_score": 63,
        "listennotes_url": "https://www.listennotes.com/c/40b72ce8610649529542575dedf06c86/",
        "listen_score_global_rank": "0.1%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/all-in-with-chamath-jason-sacks-friedberg-yCpUza38HRh-0eWaLuirNTJ.300x300.jpg",
      "description": "<p>Follow the besties:</p> <p><a href= \"https://twitter.com/chamath\">https://twitter.com/chamath</a></p> <p><a href= \"https://linktr.ee/calacanis\">https://linktr.ee/calacanis</a></p> <p><a href= \"https://twitter.com/DavidSacks\">https://twitter.com/DavidSacks</a></p> <p><a href= \"https://twitter.com/friedberg\">https://twitter.com/friedberg</a></p> <p><a href= \"https://twitter.com/Money23Green\">https://twitter.com/Money23Green</a></p> <p>Follow the pod:</p> <p><a href= \"https://twitter.com/theallinpod\">https://twitter.com/theallinpod</a></p> <p><a href= \"https://linktr.ee/allinpodcast\">https://linktr.ee/allinpodcast</a></p> <p>Intro Music Credit:</p> <p><a href=\"https://rb.gy/tppkzl\">https://rb.gy/tppkzl</a></p> <p><a href= \"https://twitter.com/yung_spielburg\">https://twitter.com/yung_spielburg</a></p> <p>Intro Video Credit:</p> <p><a href= \"https://twitter.com/MikeSylvan\">https://twitter.com/MikeSylvan</a></p> <p>Referenced in the show:</p> <p>David Sacks on Tucker Carlson</p> <p><a href= \"https://youtu.be/MukXS8uaVns\">https://youtu.be/MukXS8uaVns</a></p> <p>Gell-Mann Amnesia</p> <p><a href= \"https://www.epsilontheory.com/gell-mann-amnesia\">https://www.epsilontheory.com/gell-mann-amnesia</a></p> <p>Show Notes:</p> <p>0:00 Discussing Sacks' recent hit on Tucker Carlson</p> <p>7:25 Media misalignment, subjects as sources, new age of journalism</p> <p>25:53 Bold prediction for the future of media, potential All-In Network, mistrusting everyone except individuals</p> <p>34:28 Bestie Guestie Draymond Green joins the show to talk dealing with day-to-day NBA life under COVID protocols, the temperature of the nation, issues with the media & more</p> <p>1:08:02 Mean tweets</p>",
      "pub_date_ms": 1612583957000,
      "guid_from_rss": "23fa090b-a6ae-4862-99dd-135b6d8d7004",
      "listennotes_url": "https://www.listennotes.com/e/55828aaa81ee4153a6f37c1af1fdccff/",
      "audio_length_sec": 4524,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/55828aaa81ee4153a6f37c1af1fdccff/#edit"
    },
    {
      "id": "ea8ed0394b28400c88f91faf319d2d5d",
      "link": "http://feedproxy.google.com/~r/twist-audio/~3/7Rbj1ZDSBII/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/ea8ed0394b28400c88f91faf319d2d5d/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-rMEoeGBJqt1-EKckR36zrnA.1400x1400.jpg",
      "title": "Building a production location marketplace with Hank Leber, Co-Founder of Giggster | E1196",
      "podcast": {
        "id": "9a62e2581908415185dee35d2d19f9b5",
        "image": "https://cdn-images-1.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-rMEoeGBJqt1-EKckR36zrnA.1400x1400.jpg",
        "title": "This Week in Startups",
        "publisher": "Jason Calacanis",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-txh7pAS-Xsy-EKckR36zrnA.300x300.jpg",
        "listen_score": 62,
        "listennotes_url": "https://www.listennotes.com/c/9a62e2581908415185dee35d2d19f9b5/",
        "listen_score_global_rank": "0.5%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-txh7pAS-Xsy-EKckR36zrnA.300x300.jpg",
      "description": "Hank Leber, co-founder of Giggster, talks about growing their production location marketplace, onboarding 10,000 locations from a totally offline process and building \"Airbnb for professional locations\" (0:00). He shares Giggster's fundraising history and the impact of raising at Remote Demo Day (17:35), and also dives into common use cases and more (30:05)! Check out the advanced pod notes here: https://bit.ly/twist-notes-giggster\n\nFOUNDERS! Apply to pitch 7000+ angel investors at Remote Demo Day here: https://remotedemoday.com<img src=\"http://feeds.feedburner.com/~r/twist-audio/~4/7Rbj1ZDSBII\" height=\"1\" width=\"1\" alt=\"\"/>",
      "pub_date_ms": 1617999352000,
      "guid_from_rss": "https://thisweekinstartups.com/?p=42498",
      "listennotes_url": "https://www.listennotes.com/e/ea8ed0394b28400c88f91faf319d2d5d/",
      "audio_length_sec": 3121,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/ea8ed0394b28400c88f91faf319d2d5d/#edit"
    },
    {
      "id": "23edf77bbc8e458eae6b4a70763e909a",
      "link": "https://product-hunt-radio.simplecast.com/episodes/how-to-bounce-back-as-a-maker-with-josh-howarth-XbOKZ76t?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/23edf77bbc8e458eae6b4a70763e909a/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/product-hunt-radio-product-hunt-GWVKjh-0kgs-4qPNklrZI93.1400x1400.jpg",
      "title": "How to bounce back as a maker with Josh Howarth",
      "podcast": {
        "id": "40426582e3cd4dd2bf931f880e7374aa",
        "image": "https://cdn-images-1.listennotes.com/podcasts/product-hunt-radio-product-hunt-GWVKjh-0kgs-4qPNklrZI93.1400x1400.jpg",
        "title": "Product Hunt Radio",
        "publisher": "Product Hunt",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/product-hunt-radio-product-hunt--QOpzec69YV-4qPNklrZI93.300x300.jpg",
        "listen_score": 46,
        "listennotes_url": "https://www.listennotes.com/c/40426582e3cd4dd2bf931f880e7374aa/",
        "listen_score_global_rank": "1%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/product-hunt-radio-product-hunt--QOpzec69YV-4qPNklrZI93.300x300.jpg",
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
      "id": "8bf53687945f4c918548c7aef831176c",
      "link": "https://businessgrowthpodcast.libsyn.com/how-to-spot-and-avoid-financial-fraud-in-your-business-episode-107?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/8bf53687945f4c918548c7aef831176c/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/business-growth/how-to-spot-and-avoid--FXjgA_y3v1-tdHal7yYb86.1200x1200.jpg",
      "title": "How to Spot and Avoid Financial Fraud in Your Business - Episode 107",
      "podcast": {
        "id": "b8016340502a4aadb171cb0bea02c5cd",
        "image": "https://cdn-images-1.listennotes.com/podcasts/business-growth-spencer-shaw-5yTe_m0wPqv-VJkEjbL3WIl.1400x1400.jpg",
        "title": "Business Growth",
        "publisher": "Spencer Shaw",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/business-growth-spencer-shaw-WyCqbUg-AiS-VJkEjbL3WIl.300x300.jpg",
        "listen_score": 33,
        "listennotes_url": "https://www.listennotes.com/c/b8016340502a4aadb171cb0bea02c5cd/",
        "listen_score_global_rank": "5%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/business-growth/how-to-spot-and-avoid-SeN9ld2ZRLI-tdHal7yYb86.300x300.jpg",
      "description": "<p>Stephen King of <a href= \"http://www.growthforce.com\">www.GrowthForce.com</a> explains how you can avoid having an employee commit financial fraud against your business. You'll learn the things to be aware of, where it originates, and then how to prevent it.</p> <p>\u00a0</p> <p>Episode Highlights</p> <ul> <li style=\"font-weight: 400;\">How to reduce risk</li> <li style=\"font-weight: 400;\">Who to trust</li> <li style=\"font-weight: 400;\">Reducing the risk of fraud</li> <li style=\"font-weight: 400;\">Rationalizing behavior</li> <li style=\"font-weight: 400;\">Level of risk</li> <li style=\"font-weight: 400;\">Understanding your risk</li> <li style=\"font-weight: 400;\">GrowthForce goal</li> <li style=\"font-weight: 400;\">Helping business owners to grow</li> <li style=\"font-weight: 400;\">A webinar about how fraud happens</li> </ul> <p>\u00a0</p> <p>Links and Resources</p> <ul> <li style=\"font-weight: 400;\"><a href= \"http://www.growthforce.com\">www.growthforce.com</a>\u00a0</li> <li style=\"font-weight: 400;\"><a href= \"https://twitter.com/skingGForce\">https://twitter.com/skingGForce</a></li> <li style=\"font-weight: 400;\"><a href= \"https://www.linkedin.com/in/stephenkingcpa\">https://www.linkedin.com/in/stephenkingcpa</a></li> </ul> <p>\u00a0</p> <p>Subscribe and Share</p> <ul> <li style=\"font-weight: 400;\">Find us on <a href= \"https://itunes.apple.com/us/podcast/business-growth-podcast/id665698424?mt=2\"> Apple Podcasts</a></li> <li style=\"font-weight: 400;\">Follow us on <a href= \"https://open.spotify.com/show/4KrAcqWNJVjvafU29JnTqd?si=v2Uy-EWqTSWUgOXComoTrw\"> Spotify</a></li> <li style=\"font-weight: 400;\">Listen on <a href= \"http://www.stitcher.com/s?fid=52093\">Stitcher</a></li> <li style=\"font-weight: 400;\">Say hi on Twitter <a href= \"https://twitter.com/spencershaw\">@spencershaw</a></li> </ul> <p> If you like what you hear we\u2019d love for you to <a href= \"https://itunes.apple.com/us/podcast/business-growth-podcast/id665698424?mt=2\"> leave a review</a> and tell us what you think. Your support is the fuel that keeps us going!</p>",
      "pub_date_ms": 1595494800000,
      "guid_from_rss": "1cee5370-3f05-4bca-8577-123ef447dee2",
      "listennotes_url": "https://www.listennotes.com/e/8bf53687945f4c918548c7aef831176c/",
      "audio_length_sec": 1510,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/8bf53687945f4c918548c7aef831176c/#edit"
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
      "id": "0f34a9099579490993eec9e8c8cebb82",
      "link": "https://cms.megaphone.fm/channel/business-unusual-with-barbara-corcoran?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/0f34a9099579490993eec9e8c8cebb82/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-0xz1V7EmgRh-aZPn3Ic47rx.1400x1400.jpg",
      "title": "35: Don\u2019t Make Your Landlord Rich",
      "podcast": {
        "id": "68faf62be97149c280ebcc25178aa731",
        "image": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-0xz1V7EmgRh-aZPn3Ic47rx.1400x1400.jpg",
        "title": "Business Unusual with Barbara Corcoran",
        "publisher": "Barbara Corcoran",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-rPvxTmILGYJ-aZPn3Ic47rx.300x300.jpg",
        "listen_score": 57,
        "listennotes_url": "https://www.listennotes.com/c/68faf62be97149c280ebcc25178aa731/",
        "listen_score_global_rank": "0.5%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-rPvxTmILGYJ-aZPn3Ic47rx.300x300.jpg",
      "description": "<p>If you\u2019re starting a new business, you need to keep costs low \u2013 so renting is the way to go, right?\n\nI say no! I\u2019ll tell you why you should scrape together the cash to buy your business headquarters from the get-go.\u00a0\n\nAlso, I\u2019ll answer some more of your great questions about how to get the press to pay attention to your little mom and pop shop and what to do about a toxic work environment.\n\nGot a business question you want to ask me? Tweet it @BarbaraCorcoran and I may just answer it on a future episode!\n\nFollow Business Unusual with Barbara Corcoran on iHeartRadio, or subscribe wherever you listen to podcasts.\n\nThis episode of Business Unusual with Barbara Corcoran is presented by\u00a0On Deck Business Loans\u00a0(http://www.ondeck.com/barbara).\u00a0\u00a0\u00a0</p>",
      "pub_date_ms": 1546232460067,
      "guid_from_rss": "gid://art19-episode-locator/V0/Q3wpi1LpU7b7vFqc3_T1BsaIqZJruq-YWy3Ud4sJnJo",
      "listennotes_url": "https://www.listennotes.com/e/0f34a9099579490993eec9e8c8cebb82/",
      "audio_length_sec": 486,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/0f34a9099579490993eec9e8c8cebb82/#edit"
    },
    {
      "id": "c577d55b2b2b483c969fae3ceb58e362",
      "link": "https://www.listenmoneymatters.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/c577d55b2b2b483c969fae3ceb58e362/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/listen-money-matters-free-your-inner-7gAv31w6e5z-SJEHNr84kVg.1400x1400.jpg",
      "title": "Do Things That Scale: Starting a Business That Will Take Off",
      "podcast": {
        "id": "3302bc71139541baa46ecb27dbf6071a",
        "image": "https://cdn-images-1.listennotes.com/podcasts/listen-money-matters-free-your-inner-7gAv31w6e5z-SJEHNr84kVg.1400x1400.jpg",
        "title": "Listen Money Matters - Free your inner financial badass. All the stuff you should know about personal finance.",
        "publisher": "ListenMoneyMatters.com | Andrew Fiebert and Matt Giovanisci",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/listen-money-matters-free-your-inner-Uo_qv9RYI6A-SJEHNr84kVg.300x300.jpg",
        "listen_score": 66,
        "listennotes_url": "https://www.listennotes.com/c/3302bc71139541baa46ecb27dbf6071a/",
        "listen_score_global_rank": "0.1%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/listen-money-matters-free-your-inner-Uo_qv9RYI6A-SJEHNr84kVg.300x300.jpg",
      "description": "<p>There are only so many hours in a day so you need to build a business that can grow while you\u2019re sleeping, on vacation, or working on your next business. You have to do things that scale when starting a business that will take off. While we are discussing scaling a business, there are plenty of other areas of life that you can scale including investing and video games. To scale a business means to create a system, product, or service that can generate more money through some resource that isn\u2019t your time. Scale is a concept that is meant to support infinite growth. When starting a business, you want to find ways to apply your time and money that are scalable and to shift your focus from things with a hard maximum return to things that have the potential to be infinitely scalable.</p><p>\u00a0</p><p><a href=\"https://www.listenmoneymatters.com/starting-a-business-that-scales/%20%E2%80%8E\">Full Article Here</a></p><p><strong></p><p>Show Notes</p><p></strong></p><p><a href=\"http://portbrewing.com/beer/board-meeting/\"><strong>Board Meeting:</strong></a> A coffee flavored brown ale.</p><p><a href=\"https://www.listenmoneymatters.com/toolbox/\"><strong>Tool Box:</strong></a> All the best stuff to manage your money.</p><p><a href=\"http://paulgraham.com/ds.html\"><strong>Do Things That Don't Scale:</strong></a> The essay Andrew mentioned by Paul Graham.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://megaphone.fm/adchoices\">megaphone.fm/adchoices</a></p>",
      "pub_date_ms": 1528088400089,
      "guid_from_rss": "https://www.listenmoneymatters.com/?p=46659",
      "listennotes_url": "https://www.listennotes.com/e/c577d55b2b2b483c969fae3ceb58e362/",
      "audio_length_sec": 3683,
      "explicit_content": true,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/c577d55b2b2b483c969fae3ceb58e362/#edit"
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
      "email": "admin@stratechery.com",
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
        "twitter_handle": "exponentfm",
        "facebook_handle": "",
        "instagram_handle": ""
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-Hp-mWcd9xkK-OaJSjb4xQv3.1400x1400.jpg",
      "title": "Exponent",
      "country": "United States",
      "website": "http://exponent.fm?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        129,
        93,
        127,
        157,
        149
      ],
      "itunes_id": 826420969,
      "publisher": "Ben Thompson / James Allworth",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-dB9NRYQvLw7-OaJSjb4xQv3.300x300.jpg",
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
      "latest_pub_date_ms": 1619771580000,
      "earliest_pub_date_ms": 1392899826193,
      "listen_score_global_rank": "0.5%"
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
        "google_url": "",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "BarbaraCorcoran",
        "facebook_handle": "TheBarbaraCorcoran",
        "instagram_handle": ""
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-0xz1V7EmgRh-aZPn3Ic47rx.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-rPvxTmILGYJ-aZPn3Ic47rx.300x300.jpg",
      "is_claimed": false,
      "description": "I\u2019m smart at getting to where I want to go, and I can teach you how to do it! I had 22 jobs before starting my real estate company with a $1000 loan and built it into a $5 billion business. Today I\u2019m a \u2019Shark\u2019 on ABC\u2019s hit show \"Shark Tank.\" It didn\u2019t take a fancy degree to get here but took street smarts and a lot of courage. Life is too short to waste your time practicing someone else\u2019s fancy theory on success. I give you the straight talk and the confidence to get there. Got a question? Call me at 888-BARBARA. Subscribe to Business Unusual with Barbara Corcoran wherever you listen to podcasts.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 57,
      "total_episodes": 109,
      "listennotes_url": "https://www.listennotes.com/c/68faf62be97149c280ebcc25178aa731/",
      "explicit_content": false,
      "latest_pub_date_ms": 1619496000000,
      "earliest_pub_date_ms": 1525202794102,
      "listen_score_global_rank": "0.5%"
    },
    {
      "id": "9cf19c590ff0484d97b18b329fed0c6a",
      "rss": "https://rss.art19.com/binge-mode-game-of-thrones",
      "type": "serial",
      "email": "info@theringer.com",
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
        "twitter_handle": "binge_mode",
        "facebook_handle": "",
        "instagram_handle": ""
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/binge-mode-marvel-the-ringer-eVxlrUKNObE-BdPpshCaFDu.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/binge-mode-marvel-the-ringer-pvH0d1CzG92-BdPpshCaFDu.300x300.jpg",
      "is_claimed": false,
      "description": "The Ringer\u2019s Mallory Rubin and Jason Concepcion return to take their signature deep dives into the Marvel Cinematic Universe, covering all 23 films!",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 79,
      "total_episodes": 256,
      "listennotes_url": "https://www.listennotes.com/c/9cf19c590ff0484d97b18b329fed0c6a/",
      "explicit_content": true,
      "latest_pub_date_ms": 1616634382000,
      "earliest_pub_date_ms": 1496277060025,
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
        "google_url": "",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "MoneyMattersMan",
        "facebook_handle": "ListenMoneyMatters",
        "instagram_handle": "listenmoneymatters"
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/listen-money-matters-free-your-inner-7gAv31w6e5z-SJEHNr84kVg.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/listen-money-matters-free-your-inner-Uo_qv9RYI6A-SJEHNr84kVg.300x300.jpg",
      "is_claimed": false,
      "description": "Honest and uncensored - this is not your father\u2019s boring finance show. This show brings much needed ACTIONABLE advice to a people who hate being lectured about personal finance from the out-of-touch one percent. Andrew and Matt are relatable, funny, and brash. Their down-to-earth discussions about money are entertaining whether you\u2019re a financial whiz or just starting out. To be a part of the show and get your financial questions answered, send an email to listenmoneymatters@gmail.com.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 66,
      "total_episodes": 546,
      "listennotes_url": "https://www.listennotes.com/c/3302bc71139541baa46ecb27dbf6071a/",
      "explicit_content": true,
      "latest_pub_date_ms": 1589169600000,
      "earliest_pub_date_ms": 1374314413000,
      "listen_score_global_rank": "0.1%"
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/find-money-you-didnt-know-you-had-npr-WuHnh0Poiyb-IDT1XPkq4rb.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/find-money-you-didnt-know-you-had-npr-Dl7VZ86KyNA-IDT1XPkq4rb.300x300.jpg",
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
      "rss": "http://feeds.feedburner.com/marketsnacks-daily",
      "type": "episodic",
      "email": "podcasts@cadence13.com",
      "extra": {
        "url1": "http://www.marketsnacks.com/",
        "url2": "",
        "url3": "",
        "google_url": "",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "marketsnacks",
        "facebook_handle": "MarketSnacks",
        "instagram_handle": ""
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-hu4HiXUtv3y-kmx0XIZTAys.1400x1400.jpg",
      "title": "Snacks Daily",
      "country": "United States",
      "website": "https://snacks.robinhood.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        98,
        95,
        93,
        67
      ],
      "itunes_id": 1386234384,
      "publisher": "Robinhood Financial, LLC",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-3qgUaLoWpvA-kmx0XIZTAys.300x300.jpg",
      "is_claimed": false,
      "description": "Digestible financial news. Get smarter fast with an entertaining breakdown of our top 3 business stories in 15 minutes. Pairs perfectly with your commute, workout, or morning oatmeal ritual. Hosted by Jack Kramer and Nick Martell.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 72,
      "total_episodes": 496,
      "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
      "explicit_content": false,
      "latest_pub_date_ms": 1619773200000,
      "earliest_pub_date_ms": 1553519100495,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/philosophize-this-stephen-west-Y2PvRelyrIN-ivQCfmkqM_h.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/philosophize-this-stephen-west-oSuiCW7Bz8T-ivQCfmkqM_h.300x300.jpg",
      "is_claimed": false,
      "description": "Beginner friendly if listened to in order! For anyone interested in an educational podcast about philosophy where you don't need to be a graduate-level philosopher to understand it. In chronological order, the thinkers and ideas that forged the world we live in are broken down and explained.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 79,
      "total_episodes": 153,
      "listennotes_url": "https://www.listennotes.com/c/3a2a6ddd549f4df0b876e7315fa1a319/",
      "explicit_content": false,
      "latest_pub_date_ms": 1617311333000,
      "earliest_pub_date_ms": 1370556600152,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/espionage-parcast-network-6YfZjN1qEwC-ReK0QUN-VP_.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/espionage-parcast-network-G9K7-WvercO-ReK0QUN-VP_.300x300.jpg",
      "is_claimed": false,
      "description": "Not all spies look like James Bond and Ethan Hunt. Most of them look like ordinary people, which makes them all the more dangerous... So what does it really take to be a spy? Every week, we cover a real-life spy mission: the stakes, the deception, the gadgets, and how it changed the course of history. Each two-part series follows one mission of a historic spy, and if they made it out alive. Espionage is a production of Cutler Media and part of the Parcast Network.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 64,
      "total_episodes": 83,
      "listennotes_url": "https://www.listennotes.com/c/bacb2f7ca7a04ed0b21efd21192f5014/",
      "explicit_content": false,
      "latest_pub_date_ms": 1618815660000,
      "earliest_pub_date_ms": 1553471173023,
      "listen_score_global_rank": "0.1%"
    }
  ],
  "latest_episodes": [
    {
      "id": "9447ce07dd2345618054b04b733e4ad5",
      "link": "https://snacks.robinhood.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/9447ce07dd2345618054b04b733e4ad5/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-hu4HiXUtv3y-kmx0XIZTAys.1400x1400.jpg",
      "title": "Google\u2019s $399 smartphone, Crocs\u2019 comeback, and GM\u2019s robotaxi Cruise snags $1B",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-hu4HiXUtv3y-kmx0XIZTAys.1400x1400.jpg",
        "title": "Snacks Daily",
        "publisher": "Robinhood Financial, LLC",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-3qgUaLoWpvA-kmx0XIZTAys.300x300.jpg",
        "listen_score": 72,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-3qgUaLoWpvA-kmx0XIZTAys.300x300.jpg",
      "description": "<p>Google\u2019s I/O event day enjoyed protests, AI tech to screen fake\u00a0calls, and a $399 Pixel phone. General Motors acquired self-driving car startup Cruise when it was worth $1B \u2014 Now it\u2019s worth $19B, and wants robotaxis on streets this year. And Crocs shares have nearly doubled in the past year, so we look at why.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1557309360464,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-hu4HiXUtv3y-kmx0XIZTAys.1400x1400.jpg",
      "title": "Big Trade War update, Apple\u2019s bought 20+ companies in 6 months, and the largest VC investment in Latin America ever",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-hu4HiXUtv3y-kmx0XIZTAys.1400x1400.jpg",
        "title": "Snacks Daily",
        "publisher": "Robinhood Financial, LLC",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-3qgUaLoWpvA-kmx0XIZTAys.300x300.jpg",
        "listen_score": 72,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-3qgUaLoWpvA-kmx0XIZTAys.300x300.jpg",
      "description": "<p>The Trade War was supposed to end this week with a peace\u00a0deal. That\u2019s not looking likely, and we\u2019ll tell you why. Apple\u2019s CEO casually dropped that the company\u2019s bought over 20 startups over the last six months. And super delivery app Rappi just raised $1B from Softbank, making it the biggest Latin American venture\u00a0investment ever.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1557222960465,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-0xz1V7EmgRh-aZPn3Ic47rx.1400x1400.jpg",
      "title": "53: Something About Mary",
      "podcast": {
        "id": "68faf62be97149c280ebcc25178aa731",
        "image": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-0xz1V7EmgRh-aZPn3Ic47rx.1400x1400.jpg",
        "title": "Business Unusual with Barbara Corcoran",
        "publisher": "Barbara Corcoran",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-rPvxTmILGYJ-aZPn3Ic47rx.300x300.jpg",
        "listen_score": 57,
        "listennotes_url": "https://www.listennotes.com/c/68faf62be97149c280ebcc25178aa731/",
        "listen_score_global_rank": "0.5%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-rPvxTmILGYJ-aZPn3Ic47rx.300x300.jpg",
      "description": "<p><strong>CNBC Producer Mary Hanan has the TV business dream job. I met Mary when she interviewed me for CNBC's \"The Brave Ones\" and I knew immediately I had to have her on the show. So I turned the tables on Mary and put her in the hot seat to learn how she worked her way up to the top, and she shared many of the interesting situations she found herself in along the way.Got a question for me? Call me at 888-BARBARA to ask a question for a future episode. Follow Business Unusual with Barbara Corcoran on iHeartRadio, or subscribe wherever you listen to podcasts. </strong>\u00a0<strong>This episode of Business Unusual with Barbara Corcoran is presented by OnDeck Business Loans (</strong><a href=\"https://urldefense.proofpoint.com/v2/url?u=http-3A__www.ondeck.com_Barbara&amp;d=DwMFaQ&amp;c=GC0NZZhaEw6GOQSjMHI2g15k_drElRoPmOYiK2k0eZ8&amp;r=xy9pRdG6lpZ6ogtRUMNvODnG4DdmLUxjZ2d9xbUZdbU5UshE20nENw68An-bhaS4&amp;m=b7G5z-S4fY6jYnVJoDD0IxLhdkIPrFOrNN2yLnt3Odc&amp;s=ecKEHfTJ9QtY2QfvkGL3kNIB-ZJ848-poG_hR6akhwQ&amp;e=\"><strong>http://www.ondeck.com/Barbara</strong></a><strong>)</strong></p>",
      "pub_date_ms": 1557201660049,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-hu4HiXUtv3y-kmx0XIZTAys.1400x1400.jpg",
      "title": "Warren Buffett\u2019s epic annual event, Planet Fitness\u2019 innovative real estate strategy, and almond milk vs. Dean Foods dairy",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-hu4HiXUtv3y-kmx0XIZTAys.1400x1400.jpg",
        "title": "Snacks Daily",
        "publisher": "Robinhood Financial, LLC",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-3qgUaLoWpvA-kmx0XIZTAys.300x300.jpg",
        "listen_score": 72,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-3qgUaLoWpvA-kmx0XIZTAys.300x300.jpg",
      "description": "<p>The annual Berkshire Hathaway shareholder meeting showcased\u00a088-year-old legendary investor Warren Buffett, so we broke down his 6 hours of one-liner business takeaways. Planet Fitness shares are up 75% in the last year, so we\u2019re focused on its innovative real estate strategy that feeds off the retail-pocalypse. And Dean Foods is America\u2019s biggest dairy company, but the stock is down 62% in 2019 because of alt-milk.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1557136560466,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/listen-money-matters-free-your-inner-7gAv31w6e5z-SJEHNr84kVg.1400x1400.jpg",
      "title": "All Things Gold",
      "podcast": {
        "id": "3302bc71139541baa46ecb27dbf6071a",
        "image": "https://cdn-images-1.listennotes.com/podcasts/listen-money-matters-free-your-inner-7gAv31w6e5z-SJEHNr84kVg.1400x1400.jpg",
        "title": "Listen Money Matters - Free your inner financial badass. All the stuff you should know about personal finance.",
        "publisher": "ListenMoneyMatters.com | Andrew Fiebert and Matt Giovanisci",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/listen-money-matters-free-your-inner-Uo_qv9RYI6A-SJEHNr84kVg.300x300.jpg",
        "listen_score": 66,
        "listennotes_url": "https://www.listennotes.com/c/3302bc71139541baa46ecb27dbf6071a/",
        "listen_score_global_rank": "0.1%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/listen-money-matters-free-your-inner-Uo_qv9RYI6A-SJEHNr84kVg.300x300.jpg",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-hu4HiXUtv3y-kmx0XIZTAys.1400x1400.jpg",
      "title": "The Taser CEO gets $246M in stock comp, Beyond Meat surges 163%, and Wayfair drops 7% because you\u2019re expensive",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-hu4HiXUtv3y-kmx0XIZTAys.1400x1400.jpg",
        "title": "Snacks Daily",
        "publisher": "Robinhood Financial, LLC",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-3qgUaLoWpvA-kmx0XIZTAys.300x300.jpg",
        "listen_score": 72,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-3qgUaLoWpvA-kmx0XIZTAys.300x300.jpg",
      "description": "<p>Axon Enterprises is the company behind the taser, and it just awarded its CEO $246M in compensation \u2014 So we look in to how it\u2019s set up to incentivize him. Beyond Meat surged 163% on its IPO day. And Wayfair is the biggest online furniture platform whose stock fell 7%, but it\u2019s got a fascinating relationship with 80 \u201chouse brands.\u201d</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1556877360467,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/espionage-parcast-network-6YfZjN1qEwC-ReK0QUN-VP_.1400x1400.jpg",
      "title": "Henri D\u00e9ricourt Pt. 2: Triple Agent",
      "podcast": {
        "id": "bacb2f7ca7a04ed0b21efd21192f5014",
        "image": "https://cdn-images-1.listennotes.com/podcasts/espionage-parcast-network-6YfZjN1qEwC-ReK0QUN-VP_.1400x1400.jpg",
        "title": "Espionage",
        "publisher": "Parcast Network",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/espionage-parcast-network-G9K7-WvercO-ReK0QUN-VP_.300x300.jpg",
        "listen_score": 64,
        "listennotes_url": "https://www.listennotes.com/c/bacb2f7ca7a04ed0b21efd21192f5014/",
        "listen_score_global_rank": "0.1%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/espionage-parcast-network-G9K7-WvercO-ReK0QUN-VP_.300x300.jpg",
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
      "id": "77fab92c66884302a7279553233a0171",
      "link": "https://art19.com/shows/binge-mode-game-of-thrones?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/77fab92c66884302a7279553233a0171/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/binge-mode-weekly/s8e3-the-long-night-game-of-4-ZvQDM2BsO-mh4NwCA3iJP.1400x1400.jpg",
      "title": "S8E3: The Long Night | Game of Thrones",
      "podcast": {
        "id": "9cf19c590ff0484d97b18b329fed0c6a",
        "image": "https://cdn-images-1.listennotes.com/podcasts/binge-mode-marvel-the-ringer-eVxlrUKNObE-BdPpshCaFDu.1400x1400.jpg",
        "title": "Binge Mode: Marvel",
        "publisher": "The Ringer",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/binge-mode-marvel-the-ringer-pvH0d1CzG92-BdPpshCaFDu.300x300.jpg",
        "listen_score": 79,
        "listennotes_url": "https://www.listennotes.com/c/9cf19c590ff0484d97b18b329fed0c6a/",
        "listen_score_global_rank": "0.01%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/binge-mode-weekly/s8e3-the-long-night-game-of-M3Urs7ZXWQw-mh4NwCA3iJP.300x300.jpg",
      "description": "<p>Mal and Jason discuss \u2018Game of Thrones\u2019 Season 8, Episode 3, \u201cThe Long Night,\u201d by exploring the last stand of humanity, examining the differences between the on-screen Night King and his book counterpart, sharing seven of their favorite insights and observations, and awarding the Champion\u2019s Purse to a heroic assassin.</p>",
      "pub_date_ms": 1556791274048,
      "guid_from_rss": "gid://art19-episode-locator/V0/XtCiz3BVzmqiPxwC1-cDyhyMjySnbeFfehcTxvjMRR0",
      "listennotes_url": "https://www.listennotes.com/e/77fab92c66884302a7279553233a0171/",
      "audio_length_sec": 8254,
      "explicit_content": true,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/77fab92c66884302a7279553233a0171/#edit"
    },
    {
      "id": "f0f2cc1d772c4ae4aef5bd1d1c8fb834",
      "link": "https://snacks.robinhood.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/f0f2cc1d772c4ae4aef5bd1d1c8fb834/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-hu4HiXUtv3y-kmx0XIZTAys.1400x1400.jpg",
      "title": "Molson Coors falls 8% on mid-beer crisis, Royal Caribbean becomes pricing power superhero, and Fitbit is our \u201cSurvivor of the Day\u201d",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-hu4HiXUtv3y-kmx0XIZTAys.1400x1400.jpg",
        "title": "Snacks Daily",
        "publisher": "Robinhood Financial, LLC",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-3qgUaLoWpvA-kmx0XIZTAys.300x300.jpg",
        "listen_score": 72,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-3qgUaLoWpvA-kmx0XIZTAys.300x300.jpg",
      "description": "<p>With beer sales slowing, Molson Coors is desperately\u00a0focused on innovation (aka non-alcohol drinks), but shares fell because of its beer battles. Fitbit used to be profitable, now it\u2019s using partnerships to survive. And Royal Caribbean jumped 7% as it realizes it can charge a lot more for cruises.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1556790960468,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-hu4HiXUtv3y-kmx0XIZTAys.1400x1400.jpg",
      "title": "Facebook\u2019s new \u201cFB5\u201d redesign (and dating feature), Apple\u2019s past-dependent business model, and Merck\u2019s profits quadruple",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-hu4HiXUtv3y-kmx0XIZTAys.1400x1400.jpg",
        "title": "Snacks Daily",
        "publisher": "Robinhood Financial, LLC",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-3qgUaLoWpvA-kmx0XIZTAys.300x300.jpg",
        "listen_score": 72,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-3qgUaLoWpvA-kmx0XIZTAys.300x300.jpg",
      "description": "<p>Apple\u2019s earnings report was critical for what it didn\u2019t say, just as much as what it did \u2014 And it reveals that Apple\u2019s transformation. Facebook\u2019s F8 event revealed new features (dating and crushes), but the big focus was its app redesign. And Merck\u2019s profits quadrupled because a measles vaccine and a new cancer drug have become its profit puppies.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1556704560469,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-hu4HiXUtv3y-kmx0XIZTAys.1400x1400.jpg",
      "title": "Spotify hits 217M profitless users, Airbnb & Marriott\u2019s twin announcements, and Chewy.com\u2019s \u201cpet humanization\u201d IPO",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-hu4HiXUtv3y-kmx0XIZTAys.1400x1400.jpg",
        "title": "Snacks Daily",
        "publisher": "Robinhood Financial, LLC",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-3qgUaLoWpvA-kmx0XIZTAys.300x300.jpg",
        "listen_score": 72,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-3qgUaLoWpvA-kmx0XIZTAys.300x300.jpg",
      "description": "<p>Spotify now boasts 100M paying subscribers, so we looked\u00a0into why it\u2019s still losing so much money (hint: It\u2019s betting on podcasts). Airbnb and Marriott both revealed new services that look a lot like each other (awkward). And PetSmart\u2019s digital brand Chewy.com will IPO thanks to \u201cpet humanization\u201d trends.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1556618160470,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-0xz1V7EmgRh-aZPn3Ic47rx.1400x1400.jpg",
      "title": "52: What I Learned From Bad Bosses",
      "podcast": {
        "id": "68faf62be97149c280ebcc25178aa731",
        "image": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-0xz1V7EmgRh-aZPn3Ic47rx.1400x1400.jpg",
        "title": "Business Unusual with Barbara Corcoran",
        "publisher": "Barbara Corcoran",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-rPvxTmILGYJ-aZPn3Ic47rx.300x300.jpg",
        "listen_score": 57,
        "listennotes_url": "https://www.listennotes.com/c/68faf62be97149c280ebcc25178aa731/",
        "listen_score_global_rank": "0.5%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-rPvxTmILGYJ-aZPn3Ic47rx.300x300.jpg",
      "description": "<p><strong>I had 23 bosses before starting my business and I know that a bad one is sure to kill your confidence. So what do you do when you don't see eye to eye? I answer your questions about dealing with a bad boss and becoming a better leader. </strong>\u00a0<strong>Want to hear your question on Business Unusual? Call me at 888-BARBARA or tweet at @barbaracorcoran to ask a question for a future episode. Follow Business Unusual with Barbara Corcoran on iHeartRadio, or subscribe wherever you listen to podcasts. </strong>\u00a0<strong>This episode of Business Unusual with Barbara Corcoran is presented by OnDeck Business Loans (</strong><a href=\"https://urldefense.proofpoint.com/v2/url?u=http-3A__www.ondeck.com_Barbara&amp;d=DwMFaQ&amp;c=GC0NZZhaEw6GOQSjMHI2g15k_drElRoPmOYiK2k0eZ8&amp;r=xy9pRdG6lpZ6ogtRUMNvODnG4DdmLUxjZ2d9xbUZdbU5UshE20nENw68An-bhaS4&amp;m=iyzCy3KkByFDhAZKPNnXfRZDwVi9wa4vgtkjqAegOYo&amp;s=AR-0E6fCOSktW28rNgQpCe-kEyu1odFgovlqPFyavSA&amp;e=\"><strong>http://www.ondeck.com/Barbara</strong></a><strong>)</strong>\u00a0</p>",
      "pub_date_ms": 1556596860050,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/philosophize-this-stephen-west-Y2PvRelyrIN-ivQCfmkqM_h.1400x1400.jpg",
      "title": "Episode #130 ... Dewey and Lippman on Democracy",
      "podcast": {
        "id": "3a2a6ddd549f4df0b876e7315fa1a319",
        "image": "https://cdn-images-1.listennotes.com/podcasts/philosophize-this-stephen-west-Y2PvRelyrIN-ivQCfmkqM_h.1400x1400.jpg",
        "title": "Philosophize This!",
        "publisher": "Stephen West",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/philosophize-this-stephen-west-oSuiCW7Bz8T-ivQCfmkqM_h.300x300.jpg",
        "listen_score": 79,
        "listennotes_url": "https://www.listennotes.com/c/3a2a6ddd549f4df0b876e7315fa1a319/",
        "listen_score_global_rank": "0.01%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/philosophize-this-stephen-west-oSuiCW7Bz8T-ivQCfmkqM_h.300x300.jpg",
      "description": "<p>Today we talk about a famous debate from the early 20th century.\u00a0</p>",
      "pub_date_ms": 1556594432023,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-hu4HiXUtv3y-kmx0XIZTAys.1400x1400.jpg",
      "title": "Beyond Meat boots its meat-focused investor, Comcast (shockingly) hits record high, and one startup\u2019s worst 1st week",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-hu4HiXUtv3y-kmx0XIZTAys.1400x1400.jpg",
        "title": "Snacks Daily",
        "publisher": "Robinhood Financial, LLC",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-3qgUaLoWpvA-kmx0XIZTAys.300x300.jpg",
        "listen_score": 72,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-3qgUaLoWpvA-kmx0XIZTAys.300x300.jpg",
      "description": "<p>Plant-based meat innovator Beyond Meat had an awkward investor: The world\u2019s 2nd biggest meat producer, Tyson Foods -- So Beyond Meat kicked it out before its upcoming IPO. Old school cable throwback Comcast is winning even though you cut the cord. And Luminary was supposed to be the future of podcasting, but its 1st week went really badly.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1556531760471,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/find-money-you-didnt-know-you-had-npr-WuHnh0Poiyb-IDT1XPkq4rb.1400x1400.jpg",
      "title": "Special Announcement From Life Kit",
      "podcast": {
        "id": "613aa80ec729409ea0db4265cf3e3899",
        "image": "https://cdn-images-1.listennotes.com/podcasts/find-money-you-didnt-know-you-had-npr-WuHnh0Poiyb-IDT1XPkq4rb.1400x1400.jpg",
        "title": "Find Money You Didn't Know You Had",
        "publisher": "NPR",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/find-money-you-didnt-know-you-had-npr-Dl7VZ86KyNA-IDT1XPkq4rb.300x300.jpg",
        "listen_score": null,
        "listennotes_url": "https://www.listennotes.com/c/613aa80ec729409ea0db4265cf3e3899/",
        "listen_score_global_rank": null
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/find-money-you-didnt-know-you-had-npr-Dl7VZ86KyNA-IDT1XPkq4rb.300x300.jpg",
      "description": "Based on your feedback, we've created new ways to listen to Life Kit. If you never want to miss an episode, subscribe to Life Kit: All Guides. We also divided our guides by subject \u2014 health, money and parenting - and more to come in the future \u2014 so you can subscribe to only the topics you want to learn about.",
      "pub_date_ms": 1556519451000,
      "guid_from_rss": "f0925b4c-fc2f-494d-acf1-0c2fb96627ff",
      "listennotes_url": "https://www.listennotes.com/e/117e3b5027f14fb9842591aaa4b794eb/",
      "audio_length_sec": 53,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/117e3b5027f14fb9842591aaa4b794eb/#edit"
    }
  ],
  "next_episode_pub_date": 1556519451000
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
  "id": "f984973b797443308f87d2f2216bd5f8",
  "link": "https://blubrry.com/fortheloveofclimbing/76270669/26-im-a-liver-not-a-fighter/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
  "audio": "https://www.listennotes.com/e/p/f984973b797443308f87d2f2216bd5f8/",
  "image": "https://cdn-images-1.listennotes.com/podcasts/for-the-love-of-climbing-kathy-karlo-OigJy-n5_ZL-e-gnMlHp0x4.1400x1400.jpg",
  "title": "26: I\u2019m a Liver, Not a Fighter",
  "podcast": {
    "id": "26a816baaff0471da32906db5a044568",
    "image": "https://cdn-images-1.listennotes.com/podcasts/for-the-love-of-climbing-kathy-karlo-OigJy-n5_ZL-e-gnMlHp0x4.1400x1400.jpg",
    "title": "For the Love of Climbing",
    "publisher": "Kathy Karlo",
    "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/for-the-love-of-climbing-kathy-karlo-V8kKof-mMZR-e-gnMlHp0x4.300x300.jpg",
    "listen_score": 53,
    "listennotes_url": "https://www.listennotes.com/c/26a816baaff0471da32906db5a044568/",
    "listen_score_global_rank": "0.5%"
  },
  "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/for-the-love-of-climbing-kathy-karlo-V8kKof-mMZR-e-gnMlHp0x4.300x300.jpg",
  "description": "<p class=\"p1\"><span class=\"s1\">Cedar, who was named after a tree, has achieved a lot in her almost-decade of being alive\u2014she has a podcast, she\u2019s sort of a Do-It-Yourself queen, an accomplished video game champion (thanks to Covid), and she likes a lot of, you know, normal kid stuff\u2014not including getting a liver transplant at the age of five.</span></p>\n<p class=\"p2\">\u00a0</p>\n<p class=\"p1\"><span class=\"s1\">Cedar has something called Progressive Familial Intrahepatic Cholestasis, otherwise known as PFIC 2. This devastating genetic disorder affects 1 in 50,000 to 1 in 100,000 live births and, if untreated, can be fatal by the age of twenty. Visit <a href=\"http://pfic.org\">pfic.org</a> for more information.</span></p>\n<p class=\"p1\"><span class=\"s1\"><br /></span></p>\n<p class=\"p3\"><span class=\"s1\"><strong></strong></span></p>\n<p class=\"p4\"><span class=\"s1\"><strong>This mini-episode is brought to you by </strong><a href=\"https://www.deuter.com/us-en\"><span class=\"s2\"><strong>Deuter USA</strong></span></a><strong>, </strong><a href=\"https://gognarly.com/\"><span class=\"s2\"><strong>Gnarly Nutrition</strong></span></a><strong>, </strong><a href=\"https://allezoutdoor.com/\"><span class=\"s2\"><strong>Allez Outdoors</strong></span></a><strong>, </strong><a href=\"https://www.firstascentcoffee.com/\"><span class=\"s2\"><strong>First Ascent Coffee</strong></span></a><strong>, and </strong><a href=\"https://www.patagonia.com/home/\"><span class=\"s2\"><strong>Patagonia</strong></span></a><strong>.</strong></span></p>\n<p class=\"p4\"><span class=\"s1\"><strong><br /></strong></span></p>\n<p class=\"p3\"><span class=\"s1\"><strong></strong></span></p>\n<p class=\"p4\"><span class=\"s1\"><strong>Music by: Kakurenbo and Podington Bear. Additional music licensed by Music Bed. A HUGE thank you to Chad Crouch for creating absolute magic and to Peter Darmi for mixing this episode.</strong></span></p>\n<p class=\"p4\"><span class=\"s1\"><strong><br /></strong></span></p>\n<p class=\"p3\"><span class=\"s1\"><strong></strong></span></p>\n<p class=\"p4\"><span class=\"s1\">Additional sound effects from zapsplat.com.</span></p>\n<p class=\"p4\"><span class=\"s1\"><br /></span></p>\n<p class=\"p3\"><span class=\"s1\"><strong></strong></span></p>\n<p class=\"p4\"><span class=\"s1\"><strong>Cover photo by </strong><a href=\"https://www.kikamacfarlane.co/\"><span class=\"s2\"><strong>Kika MacFarlane</strong></span></a><strong>.</strong></span></p>\n<p class=\"p4\"><span class=\"s1\"><strong><br /></strong></span></p>\n<p class=\"p3\"><span class=\"s1\"><strong></strong></span></p>\n<p class=\"p4\"><span class=\"s1\"><strong>Read the transcript </strong><a href=\"https://www.fortheloveofclimbing.com/episodes/mini-episode-9-i-did-not-know\"><span class=\"s3\"><strong>here</strong></span></a><strong>.</strong></span></p>\n<p class=\"p4\"><span class=\"s1\"><strong><br /></strong></span></p>\n<p class=\"p3\"><span class=\"s1\"><strong></strong></span></p>\n<p class=\"p4\"><span class=\"s1\"><strong>Follow us on </strong><a href=\"https://www.instagram.com/inheadlights/\"><span class=\"s4\"><strong>Instagram</strong></span></a><strong> for podcast (pod-Kath?) updates and general life things.</strong></span></p>\n<p class=\"p4\"><span class=\"s1\"><strong><br /></strong></span></p>\n<p class=\"p3\"><span class=\"s1\"><strong></strong></span></p>\n<p class=\"p4\"><span class=\"s1\"><strong>Support us on </strong><a href=\"https://www.patreon.com/fortheloveofclimbing\"><span class=\"s4\"><strong>Patreon</strong></span></a><strong> in exchange for a warm, fuzzy feeling.</strong></span></p>",
  "pub_date_ms": 1619869680000,
  "guid_from_rss": "http://www.blubrry.com/fortheloveofclimbing/76270669/26-im-a-liver-not-a-fighter/",
  "listennotes_url": "https://www.listennotes.com/e/f984973b797443308f87d2f2216bd5f8/",
  "audio_length_sec": 2201,
  "explicit_content": false,
  "maybe_audio_invalid": false,
  "listennotes_edit_url": "https://www.listennotes.com/e/f984973b797443308f87d2f2216bd5f8/#edit"
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
        "google_url": "",
        "spotify_url": "https://open.spotify.com/show/0QhzjA2zKdKgIQsd2ltHtp?si=1G6nu1YnRKiM9XPgjs3fyw",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "maedinindia",
        "facebook_handle": "maedinindia",
        "instagram_handle": "maedinindia"
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/maed-in-india-maed-in-india-LZHgafrGi0q-y2oQTwMN73p.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/maed-in-india-maed-in-india-5BQCUd3FfYV-y2oQTwMN73p.300x300.jpg",
      "is_claimed": false,
      "description": "Maed in India - India's first indie music podcast that showcases the best Indian independent musicians from India and abroad. Each episode presents an interview with an artist/band along with an exclusive stripped down session or acoustic renditions of their original music. The weekly show prides itself on being the destination for new music, little known stories, and unreleased music never heard before.\n\nIt features all kinds of artists from new-comers to veterans and under a variety of genres from hip hop, blues, soul, to folk, punk, rock, and everything in between.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 44,
      "total_episodes": 251,
      "listennotes_url": "https://www.listennotes.com/c/c463d5980b8e480fb78db6b3ed6be115/",
      "explicit_content": false,
      "latest_pub_date_ms": 1619393400000,
      "earliest_pub_date_ms": 1434346200250,
      "listen_score_global_rank": "1.5%"
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
      "thumbnail": "https://cdn-images-1.listennotes.com/channel/image/b956ac6715da4f5bb57a3f770824a061.jpg",
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
      "type": "episodic",
      "email": "trialbyerror@arre.co.in",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/trial-by-error-the-aarushi-files-arre--hleb0zIEPC.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/trial-by-error-the-aarushi-files-arre--hleb0zIEPC.300x300.jpg",
      "is_claimed": false,
      "description": "Trial by Error, adapted from Avirook Sen's haunting book Aarushi, is an eight-part investigative audio series that narrates the story of the Noida double murder, and the controversial trial that convicted the Talwars. Follow investigative journalist Nishita Jha as she turns a lens on the murky details of the case to see whether justice truly has been served.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 42,
      "total_episodes": 8,
      "listennotes_url": "https://www.listennotes.com/c/10a1ff15904548978355ff69166b2578/",
      "explicit_content": false,
      "latest_pub_date_ms": 1468183671000,
      "earliest_pub_date_ms": 1462135535000,
      "listen_score_global_rank": "2%"
    },
    {
      "id": "00c5d061be3d42bb954b7a05dc044166",
      "rss": "http://feeds.soundcloud.com/users/soundcloud:users:152973991/sounds.rss",
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
        "twitter_handle": "cheapadventures",
        "facebook_handle": "theadventuresofcheapbeer",
        "instagram_handle": ""
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/adventures-of-cheap-beer-adventures-of-7f4UTIhYQ01-vkZfSh-TJCt.1400x1400.jpg",
      "title": "Adventures of Cheap Beer",
      "country": "United States",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/adventures-of-cheap-beer-adventures-of-YAOIas3ND7W-vkZfSh-TJCt.300x300.jpg",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/watcha-ivm-podcasts-Qv2WOYNyz5V-HEvn-LS7uyo.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/watcha-ivm-podcasts-wSHZVq-i_TJ-HEvn-LS7uyo.300x300.jpg",
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
      "rss": "http://feeds.soundcloud.com/users/soundcloud:users:90732272/sounds.rss",
      "type": "episodic",
      "email": "synthesistalk@gmail.com",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/syntalk-syntalk-XAK8ijB3nPD-j2nFBUVDzq_.1006x1006.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/syntalk-syntalk-8trk50CK1vn-j2nFBUVDzq_.300x300.jpg",
      "is_claimed": false,
      "description": "f(q) = Is everything moving? (#TSAM)\n\nSynTalk is a freewheeling interdisciplinary talk show with a philosophical approach to understanding the world from a long term perspective.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 33,
      "total_episodes": 171,
      "listennotes_url": "https://www.listennotes.com/c/c40188a1a51249a3bafb11793a011359/",
      "explicit_content": false,
      "latest_pub_date_ms": 1594488821000,
      "earliest_pub_date_ms": 1405191856170,
      "listen_score_global_rank": "5%"
    },
    {
      "id": "24ece1d0922d4d9a9659e9e6cb2b241e",
      "rss": "https://rss.simplecast.com/podcasts/1298/rss",
      "type": "episodic",
      "email": "hello@neilpatel.co",
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
        "twitter_handle": "Indianstartupsh",
        "facebook_handle": "indianstartupshow",
        "instagram_handle": ""
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-indian-startup-show-neil-patel-rlWOvzA5b6V-9574y1CKU8j.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-indian-startup-show-neil-patel-BeZ64kRjnOM-9574y1CKU8j.300x300.jpg",
      "is_claimed": false,
      "description": "A Weekly Podcast Show About Indian Startups\nEntrepreneurs & More !\nHosted by Neil Patel & Friends\n",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 42,
      "total_episodes": 174,
      "listennotes_url": "https://www.listennotes.com/c/24ece1d0922d4d9a9659e9e6cb2b241e/",
      "explicit_content": false,
      "latest_pub_date_ms": 1619046000000,
      "earliest_pub_date_ms": 1439366880162,
      "listen_score_global_rank": "2%"
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/sixth-world-radio-TofYFXxGOKn.600x600.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/sixth-world-radio-TofYFXxGOKn.300x300.jpg",
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
        "google_url": "",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "GeekFruitHQ",
        "facebook_handle": "ivmpodcasts",
        "instagram_handle": "ivmpodcasts"
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/geek-fruit-podcast-ivm-podcasts-eLbAdx-J8yq-hNgR81AbBO4.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/geek-fruit-podcast-ivm-podcasts-lS_yLej9CAr-hNgR81AbBO4.300x300.jpg",
      "is_claimed": true,
      "description": "We spend way too much time discussing minuscule facts, character dynamics, story arcs and unique concepts in the wonderful world of science-fiction and overall nerd culture. Think you do that too? Find us and become one with the geeks! And believe it; the Force is totally strong with us.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 35,
      "total_episodes": 341,
      "listennotes_url": "https://www.listennotes.com/c/4151ce9377a6435c8aac7d23f306243d/",
      "explicit_content": false,
      "latest_pub_date_ms": 1595810106000,
      "earliest_pub_date_ms": 1450868870327,
      "listen_score_global_rank": "5%"
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
        "google_url": "",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "cyrussaysin",
        "facebook_handle": "ivmpodcasts",
        "instagram_handle": "ivmpodcasts"
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/cyrus-says-ivm-podcasts-gt9cFehsliV-1q2UDTO6ztZ.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/cyrus-says-ivm-podcasts-B8_wofUFStK-1q2UDTO6ztZ.300x300.jpg",
      "is_claimed": true,
      "description": "Broadcasting twice a week with a rotating panel of guests, Cyrus Says is the definitive show on life in urban India, politics, sports, civic sense, traffic, kids, food, and everything that matters. Mostly.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 53,
      "total_episodes": 692,
      "listennotes_url": "https://www.listennotes.com/c/2641ed2ce5524b3da43b8f19fe0f5ae9/",
      "explicit_content": false,
      "latest_pub_date_ms": 1619786109000,
      "earliest_pub_date_ms": 1426829400582,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-real-food-podcast-audiomatic-Kb91aMGW8JA.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-real-food-podcast-audiomatic-Kb91aMGW8JA.300x300.jpg",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/all-india-bakchod-all-india-bakchod-wx3rMv6WfdH-kgcdJ-xKmAL.1023x990.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/all-india-bakchod-all-india-bakchod-4kPM70-W_Ue-kgcdJ-xKmAL.300x290.jpg",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/our-last-week-audiomatic-ed96Q4pHgsE.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/our-last-week-audiomatic-ed96Q4pHgsE.300x300.jpg",
      "is_claimed": false,
      "description": "Podcast by Our Last Week",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": null,
      "total_episodes": 45,
      "listennotes_url": "https://www.listennotes.com/c/d203864a67fb43b1a98b7107cabeaa4b/",
      "explicit_content": false,
      "latest_pub_date_ms": 1579417200000,
      "earliest_pub_date_ms": 1431062738044,
      "listen_score_global_rank": null
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
        "google_url": "",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "historyofindiapodcast",
        "instagram_handle": ""
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-history-of-india-podcast-kit-patrick-rpU53uF0ckj-lE64kqFsTHC.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-history-of-india-podcast-kit-patrick-kCpZW6V-tnP-lE64kqFsTHC.300x300.jpg",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/kaanmasti-hoezaay-flIyRD8c4VU.600x600.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/kaanmasti-hoezaay-flIyRD8c4VU.300x300.jpg",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/tfg-sports-podcast-ivm-podcasts-TnJ7PSoMCbA-5Mq0usV3E84.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/tfg-sports-podcast-ivm-podcasts-HjVfPrghzdy-5Mq0usV3E84.300x300.jpg",
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
  "total": 3545,
  "has_next": true,
  "page_number": 2,
  "has_previous": true,
  "curated_lists": [
    {
      "id": "c6be5T-_g84",
      "title": "The 18 best tech podcasts (that aren't 'Reply All')",
      "total": 18,
      "podcasts": [
        {
          "id": "1ed81603a1754ce2aacf3879313a34a6",
          "image": "https://cdn-images-1.listennotes.com/podcasts/there-are-no-girls-on-the-internet-h1n0oTV5DQi-GsR_U2Yhk5J.1400x1400.jpg",
          "title": "There Are No Girls on the Internet",
          "publisher": "iHeartRadio",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/there-are-no-girls-on-the-internet-gxNdemI3FCc-GsR_U2Yhk5J.300x300.jpg",
          "listen_score": 53,
          "listennotes_url": "https://www.listennotes.com/c/1ed81603a1754ce2aacf3879313a34a6/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "1f30a73c49fb4aa1b3c87af28121f69c",
          "image": "https://cdn-images-1.listennotes.com/podcasts/get-wired-ICd5wYSxNb0-2Dex4CwKpEP.1400x1400.jpg",
          "title": "Get WIRED",
          "publisher": "WIRED & Cond\u00e9 Nast",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/get-wired-ZjAbcI2Kqdi-2Dex4CwKpEP.300x300.jpg",
          "listen_score": 46,
          "listennotes_url": "https://www.listennotes.com/c/1f30a73c49fb4aa1b3c87af28121f69c/",
          "listen_score_global_rank": "1.5%"
        },
        {
          "id": "c2955c3615da4a5e93e66c4be7577012",
          "image": "https://cdn-images-1.listennotes.com/podcasts/rabbit-hole-the-new-york-times-bTHknl-FsMZ-L1T0AguhCd9.1400x1400.jpg",
          "title": "Rabbit Hole",
          "publisher": "The New York Times",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/rabbit-hole-the-new-york-times-Ew0A986HGjn-L1T0AguhCd9.300x300.jpg",
          "listen_score": 73,
          "listennotes_url": "https://www.listennotes.com/c/c2955c3615da4a5e93e66c4be7577012/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "0542eaab7de1459fa234d84b311be502",
          "image": "https://cdn-images-1.listennotes.com/podcasts/land-of-the-giants-recode-TWMUrJwSKiE-lHv0Wt-PcMh.1400x1400.jpg",
          "title": "Land of the Giants",
          "publisher": "Recode",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/land-of-the-giants-recode-6vWEOpJstxj-lHv0Wt-PcMh.300x300.jpg",
          "listen_score": 62,
          "listennotes_url": "https://www.listennotes.com/c/0542eaab7de1459fa234d84b311be502/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "f34331ecc2db4b3bab17f00c477458ca",
          "image": "https://cdn-images-1.listennotes.com/podcasts/qanon-anonymous-julian-feeld-travis-view-l4sd9F3Gezg-My4uHNvEbPI.970x970.jpg",
          "title": "QAnon Anonymous",
          "publisher": "Julian Feeld, Travis View & Jake Rockatansky",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/qanon-anonymous-julian-feeld-travis-view-KqFvWzrOCa--My4uHNvEbPI.300x300.jpg",
          "listen_score": 60,
          "listennotes_url": "https://www.listennotes.com/c/f34331ecc2db4b3bab17f00c477458ca/",
          "listen_score_global_rank": "0.5%"
        }
      ],
      "source_url": "https://mashable.com/article/best-tech-podcasts-reply-all-alternatives/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"But maybe it's time we do our own version of a Super Tech Support, with a special round of Yes-Yes-No on tech podcasts you might not have heard of yet, but should know about.\"",
      "pub_date_ms": 1618246951193,
      "source_domain": "mashable.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/the-18-best-tech-podcasts-that-arent-c6be5T-_g84/"
    },
    {
      "id": "PCejNmfW1Z0",
      "title": "Top 5 Gaming Podcasts To Listen To In 2021",
      "total": 5,
      "podcasts": [
        {
          "id": "41d3488f1460443683d9c71fafc336cb",
          "image": "https://cdn-images-1.listennotes.com/podcasts/major-nelson-radio-larry-major-nelson-hryb-1Tf8eCUX495-FebBzDUcw6l.1400x1400.jpg",
          "title": "The Xbox Podcast (Was Major Nelson Radio)",
          "publisher": "Larry 'Major Nelson' Hryb",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/major-nelson-radio-larry-major-nelson-hryb-Qzvw3Rn6SWM-FebBzDUcw6l.300x300.jpg",
          "listen_score": 58,
          "listennotes_url": "https://www.listennotes.com/c/41d3488f1460443683d9c71fafc336cb/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "22916d423e8844deba99a33231a195ff",
          "image": "https://cdn-images-1.listennotes.com/podcasts/remember-the-game-retro-gaming-podcast-adam-8BOyjVGrWs1-H17CwDpYZbt.1400x1400.jpg",
          "title": "Remember The Game? Retro Gaming Podcast",
          "publisher": "Adam Blank",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/remember-the-game-retro-gaming-podcast-adam-e2inbwXW78C-H17CwDpYZbt.300x300.jpg",
          "listen_score": 40,
          "listennotes_url": "https://www.listennotes.com/c/22916d423e8844deba99a33231a195ff/",
          "listen_score_global_rank": "2%"
        },
        {
          "id": "566ff1b0697c474283cef5a7bfc98e8a",
          "image": "https://cdn-images-1.listennotes.com/podcasts/whats-good-games-a-video-game-podcast-whats-9br7u_qaBGo-GoZRVBe3y-0.1400x1400.jpg",
          "title": "What's Good Games: A Video Game Podcast",
          "publisher": "What's Good Games",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/whats-good-games-a-video-game-podcast-whats-UQBE_2HoOL3-GoZRVBe3y-0.300x300.jpg",
          "listen_score": 64,
          "listennotes_url": "https://www.listennotes.com/c/566ff1b0697c474283cef5a7bfc98e8a/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "b1daa6e2c3454c30abf7ef48ede585f4",
          "image": "https://cdn-images-1.listennotes.com/podcasts/video-game-outsiders-john-jacobsen-and-W37HlzdN0Uq-fEjpvLNV3Gq.1400x1400.jpg",
          "title": "Video Game Outsiders",
          "publisher": "John Jacobsen and Michelle Madison",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/video-game-outsiders-john-jacobsen-and-rbXc2ZUH3tL-fEjpvLNV3Gq.300x300.jpg",
          "listen_score": 50,
          "listennotes_url": "https://www.listennotes.com/c/b1daa6e2c3454c30abf7ef48ede585f4/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "778cebb5c9654e7792fdde70731d7a93",
          "image": "https://cdn-images-1.listennotes.com/podcasts/kinda-funny-games-daily-video-games-news-vW5N0JISYM6-OIPJ7blyuK2.1400x1400.jpg",
          "title": "Kinda Funny Games Daily: Video Games News Podcast",
          "publisher": "Kinda Funny",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/kinda-funny-games-daily-video-games-news-EO83oGrwsTn-OIPJ7blyuK2.300x300.jpg",
          "listen_score": 68,
          "listennotes_url": "https://www.listennotes.com/c/778cebb5c9654e7792fdde70731d7a93/",
          "listen_score_global_rank": "0.05%"
        }
      ],
      "source_url": "https://www.gamespace.com/featured/top-5-gaming-podcasts-to-listen-to-in-2021/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"I listen to a ton of different podcasts, but today I am sharing the five podcasts that I make sure to listen to every week. All of them can be found at the websites I\u2019ve linked below or through most any podcast service of your choice. I hope you enjoy what they have to offer, and be sure to list your favorites in the comments below.\"",
      "pub_date_ms": 1617506302152,
      "source_domain": "www.gamespace.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/top-5-gaming-podcasts-to-listen-to-in-PCejNmfW1Z0/"
    },
    {
      "id": "jWbNi1RQZYs",
      "title": "10 Body-Positivity Podcasts to Download for a Boost of Self-Love",
      "total": 10,
      "podcasts": [
        {
          "id": "4a66cd58b54d478f8c5d10361a051eb6",
          "image": "https://cdn-images-1.listennotes.com/podcasts/eat-the-rules-with-summer-innanen-summer-X9tRNIbhd53-p8KXj6MkmZ_.1400x1400.jpg",
          "title": "Eat the Rules with Summer Innanen",
          "publisher": "Summer Innanen",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/eat-the-rules-with-summer-innanen-summer-buyEnSBlmVW-p8KXj6MkmZ_.300x300.jpg",
          "listen_score": 51,
          "listennotes_url": "https://www.listennotes.com/c/4a66cd58b54d478f8c5d10361a051eb6/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "09a61287e0ed414d9921cab6762dae66",
          "image": "https://cdn-images-1.listennotes.com/podcasts/fat-girls-club-jessica-torres-liesl-binx-l3xw7BkDYWI.1400x1400.jpg",
          "title": "Fat Girls Club ",
          "publisher": "Jessica Torres & Liesl Binx",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/fat-girls-club-jessica-torres-liesl-binx-l3xw7BkDYWI.300x300.jpg",
          "listen_score": 43,
          "listennotes_url": "https://www.listennotes.com/c/09a61287e0ed414d9921cab6762dae66/",
          "listen_score_global_rank": "1.5%"
        },
        {
          "id": "edbd84ed2b874fbca126fa112d057d9a",
          "image": "https://cdn-images-1.listennotes.com/podcasts/nutrition-matters-podcast-paige-smathers-kR9hWJPvdmC-O251LDw0tRC.640x640.jpg",
          "title": "Nutrition Matters Podcast",
          "publisher": "Paige Smathers, RDN, CD",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/nutrition-matters-podcast-paige-smathers-z5BWrF1yYRf-O251LDw0tRC.300x300.jpg",
          "listen_score": 57,
          "listennotes_url": "https://www.listennotes.com/c/edbd84ed2b874fbca126fa112d057d9a/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "24262b04040f451a859a4d86fd43665b",
          "image": "https://cdn-images-1.listennotes.com/podcasts/yes-body-politics-tresla-and-guru-shabd-8yCT6SW5g0s.1400x1400.jpg",
          "title": "Yes& Body Politics",
          "publisher": "Tresla and Guru Shabd",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/yes-body-politics-tresla-and-guru-shabd-8yCT6SW5g0s.300x300.jpg",
          "listen_score": 26,
          "listennotes_url": "https://www.listennotes.com/c/24262b04040f451a859a4d86fd43665b/",
          "listen_score_global_rank": "10%"
        },
        {
          "id": "83433fcabd5645308799043b9871649c",
          "image": "https://cdn-images-1.listennotes.com/podcasts/call-your-girlfriend-ann-friedman-and-fTF7QdKMwnh-i7XLJ4QmTAh.1400x1400.jpg",
          "title": "Call Your Girlfriend",
          "publisher": "Ann Friedman and Aminatou Sow",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/call-your-girlfriend-ann-friedman-and-8TORHFQcKIh-i7XLJ4QmTAh.300x300.jpg",
          "listen_score": 71,
          "listennotes_url": "https://www.listennotes.com/c/83433fcabd5645308799043b9871649c/",
          "listen_score_global_rank": "0.05%"
        }
      ],
      "source_url": "https://www.realsimple.com/work-life/life-strategies/podcasts/podcasts-for-body-acceptance-and-positivity?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"Here are 10 fantastic podcasts to help you start\u2014or continue\u2014your journey toward body acceptance and positivity and find a community of like-minded listeners along the way.\"",
      "pub_date_ms": 1617506219017,
      "source_domain": "www.realsimple.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/10-body-positivity-podcasts-to-jWbNi1RQZYs/"
    },
    {
      "id": "a1BEHi6M3jI",
      "title": "The 6 Best News Podcasts for Kids",
      "total": 5,
      "podcasts": [
        {
          "id": "91a4870552164a9ab94330a003db0926",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-week-junior-show-fun-kids-mrJdKq4S7yE-AgmWXCF7120.1400x1400.jpg",
          "title": "The Week Junior Show",
          "publisher": "Fun Kids",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-week-junior-show-fun-kids-Ht5IYlVAjvn-AgmWXCF7120.300x300.jpg",
          "listen_score": 57,
          "listennotes_url": "https://www.listennotes.com/c/91a4870552164a9ab94330a003db0926/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "5b883c1ab1094345b944a4f5f3f86673",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-ten-news-small-but-mighty-media-next-WShnbuzp-P3-X0GqmEJT4xN.1400x1400.jpg",
          "title": "The Ten News",
          "publisher": "Small But Mighty Media, Next Chapter Podcasts & iHeartRadio",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-ten-news-small-but-mighty-media-next-3j4zoc5NOyD-X0GqmEJT4xN.300x300.jpg",
          "listen_score": 44,
          "listennotes_url": "https://www.listennotes.com/c/5b883c1ab1094345b944a4f5f3f86673/",
          "listen_score_global_rank": "1.5%"
        },
        {
          "id": "2cbd986d3d8542a5bdd0795aec9a9e13",
          "image": "https://cdn-images-1.listennotes.com/podcasts/abc-kids-news-time-abc-kids-listen-yNbI2MUXQLs-eOBxRbqSFXj.1400x1400.jpg",
          "title": "ABC KIDS News Time",
          "publisher": "ABC KIDS listen",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/abc-kids-news-time-abc-kids-listen-6cNiFpG3Syb-eOBxRbqSFXj.300x300.jpg",
          "listen_score": 50,
          "listennotes_url": "https://www.listennotes.com/c/2cbd986d3d8542a5bdd0795aec9a9e13/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "7aa7f0b533884f76a435600ff5b3935c",
          "image": "https://cdn-images-1.listennotes.com/podcasts/kidnuz-kidnuz-hSGELuCJHDT-kNo8xgZuGqj.1400x1400.jpg",
          "title": "KidNuz",
          "publisher": "KidNuz",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/kidnuz-kidnuz-3BCUWsupIZa-kNo8xgZuGqj.300x300.jpg",
          "listen_score": 57,
          "listennotes_url": "https://www.listennotes.com/c/7aa7f0b533884f76a435600ff5b3935c/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "0b8e88bb527545a190a44eace8e27a65",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-big-fib-gen-z-media-Ow8gNWPAchM-YlCDy8_IV9m.1400x1400.jpg",
          "title": "The Big Fib",
          "publisher": "Gen-Z Media",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-big-fib-gen-z-media--AKZzJ8yOYx-YlCDy8_IV9m.300x300.jpg",
          "listen_score": 68,
          "listennotes_url": "https://www.listennotes.com/c/0b8e88bb527545a190a44eace8e27a65/",
          "listen_score_global_rank": "0.05%"
        }
      ],
      "source_url": "https://www.nymetroparents.com/article/news-podcasts-for-kids?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"It\u2019s hard enough for adults to keep up with the news\u2014but kids also need to know what\u2019s going on, especially now. And they need to be informed by sources that can filter and craft the stories appropriately. We recently discovered some fantastic news podcasts for kids that manage to enlighten kids while also entertaining them. Here are some of our favorite.\"",
      "pub_date_ms": 1617506115594,
      "source_domain": "www.nymetroparents.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/the-6-best-news-podcasts-for-kids-a1BEHi6M3jI/"
    },
    {
      "id": "2kmaBgw_DLV",
      "title": "7 Beauty Podcasts We Know You'll Love",
      "total": 7,
      "podcasts": [
        {
          "id": "55d4b4f2e3cc480dbd26abdc5b323d27",
          "image": "https://cdn-images-1.listennotes.com/podcasts/fat-mascara-embassy-row-7OPFziKlZd8.1400x1400.jpg",
          "title": "Fat Mascara",
          "publisher": "Embassy Row",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/fat-mascara-embassy-row-7OPFziKlZd8.300x300.jpg",
          "listen_score": null,
          "listennotes_url": "https://www.listennotes.com/c/55d4b4f2e3cc480dbd26abdc5b323d27/",
          "listen_score_global_rank": null
        },
        {
          "id": "bd69ada9f4ed41fb984bfeb878e31ac9",
          "image": "https://cdn-images-1.listennotes.com/podcasts/beauty-from-the-heart-Vq7lt9bn8Aj-mL3dxjTlIW0.1400x1400.jpg",
          "title": "Beauty from the Heart ",
          "publisher": "Rose Gallagher",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/beauty-from-the-heart-z7r98mnQBEK-mL3dxjTlIW0.300x300.jpg",
          "listen_score": 43,
          "listennotes_url": "https://www.listennotes.com/c/bd69ada9f4ed41fb984bfeb878e31ac9/",
          "listen_score_global_rank": "1.5%"
        },
        {
          "id": "9bbb587fecd144dba275f0c5154b7c35",
          "image": "https://cdn-images-1.listennotes.com/podcasts/breaking-beauty-podcast-dear-media-jill-T_o-HM1GBsj-BIaMtbCvm_i.1400x1400.jpg",
          "title": "Breaking Beauty Podcast",
          "publisher": "Dear Media, Jill Dunn and Carlene Higgins",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/breaking-beauty-podcast-dear-media-jill-G6iRmtY0fDc-BIaMtbCvm_i.300x300.jpg",
          "listen_score": 60,
          "listennotes_url": "https://www.listennotes.com/c/9bbb587fecd144dba275f0c5154b7c35/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "8fa2ff7d7ad34df79fe3df783ce3dacf",
          "image": "https://cdn-images-1.listennotes.com/podcasts/allure-the-science-of-beauty-cZE81bXwMlH-Oecp2utrWid.1400x1400.jpg",
          "title": "Allure: The Science of Beauty",
          "publisher": "Allure & Cond\u00e9 Nast",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/allure-the-science-of-beauty-ibqkStwX-H7-Oecp2utrWid.300x300.jpg",
          "listen_score": 48,
          "listennotes_url": "https://www.listennotes.com/c/8fa2ff7d7ad34df79fe3df783ce3dacf/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "e59ccaddd4684c908182844833e7b2e5",
          "image": "https://cdn-images-1.listennotes.com/podcasts/glowing-up-starburns-audio-Hz_6h9FkCn--9NcBGdZ_ejn.1400x1400.jpg",
          "title": "Glowing Up",
          "publisher": "Starburns Audio",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/glowing-up-starburns-audio-yQeh4tJgfBU-9NcBGdZ_ejn.300x300.jpg",
          "listen_score": 61,
          "listennotes_url": "https://www.listennotes.com/c/e59ccaddd4684c908182844833e7b2e5/",
          "listen_score_global_rank": "0.5%"
        }
      ],
      "source_url": "https://gothammag.com/best-beauty-podcasts?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"Pick up your headphones, meet beauty celebrities and get ahead of the trends with these insightful experts.\"",
      "pub_date_ms": 1617506026205,
      "source_domain": "gothammag.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/7-beauty-podcasts-we-know-youll-love-2kmaBgw_DLV/"
    },
    {
      "id": "9aorqKcy6zY",
      "title": "Top 10 Most-Recommended Entrepreneurship Podcasts",
      "total": 10,
      "podcasts": [
        {
          "id": "25212ac3c53240a880dd5032e547047b",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-tim-ferriss-show-tim-ferriss-7NwMpUz5o0S.1400x1400.jpg",
          "title": "The Tim Ferriss Show",
          "publisher": "Tim Ferriss: Bestselling Author, Human Guinea Pig",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-tim-ferriss-show-tim-ferriss-7NwMpUz5o0S.300x300.jpg",
          "listen_score": 82,
          "listennotes_url": "https://www.listennotes.com/c/25212ac3c53240a880dd5032e547047b/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "f9d5885d7cf7485d891e82dea3186640",
          "image": "https://cdn-images-1.listennotes.com/podcasts/how-i-built-this-with-guy-raz-npr-G7ePAvBMW2l-UC0qH23iP9T.1400x1400.jpg",
          "title": "How I Built This with Guy Raz",
          "publisher": "NPR",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/how-i-built-this-with-guy-raz-npr-AbxLGkT50v9-UC0qH23iP9T.300x300.jpg",
          "listen_score": 85,
          "listennotes_url": "https://www.listennotes.com/c/f9d5885d7cf7485d891e82dea3186640/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "1db44068428d431c89be369e8535b6ae",
          "image": "https://cdn-images-1.listennotes.com/podcasts/startup-stories-mixergy-andrew-warner-h-YESKzBfpl-wDrsz0Q7om3.1400x1400.jpg",
          "title": "Startup Stories - Mixergy",
          "publisher": "Andrew Warner",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/startup-stories-mixergy-andrew-warner-T7gwUXcz3IQ-wDrsz0Q7om3.300x300.jpg",
          "listen_score": 59,
          "listennotes_url": "https://www.listennotes.com/c/1db44068428d431c89be369e8535b6ae/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "0d362b13399240de97602ef614acdcbc",
          "image": "https://cdn-images-1.listennotes.com/podcasts/startup-podcast-gimlet-14zU0c_MOmv-n9PpCBTQvoJ.1400x1400.jpg",
          "title": "StartUp Podcast",
          "publisher": "Gimlet",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/startup-podcast-gimlet-8If7QBKU5jb-n9PpCBTQvoJ.300x300.jpg",
          "listen_score": 76,
          "listennotes_url": "https://www.listennotes.com/c/0d362b13399240de97602ef614acdcbc/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "a409b8bb93f44054a7be2d6b30843899",
          "image": "https://cdn-images-1.listennotes.com/podcasts/entrepreneurs-on-fire-business-podcast-john-1l4t9KZmDqY-1WOhT7u6VQb.1400x1400.jpg",
          "title": "Entrepreneurs on Fire",
          "publisher": "John Lee Dumas of EOFire",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/entrepreneurs-on-fire-business-podcast-john-yvaRnjETmfP-1WOhT7u6VQb.300x300.jpg",
          "listen_score": 71,
          "listennotes_url": "https://www.listennotes.com/c/a409b8bb93f44054a7be2d6b30843899/",
          "listen_score_global_rank": "0.05%"
        }
      ],
      "source_url": "https://www.forbes.com/sites/forbescoachescouncil/2021/03/31/top-10-most-recommended-entrepreneurship-podcasts/?sh=1172b333791d&utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"When you are on the run, turn on one of these podcasts for inspiration and knowledge.\"",
      "pub_date_ms": 1617505344788,
      "source_domain": "www.forbes.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/top-10-most-recommended-9aorqKcy6zY/"
    },
    {
      "id": "LzZ4wjMTY6i",
      "title": "The 10 Best Finance Podcasts for Beginners, Investors\u2014and Everyone Else",
      "total": 10,
      "podcasts": [
        {
          "id": "9a94d1ed8a7a47a8b988e2c451171888",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-fairer-cents-women-money-and-the-fight-wWdikbrnG5U-n5DVpXtH7kr.1400x1399.jpg",
          "title": "The Fairer Cents: Women, Money and the Fight to Get Equal",
          "publisher": "Tanja Hester & Kara Perez",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-fairer-cents-women-money-and-the-fight-Yjn1s5okyme-n5DVpXtH7kr.300x299.jpg",
          "listen_score": 53,
          "listennotes_url": "https://www.listennotes.com/c/9a94d1ed8a7a47a8b988e2c451171888/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "b925a2e959e14ee79b4f5294ea6f5a37",
          "image": "https://cdn-images-1.listennotes.com/podcasts/brown-ambition-mandi-woodruff-and-tiffany-B8H5Ms2pQq4-f39F1YXI-8r.1400x1400.jpg",
          "title": "Brown Ambition",
          "publisher": "Mandi Woodruff and Tiffany Aliche / Cumulus Podcast Network",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/brown-ambition-mandi-woodruff-and-tiffany-yYO6WL5NVqA-f39F1YXI-8r.300x300.jpg",
          "listen_score": 61,
          "listennotes_url": "https://www.listennotes.com/c/b925a2e959e14ee79b4f5294ea6f5a37/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "7cb45584ac0c4db9a9deb74c70d413f5",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-clever-girls-know-podcast-clever-girl-yuLDkrxXsvj-vmNJ8k_c2LM.1400x1400.jpg",
          "title": "The Clever Girls Know Podcast",
          "publisher": "Clever Girl Finance",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-clever-girls-know-podcast-clever-girl-LpPJciH8v_U-vmNJ8k_c2LM.300x300.jpg",
          "listen_score": 57,
          "listennotes_url": "https://www.listennotes.com/c/7cb45584ac0c4db9a9deb74c70d413f5/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "4febd3594ce14b50a12341219ba63780",
          "image": "https://cdn-images-1.listennotes.com/podcasts/so-money-with-farnoosh-torabi-farnoosh-torabi-zm0_KRCLgbG-mOb-SgP2jlN.1400x1400.jpg",
          "title": "So Money with Farnoosh Torabi",
          "publisher": "Farnoosh Torabi ",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/so-money-with-farnoosh-torabi-farnoosh-torabi-v3xyhOXSAL8-mOb-SgP2jlN.300x300.jpg",
          "listen_score": 64,
          "listennotes_url": "https://www.listennotes.com/c/4febd3594ce14b50a12341219ba63780/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "0b0f001692ac437a9566edf42f4bbe9e",
          "image": "https://cdn-images-1.listennotes.com/podcasts/financial-grownup-with-bobbi-rebell-cfp-sadENLz3SpM-tPYNqkOnlCW.1400x1400.jpg",
          "title": "Financial Grownup with Bobbi Rebell CFP",
          "publisher": "Bobbi Rebell",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/financial-grownup-with-bobbi-rebell-cfp-vZ8dPDqYp6b-tPYNqkOnlCW.300x300.jpg",
          "listen_score": 46,
          "listennotes_url": "https://www.listennotes.com/c/0b0f001692ac437a9566edf42f4bbe9e/",
          "listen_score_global_rank": "1%"
        }
      ],
      "source_url": "https://www.realsimple.com/work-life/money/best-finance-podcasts?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"Want to manifest money, or dig deeper into the (formerly) intimidating world of investing? Listen in to the 10 best finance podcasts\u2014that won't overwhelm you with stuffy money lingo.\"",
      "pub_date_ms": 1617500670755,
      "source_domain": "www.realsimple.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/the-10-best-finance-podcasts-for-LzZ4wjMTY6i/"
    },
    {
      "id": "ui6kzrx8SJd",
      "title": "7 Podcasts to Binge in a Day",
      "total": 7,
      "podcasts": [
        {
          "id": "842eed0c7d3647a8b819c61c49e92f48",
          "image": "https://cdn-images-1.listennotes.com/podcasts/wind-of-change-pineapple-street-studios-6QUJDg9h0Pc-I9qu80sCmzw.1400x1400.jpg",
          "title": "Wind of Change",
          "publisher": "Pineapple Street Studios / Crooked Media / Spotify",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/wind-of-change-pineapple-street-studios-XLVNI-y9Hjr-I9qu80sCmzw.300x300.jpg",
          "listen_score": 69,
          "listennotes_url": "https://www.listennotes.com/c/842eed0c7d3647a8b819c61c49e92f48/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "581fc67e281047d09fa90f7782c51feb",
          "image": "https://cdn-images-1.listennotes.com/podcasts/dirty-john-la-times-wondery-JmyBVLS16fd-1rJzL4wEyuY.1400x1400.jpg",
          "title": "Dirty John",
          "publisher": "Los Angeles Times | Wondery",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/dirty-john-la-times-wondery-eJbmoxLg8-I-1rJzL4wEyuY.300x300.jpg",
          "listen_score": 86,
          "listennotes_url": "https://www.listennotes.com/c/581fc67e281047d09fa90f7782c51feb/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "54a67c045e334bbb9c8cb066bc98480d",
          "image": "https://cdn-images-1.listennotes.com/podcasts/mystery-show-gimlet--DQ4lWkq_JC.600x600.jpg",
          "title": "Mystery Show",
          "publisher": "Gimlet",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/mystery-show-gimlet--DQ4lWkq_JC.300x300.jpg",
          "listen_score": 72,
          "listennotes_url": "https://www.listennotes.com/c/54a67c045e334bbb9c8cb066bc98480d/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "507cc88e1fe94bb9aa7008a0250241be",
          "image": "https://cdn-images-1.listennotes.com/podcasts/passenger-list-passenger-list-and-radiotopia-fb4HaCwOv_s-hY46NRDu3vz.1400x1400.jpg",
          "title": "Passenger List",
          "publisher": "Passenger List and Radiotopia",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/passenger-list-passenger-list-and-radiotopia-4TVcm2HzgWy-hY46NRDu3vz.300x300.jpg",
          "listen_score": 65,
          "listennotes_url": "https://www.listennotes.com/c/507cc88e1fe94bb9aa7008a0250241be/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "d2ced1d1ae86438ab1eca93dfa91f5a0",
          "image": "https://cdn-images-1.listennotes.com/podcasts/dolly-partons-america-W4Rz9NP-Gw2-byxXL4fwK6J.1400x1400.jpg",
          "title": "Dolly Parton's America",
          "publisher": "WNYC Studios & OSM Audio ",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/dolly-partons-america-wygrH4V9jJS-byxXL4fwK6J.300x300.jpg",
          "listen_score": 79,
          "listennotes_url": "https://www.listennotes.com/c/d2ced1d1ae86438ab1eca93dfa91f5a0/",
          "listen_score_global_rank": "0.01%"
        }
      ],
      "source_url": "https://www.nytimes.com/2021/03/30/arts/podcasts-binge.html?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"Whether you\u2019re craving a thriller, a spy documentary or an exploration of an American musical icon, each of these limited series can be enjoyed in one big gulp.\"",
      "pub_date_ms": 1617500480927,
      "source_domain": "www.nytimes.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/7-podcasts-to-binge-in-a-day-ui6kzrx8SJd/"
    },
    {
      "id": "QefMkxU_oTg",
      "title": "These 9 Podcasts Will Keep You Thoroughly Engrossed on Your Next Walk",
      "total": 9,
      "podcasts": [
        {
          "id": "d50f00edeb8c446f955f80716154a3a3",
          "image": "https://cdn-images-1.listennotes.com/podcasts/armchair-expert-with-dax-shepard-armchair-aKx1MHSXjw5-DNVvf-Jygxn.1400x1400.jpg",
          "title": "Armchair Expert with Dax Shepard",
          "publisher": "Armchair Umbrella",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/armchair-expert-with-dax-shepard-armchair-PrWuvUt0Zxq-DNVvf-Jygxn.300x300.jpg",
          "listen_score": 89,
          "listennotes_url": "https://www.listennotes.com/c/d50f00edeb8c446f955f80716154a3a3/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "9a08629f7a8f4251a56c0c41f8f8a92a",
          "image": "https://cdn-images-1.listennotes.com/podcasts/happier-with-gretchen-rubin-gretchen-rubin-u6yZWDx4B9--NBPDw-ZbzAC.1400x1400.jpg",
          "title": "Happier with Gretchen Rubin",
          "publisher": "Gretchen Rubin / The Onward Project",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/happier-with-gretchen-rubin-gretchen-rubin-YOwZ3lg_du7-NBPDw-ZbzAC.300x300.jpg",
          "listen_score": 79,
          "listennotes_url": "https://www.listennotes.com/c/9a08629f7a8f4251a56c0c41f8f8a92a/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "c98e2fa600b24af2a5806ee3b8ce5a47",
          "image": "https://cdn-images-1.listennotes.com/podcasts/this-american-life-this-american-life-UdsJ_ibYP16-0iKakprjsG-.1400x1400.jpg",
          "title": "This American Life",
          "publisher": "This American Life",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/this-american-life-this-american-life-Rks9MYyCFS2-0iKakprjsG-.300x300.jpg",
          "listen_score": 91,
          "listennotes_url": "https://www.listennotes.com/c/c98e2fa600b24af2a5806ee3b8ce5a47/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "3822eb1c55814bf98e4f4246d0725e83",
          "image": "https://cdn-images-1.listennotes.com/podcasts/death-sex-money-wnyc-studios-GX52kvChWpo--X7mk3G1dFY.1400x1400.jpg",
          "title": "Death, Sex & Money",
          "publisher": "WNYC Studios",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/death-sex-money-wnyc-studios-moqvPIMg_pz--X7mk3G1dFY.300x300.jpg",
          "listen_score": 74,
          "listennotes_url": "https://www.listennotes.com/c/3822eb1c55814bf98e4f4246d0725e83/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "5b6fa3dc34f84868b83a0ca03a87ea1a",
          "image": "https://cdn-images-1.listennotes.com/podcasts/dr-death-wondery-V7lMDuP5HjF-5ZT0_eNfQOL.1400x1400.jpg",
          "title": "Dr. Death",
          "publisher": "Wondery",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/dr-death-wondery-stpAZau7Pkz-5ZT0_eNfQOL.300x300.jpg",
          "listen_score": 91,
          "listennotes_url": "https://www.listennotes.com/c/5b6fa3dc34f84868b83a0ca03a87ea1a/",
          "listen_score_global_rank": "0.01%"
        }
      ],
      "source_url": "https://www.realsimple.com/work-life/life-strategies/podcasts/podcasts-to-listen-to-while-walking?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"While getting in your steps, you can download a podcast episode or two to catch up on the news, take a deep-dive into pop culture, learn a thing or two about history, or even raise your heart rate just a little bit more with a true-crime thriller. Here are a few podcasts to add to your library that will have you walking even further just so you can finish the episode.\"",
      "pub_date_ms": 1617500389808,
      "source_domain": "www.realsimple.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/these-9-podcasts-will-keep-you-QefMkxU_oTg/"
    },
    {
      "id": "sPo9TAwB4F_",
      "title": "5 fun podcasts to listen to when you want to escape from it all",
      "total": 5,
      "podcasts": [
        {
          "id": "69f4f2748e9b44009904af49fef82f38",
          "image": "https://cdn-images-1.listennotes.com/podcasts/best-friends-with-nicole-byer-and-sasheer-zw9X0gkD5Bh-YObk72QpeVd.1400x1400.jpg",
          "title": "Best Friends with Nicole Byer and Sasheer Zamata",
          "publisher": "Earwolf & Nicole Byer, Sasheer Zamata",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/best-friends-with-nicole-byer-and-sasheer-WsyChgRlnV_-YObk72QpeVd.300x300.jpg",
          "listen_score": 66,
          "listennotes_url": "https://www.listennotes.com/c/69f4f2748e9b44009904af49fef82f38/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "51f18eac5e9d4d2d9e93bf215ebe64c5",
          "image": "https://cdn-images-1.listennotes.com/podcasts/unhappy-hour-with-matt-bellassai-pineapple-jNqpJsuX26_-gvU_9iFpLqy.1400x1400.jpg",
          "title": "Unhappy Hour with Matt Bellassai ",
          "publisher": "Pineapple Street Studios",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/unhappy-hour-with-matt-bellassai-pineapple-eFkEgb4GP6Q-gvU_9iFpLqy.300x300.jpg",
          "listen_score": 62,
          "listennotes_url": "https://www.listennotes.com/c/51f18eac5e9d4d2d9e93bf215ebe64c5/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "267c9d0ae0b24fd0beb5c7bf1aedb306",
          "image": "https://cdn-images-1.listennotes.com/podcasts/thirst-aid-kit-slate-podcasts-7LzpMTNvId0-chxyitAGIFO.1400x1400.jpg",
          "title": "Thirst Aid Kit",
          "publisher": "Slate Podcasts",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/thirst-aid-kit-slate-podcasts-tBrP9xaSq0h-chxyitAGIFO.300x300.jpg",
          "listen_score": 65,
          "listennotes_url": "https://www.listennotes.com/c/267c9d0ae0b24fd0beb5c7bf1aedb306/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "94312887e3e44a6c848f30f57c3de12d",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-bald-and-the-beautiful-with-trixie-R3q0kIC_lcd-VeS0EqArRgk.1400x1400.jpg",
          "title": "The Bald and the Beautiful with Trixie Mattel and Katya Zamo",
          "publisher": "Studio71",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-bald-and-the-beautiful-with-trixie-ur8kCbNWtDi-VeS0EqArRgk.300x300.jpg",
          "listen_score": 68,
          "listennotes_url": "https://www.listennotes.com/c/94312887e3e44a6c848f30f57c3de12d/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "aea6258a7eea42bfb225f60d25ffa94c",
          "image": "https://cdn-images-1.listennotes.com/podcasts/sweet-boys-RaPgrM6ZJAG-OWM3Kaw1G0E.1400x1400.jpg",
          "title": "Sweet Boys",
          "publisher": "The Roost x Sweet Boys",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/sweet-boys-gFfyqI2en8z-OWM3Kaw1G0E.300x300.jpg",
          "listen_score": 68,
          "listennotes_url": "https://www.listennotes.com/c/aea6258a7eea42bfb225f60d25ffa94c/",
          "listen_score_global_rank": "0.05%"
        }
      ],
      "source_url": "https://culturess.com/2021/03/31/5-fun-podcasts-listen-want-escape/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"Here we introduce you to five podcasts where the hosts talk about topics that bring about joy and passion.\"",
      "pub_date_ms": 1617500280284,
      "source_domain": "culturess.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/5-fun-podcasts-to-listen-to-when-you-sPo9TAwB4F_/"
    },
    {
      "id": "QJpti8eFSP1",
      "title": "10 podcasts that every entrepreneur needs to listen to",
      "total": 10,
      "podcasts": [
        {
          "id": "25212ac3c53240a880dd5032e547047b",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-tim-ferriss-show-tim-ferriss-7NwMpUz5o0S.1400x1400.jpg",
          "title": "The Tim Ferriss Show",
          "publisher": "Tim Ferriss: Bestselling Author, Human Guinea Pig",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-tim-ferriss-show-tim-ferriss-7NwMpUz5o0S.300x300.jpg",
          "listen_score": 82,
          "listennotes_url": "https://www.listennotes.com/c/25212ac3c53240a880dd5032e547047b/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "9f6ee51adfb046cc9936490abd2666ce",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-school-of-greatness-lewis-howes-8OujKr7iF2V-H1zdqljixbp.1400x1400.jpg",
          "title": "The School of Greatness",
          "publisher": "Lewis Howes",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-school-of-greatness-lewis-howes-R3oaZzBKnet-H1zdqljixbp.300x300.jpg",
          "listen_score": 78,
          "listennotes_url": "https://www.listennotes.com/c/9f6ee51adfb046cc9936490abd2666ce/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "9a62e2581908415185dee35d2d19f9b5",
          "image": "https://cdn-images-1.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-rMEoeGBJqt1-EKckR36zrnA.1400x1400.jpg",
          "title": "This Week in Startups",
          "publisher": "Jason Calacanis",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-txh7pAS-Xsy-EKckR36zrnA.300x300.jpg",
          "listen_score": 62,
          "listennotes_url": "https://www.listennotes.com/c/9a62e2581908415185dee35d2d19f9b5/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "1db44068428d431c89be369e8535b6ae",
          "image": "https://cdn-images-1.listennotes.com/podcasts/startup-stories-mixergy-andrew-warner-h-YESKzBfpl-wDrsz0Q7om3.1400x1400.jpg",
          "title": "Startup Stories - Mixergy",
          "publisher": "Andrew Warner",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/startup-stories-mixergy-andrew-warner-T7gwUXcz3IQ-wDrsz0Q7om3.300x300.jpg",
          "listen_score": 59,
          "listennotes_url": "https://www.listennotes.com/c/1db44068428d431c89be369e8535b6ae/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "c05fbbf0cd6a4f5fa5c5baf1b63e640a",
          "image": "https://cdn-images-1.listennotes.com/podcasts/minding-my-black-business-dr-jana\u00e8-taylor-I3dZWkj7F4w-21GCmkH_W9Y.1400x1400.jpg",
          "title": "Minding My BLACK Business",
          "publisher": "Dr. JaNa\u00e8 Taylor, podcaster, Black entrepreneur, therapist",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/minding-my-black-business-dr-jana\u00e8-taylor-YqECeGRg52Z-21GCmkH_W9Y.300x300.jpg",
          "listen_score": 39,
          "listennotes_url": "https://www.listennotes.com/c/c05fbbf0cd6a4f5fa5c5baf1b63e640a/",
          "listen_score_global_rank": "2.5%"
        }
      ],
      "source_url": "https://www.image.ie/agenda/podcasts-entrepreneur-201895?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"If you are an entrepreneur, manager or trying to get a business off the ground, then these 10 podcasts are essential listening.\"",
      "pub_date_ms": 1617500171202,
      "source_domain": "www.image.ie",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/10-podcasts-that-every-entrepreneur-QJpti8eFSP1/"
    },
    {
      "id": "1hgiRxJF2df",
      "title": "10 Essential Podcasts From AAPI Creators",
      "total": 10,
      "podcasts": [
        {
          "id": "5ec8fde40739498b91099d246f0c1d79",
          "image": "https://cdn-images-1.listennotes.com/podcasts/self-evident-asian-americas-stories-WItuPyhH945.1400x1400.jpg",
          "title": "Self Evident: Asian America's Stories",
          "publisher": "Self Evident Media",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/self-evident-asian-americas-stories-WItuPyhH945.300x300.jpg",
          "listen_score": 45,
          "listennotes_url": "https://www.listennotes.com/c/5ec8fde40739498b91099d246f0c1d79/",
          "listen_score_global_rank": "1.5%"
        },
        {
          "id": "a19c621f4f8b425bafdd25b9a1aaa204",
          "image": "https://cdn-images-1.listennotes.com/podcasts/asian-enough-O1lVHy2W4U9-hPb47eslkip.1400x1400.jpg",
          "title": "Asian Enough",
          "publisher": "Los Angeles Times",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/asian-enough-pT-dDGuXYJU-hPb47eslkip.300x300.jpg",
          "listen_score": 58,
          "listennotes_url": "https://www.listennotes.com/c/a19c621f4f8b425bafdd25b9a1aaa204/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "58ef24ac8ff844b0925fa2ff4bbaa35a",
          "image": "https://cdn-images-1.listennotes.com/podcasts/long-distance-paola-mardo-0-cNtbqJGBe-DXQLwI2ce43.1400x1400.jpg",
          "title": "Long Distance",
          "publisher": "Paola Mardo",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/long-distance-paola-mardo-i8y2Va3w0IO-DXQLwI2ce43.300x300.jpg",
          "listen_score": 50,
          "listennotes_url": "https://www.listennotes.com/c/58ef24ac8ff844b0925fa2ff4bbaa35a/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "f494f3ac3c434c8d95ca47b9ee2249a4",
          "image": "https://cdn-images-1.listennotes.com/podcasts/southern-fried-asian-hard-noc-media-uLDlngQ8KaO-lgkR18dcJCv.1400x1400.jpg",
          "title": "Southern Fried Asian",
          "publisher": "Hard NOC Media",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/southern-fried-asian-hard-noc-media-NviZ0GEWh4D-lgkR18dcJCv.300x300.jpg",
          "listen_score": 26,
          "listennotes_url": "https://www.listennotes.com/c/f494f3ac3c434c8d95ca47b9ee2249a4/",
          "listen_score_global_rank": "10%"
        },
        {
          "id": "9fb0fc78f96e4da0a0cc70f5a3abe682",
          "image": "https://cdn-images-1.listennotes.com/podcasts/they-call-us-bruce-jeff-yang-phil-yu-HOjUw8XtCYd-rhMfDYsI1WL.1400x1400.jpg",
          "title": "They Call Us Bruce",
          "publisher": "Jeff Yang & Phil Yu",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/they-call-us-bruce-jeff-yang-phil-yu-baNW6mHrn8p-rhMfDYsI1WL.300x300.jpg",
          "listen_score": 45,
          "listennotes_url": "https://www.listennotes.com/c/9fb0fc78f96e4da0a0cc70f5a3abe682/",
          "listen_score_global_rank": "1.5%"
        }
      ],
      "source_url": "https://www.vanityfair.com/style/2021/04/10-essential-podcasts-from-aapi-creators?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\u201cThese podcasts explore the richness and complexity of Asian American identity, and emphasize how AAPI history is integral to American history.\u201d",
      "pub_date_ms": 1617398605207,
      "source_domain": "www.vanityfair.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/10-essential-podcasts-from-aapi-creators-1hgiRxJF2df/"
    },
    {
      "id": "MqGax2Yitjm",
      "title": "The top 5 best cricket podcasts in the world",
      "total": 5,
      "podcasts": [
        {
          "id": "ab84b2c05ca94bdc94a8137616b55e13",
          "image": "https://cdn-images-1.listennotes.com/podcasts/history-of-cricket-historyofcricket-bD5-_8nYP29.1400x1732.jpg",
          "title": "History of Cricket",
          "publisher": "historyofcricket",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/history-of-cricket-historyofcricket-bD5-_8nYP29.300x371.jpg",
          "listen_score": null,
          "listennotes_url": "https://www.listennotes.com/c/ab84b2c05ca94bdc94a8137616b55e13/",
          "listen_score_global_rank": null
        },
        {
          "id": "60ee54d2878247bc8784e1ffc67934dd",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-cricket-podcast-the-cricket-podcast-LSkw483slFc-9clmYuQAtHe.1400x1400.jpg",
          "title": "The Cricket Podcast",
          "publisher": "The Cricket Podcast",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-cricket-podcast-the-cricket-podcast-yrqZB7RPAIz-9clmYuQAtHe.300x300.jpg",
          "listen_score": 42,
          "listennotes_url": "https://www.listennotes.com/c/60ee54d2878247bc8784e1ffc67934dd/",
          "listen_score_global_rank": "2%"
        },
        {
          "id": "eda5ce39a2b74aa3bc5be344caf76a5a",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-guerilla-cricket-podcast-qHPKS-sE8VI-6ayWIeH7jq-.1400x1400.jpg",
          "title": "The Guerilla Cricket Podcast",
          "publisher": "guerillacricket",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-guerilla-cricket-podcast-yJNPXsEbKAq-6ayWIeH7jq-.300x300.jpg",
          "listen_score": 27,
          "listennotes_url": "https://www.listennotes.com/c/eda5ce39a2b74aa3bc5be344caf76a5a/",
          "listen_score_global_rank": "10%"
        },
        {
          "id": "281a6a27ac524a0b80313d0f130c9da0",
          "image": "https://cdn-images-1.listennotes.com/podcasts/sky-sports-cricket-podcast-sky-sports-OHK-5FVnuTE-TYO_Huy2tIW.1400x1400.jpg",
          "title": "Sky Sports Cricket Podcast",
          "publisher": "Sky Sports",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/sky-sports-cricket-podcast-sky-sports-z64Xsveoyid-TYO_Huy2tIW.300x300.jpg",
          "listen_score": 52,
          "listennotes_url": "https://www.listennotes.com/c/281a6a27ac524a0b80313d0f130c9da0/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "77eb2a154a094f3fb067a51ba71e4137",
          "image": "https://cdn-images-1.listennotes.com/podcasts/oborne-heller-on-cricket-peter-oborne-a52eoUr3HCs-30HrdunGiIg.1400x1400.jpg",
          "title": "Oborne & Heller on Cricket",
          "publisher": "Peter Oborne, Richard Heller",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/oborne-heller-on-cricket-peter-oborne-r10NYHVsKaz-30HrdunGiIg.300x300.jpg",
          "listen_score": 32,
          "listennotes_url": "https://www.listennotes.com/c/77eb2a154a094f3fb067a51ba71e4137/",
          "listen_score_global_rank": "10%"
        }
      ],
      "source_url": "https://lastwordonsports.com/cricket/2021/03/26/the-top-5-best-cricket-podcasts-in-the-world/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"Whether it\u2019s while commuting to work, or while working-out at the gym, podcasts make great company. Unfortunately, with so many of them out there, discerning listeners often have to trawl through a lot of detritus before finding the right podcast for them. So to make life a little easier for cricket fans, here are LWOC\u2019s top 5 best cricket podcasts that we recommend you listen to.\"",
      "pub_date_ms": 1617042737021,
      "source_domain": "lastwordonsports.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/the-top-5-best-cricket-podcasts-in-the-MqGax2Yitjm/"
    },
    {
      "id": "dC84GaX6qks",
      "title": "7 Podcasts Every Book Lover Needs to Listen to",
      "total": 7,
      "podcasts": [
        {
          "id": "0d59171ee75d4669bd8d61c9e61775b5",
          "image": "https://cdn-images-1.listennotes.com/podcasts/bad-on-paper-grace-atwood-becca-freeman-13NpaRW5uyQ-l_4wC7E8sWt.1400x1400.jpg",
          "title": "Bad On Paper",
          "publisher": "Grace Atwood & Becca Freeman",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/bad-on-paper-grace-atwood-becca-freeman-yVws5jtclJk-l_4wC7E8sWt.300x300.jpg",
          "listen_score": 66,
          "listennotes_url": "https://www.listennotes.com/c/0d59171ee75d4669bd8d61c9e61775b5/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "db7a568979d641cc93ace33df63fda29",
          "image": "https://cdn-images-1.listennotes.com/podcasts/reading-women-reading-women-f-boWF7El90-srK1ApOjETJ.1400x1400.jpg",
          "title": "Reading Women",
          "publisher": "Reading Women",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/reading-women-reading-women-A6paCSgTLq5-srK1ApOjETJ.300x300.jpg",
          "listen_score": 53,
          "listennotes_url": "https://www.listennotes.com/c/db7a568979d641cc93ace33df63fda29/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "ff133d1cbf2f4d09b7ecd586b567c576",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-readheads-book-club-toast-news-network-UW68Mu0JlpI-_vVF6a2Xtwe.1400x1400.jpg",
          "title": "The Readheads Book Club",
          "publisher": "Toast News Network",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-readheads-book-club-toast-news-network-4laf5N2iFWu-_vVF6a2Xtwe.300x300.jpg",
          "listen_score": 59,
          "listennotes_url": "https://www.listennotes.com/c/ff133d1cbf2f4d09b7ecd586b567c576/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "21ca662e42104402a598f56239bc93b5",
          "image": "https://cdn-images-1.listennotes.com/podcasts/when-in-romance-book-riot-He905URG_MZ-sIaUCQk5eix.1400x1400.jpg",
          "title": "When In Romance",
          "publisher": "Book Riot",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/when-in-romance-book-riot-ApJ38X0eKIn-sIaUCQk5eix.300x300.jpg",
          "listen_score": 43,
          "listennotes_url": "https://www.listennotes.com/c/21ca662e42104402a598f56239bc93b5/",
          "listen_score_global_rank": "1.5%"
        },
        {
          "id": "a963c831c26846739b3ca5d9fe690b2f",
          "image": "https://cdn-images-1.listennotes.com/podcasts/black-chick-lit-black-chick-lit-JTI-Ps7mUr1-Oc6XbBTArYm.1400x1400.jpg",
          "title": "Black Chick Lit",
          "publisher": "Black Chick Lit",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/black-chick-lit-black-chick-lit-WUtZ96cPihn-Oc6XbBTArYm.300x300.jpg",
          "listen_score": 42,
          "listennotes_url": "https://www.listennotes.com/c/a963c831c26846739b3ca5d9fe690b2f/",
          "listen_score_global_rank": "2%"
        }
      ],
      "source_url": "https://hellogiggles.com/reviews-coverage/books/book-podcasts/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"Dive deep into the literary world through author sit-downs, in-depth character and plot analysis, book news, and of course, plenty of book recommendations. From thrillers to chick lit and YA to non-fiction, we've compiled an amazing list of book-centric podcasts, many of which focus on BIPOC authors and woman-led narratives. Grab your headphones and keep the conversation going with one of the book podcasts below. You may even find your new favorite bookworm!\"",
      "pub_date_ms": 1617042673515,
      "source_domain": "hellogiggles.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/7-podcasts-every-book-lover-needs-to-dC84GaX6qks/"
    },
    {
      "id": "oz8yc61vHlb",
      "title": "TikTok Stars With Podcasts You Should Be Listening To",
      "total": 9,
      "podcasts": [
        {
          "id": "d14b0c419af44c8caa55d973ec7b3916",
          "image": "https://cdn-images-1.listennotes.com/podcasts/charli-and-dixie-2-chix-HjgL5TS2_G--twVGCr7Ilb2.1400x1400.jpg",
          "title": "CHARLI AND DIXIE: 2 CHIX",
          "publisher": "Ramble and Charli and Dixie D\u2019Amelio",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/charli-and-dixie-2-chix-YUw_d-Qx5ZE-twVGCr7Ilb2.300x300.jpg",
          "listen_score": 75,
          "listennotes_url": "https://www.listennotes.com/c/d14b0c419af44c8caa55d973ec7b3916/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "90103917d5c5427a817cfe6d48864436",
          "image": "https://cdn-images-1.listennotes.com/podcasts/besties-from-birth-BmnVCgbo86r-ZCyK9B3t0-l.1400x1400.jpg",
          "title": "Besties from birth",
          "publisher": "Queeny Addison rae",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/besties-from-birth-rSco9hZq08I-ZCyK9B3t0-l.300x300.jpg",
          "listen_score": 41,
          "listennotes_url": "https://www.listennotes.com/c/90103917d5c5427a817cfe6d48864436/",
          "listen_score_global_rank": "2%"
        },
        {
          "id": "bee3a6eeb43d45d482cff16d7e6eec6d",
          "image": "https://cdn-images-1.listennotes.com/podcasts/bffs-WR26UQOXor0-UwCtO6PxIiq.1400x1400.jpg",
          "title": "BFFs featuring Josh Richards and Dave Portnoy",
          "publisher": "Barstool Sports",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/bffs-lvx_8ydqYbn-UwCtO6PxIiq.300x300.jpg",
          "listen_score": 69,
          "listennotes_url": "https://www.listennotes.com/c/bee3a6eeb43d45d482cff16d7e6eec6d/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "af6ffc10c67244028e88ff49c73153df",
          "image": "https://cdn-images-1.listennotes.com/podcasts/capital-university-RyA-ov49bjF-u3NCeTRGi4t.1400x1400.jpg",
          "title": "Capital University ",
          "publisher": "Bryce Hall and Anthony Pompliano ",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/capital-university-d1LyrOnK095-u3NCeTRGi4t.300x300.jpg",
          "listen_score": 78,
          "listennotes_url": "https://www.listennotes.com/c/af6ffc10c67244028e88ff49c73153df/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "8feeaabea4d34d54ae8c8f2aa3b6cb31",
          "image": "https://cdn-images-1.listennotes.com/podcasts/dropouts-zach-justice-lAzoUM5Ja2Y-1puwcqaC5yL.1400x1400.jpg",
          "title": "Dropouts",
          "publisher": "ZACH JUSTICE",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/dropouts-zach-justice-lc_t6mGsH8P-1puwcqaC5yL.300x300.jpg",
          "listen_score": 57,
          "listennotes_url": "https://www.listennotes.com/c/8feeaabea4d34d54ae8c8f2aa3b6cb31/",
          "listen_score_global_rank": "0.5%"
        }
      ],
      "source_url": "https://toofab.com/2021/03/28/tiktok-stars-with-podcasts-you-should-be-listening-to/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"Social media stars from Charli D'Amelio to Bryce Hall are launching their own successful podcasts, each offering a new kind of content to listen to. While Charli and her older sister Dixie dish on mental health and dispel rumors, Bryce focuses on helping influencers better manage their money and investments. Whichever side of TikTok you've ended up on, there's sure to be a podcast to keep you coming back for more!\"",
      "pub_date_ms": 1617042613301,
      "source_domain": "toofab.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/tiktok-stars-with-podcasts-you-should-oz8yc61vHlb/"
    },
    {
      "id": "2rhVUNWXR5z",
      "title": "The Best Rapper Interview Shows",
      "total": 8,
      "podcasts": [
        {
          "id": "0278f6761e444721ba1d7cf7ef7cda9a",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-big-fat-joey-show-radio-podcast-T4BkFrzhcP_-uT2yqpIfrG3.1400x1400.jpg",
          "title": "The Big Fat Joey Show Radio Podcast",
          "publisher": "thebigfatjoeyshow",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-big-fat-joey-show-radio-podcast-QfanI1ylAdR-uT2yqpIfrG3.300x300.jpg",
          "listen_score": null,
          "listennotes_url": "https://www.listennotes.com/c/0278f6761e444721ba1d7cf7ef7cda9a/",
          "listen_score_global_rank": null
        },
        {
          "id": "fd7797f9e47847ccbcb362bd326cbb0b",
          "image": "https://cdn-images-1.listennotes.com/podcasts/deeper-than-rap-rinse-france-F0MxvKUnbB7.1400x1400.jpg",
          "title": "Deeper Than Rap",
          "publisher": "Rinse France",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/deeper-than-rap-rinse-france-F0MxvKUnbB7.300x300.jpg",
          "listen_score": null,
          "listennotes_url": "https://www.listennotes.com/c/fd7797f9e47847ccbcb362bd326cbb0b/",
          "listen_score_global_rank": null
        },
        {
          "id": "e90b57819fd2446a8e4e5e2b8cddcaab",
          "image": "https://cdn-images-1.listennotes.com/podcasts/snoop-doggs-ggn-podcast-snoop-dogg-xwPfbKoIrQR-7KI_Gmsfb6j.1400x1400.jpg",
          "title": "Snoop Dogg's GGN Podcast",
          "publisher": "Snoop Dogg",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/snoop-doggs-ggn-podcast-snoop-dogg-ki3MGbwE6jl-7KI_Gmsfb6j.300x300.jpg",
          "listen_score": 57,
          "listennotes_url": "https://www.listennotes.com/c/e90b57819fd2446a8e4e5e2b8cddcaab/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "fe4b08cdbe6e4d1f84b71fe73840c5d1",
          "image": "https://cdn-images-1.listennotes.com/podcasts/drink-champs-the-black-effect-iheartradio-qh8HnsM2y_U-MHC8wrlqAu7.1400x1400.jpg",
          "title": "Drink Champs",
          "publisher": "The Black Effect & iHeartRadio",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/drink-champs-the-black-effect-iheartradio-6H-Qr0vdNPG-MHC8wrlqAu7.300x300.jpg",
          "listen_score": 69,
          "listennotes_url": "https://www.listennotes.com/c/fe4b08cdbe6e4d1f84b71fe73840c5d1/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "57156f7e27424b978c4084f5316297ee",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-joe-budden-podcast-with-rory-mal-the-7gRaFsf_-Au-nbyOHL4mi02.1400x1400.jpg",
          "title": "The Joe Budden Podcast with Rory & Mal",
          "publisher": "The Joe Budden Network",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-joe-budden-podcast-with-rory-mal-the-_NGdsFEtUK--nbyOHL4mi02.300x300.jpg",
          "listen_score": 64,
          "listennotes_url": "https://www.listennotes.com/c/57156f7e27424b978c4084f5316297ee/",
          "listen_score_global_rank": "0.1%"
        }
      ],
      "source_url": "https://www.complex.com/music/best-rapper-interview-shows/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"Traditional interviews are necessary to get the 5 Ws from artists, but informal conversations are always fun to spectate. We decided to list some of the most talked about-led shows, in no particular order. Huge qualifier: we realize that some of these shows have hosts and sponsors  that are a no-go for many potential listeners, and we considered not mentioning them, but picking and choosing would have created a circumstance where there weren\u2019t even enough shows for a list.\"",
      "pub_date_ms": 1617042257685,
      "source_domain": "www.complex.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/the-best-rapper-interview-shows-2rhVUNWXR5z/"
    },
    {
      "id": "BO289wEJaWn",
      "title": "8 History Podcasts That Will Help You Relearn The World As You Know It",
      "total": 6,
      "podcasts": [
        {
          "id": "0d31d3a6a5bf43fea0de6ad4c99501dd",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-zest-is-history-DWY8m-JqowB-ERLg3sIrj7H.1400x1400.jpg",
          "title": "The Zest Is History",
          "publisher": "Josephine Rozenberg-Clarke and Melissa Mason",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-zest-is-history-Sdyc2RlZ-ge-ERLg3sIrj7H.300x300.jpg",
          "listen_score": 49,
          "listennotes_url": "https://www.listennotes.com/c/0d31d3a6a5bf43fea0de6ad4c99501dd/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "c50bdaa9251f4c44a9344d5dff0d8a4c",
          "image": "https://cdn-images-1.listennotes.com/podcasts/history-is-gay-leigh-gretchen-FkjHBR0TKIl-SNxqeiX0L43.1400x1400.jpg",
          "title": "History is Gay",
          "publisher": "Leigh & Gretchen",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/history-is-gay-leigh-gretchen-Eb2pOq_yu4J-SNxqeiX0L43.300x300.jpg",
          "listen_score": 49,
          "listennotes_url": "https://www.listennotes.com/c/c50bdaa9251f4c44a9344d5dff0d8a4c/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "c6ce7687167c49b69247a50559840e3e",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-history-hour-bbc-world-service-S5OZKtn2pMD.1400x1400.jpg",
          "title": "The History Hour",
          "publisher": "BBC World Service",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-history-hour-bbc-world-service-S5OZKtn2pMD.300x300.jpg",
          "listen_score": 61,
          "listennotes_url": "https://www.listennotes.com/c/c6ce7687167c49b69247a50559840e3e/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "2877905e97474da2850de19eaa9f2461",
          "image": "https://cdn-images-1.listennotes.com/podcasts/conflicted-a-history-podcast-evergreen-sVSOxWJ5UbY-BAVr0k6cCgM.1400x1400.jpg",
          "title": "Conflicted: A History Podcast",
          "publisher": "Evergreen Podcasts",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/conflicted-a-history-podcast-evergreen-rlZuzASIi7y-BAVr0k6cCgM.300x300.jpg",
          "listen_score": 36,
          "listennotes_url": "https://www.listennotes.com/c/2877905e97474da2850de19eaa9f2461/",
          "listen_score_global_rank": "3%"
        },
        {
          "id": "ddd68cefb31c442c9c366229196344c5",
          "image": "https://cdn-images-1.listennotes.com/podcasts/dark-histories-ben-cutmore-o_8K7vbSTnc-0K6WgJdMT3e.1400x1400.jpg",
          "title": "Dark Histories",
          "publisher": "Ben Cutmore",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/dark-histories-ben-cutmore-ZjQhgVbK3RF-0K6WgJdMT3e.300x300.jpg",
          "listen_score": 59,
          "listennotes_url": "https://www.listennotes.com/c/ddd68cefb31c442c9c366229196344c5/",
          "listen_score_global_rank": "0.5%"
        }
      ],
      "source_url": "https://www.theurbanlist.com/a-list/best-history-podcasts?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"History podcasts\u2014they\u2019re juicy, they\u2019re plumpin\u2019 and they\u2019ve got all the tea that will make you light up the front bar the next time you crack open a \u201cdid you know\u201d question at the pub. Whether you\u2019re a self-proclaimed history fiend or you still think the Battle of Waterloo is an ABBA song, these podcasts will guide you to max historical enlightenment harder than the 1700s.\"",
      "pub_date_ms": 1617042012860,
      "source_domain": "www.theurbanlist.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/8-history-podcasts-that-will-help-you-BO289wEJaWn/"
    },
    {
      "id": "wBF-CUqk_j4",
      "title": "The Best Podcasts for Financial Advisors",
      "total": 10,
      "podcasts": [
        {
          "id": "be63ff4aaafd4398934e4988cdbe4bc4",
          "image": "https://cdn-images-1.listennotes.com/podcasts/financial-advisor-success-michael-kitces-K8aWmTRMsU9-RlwSZ7gk2HC.1400x1400.jpg",
          "title": "Financial Advisor Success",
          "publisher": "Michael Kitces",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/financial-advisor-success-michael-kitces-C7D0Ei_JVsM-RlwSZ7gk2HC.300x300.jpg",
          "listen_score": 56,
          "listennotes_url": "https://www.listennotes.com/c/be63ff4aaafd4398934e4988cdbe4bc4/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "00dc12959aa54f4597822f898973d56d",
          "image": "https://cdn-images-1.listennotes.com/podcasts/retirement-answer-man-roger-whitney-cfp-h8RvEcHJdMI.1400x1400.jpg",
          "title": "Retirement Answer Man",
          "publisher": "Roger Whitney, CFP\u00ae, CIMA\u00ae, RMA, CPWA\u00ae, AIF\u00ae",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/retirement-answer-man-roger-whitney-cfp-h8RvEcHJdMI.300x300.jpg",
          "listen_score": 55,
          "listennotes_url": "https://www.listennotes.com/c/00dc12959aa54f4597822f898973d56d/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "b1a899f920c1467288ff2dd70c78d062",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-innovating-advice-show-kate-holmes-pCn7y-H4dvw-VgfZCuxeP0z.1400x1400.jpg",
          "title": "The Innovating Advice Show",
          "publisher": "Kate Holmes",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-innovating-advice-show-kate-holmes-TYIBteiuw-x-VgfZCuxeP0z.300x300.jpg",
          "listen_score": 31,
          "listennotes_url": "https://www.listennotes.com/c/b1a899f920c1467288ff2dd70c78d062/",
          "listen_score_global_rank": "10%"
        },
        {
          "id": "a1df0b7c8feb4022b80743e75a4a524e",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-advisor-lab-seven-group-mN_T8epgIsP-yYsXRmKgE5w.1400x1400.jpg",
          "title": "The Advisor Lab",
          "publisher": "Seven Group",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-advisor-lab-seven-group-lFOe5Ca9ndL-yYsXRmKgE5w.300x300.jpg",
          "listen_score": 28,
          "listennotes_url": "https://www.listennotes.com/c/a1df0b7c8feb4022b80743e75a4a524e/",
          "listen_score_global_rank": "10%"
        },
        {
          "id": "91d4d7eb78b445deae0de04ccca371a8",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-meb-faber-show-meb-faber-aN3xwFX7MbB-JipcPNt6-Io.1400x1400.jpg",
          "title": "The Meb Faber Show",
          "publisher": "Meb Faber",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-meb-faber-show-meb-faber-qaPOLtkg90A-JipcPNt6-Io.300x300.jpg",
          "listen_score": 59,
          "listennotes_url": "https://www.listennotes.com/c/91d4d7eb78b445deae0de04ccca371a8/",
          "listen_score_global_rank": "0.5%"
        }
      ],
      "source_url": "https://news.yahoo.com/best-podcasts-financial-advisors-212709204.html?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"These financial advisor podcasts cover a range of financial topics, including marketing for financial advisors, financial planning strategies and how advisors can build a more diverse financial industry.\"",
      "pub_date_ms": 1616354236524,
      "source_domain": "news.yahoo.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/the-best-podcasts-for-financial-advisors-wBF-CUqk_j4/"
    },
    {
      "id": "R2shy390lxJ",
      "title": "12 Best LGBTQ Podcasts of 2021",
      "total": 6,
      "podcasts": [
        {
          "id": "ae4b075ec70e46009d51ef18a69301ac",
          "image": "https://cdn-images-1.listennotes.com/podcasts/a-gay-and-a-nongay-james-barr-and-dan-hudson-NpnJ9WvVj_y-xgbq6-Nl1XC.1400x1400.jpg",
          "title": "A Gay and A NonGay",
          "publisher": "James Barr and Dan Hudson",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/a-gay-and-a-nongay-james-barr-and-dan-hudson-JObgasNjXSE-xgbq6-Nl1XC.300x300.jpg",
          "listen_score": 55,
          "listennotes_url": "https://www.listennotes.com/c/ae4b075ec70e46009d51ef18a69301ac/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "32211350262343f28eef1a97e859fb82",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-log-books-tash-walker-adam-smith-and-Bf_rtiNve-A-uSOQeIHkV4l.1400x1400.jpg",
          "title": "The Log Books",
          "publisher": "Tash Walker, Adam Zmith and Shivani Dave",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-log-books-tash-walker-adam-smith-and-Ew3gSrIhHWN-uSOQeIHkV4l.300x300.jpg",
          "listen_score": 46,
          "listennotes_url": "https://www.listennotes.com/c/32211350262343f28eef1a97e859fb82/",
          "listen_score_global_rank": "1.5%"
        },
        {
          "id": "989601415cf3428a831349104cc4b717",
          "image": "https://cdn-images-1.listennotes.com/podcasts/busy-being-black-wzard-studios-imaWuyw_5nS-B-S_aHiEVUP.1400x1400.jpg",
          "title": "Busy Being Black",
          "publisher": "W!ZARD Studios",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/busy-being-black-wzard-studios-kMpn8wQVE_y-B-S_aHiEVUP.300x300.jpg",
          "listen_score": 43,
          "listennotes_url": "https://www.listennotes.com/c/989601415cf3428a831349104cc4b717/",
          "listen_score_global_rank": "1.5%"
        },
        {
          "id": "772a2a7636184cee8e042d5612e39fd4",
          "image": "https://cdn-images-1.listennotes.com/podcasts/queer-talk-queertalk-ykibJ2rGz7c-SUcdVt9iR_3.1400x1400.jpg",
          "title": "Queer Talk",
          "publisher": "queertalk",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/queer-talk-queertalk-uFJhezYS6G_-SUcdVt9iR_3.300x300.jpg",
          "listen_score": 33,
          "listennotes_url": "https://www.listennotes.com/c/772a2a7636184cee8e042d5612e39fd4/",
          "listen_score_global_rank": "5%"
        },
        {
          "id": "2fa299aa21f74ae0807a0ecf81589f1d",
          "image": "https://cdn-images-1.listennotes.com/podcasts/two-twos-podcast-two-twos-podcast-Tfih2b6s0F7-Sbrv2k_hKcl.1400x1400.jpg",
          "title": "Two Twos Podcast",
          "publisher": "Two Twos Podcast",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/two-twos-podcast-two-twos-podcast-dtxlPn_S3cq-Sbrv2k_hKcl.300x300.jpg",
          "listen_score": 41,
          "listennotes_url": "https://www.listennotes.com/c/2fa299aa21f74ae0807a0ecf81589f1d/",
          "listen_score_global_rank": "2%"
        }
      ],
      "source_url": "https://www.gaystarnews.com/article/the-best-lgbtq-podcasts-to-binge-in-2021/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"More so recently LGBTQ+ creatives have entered this space and have been giving us some amazing conversations to listen to on our commute homes.\"",
      "pub_date_ms": 1616354145318,
      "source_domain": "www.gaystarnews.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/12-best-lgbtq-podcasts-of-2021-R2shy390lxJ/"
    },
    {
      "id": "qRaVF7IOEuT",
      "title": "7 Podcasts to listen to during Women\u2019s History Month",
      "total": 7,
      "podcasts": [
        {
          "id": "30c2850427c945619fe4c1b7878de32a",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-history-chicks-the-history-chicks-wondery-xRkO7zIaFeK-7O34S1xLdXb.1400x1400.jpg",
          "title": "The History Chicks",
          "publisher": "The History Chicks /Wondery",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-history-chicks-the-history-chicks-wondery-Kmj47R-xLHq-7O34S1xLdXb.300x300.jpg",
          "listen_score": 74,
          "listennotes_url": "https://www.listennotes.com/c/30c2850427c945619fe4c1b7878de32a/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "3284b8ee1de04c2e8a3a9b44e43b92ea",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-profess-hers-podcast-profess-hers-P9b_6wnH5R-.1400x1400.jpg",
          "title": "The Profess-Hers Podcast",
          "publisher": "Profess-Hers",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-profess-hers-podcast-profess-hers-P9b_6wnH5R-.300x300.jpg",
          "listen_score": 36,
          "listennotes_url": "https://www.listennotes.com/c/3284b8ee1de04c2e8a3a9b44e43b92ea/",
          "listen_score_global_rank": "5%"
        },
        {
          "id": "cf2aeef05c8841f5867bce27d7925c33",
          "image": "https://cdn-images-1.listennotes.com/podcasts/whatshername-whatshername-podcast-7E3oZhctvqp.1400x1400.jpg",
          "title": "What'sHerName",
          "publisher": "Dr. Katie Nelson and Olivia Meikle",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/whatshername-whatshername-podcast-7E3oZhctvqp.300x300.jpg",
          "listen_score": 51,
          "listennotes_url": "https://www.listennotes.com/c/cf2aeef05c8841f5867bce27d7925c33/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "c1015b907a474b7ab218c055174f0077",
          "image": "https://cdn-images-1.listennotes.com/podcasts/history-extra-podcast-immediate-media-_aI4LQRlDBk-xPOnjhIz-7b.1400x1400.jpg",
          "title": "History Extra podcast",
          "publisher": "Immediate Media",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/history-extra-podcast-immediate-media-8kmGQ_TXPZo-xPOnjhIz-7b.300x300.jpg",
          "listen_score": 70,
          "listennotes_url": "https://www.listennotes.com/c/c1015b907a474b7ab218c055174f0077/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "32db13b4a6744173afc99a09d44cfc7e",
          "image": "https://cdn-images-1.listennotes.com/podcasts/in-plain-sight-lady-bird-johnson-7QgESwO8zmM-Mlzqr4QfPcm.1400x1400.jpg",
          "title": "In Plain Sight: Lady Bird Johnson",
          "publisher": "ABC News",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/in-plain-sight-lady-bird-johnson-0tOXp6G_wkh-Mlzqr4QfPcm.300x300.jpg",
          "listen_score": 54,
          "listennotes_url": "https://www.listennotes.com/c/32db13b4a6744173afc99a09d44cfc7e/",
          "listen_score_global_rank": "0.5%"
        }
      ],
      "source_url": "https://www.digitaltrends.com/mobile/podcasts-to-listen-to-during-womens-history-month/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"We\u2019ve hand-picked seven of the best podcasts for Women\u2019s History Month \u2014 or any month really \u2014 so settle down with your favorite beverage and get to know these remarkable women, hear their stories, and be inspired by their achievements.\"",
      "pub_date_ms": 1616353961838,
      "source_domain": "www.digitaltrends.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/7-podcasts-to-listen-to-during-womens-qRaVF7IOEuT/"
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
    "image": "https://cdn-images-1.listennotes.com/podcasts/committed-iheartradio-OLW0RiJrQwX-Lvh5Xq29dtK.1400x1400.jpg",
    "title": "Committed",
    "publisher": "iHeartRadio",
    "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/committed-iheartradio-NIrAHbJRduy-Lvh5Xq29dtK.300x300.jpg",
    "listen_score": 62,
    "listennotes_url": "https://www.listennotes.com/c/bc9546c04f7445e48d611112ec6438ca/",
    "listen_score_global_rank": "0.5%"
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
  "image": "https://cdn-images-1.listennotes.com/playlist/image/6907e8ff6b6c45df94cc059753f369cc.JPEG",
  "items": [
    {
      "id": 580202,
      "data": {
        "id": "463b7db874c04c3ca66cefda3e9d4679",
        "link": "http://exponent.fm/episode-194-back-on-spotify/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/463b7db874c04c3ca66cefda3e9d4679/",
        "image": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-Hp-mWcd9xkK-OaJSjb4xQv3.1400x1400.jpg",
        "title": "Episode 194 \u2014 Back on Spotify",
        "podcast": {
          "id": "37589a3e121e40debe4cef3d9638932a",
          "image": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-Hp-mWcd9xkK-OaJSjb4xQv3.1400x1400.jpg",
          "title": "Exponent",
          "publisher": "Ben Thompson / James Allworth",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-dB9NRYQvLw7-OaJSjb4xQv3.300x300.jpg",
          "listen_score": 61,
          "listennotes_url": "https://www.listennotes.com/c/37589a3e121e40debe4cef3d9638932a/",
          "listen_score_global_rank": "0.5%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-dB9NRYQvLw7-OaJSjb4xQv3.300x300.jpg",
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
        "link": "https://bloomberg.com/podcasts/advantage?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/5810e500db4c472aa03a6a5685bf8fbd/",
        "image": "https://cdn-images-1.listennotes.com/podcasts/bloomberg-businessweek-bloomberg-radio-Ft6c9ksGVJ_-yn5Mm7jSGBe.1400x1400.jpg",
        "title": "Spotify Betting Big on Podcasts",
        "podcast": {
          "id": "10954ad3114841e18abad343b3a9156f",
          "image": "https://cdn-images-1.listennotes.com/podcasts/bloomberg-businessweek-bloomberg-radio-Ft6c9ksGVJ_-yn5Mm7jSGBe.1400x1400.jpg",
          "title": "Bloomberg Businessweek",
          "publisher": "Bloomberg Radio",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/bloomberg-businessweek-bloomberg-radio-hOqQSF4gxpa-yn5Mm7jSGBe.300x300.jpg",
          "listen_score": 49,
          "listennotes_url": "https://www.listennotes.com/c/10954ad3114841e18abad343b3a9156f/",
          "listen_score_global_rank": "1%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/bloomberg-businessweek-bloomberg-radio-hOqQSF4gxpa-yn5Mm7jSGBe.300x300.jpg",
        "description": "<p>Dr. Sandro Galea, Dean of Boston University School of Public Health, provides a coronavirus and vaccine update. Bloomberg Businessweek Editor Joel Weber and Bloomberg News Entertainment Reporter Lucas Shaw talk about Spotify betting big on podcasts as a path to profitability. Bloomberg News Cybersecurity Reporter William Turton discusses the article \u201c\u2018No Regrets\u2019: A Capitol Rioter Tells His Story From Inside.\u201d And we Drive to the Close with Yana Barton, Co-Director of Growth Equity at Eaton Vance.</p><p>Hosts: Carol Massar and Tim Stenovec. Producer: Doni Holloway.</p>",
        "pub_date_ms": 1610574796060,
        "guid_from_rss": "d670bee0-5522-11eb-9cc8-8730cc4cbee6",
        "listennotes_url": "https://www.listennotes.com/e/5810e500db4c472aa03a6a5685bf8fbd/",
        "audio_length_sec": 2207,
        "explicit_content": false,
        "maybe_audio_invalid": false,
        "listennotes_edit_url": "https://www.listennotes.com/e/5810e500db4c472aa03a6a5685bf8fbd/#edit"
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/the-james-altucher/side-hustle-friday-monetize-LncxE9KjCgt-jDmTs6Nl-tr.1400x1400.jpg",
        "title": "Side Hustle Friday: Why should you START a podcast and MONETIZE your podcast through Ads and Patreon!",
        "podcast": {
          "id": "6dabf2f65c384e1f897bb606859309f4",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-james-altucher-show-james-altucher-ydcMlwOz5W7-sSHocv8YjIe.1400x1400.jpg",
          "title": "The James Altucher Show",
          "publisher": "James Altucher",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-james-altucher-show-james-altucher-Hnzt-457Amb-sSHocv8YjIe.300x300.jpg",
          "listen_score": 67,
          "listennotes_url": "https://www.listennotes.com/c/6dabf2f65c384e1f897bb606859309f4/",
          "listen_score_global_rank": "0.05%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-james-altucher/side-hustle-friday-monetize-qtbDBvrK5Ii-jDmTs6Nl-tr.300x300.jpg",
        "description": "<p>Another Side Hustle Friday! I sat down with Jay Yow, the Sound Engineer/ Producer of The James Altucher, to discuss ways to monetize a podcast, we spoke about why this is the best time to launch a podcast and our equipment set up for remote recording and interview. In this episode, we break down that's the different ways you can monetize through Ads, sponsors, affiliate deals, and Patreon! Part 2 will be coming soon Monday!</p>\n<hr>\n<p><strong>I write about all my podcasts! Check out the full post and learn what I learned at&nbsp;<a href=\"https://www.jamesaltucher.com/podcast\">jamesaltucher.com/podcast</a>.</strong></p>\n<p><strong>Thanks so much for listening! If you like this episode, please subscribe to &ldquo;The James Altucher Show&rdquo; and rate and review wherever you get your podcasts:</strong></p>\n<p><a href=\"https://itunes.apple.com/us/podcast/the-james-altucher-show/id794030859?mt=2\">Apple Podcasts</a></p>\n<p><a href=\"https://www.stitcher.com/podcast/stansberry-radio-network/the-james-altucher-show/e/52735033\">Stitcher</a></p>\n<p><a href=\"https://www.iheart.com/podcast/232-The-James-Altucher-Show-27085086/episode/ep-298-ryan-holiday-competition-28789411/\">iHeart Radio</a></p>\n<p><a href=\"https://open.spotify.com/episode/0ABi9w3Qrb2EFNDeeXlHyz\">Spotify</a></p>\n<p>&nbsp;</p>\n<p><strong>Follow me on Social Media:</strong></p>\n<p><a href=\"https://www.youtube.com/channel/UCRQlx2klE_aNrPhz2OyKRdg\">YouTube</a></p>\n<p><a href=\"https://twitter.com/jaltucher\">Twitter</a></p>\n<p><a href=\"https://www.facebook.com/JAltucher.Blog/\">Facebook</a></p>\n<p><a href=\"https://www.linkedin.com/in/jamesaltucher\">Linkedin</a></p><p>See <a href=\"https://omnystudio.com/listener\">omnystudio.com/listener</a> for privacy information.</p>",
        "pub_date_ms": 1602831600085,
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/the-james-altucher/side-hustle-friday-monetize-OBljDR14EC3-vZt0gi5hoDN.1400x1400.jpg",
        "title": "Side Hustle Friday: Monetize your podcast right now!",
        "podcast": {
          "id": "6dabf2f65c384e1f897bb606859309f4",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-james-altucher-show-james-altucher-ydcMlwOz5W7-sSHocv8YjIe.1400x1400.jpg",
          "title": "The James Altucher Show",
          "publisher": "James Altucher",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-james-altucher-show-james-altucher-Hnzt-457Amb-sSHocv8YjIe.300x300.jpg",
          "listen_score": 67,
          "listennotes_url": "https://www.listennotes.com/c/6dabf2f65c384e1f897bb606859309f4/",
          "listen_score_global_rank": "0.05%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-james-altucher/side-hustle-friday-monetize-i4IhCZMzQTl-vZt0gi5hoDN.300x300.jpg",
        "description": "<p>Part 2 on monetizing your podcast! In this episode, we talked about ways to monetize your podcast via merchandising, getting hired as a consultant through your podcast, speaking gigs, on and on! Also, enjoy Jay's episodic debut on the podcast! (Technically a second since this is a part of Friday's podcast!)</p>\n<hr>\n<p><strong>I write about all my podcasts! Check out the full post and learn what I learned at&nbsp;<a href=\"https://www.jamesaltucher.com/podcast\">jamesaltucher.com/podcast</a>.</strong></p>\n<p><strong>Thanks so much for listening! If you like this episode, please subscribe to &ldquo;The James Altucher Show&rdquo; and rate and review wherever you get your podcasts:</strong></p>\n<p><a href=\"https://itunes.apple.com/us/podcast/the-james-altucher-show/id794030859?mt=2\">Apple Podcasts</a></p>\n<p><a href=\"https://www.stitcher.com/podcast/stansberry-radio-network/the-james-altucher-show/e/52735033\">Stitcher</a></p>\n<p><a href=\"https://www.iheart.com/podcast/232-The-James-Altucher-Show-27085086/episode/ep-298-ryan-holiday-competition-28789411/\">iHeart Radio</a></p>\n<p><a href=\"https://open.spotify.com/episode/0ABi9w3Qrb2EFNDeeXlHyz\">Spotify</a></p>\n<p>&nbsp;</p>\n<p><strong>Follow me on Social Media:</strong></p>\n<p><a href=\"https://www.youtube.com/channel/UCRQlx2klE_aNrPhz2OyKRdg\">YouTube</a></p>\n<p><a href=\"https://twitter.com/jaltucher\">Twitter</a></p>\n<p><a href=\"https://www.facebook.com/JAltucher.Blog/\">Facebook</a></p>\n<p><a href=\"https://www.linkedin.com/in/jamesaltucher\">Linkedin</a></p><p>See <a href=\"https://omnystudio.com/listener\">omnystudio.com/listener</a> for privacy information.</p>",
        "pub_date_ms": 1603090800083,
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-rMEoeGBJqt1-EKckR36zrnA.1400x1400.jpg",
        "title": "E1096: Podcasting State of the Union featuring Overcast\u2019s Marco Arment & Oxford Road\u2019s Dan Granger",
        "podcast": {
          "id": "9a62e2581908415185dee35d2d19f9b5",
          "image": "https://cdn-images-1.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-rMEoeGBJqt1-EKckR36zrnA.1400x1400.jpg",
          "title": "This Week in Startups",
          "publisher": "Jason Calacanis",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-txh7pAS-Xsy-EKckR36zrnA.300x300.jpg",
          "listen_score": 62,
          "listennotes_url": "https://www.listennotes.com/c/9a62e2581908415185dee35d2d19f9b5/",
          "listen_score_global_rank": "0.5%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-txh7pAS-Xsy-EKckR36zrnA.300x300.jpg",
        "description": "<p>The post <a rel=\"nofollow\" href=\"https://thisweekinstartups.com/e1096-podcasting-state-of-the-union-featuring-overcasts-marco-arment-oxford-roads-dan-granger/\">E1096: Podcasting State of the Union featuring Overcast\u2019s Marco Arment & Oxford Road\u2019s Dan Granger</a> appeared first on <a rel=\"nofollow\" href=\"https://thisweekinstartups.com\">This Week In Startups</a>.</p><img src=\"http://feeds.feedburner.com/~r/twist-audio/~4/mpdJUZ2omI0\" height=\"1\" width=\"1\" alt=\"\"/>",
        "pub_date_ms": 1597416466000,
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/rise-of-the-young-casey-adams-v_hFQlZeGx2-YuarHs5lfDI.1400x1400.jpg",
        "title": "Elise Hu - Hosting \"TED Talks Daily\" & The Future of Podcasting",
        "podcast": {
          "id": "11362a0682e744b29ce5ea73c920132e",
          "image": "https://cdn-images-1.listennotes.com/podcasts/rise-of-the-young-casey-adams-v_hFQlZeGx2-YuarHs5lfDI.1400x1400.jpg",
          "title": "Rise of The Young",
          "publisher": "Casey Adams",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/rise-of-the-young-casey-adams-VrKjhGOgkuf-YuarHs5lfDI.300x300.jpg",
          "listen_score": 55,
          "listennotes_url": "https://www.listennotes.com/c/11362a0682e744b29ce5ea73c920132e/",
          "listen_score_global_rank": "0.5%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/rise-of-the-young-casey-adams-VrKjhGOgkuf-YuarHs5lfDI.300x300.jpg",
        "description": "<p>Elise Hu is a host-at-large based at NPR West in Culver City, Calif. Previously, she explored the future with her video series, <a href=\"https://www.npr.org/2019/05/06/716414780/videos-future-you\"><em>Future You with Elise Hu</em></a>, and served as the founding bureau chief and International Correspondent for NPR's Seoul office. She was based in Seoul for nearly four years, responsible for the network's coverage of both Koreas and Japan, and filed from a dozen countries across Asia. Before joining NPR, she was one of the founding reporters at <a href=\"http://www.texastribune.org/\">The Texas Tribune</a>, a non-profit digital news startup devoted to politics and public policy. While at the Tribune, Hu oversaw television partnerships and multimedia projects, contributed to <em>The New York Times</em>' expanded Texas coverage, and pushed for editorial innovation across platforms.Her work at NPR has earned a DuPont-Columbia award and a Gracie Award from the Alliance for Women in Media for her video series, <em>Elise Tries</em>. Her previous work has earned a Gannett Foundation Award for Innovation in Watchdog Journalism, a National Edward R. Murrow award for best online video, and beat reporting awards from the Texas Associated Press. <em>The Austin Chronicle</em> once dubiously named her the \"<a href=\"http://www.austinchronicle.com/gyrobase/Awards/BestOfAustin?Award=660138\">Best TV Reporter Who Can Write</a>.\"</p>\n<p>Follow Elise Hu on Instagram: <a href=\"https://www.instagram.com/elisewho/?hl=en\">https://www.instagram.com/elisewho/?hl=en</a></p>\n<p>Learn more about Elise Hu: <a href=\"https://elisehu.com/\">https://elisehu.com/</a></p>\n<p>Listen to \"TED Talks Daily\" <a href=\"https://podcasts.apple.com/us/podcast/ted-talks-daily/id160904630\">https://podcasts.apple.com/us/podcast/ted-talks-daily/id160904630</a></p>",
        "pub_date_ms": 1586266731082,
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/the-feed-the/167-cleanfeed-with-a-side-of-_HxANWiUlRk-OS-PBaQKcgl.1400x1400.jpg",
        "title": "167 Cleanfeed With A Side of Google Podcasts",
        "podcast": {
          "id": "ce3754058c7a44a0abd574f86ff5c719",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-feed-the-official-libsyn-podcast-elsie-vpSizOJdtuG-2kOexVdGJIv.1400x1400.jpg",
          "title": "The Feed The Official Libsyn Podcast",
          "publisher": "Elsie Escobar and Rob Walch",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-feed-the-official-libsyn-podcast-elsie-1gCfKIP5XVy-2kOexVdGJIv.300x300.jpg",
          "listen_score": 45,
          "listennotes_url": "https://www.listennotes.com/c/ce3754058c7a44a0abd574f86ff5c719/",
          "listen_score_global_rank": "1.5%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-feed-the/167-cleanfeed-with-a-side-of-KEMJ65zVY4x-OS-PBaQKcgl.300x300.jpg",
        "description": "<p>Tons of details on all things Google Podcasts Manager! It\u2019s like Apple Podcasts connect but of course Google. Then, we move on to jobs in podcasting, so much about feedback about Cleanfeed, some very interesting Facebook updates, Libsyn player automation, what if someone uses YOUR podcast name, a massive breakdown of the podfader types and of course we\u2019ve got a crazy amount of stats!</p> <p>Audience feedback drives the show. We\u2019d love for you to email us and keep the conversation going! Email thefeed@libsyn.com or call 412\u2013573\u20131934. We\u2019d love to hear from you!</p> Quick Episode Summary <ul> <li><em>:07</em> Intro!</li> <li><em>3:04 PROMO 1: Sailing in the Mediterranean and Beyond</em></li> <li><em>3:34</em> Rob and Elsie conversation</li> <li>Announcement of Google Podcasts Manager!</li> <li>What it is, what it gives you and how it it different than Apple Podcasts analytics</li> <li>9:46 Apple is hiring for all kinds of podcasting positions</li> <li>13:56 Cleanfeed audio feedback from Carey Green</li> <li>Emails about Cleanfeed</li> <li>18:08 Cleanfeed audio feedback from CG</li> <li>Thoughts and processes about remote recording</li> <li>There\u2019s a new kid in town</li> <li>27:35 Facebook updates about charging for online events and listening to Faceboook Lives</li> <li>30:58 PROMO 2: The Naturist Living Show</li> <li>New version of Podcast Addict now with reviews</li> <li>Custom automation for the libsyn players</li> <li>Face ID and masks</li> <li>39:55 What if someone is using the name of your show? How do you go about dealing with it?</li> <li>A show appearing twice on some apps</li> <li>49:43 Podfading - the key main groups</li> <li>UK data from Rajar on internet delivery audio services via Neil!</li> <li>57:38 PROMO 3: The Europe Desk</li> <li>Stats, stats, stats: mean and median</li> <li>59:52 COVID\u201319 libsyn stats</li> <li>Where have we been?</li> <li>Where are we going?</li> </ul> Featured Podcast Promos + Audio <ul> <li><a href=\"https://www.medsailor.com/\">PROMO 1: Sailing in the Mediterranean and Beyond</a></li> <li><a href=\"https://www.naturistlivingshow.com/\">PROMO 2: The Naturist Living Show</a></li> <li><a href=\"https://cges.georgetown.edu/research/podcast/\">PROMO 3: The Europe Desk</a></li> <li><a href=\"https://podcastfasttrack.com/\">Carey Green from Podcast Fast Track</a></li> <li><a href=\"https://www.therocketryshow.com/\">CB from the Rocketry Show</a></li> </ul> <p>Thank you to Nick from <a href= \"http://micme.com\">MicMe</a> for our awesome intro!</p>  <p><em>Podcasting Articles and Links mentioned by Rob and Elsie</em></p> <ul> <li><a href=\"http://speakpipe.com/thefeed\">Our SpeakPipe Feedback page!</a> Leave us feedback :)</li> <li><a href=\"http://podcastsmanager.google.com\">Google Podcasts Podcast Manager</a></li> <li><a href=\"https://podcasts.google.com/manager/about\">Google Podcasts Manager About Page</a></li> <li><a href= \"https://support.google.com/podcast-publishers/answer/9479755?hl=en&ref_topic=9476973&authuser=0\"> Adding new and existing podcasts</a></li> <li><a href=\"https://search.google.com/devtools/podcast/preview\">Is your show already in Google Podcasts? Check here</a></li> <li><a href= \"https://support.google.com/podcast-publishers/answer/9696727?hl=en&ref_topic=9476973&authuser=0\"> Manage users and permissions on Google Podcasts Manager</a></li> <li><a href= \"https://support.google.com/podcast-publishers?hl=en&authuser=0#topic=9476973\"> Google Podcasts Manager Support</a></li> <li><a href= \"https://jobs.apple.com/en-us/details/200164774/podcasts-operations-manager?team=MKTG\"> Podcasts Operations Manager</a></li> <li><a href= \"https://jobs.apple.com/en-us/details/200164287/program-manager-podcasts-apple-media-products?team=SFTWR\"> Program Manager, Podcasts, Apple Media Products</a></li> <li><a href= \"https://jobs.apple.com/en-us/details/200164774/podcasts-operations-manager?team=MKTG\"> UI Engineer, Apple Media Products (Podcasts)</a></li> <li><a href=\"https://youtu.be/DpRHSmJT_Vk\">Carey\u2019s Cleanfeed demo video</a></li> <li><a href= \"http://podcastification.com/in-search-of-the-best-way-to-record-an-interview-with-mark-hills-of-cleanfeed-ep-69\"> Carey\u2019s interview with Mark from Cleanfeed</a></li> <li><a href= \"https://podcastengineeringschool.com/marc-bakos-of-cleanfeed-pes-104/\"> Chris Curran\u2019s interview with Marc from Cleanfeed</a></li> <li><a href= \"https://www.reddit.com/r/podcasting/comments/flw9ae/services_and_applications_to_allow_remote/\"> Services and applications to allow remote recordings of remote guests and co-hosts. - Reddit</a></li> <li><a href=\"http://podcast411.com/mixer.pdf\">Rob\u2019s PDF</a></li> <li><a href= \"https://resonaterecordings.com/2020/04/voice-recorder\">Resonate Recordings new recorder</a></li> <li><a href= \"https://about.fb.com/news/2020/04/introducing-messenger-rooms/\">Facebook news</a></li> <li><a href= \"https://www.rajar.co.uk/docs/news/MIDAS_Spring_2020.pdf\">Rajar data for Measurement of Internet Delivery Audio Services</a></li> <li><a href= \"https://twitter.com/search?q=podcast411%20%23cmworld&src=typed_query&f=live\"> Rob\u2019s #CMWorld twitter chat</a></li> <li><a href= \"https://jacobsmedia.com/there-are-over-a-million-podcasts-in-apples-podcasts-app-what-does-it-mean/\"> There Are Over A Million Podcasts In Apple\u2019s Podcasts App, What Does It Mean?</a></li> <li><a href= \"http://www.insideradio.com/podcastnewsdaily/walch-podcast-downloads-aren-t-down-as-much-as-mobility-showing-medium-s-stickiness/article_394e057a-84ba-11ea-a6d0-a3defc713949.html\"> Walch: Proof Of Podcast \u2018Stickiness.\u2019</a></li> </ul>  <em>HELP US SPREAD THE WORD!</em> <p><em>We\u2019d love it if you could please share #TheFeed with your twitter followers. <a href= \"http://clicktotweet.com/9d2te\">Click here to post a tweet!</a></em></p> <p><em>If you dug this episode head on over to Apple Podcasts and kindly <a href= \"https://itunes.apple.com/us/podcast/feed-official-libsyn-podcast/id668413144\"> leave us a rating, a review and subscribe!</a></em></p> <em>Ways to subscribe to The Feed: The Official Libsyn Podcast</em> <ul> <li><em><a href= \"https://itunes.apple.com/us/podcast/feed-official-libsyn-podcast/id668413144\"> Click here to subscribe via Apple Podcasts</a></em></li> <li><em><a href=\"http://thefeed.libsyn.com/rss\">Click here to subscribe via RSS</a></em></li> <li><em><a href= \"http://www.stitcher.com/podcast/libsyn/the-feed\">You can also subscribe via Stitcher</a></em></li> </ul> FEEDBACK + PROMOTION <p><em>You can ask your questions, make comments and create a segment about podcasting for podcasters! Let your voice be heard.</em></p> <ul> <li>Download the FREE The Feed App for <a href= \"https://itunes.apple.com/us/app/the-feed-podcasting-tips-from-libsyn/id381787434?mt=8\"> iOS</a> and <a href= \"https://play.google.com/store/apps/details?id=com.libsyn.android.thefeed&hl=en\"> Android</a> (you can send feedback straight from within the app)</li> <li>Call 412 573 1934</li> <li>Email thefeed@libsyn.com</li> <li>Use our <a href=\"http://speakpipe.com/thefeed\">SpeakPipe Page</a>!</li> </ul>",
        "pub_date_ms": 1588694700014,
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/marketing-school-digital-marketing-and-K_0qXgISwbM-pHyiIJT4Lxl.1400x1400.jpg",
        "title": "Spotify Acquired 'The Ringer' Podcast ($15M In Revenues) - Here's What It Means  | Ep. #1306",
        "podcast": {
          "id": "9a2abf6b68b54554a60a32a2932febcb",
          "image": "https://cdn-images-1.listennotes.com/podcasts/marketing-school-digital-marketing-and-K_0qXgISwbM-pHyiIJT4Lxl.1400x1400.jpg",
          "title": "Marketing School - Digital Marketing and Online Marketing Tips",
          "publisher": "Eric Siu & Neil Patel",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/marketing-school-digital-marketing-and-0NEIcZxdOo5-pHyiIJT4Lxl.300x300.jpg",
          "listen_score": 64,
          "listennotes_url": "https://www.listennotes.com/c/9a2abf6b68b54554a60a32a2932febcb/",
          "listen_score_global_rank": "0.1%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/marketing-school-digital-marketing-and-0NEIcZxdOo5-pHyiIJT4Lxl.300x300.jpg",
        "description": "<p>In episode #1306, we discuss Spotify\u2019s acquisition of The Ringer. The podcasting industry is growing exponentially and Spotify wanted to make an aggressive move toward growing its market share. Tune in to hear why this was a super smart decision on their part!</p> <p>TIME-STAMPED SHOW NOTES:</p> <ul> <li>[00:25] Today\u2019s topic: How Spotify Acquired The Ringer.\u00a0\u00a0</li> <li>[00:42] The solid financial results for Spotify in Q4 of 2019.</li> <li>[00:56] How Spotify recognized exponential growth in podcast hours streamed.</li> <li>[01:24] Realizing that they needed to acquire a big podcast to double down on opportunities.\u00a0\u00a0\u00a0</li> <li>[01:53] The impressive retention rates of the Marketing School podcast.</li> <li>[02:09] Why Spotify\u2019s decision makes a lot of sense.\u00a0</li> <li>[02:39] Keep in mind that all good channels eventually become crowded.\u00a0\u00a0</li> <li>[03:09] Spotify\u2019s market share around podcasting and how they\u2019re more aggressive than Apple.\u00a0</li> <li>[03:48] The number of downloads The Ringer podcast is getting.\u00a0</li> <li>[04:07] Start comparing your Apple Podcast and Spotify analytics for your podcast.\u00a0</li> <li>[04:50] How our podcasts and Eric\u2019s own podcast are performing.\u00a0\u00a0</li> <li>[05:56] The proposed price for The Ringer stated by Bill Simmons: $100 million.\u00a0</li> <li>[06:25] That\u2019s it for today!</li> <li>[06:26] To stay updated with events and learn more about our mastermind, go to the <a href= \"https://marketingschool.io/growth-accelerator-mastermind\"> Marketing School</a> site for more information.</li> </ul> <p>Links Mentioned in Today\u2019s Episode:</p> <ul> <li><a href=\"https://www.spotify.com/\">Spotify</a>\u00a0</li> <li><a href=\"https://www.theringer.com\">The Ringer</a></li> <li><a href=\"https://www.apple.com\">Apple</a></li> <li><a href= \"https://growtheverywhere.com/podcast-player/\">Leveling Up Podcast</a></li> <li><a href=\"https://twitter.com/BillSimmons?ref_src\">Bill Simmons on Twitter</a></li> </ul> <p>Leave Some Feedback:</p> <p>\u00a0</p> <ul> <li>What should we talk about next?\u00a0Please let us know in the comments below</li> </ul> <ul> <li>Did you enjoy this episode?\u00a0If so, please leave a short review.</li> </ul> <p>\u00a0</p> <p>Connect with Us:\u00a0</p> <ul> <li style=\"font-weight: 400;\"><a href= \"http://neilpatel.com\">Neilpatel.com</a></li> <li style=\"font-weight: 400;\"><a href= \"https://www.quicksprout.com/\">Quick Sprout</a>\u00a0</li> <li style=\"font-weight: 400;\"><a href= \"https://growtheverywhere.com/\">Growth Everywhere</a></li> <li style=\"font-weight: 400;\"><a href= \"https://www.singlegrain.com/\">Single Grain</a></li> <li style=\"font-weight: 400;\"><a href= \"https://twitter.com/neilpatel\">Twitter @neilpatel</a>\u00a0</li> <li style=\"font-weight: 400;\"><a href= \"https://twitter.com/ericosiu\">Twitter @ericosiu</a></li> </ul>",
        "pub_date_ms": 1582812000350,
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/recode-media-recode-BZlna1CAThx-1iPwTajLXlS.1400x1400.jpg",
        "title": "Spotify, The Ringer and the future of podcasts",
        "podcast": {
          "id": "2aba49dc3fc04e3e96fe89f79a261798",
          "image": "https://cdn-images-1.listennotes.com/podcasts/recode-media-recode-BZlna1CAThx-1iPwTajLXlS.1400x1400.jpg",
          "title": "Recode Media",
          "publisher": "Recode",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/recode-media-recode-UXOHc-3mo_8-1iPwTajLXlS.300x300.jpg",
          "listen_score": 54,
          "listennotes_url": "https://www.listennotes.com/c/2aba49dc3fc04e3e96fe89f79a261798/",
          "listen_score_global_rank": "0.5%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/recode-media-recode-UXOHc-3mo_8-1iPwTajLXlS.300x300.jpg",
        "description": "<p>Spotify is buying Bill Simmons\u2019 sports and pop culture website and podcast network, The Ringer. It\u2019s Spotify\u2019s fourth podcast acquisition in a year. Recode\u2019s Peter Kafka (who broke the story) sits down with Vox Media Podcast Network producer and former Ringer staff member Zach Mack to discuss what this deal means for Spotify, The Ringer and the future of podcasts.</p><p><br></p><p><strong>Featuring</strong>: Zach Mack (<a href=\"https://twitter.com/zachthemack\">@zachthemack</a>), Senior Podcast Producer at Vox Media Podcast Network</p><p><strong>Host</strong>: Peter Kafka\u00a0(<a href=\"https://twitter.com/pkafka\">@pkafka</a>), Senior Editor at Recode</p><p><strong>More to explore</strong>: <a href=\"https://pod.link/1080467174\">Subscribe for free to Recode Media</a>, Peter Kafka, one of the media industry's most acclaimed reporters, talks to business titans, journalists, comedians, and more to get their take on today's media landscape.</p><p><strong>About Recode by Vox</strong>: Recode by Vox helps you understand how tech is changing the world \u2014 and changing us.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://megaphone.fm/adchoices\">megaphone.fm/adchoices</a></p>",
        "pub_date_ms": 1581021870062,
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/a16z-podcast-andreessen-horowitz-sBmS7T_86qH-IWF2alEr-9h.1400x1400.jpg",
        "title": "How We Podcast",
        "podcast": {
          "id": "7c20388d8d7e45d6ae4b770c1fe36b6f",
          "image": "https://cdn-images-1.listennotes.com/podcasts/a16z-podcast-andreessen-horowitz-sBmS7T_86qH-IWF2alEr-9h.1400x1400.jpg",
          "title": "a16z Podcast",
          "publisher": "Andreessen Horowitz",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/a16z-podcast-andreessen-horowitz-3bPEYm06XuR-IWF2alEr-9h.300x300.jpg",
          "listen_score": 62,
          "listennotes_url": "https://www.listennotes.com/c/7c20388d8d7e45d6ae4b770c1fe36b6f/",
          "listen_score_global_rank": "0.5%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/a16z-podcast-andreessen-horowitz-3bPEYm06XuR-IWF2alEr-9h.300x300.jpg",
        "description": "<p>\"Hi everyone, welcome to the a16z Podcast...\" ... and welcome to our 500th episode, where, for the first time, we reveal behind-the-scenes details and the backstory of how we built this show, and the broader editorial operation. [You can also listen to episode 499, with head of marketing Margit Wennmachers, on building the a16z brand, <a href=\"https://a16z.com/2019/11/20/brand-building-a16z-ideas-people-marketing/\" target=\"_blank\">here</a>.]</p><p>We've talked a lot about the podcasting industry, and even done podcasts about podcasting, so for this special episode, editor-in-chief and showrunner Sonal Chokshi reveals the how, what, and why in conversation with a16z general partner (and guest-host for this special episode) <a href=\"https://a16z.com/2019/10/01/knowable-audio-startups/\" target=\"_blank\">podcasting</a> fan Connie Chan. We also answer some frequently asked questions that we often get (and recently <a href=\"https://twitter.com/smc90/status/1198026729421324289\" target=\"_blank\">got</a> via Twitter), such as:</p><ul><li>how we program podcasts</li><li>what's the process, from ideas to publishing</li><li>do we edit them and how!</li><li>do guests prep, do we have a script</li><li>technical stack</li></ul><p>...and much more. In fact, much of the conversation goes beyond the a16z Podcast and towards Sonal's broader principles of 'editorial content marketing', which hopefully helps those thinking about their own content operations and podcasts, too. Including where podcasting may be going.</p><p>Finally, we share some unexpected moments, and lessons learned along the way; our positions on \"tics\", swear-words, and talking too fast; failed experiments, and new directions. But most importantly, we share some of the people behind the scenes who help make the a16z Podcast what it was, is, and can be... with thanks most of all to *you*, our wonderful fans!</p>",
        "pub_date_ms": 1574838000128,
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-hu4HiXUtv3y-kmx0XIZTAys.1400x1400.jpg",
        "title": "*Live* at Spotify - Part II: Why Spotify is doing podcasts \u2014 Our interview with Max Cutler,  Founder & MD of podcasts at Spotify",
        "podcast": {
          "id": "c5ce6c02cbf1486496206829f7d42e8e",
          "image": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-hu4HiXUtv3y-kmx0XIZTAys.1400x1400.jpg",
          "title": "Snacks Daily",
          "publisher": "Robinhood Financial, LLC",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-3qgUaLoWpvA-kmx0XIZTAys.300x300.jpg",
          "listen_score": 72,
          "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
          "listen_score_global_rank": "0.05%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-3qgUaLoWpvA-kmx0XIZTAys.300x300.jpg",
        "description": "<p>The 2nd half of our Snacks recording live from Spotify. We sit down with Max Cutler, the Founder &amp; MD of Parcast Studios at Spotify \u2014 his startup was acquired by Spotify earlier this year. We\u2019re asking about how he first pitched his company, whether podcasts will follow the Netflix strategy, and what his favorite pod is. Ever.</p><p><br></p><p><br></p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
        "pub_date_ms": 1574852400329,
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-hu4HiXUtv3y-kmx0XIZTAys.1400x1400.jpg",
        "title": "*Live* at Spotify - Part I: How we build this (every day)",
        "podcast": {
          "id": "c5ce6c02cbf1486496206829f7d42e8e",
          "image": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-hu4HiXUtv3y-kmx0XIZTAys.1400x1400.jpg",
          "title": "Snacks Daily",
          "publisher": "Robinhood Financial, LLC",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-3qgUaLoWpvA-kmx0XIZTAys.300x300.jpg",
          "listen_score": 72,
          "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
          "listen_score_global_rank": "0.05%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/snacks-daily-robinhood-financial-llc-3qgUaLoWpvA-kmx0XIZTAys.300x300.jpg",
        "description": "<p>Spotify invited us to their NYC offices to record a live podcast \u2014 it\u2019s a podcast about podcasts for our podcast listening Snackers. We introduce to the Snackers how we got into podcasting, how we built this podcast (every day), and the 5 ingredients for a podcast that people will actually listen to.\u00a0</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
        "pub_date_ms": 1574420400332,
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/product-hunt-radio-product-hunt-GWVKjh-0kgs-4qPNklrZI93.1400x1400.jpg",
        "title": "The future of podcasting with Andrew Mason",
        "podcast": {
          "id": "40426582e3cd4dd2bf931f880e7374aa",
          "image": "https://cdn-images-1.listennotes.com/podcasts/product-hunt-radio-product-hunt-GWVKjh-0kgs-4qPNklrZI93.1400x1400.jpg",
          "title": "Product Hunt Radio",
          "publisher": "Product Hunt",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/product-hunt-radio-product-hunt--QOpzec69YV-4qPNklrZI93.300x300.jpg",
          "listen_score": 46,
          "listennotes_url": "https://www.listennotes.com/c/40426582e3cd4dd2bf931f880e7374aa/",
          "listen_score_global_rank": "1%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/product-hunt-radio-product-hunt--QOpzec69YV-4qPNklrZI93.300x300.jpg",
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/demandgen-radio-david-lewis-demandgencom-oVByO3tuFwR.1400x1400.jpg",
        "title": "#129 How to Build your Brand with Podcasting",
        "podcast": {
          "id": "f446a0eaac2e481991e36467e4a4f96f",
          "image": "https://cdn-images-1.listennotes.com/podcasts/demandgen-radio-david-lewis-demandgencom-oVByO3tuFwR.1400x1400.jpg",
          "title": "DemandGen Radio",
          "publisher": "DemandGen International, Inc.",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/demandgen-radio-david-lewis-demandgencom-oVByO3tuFwR.300x300.jpg",
          "listen_score": 36,
          "listennotes_url": "https://www.listennotes.com/c/f446a0eaac2e481991e36467e4a4f96f/",
          "listen_score_global_rank": "3%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/demandgen-radio-david-lewis-demandgencom-oVByO3tuFwR.300x300.jpg",
        "description": "<p></p>\n<p>Jordan Paris is a 21-year-old entrepreneur who runs a wildly successful podcast. In this episode, he shares how and why he started his podcast and how podcasting propelled the growth of his business and personal brand. Tune in as Jordan shares how he remains so driven and accomplished at an early age, what lessons he\u2019s learned from starting his podcast, and how you can benefit from starting your own podcast.</p>",
        "pub_date_ms": 1569146400075,
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/cold-call-hbr-presents-brian-kenny-UepvPhNmMFV-sC2kfX7gM0D.1400x1400.jpg",
        "title": "Can Gimlet Turn a Podcast Network Into a Disruptive Platform?",
        "podcast": {
          "id": "841eca7a25c64420b2bd0b536d35108d",
          "image": "https://cdn-images-1.listennotes.com/podcasts/cold-call-hbr-presents-brian-kenny-UepvPhNmMFV-sC2kfX7gM0D.1400x1400.jpg",
          "title": "Cold Call",
          "publisher": "HBR Presents / Brian Kenny",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/cold-call-hbr-presents-brian-kenny-egRtK2b1Odo-sC2kfX7gM0D.300x300.jpg",
          "listen_score": 48,
          "listennotes_url": "https://www.listennotes.com/c/841eca7a25c64420b2bd0b536d35108d/",
          "listen_score_global_rank": "1%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/cold-call-hbr-presents-brian-kenny-egRtK2b1Odo-sC2kfX7gM0D.300x300.jpg",
        "description": "<p>Harvard Business School professors <strong><a href=\"https://www.hbs.edu/faculty/Pages/profile.aspx?facId=6446\" target=\"_blank\" rel=\"noopener\">John Deighton</a></strong> and <strong><a href=\"https://www.hbs.edu/faculty/Pages/profile.aspx?facId=6536\" target=\"_blank\" rel=\"noopener\">Jeffrey Rayport</a></strong> discuss their case, &#8220;<a href=\"https://store.hbr.org/product/gimlet-media-a-podcasting-startup/918413?sku=918413-PDF-ENG\" target=\"_blank\" rel=\"noopener\">Gimlet Media: A Podcasting Startup</a>,&#8221; and how two former public radio producers launch a podcast network, entering the last frontier of digital media. Can they turn a content supplier into a disruptive platform?</p>",
        "pub_date_ms": 1569948476032,
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
        "image": "https://cdn-images-1.listennotes.com/episode/image/e816164a99cb4339bb248b7218d8c9d5.jpg",
        "title": "The Wild World of Podcast Ads",
        "podcast": {
          "id": "3b7c6c851ec14f40bb062b918942aa15",
          "image": "https://cdn-images-1.listennotes.com/podcasts/function-with-anil-dash-vox-media-3DjNoAIGtV_-pfqIzGD4odn.1400x1400.jpg",
          "title": "Function with Anil Dash",
          "publisher": "Vox Media",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/function-with-anil-dash-vox-media-yYP_8KQFk06-pfqIzGD4odn.300x300.jpg",
          "listen_score": 45,
          "listennotes_url": "https://www.listennotes.com/c/3b7c6c851ec14f40bb062b918942aa15/",
          "listen_score_global_rank": "1.5%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/episode/image/c76197bdbdc4438e85fc13a05637a420.jpg",
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
        "link": "https://chtbl.com/track/65FD73/traffic.libsyn.com/secure/chinatalkshow/CET_July_10_Yang_Yi_Final.mp3?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/89765fa2bee24603a93b4098830c4efa/",
        "image": "https://cdn-images-1.listennotes.com/podcasts/chinatalk/learning-to-listen-chinas-8-wIXsvQgz7-LoO0UAa_G4e.1400x1400.jpg",
        "title": "Learning to listen: China's billion-dollar podcast industry",
        "podcast": {
          "id": "5cd3fe3fc0c04c8da9abf4a6fb897a31",
          "image": "https://cdn-images-1.listennotes.com/podcasts/chinatalk-jordan-schneider-OX3PVhimRly-Jz4DAyqm9ZV.1400x1400.jpg",
          "title": "ChinaTalk",
          "publisher": "Jordan Schneider",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/chinatalk-jordan-schneider-fcvUsS4LrB8-Jz4DAyqm9ZV.300x300.jpg",
          "listen_score": 35,
          "listennotes_url": "https://www.listennotes.com/c/5cd3fe3fc0c04c8da9abf4a6fb897a31/",
          "listen_score_global_rank": "5%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/chinatalk/learning-to-listen-chinas-LvZy8wklndI-LoO0UAa_G4e.300x300.jpg",
        "description": "While it may be a pipe dream for ChinaEconTalk to ever merit a billion-dollar price tag, in China, podcast \u201cunicorns\u201d are everywhere. Companies like Ximalaya and Yudao have multibillion-dollar valuations, but feature startlingly different content from what consumers expect in the West. What drives these differences, and what does the future hold for spoken audio in China? To answer these questions, Yi Yang, a young podcast host and founder of the Mandarin-language podcast startup JustPod \u64ad\u5ba2\u4e00\u4e0b, joins Jordan to explain how, after the advent of podcasts in China, people are finally \u201clearning to listen.\u201d Yi Yang's original podcast is called LeftRight\u00a0\u5ffd\u5de6\u5ffd\u53f3. His two branded podcasts are\u00a0Startup Insider\u00a0\u521b\u4e1a\u5185\u5e55 and Bessie\u2019s Notes\u00a0\u8d1d\u671b\u5f55. ChinaEconTalk's newsletter is dope. Sign up here at\u00a0www.chinaecontalk.substack.com. The latest issues include an analysis of why Amazon lost in China and learn about the bane of China\u2019s automobile industry.",
        "pub_date_ms": 1562795773097,
        "guid_from_rss": "807301962fd14ffdbd8392824f6f1e5f",
        "listennotes_url": "https://www.listennotes.com/e/89765fa2bee24603a93b4098830c4efa/",
        "audio_length_sec": 2910,
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
        "image": "https://cdn-images-1.listennotes.com/episode/image/96fb8e1ea1ba4d69ab5164c6d0499003.jpg",
        "title": "Season 2, Episode 6:\u00a0Spotify\u2019s Direct Listing",
        "podcast": {
          "id": "50d02b7d32b246a5a6b43e3ca1676657",
          "image": "https://cdn-images-1.listennotes.com/podcasts/acquired-ben-gilbert-and-david-rosenthal-N2aQHeuB0CV-9pne_5jCY2u.1400x1400.jpg",
          "title": "Acquired",
          "publisher": "Ben Gilbert and David Rosenthal",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/acquired-ben-gilbert-and-david-rosenthal-27KuhDaUGsL-9pne_5jCY2u.300x300.jpg",
          "listen_score": 61,
          "listennotes_url": "https://www.listennotes.com/c/50d02b7d32b246a5a6b43e3ca1676657/",
          "listen_score_global_rank": "0.5%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/episode/image/6dc6933a8143463a89449a846cfe0c24.jpg",
        "description": "<p>Join the Acquired Limited Partner program! <a href= \"https://kimberlite.fm/acquired/\">https://kimberlite.fm/acquired/</a> (works best on mobile)</p> <p>Acquired wraps up a big few weeks of coverage with not an IPO or an M&A or a fundraising round, but what\u2019s still the largest tech exit in recent memory: Spotify\u2019s $30B direct public listing. We dive into what it all means and how we got here: from Napster to iTunes to Facebook (and even some Justin Timberlake thrown in for good measure). Acquired FM is on the scene and spinning all the hits from this new wave music industry titan!\u00a0</p> <p>\u00a0</p> <p><em>Note: We incorrectly described Spotify CEO Daniel Ek\u2019s ownership stake in Spotify as 25%+; that is actually his voting control. His economic ownership is 9.3%, and cofounder Martin Lorentzon\u2019s is 12.4%. We apologize for the error!</em></p> <p>\u00a0</p> <p>Links:</p> <ul> <li><a href= \"http://www.internethistorypodcast.com/2017/04/the-napster-story-with-jordan-ritter/\"> Internet History Podcast on the Napster Story with Jordan Ritter</a></li> <li><a href= \"https://www.scribd.com/doc/67465758/Sean-Parker-s-Email-to-Spotify-s-Daniel-Ek\"> Sean Parker\u2019s email to Daniel Ek</a></li> </ul> <p>\u00a0</p> <p>Carve Outs:</p> <ul> <li>Ben: <a href=\"http://www.imdb.com/title/tt1825683/\">Black Panther</a> (and <a href= \"https://open.spotify.com/user/g0u1d1e1/playlist/4Vaus6GcI1TAMGmepUK3WO\"> soundtrack on Spotify</a>!)</li> <li>David: <a href=\"https://www.sfballet.org/boundless\">\u201cSilicon Ballet\u201d panel at San Francisco Ballet on Saturday, April 28</a></li> </ul> <p>\u00a0</p> <p>Sponsor:</p> <ul> <li>Thanks to <a href=\"https://www.perkinscoie.com/\">Perkins Coie</a>, Counsel to Great Companies, for sponsoring Acquired Season 2. You can get in touch with Lee Schindler, who you heard at the beginning of this podcast, <a href= \"https://www.perkinscoie.com/en/professionals/r-lee-schindler.html\"> here</a>.</li> </ul>",
        "pub_date_ms": 1522992660072,
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/the-vergecast-the-verge-TY5x7SlUdZC-n6zR1v83Ejt.1400x1400.jpg",
        "title": "Spotify\u2019s big audio play, plus a Palm tiny phone review",
        "podcast": {
          "id": "cfeaa7a758a94e069ba087f323ffa225",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-vergecast-the-verge-TY5x7SlUdZC-n6zR1v83Ejt.1400x1400.jpg",
          "title": "The Vergecast",
          "publisher": "The Verge",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-vergecast-the-verge-zv61loVeM2G-n6zR1v83Ejt.300x300.jpg",
          "listen_score": 68,
          "listennotes_url": "https://www.listennotes.com/c/cfeaa7a758a94e069ba087f323ffa225/",
          "listen_score_global_rank": "0.05%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-vergecast-the-verge-zv61loVeM2G-n6zR1v83Ejt.300x300.jpg",
        "description": "<p>Spotify acquires Gimlet Media and Anchor in a play to further expand into audio beyond music streaming. Later, Nilay Patel, Dieter Bohn, and Paul Miller review the tiny new Palm phone, address Samsung Galaxy S10 rumors and finally, some Apple updates.</p><p>Links: </p><p>- <a href=\"https://www.theverge.com/2019/2/6/18213462/spotify-podcasts-gimlet-anchor-acquisition\">Spotify gets serious about podcasts with two acquisitions</p><p></a></p><p>- <a href=\"https://www.theverge.com/circuitbreaker/2019/2/6/18213597/samsung-galaxy-s10e-variant-smaller-screen-leak-name-pictures\">Latest leaks confirm cheaper and smaller Samsung Galaxy S10e</p><p></a></p><p>- <a href=\"https://www.theverge.com/2019/2/4/18210291/samsung-galaxy-s10-wifi-6-leak\">Samsung\u2019s Galaxy S10 will be one of the first Wi-Fi 6 phones</p><p></a></p><p>- <a href=\"https://www.theverge.com/2019/2/6/18213974/samsung-true-wireless-galaxy-buds-earphones-promotional-image-leak\">New Samsung true wireless earbuds appear in leaked promotional \u2026</p><p></a></p><p>- <a href=\"https://www.theverge.com/2019/2/4/18211261/samsung-galaxy-sport-leak-shows-a-sleek-bezel-less-smartwatch\">Samsung Galaxy Sport leak shows a sleek bezel-less smartwatch \u2026</p><p></a></p><p>- <a href=\"https://www.theverge.com/2019/2/6/18212311/palm-phone-review-time-well-spent-life-mode-lite-verizon\">Palm phone review: it won\u2019t save you from your phone</p><p></a></p><p>- <a href=\"https://www.theverge.com/2019/2/7/18203706/apple-ios-12-1-4-group-facetime-security-fix\">Apple releases iOS 12.1.4 to fix Group FaceTime security flaw</p><p></a></p><p>- <a href=\"https://www.theverge.com/2019/2/7/18215885/apple-group-facetime-security-bug-bounty-compensation\">Apple is compensating the 14-year-old who discovered major FaceTime security bug</p><p></a></p><p>- <a href=\"https://www.theverge.com/2019/2/5/18212657/apple-retail-chief-angela-ahrendts-leaving-replacement\">Apple retail chief Angela Ahrendts is leaving in April</p><p></a></p><p>- <a href=\"https://www.theverge.com/2019/2/4/18211044/apple-att-5g-e-network-icon-iphones-misleading-ios-software-update-beta\">Apple just endorsed AT&amp;T\u2019s fake 5G E network</p><p></a></p><p>- <a href=\"https://www.theverge.com/circuitbreaker/2019/2/4/18210866/belkin-ethernet-lightning-dongle-release-date-price-power\">Fine, here\u2019s a $100 Lightning to Ethernet dongle for iPads</p><p></a></p><p>- <a href=\"https://www.theverge.com/2019/2/7/18215639/net-neutrality-congress-hearing-energy-commerce-committee\">Net neutrality takes center stage at congressional hearing</p><p></a></p><p>Check out: <a href=\"http://www.azure.com/trial\">Azure.com/trial</a> to sign up for a trial today!</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://megaphone.fm/adchoices\">megaphone.fm/adchoices</a></p>",
        "pub_date_ms": 1549623600184,
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
    },
    {
      "id": 263791,
      "data": {
        "id": "a211b2041cb649ab9bd0406453a6578b",
        "link": "http://relay.fm/download/90?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/a211b2041cb649ab9bd0406453a6578b/",
        "image": "https://cdn-images-1.listennotes.com/podcasts/download-relay-fm-xUtu3il0ONa.1400x1400.jpg",
        "title": "Download 90: Spotify Buys Podcasting",
        "podcast": {
          "id": "e5e08ad405cf427985346229ea3fb611",
          "image": "https://cdn-images-1.listennotes.com/podcasts/download-relay-fm-xUtu3il0ONa.1400x1400.jpg",
          "title": "Download",
          "publisher": "Relay FM",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/download-relay-fm-xUtu3il0ONa.300x300.jpg",
          "listen_score": 42,
          "listennotes_url": "https://www.listennotes.com/c/e5e08ad405cf427985346229ea3fb611/",
          "listen_score_global_rank": "2%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/download-relay-fm-xUtu3il0ONa.300x300.jpg",
        "description": "<p>Jason and Stephen discuss Apple&#39;s retail changes and Facebook&#39;s 15th anniversary. Then Natalie Jarvey of The Hollywood Reporter visits to discuss Spotify spending a lot of money on podcasting companies, and Jeremy Burge of Emojipedia unveils the new emoji coming later in 2019.</p>\n <h4>This episode of Download is sponsored by:</h4> <ul>\n<li><a href=\"https://linode.com/downloadfm/?utm_source=downloadfm&amp;utm_medium=podcast&amp;utm_content=20%20dollar&amp;utm_campaign=downloadfm20\">Linode</a>: High performance SSD Linux servers for all of your infrastructure needs. Get a $20 credit.</li>\n<li><a href=\"http://burrow.com/download\">Burrow</a>: The Luxury Couch for Real Life. Save $75.</li>\n</ul>\n<h4 style='display: inline;'>Guest Starring:</h4> <p style='display: inline;'><a href='http://www.relay.fm/people/nataliejarvey'>Natalie Jarvey</a> and <a href='http://www.relay.fm/people/jeremyburge'>Jeremy Burge</a></p>\n<h4>Links and Show Notes</h4>  <h5><a rel='payment' href='https://relayfm.memberful.com/checkout?plan=20854'>Support Download with a Relay FM Membership</a></h5> <h5><a href=\"https://www.apple.com/newsroom/2019/02/apple-names-deirdre-obrien-senior-vice-president-of-retail-and-people/\" target=\"_blank\">Apple names Deirdre O\u2019Brien senior vice president of Retail and People - Apple</a></h5> <h5><a href=\"https://www.vox.com/technology/2019/2/4/18205138/facebook-15-anniversary-social-network-founded-date-2004\" target=\"_blank\">Facebook 15th anniversary: Has Facebook been good or bad for the world? - Vox</a></h5> <h5><a href=\"https://daringfireball.net/linked/2019/02/06/ahrendts-london\" target=\"_blank\">Daring Fireball: More From Angela Ahrendts on Whether She Misses Fashion (and London)</a></h5> <h5><a href=\"https://twitter.com/nytopinion/status/1092619825535307776\" target=\"_blank\">NYT Opinion on Twitter: \"Happy Birthday, Facebook! 15 years today \u2014 and what a rollercoaster it has been.\"</a></h5> <h5><a href=\"https://www.vox.com/technology/2019/2/4/18205138/facebook-15-anniversary-social-network-founded-date-2004\" target=\"_blank\">Facebook 15th anniversary: Has Facebook been good or bad for the world? - Vox</a></h5> <h5><a href=\"https://www.bbc.com/news/technology-47146431\" target=\"_blank\">Facebook ordered by Germany to gather and mix less data - BBC News</a></h5> <h5><a href=\"https://juliareda.eu/2019/02/article-13-worse/\" target=\"_blank\">Julia Reda \u2013 Article 13 is back on \u2013 and it got worse, not better</a></h5> <h5><a href=\"https://www.theverge.com/2019/2/5/18212383/google-assistant-interpreter-mode-available-roll-out-home-smart-speaker-smart-display\" target=\"_blank\">Google Assistant\u2019s interpreter mode is now available - The Verge</a></h5> <h5><a href=\"https://variety.com/2019/digital/news/spotify-podcast-gimlet-anchor-1203129844/\" target=\"_blank\">Spotify Buys Podcast Startups Gimlet Media and Anchor \u2013 Variety</a></h5> <h5><a href=\"https://twitter.com/Lucas_Shaw/status/1093103778272751616\" target=\"_blank\">Lucas Shaw on Twitter: \"Spotify says it is buying 2 podcasting companies.\"</a></h5> <h5><a href=\"https://blog.emojipedia.org/230-new-emojis-in-final-list-for-2019/\" target=\"_blank\">230 New Emojis in Final List for 2019</a></h5> <h5><a href=\"https://www.nydailynews.com/news/national/ny-news-bear-eaten-redneck-tennessee-meth-20190205-story.html\" target=\"_blank\">Meth overdose, not a bear attack, killed man whose body was found in Smoky Mountains - NY Daily News</a></h5> <h5><a href=\"https://www.fox23.com/news/fort-gibson-man-uses-cpr-to-save-three-puppies-rescued-from-burning-home/914745070\" target=\"_blank\">PUPPY RESCUE: Oklahoma Man Uses CPR on Dogs Saved From Burning Home | FOX23</a></h5> <h5><a href=\"https://nypost.com/2019/02/06/video-shows-man-using-mouth-to-mouth-cpr-to-revive-puppies/\" target=\"_blank\">Video shows man using mouth-to-mouth to revive puppies</a></h5>",
        "pub_date_ms": 1549564200015,
        "guid_from_rss": "http://relay.fm/download/90",
        "listennotes_url": "https://www.listennotes.com/e/a211b2041cb649ab9bd0406453a6578b/",
        "audio_length_sec": 4217,
        "explicit_content": false,
        "maybe_audio_invalid": false,
        "listennotes_edit_url": "https://www.listennotes.com/e/a211b2041cb649ab9bd0406453a6578b/#edit"
      },
      "type": "episode",
      "notes": "",
      "added_at_ms": 1563257399371
    }
  ],
  "total": 35,
  "thumbnail": "https://d3sv2eduhewoas.cloudfront.net/playlist/image/48477deae02649d7ab9d3f1b3966af38.JPEG",
  "visibility": "public",
  "description": "A curated playlist of podcasts by Wenbin Fang.",
  "listennotes_url": "https://www.listennotes.com/listen/podcasts-about-podcasting-m1pe7z60bsw/?display=episode",
  "last_timestamp_ms": 1563257399371
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
      "episode_count": 4579,
      "podcast_count": 45,
      "listennotes_url": "https://www.listennotes.com/listen/wenbin-fangs-podcast-playlist-kr3-ta28cJu/?display=episode"
    },
    {
      "id": "m1pe7z60bsw",
      "name": "Podcasts about podcasting",
      "image": "https://cdn-images-1.listennotes.com/playlist/image/6907e8ff6b6c45df94cc059753f369cc.JPEG",
      "thumbnail": "https://d3sv2eduhewoas.cloudfront.net/playlist/image/48477deae02649d7ab9d3f1b3966af38.JPEG",
      "visibility": "public",
      "description": "A curated playlist of podcasts by Wenbin Fang.",
      "episode_count": 35,
      "podcast_count": 2,
      "listennotes_url": "https://www.listennotes.com/listen/podcasts-about-podcasting-m1pe7z60bsw/?display=episode"
    },
    {
      "id": "uIK85BM6EWJ",
      "name": "There's a podcast for that",
      "image": "https://cdn-images-1.listennotes.com/playlist/image/6e7c344a7a664320854a0677b57b3342.JPEG",
      "thumbnail": "https://cdn-images-1.listennotes.com/playlist/image/6e7c344a7a664320854a0677b57b3342.JPEG",
      "visibility": "public",
      "description": "Inspired by \"There's an app for that\". Email me if you want to become a contributor of this list: hello@listennotes.com",
      "episode_count": 0,
      "podcast_count": 125,
      "listennotes_url": "https://www.listennotes.com/listen/theres-a-podcast-for-that-uIK85BM6EWJ/?display=podcast"
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



