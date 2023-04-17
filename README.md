# Podcast API Python Library

[![Python CI](https://github.com/ListenNotes/podcast-api-python/actions/workflows/python.yml/badge.svg)](https://github.com/ListenNotes/podcast-api-python/actions/workflows/python.yml) [![PyPI](https://img.shields.io/pypi/v/podcast-api)](https://pypi.org/project/podcast-api/)

The Podcast API Python library provides convenient access to the [Listen Notes Podcast API](https://www.listennotes.com/podcast-api/) from
applications written in the Python language.

Simple and no-nonsense podcast search & directory API. Search the meta data of all podcasts and episodes by people, places, or topics. It's the same API that powers [the best podcast search engine Listen Notes](https://www.listennotes.com/).

If you have any questions, please contact [hello@listennotes.com](hello@listennotes.com?subject=Questions+about+the+Python+SDK+of+Listen+API)

<a href="https://www.listennotes.com/podcast-api/"><img src="https://raw.githubusercontent.com/ListenNotes/ListenApiDemo/master/web/src/powered_by_listennotes.png" width="300" /></a>


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
    - [Fetch a playlist's info and items (i.e., episodes or podcasts).](#fetch-a-playlists-info-and-items-ie-episodes-or-podcasts)
    - [Fetch a list of your playlists.](#fetch-a-list-of-your-playlists)
    - [Fetch trending search terms](#fetch-trending-search-terms)
    - [Fetch related search terms](#fetch-related-search-terms)
    - [Spell check on a search term](#spell-check-on-a-search-term)
    - [Fetch audience demographics for a podcast](#fetch-audience-demographics-for-a-podcast)
    - [Fetch podcasts by a publisher's domain name](#fetch-podcasts-by-a-publishers-domain-name)


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
available in your [Listen API Dashboard](https://www.listennotes.com/podcast-api/dashboard/#apps). Set `api_key` to its
value:

```python
from listennotes import podcast_api

api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)

response = client.search(q='star wars')

print(response.json())
```

If `api_key` is None, then we'll connect to a [mock server](https://www.listennotes.com/podcast-api/tutorials/#faq0) that returns fake data for testing purposes.


### Handling exceptions

Unsuccessful requests raise exceptions. The class of the exception will reflect
the sort of error that occurred.

| Exception Class  | Description |
| ------------- | ------------- |
|  AuthenticationError | wrong api key or your account is suspended  |
| APIConnectionError  | fail to connect to API servers  |
| InvalidRequestError  | something wrong on your end (client side errors), e.g., missing required parameters  |
| RateLimitError  | for FREE plan, exceeding the quota limit; or for all plans, sending too many requests too fast and exceeding the rate limit  |
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
  "took": 0.616,
  "count": 10,
  "total": 9135,
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
          264,
          68
        ],
        "thumbnail": "https://production.listennotes.com/podcasts/the-rough-cut-matt-feury-DEkF_8ybj6A-53MLh7NpAwm.300x300.jpg",
        "listen_score": 39,
        "title_original": "The Rough Cut",
        "listennotes_url": "https://www.listennotes.com/c/8758da9be6c8452884a8cab6373b007c/",
        "title_highlighted": "The Rough Cut",
        "publisher_original": "Matt Feury",
        "publisher_highlighted": "Matt Feury",
        "listen_score_global_rank": "2%"
      },
      "itunes_id": 1471556007,
      "thumbnail": "https://production.listennotes.com/podcasts/the-rough-cut-matt-feury-DEkF_8ybj6A-53MLh7NpAwm.300x300.jpg",
      "pub_date_ms": 1579507216163,
      "guid_from_rss": "004f03c8-cdf9-4ff5-9d89-b2147f8d55cf",
      "title_original": "Star Wars - The Force Awakens",
      "listennotes_url": "https://www.listennotes.com/e/ea09b575d07341599d8d5b71f205517b/",
      "audio_length_sec": 1694,
      "explicit_content": false,
      "title_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> - The Force Awakens",
      "description_original": "<p>In this episode of The Rough Cut we close out our study of the final Skywalker trilogy with a look back on the film that helped the dormant franchise make the jump to lightspeed, <a href=\"https://www.imdb.com/title/tt2488496/\">Episode VII - The Force Awakens</a>.\u00a0 Recorded in Amsterdam in front of a festival audience in 2018, editor <a href=\"https://www.imdb.com/name/nm0104783/?ref_=nv_sr_srsg_0\">Maryann Brandon ACE</a> recounts her work on <em>The Force Awakens</em> just as she was about to begin editing what would come to be known as <a href=\"https://www.imdb.com/title/tt2527338/?ref_=nm_flmg_edt_1\">Episode IX - The Rise of Skywalker</a>.</p> <p>\u00a0</p> <p>Go back to the beginning and listen to our <a href=\"http://theroughcutpod.com/paul-hirsch/\">podcast with Star Wars and 'Empire' editor, Paul Hirsch</a>.</p> <p>Hear editor Bob Ducsay talk about cutting <a href=\"http://theroughcutpod.com/last-jedi/\">The Last Jedi</a>.</p> <p>Listen to Maryann Brandon talk about her work on <a href=\"http://theroughcutpod.com/star-wars/\">The Rise of Skywalker</a>.</p> <p>Get your hands on the non-linear editor behind the latest Skywalker trilogy,\u00a0 <a href=\"https://www.avid.com/video-editor-right-for-you\">Avid Media Composer!</a></p> <p><a href=\"http://theroughcutpod.com/subscribe/\">Subscribe to The Rough Cut</a> for more great interviews with the heroes of the editing room!</p> <p>\u00a0</p> <p>\u00a0</p>",
      "description_highlighted": "...Go back to the beginning and listen to our podcast with <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> and 'Empire' editor, Paul Hirsch. \nHear editor Bob Ducsay talk about cutting The Last Jedi....",
      "transcripts_highlighted": []
    },
    {
      "id": "c877bf360bda4c74adea2ba066df6929",
      "rss": "https://feeds.megaphone.fm/ROOSTER7199250968",
      "link": "https://supercarlinbrothers.libsyn.com/star-wars-theory-the-great-star-wars-ice-cream-conspiracy?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/c877bf360bda4c74adea2ba066df6929/",
      "image": "https://production.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-biwhM2N35Rj-BodDr7iIAR3.1400x1400.jpg",
      "podcast": {
        "id": "8bdbb906eef04e5d8b391e947998e9af",
        "image": "https://production.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-biwhM2N35Rj-BodDr7iIAR3.1400x1400.jpg",
        "genre_ids": [
          99,
          265,
          214,
          68
        ],
        "thumbnail": "https://production.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-EtH8D7G3Qyq-BodDr7iIAR3.300x300.jpg",
        "listen_score": 53,
        "title_original": "Super Carlin Brothers",
        "listennotes_url": "https://www.listennotes.com/c/8bdbb906eef04e5d8b391e947998e9af/",
        "title_highlighted": "Super Carlin Brothers",
        "publisher_original": "J and Ben Carlin",
        "publisher_highlighted": "J and Ben Carlin",
        "listen_score_global_rank": "0.5%"
      },
      "itunes_id": 1479112798,
      "thumbnail": "https://production.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-EtH8D7G3Qyq-BodDr7iIAR3.300x300.jpg",
      "pub_date_ms": 1574355600328,
      "guid_from_rss": "d6549e8f-3718-4cbc-8fa0-6a5ce7c021b7",
      "title_original": "Star Wars Theory: The Great Star Wars Ice Cream Conspiracy",
      "listennotes_url": "https://www.listennotes.com/e/c877bf360bda4c74adea2ba066df6929/",
      "audio_length_sec": 638,
      "explicit_content": false,
      "title_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Theory: The Great <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Ice Cream Conspiracy",
      "description_original": "<p>Hurry to <a href=\"https://www.youtube.com/redirect?q=http%3A%2F%2Fupstart.com%2FSCB&amp;redir_token=7amGNOaR8D8jg7lSuoxwd30QvaB8MTU3OTExMTA1MkAxNTc5MDI0NjUy&amp;v=qmB4icIp8JM&amp;event=video_description\">http://upstart.com/SCB</a> to find out HOW LOW your Upstart rate is.</p> <p>\u00a0</p> <p>The Mandalorian has introduced to us some brand new Star Wars Jargon. In the very first episode we learn about a special metal called Beskar that can be melted down and reinforce the Mandalorian\u2019s armor. We also know that if he can complete his mission he has an ENTIRE CAMONTO of the stuff waiting for him upon delivery of the Young Orphan Darling Asset, aka LIL YODA. But how much is a camtono? And how on TATOOINE could it have anything to do with ICE CREAM!?</p>",
      "description_highlighted": "...The Mandalorian has introduced to us some brand new <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Jargon....",
      "transcripts_highlighted": []
    },
    {
      "id": "39746ccfc0d64f62aea8e96641366109",
      "rss": "https://www.spreaker.com/show/3200822/episodes/feed",
      "link": "https://www.spreaker.com/user/mcucast/star-wars-is-better-than-star-trek?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/39746ccfc0d64f62aea8e96641366109/",
      "image": "https://production.listennotes.com/podcasts/marvel-cinematic-universe-podcast-stranded-a3b_OGr0iUT-aXR7VuG2z4p.1400x1400.jpg",
      "podcast": {
        "id": "593c42e343ba44e7b6f8634a946f0b52",
        "image": "https://production.listennotes.com/podcasts/marvel-cinematic-universe-podcast-stranded-a3b_OGr0iUT-aXR7VuG2z4p.1400x1400.jpg",
        "genre_ids": [
          68,
          99,
          122
        ],
        "thumbnail": "https://production.listennotes.com/podcasts/marvel-cinematic-universe-podcast-stranded-6nzjMFWwxU4-aXR7VuG2z4p.300x300.jpg",
        "listen_score": 58,
        "title_original": "Marvel Cinematic Universe Podcast",
        "listennotes_url": "https://www.listennotes.com/c/593c42e343ba44e7b6f8634a946f0b52/",
        "title_highlighted": "Marvel Cinematic Universe Podcast",
        "publisher_original": "Stranded Panda",
        "publisher_highlighted": "Stranded Panda",
        "listen_score_global_rank": "0.5%"
      },
      "itunes_id": 907175322,
      "thumbnail": "https://production.listennotes.com/podcasts/marvel-cinematic-universe-podcast-stranded-6nzjMFWwxU4-aXR7VuG2z4p.300x300.jpg",
      "pub_date_ms": 1575521386385,
      "guid_from_rss": "https://api.spreaker.com/episode/20495415",
      "title_original": "Star Wars is better than Star Trek",
      "listennotes_url": "https://www.listennotes.com/e/39746ccfc0d64f62aea8e96641366109/",
      "audio_length_sec": 734,
      "explicit_content": true,
      "title_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> is better than <span class=\"ln-search-highlight\">Star</span> Trek",
      "description_original": "A just for fun episode.  Time to punish Matt for his sins against baby yoda",
      "description_highlighted": "...A just for fun episode.  Time to punish Matt for his sins against baby yoda...",
      "transcripts_highlighted": []
    },
    {
      "id": "a5ae21acf75a43538b635cf6b089f0b3",
      "rss": "http://feeds.feedburner.com/FramesPerSecondPodcast",
      "link": "https://megaphone.link/STU5698215144?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/a5ae21acf75a43538b635cf6b089f0b3/",
      "image": "https://production.listennotes.com/podcasts/frames-per-second-studio71-Tk47uwatlcN-J_3zM-VyFvj.1400x1400.jpg",
      "podcast": {
        "id": "88c28bd52e32422c8f3a71fab45aa77f",
        "image": "https://production.listennotes.com/podcasts/frames-per-second-studio71-Tk47uwatlcN-J_3zM-VyFvj.1400x1400.jpg",
        "genre_ids": [
          68
        ],
        "thumbnail": "https://production.listennotes.com/podcasts/frames-per-second-studio71-nFjw84GgN7c-J_3zM-VyFvj.300x300.jpg",
        "listen_score": 49,
        "title_original": "Frames Per Second",
        "listennotes_url": "https://www.listennotes.com/c/88c28bd52e32422c8f3a71fab45aa77f/",
        "title_highlighted": "Frames Per Second",
        "publisher_original": "Studio71",
        "publisher_highlighted": "Studio71",
        "listen_score_global_rank": "0.5%"
      },
      "itunes_id": 1453571424,
      "thumbnail": "https://production.listennotes.com/podcasts/frames-per-second-studio71-nFjw84GgN7c-J_3zM-VyFvj.300x300.jpg",
      "pub_date_ms": 1576544400475,
      "guid_from_rss": "90b15eb4-1fae-11ea-9f65-17cad885ccc2",
      "title_original": "Is Star Wars Overrated?",
      "listennotes_url": "https://www.listennotes.com/e/a5ae21acf75a43538b635cf6b089f0b3/",
      "audio_length_sec": 778,
      "explicit_content": true,
      "title_highlighted": "Is <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Overrated?",
      "description_original": "<p>In this episode, we discuss whether or not Star Wars is overrated. Let us know your thoughts. </p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://megaphone.fm/adchoices\">megaphone.fm/adchoices</a></p>",
      "description_highlighted": "...In this episode, we discuss whether or not <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> is overrated. Let us know your thoughts. \n \nLearn more about your ad choices. Visit megaphone.fm/adchoices...",
      "transcripts_highlighted": []
    },
    {
      "id": "42b1898db6a84973b41879618002937b",
      "rss": "https://www.spreaker.com/show/5650052/episodes/feed",
      "link": "https://www.spreaker.com/user/16701867/star-wars-galaxy-guides?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/42b1898db6a84973b41879618002937b/",
      "image": "https://production.listennotes.com/podcasts/the-vintage-rpg-podcast-vintage-rpg-ULe2OuyiBPx-eq8uGUY6vXN.1400x1400.jpg",
      "podcast": {
        "id": "f3094a0b14684300a3d6b69a1063e708",
        "image": "https://production.listennotes.com/podcasts/the-vintage-rpg-podcast-vintage-rpg-ULe2OuyiBPx-eq8uGUY6vXN.1400x1400.jpg",
        "genre_ids": [
          83,
          85,
          82
        ],
        "thumbnail": "https://production.listennotes.com/podcasts/the-vintage-rpg-podcast-vintage-rpg-N-xGey_CAin-eq8uGUY6vXN.300x300.jpg",
        "listen_score": 47,
        "title_original": "The Vintage RPG Podcast",
        "listennotes_url": "https://www.listennotes.com/c/f3094a0b14684300a3d6b69a1063e708/",
        "title_highlighted": "The Vintage RPG Podcast",
        "publisher_original": "Vintage RPG",
        "publisher_highlighted": "Vintage RPG",
        "listen_score_global_rank": "1%"
      },
      "itunes_id": 1409477830,
      "thumbnail": "https://production.listennotes.com/podcasts/the-vintage-rpg-podcast-vintage-rpg-N-xGey_CAin-eq8uGUY6vXN.300x300.jpg",
      "pub_date_ms": 1575867600166,
      "guid_from_rss": "9861105d-bf98-4684-871a-5cbe11484159",
      "title_original": "Star Wars Galaxy Guides",
      "listennotes_url": "https://www.listennotes.com/e/42b1898db6a84973b41879618002937b/",
      "audio_length_sec": 1519,
      "explicit_content": false,
      "title_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Galaxy Guides",
      "description_original": "Because Star Wars is hitting the critical mass point for 2019, we figured we'd add to the fun with an episode that looks at the Galaxy Guides series of sourcebooks for the West End Games Star Wars Role Playing Game. We take a quick tour through each of the twelve volumes and chat about what they added to the RPG experience and how they formed the backbone of the greater Star Wars Expanded Universe. * * * If\u00a0 you dig what we do, join us on the Vintage RPG Patreon for more roleplaying fun and surprises! Patrons keep us going! Like, Rate, Subscribe and Review the Vintage RPG Podcast! Send questions, comments or corrections to\u00a0<a href=\"mailto:info@vintagerpg.com\">info@vintagerpg.com</a>. Follow\u00a0Vintage RPG\u00a0on\u00a0Instagram,\u00a0Tumblr\u00a0and\u00a0Facebook. Learn more at the\u00a0Vintage RPG FAQ. Follow\u00a0Stu Horvath,\u00a0John McGuire,\u00a0VintageRPG\u00a0and\u00a0Unwinnable\u00a0on Twitter. Intro music by\u00a0George Collazo. The Vintage RPG illustration is by\u00a0Shafer Brown. Follow\u00a0him on Twitter. Tune in next week for the next episode. Until then, may the dice always roll in your favor!",
      "description_highlighted": "...Because <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> is hitting the critical mass point for 2019, we figured we'd add to the fun with an episode that looks at the Galaxy Guides series of sourcebooks for the West End Games <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Role...",
      "transcripts_highlighted": []
    },
    {
      "id": "a47ed9e517ed4767a679ac8499f27565",
      "rss": "https://filmthreat.libsyn.com/rss",
      "link": "https://filmthreat.libsyn.com/the-star-wars-saga-ranked?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/a47ed9e517ed4767a679ac8499f27565/",
      "image": "https://production.listennotes.com/podcasts/film-threat-film-threat-podcast-network-qh2IVg58zR6-cBuD3xXjTAG.1400x1400.jpg",
      "podcast": {
        "id": "f0a8fa8df3d04ec08fba8d317dafdeb0",
        "image": "https://production.listennotes.com/podcasts/film-threat-film-threat-podcast-network-qh2IVg58zR6-cBuD3xXjTAG.1400x1400.jpg",
        "genre_ids": [
          68
        ],
        "thumbnail": "https://production.listennotes.com/podcasts/film-threat-film-threat-podcast-network-Awkm8hri9Sg-cBuD3xXjTAG.300x300.jpg",
        "listen_score": 38,
        "title_original": "Film Threat",
        "listennotes_url": "https://www.listennotes.com/c/f0a8fa8df3d04ec08fba8d317dafdeb0/",
        "title_highlighted": "Film Threat",
        "publisher_original": "Film Threat Podcast Network",
        "publisher_highlighted": "Film Threat Podcast Network",
        "listen_score_global_rank": "2%"
      },
      "itunes_id": 1202134377,
      "thumbnail": "https://production.listennotes.com/podcasts/film-threat-film-threat-podcast-network-Awkm8hri9Sg-cBuD3xXjTAG.300x300.jpg",
      "pub_date_ms": 1577019600037,
      "guid_from_rss": "7bbf8fdc-22cb-4e9b-b3cb-edc9cd59a71f",
      "title_original": "The Star Wars Saga Ranked",
      "listennotes_url": "https://www.listennotes.com/e/a47ed9e517ed4767a679ac8499f27565/",
      "audio_length_sec": 1512,
      "explicit_content": true,
      "title_highlighted": "The <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Saga Ranked",
      "description_original": "The circle is now complete. The Film Threat staff discusses all nine episodes of the Star Wars saga and ranks the best films, characters and now that we've seen them all, debates which is the best trilogy.",
      "description_highlighted": "...The Film Threat staff discusses all nine episodes of the <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> saga and ranks the best films, characters and now that we've seen them all, debates which is the best trilogy....",
      "transcripts_highlighted": []
    },
    {
      "id": "abdc7a70194c4d6daaa429b7fc2ec5c6",
      "rss": "https://triviawithbudds.libsyn.com/rss",
      "link": "https://triviawithbudds.libsyn.com/11-trivia-questions-on-modern-star-wars?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/abdc7a70194c4d6daaa429b7fc2ec5c6/",
      "image": "https://production.listennotes.com/podcasts/trivia-with-budds-ryan-budds-FE72QeI6CSP-odHDeJf8O5Y.1400x1400.jpg",
      "podcast": {
        "id": "9229022e1b7e46578d8793b1601f983d",
        "image": "https://production.listennotes.com/podcasts/trivia-with-budds-ryan-budds-FE72QeI6CSP-odHDeJf8O5Y.1400x1400.jpg",
        "genre_ids": [
          68,
          82,
          133
        ],
        "thumbnail": "https://production.listennotes.com/podcasts/trivia-with-budds-ryan-budds-Cb9oyie0tUZ-odHDeJf8O5Y.300x300.jpg",
        "listen_score": 49,
        "title_original": "Trivia With Budds",
        "listennotes_url": "https://www.listennotes.com/c/9229022e1b7e46578d8793b1601f983d/",
        "title_highlighted": "Trivia With Budds",
        "publisher_original": "Ryan Budds",
        "publisher_highlighted": "Ryan Budds",
        "listen_score_global_rank": "0.5%"
      },
      "itunes_id": 1139115219,
      "thumbnail": "https://production.listennotes.com/podcasts/trivia-with-budds-ryan-budds-Cb9oyie0tUZ-odHDeJf8O5Y.300x300.jpg",
      "pub_date_ms": 1577226086771,
      "guid_from_rss": "6ab99079-61c0-4fa3-91f0-28cca5d918b0",
      "title_original": "11 Trivia Questions on Modern Star Wars",
      "listennotes_url": "https://www.listennotes.com/e/abdc7a70194c4d6daaa429b7fc2ec5c6/",
      "audio_length_sec": 646,
      "explicit_content": false,
      "title_highlighted": "11 Trivia Questions on Modern <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span>",
      "description_original": "<p>With the release of Rise of Skywalker, I just had to include a round on the most recent Star Wars movies at my live events last week, and now, on the podcast! Grab a wookie and play!</p> <p>Question of the Day brought to you by Funky Monkey Design of San Dimas, CA:\u00a0 What network originally aired Eureka's castle? Tweet me your answer @ryanbudds or email <a href=\"mailto:ryanbudds@gmail.com\">ryanbudds@gmail.com</a>\u00a0to be eligible for a prize!\u00a0</p> <p>Yesterday's QotD answer:\u00a0 Terry Trivia Team Name of the Day:\u00a0 Bob's Wahlburgers  Funky Monkey Designs:\u00a0 <a href=\"http://fmdesignsinc.com/\">http://fmdesignsinc.com/</a></p> <p>Save 25% site wide when using the code BUDDS25 on <a href=\"http://www.DrewBlank.com!\">www.DrewBlank.com!</a> This guy makes the best pop culture art around. Grab some Office, Parks and Rec, Big Lebowski, Bill Murray, and Horror Icon coloring books for the ones you love, along with hundreds of other great creations, all for 1/4th off!\u00a0</p> <p>THE FIRST TRIVIA QUESTION STARTS AT 03:53 Theme song by <a href=\"http://www.soundcloud.com/Frawsty\">www.soundcloud.com/Frawsty</a></p> <p>Bed Music:\u00a0 \"Misuse\" Kevin MacLeod (incompetech.com) Licensed under Creative Commons: By Attribution 4.0 License http://creativecommons.org/licenses/by/4.0/</p> <p><a href=\"http://TriviaWithBudds.com\">http://TriviaWithBudds.com</a><a href=\"http://facebook.com/TriviaWithBudds\">http://Facebook.com/TriviaWithBudds </a> <a href=\"http://twitter.com/ryanbudds\">http://Twitter.com/ryanbudds</a>  <a href=\"http://instagram.com/ryanbudds\">http://Instagram.com/ryanbudds</a></p> <p>Book a party, corporate event, or fundraiser anytime by emailing <a href=\"mailto:ryanbudds@gmail.com\">ryanbudds@gmail.com</a> or use the contact form here: <a href=\"https://www.triviawithbudds.com/contact\">https://www.triviawithbudds.com/contact</a></p> <p>SUPPORT THE SHOW:\u00a0<a href=\"http://www.Patreon.com/TriviaWithBudds\">www.Patreon.com/TriviaWithBudds</a></p> <p>Send me your questions and I'll read them/answer them on the show. Also send me any topics you'd like me to cover on future episodes, anytime! Cheers.\u00a0</p> <p><em>SPECIAL THANKS TO ALL MY PATREON SUBSCRIBERS INCLUDING:</em>\u00a0 Chris Adams, Christopher Callahan, Veronica Baker, Manny Majarian, Greg Bristow, Brenda Martinez, Alex DeSmet, Joe Finnie, Manny Cortez, Sarah McKavetz, Simon Time, Mo Martinez, Randy Tatum, Joan Bryce, Katie Christofferson, Denise Leonard, Jen Wojnar, Sarah Guest, Jess Whitener, Kyle Bonnin, Dan Papallo, Robert Casey, Ian Schulze, Casey O'Connor, Marissa Cuthbertson, Kyle Aumer, Taryn Napolitano, Matthew Frost, Katie Smith, Brian Salyer, Megan Acuna, Anna Evans, Jim Fields, Lauren Ward, Greg Heinz, Wreck My Podcast, Douglas French, Erika Cooper, Mark Haas, Sarah Haas, Katelyn Reik, Casey Becker, Paul McLaughlin, Amy Jeppesen, Melissa Chesser, Shaun Delacruz, Feana Nevel, Cody Welter, Paul Doronila, Kathryn Mott, Luke McKay, Ricky Carney, Kyle Hendrickson, Willy Powell, Myke Edwards, Joe Jermolowicz, Joey Mucha, Mona Bray, and Russ Friedewald! YOU GUYS ROCK!\u00a0</p>",
      "description_highlighted": "...With the release of Rise of Skywalker, I just had to include a round on the most recent <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> movies at my live events last week, and now, on the podcast! Grab a wookie and play!...",
      "transcripts_highlighted": []
    },
    {
      "id": "9cfb4901a891449aa30553cddfa582f8",
      "rss": "http://sw7x7.libsyn.com/rss",
      "link": "https://sites.libsyn.com/55931/1945-answering-star-wars-questions-from-star-wars-77-patrons?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/9cfb4901a891449aa30553cddfa582f8/",
      "image": "https://production.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-HN08OoDE7pc-AIg3cZVKCsL.1400x1400.jpg",
      "podcast": {
        "id": "4d3fe717742d4963a85562e9f84d8c79",
        "image": "https://production.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-HN08OoDE7pc-AIg3cZVKCsL.1400x1400.jpg",
        "genre_ids": [
          86,
          68,
          82,
          100,
          101,
          160,
          138
        ],
        "thumbnail": "https://production.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-2LryqMj-sGP-AIg3cZVKCsL.300x300.jpg",
        "listen_score": 49,
        "title_original": "Star Wars 7x7: The Daily Star Wars Podcast",
        "listennotes_url": "https://www.listennotes.com/c/4d3fe717742d4963a85562e9f84d8c79/",
        "title_highlighted": "Star Wars 7x7: The Daily Star Wars Podcast",
        "publisher_original": "Star Wars 7x7",
        "publisher_highlighted": "Star Wars 7x7",
        "listen_score_global_rank": "0.5%"
      },
      "itunes_id": 896354638,
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-2LryqMj-sGP-AIg3cZVKCsL.300x300.jpg",
      "pub_date_ms": 1572505201232,
      "guid_from_rss": "dacf14513dd34eddaace4f1b4bc27f86",
      "title_original": "1,945. Answering Star Wars Questions from Star Wars 7\u00d77 Patrons!",
      "listennotes_url": "https://www.listennotes.com/e/9cfb4901a891449aa30553cddfa582f8/",
      "audio_length_sec": 777,
      "explicit_content": false,
      "title_highlighted": "Answering <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Questions from <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> 7\u00d77 Patrons!",
      "description_original": "<p>Patrons of Star Wars 7x7 at the \"Vader's Fist\" level and above can submit questions for me to answer on the show every month! In this installment, we'll be talking about an aspect of the Millennium Falcon as it appears in The Rise of Skywalker; why Ben Solo may or may not have talked to his Force-ghost grandfather; and favorite Star Wars Halloween costumes. Punch it!</p> <p>***I'm listener supported! Join the community at http://Patreon.com/sw7x7 to get access to bonus episodes and other insider rewards.***\u00a0</p>",
      "description_highlighted": "...Patrons of <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> 7x7 at the \"Vader's Fist\" level and above can submit questions for me to answer on the show every month!...",
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
        "listen_score": 43,
        "title_original": "Saturday Night Live (SNL) Afterparty",
        "listennotes_url": "https://www.listennotes.com/c/09b986e503d4448ab0b625f6233bdd65/",
        "title_highlighted": "Saturday Night Live (SNL) Afterparty",
        "publisher_original": "John Murray / Spry FM",
        "publisher_highlighted": "John Murray / Spry FM",
        "listen_score_global_rank": "1%"
      },
      "itunes_id": 1133381225,
      "thumbnail": "https://production.listennotes.com/podcasts/saturday-night-live-snl-afterparty-john-wm1CtQVkRfy-_iOE4lLZ2pD.300x300.jpg",
      "pub_date_ms": 1576989000072,
      "guid_from_rss": "98206b6e-fc6e-45a5-85a6-e54eb4657299",
      "title_original": "Sample: Star Wars TV Talk Podcast",
      "listennotes_url": "https://www.listennotes.com/e/6280a11466dd407e99c66130f203167a/",
      "audio_length_sec": 1690,
      "explicit_content": false,
      "title_highlighted": "Sample: <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> TV Talk Podcast",
      "description_original": "<p>While John is hard at work editing our coverage of Eddie Murphy's triumphant return to Studio 8H, please enjoy this excerpt from the Star Wars TV Talk podcast\u2014on which John is regularly featured.</p> <p>This excerpt is from their discussion of the Disney+ streaming series The Mandalorian chapter 3: \"The Sin\", and contains heavy spoilers.</p> <p>John's take on all things Star Wars TV, can be heard weekly at <a href=\"https://starwarstvtalk.com\" rel=\"noopener\" target=\"_blank\">starwarstvtalk.com</a> or by subscribing to \"Star Wars TV Talk\" wherever better podcasts can be found.</p> Get Our Full-Length Episodes on Patreon <ul> <li><a href=\"https://www.patreon.com/snlpodcast\" rel=\"noopener\" target=\"_blank\">Patreon</a>: Become a patron to access our full-length, ad-free episodes and other exclusive member rewards.</li> </ul> Notes <ul> <li><a href=\"https://darylsbars.com/ref/john/\" rel=\"noopener\" target=\"_blank\">Daryl's All Natural Protein Bars</a>: Wholesome, nutritious, great tasting, gluten free, low-carb protein bars.</li> </ul> <ul> <li>Connect with us at: <ul> <li><a href=\"http://snlpodcast.com\" rel=\"noopener\" target=\"_blank\">snlpodcast.com</a></li> <li>Patreon: <a href=\"https://www.patreon.com/snlpodcast\" rel=\"noopener\" target=\"_blank\">snlpodcast</a></li> <li>Twitter: <a href=\"https://twitter.com/snlpodcast\" rel=\"noopener\" target=\"_blank\">@snlpodcast</a></li> <li>Instagram: <a href=\"https://www.instagram.com/snlpodcast/\" rel=\"noopener\" target=\"_blank\">snlpodcast</a></li> <li>Facebook: <a href=\"https://www.facebook.com/snlpodcast/\" rel=\"noopener\" target=\"_blank\">@snlpodcast</a></li> <li><a href=\"mailto:feedback@snlpodcast.com\">feedback@snlpodcast.com</a></li> </ul> </li> </ul>",
      "description_highlighted": "...John's take on all things <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> TV, can be heard weekly at starwarstvtalk.com or by subscribing to \"<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> TV Talk\" wherever better podcasts can be found....",
      "transcripts_highlighted": []
    },
    {
      "id": "6c02148d56814a289524f223bd072132",
      "rss": "https://feeds.megaphone.fm/ADV7475920787",
      "link": "https://www.imaginaryworldspodcast.org/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/6c02148d56814a289524f223bd072132/",
      "image": "https://production.listennotes.com/podcasts/imaginary-worlds-eric-molinsky-3LMZCqH2RDa-Va53GbWDK_U.1400x1400.jpg",
      "podcast": {
        "id": "c64d9295ac8e4ac1875ee23f564ea186",
        "image": "https://production.listennotes.com/podcasts/imaginary-worlds-eric-molinsky-3LMZCqH2RDa-Va53GbWDK_U.1400x1400.jpg",
        "genre_ids": [
          68,
          122,
          159,
          165,
          100
        ],
        "thumbnail": "https://production.listennotes.com/podcasts/imaginary-worlds-eric-molinsky-emTw3lA2ujL-Va53GbWDK_U.300x300.jpg",
        "listen_score": 63,
        "title_original": "Imaginary Worlds",
        "listennotes_url": "https://www.listennotes.com/c/c64d9295ac8e4ac1875ee23f564ea186/",
        "title_highlighted": "Imaginary Worlds",
        "publisher_original": "Eric Molinsky",
        "publisher_highlighted": "Eric Molinsky",
        "listen_score_global_rank": "0.1%"
      },
      "itunes_id": 916273527,
      "thumbnail": "https://production.listennotes.com/podcasts/imaginary-worlds-eric-molinsky-emTw3lA2ujL-Va53GbWDK_U.300x300.jpg",
      "pub_date_ms": 1577293200080,
      "guid_from_rss": "gid://art19-episode-locator/V0/nFFci_ugkpSRbZ0k8Qo5J-BoyCTYoauKO_E09Pd3KCM",
      "title_original": "In Defense of The Star Wars Holiday Special",
      "listennotes_url": "https://www.listennotes.com/e/6c02148d56814a289524f223bd072132/",
      "audio_length_sec": 1516,
      "explicit_content": true,
      "title_highlighted": "In Defense of The <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Holiday Special",
      "description_original": "<p>As far as Star Wars fans are concerned, there is no greater hive of scum and villainy than the 1978 made-for-TV Star Wars Holiday Special. The musical variety program, which centered on Chewbacca\u2019s family, is considered a hokey, misguided embarrassment. But entertainment writer Bonnie Burton and comedian Alex Schmidt think there\u2019s something to love about The Holiday Special -- and it may be in canon after all.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://megaphone.fm/adchoices\">megaphone.fm/adchoices</a></p>",
      "description_highlighted": "...As far as <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> fans are concerned, there is no greater hive of scum and villainy than the 1978 made-for-TV <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Holiday Special....",
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
                "description": "Episode id, which can be used to further fetch detailed episode metadata via `GET /episodes/{id}`."
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
                    "description": "Podcast id, which can be used to further fetch detailed podcast metadata via `GET /podcasts/{id}`."
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
                "description": "Podcast id, which can be used to further fetch detailed podcast metadata via `GET /podcasts/{id}`."
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
              "audio_length_sec": {
                "type": "integer",
                "example": 1291,
                "description": "Average audio length of all episodes of this podcast. In seconds."
              },
              "explicit_content": {
                "type": "boolean",
                "example": false,
                "description": "Whether this podcast contains explicit language."
              },
              "latest_episode_id": {
                "type": "string",
                "example": "d057092e57cc4ced80e0efaa196593d9",
                "description": "The id of the most recently published episode of this podcast, which can be used to further fetch detailed episode metadata via `GET /episodes/{id}`."
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
              "update_frequency_hours": {
                "type": "integer",
                "example": 168,
                "description": "How frequently does this podcast release a new episode? In hours. For example, if the value is 166, then it's every 166 hours (or weekly)."
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
                "description": "Curated list id, which can be used to further fetch detailed curated list metadata via `GET /curated_podcasts/{id}`."
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
                      "description": "Podcast id, which can be used to further fetch detailed podcast metadata via `GET /podcasts/{id}`."
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
      "id": "912f36444ea6475693ab3ab899cc3782",
      "image": "https://production.listennotes.com/podcasts/star-wars-theory-jigowatt-media-C8gLMex9FE5-FGYt8XM-sIK.1400x1400.jpg",
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-theory-jigowatt-media-ANg49Ewk-uz-FGYt8XM-sIK.300x300.jpg",
      "title_original": "Star Wars Theory",
      "explicit_content": false,
      "title_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Theory",
      "publisher_original": "Jigowatt Media",
      "publisher_highlighted": "Jigowatt Media"
    },
    {
      "id": "e8bdeb557c194bb9a97f8e1835a405b0",
      "image": "https://production.listennotes.com/podcasts/star-wars-stuff-podcast-star-wars-JAvZVoa09r8-4-E8Ab7PQ_B.1400x1400.jpg",
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-stuff-podcast-star-wars-4prJOMj3HID-4-E8Ab7PQ_B.300x300.jpg",
      "title_original": "Star Wars STUFF Podcast",
      "explicit_content": false,
      "title_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> STUFF Podcast",
      "publisher_original": "Star Wars",
      "publisher_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span>"
    },
    {
      "id": "46c50b17a1c6474fb77e21f438ccd78d",
      "image": "https://production.listennotes.com/podcasts/skytalkers-charlotte-caitlin-star-wars-S7L8tE_nIaZ--hNC10LzS4A.1400x1400.jpg",
      "thumbnail": "https://production.listennotes.com/podcasts/skytalkers-charlotte-caitlin-star-wars-DEIoXLeJOM9--hNC10LzS4A.300x300.jpg",
      "title_original": "Skytalkers",
      "explicit_content": false,
      "title_highlighted": "Skytalkers",
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
            "description": "Podcast id, which can be used to further fetch detailed podcast metadata via `GET /podcasts/{id}`."
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
    "amazon_music_url": "",
    "instagram_handle": ""
  },
  "image": "https://production.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-HN08OoDE7pc-AIg3cZVKCsL.1400x1400.jpg",
  "title": "Star Wars 7x7: The Daily Star Wars Podcast",
  "country": "United States",
  "website": "https://sw7x7.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
  "episodes": [
    {
      "id": "4e7c59e10e4640b98f2f3cb1777dbb43",
      "link": "https://sites.libsyn.com/55931/864-part-2-of-my-new-conversation-with-bobby-roberts?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/4e7c59e10e4640b98f2f3cb1777dbb43/",
      "image": "https://production.listennotes.com/podcasts/star-wars-7x7-the/864-part-2-of-my-new--vDBMTjY_mK-2WVsxtU0f3m.600x315.jpg",
      "title": "864: Part 2 of My (New) Conversation With Bobby Roberts",
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-7x7-the/864-part-2-of-my-new-yqjrzNDEXaS-2WVsxtU0f3m.300x157.jpg",
      "description": "<p>The second half of my latest conversation with Bobby Roberts, Podcast Emeritus from Full of Sith and now Star Wars \"Podcast Force Ghost at Large.\" Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1479110402174,
      "guid_from_rss": "bbada2b3a99054ce93b0eb95dd762b4d",
      "listennotes_url": "https://www.listennotes.com/e/4e7c59e10e4640b98f2f3cb1777dbb43/",
      "audio_length_sec": 2447,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/4e7c59e10e4640b98f2f3cb1777dbb43/#edit"
    },
    {
      "id": "9ae0e2e49a9c477191263df90adf7f3e",
      "link": "https://sites.libsyn.com/55931/863-a-new-conversation-with-bobby-roberts-part-1?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/9ae0e2e49a9c477191263df90adf7f3e/",
      "image": "https://production.listennotes.com/podcasts/star-wars-7x7-the/863-a-new-conversation-with-e_vHo9SM7ft-0YRBTlgiVeU.600x315.jpg",
      "title": "863: A (New) Conversation With Bobby Roberts, Part 1",
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-7x7-the/863-a-new-conversation-with-lcQsDS5uvYb-0YRBTlgiVeU.300x157.jpg",
      "description": "<p>An in-depth conversation about the Star Wars \"Story\" movies and so much more, featuring Bobby Roberts, Star Wars \"Podcast Force Ghost at Large.\" Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1479024002175,
      "guid_from_rss": "2c298fe68246aad30bd5afe0b79fdd76",
      "listennotes_url": "https://www.listennotes.com/e/9ae0e2e49a9c477191263df90adf7f3e/",
      "audio_length_sec": 2916,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/9ae0e2e49a9c477191263df90adf7f3e/#edit"
    },
    {
      "id": "98bcfa3fd1b44727913385938788bcc5",
      "link": "https://sites.libsyn.com/55931/862-assassin-clone-wars-briefing-season-3-episode-7?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/98bcfa3fd1b44727913385938788bcc5/",
      "image": "https://production.listennotes.com/podcasts/star-wars-7x7-the/862-assassin-clone-wars-lP94b2q5iOz-jEcMAdTntzs.600x315.jpg",
      "title": "862: \"Assassin\" - Clone Wars Briefing, Season 3, Episode 7",
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-7x7-the/862-assassin-clone-wars-Uh3E0GwOQRX-jEcMAdTntzs.300x157.jpg",
      "description": "<p>The beginnings of the true power of the Force, revealed in \"Assassin,\" season 3, episode 7 of the Star Wars: The Clone Wars cartoon series. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478937602176,
      "guid_from_rss": "6f64d1b37c661bbd066e773ae3b72d5e",
      "listennotes_url": "https://www.listennotes.com/e/98bcfa3fd1b44727913385938788bcc5/",
      "audio_length_sec": 636,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/98bcfa3fd1b44727913385938788bcc5/#edit"
    },
    {
      "id": "61d1de72f97e48e887c5d6280d3de384",
      "link": "https://sites.libsyn.com/55931/861-rogue-one-international-trailer-breakdown?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/61d1de72f97e48e887c5d6280d3de384/",
      "image": "https://production.listennotes.com/podcasts/star-wars-7x7-the/861-rogue-one-international-6rZOEiJHPpx-nGxaRC95V6o.600x315.jpg",
      "title": "861: Rogue One International Trailer Breakdown",
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-7x7-the/861-rogue-one-international-AFlEBXPHG6d-nGxaRC95V6o.300x157.jpg",
      "description": "<p>Surprise! An international trailer for Rogue One has dropped, and it includes new scenes, new dialogue, and some heavy foreshadowing about Jyn Erso's fate. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478851458177,
      "guid_from_rss": "10f042cf7346e078e201769b1097d651",
      "listennotes_url": "https://www.listennotes.com/e/61d1de72f97e48e887c5d6280d3de384/",
      "audio_length_sec": 1082,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/61d1de72f97e48e887c5d6280d3de384/#edit"
    },
    {
      "id": "53f5d00491134367ac3baf8c75b9a46b",
      "link": "https://sites.libsyn.com/55931/860-will-jyn-and-cassian-survive-rogue-one?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/53f5d00491134367ac3baf8c75b9a46b/",
      "image": "https://production.listennotes.com/podcasts/star-wars-7x7-the/860-will-jyn-and-cassian-VHAJQ1N57hE-l_3qXNfHAU0.600x315.jpg",
      "title": "860: Will Jyn and Cassian Survive Rogue One?",
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-7x7-the/860-will-jyn-and-cassian-k-2Si6HYjTP-l_3qXNfHAU0.300x157.jpg",
      "description": "<p>Today I conclude a two-episode set looking at the odds of survival for major Rogue One characters. Today: Jyn Erso, Cassian Andor, Bodhi Rook, and K-2SO. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478764802178,
      "guid_from_rss": "18062743dbffa4ce293686607ce30af4",
      "listennotes_url": "https://www.listennotes.com/e/53f5d00491134367ac3baf8c75b9a46b/",
      "audio_length_sec": 651,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/53f5d00491134367ac3baf8c75b9a46b/#edit"
    },
    {
      "id": "76c00b559f7d4f1c8be3ff1e2d808af9",
      "link": "https://sites.libsyn.com/55931/859-the-odds-who-will-survive-rogue-one?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/76c00b559f7d4f1c8be3ff1e2d808af9/",
      "image": "https://production.listennotes.com/podcasts/star-wars-7x7-the/859-the-odds-who-will-nM7l1BNPbIa-kprAXUCS8uQ.600x315.jpg",
      "title": "859: The Odds: Who Will Survive Rogue One?",
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-7x7-the/859-the-odds-who-will-RlXojiI5Wm6-kprAXUCS8uQ.300x157.jpg",
      "description": "<p>Will Galen Erso, Lyra Erso, Saw Gerrera, and Orson Krennic survive the events of Rogue One: A Star Wars Story? Starting a mini-series to look at the odds... Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478678402179,
      "guid_from_rss": "98e4d31b23bc7f48db490effe4d77e73",
      "listennotes_url": "https://www.listennotes.com/e/76c00b559f7d4f1c8be3ff1e2d808af9/",
      "audio_length_sec": 483,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/76c00b559f7d4f1c8be3ff1e2d808af9/#edit"
    },
    {
      "id": "62cdfe0b9ef64d1288a975a659dcf442",
      "link": "https://sites.libsyn.com/55931/858-together-new-rogue-one-commercial-dialogue?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/62cdfe0b9ef64d1288a975a659dcf442/",
      "image": "https://production.listennotes.com/podcasts/star-wars-7x7-the/858-together-new-rogue-one-TsLghBq5enX-WpFSsNUOzcL.600x315.jpg",
      "title": "858: \"Together\" - New Rogue One Commercial Dialogue",
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-7x7-the/858-together-new-rogue-one-dJF6XLmfYl4-WpFSsNUOzcL.300x157.jpg",
      "description": "<p>A new Rogue One commercial dropped Sunday, with some new dialogue that hints at the relationship between Jyn Erso, Saw Gerrera, the Rebellion, and the Partisans. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478592002180,
      "guid_from_rss": "c6dd42254e561130bf891f92e944041b",
      "listennotes_url": "https://www.listennotes.com/e/62cdfe0b9ef64d1288a975a659dcf442/",
      "audio_length_sec": 448,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/62cdfe0b9ef64d1288a975a659dcf442/#edit"
    },
    {
      "id": "a98c9cb497f04aec9e09cc50ce25ea59",
      "link": "https://sites.libsyn.com/55931/857-imperial-supercommandos-star-wars-rebels-season-3-episode-7?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/a98c9cb497f04aec9e09cc50ce25ea59/",
      "image": "https://production.listennotes.com/podcasts/star-wars-7x7-the/857-imperial-supercommandos-d0c7L1grbaI-L6bAOKCmyqt.600x315.jpg",
      "title": "857: \"Imperial Supercommandos\" - Star Wars Rebels Season 3, Episode 7",
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-7x7-the/857-imperial-supercommandos-OFpdNki02M_-L6bAOKCmyqt.300x157.jpg",
      "description": "<p>\"Imperial Supercommandos\" is Season 3, episode 7 of Star Wars Rebels, referring to Mandalorians serving the Empire. But can Fenn Rau be trusted, either? Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478505602181,
      "guid_from_rss": "007883a51d5ddc49b8b8d7fee80cb1ba",
      "listennotes_url": "https://www.listennotes.com/e/a98c9cb497f04aec9e09cc50ce25ea59/",
      "audio_length_sec": 494,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/a98c9cb497f04aec9e09cc50ce25ea59/#edit"
    },
    {
      "id": "e055bd1750a745a6adfcb70b935c03b7",
      "link": "https://sites.libsyn.com/55931/856-the-academy-clone-wars-briefing-season-3-episode-6?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/e055bd1750a745a6adfcb70b935c03b7/",
      "image": "https://production.listennotes.com/podcasts/star-wars-7x7-the/856-the-academy-clone-wars-6-EXfkbp4Sz-l6QpC-2RDTH.600x315.jpg",
      "title": "856: \"The Academy\" - Clone Wars Briefing, Season 3, Episode 6",
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-7x7-the/856-the-academy-clone-wars-x6_sqVGe-KS-l6QpC-2RDTH.300x157.jpg",
      "description": "<p>\"The Academy,\" Season 3 Episode 6 of the Clone Wars cartoon series, is a quieter episode that highlights the importance of Mandalore to the Star Wars franchise. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478415602182,
      "guid_from_rss": "f346a6e7575ab41197cacc6648070da2",
      "listennotes_url": "https://www.listennotes.com/e/e055bd1750a745a6adfcb70b935c03b7/",
      "audio_length_sec": 561,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/e055bd1750a745a6adfcb70b935c03b7/#edit"
    },
    {
      "id": "d602a45cdb524f3fac1effd79a61f828",
      "link": "https://sites.libsyn.com/55931/855-episode-viii-and-han-solo-movie-updates?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/d602a45cdb524f3fac1effd79a61f828/",
      "image": "https://production.listennotes.com/podcasts/star-wars-7x7-the/855-episode-viii-and-han-3Wkgr82DBxf-9vz38ko_X2s.600x315.jpg",
      "title": "855: Episode VIII and Han Solo Movie Updates",
      "thumbnail": "https://production.listennotes.com/podcasts/star-wars-7x7-the/855-episode-viii-and-han-naM8NWQxR19-9vz38ko_X2s.300x157.jpg",
      "description": "<p>Daisy Ridley says wait for Episode VIII for answers about Rey's parents. Bradford Young says the Han Solo movie won't be what you expect. Updates here... Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478329202183,
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
  "listen_score": 49,
  "total_episodes": 3272,
  "listennotes_url": "https://www.listennotes.com/c/4d3fe717742d4963a85562e9f84d8c79/",
  "audio_length_sec": 595,
  "explicit_content": false,
  "latest_episode_id": "eb1a656babb043239eaab3747e40efef",
  "latest_pub_date_ms": 1681716600000,
  "earliest_pub_date_ms": 1404637200000,
  "next_episode_pub_date": 1478329202183,
  "update_frequency_hours": 20,
  "listen_score_global_rank": "0.5%"
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
      "description": "Podcast id, which can be used to further fetch detailed podcast metadata via `GET /podcasts/{id}`."
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
          "example": "https://podcasts.google.com/feed/aHR0cHM6Ly9yc3MuYXJ0MTkuY29tL2pvaG4tc29sb21vbi1yZXBvcnRz",
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
        "amazon_music_url": {
          "type": "string",
          "example": "https://music.amazon.com/podcasts/6fc6d683-9ef3-4850-9c35-8e8b1a42a147/the-lock-sportscast",
          "description": "Amazon Music url for this podcast"
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
            "description": "Episode id, which can be used to further fetch detailed episode metadata via `GET /episodes/{id}`."
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
    "audio_length_sec": {
      "type": "integer",
      "example": 1291,
      "description": "Average audio length of all episodes of this podcast. In seconds."
    },
    "explicit_content": {
      "type": "boolean",
      "example": false,
      "description": "Whether this podcast contains explicit language."
    },
    "latest_episode_id": {
      "type": "string",
      "example": "d057092e57cc4ced80e0efaa196593d9",
      "description": "The id of the most recently published episode of this podcast, which can be used to further fetch detailed episode metadata via `GET /episodes/{id}`."
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
    "update_frequency_hours": {
      "type": "integer",
      "example": 168,
      "description": "How frequently does this podcast release a new episode? In hours. For example, if the value is 166, then it's every 166 hours (or weekly)."
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
  "title": "S1 Ep16: Arly Velasquez on Managing Risk",
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
      "amazon_music_url": "",
      "instagram_handle": "paralympics"
    },
    "image": "https://production.listennotes.com/podcasts/a-winning-mindset-a-winning-mindset-lessons-f06IOp3gkZq-BktA4YUzNbu.1400x1400.jpg",
    "title": "A Winning Mindset",
    "country": "Germany",
    "website": "https://www.paralympic.org/a-winning-mindset-lessons-from-the-paralympics?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
    "language": "English",
    "genre_ids": [
      88,
      181,
      90,
      191,
      217,
      78,
      77,
      111,
      67,
      122,
      124
    ],
    "itunes_id": 1527733477,
    "publisher": "A Winning Mindset: Lessons From The Paralympics",
    "thumbnail": "https://production.listennotes.com/podcasts/a-winning-mindset-a-winning-mindset-lessons-DHlfCBAqXh6-BktA4YUzNbu.300x300.jpg",
    "is_claimed": true,
    "description": "A Winning Mindset, an award-winning partnership between the International Paralympic Committee and Allianz, is a fascinating journey into the minds of Paralympians, with experiences that can benefit your own personal and professional life. \u00a0\n\u00a0\nThe official podcast of the Paralympic Games provides a platform for Para athletes to talk about their empowering and inspirational stories and allows each athlete to showcase their true personalities.\u00a0\n\nWINNER OF BEST BRANDED PODCAST AT THE 2021 WEBBY AWARDS\nWINNER OF BEST PODCAST AT 2021 DIGIDAY MEDIA EUROPE AWARDS\nWINNER OF BEST SPORT PODCAST AT 2021 SPORT INDUSTRY AWARDS\nWINNER OF BEST BRAND PARTNERSHIP AT 2022 DIGIDAY MEDIA EUROPE AWARDS\n\u00a0\nEpisodes go beyond Paralympic stories by covering a range of educational, mental health and self-improvement themes.\u00a0 Athletes also tackle subjects that are close to their hearts and of interest to fans. Issues explored include finding purpose, wellbeing, motivation, changing attitudes, overcoming failure, support systems, resilience, positivity, diversity and inclusion, body confidence and many more. \u00a0\n\nAllianz is a long-standing partner of the International Paralympic Committee. Together, we bring you this series of podcasts. We will introduce you to stories with Paralympians that will spark confidence in your everyday life. Stories of challenges, ups and downs, determination, and excellence. Stories that demonstrate the true power of having the right team behind you. And prepare you for what\u2019s ahead.\u00a0\n\u00a0\n\nThe Paralympic podcast series is presented by British broadcaster Andy Stevenson, who has reported on the Paralympic Games since 2012 for BBC and Channel 4.\u00a0\n\u00a0\nFeatured athletes include Tatyana McFadden, Jonnie Peacock and Arly Velasquez. Make sure you subscribe to hear upcoming episodes from athletes including Marcel Hug and Anastasia Pagonis.\u00a0",
    "looking_for": {
      "guests": false,
      "cohosts": false,
      "sponsors": false,
      "cross_promotion": true
    },
    "listen_score": 41,
    "total_episodes": 36,
    "listennotes_url": "https://www.listennotes.com/c/073a66b496824a5d9e80d52621f372dc/",
    "audio_length_sec": 1618,
    "explicit_content": false,
    "latest_episode_id": "ee3e98706e2f4e6b90f47406ca5a2024",
    "latest_pub_date_ms": 1643957760000,
    "earliest_pub_date_ms": 1598436120035,
    "update_frequency_hours": 155,
    "listen_score_global_rank": "1.5%"
  },
  "thumbnail": "https://production.listennotes.com/podcasts/a-winning-mindset/16-arly-velasquez-on-ftCxqnUg0Sr-c5khPVKzowB.300x300.jpg",
  "transcript": "\nA Paralympic skiier from Mexico isn\u2019t something you expect to see too often. But Arly Velasquez doesn\u2019t believe in expectations. \n\nVelasquez, one of a select few to ever represent Mexico at a Winter Paralympic Games, discusses the role of risk in his life - and how we can all learn to manage it.\u00a0\n\n\u201cI have developed because of taking decisions where I have no idea. It\u2019s a matter of 'does it feel right or not?'\" he said.\n\n\"I don't see it as a risk, I see that when I am in the mountain on a sit ski, I just feel the most free.\u201d\u00a0\n\nThe former BMX champion also discusses the risks he took when leaving Mexico on the spur of a moment, building a new life on the ski slopes in Canada. \u00a0\n\n\u201c(Skiing) gave me the belief to go back to Mexico, sell all my stuff,\u00a0 sell my car and pretty much fly to the border,\" he said.\u00a0\n\n\"It's very, rare that there are moments in your life where you are feeling and your gut tells you that you are in the right place. That you are doing the right thing and that it's something that you want to keep doing in your life. That's what I felt for the first time.\u201d\u00a0\n\nLearning topics for this episode include managing risk, how to build a brand, self-understanding, defiance, thrill-seeking and exploration. \u00a0\n\nAllianz is a long-standing partner of the International Paralympic Committee. Together, we\u2019re proud to bring you A Winning Mindset: Lessons From The Paralympics. We aim to help you move forward in all aspects of your personal and professional life.\u00a0\n\nBy hearing from Paralympic stars, you\u2019ll be introduced to stories that inspire and change the way you think. Stories of facing life\u2019s challenges with confidence, determination and excellence, and the true power of having the right team behind you.\u00a0",
  "description": "<div>\n<strong>A Paralympic skiier from Mexico isn\u2019t something you expect to see too often. But Arly Velasquez doesn\u2019t believe in expectations. </strong><br />\n<br />\nVelasquez, one of a select few to ever represent Mexico at a Winter Paralympic Games, discusses the role of risk in his life - and how we can all learn to manage it.\u00a0<br />\n<br />\n\u201cI have developed because of taking decisions where I have no idea. It\u2019s a matter of 'does it feel right or not?'\" he said.<br />\n<br />\n\"I don't see it as a risk, I see that when I am in the mountain on a sit ski, I just feel the most free.\u201d\u00a0<br />\n<br />\nThe former BMX champion also discusses the risks he took when leaving Mexico on the spur of a moment, building a new life on the ski slopes in Canada. \u00a0<br />\n<br />\n\u201c(Skiing) gave me the belief to go back to Mexico, sell all my stuff,\u00a0 sell my car and pretty much fly to the border,\" he said.\u00a0<br />\n<br />\n\"It's very, rare that there are moments in your life where you are feeling and your gut tells you that you are in the right place. That you are doing the right thing and that it's something that you want to keep doing in your life. That's what I felt for the first time.\u201d\u00a0<br />\n<br />\nLearning topics for this episode include managing risk, how to build a brand, self-understanding, defiance, thrill-seeking and exploration. \u00a0<br />\n<br />\nAllianz is a long-standing partner of the International Paralympic Committee. Together, we\u2019re proud to bring you A Winning Mindset: Lessons From The Paralympics. We aim to help you move forward in all aspects of your personal and professional life.\u00a0<br />\n<br />\nBy hearing from Paralympic stars, you\u2019ll be introduced to stories that inspire and change the way you think. Stories of facing life\u2019s challenges with confidence, determination and excellence, and the true power of having the right team behind you.\u00a0</div>",
  "pub_date_ms": 1607054220019,
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
      "description": "Episode id, which can be used to further fetch detailed episode metadata via `GET /episodes/{id}`."
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
          "description": "Podcast id, which can be used to further fetch detailed podcast metadata via `GET /podcasts/{id}`."
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
              "example": "https://podcasts.google.com/feed/aHR0cHM6Ly9yc3MuYXJ0MTkuY29tL2pvaG4tc29sb21vbi1yZXBvcnRz",
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
            "amazon_music_url": {
              "type": "string",
              "example": "https://music.amazon.com/podcasts/6fc6d683-9ef3-4850-9c35-8e8b1a42a147/the-lock-sportscast",
              "description": "Amazon Music url for this podcast"
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
        "audio_length_sec": {
          "type": "integer",
          "example": 1291,
          "description": "Average audio length of all episodes of this podcast. In seconds."
        },
        "explicit_content": {
          "type": "boolean",
          "example": false,
          "description": "Whether this podcast contains explicit language."
        },
        "latest_episode_id": {
          "type": "string",
          "example": "d057092e57cc4ced80e0efaa196593d9",
          "description": "The id of the most recently published episode of this podcast, which can be used to further fetch detailed episode metadata via `GET /episodes/{id}`."
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
        "update_frequency_hours": {
          "type": "integer",
          "example": 168,
          "description": "How frequently does this podcast release a new episode? In hours. For example, if the value is 166, then it's every 166 hours (or weekly)."
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
      "id": 77,
      "name": "Sports",
      "parent_id": 67
    },
    {
      "id": 93,
      "name": "Business",
      "parent_id": 67
    },
    {
      "id": 125,
      "name": "History",
      "parent_id": 67
    },
    {
      "id": 122,
      "name": "Society & Culture",
      "parent_id": 67
    },
    {
      "id": 127,
      "name": "Technology",
      "parent_id": 67
    },
    {
      "id": 132,
      "name": "Kids & Family",
      "parent_id": 67
    },
    {
      "id": 168,
      "name": "Fiction",
      "parent_id": 67
    },
    {
      "id": 88,
      "name": "Health & Fitness",
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
      "id": 133,
      "name": "Comedy",
      "parent_id": 67
    },
    {
      "id": 100,
      "name": "Arts",
      "parent_id": 67
    },
    {
      "id": 69,
      "name": "Religion & Spirituality",
      "parent_id": 67
    },
    {
      "id": 117,
      "name": "Government",
      "parent_id": 67
    },
    {
      "id": 68,
      "name": "TV & Film",
      "parent_id": 67
    },
    {
      "id": 82,
      "name": "Leisure",
      "parent_id": 67
    },
    {
      "id": 111,
      "name": "Education",
      "parent_id": 67
    },
    {
      "id": 107,
      "name": "Science",
      "parent_id": 67
    },
    {
      "id": 135,
      "name": "True Crime",
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
  "total": 728,
  "has_next": true,
  "podcasts": [
    {
      "id": "28ba59be5b8346589e910e24d4b3eed7",
      "rss": "https://pultepodcast.libsyn.com/rss",
      "type": "episodic",
      "email": "Bill@pulte.org",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9wdWx0ZXBvZGNhc3QubGlic3luLmNvbS9yc3M=",
        "spotify_url": "https://open.spotify.com/show/31g21O5kSlCstxSswwtPzh",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-pulte-podcast-8PvlfCgcR_X-xBWa8_-4MTR.1400x1400.jpg",
      "title": "The Pulte Podcast",
      "country": "United States",
      "website": "http://www.pulte.org?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        171,
        93,
        94,
        67
      ],
      "itunes_id": 1525585134,
      "publisher": "Bill Pulte | Giving Money and Knowledge",
      "thumbnail": "https://production.listennotes.com/podcasts/the-pulte-podcast-gqCft_ZYOIz-xBWa8_-4MTR.300x300.jpg",
      "is_claimed": false,
      "description": "I'm giving away money, rent, food, and knowledge to people in need. I've built and sold 8 figure companies and now I want to help people.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 73,
      "total_episodes": 12,
      "listennotes_url": "https://www.listennotes.com/c/28ba59be5b8346589e910e24d4b3eed7/",
      "audio_length_sec": 446,
      "explicit_content": false,
      "latest_episode_id": "e26262d976694428bc1cc8c7af791d1b",
      "latest_pub_date_ms": 1621426832000,
      "earliest_pub_date_ms": 1596040778010,
      "update_frequency_hours": 202,
      "listen_score_global_rank": "0.01%"
    },
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
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/startup-podcast-gimlet-14zU0c_MOmv-n9PpCBTQvoJ.1400x1400.jpg",
      "title": "StartUp Podcast",
      "country": "United States",
      "website": "https://www.gimletmedia.com/startup?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        97,
        93,
        157,
        94,
        68,
        127,
        67,
        171
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
      "listen_score": 73,
      "total_episodes": 153,
      "listennotes_url": "https://www.listennotes.com/c/0d362b13399240de97602ef614acdcbc/",
      "audio_length_sec": 2176,
      "explicit_content": false,
      "latest_episode_id": "3663e1ba8f944df7956378ab332bf12b",
      "latest_pub_date_ms": 1598004000000,
      "earliest_pub_date_ms": 1396742400151,
      "update_frequency_hours": 253,
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
        "spotify_url": "https://open.spotify.com/show/4X3yDKgVTWRjSd6r0vhgo4",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "planetmoney",
        "facebook_handle": "planetmoney",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-indicator-from-planet-money-npr-zjaIT2Ovo-r-G2EDjFO-TLA.1400x1400.jpg",
      "title": "The Indicator from Planet Money",
      "country": "United States",
      "website": "https://www.npr.org/podcasts/510325/the-indicator-from-planet-money?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        99,
        98,
        144,
        171,
        93,
        67
      ],
      "itunes_id": 1320118593,
      "publisher": "NPR",
      "thumbnail": "https://production.listennotes.com/podcasts/the-indicator-from-planet-money-npr-pb1-q5f_msG-G2EDjFO-TLA.300x300.jpg",
      "is_claimed": false,
      "description": "A little show about big ideas. From the people who make <em>Planet Money</em>, <em>The Indicator</em> helps you make sense of what's happening today. It's a quick hit of insight into work, business, the economy, and everything else. Listen weekday afternoons.<br><br><em>Got money on your mind? Try Planet Money+ \u2014 a new way to support the show you love, get a sponsor-free feed of the podcast, *and* get access to bonus content. A subscription also gets you access to The Indicator and Planet Money Summer School, both without interruptions. </em>",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 73,
      "total_episodes": 1229,
      "listennotes_url": "https://www.listennotes.com/c/5f237b79824e4dfb8355f6dff9b1c542/",
      "audio_length_sec": 574,
      "explicit_content": false,
      "latest_episode_id": "33b9445be544477a8931f5c30b6cee1a",
      "latest_pub_date_ms": 1681507413000,
      "earliest_pub_date_ms": 1527108300299,
      "update_frequency_hours": 29,
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
        "spotify_url": "https://open.spotify.com/show/4eylg9GZJOVvUhTynt4jjA",
        "youtube_url": "",
        "linkedin_url": "https://www.linkedin.com/in/adammgrant/",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "AdamMGrant",
        "facebook_handle": "AdamMGrant",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/worklife-with-adam-grant-ted-KgaXjFPEoVc.1400x1400.jpg",
      "title": "WorkLife with Adam Grant",
      "country": "United States",
      "website": "https://www.ted.com/podcasts/worklife?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        97,
        111,
        93
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
      "listen_score": 73,
      "total_episodes": 111,
      "listennotes_url": "https://www.listennotes.com/c/34beae8ad8fd4b299196f413b8270a30/",
      "audio_length_sec": 2370,
      "explicit_content": false,
      "latest_episode_id": "7d8be1e80e314f378fb38082c3c5585b",
      "latest_pub_date_ms": 1681185600000,
      "earliest_pub_date_ms": 1518044524105,
      "update_frequency_hours": 166,
      "listen_score_global_rank": "0.01%"
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
        "spotify_url": "https://open.spotify.com/show/6fZXOzehJ9JtOyFjirF3qt",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "tonyrobbins",
        "facebook_handle": "TonyRobbins",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-tony-robbins-podcast-tony-robbins-eh9wNFJcP1W.1400x1400.jpg",
      "title": "The Tony Robbins Podcast",
      "country": "United States",
      "website": "http://tonyrobbins.com/podcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        97,
        111,
        144,
        181,
        93,
        78,
        157,
        90
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
      "listen_score": 72,
      "total_episodes": 158,
      "listennotes_url": "https://www.listennotes.com/c/fc6d33e22b7f4db38df3bb64a9a8c227/",
      "audio_length_sec": 2839,
      "explicit_content": false,
      "latest_episode_id": "ad611e0c0a1b4792b39e9c9732b6fa7a",
      "latest_pub_date_ms": 1679533500000,
      "earliest_pub_date_ms": 1459373820099,
      "update_frequency_hours": 885,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "ed79b615ed074204bc4702b56a264a78",
      "rss": "https://thelifecoachschool.libsyn.com/rss",
      "type": "episodic",
      "email": "brooke@thelifecoachschool.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly90aGVsaWZlY29hY2hzY2hvb2wubGlic3luLmNvbS9yc3M=",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "brookecastillo",
        "facebook_handle": "",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-life-coach-school-podcast-brooke-castillo-xURrlLHEVv--V5of7JlG_RD.1400x1400.jpg",
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
      "thumbnail": "https://production.listennotes.com/podcasts/the-life-coach-school-podcast-brooke-castillo-vTH8ygOuwXd-V5of7JlG_RD.300x300.jpg",
      "is_claimed": false,
      "description": "The Life Coach School Podcast is your go-to resource for learning, growing, and becoming certified as a Life Coach & Weight Loss Coach. Through this podcast, you'll hear directly from the Master Coach Brooke Castillo to help you better understand life coaching, the required skills and mindsets, and how we focus on serving the client to get them the results they seek.  At The Life Coach School, we offer a thorough and intense certification course that produces some of the most successful coaches coaching today. Learn more at TheLifeCoachSchool.com.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 72,
      "total_episodes": 504,
      "listennotes_url": "https://www.listennotes.com/c/ed79b615ed074204bc4702b56a264a78/",
      "audio_length_sec": 1915,
      "explicit_content": false,
      "latest_episode_id": "f914f36e10d4428399f1a6284b965c94",
      "latest_pub_date_ms": 1681376400000,
      "earliest_pub_date_ms": 1398606925476,
      "update_frequency_hours": 151,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "bee3a6eeb43d45d482cff16d7e6eec6d",
      "rss": "https://mcsorleys.barstoolsports.com/feed/bffs",
      "type": "episodic",
      "email": "podcasting@barstoolsports.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9tY3NvcmxleXMuYmFyc3Rvb2xzcG9ydHMuY29tL2ZlZWQvYmZmcw==",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/bffs-with-dave-portnoy-josh-richards-and-c-YmGvaLCjt-UwCtO6PxIiq.1400x1400.jpg",
      "title": "BFFs with Dave Portnoy, Josh Richards, and Brianna Chickenfry",
      "country": "United States",
      "website": "https://www.barstoolsports.com/shows/134/Bffs?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        98,
        67
      ],
      "itunes_id": 1534324153,
      "publisher": "Barstool Sports",
      "thumbnail": "https://production.listennotes.com/podcasts/bffs-with-dave-portnoy-josh-richards-and-0vXYw5UR7ut-UwCtO6PxIiq.300x300.jpg",
      "is_claimed": false,
      "description": "<p>The unlikely trio of Josh Richards, Dave Portnoy & Brianna Chickenfry team up to talk all things pop culture, celebrities, influencers & TikTok. You never know what to expect from this trio from breaking entertainment news to generational differences they\u2019re sure to make you laugh while keeping you up to date.</p><br /><p>You can find every episode of this show on Apple Podcasts, Spotify or YouTube. Prime Members can listen ad-free on Amazon Music. For more, visit <a href=\"https://barstool.link/bffspod\">barstool.link/bffspod</a></p>",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 71,
      "total_episodes": 124,
      "listennotes_url": "https://www.listennotes.com/c/bee3a6eeb43d45d482cff16d7e6eec6d/",
      "audio_length_sec": 3781,
      "explicit_content": true,
      "latest_episode_id": "1741183d6583436fbd4b58d45d669ac1",
      "latest_pub_date_ms": 1681344000000,
      "earliest_pub_date_ms": 1601668154000,
      "update_frequency_hours": 168,
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
        "spotify_url": "https://open.spotify.com/show/7tznexFwtbxfPOYF5mxkxI",
        "youtube_url": "https://www.youtube.com/@craiggroeschel",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "craiggroeschel",
        "facebook_handle": "life.church",
        "amazon_music_url": "",
        "instagram_handle": "craiggroeschel"
      },
      "image": "https://production.listennotes.com/podcasts/craig-groeschel-leadership-podcast-lifechurch--_K8zgsM0x1-dy-uJsHC_9T.1400x1400.jpg",
      "title": "Craig Groeschel Leadership Podcast",
      "country": "United States",
      "website": "https://www.life.church/leadershippodcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        97
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
      "listen_score": 71,
      "total_episodes": 128,
      "listennotes_url": "https://www.listennotes.com/c/2184bada602d431689dbb4c6c1bc5839/",
      "audio_length_sec": 1731,
      "explicit_content": false,
      "latest_episode_id": "7e989412b8f7427eb4ae75bb3af2863f",
      "latest_pub_date_ms": 1680775200000,
      "earliest_pub_date_ms": 1452675180120,
      "update_frequency_hours": 407,
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
        "spotify_url": "https://open.spotify.com/show/5RllMBgvDnTau8nnsCUdse",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "marketsnacks",
        "facebook_handle": "MarketSnacks",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-syLJP5rimSp-kmx0XIZTAys.1400x1400.jpg",
      "title": "The Best One Yet",
      "country": "United States",
      "website": "https://www.instagram.com/tboypod?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        98,
        67,
        93,
        95,
        99
      ],
      "itunes_id": 1386234384,
      "publisher": "Nick & Jack Studios",
      "thumbnail": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-YPWcDaHknUz-kmx0XIZTAys.300x300.jpg",
      "is_claimed": false,
      "description": "Feel brighter every day with our 20-minute pop-biz podcast. The 3 business news stories you need, with fresh takes you can pretend you came up with \u2014 Pairs perfectly with your morning oatmeal ritual. Hosted by Jack Crivici-Kramer & Nick Martell.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 71,
      "total_episodes": 950,
      "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
      "audio_length_sec": 1090,
      "explicit_content": false,
      "latest_episode_id": "e67a558bc7564f72aede4f01d3e0004f",
      "latest_pub_date_ms": 1681722000000,
      "earliest_pub_date_ms": 1553519100903,
      "update_frequency_hours": 33,
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
        "spotify_url": "https://open.spotify.com/show/1bJRgaFZHuzifad4IAApFR",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "mastersofscale",
        "facebook_handle": "mastersofscale",
        "amazon_music_url": "",
        "instagram_handle": "mastersofscale"
      },
      "image": "https://production.listennotes.com/podcasts/masters-of-scale-with-reid-hoffman-waitwhat-PJGeHLMmxa6-mYoV0CUyxTD.1400x1400.jpg",
      "title": "Masters of Scale",
      "country": "United States",
      "website": "http://www.mastersofscale.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        122,
        97,
        93,
        149,
        173,
        127,
        157,
        67,
        171
      ],
      "itunes_id": 1227971746,
      "publisher": "WaitWhat ",
      "thumbnail": "https://production.listennotes.com/podcasts/masters-of-scale-with-reid-hoffman-waitwhat-XJs3WwmUrx7-mYoV0CUyxTD.300x300.jpg",
      "is_claimed": false,
      "description": "\n      <p>Award-winning business advice from Silicon Valley and beyond. Iconic CEOs, from Nike to Netflix, Starbucks to Slack, share the strategies that helped them grow from startups into global brands \u2014 and to weather crisis when it strikes.&nbsp;</p><p>Our two formats help tell the complete story of how a business grows, survives and thrives, and the mindsets of growth that keep leaders in the game.</p><p>On each episode of our classic format, host Reid Hoffman \u2014 LinkedIn cofounder, Greylock partner and legendary Silicon Valley investor \u2014 proves an unconventional theory about how businesses scale, asking his guests to share their stories of entrepreneurship, leadership, strategy, management, fundraising. You\u2019ll hear the human journey too \u2014 failures, setbacks, learnings.&nbsp;</p><p>From our Rapid Response format, you can expect real-time wisdom from business leaders in fast-changing situations. Hosted by Bob Safian, past editor in chief of Fast Company, these episodes tackle crisis response, rebuilding, diversity &amp; inclusion, leadership change and much more.&nbsp;</p>\n    ",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 71,
      "total_episodes": 383,
      "listennotes_url": "https://www.listennotes.com/c/d863da7f921e435fb35f512b54e774d6/",
      "audio_length_sec": 2049,
      "explicit_content": false,
      "latest_episode_id": "3e6e6e405f794ce69855d60079b2c60d",
      "latest_pub_date_ms": 1681203600000,
      "earliest_pub_date_ms": 1492543297377,
      "update_frequency_hours": 107,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "5590cb1318054bceb942564a4f067eb6",
      "rss": "https://www.marketplace.org/feed/podcast/marketplace",
      "type": "episodic",
      "email": "marketplacecomments@marketplace.org",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly93d3cubWFya2V0cGxhY2Uub3JnL2ZlZWQvcG9kY2FzdC9tYXJrZXRwbGFjZQ==",
        "spotify_url": "https://open.spotify.com/show/6zYlX5UGEPmNCWacYUJQGD",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "Marketplace",
        "facebook_handle": "marketplaceapm",
        "amazon_music_url": "",
        "instagram_handle": "marketplaceapm"
      },
      "image": "https://production.listennotes.com/podcasts/marketplace-marketplace-WHc17NQy23S-Jing2WtK5UE.1400x1400.jpg",
      "title": "Marketplace",
      "country": "United States",
      "website": "https://www.marketplace.org/shows/marketplace/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        95,
        99,
        173,
        93,
        67
      ],
      "itunes_id": 201853034,
      "publisher": "Marketplace",
      "thumbnail": "https://production.listennotes.com/podcasts/marketplace-marketplace-_YVywHeR0-S-Jing2WtK5UE.300x300.jpg",
      "is_claimed": false,
      "description": "<p>Every weekday, host Kai Ryssdal helps you make sense of the day\u2019s business and economic news \u2014 no econ degree or finance background required. \u201cMarketplace\u201d takes you beyond the numbers, bringing you context. Our team of reporters all over the world speak with CEOs, policymakers and regular people just trying to get by.</p>\n",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 71,
      "total_episodes": 344,
      "listennotes_url": "https://www.listennotes.com/c/5590cb1318054bceb942564a4f067eb6/",
      "audio_length_sec": 1652,
      "explicit_content": false,
      "latest_episode_id": "f340ca7271c0406498e9ef676c6226ac",
      "latest_pub_date_ms": 1681511980000,
      "earliest_pub_date_ms": 1640304971049,
      "update_frequency_hours": 28,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "23bd4f3432c2452d93f525e2446a5878",
      "rss": "https://feeds.simplecast.com/4YELvXgu",
      "type": "episodic",
      "email": "rss@earwolf.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5zaW1wbGVjYXN0LmNvbS80WUVMdlhndQ==",
        "spotify_url": "https://open.spotify.com/show/0Vdp4gyQoY0kkcvaLnIgvx",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/scam-goddess-earwolf-laci-mosley-pMX-87Jicaq-PstEMgqXCUd.1400x1400.jpg",
      "title": "Scam Goddess",
      "country": "United States",
      "website": "https://www.earwolf.com/show/scam-goddess/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        133,
        135,
        67
      ],
      "itunes_id": 1479455008,
      "publisher": "Earwolf & Laci Mosley",
      "thumbnail": "https://production.listennotes.com/podcasts/scam-goddess-earwolf-laci-mosley-fy8Bs4RlT06-PstEMgqXCUd.300x300.jpg",
      "is_claimed": false,
      "description": "\u201cScam Goddess is a podcast dedicated to fraud and all those who practice it! Each week host Laci Mosley (aka Scam Goddess) keeps listeners up to date on current rackets, digs deep into the latest scams, and breaks down historic hoodwinks alongside some of your favorite comedians! It's like true crime only without all the death! True fun crime!\u201d",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 70,
      "total_episodes": 123,
      "listennotes_url": "https://www.listennotes.com/c/23bd4f3432c2452d93f525e2446a5878/",
      "audio_length_sec": 4051,
      "explicit_content": true,
      "latest_episode_id": "f224faef768f4d31b1761df0805af826",
      "latest_pub_date_ms": 1681185900000,
      "earliest_pub_date_ms": 1420099200036,
      "update_frequency_hours": 167,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "4e272a4cec844b32be6ad2048d614b28",
      "rss": "https://feeds.simplecast.com/mWO0BLec",
      "type": "episodic",
      "email": null,
      "extra": {
        "url1": "https://bythebookpod.com/",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly93d3cub21ueWNvbnRlbnQuY29tL2QvcGxheWxpc3QvYWFlYTRlNjktYWY1MS00OTVlLWFmYzktYTk3NjAxNDY5MjJiLzczZmQ4MGMyLTQ4ZDYtNDMzYy04MTdmLWFhYTQwMTdjM2MxNi8xYzM1Yzk0Ny01NmQyLTQ5Y2MtYmUxNS1hYWE0MDE3YzNjMWUvcG9kY2FzdC5yc3M=",
        "spotify_url": "https://open.spotify.com/show/4uPxHwRyvRC7ebz3gMxpk1",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "bythebookpod",
        "facebook_handle": "kristenandjolenta",
        "amazon_music_url": "",
        "instagram_handle": "bythebookpod"
      },
      "image": "https://production.listennotes.com/podcasts/how-to-be-fine-stitcher-jolenta-greenberg-SXRBvqDjNth--sCyAljv4BT.1400x1400.jpg",
      "title": "How to Be Fine",
      "country": "United States",
      "website": "https://www.stitcher.com/podcast/stitcher/by-the-book?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        88,
        90,
        122,
        133,
        93,
        78,
        191,
        104,
        67
      ],
      "itunes_id": 1217948628,
      "publisher": "Stitcher & Jolenta Greenberg, Kristen Meinzer",
      "thumbnail": "https://production.listennotes.com/podcasts/how-to-be-fine-stitcher-jolenta-greenberg-1DC5KVBFAc7--sCyAljv4BT.300x300.jpg",
      "is_claimed": false,
      "description": "Half advice show, half cultural critique, and one wild ride through the world of wellness. Join podcast besties Kristen Meinzer and Jolenta Greenberg as they dissect the inner workings of the betterment industry - and offer up some advice along the way. Their goal? To help get you a little closer to fine.\n\nKristen and Jolenta's first show By the Book is on this feed. To hear back episodes of By the Book, just scroll down!",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 70,
      "total_episodes": 248,
      "listennotes_url": "https://www.listennotes.com/c/4e272a4cec844b32be6ad2048d614b28/",
      "audio_length_sec": 2083,
      "explicit_content": true,
      "latest_episode_id": "cdb493d25c9a4a6183c061f62e99f9d2",
      "latest_pub_date_ms": 1681358700000,
      "earliest_pub_date_ms": 1489787580232,
      "update_frequency_hours": 165,
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
        "spotify_url": "https://open.spotify.com/show/7wjv5MRCXWXImqTFhcufLy",
        "youtube_url": "https://www.youtube.com/user/smartpassiveincome",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "patflynn",
        "facebook_handle": "smartpassiveincome",
        "amazon_music_url": "https://music.amazon.com/podcasts/341282a1-cba9-4188-aa58-e09a51ccaa87/the-smart-passive-income-online-business-and-blogging-podcast",
        "instagram_handle": "patflynn"
      },
      "image": "https://production.listennotes.com/podcasts/the-smart-passive-income-online-business-jN-aR6qdYuo-NDa6-ySp9kw.1400x1400.jpg",
      "title": "The Smart Passive Income Online Business and Blogging Podcast",
      "country": "United States",
      "website": "https://art19.com/shows/smart-passive-income-podcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        97,
        67,
        94,
        111,
        115,
        127,
        98,
        157,
        171,
        144,
        93,
        173
      ],
      "itunes_id": 383084001,
      "publisher": "Pat Flynn",
      "thumbnail": "https://production.listennotes.com/podcasts/the-smart-passive-income-online-business-sF24owQHYWy-NDa6-ySp9kw.300x300.jpg",
      "is_claimed": false,
      "description": "\n      <p>Pat Flynn from The Smart Passive Income Blog reveals all of his online business and blogging strategies, income sources and killer marketing tips and tricks so you can be ahead of the curve with your online business or blog. Discover how you can create multiple passive income streams that work for you so that you can have the time and freedom to do what you love, whether it's traveling the world, or just living comfortably at home. Since 2008, he's been supporting his family with his many online businesses, and he's been openly sharing his wins, his losses, and all the lessons in between with the community of energetic but humble entrepreneurs who follow him. Self-proclaimed \"crash test dummy of online business\", you'll learn about building authority online, email marketing, building a team and outsourcing, content marketing, podcasting, search engine optimization, niche sites, social media strategies, how to get more traffic, creating online courses, affiliate marketing, and productivity tips so that you create something amazing without burning yourself out. It's a mix of interviews, special co-hosts and solo shows from Pat you're not going to want to miss. Hit subscribe, and get ready to change your life.</p><p><br></p>\n    ",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 70,
      "total_episodes": 685,
      "listennotes_url": "https://www.listennotes.com/c/499661f3589f42aaa1532673e0e0aedf/",
      "audio_length_sec": 2519,
      "explicit_content": false,
      "latest_episode_id": "677e8c0b94154ae083be8c88f612e03c",
      "latest_pub_date_ms": 1681455600000,
      "earliest_pub_date_ms": 1279551600655,
      "update_frequency_hours": 83,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "0da3baee05cc47e4b3222da775573efe",
      "rss": "https://rss.art19.com/the-investors-podcast",
      "type": "episodic",
      "email": "stig@theinvestorspodcast.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9yc3MuYXJ0MTkuY29tL3RoZS1pbnZlc3RvcnMtcG9kY2FzdA==",
        "spotify_url": "https://open.spotify.com/show/28RHOkXkuHuotUrkCdvlOP",
        "youtube_url": "https://www.youtube.com/user/BuffettsBooks",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "PrestonPysh",
        "facebook_handle": "WeStudyBillionaires",
        "amazon_music_url": "https://music.amazon.com/podcasts/b42b0171-d75e-4f9a-999f-da3a4db30f45/we-study-billionaires---the-investor%E2%80%99s-podcast-network",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/we-study-billionaires-the-investors-podcast-CrF62Mw39ov-ZuO23m60ePb.1400x1400.jpg",
      "title": "We Study Billionaires - The Investor\u2019s Podcast Network",
      "country": "United States",
      "website": "https://www.theinvestorspodcast.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        97,
        144,
        93,
        111,
        67,
        98
      ],
      "itunes_id": 928933489,
      "publisher": "The Investor's Podcast Network",
      "thumbnail": "https://production.listennotes.com/podcasts/we-study-billionaires-the-investors-podcast-xPmzOS9Y4lQ-ZuO23m60ePb.300x300.jpg",
      "is_claimed": false,
      "description": "\n      <p>We interview and study famous financial billionaires, including Warren Buffett, Ray Dalio, and Howard Marks, and teach you what we learn and how you can apply their investment strategies in the stock market.</p><p>We Study Billionaires is the largest stock investing podcast show in the world with 100,000,000+ downloads and is hosted by Stig Brodersen, Trey Lockerbie, and Clay Finck.</p><p>This podcast also includes the Richer Wiser Happier series hosted by best-selling author William Green. William regularly interviews legendary investors such as Mohnish Pabrai and Guy Spier, exploring what they can teach us about how to succeed in markets and life.</p><p>And finally, our Bitcoin Fundamentals series is hosted by Preston Pysh, where he interviews prominent figures in the Bitcoin and macroeconomic space. To learn more about TIP, you can visit&nbsp;<a href=\"http://theinvestorspodcast.com/\" rel=\"noopener noreferrer\" target=\"_blank\">theinvestorspodcast.com</a>&nbsp;or subscribe to our free daily newsletter&nbsp;<a href=\"https://www.theinvestorspodcast.com/westudymarkets\" rel=\"noopener noreferrer\" target=\"_blank\">here</a>.</p>\n    ",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 70,
      "total_episodes": 719,
      "listennotes_url": "https://www.listennotes.com/c/0da3baee05cc47e4b3222da775573efe/",
      "audio_length_sec": 3380,
      "explicit_content": false,
      "latest_episode_id": "7e7ff753095348109cc4183a588da9e5",
      "latest_pub_date_ms": 1681603200000,
      "earliest_pub_date_ms": 1411981990704,
      "update_frequency_hours": 43,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "a10d3bea3ffc40329727291321721c11",
      "rss": "https://feeds.megaphone.fm/TPG1669083856",
      "type": "episodic",
      "email": "listen@thepodglomerate.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5tZWdhcGhvbmUuZm0vVFBHMTY2OTA4Mzg1Ng==",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/money-rehab-with-nicole-lapin-money-news-ixsLZayFUCK-AvJIC3_u-j8.1400x1400.jpg",
      "title": "Money Rehab with Nicole Lapin",
      "country": "United States",
      "website": "https://moneynewsnetwork.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        111,
        181,
        67
      ],
      "itunes_id": 1559564016,
      "publisher": "Money News Network",
      "thumbnail": "https://production.listennotes.com/podcasts/money-rehab-with-nicole-lapin-money-news-v24RloNcmpf-AvJIC3_u-j8.300x300.jpg",
      "is_claimed": false,
      "description": "Ever notice that we will talk about everything before we talk about money? Sex? No problem. Politics? Bring it on. Money? Totally taboo. But not for long! Nicole Lapin\u2014 the only financial expert you don\u2019t need a dictionary to understand, New York Times best selling author of Rich Bitch, and host of Money Rehab\u2014 is here to rehab your wallet, so you can get your financial life together once and for all. Episodes are just ten minutes-ish... no frills, just bite-sized tips and tricks so you don\u2019t waste any time. And Nicole wants to hear from YOU! Email the money questions you want answered to MoneyRehab@NicoleLapin.com and Nicole will help\u2013and you could even join Nicole on the show for a one-on-one intervention.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 69,
      "total_episodes": 481,
      "listennotes_url": "https://www.listennotes.com/c/a10d3bea3ffc40329727291321721c11/",
      "audio_length_sec": 896,
      "explicit_content": true,
      "latest_episode_id": "7a81dadbe6cf4e0598a155c8308f980f",
      "latest_pub_date_ms": 1681714800000,
      "earliest_pub_date_ms": 1616593020458,
      "update_frequency_hours": 33,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "13a7957aeac34e1c9e004f2a2ced5fb0",
      "rss": "https://feeds.megaphone.fm/pivot",
      "type": "episodic",
      "email": "pivot@voxmedia.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5tZWdhcGhvbmUuZm0vcGl2b3Q=",
        "spotify_url": "https://open.spotify.com/show/4MU3RFGELZxPT9XHVwTNPR",
        "youtube_url": "",
        "linkedin_url": "https://www.linkedin.com/company/re-code-news/",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "recode",
        "facebook_handle": "RecodeDotNet",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/pivot-new-york-magazine-b0XsOSV7WDZ-YyJxq4Dbk67.1400x1400.jpg",
      "title": "Pivot",
      "country": "United States",
      "website": null,
      "language": "English",
      "genre_ids": [
        99,
        131,
        97,
        157,
        171,
        94,
        127,
        93,
        67
      ],
      "itunes_id": 1073226719,
      "publisher": "New York Magazine",
      "thumbnail": "https://production.listennotes.com/podcasts/pivot-new-york-magazine-L2FeZNEqKst-YyJxq4Dbk67.300x300.jpg",
      "is_claimed": false,
      "description": "Every Tuesday and Friday, tech journalist Kara Swisher and NYU Professor Scott Galloway offer sharp, unfiltered insights into the biggest stories in tech, business, and politics. They make bold predictions, pick winners and losers, and bicker and banter like no one else. After all, with great power comes great scrutiny. From New York Magazine and the Vox Media Podcast Network.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 69,
      "total_episodes": 434,
      "listennotes_url": "https://www.listennotes.com/c/13a7957aeac34e1c9e004f2a2ced5fb0/",
      "audio_length_sec": 3336,
      "explicit_content": false,
      "latest_episode_id": "429687c9391440d9b5b0b0daf20a49c4",
      "latest_pub_date_ms": 1681466400000,
      "earliest_pub_date_ms": 1537812480412,
      "update_frequency_hours": 77,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "f4a7bdbef7a84fd0b4a712b70a3c5ec5",
      "rss": "https://choosefi.libsyn.com/rss",
      "type": "episodic",
      "email": "feedback@choosefi.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9jaG9vc2VmaS5saWJzeW4uY29tL3Jzcw==",
        "spotify_url": "",
        "youtube_url": "https://www.youtube.com/choosefi",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "choosefi",
        "facebook_handle": "ChooseFi",
        "amazon_music_url": "",
        "instagram_handle": "choosefiradio"
      },
      "image": "https://production.listennotes.com/podcasts/choosefi-jonathan-mendonsa-brad-barrett-Xb8c9pQA_y--e8_g1GAYHIj.1400x1400.jpg",
      "title": "ChooseFI",
      "country": "United States",
      "website": "https://www.choosefi.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        93,
        97,
        122,
        123,
        127,
        129,
        98,
        144
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
      "listen_score": 69,
      "total_episodes": 594,
      "listennotes_url": "https://www.listennotes.com/c/f4a7bdbef7a84fd0b4a712b70a3c5ec5/",
      "audio_length_sec": 3358,
      "explicit_content": false,
      "latest_episode_id": "9b6878be290243b5b323f8a1a5ba5c23",
      "latest_pub_date_ms": 1681707600000,
      "earliest_pub_date_ms": 1482062785588,
      "update_frequency_hours": 167,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "c73271d55ffa4e2d9b529220072fbd79",
      "rss": "https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/3e7f11c6-1170-40a0-be58-ae330037e2f5/dea7cb4c-cbee-49ce-83f0-ae330037e303/podcast.rss",
      "type": "episodic",
      "email": "michael@earnyourleisure.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly93d3cub21ueWNvbnRlbnQuY29tL2QvcGxheWxpc3QvZTczYzk5OGUtNmU2MC00MzJmLTg2MTAtYWUyMTAxNDBjNWIxLzNlN2YxMWM2LTExNzAtNDBhMC1iZTU4LWFlMzMwMDM3ZTJmNS9kZWE3Y2I0Yy1jYmVlLTQ5Y2UtODNmMC1hZTMzMDAzN2UzMDMvcG9kY2FzdC5yc3M=",
        "spotify_url": "https://open.spotify.com/show/2S4tSSlT71Z5i8Dt1vlDJc",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/earn-your-leisure-eyl-network--AFWvtrYomD-CSRy4Lz625Y.1400x1400.jpg",
      "title": "Earn Your Leisure",
      "country": "United States",
      "website": "https://redcircle.com/shows/earn-your-leisure7962?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        93
      ],
      "itunes_id": 1450211392,
      "publisher": "EYL Network",
      "thumbnail": "https://production.listennotes.com/podcasts/earn-your-leisure-eyl-network-Ni5dRWAQFJc-CSRy4Lz625Y.300x300.jpg",
      "is_claimed": false,
      "description": "<p>Welcome to The Earn Your Leisure Podcast. Rashad Bilal and Troy Millings will be your host. Earn Your Leisure will be giving you behind the scenes financial views into the entertainment and sports industries as well as highlighting back stories of entrepreneurs. We will also be breaking down business models and examining the latest trends in finance. Earn Your Leisure is a college business class mixed with pop culture. We blend the two together for a unique and exciting look into the world of business. Let\u2019s go!! #earnyourleisurepodcast</p>",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 69,
      "total_episodes": 591,
      "listennotes_url": "https://www.listennotes.com/c/c73271d55ffa4e2d9b529220072fbd79/",
      "audio_length_sec": 2549,
      "explicit_content": false,
      "latest_episode_id": "bf34693226ea4eb8a8ca90022bc54475",
      "latest_pub_date_ms": 1681662600000,
      "earliest_pub_date_ms": 1548186120509,
      "update_frequency_hours": 23,
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
        "spotify_url": "https://open.spotify.com/show/5z7TqC6tll8egI9prMqXhd",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "AmyPorterfield",
        "facebook_handle": "AmyPorterfield",
        "amazon_music_url": "",
        "instagram_handle": "amyporterfield"
      },
      "image": "https://production.listennotes.com/podcasts/online-marketing-made-easy-with-amy-HmKNg8E7VI0-jXUyf4vBV20.1400x1400.jpg",
      "title": "Online Marketing Made Easy with Amy Porterfield",
      "country": "United States",
      "website": "https://amyporterfield.com/category/podcast/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        97,
        94,
        157,
        93,
        173
      ],
      "itunes_id": 594703545,
      "publisher": "Amy Porterfield",
      "thumbnail": "https://production.listennotes.com/podcasts/online-marketing-made-easy-with-amy-yMjTufCWtoa-jXUyf4vBV20.300x300.jpg",
      "is_claimed": false,
      "description": "Ever wish you had a business mentor with over a decade of experience whispering success secrets in your ear? That\u2019s exactly what you\u2019ll get when you tune into the top-ranked Online Marketing Made Easy Podcast with your host, 9 to 5er turned CEO of a multi-million dollar business & NY Times Best Selling Author, Amy Porterfield. Her specialty? Breaking down big ideas and strategies into actionable step-by-step processes designed to get you results with a whole lot less stress. Tune in, get inspired, and get ready to discover why hundreds of thousands of online business owners turn to Amy for guidance when it comes to all things online business including digital courses, list building, social media, content, webinars, and so much more. Whether you're a budding entrepreneur, have a comfy side-hustle, or are looking to take your business to the next level, each episode is designed to help you take immediate action on the most important strategies for starting and growing your online business today.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 69,
      "total_episodes": 605,
      "listennotes_url": "https://www.listennotes.com/c/fbecfdd4116e4e7a954bd6bc4cb0b406/",
      "audio_length_sec": 2282,
      "explicit_content": false,
      "latest_episode_id": "a7240cd87ceb4f66baaf21fff6f15167",
      "latest_pub_date_ms": 1681369260000,
      "earliest_pub_date_ms": 1358200867587,
      "update_frequency_hours": 74,
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
            "description": "Podcast id, which can be used to further fetch detailed podcast metadata via `GET /podcasts/{id}`."
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
                "example": "https://podcasts.google.com/feed/aHR0cHM6Ly9yc3MuYXJ0MTkuY29tL2pvaG4tc29sb21vbi1yZXBvcnRz",
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
              "amazon_music_url": {
                "type": "string",
                "example": "https://music.amazon.com/podcasts/6fc6d683-9ef3-4850-9c35-8e8b1a42a147/the-lock-sportscast",
                "description": "Amazon Music url for this podcast"
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
          "audio_length_sec": {
            "type": "integer",
            "example": 1291,
            "description": "Average audio length of all episodes of this podcast. In seconds."
          },
          "explicit_content": {
            "type": "boolean",
            "example": false,
            "description": "Whether this podcast contains explicit language."
          },
          "latest_episode_id": {
            "type": "string",
            "example": "d057092e57cc4ced80e0efaa196593d9",
            "description": "The id of the most recently published episode of this podcast, which can be used to further fetch detailed episode metadata via `GET /episodes/{id}`."
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
          "update_frequency_hours": {
            "type": "integer",
            "example": 168,
            "description": "How frequently does this podcast release a new episode? In hours. For example, if the value is 166, then it's every 166 hours (or weekly)."
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
      "type": "boolean",
      "example": true
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
    "al": "Albania",
    "am": "Armenia",
    "ar": "Argentina",
    "at": "Austria",
    "au": "Australia",
    "az": "Azerbaijan",
    "be": "Belgium",
    "bg": "Bulgaria",
    "bh": "Bahrain",
    "bn": "Brunei Darussalam",
    "bo": "Bolivia",
    "br": "Brazil",
    "by": "Belarus",
    "bz": "Belize",
    "ca": "Canada",
    "ch": "Switzerland",
    "cl": "Chile",
    "cn": "China",
    "co": "Colombia",
    "cr": "Costa Rica",
    "cz": "Czech Republic",
    "de": "Germany",
    "dk": "Denmark",
    "do": "Dominican Republic",
    "dz": "Algeria",
    "ec": "Ecuador",
    "ee": "Estonia",
    "eg": "Egypt",
    "es": "Spain",
    "fi": "Finland",
    "fr": "France",
    "gb": "United Kingdom",
    "gr": "Greece",
    "gt": "Guatemala",
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
    "kr": "South Korea",
    "kw": "Kuwait",
    "kz": "Kazakhstan",
    "lb": "Lebanon",
    "lt": "Lithuania",
    "lu": "Luxembourg",
    "lv": "Latvia",
    "mk": "Macedonia",
    "mn": "Mongolia",
    "mo": "Macau",
    "mt": "Malta",
    "mx": "Mexico",
    "my": "Malaysia",
    "ni": "Nicaragua",
    "nl": "Netherlands",
    "no": "Norway",
    "nz": "New Zealand",
    "om": "Oman",
    "pa": "Panama",
    "pe": "Peru",
    "ph": "Philippines",
    "pk": "Pakistan",
    "pl": "Poland",
    "pt": "Portugal",
    "py": "Paraguay",
    "qa": "Qatar",
    "ro": "Romania",
    "ru": "Russia",
    "sa": "Saudi Arabia",
    "se": "Sweden",
    "sg": "Singapore",
    "si": "Slovenia",
    "sk": "Slovakia",
    "sv": "El Salvador",
    "th": "Thailand",
    "tn": "Tunisia",
    "tr": "Turkey",
    "tw": "Taiwan",
    "ua": "Ukraine",
    "us": "United States",
    "uy": "Uruguay",
    "uz": "Uzbekistan",
    "ve": "Venezuela",
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
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-tim-ferriss-show-5-minute-podcast-mpqMa73u08D-mYx8LcSkhz1.1400x1400.jpg",
      "title": "The Tim Ferriss Show | 5 minute podcast summaries",
      "country": "United States",
      "website": "https://www.spreaker.com/show/the-tim-ferriss-show-5-minute-podcast-su?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        111,
        181,
        67
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
      "listen_score": 34,
      "total_episodes": 12,
      "listennotes_url": "https://www.listennotes.com/c/7060b5d48b3440ba9668f9af2a90fa7f/",
      "audio_length_sec": 221,
      "explicit_content": false,
      "latest_episode_id": "9163fe8fdfc34710af8d41b575023e07",
      "latest_pub_date_ms": 1625881044000,
      "earliest_pub_date_ms": 1619229600011,
      "update_frequency_hours": 165,
      "listen_score_global_rank": "3%"
    },
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
        "amazon_music_url": "",
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
      "listen_score": 36,
      "total_episodes": 64,
      "listennotes_url": "https://www.listennotes.com/c/805535e1de5a4c7991f4f323e82ce9e7/",
      "audio_length_sec": 1695,
      "explicit_content": false,
      "latest_episode_id": "99eb35864e2242a480f4709ded9471b5",
      "latest_pub_date_ms": 1502287200000,
      "earliest_pub_date_ms": 1453246535000,
      "update_frequency_hours": 327,
      "listen_score_global_rank": "2.5%"
    },
    {
      "id": "d1344e580523433e9e7b6d3d17579c68",
      "rss": "https://feeds.acast.com/public/shows/eddbcc04-6cf8-4a7b-8bf7-f29cb306da8c",
      "type": "episodic",
      "email": null,
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5hY2FzdC5jb20vcHVibGljL3Nob3dzL2VkZGJjYzA0LTZjZjgtNGE3Yi04YmY3LWYyOWNiMzA2ZGE4Yw==",
        "spotify_url": "",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-guinea-pig-the-guinea-pig-podcast-f71pCJnAd8Q-bpDvSg1QWR4.1400x1400.jpg",
      "title": "The Guinea Pig",
      "country": "United States",
      "website": null,
      "language": "English",
      "genre_ids": [
        90,
        107,
        111,
        67
      ],
      "itunes_id": 1453993716,
      "publisher": "The Guinea Pig Podcast",
      "thumbnail": "https://production.listennotes.com/podcasts/the-guinea-pig-the-guinea-pig-podcast-eQwm9xXzlPv-bpDvSg1QWR4.300x300.jpg",
      "is_claimed": false,
      "description": "Leading surgeon and founder of cult brand MZ SKIN, Dr&nbsp;Maryam&nbsp;Zamani and ex-Vogue editor-at-Large, Fiona Golfar&nbsp;present&nbsp;The Guinea Pig&nbsp;podcast!Fiona and&nbsp;Maryam&nbsp;share their honest opinions and hilarious real-life experiences and give essential safety advice to those considering any kind of aesthetic procedure.For adults only, this bi-weekly podcast covers the latest aesthetic treatment reviews by the resident guinea pig, Fiona Golfar, supported by necessary medical advice and insights from Dr&nbsp;Maryam&nbsp;Zamani.Fiona tries the treatments - so you don\u2019t have to -&nbsp;allowing the listener to decide for themselves once they are armed with the necessary knowledge, questions to ask and potential risks.&nbsp;Maryam&nbsp;and Fiona chat openly and candidly about products and procedures aided by experts & high-profile friends to offer advice and insights to anyone considering a treatment.So if you, or someone you know is thinking of changing their&nbsp;moisturiser, dealing with tired looking eyes, or even having a neck-lift, The Guinea Pig is here to help you!<br /><hr><p style='color:grey; font-size:0.75em;'> Hosted on Acast. See <a style='color:grey;' target='_blank' rel='noopener noreferrer' href='https://acast.com/privacy'>acast.com/privacy</a> for more information.</p>",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 40,
      "total_episodes": 70,
      "listennotes_url": "https://www.listennotes.com/c/d1344e580523433e9e7b6d3d17579c68/",
      "audio_length_sec": 1715,
      "explicit_content": true,
      "latest_episode_id": "7ce4a41ab7034fb2936646236b392dc0",
      "latest_pub_date_ms": 1613008800000,
      "earliest_pub_date_ms": 1550841504069,
      "update_frequency_hours": 319,
      "listen_score_global_rank": "1.5%"
    },
    {
      "id": "f9d5885d7cf7485d891e82dea3186640",
      "rss": "https://rss.art19.com/how-i-built-this",
      "type": "episodic",
      "email": "iwonder@wondery.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9yc3MuYXJ0MTkuY29tL2hvdy1pLWJ1aWx0LXRoaXM=",
        "spotify_url": "https://open.spotify.com/show/6E709HRH7XaiZrMfgtNCun",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "HowIBuiltThis",
        "facebook_handle": "howibuiltthis",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/how-i-built-this-with-guy-raz-guy-raz-wondery-7krpVtcCzMB-UC0qH23iP9T.1400x1400.jpg",
      "title": "How I Built This with Guy Raz",
      "country": "United States",
      "website": "https://wondery.com/shows/how-i-built-this/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        157,
        90,
        173,
        94,
        106,
        127,
        93,
        67,
        171
      ],
      "itunes_id": 1150510297,
      "publisher": "Guy Raz | Wondery",
      "thumbnail": "https://production.listennotes.com/podcasts/how-i-built-this-with-guy-raz-guy-raz-wondery--t38KFIqlAi-UC0qH23iP9T.300x300.jpg",
      "is_claimed": false,
      "description": "\n      <p>Guy Raz interviews the world\u2019s best-known entrepreneurs to learn how they built their iconic brands. In each episode, founders reveal deep, intimate moments of doubt and failure, and share insights on their eventual success.&nbsp;<em>How I Built This&nbsp;</em>is a master-class on innovation, creativity, leadership and how to navigate challenges of all kinds.</p><p>New episodes on Mondays and Thursdays for free. Listen 1-week early and to all episodes ad-free with Wondery+ or Amazon Music with a Prime membership or Amazon Music Unlimited subscription.</p><p>Get your How I Built This merch at <a href=\"https://wonderyshop.com/pages/howibuiltthis ?utm_source=hibt-podcast&amp;utm_medium=referral&amp;utm_campaign=hibt-description\" rel=\"noopener noreferrer\" target=\"_blank\">WonderyShop.com/HowIBuiltThis</a></p>\n    ",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 83,
      "total_episodes": 512,
      "listennotes_url": "https://www.listennotes.com/c/f9d5885d7cf7485d891e82dea3186640/",
      "audio_length_sec": 2970,
      "explicit_content": false,
      "latest_episode_id": "b56382eaef9346d588e5b22510f64e34",
      "latest_pub_date_ms": 1681715400000,
      "earliest_pub_date_ms": 1472828160488,
      "update_frequency_hours": 83,
      "listen_score_global_rank": "0.01%"
    },
    {
      "id": "fe6864628066420c8103c94e91e72eb3",
      "rss": "https://anchor.fm/s/f39a864/podcast/rss",
      "type": "episodic",
      "email": "justin.schnell@vaynermedia.com",
      "extra": {
        "url1": "https://medium.com/@garyvee",
        "url2": "https://www.snapchat.com/add/garyvee",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cDovL2Fza2dhcnl2ZWUuZ2FyeXZlZS5saWJzeW5wcm8uY29tL3Jzcw==",
        "spotify_url": "https://open.spotify.com/show/6SZVsPIxPfVs6aavqM1peY",
        "youtube_url": "https://www.youtube.com/user/garyvaynerchuk",
        "linkedin_url": "https://www.linkedin.com/in/garyvaynerchuk/",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "garyvee",
        "facebook_handle": "gary",
        "amazon_music_url": "https://music.amazon.com/podcasts/97113abf-5c18-4c7e-8d2b-efcf161f4848/the-garyvee-audio-experience",
        "instagram_handle": "garyvee"
      },
      "image": "https://production.listennotes.com/podcasts/the-garyvee-audio-experience-gary-vaynerchuk-KMaejZIN9lv-X0Dfm7O_o3y.1400x1400.jpg",
      "title": "The GaryVee Audio Experience",
      "country": "United States",
      "website": "http://www.garyvaynerchuk.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        95,
        127,
        169,
        78,
        157,
        97,
        98,
        173,
        93,
        171,
        67
      ],
      "itunes_id": 928159684,
      "publisher": "Gary Vaynerchuk",
      "thumbnail": "https://production.listennotes.com/podcasts/the-garyvee-audio-experience-gary-vaynerchuk-LK-6lUgsYyT-X0Dfm7O_o3y.300x300.jpg",
      "is_claimed": false,
      "description": "Welcome to The GaryVee Audio Experience, hosted by entrepreneur, CEO, investor, content creator, and public speaker Gary Vaynerchuk. On this podcast you'll find a mix of the #AskGaryVee show episodes, keynote speeches on marketing and business, segments from my DAILYVEE video series, interviews and fireside chats I've given, as well as new and current thoughts I record originally for this audio experience!\n\n",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 80,
      "total_episodes": 2581,
      "listennotes_url": "https://www.listennotes.com/c/fe6864628066420c8103c94e91e72eb3/",
      "audio_length_sec": 1843,
      "explicit_content": true,
      "latest_episode_id": "6fe820a7280f47258b30e6cba01ffc10",
      "latest_pub_date_ms": 1681744068000,
      "earliest_pub_date_ms": 1412179202542,
      "update_frequency_hours": 22,
      "listen_score_global_rank": "0.01%"
    },
    {
      "id": "9f6ee51adfb046cc9936490abd2666ce",
      "rss": "https://feeds.simplecast.com/AAvup9Zz",
      "type": "episodic",
      "email": "podcast@schoolofgreatness.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5zaW1wbGVjYXN0LmNvbS9BQXZ1cDlaeg==",
        "spotify_url": "https://open.spotify.com/show/07GQhOZboEZOE1ysnFLipT",
        "youtube_url": "https://www.youtube.com/user/lewishowes",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "lewishowes",
        "facebook_handle": "lewishowes",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-school-of-greatness-lewis-howes-Ggb9PDwVr63-H1zdqljixbp.1400x1400.jpg",
      "title": "The School of Greatness",
      "country": "United States",
      "website": "http://lewishowes.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        77,
        78,
        90,
        89,
        97,
        94,
        171,
        93,
        181,
        111,
        91,
        67,
        88
      ],
      "itunes_id": 596047499,
      "publisher": "Lewis Howes",
      "thumbnail": "https://production.listennotes.com/podcasts/the-school-of-greatness-lewis-howes-jyfMSXd41U8-H1zdqljixbp.300x300.jpg",
      "is_claimed": false,
      "description": "Lewis Howes is a New York Times best-selling author, 2x All-American athlete, keynote speaker, and entrepreneur. The School of Greatness shares inspiring interviews from the most successful people on the planet\u2014world-renowned leaders in business, entertainment, sports, science, health, and literature\u2014to inspire YOU to unlock your inner greatness and live your best life.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 78,
      "total_episodes": 1425,
      "listennotes_url": "https://www.listennotes.com/c/9f6ee51adfb046cc9936490abd2666ce/",
      "audio_length_sec": 3111,
      "explicit_content": false,
      "latest_episode_id": "b0bc289e97c24f77bc62715b73364e2b",
      "latest_pub_date_ms": 1681714800000,
      "earliest_pub_date_ms": 1358928001418,
      "update_frequency_hours": 47,
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
        "spotify_url": "https://open.spotify.com/show/25wgHxrQY2e7WNeV4UtECI",
        "youtube_url": "https://www.youtube.com/channel/UCXfzpliAfdjParawJljHo2g",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "johnleedumas",
        "facebook_handle": "johnleedumas1",
        "amazon_music_url": "https://music.amazon.com/podcasts/4728a7fc-731f-4b18-971b-85b0b8c2e784/entrepreneurs-on-fire",
        "instagram_handle": "johnleedumas"
      },
      "image": "https://production.listennotes.com/podcasts/entrepreneurs-on-fire-john-lee-dumas-of-DekxRsp0tNA-1WOhT7u6VQb.1400x1400.jpg",
      "title": "Entrepreneurs on Fire",
      "country": "United States",
      "website": "https://www.eofire.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        88,
        111,
        90,
        94,
        97,
        169,
        157,
        173,
        93,
        67,
        171
      ],
      "itunes_id": 564001633,
      "publisher": "John Lee Dumas of EOFire",
      "thumbnail": "https://production.listennotes.com/podcasts/entrepreneurs-on-fire-john-lee-dumas-of-o7xODP0r6-Q-1WOhT7u6VQb.300x300.jpg",
      "is_claimed": true,
      "description": "John Lee Dumas is the founder and host of the award winning podcast, Entrepreneurs On Fire. With over 100 million listens of his 3000+ episodes, JLD has turned Entrepreneurs On Fire into a media empire that generates over a million listens every month and 7-figures of NET annual revenue 8-years in a row. His first traditionally published book, The Common Path to Uncommon Success is the modern day version of Think and Grow Rich with a revolutionary 17-step roadmap to financial freedom and fulfillment. Learn more at UncommonSuccessBook.com",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 69,
      "total_episodes": 3322,
      "listennotes_url": "https://www.listennotes.com/c/a409b8bb93f44054a7be2d6b30843899/",
      "audio_length_sec": 1815,
      "explicit_content": false,
      "latest_episode_id": "48338dd4d0fa4c8e9f6587dd48dd9d2a",
      "latest_pub_date_ms": 1681720200000,
      "earliest_pub_date_ms": 1348297203313,
      "update_frequency_hours": 24,
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
        "spotify_url": "https://open.spotify.com/show/7wjv5MRCXWXImqTFhcufLy",
        "youtube_url": "https://www.youtube.com/user/smartpassiveincome",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "patflynn",
        "facebook_handle": "smartpassiveincome",
        "amazon_music_url": "https://music.amazon.com/podcasts/341282a1-cba9-4188-aa58-e09a51ccaa87/the-smart-passive-income-online-business-and-blogging-podcast",
        "instagram_handle": "patflynn"
      },
      "image": "https://production.listennotes.com/podcasts/the-smart-passive-income-online-business-jN-aR6qdYuo-NDa6-ySp9kw.1400x1400.jpg",
      "title": "The Smart Passive Income Online Business and Blogging Podcast",
      "country": "United States",
      "website": "https://art19.com/shows/smart-passive-income-podcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        97,
        67,
        94,
        111,
        115,
        127,
        98,
        157,
        171,
        144,
        93,
        173
      ],
      "itunes_id": 383084001,
      "publisher": "Pat Flynn",
      "thumbnail": "https://production.listennotes.com/podcasts/the-smart-passive-income-online-business-sF24owQHYWy-NDa6-ySp9kw.300x300.jpg",
      "is_claimed": false,
      "description": "\n      <p>Pat Flynn from The Smart Passive Income Blog reveals all of his online business and blogging strategies, income sources and killer marketing tips and tricks so you can be ahead of the curve with your online business or blog. Discover how you can create multiple passive income streams that work for you so that you can have the time and freedom to do what you love, whether it's traveling the world, or just living comfortably at home. Since 2008, he's been supporting his family with his many online businesses, and he's been openly sharing his wins, his losses, and all the lessons in between with the community of energetic but humble entrepreneurs who follow him. Self-proclaimed \"crash test dummy of online business\", you'll learn about building authority online, email marketing, building a team and outsourcing, content marketing, podcasting, search engine optimization, niche sites, social media strategies, how to get more traffic, creating online courses, affiliate marketing, and productivity tips so that you create something amazing without burning yourself out. It's a mix of interviews, special co-hosts and solo shows from Pat you're not going to want to miss. Hit subscribe, and get ready to change your life.</p><p><br></p>\n    ",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 70,
      "total_episodes": 685,
      "listennotes_url": "https://www.listennotes.com/c/499661f3589f42aaa1532673e0e0aedf/",
      "audio_length_sec": 2519,
      "explicit_content": false,
      "latest_episode_id": "677e8c0b94154ae083be8c88f612e03c",
      "latest_pub_date_ms": 1681455600000,
      "earliest_pub_date_ms": 1279551600655,
      "update_frequency_hours": 83,
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
            "description": "Podcast id, which can be used to further fetch detailed podcast metadata via `GET /podcasts/{id}`."
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
                "example": "https://podcasts.google.com/feed/aHR0cHM6Ly9yc3MuYXJ0MTkuY29tL2pvaG4tc29sb21vbi1yZXBvcnRz",
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
              "amazon_music_url": {
                "type": "string",
                "example": "https://music.amazon.com/podcasts/6fc6d683-9ef3-4850-9c35-8e8b1a42a147/the-lock-sportscast",
                "description": "Amazon Music url for this podcast"
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
          "audio_length_sec": {
            "type": "integer",
            "example": 1291,
            "description": "Average audio length of all episodes of this podcast. In seconds."
          },
          "explicit_content": {
            "type": "boolean",
            "example": false,
            "description": "Whether this podcast contains explicit language."
          },
          "latest_episode_id": {
            "type": "string",
            "example": "d057092e57cc4ced80e0efaa196593d9",
            "description": "The id of the most recently published episode of this podcast, which can be used to further fetch detailed episode metadata via `GET /episodes/{id}`."
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
          "update_frequency_hours": {
            "type": "integer",
            "example": 168,
            "description": "How frequently does this podcast release a new episode? In hours. For example, if the value is 166, then it's every 166 hours (or weekly)."
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
      "image": "https://production.listennotes.com/podcasts/the-first-mint-podcast-the-first-mint-Gr3QBqaS-co-NuBwOlnV0bt.1400x1400.jpg",
      "title": "Roham",
      "podcast": {
        "id": "fbdf83bb46ac4e0b9e807991719e210f",
        "image": "https://production.listennotes.com/podcasts/the-first-mint-podcast-the-first-mint-Gr3QBqaS-co-NuBwOlnV0bt.1400x1400.jpg",
        "title": "The First Mint Podcast",
        "publisher": "The First Mint",
        "thumbnail": "https://production.listennotes.com/podcasts/the-first-mint-podcast-the-first-mint-SyV02rj4mN5-NuBwOlnV0bt.300x300.jpg",
        "listen_score": 47,
        "listennotes_url": "https://www.listennotes.com/c/fbdf83bb46ac4e0b9e807991719e210f/",
        "listen_score_global_rank": "1%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/the-first-mint-podcast-the-first-mint-SyV02rj4mN5-NuBwOlnV0bt.300x300.jpg",
      "description": "<p>Episode 83 of The First Mint.</p>\n<p>Roham.</p>\n<p>To kick off First Mint Fest, LG Doucet sat down with Roham Gharegozlou, the Founder &amp; CEO of Dapper Labs, the company behind NBA Top Shot and the Flow Blockchain.&nbsp;</p>",
      "pub_date_ms": 1628143512119,
      "guid_from_rss": "f148e49b-dfbf-4a94-8e3a-19bcb4ff1c17",
      "listennotes_url": "https://www.listennotes.com/e/8c9fcee265fc4f54bbca6afafcb8c28c/",
      "audio_length_sec": 3738,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/8c9fcee265fc4f54bbca6afafcb8c28c/#edit"
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
        "publisher": "CoinDesk",
        "thumbnail": "https://production.listennotes.com/podcasts/coindesk-reports-coindeskcom-vcYaEq5G_Ox-TElxWfYmVpQ.300x300.jpg",
        "listen_score": 28,
        "listennotes_url": "https://www.listennotes.com/c/188eb6965eb048469400414acb5749ae/",
        "listen_score_global_rank": "10%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/coindesk-reports/money-reimagined-inside-what-ezmdK02jRlc-CHxWD0gME75.300x300.jpg",
      "description": "<p>At the end of a high-energy week in the burgeoning digital art world, \u201cMoney Reimagined\u201d brings you the third and (for now) final edition of our NFT series.&nbsp;</p><p>In between recording this episode and publishing it two days later, a non-fungible token attached to a piece of digital art sold for a whopping $69.3 million. The sale, orchestrated by Christie\u2019s, turned the digital creator known as Beeple into the third-highest paid living artist. It also represented a high point in the media attention now swirling around this new, crypto-based technology.&nbsp;</p><p>So, it\u2019s appropriate we end on a note that grounds things in the reality of the technology and its potential to transform the creator economy generally, rather than being caught up in the celebrity story and media sensations. To do so, we talk with Roham Gharegozlou, the CEO and founder of Dapper Labs, the startup that in many respects is responsible for kicking off the entire NFT phenomenon.&nbsp;</p><p>We talk about the early days when Dapper created the ERC-721 standard on Ethereum and launched the popular CryptoKitties program. We talk about why the team made the decision to build its own blockchain, known as Flow, and to migrate the business there away from Ethereum. And we talk about where this rapidly evolving industry, with its competing platforms and wild debates over rights and opportunities, is going.</p><p>Join us for the conversation.&nbsp;</p><p><br /></p><p><em>Image credit:&nbsp;</em>&nbsp;<a href=\"https://unsplash.com/@benjaminjsuter?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText\" rel=\"noopener noreferrer\" target=\"_blank\">Benjamin Suter</a>&nbsp;on&nbsp;<a href=\"https://unsplash.com/s/photos/basketball?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText\" rel=\"noopener noreferrer\" target=\"_blank\">Unsplash</a>,&nbsp;<em>modified by CoinDesk</em></p><p><br /></p><p><br /></p><p>See Privacy Policy at <a href=\"https://art19.com/privacy\" rel=\"noopener noreferrer\" target=\"_blank\">https://art19.com/privacy</a> and California Privacy Notice at <a href=\"https://art19.com/privacy#do-not-sell-my-info\" rel=\"noopener noreferrer\" target=\"_blank\">https://art19.com/privacy#do-not-sell-my-info</a>.</p>",
      "pub_date_ms": 1615573111245,
      "guid_from_rss": "gid://art19-episode-locator/V0/TIr9Oc1xT-lNsuHS68HF9xWQ3oPV6E8w41xzcI0Ebdg",
      "listennotes_url": "https://www.listennotes.com/e/9aaeb046a07042d09ca5214a94f999b4/",
      "audio_length_sec": 2692,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/9aaeb046a07042d09ca5214a94f999b4/#edit"
    },
    {
      "id": "2afa18fe81b64fae9a178ea4e6ea1b78",
      "link": "http://samsungnext.com/podcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/2afa18fe81b64fae9a178ea4e6ea1b78/",
      "image": "https://production.listennotes.com/podcasts/whats-next-samsung-next-BOU80jWegKh-kG8U3EdxHWo.1400x1400.jpg",
      "title": "Building blockchain collectibles with Dapper Labs founder Roham Gharegozlou",
      "podcast": {
        "id": "0615f79f64de4f1989d4ad1bac7cbc9e",
        "image": "https://production.listennotes.com/podcasts/whats-next-samsung-next-BOU80jWegKh-kG8U3EdxHWo.1400x1400.jpg",
        "title": "What's NEXT",
        "publisher": "Samsung NEXT",
        "thumbnail": "https://production.listennotes.com/podcasts/whats-next-samsung-next-RaNEz68Vhc0-kG8U3EdxHWo.300x300.jpg",
        "listen_score": 26,
        "listennotes_url": "https://www.listennotes.com/c/0615f79f64de4f1989d4ad1bac7cbc9e/",
        "listen_score_global_rank": "10%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/whats-next-samsung-next-RaNEz68Vhc0-kG8U3EdxHWo.300x300.jpg",
      "description": "<p>Welcome back to What\u2019s NEXT, the podcast exploring the technology of the future. This is the last in our series of conversations from the Web Summit conference last year. <br> <br>In this episode, Samsung NEXT\u2019s Haley Lancaster speaks with Roham Gharegozlou, the founder and CEO of Dapper Labs, which made CryptoKitties and a number of other decentralized apps. Roham speaks about the early success of CryptoKitties, how his company works with partners like the NBA and Ubisoft, and why Dapper Labs is building a new, developer-friendly blockchain platform called Flow. <br><br></p>",
      "pub_date_ms": 1580972400005,
      "guid_from_rss": "8efdfab2-46e8-11ea-9483-0e1facdaf5fd",
      "listennotes_url": "https://www.listennotes.com/e/2afa18fe81b64fae9a178ea4e6ea1b78/",
      "audio_length_sec": 851,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/2afa18fe81b64fae9a178ea4e6ea1b78/#edit"
    },
    {
      "id": "221ff88340b941148ad90749f0c745e7",
      "link": "https://foundersproject.inc.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/221ff88340b941148ad90749f0c745e7/",
      "image": "https://production.listennotes.com/podcasts/inc-founders-project-with-alexa-von-tobel-PQEWgmYsAyD-M25bgqtK8-I.1400x1400.jpg",
      "title": "Flashback Episode: How to Build Community Through Ownership with Roham Gharegozlou of Dapper Labs",
      "podcast": {
        "id": "0694a18b25354ce593c3aeba7fb94d67",
        "image": "https://production.listennotes.com/podcasts/inc-founders-project-with-alexa-von-tobel-PQEWgmYsAyD-M25bgqtK8-I.1400x1400.jpg",
        "title": "Inc. Founders Project with Alexa von Tobel ",
        "publisher": "Inc. Magazine",
        "thumbnail": "https://production.listennotes.com/podcasts/inc-founders-project-with-alexa-von-tobel-LOXAc3mvR86-M25bgqtK8-I.300x300.jpg",
        "listen_score": 38,
        "listennotes_url": "https://www.listennotes.com/c/0694a18b25354ce593c3aeba7fb94d67/",
        "listen_score_global_rank": "2%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/inc-founders-project-with-alexa-von-tobel-LOXAc3mvR86-M25bgqtK8-I.300x300.jpg",
      "description": "<p>If you've heard of NFTs (non-fungible tokens), it's likely thanks to the work of Roham Gharegozlou. Roham is the Co-Founder and CEO of Dapper Labs, the NFT company that has created some of the most viral brands out there, from CryptoKitties to NBA Top Shot. Through his venture studio Axiom Zen, he started looking into crypto back in 2014. With a mission to bring play to crypto, Dapper Labs has been named one of the most innovative gaming companies by Fast Company and has created some of the most broadly used applications in the history of crypto. Roham shares how NBA Top Shot scaled to over one million users, why he thinks of NFTs as the next evolution of social media, and why entrepreneurship requires a healthy balance of optimism and paranoia.\u00a0</p>",
      "pub_date_ms": 1655888400032,
      "guid_from_rss": "ff7cc4d0-f172-11ec-b560-e703d370d4d3",
      "listennotes_url": "https://www.listennotes.com/e/221ff88340b941148ad90749f0c745e7/",
      "audio_length_sec": 1792,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/221ff88340b941148ad90749f0c745e7/#edit"
    },
    {
      "id": "3a2016291aaa415abb9563bf8192ade7",
      "link": "https://foundersproject.inc.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/3a2016291aaa415abb9563bf8192ade7/",
      "image": "https://production.listennotes.com/podcasts/inc-founders-project-with-alexa-von-tobel-PQEWgmYsAyD-M25bgqtK8-I.1400x1400.jpg",
      "title": "How to Build Community Through Ownership with Roham Gharegozlou of Dapper Labs",
      "podcast": {
        "id": "0694a18b25354ce593c3aeba7fb94d67",
        "image": "https://production.listennotes.com/podcasts/inc-founders-project-with-alexa-von-tobel-PQEWgmYsAyD-M25bgqtK8-I.1400x1400.jpg",
        "title": "Inc. Founders Project with Alexa von Tobel ",
        "publisher": "Inc. Magazine",
        "thumbnail": "https://production.listennotes.com/podcasts/inc-founders-project-with-alexa-von-tobel-LOXAc3mvR86-M25bgqtK8-I.300x300.jpg",
        "listen_score": 38,
        "listennotes_url": "https://www.listennotes.com/c/0694a18b25354ce593c3aeba7fb94d67/",
        "listen_score_global_rank": "2%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/inc-founders-project-with-alexa-von-tobel-LOXAc3mvR86-M25bgqtK8-I.300x300.jpg",
      "description": "<p>If you've heard of NFTs (non-fungible tokens), it's likely thanks to the work of Roham Gharegozlou. Roham is the Co-Founder and CEO of Dapper Labs, the NFT company that has created some of the most viral brands out there, from CryptoKitties to NBA Top Shot. Through his venture studio Axiom Zen, he started looking into crypto back in 2014. With a mission to bring play to crypto, Dapper Labs has been named one of the most innovative gaming companies by Fast Company and has created some of the most broadly used applications in the history of crypto. Roham shares how NBA Top Shot scaled to over one million users, why he thinks of NFTs as the next evolution of social media, and why entrepreneurship requires a healthy balance of optimism and paranoia.\u00a0</p>",
      "pub_date_ms": 1646215200048,
      "guid_from_rss": "09eb05a6-996e-11ec-9f17-ef743a58b593",
      "listennotes_url": "https://www.listennotes.com/e/3a2016291aaa415abb9563bf8192ade7/",
      "audio_length_sec": 1792,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/3a2016291aaa415abb9563bf8192ade7/#edit"
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
        "listen_score": 73,
        "listennotes_url": "https://www.listennotes.com/c/0d362b13399240de97602ef614acdcbc/",
        "listen_score_global_rank": "0.05%"
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
    },
    {
      "id": "b03b9f59a5df4d31bf44e1828353c8e6",
      "link": "https://www.softwaredefinedinterviews.com/ma4?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/b03b9f59a5df4d31bf44e1828353c8e6/",
      "image": "https://production.listennotes.com/podcasts/software-defined-interviews-software-yFixmv_8KZq-y7KRi_flj8t.1400x1400.jpg",
      "title": "Misaligned Incentives Episode 4: You get what you pay for - compensating tech staff is often done poorly",
      "podcast": {
        "id": "13350cb77ad548bc8991dac9657f45b7",
        "image": "https://production.listennotes.com/podcasts/software-defined-interviews-software-yFixmv_8KZq-y7KRi_flj8t.1400x1400.jpg",
        "title": "Software Defined Interviews",
        "publisher": "Software Defined Talk",
        "thumbnail": "https://production.listennotes.com/podcasts/software-defined-interviews-software-N8fPcvt0JmU-y7KRi_flj8t.300x300.jpg",
        "listen_score": null,
        "listennotes_url": "https://www.listennotes.com/c/13350cb77ad548bc8991dac9657f45b7/",
        "listen_score_global_rank": null
      },
      "thumbnail": "https://production.listennotes.com/podcasts/software-defined-interviews-software-N8fPcvt0JmU-y7KRi_flj8t.300x300.jpg",
      "description": "<pre><code>    &lt;p&gt;We discuss compensation, particularly how people in the IT department (&amp;quot;developers,&amp;quot; etc.) are so disconnected from the actual business that compensating them based on business performance is near impossible. Not good if you&amp;#39;re an IT person and like money.&lt;/p&gt;\n</code></pre>\n\n<p>There&#39;s other types of comp. then money, obviously, and those are fine too. In particular, we discuss participation in open source and more recognition. But, still: money is the best.</p>",
      "pub_date_ms": 1594980000000,
      "guid_from_rss": "efb05656-d9ef-4fe7-b583-3c49d929fb6c",
      "listennotes_url": "https://www.listennotes.com/e/b03b9f59a5df4d31bf44e1828353c8e6/",
      "audio_length_sec": 3057,
      "explicit_content": true,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/b03b9f59a5df4d31bf44e1828353c8e6/#edit"
    },
    {
      "id": "653da187c8fc4d17adee39ecc64e0658",
      "link": null,
      "audio": "https://www.listennotes.com/e/p/653da187c8fc4d17adee39ecc64e0658/",
      "image": "https://production.listennotes.com/podcasts/she-did-it-her-way/sdh-476-im-doing-it-my-way-gZBesUx8hH_-OUp-kAj5It7.1400x1400.jpg",
      "title": "SDH 476: I'm Doing It My Way (Special Announcement) with Amanda Boleyn",
      "podcast": {
        "id": "baf59c165baf441d881b39ec3cc1f320",
        "image": "https://production.listennotes.com/podcasts/she-did-it-her-way-amanda-boleyn-m7n-RzQBvEC-jsD5bCh1vo2.1400x1400.jpg",
        "title": "She Did It Her Way",
        "publisher": "Amanda Boleyn ",
        "thumbnail": "https://production.listennotes.com/podcasts/she-did-it-her-way-amanda-boleyn-ck2Y4SdwDM1-jsD5bCh1vo2.300x300.jpg",
        "listen_score": 47,
        "listennotes_url": "https://www.listennotes.com/c/baf59c165baf441d881b39ec3cc1f320/",
        "listen_score_global_rank": "1%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/she-did-it-her-way/sdh-476-im-doing-it-my-way-36NVPdTkKzI-OUp-kAj5It7.300x300.jpg",
      "description": "<p>Hello my beautiful listeners! Welcome back to another episode of the She Did It Her Way podcast. This episode is going to be a little bit different in that I have some news to share and I am going to do it in a very full-circle way, joined by my very first podcast guest ever and dear friend, Shauna VanBogart.</p><p>This news has been some time in the making and while it certainly is bittersweet and definitely not the easiest to share it\u2019s important to remember that sometimes the things that aren\u2019t the easiest are actually the most necessary.\u00a0</p><p>The purpose of having Shauna on the show is that she will actually be interviewing me and pulling some things out of me, as opposed to me being on the other side of the mic, so to speak.\u00a0</p><p>I hope that this episode gives you permission to pivot, or potentially close a chapter that no longer feels aligned with you, no matter how challenging the transition may be. Especially when you know, in your gut, that it's time for a change.</p><p>As always, my beautiful friends, keep doing it your way.\u00a0<br />\u00a0</p><p>\u00a0</p><h2><strong>Insights:</strong></h2><ul><li><i>\u201cOh, she\u2019s gonna do this.\u201d</i></li><li><i>\u201cGo inward. Stay out of your head. Stay in your heart and your gut.\u201d</i></li></ul><p>\u00a0</p><h2><strong>Resources:</strong></h2><ul><li>Check out how you can use <a href=\"https://shediditherway.com/podia\">Podia</a> in your business</li><li>Get more info about working with <a href=\"https://shaunavanbogart.com\">Shauna VanBogart</a></li></ul>",
      "pub_date_ms": 1640001600000,
      "guid_from_rss": "4ba9006a-73e0-4e78-969e-251495a7bd44",
      "listennotes_url": "https://www.listennotes.com/e/653da187c8fc4d17adee39ecc64e0658/",
      "audio_length_sec": 3002,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/653da187c8fc4d17adee39ecc64e0658/#edit"
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
            "description": "Episode id, which can be used to further fetch detailed episode metadata via `GET /episodes/{id}`."
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
                "description": "Podcast id, which can be used to further fetch detailed podcast metadata via `GET /podcasts/{id}`."
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
      "image": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-YDiw-IQe4S8-aZPn3Ic47rx.1400x1400.jpg",
      "title": "35: Don\u2019t Make Your Landlord Rich",
      "podcast": {
        "id": "68faf62be97149c280ebcc25178aa731",
        "image": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-YDiw-IQe4S8-aZPn3Ic47rx.1400x1400.jpg",
        "title": "Business Unusual with Barbara Corcoran",
        "publisher": "Barbara Corcoran",
        "thumbnail": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-_A9638PicW1-aZPn3Ic47rx.300x300.jpg",
        "listen_score": 56,
        "listennotes_url": "https://www.listennotes.com/c/68faf62be97149c280ebcc25178aa731/",
        "listen_score_global_rank": "0.5%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-_A9638PicW1-aZPn3Ic47rx.300x300.jpg",
      "description": "<p>If you\u2019re starting a new business, you need to keep costs low \u2013 so renting is the way to go, right?\n\nI say no! I\u2019ll tell you why you should scrape together the cash to buy your business headquarters from the get-go.\u00a0\n\nAlso, I\u2019ll answer some more of your great questions about how to get the press to pay attention to your little mom and pop shop and what to do about a toxic work environment.\n\nGot a business question you want to ask me? Tweet it @BarbaraCorcoran and I may just answer it on a future episode!\n\nFollow Business Unusual with Barbara Corcoran on iHeartRadio, or subscribe wherever you listen to podcasts.\n\nThis episode of Business Unusual with Barbara Corcoran is presented by\u00a0On Deck Business Loans\u00a0(http://www.ondeck.com/barbara).\u00a0\u00a0\u00a0</p>",
      "pub_date_ms": 1546232460164,
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
      "image": "https://production.listennotes.com/podcasts/listen-money-matters-free-your-inner-lPXW7V_6n0C-SJEHNr84kVg.1400x1400.jpg",
      "title": "Do Things That Scale: Starting a Business That Will Take Off",
      "podcast": {
        "id": "3302bc71139541baa46ecb27dbf6071a",
        "image": "https://production.listennotes.com/podcasts/listen-money-matters-free-your-inner-lPXW7V_6n0C-SJEHNr84kVg.1400x1400.jpg",
        "title": "Listen Money Matters - Free your inner financial badass. All the stuff you should know about personal finance.",
        "publisher": "ListenMoneyMatters.com | Andrew Fiebert and Matt Giovanisci",
        "thumbnail": "https://production.listennotes.com/podcasts/listen-money-matters-free-your-inner-d5If074qkhz-SJEHNr84kVg.300x300.jpg",
        "listen_score": 64,
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
            "description": "Episode id, which can be used to further fetch detailed episode metadata via `GET /episodes/{id}`."
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
                "description": "Podcast id, which can be used to further fetch detailed podcast metadata via `GET /podcasts/{id}`."
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
      "id": "3302bc71139541baa46ecb27dbf6071a",
      "rss": "https://feeds.megaphone.fm/listen-money-matters",
      "type": "episodic",
      "email": "listenmoneymatters@gmail.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5tZWdhcGhvbmUuZm0vbGlzdGVuLW1vbmV5LW1hdHRlcnM=",
        "spotify_url": "https://open.spotify.com/show/54VydTdMDHkfqPqzlwRJFa",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "MoneyMattersMan",
        "facebook_handle": "ListenMoneyMatters",
        "amazon_music_url": "",
        "instagram_handle": "listenmoneymatters"
      },
      "image": "https://production.listennotes.com/podcasts/listen-money-matters-free-your-inner-lPXW7V_6n0C-SJEHNr84kVg.1400x1400.jpg",
      "title": "Listen Money Matters - Free your inner financial badass. All the stuff you should know about personal finance.",
      "country": "United States",
      "website": "https://www.listenmoneymatters.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        93,
        127,
        128,
        144,
        111,
        98
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
      "listen_score": 64,
      "total_episodes": 505,
      "listennotes_url": "https://www.listennotes.com/c/3302bc71139541baa46ecb27dbf6071a/",
      "audio_length_sec": 2787,
      "explicit_content": true,
      "latest_episode_id": "d044a9f0fb304c148f4f4e9e3ad27dd6",
      "latest_pub_date_ms": 1589169600000,
      "earliest_pub_date_ms": 1383138000504,
      "update_frequency_hours": 201,
      "listen_score_global_rank": "0.05%"
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
        "spotify_url": "https://open.spotify.com/show/1bElk5alSOMk6sya929A6r",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "BarbaraCorcoran",
        "facebook_handle": "TheBarbaraCorcoran",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-YDiw-IQe4S8-aZPn3Ic47rx.1400x1400.jpg",
      "title": "Business Unusual with Barbara Corcoran",
      "country": "United States",
      "website": "https://cms.megaphone.fm/channel/business-unusual-with-barbara-corcoran?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        93,
        94,
        98,
        157
      ],
      "itunes_id": 1378685290,
      "publisher": "Barbara Corcoran",
      "thumbnail": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-_A9638PicW1-aZPn3Ic47rx.300x300.jpg",
      "is_claimed": false,
      "description": "I\u2019m smart at getting to where I want to go, and I can teach you how to do it! I had 22 jobs before starting my real estate company with a $1000 loan and built it into a $5 billion business. Today I\u2019m a \u2019Shark\u2019 on ABC\u2019s hit show \"Shark Tank.\" It didn\u2019t take a fancy degree to get here but took street smarts and a lot of courage. Life is too short to waste your time practicing someone else\u2019s fancy theory on success. I give you the straight talk and the confidence to get there. Got a question? Call me at 888-BARBARA. Subscribe to Business Unusual with Barbara Corcoran wherever you listen to podcasts.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 56,
      "total_episodes": 200,
      "listennotes_url": "https://www.listennotes.com/c/68faf62be97149c280ebcc25178aa731/",
      "audio_length_sec": 1442,
      "explicit_content": false,
      "latest_episode_id": "b97b1bb8df2d46e284d8af955c928ace",
      "latest_pub_date_ms": 1679371200000,
      "earliest_pub_date_ms": 1525202794199,
      "update_frequency_hours": 336,
      "listen_score_global_rank": "0.5%"
    },
    {
      "id": "37589a3e121e40debe4cef3d9638932a",
      "rss": "https://exponent.fm/feed/",
      "type": "episodic",
      "email": "bjthompson@mac.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9leHBvbmVudC5mbS9mZWVkLw==",
        "spotify_url": "https://open.spotify.com/show/1do6Oa0fxKFyw1Yt1IlBIk",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "exponentfm",
        "facebook_handle": "",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-xZm7IMnq5bR-OaJSjb4xQv3.1400x1400.jpg",
      "title": "Exponent",
      "country": "United States",
      "website": "https://exponent.fm?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        149,
        157,
        93,
        129,
        67,
        127
      ],
      "itunes_id": 826420969,
      "publisher": "Ben Thompson / James Allworth",
      "thumbnail": "https://production.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-8sx24A_0Jlk-OaJSjb4xQv3.300x300.jpg",
      "is_claimed": false,
      "description": "A podcast about tech and society, hosted by Ben Thompson and James Allworth",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 59,
      "total_episodes": 198,
      "listennotes_url": "https://www.listennotes.com/c/37589a3e121e40debe4cef3d9638932a/",
      "audio_length_sec": 3740,
      "explicit_content": false,
      "latest_episode_id": "dc09fd798802477b8dba0ca1e10134fa",
      "latest_pub_date_ms": 1670628575000,
      "earliest_pub_date_ms": 1392899826198,
      "update_frequency_hours": 1250,
      "listen_score_global_rank": "0.1%"
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
        "spotify_url": "https://open.spotify.com/show/6u8aqT4yaqnXiAwSHQP0NN",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "binge_mode",
        "facebook_handle": "",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/binge-mode-marvel-the-ringer-QZoDCyP6hev-BdPpshCaFDu.1400x1400.jpg",
      "title": "Binge Mode: Marvel",
      "country": "United States",
      "website": "https://art19.com/shows/binge-mode-game-of-thrones?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        68,
        162,
        122
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
      "listen_score": 76,
      "total_episodes": 41,
      "listennotes_url": "https://www.listennotes.com/c/9cf19c590ff0484d97b18b329fed0c6a/",
      "audio_length_sec": 7086,
      "explicit_content": true,
      "latest_episode_id": "349b3385606147b8b29d5aa653563669",
      "latest_pub_date_ms": 1616634120000,
      "earliest_pub_date_ms": 1496277060040,
      "update_frequency_hours": 103,
      "listen_score_global_rank": "0.01%"
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
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/find-money-you-didnt-know-you-had-npr-WuHnh0Poiyb-IDT1XPkq4rb.1400x1400.jpg",
      "title": "Find Money You Didn't Know You Had",
      "country": "United States",
      "website": "https://www.npr.org/lifekit?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        93
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
      "audio_length_sec": 520,
      "explicit_content": false,
      "latest_episode_id": "42cd0929582f4856bcca0fa98dce9119",
      "latest_pub_date_ms": 1574665259000,
      "earliest_pub_date_ms": 1544800017000,
      "update_frequency_hours": 736,
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
        "spotify_url": "https://open.spotify.com/show/5RllMBgvDnTau8nnsCUdse",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "marketsnacks",
        "facebook_handle": "MarketSnacks",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-syLJP5rimSp-kmx0XIZTAys.1400x1400.jpg",
      "title": "The Best One Yet",
      "country": "United States",
      "website": "https://www.instagram.com/tboypod?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        98,
        67,
        93,
        95,
        99
      ],
      "itunes_id": 1386234384,
      "publisher": "Nick & Jack Studios",
      "thumbnail": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-YPWcDaHknUz-kmx0XIZTAys.300x300.jpg",
      "is_claimed": false,
      "description": "Feel brighter every day with our 20-minute pop-biz podcast. The 3 business news stories you need, with fresh takes you can pretend you came up with \u2014 Pairs perfectly with your morning oatmeal ritual. Hosted by Jack Crivici-Kramer & Nick Martell.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 71,
      "total_episodes": 950,
      "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
      "audio_length_sec": 1090,
      "explicit_content": false,
      "latest_episode_id": "e67a558bc7564f72aede4f01d3e0004f",
      "latest_pub_date_ms": 1681722000000,
      "earliest_pub_date_ms": 1553519100903,
      "update_frequency_hours": 33,
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
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/philosophize-this-stephen-west-Y2PvRelyrIN-ivQCfmkqM_h.1400x1400.jpg",
      "title": "Philosophize This!",
      "country": "United States",
      "website": "http://www.philosophizethis.org?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        133,
        67,
        125,
        122,
        126,
        111
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
      "listen_score": 77,
      "total_episodes": 178,
      "listennotes_url": "https://www.listennotes.com/c/3a2a6ddd549f4df0b876e7315fa1a319/",
      "audio_length_sec": 1751,
      "explicit_content": false,
      "latest_episode_id": "02aebc6128db44a39749c008f7bfaef6",
      "latest_pub_date_ms": 1680703380000,
      "earliest_pub_date_ms": 1370556600177,
      "update_frequency_hours": 620,
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
        "amazon_music_url": "",
        "instagram_handle": "parcast"
      },
      "image": "https://production.listennotes.com/podcasts/espionage-parcast-network-X9AT-uYo8Nq-ReK0QUN-VP_.1400x1400.jpg",
      "title": "Espionage",
      "country": "United States",
      "website": "https://www.parcast.com/espionage?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        99
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
      "listen_score": 62,
      "total_episodes": 85,
      "listennotes_url": "https://www.listennotes.com/c/bacb2f7ca7a04ed0b21efd21192f5014/",
      "audio_length_sec": 2354,
      "explicit_content": false,
      "latest_episode_id": "46a1263abac242959fab3e4e14f98763",
      "latest_pub_date_ms": 1623049260000,
      "earliest_pub_date_ms": 1553471173023,
      "update_frequency_hours": 482,
      "listen_score_global_rank": "0.1%"
    },
    {
      "id": "8579c3f5d11f479d939396b1f36f30a4",
      "rss": "https://anchor.fm/s/55f4e200/podcast/rss",
      "type": "episodic",
      "email": "formosafiles@gmail.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://www.google.com/podcasts?feed=aHR0cHM6Ly9hbmNob3IuZm0vcy81NWY0ZTIwMC9wb2RjYXN0L3Jzcw==",
        "spotify_url": "https://open.spotify.com/show/23NZCM4ik6o3UYkM473Itz",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/formosa-files-lh-INvDesSm-EV8ID9SeJ1d.1400x1400.jpg",
      "title": " Formosa Files:\nThe History of Taiwan ",
      "country": "United States",
      "website": "https://www.formosafiles.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        125
      ],
      "itunes_id": 1588477096,
      "publisher": "John Ross and Eryk Michael Smith",
      "thumbnail": "https://production.listennotes.com/podcasts/formosa-files-qMZyeXN3uxL-EV8ID9SeJ1d.300x300.jpg",
      "is_claimed": false,
      "description": "The history of Taiwan (1600 C.E. - 2000) told through interesting stories in a non-chronological order. John Ross is an author and publisher of works on Taiwan and China, while Eryk Michael Smith has worked as a writer and journalist for several media outlets in Taiwan. Both hosts have lived in Taiwan for well over 20 years and call the island home. Email: formosafiles@gmail.com ",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 34,
      "total_episodes": 89,
      "listennotes_url": "https://www.listennotes.com/c/8579c3f5d11f479d939396b1f36f30a4/",
      "audio_length_sec": 1516,
      "explicit_content": false,
      "latest_episode_id": "479ad6bf3af4482bb6cf366e0b9eb526",
      "latest_pub_date_ms": 1681369066000,
      "earliest_pub_date_ms": 1630893086084,
      "update_frequency_hours": 168,
      "listen_score_global_rank": "3%"
    },
    {
      "id": "1c956b42302a488bbac0595e1922ea86",
      "rss": "https://www.omnycontent.com/d/playlist/bc559b08-358b-442a-81b6-a96000559829/c5fae094-0e75-4840-8b0d-a9ad0116ba3b/cf505041-2f72-4502-b876-a9ad0116ba3b/podcast.rss",
      "type": "episodic",
      "email": "host@alreadygonepodcast.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly93d3cub21ueWNvbnRlbnQuY29tL2QvcGxheWxpc3QvYmM1NTliMDgtMzU4Yi00NDJhLTgxYjYtYTk2MDAwNTU5ODI5L2M1ZmFlMDk0LTBlNzUtNDg0MC04YjBkLWE5YWQwMTE2YmEzYi9jZjUwNTA0MS0yZjcyLTQ1MDItYjg3Ni1hOWFkMDExNmJhM2IvcG9kY2FzdC5yc3M=",
        "spotify_url": "https://open.spotify.com/show/4qDNe5Gvl1XxdLinUGEXrC",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/already-gone-nina-innsted-p-yZYMJ0U6B-MoexDp6EKra.1400x1400.jpg",
      "title": "Already Gone",
      "country": "United States",
      "website": "https://alreadygonepodcast.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        99,
        122,
        135,
        67
      ],
      "itunes_id": 1335405710,
      "publisher": "Nina Innsted",
      "thumbnail": "https://production.listennotes.com/podcasts/already-gone-nina-innsted-L92z_F-sXQO-MoexDp6EKra.300x300.jpg",
      "is_claimed": false,
      "description": "Great Lakes. True Crime. Host Nina Innsted covers lesser known crimes, digging beneath the media and back page to tell their stories and find the truth. #Michigan #Ohio #Pennsylvania #NewYork #Wisconsin #Illinois #TrueCrime\u00a0\n\nFind me on Twitter: @Alreadygonepod (https://twitter.com/alreadygonepod) and Instagram https://www.instagram.com/ninainnsted/",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": null,
      "total_episodes": 270,
      "listennotes_url": "https://www.listennotes.com/c/1c956b42302a488bbac0595e1922ea86/",
      "audio_length_sec": 1926,
      "explicit_content": false,
      "latest_episode_id": "1ebf1f87074a44cba7354fc3f6ef8f6b",
      "latest_pub_date_ms": 1681549500000,
      "earliest_pub_date_ms": 1463950769204,
      "update_frequency_hours": 230,
      "listen_score_global_rank": null
    },
    {
      "id": "f46aac143841488b89c76923e5812846",
      "rss": "https://anchor.fm/s/cd0e434/podcast/rss",
      "type": "episodic",
      "email": null,
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy9jZDBlNDM0L3BvZGNhc3QvcnNz",
        "spotify_url": "https://open.spotify.com/show/3DDfEsKDIDrTlnPOiG4ZF4",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/sports-card-investor-sports-card-investor-GmY_9vaPHMi-vZSFLzx3p10.1400x1400.jpg",
      "title": "Sports Card Investor",
      "country": "United States",
      "website": "https://www.sportscardinvestor.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        82
      ],
      "itunes_id": 1473711424,
      "publisher": "Sports Card Investor",
      "thumbnail": "https://production.listennotes.com/podcasts/sports-card-investor-sports-card-investor-1oWHa8cJfRk-vZSFLzx3p10.300x300.jpg",
      "is_claimed": false,
      "description": "Profit from the hobby you love. What are the best baseball, basketball and football cards to invest in today? How is the market trending? How can you profit? In each episode, we tackle these questions and more.\n\nSports Card Investor is brought to you by eBay, your number one spot for cards and collectibles. With the largest inventory of sports cards from basketball to soccer, and buyers from all over the globe, eBay is the leading place to buy, sell and invest your cards. Search eBay trading cards here: https://www.ebay.com/b/Trading-Cards/bn_7116496578",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 46,
      "total_episodes": 433,
      "listennotes_url": "https://www.listennotes.com/c/f46aac143841488b89c76923e5812846/",
      "audio_length_sec": 1338,
      "explicit_content": false,
      "latest_episode_id": "6bde61b66f85466494e929420eada310",
      "latest_pub_date_ms": 1681421411000,
      "earliest_pub_date_ms": 1563549867418,
      "update_frequency_hours": 83,
      "listen_score_global_rank": "1%"
    }
  ],
  "latest_episodes": [
    {
      "id": "9447ce07dd2345618054b04b733e4ad5",
      "link": "https://www.instagram.com/tboypod?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/9447ce07dd2345618054b04b733e4ad5/",
      "image": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-syLJP5rimSp-kmx0XIZTAys.1400x1400.jpg",
      "title": "Google\u2019s $399 smartphone, Crocs\u2019 comeback, and GM\u2019s robotaxi Cruise snags $1B",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-syLJP5rimSp-kmx0XIZTAys.1400x1400.jpg",
        "title": "The Best One Yet",
        "publisher": "Nick & Jack Studios",
        "thumbnail": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-YPWcDaHknUz-kmx0XIZTAys.300x300.jpg",
        "listen_score": 71,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-YPWcDaHknUz-kmx0XIZTAys.300x300.jpg",
      "description": "<p>Google\u2019s I/O event day enjoyed protests, AI tech to screen fake\u00a0calls, and a $399 Pixel phone. General Motors acquired self-driving car startup Cruise when it was worth $1B \u2014 Now it\u2019s worth $19B, and wants robotaxis on streets this year. And Crocs shares have nearly doubled in the past year, so we look at why.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1557309360872,
      "guid_from_rss": "cc706928-7143-11e9-94ec-bf6cee57c71d",
      "listennotes_url": "https://www.listennotes.com/e/9447ce07dd2345618054b04b733e4ad5/",
      "audio_length_sec": 916,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/9447ce07dd2345618054b04b733e4ad5/#edit"
    },
    {
      "id": "68d378e5b029431dbaca6acf7ce396f2",
      "link": "https://www.instagram.com/tboypod?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/68d378e5b029431dbaca6acf7ce396f2/",
      "image": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-syLJP5rimSp-kmx0XIZTAys.1400x1400.jpg",
      "title": "Big Trade War update, Apple\u2019s bought 20+ companies in 6 months, and the largest VC investment in Latin America ever",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-syLJP5rimSp-kmx0XIZTAys.1400x1400.jpg",
        "title": "The Best One Yet",
        "publisher": "Nick & Jack Studios",
        "thumbnail": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-YPWcDaHknUz-kmx0XIZTAys.300x300.jpg",
        "listen_score": 71,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-YPWcDaHknUz-kmx0XIZTAys.300x300.jpg",
      "description": "<p>The Trade War was supposed to end this week with a peace\u00a0deal. That\u2019s not looking likely, and we\u2019ll tell you why. Apple\u2019s CEO casually dropped that the company\u2019s bought over 20 startups over the last six months. And super delivery app Rappi just raised $1B from Softbank, making it the biggest Latin American venture\u00a0investment ever.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1557222960873,
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
      "image": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-YDiw-IQe4S8-aZPn3Ic47rx.1400x1400.jpg",
      "title": "53: Something About Mary",
      "podcast": {
        "id": "68faf62be97149c280ebcc25178aa731",
        "image": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-YDiw-IQe4S8-aZPn3Ic47rx.1400x1400.jpg",
        "title": "Business Unusual with Barbara Corcoran",
        "publisher": "Barbara Corcoran",
        "thumbnail": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-_A9638PicW1-aZPn3Ic47rx.300x300.jpg",
        "listen_score": 56,
        "listennotes_url": "https://www.listennotes.com/c/68faf62be97149c280ebcc25178aa731/",
        "listen_score_global_rank": "0.5%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-_A9638PicW1-aZPn3Ic47rx.300x300.jpg",
      "description": "<p><strong>CNBC Producer Mary Hanan has the TV business dream job. I met Mary when she interviewed me for CNBC's \"The Brave Ones\" and I knew immediately I had to have her on the show. So I turned the tables on Mary and put her in the hot seat to learn how she worked her way up to the top, and she shared many of the interesting situations she found herself in along the way.Got a question for me? Call me at 888-BARBARA to ask a question for a future episode. Follow Business Unusual with Barbara Corcoran on iHeartRadio, or subscribe wherever you listen to podcasts. </strong>\u00a0<strong>This episode of Business Unusual with Barbara Corcoran is presented by OnDeck Business Loans (</strong><a href=\"https://urldefense.proofpoint.com/v2/url?u=http-3A__www.ondeck.com_Barbara&amp;d=DwMFaQ&amp;c=GC0NZZhaEw6GOQSjMHI2g15k_drElRoPmOYiK2k0eZ8&amp;r=xy9pRdG6lpZ6ogtRUMNvODnG4DdmLUxjZ2d9xbUZdbU5UshE20nENw68An-bhaS4&amp;m=b7G5z-S4fY6jYnVJoDD0IxLhdkIPrFOrNN2yLnt3Odc&amp;s=ecKEHfTJ9QtY2QfvkGL3kNIB-ZJ848-poG_hR6akhwQ&amp;e=\"><strong>http://www.ondeck.com/Barbara</strong></a><strong>)</strong></p>",
      "pub_date_ms": 1557201660146,
      "guid_from_rss": "b3ac56b2-2342-11e9-8178-17dec3a673e9",
      "listennotes_url": "https://www.listennotes.com/e/402e67e65e2a4575ab2704a977a2b4b5/",
      "audio_length_sec": 2188,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/402e67e65e2a4575ab2704a977a2b4b5/#edit"
    },
    {
      "id": "d6ff153d632f428195dfd54f002b0990",
      "link": "https://www.instagram.com/tboypod?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/d6ff153d632f428195dfd54f002b0990/",
      "image": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-syLJP5rimSp-kmx0XIZTAys.1400x1400.jpg",
      "title": "Warren Buffett\u2019s epic annual event, Planet Fitness\u2019 innovative real estate strategy, and almond milk vs. Dean Foods dairy",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-syLJP5rimSp-kmx0XIZTAys.1400x1400.jpg",
        "title": "The Best One Yet",
        "publisher": "Nick & Jack Studios",
        "thumbnail": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-YPWcDaHknUz-kmx0XIZTAys.300x300.jpg",
        "listen_score": 71,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-YPWcDaHknUz-kmx0XIZTAys.300x300.jpg",
      "description": "<p>The annual Berkshire Hathaway shareholder meeting showcased\u00a088-year-old legendary investor Warren Buffett, so we broke down his 6 hours of one-liner business takeaways. Planet Fitness shares are up 75% in the last year, so we\u2019re focused on its innovative real estate strategy that feeds off the retail-pocalypse. And Dean Foods is America\u2019s biggest dairy company, but the stock is down 62% in 2019 because of alt-milk.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1557136560874,
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
        "listen_score": 64,
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
      "link": "https://www.instagram.com/tboypod?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/e2e15dc3f99745818872e71f7c828f89/",
      "image": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-syLJP5rimSp-kmx0XIZTAys.1400x1400.jpg",
      "title": "The Taser CEO gets $246M in stock comp, Beyond Meat surges 163%, and Wayfair drops 7% because you\u2019re expensive",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-syLJP5rimSp-kmx0XIZTAys.1400x1400.jpg",
        "title": "The Best One Yet",
        "publisher": "Nick & Jack Studios",
        "thumbnail": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-YPWcDaHknUz-kmx0XIZTAys.300x300.jpg",
        "listen_score": 71,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-YPWcDaHknUz-kmx0XIZTAys.300x300.jpg",
      "description": "<p>Axon Enterprises is the company behind the taser, and it just awarded its CEO $246M in compensation \u2014 So we look in to how it\u2019s set up to incentivize him. Beyond Meat surged 163% on its IPO day. And Wayfair is the biggest online furniture platform whose stock fell 7%, but it\u2019s got a fascinating relationship with 80 \u201chouse brands.\u201d</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1556877360875,
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
        "listen_score": 62,
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
      "link": "https://www.instagram.com/tboypod?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/f0f2cc1d772c4ae4aef5bd1d1c8fb834/",
      "image": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-syLJP5rimSp-kmx0XIZTAys.1400x1400.jpg",
      "title": "Molson Coors falls 8% on mid-beer crisis, Royal Caribbean becomes pricing power superhero, and Fitbit is our \u201cSurvivor of the Day\u201d",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-syLJP5rimSp-kmx0XIZTAys.1400x1400.jpg",
        "title": "The Best One Yet",
        "publisher": "Nick & Jack Studios",
        "thumbnail": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-YPWcDaHknUz-kmx0XIZTAys.300x300.jpg",
        "listen_score": 71,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-YPWcDaHknUz-kmx0XIZTAys.300x300.jpg",
      "description": "<p>With beer sales slowing, Molson Coors is desperately\u00a0focused on innovation (aka non-alcohol drinks), but shares fell because of its beer battles. Fitbit used to be profitable, now it\u2019s using partnerships to survive. And Royal Caribbean jumped 7% as it realizes it can charge a lot more for cruises.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1556790960876,
      "guid_from_rss": "ae282d24-6c71-11e9-a7ab-eff35f170a02",
      "listennotes_url": "https://www.listennotes.com/e/f0f2cc1d772c4ae4aef5bd1d1c8fb834/",
      "audio_length_sec": 1000,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/f0f2cc1d772c4ae4aef5bd1d1c8fb834/#edit"
    },
    {
      "id": "79811cc9a5704e32881699b0b93356ab",
      "link": "https://www.instagram.com/tboypod?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/79811cc9a5704e32881699b0b93356ab/",
      "image": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-syLJP5rimSp-kmx0XIZTAys.1400x1400.jpg",
      "title": "Facebook\u2019s new \u201cFB5\u201d redesign (and dating feature), Apple\u2019s past-dependent business model, and Merck\u2019s profits quadruple",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-syLJP5rimSp-kmx0XIZTAys.1400x1400.jpg",
        "title": "The Best One Yet",
        "publisher": "Nick & Jack Studios",
        "thumbnail": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-YPWcDaHknUz-kmx0XIZTAys.300x300.jpg",
        "listen_score": 71,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-YPWcDaHknUz-kmx0XIZTAys.300x300.jpg",
      "description": "<p>Apple\u2019s earnings report was critical for what it didn\u2019t say, just as much as what it did \u2014 And it reveals that Apple\u2019s transformation. Facebook\u2019s F8 event revealed new features (dating and crushes), but the big focus was its app redesign. And Merck\u2019s profits quadrupled because a measles vaccine and a new cancer drug have become its profit puppies.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1556704560877,
      "guid_from_rss": "ad35b722-6bb0-11e9-8988-bfa74a4a2234",
      "listennotes_url": "https://www.listennotes.com/e/79811cc9a5704e32881699b0b93356ab/",
      "audio_length_sec": 888,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/79811cc9a5704e32881699b0b93356ab/#edit"
    },
    {
      "id": "82290b02fa4e48d7bda7d9a4ee0b47bc",
      "link": "https://omny.fm/shows/already-gone/the-mothers-day-murders?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/82290b02fa4e48d7bda7d9a4ee0b47bc/",
      "image": "https://production.listennotes.com/podcasts/already-gone-nina-innsted-p-yZYMJ0U6B-MoexDp6EKra.1400x1400.jpg",
      "title": "The Mother's Day Murders",
      "podcast": {
        "id": "1c956b42302a488bbac0595e1922ea86",
        "image": "https://production.listennotes.com/podcasts/already-gone-nina-innsted-p-yZYMJ0U6B-MoexDp6EKra.1400x1400.jpg",
        "title": "Already Gone",
        "publisher": "Nina Innsted",
        "thumbnail": "https://production.listennotes.com/podcasts/already-gone-nina-innsted-L92z_F-sXQO-MoexDp6EKra.300x300.jpg",
        "listen_score": null,
        "listennotes_url": "https://www.listennotes.com/c/1c956b42302a488bbac0595e1922ea86/",
        "listen_score_global_rank": null
      },
      "thumbnail": "https://production.listennotes.com/podcasts/already-gone-nina-innsted-L92z_F-sXQO-MoexDp6EKra.300x300.jpg",
      "description": "<p>Mother's Day 1982, high school students David Cole and Timothy Fowler die in a fiery blaze at the Cole home in Deerfield Michigan. This episode features an interview with the sister of Tim Fowler.\u00a0 <a href=\"https://www.facebook.com/timfowlerdavidcole/\">https://www.facebook.com/timfowlerdavidcole/</a><br /><br />If you have information on this unsolved case, please contact the Lenawee County Sheriff's Department at <strong>517-266-6161 </strong>or, submit an anonymous tip via CrimeStoppers, Online at:\u00a0<a href=\"http://www.tipsubmit.com\">www.tipsubmit.com</a> or via text \u00a0274637 Start Tip \"LENAWEE\"</p>\n<p>Additional Music provided by RFM: <a href=\"https://www.youtube.com/watch?v=dPEoasBHNiA\">https://youtu.be/dPEoasBHNiA</a><strong><br /></strong></p><p><a href=\"https://www.patreon.com/AlreadyGone\" rel=\"payment\">Support the show: https://www.patreon.com/AlreadyGone</a></p><p>See <a href=\"https://omnystudio.com/listener\">omnystudio.com/listener</a> for privacy information.</p>",
      "pub_date_ms": 1556683500101,
      "guid_from_rss": "7081a388-0ebe-4d75-98c0-aa3e01475606",
      "listennotes_url": "https://www.listennotes.com/e/82290b02fa4e48d7bda7d9a4ee0b47bc/",
      "audio_length_sec": 2001,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/82290b02fa4e48d7bda7d9a4ee0b47bc/#edit"
    },
    {
      "id": "6f4b561b98c4489f94673bd709fa0c85",
      "link": "https://www.instagram.com/tboypod?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/6f4b561b98c4489f94673bd709fa0c85/",
      "image": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-syLJP5rimSp-kmx0XIZTAys.1400x1400.jpg",
      "title": "Spotify hits 217M profitless users, Airbnb & Marriott\u2019s twin announcements, and Chewy.com\u2019s \u201cpet humanization\u201d IPO",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-syLJP5rimSp-kmx0XIZTAys.1400x1400.jpg",
        "title": "The Best One Yet",
        "publisher": "Nick & Jack Studios",
        "thumbnail": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-YPWcDaHknUz-kmx0XIZTAys.300x300.jpg",
        "listen_score": 71,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-YPWcDaHknUz-kmx0XIZTAys.300x300.jpg",
      "description": "<p>Spotify now boasts 100M paying subscribers, so we looked\u00a0into why it\u2019s still losing so much money (hint: It\u2019s betting on podcasts). Airbnb and Marriott both revealed new services that look a lot like each other (awkward). And PetSmart\u2019s digital brand Chewy.com will IPO thanks to \u201cpet humanization\u201d trends.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1556618160878,
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
      "image": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-YDiw-IQe4S8-aZPn3Ic47rx.1400x1400.jpg",
      "title": "52: What I Learned From Bad Bosses",
      "podcast": {
        "id": "68faf62be97149c280ebcc25178aa731",
        "image": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-YDiw-IQe4S8-aZPn3Ic47rx.1400x1400.jpg",
        "title": "Business Unusual with Barbara Corcoran",
        "publisher": "Barbara Corcoran",
        "thumbnail": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-_A9638PicW1-aZPn3Ic47rx.300x300.jpg",
        "listen_score": 56,
        "listennotes_url": "https://www.listennotes.com/c/68faf62be97149c280ebcc25178aa731/",
        "listen_score_global_rank": "0.5%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-_A9638PicW1-aZPn3Ic47rx.300x300.jpg",
      "description": "<p><strong>I had 23 bosses before starting my business and I know that a bad one is sure to kill your confidence. So what do you do when you don't see eye to eye? I answer your questions about dealing with a bad boss and becoming a better leader. </strong>\u00a0<strong>Want to hear your question on Business Unusual? Call me at 888-BARBARA or tweet at @barbaracorcoran to ask a question for a future episode. Follow Business Unusual with Barbara Corcoran on iHeartRadio, or subscribe wherever you listen to podcasts. </strong>\u00a0<strong>This episode of Business Unusual with Barbara Corcoran is presented by OnDeck Business Loans (</strong><a href=\"https://urldefense.proofpoint.com/v2/url?u=http-3A__www.ondeck.com_Barbara&amp;d=DwMFaQ&amp;c=GC0NZZhaEw6GOQSjMHI2g15k_drElRoPmOYiK2k0eZ8&amp;r=xy9pRdG6lpZ6ogtRUMNvODnG4DdmLUxjZ2d9xbUZdbU5UshE20nENw68An-bhaS4&amp;m=iyzCy3KkByFDhAZKPNnXfRZDwVi9wa4vgtkjqAegOYo&amp;s=AR-0E6fCOSktW28rNgQpCe-kEyu1odFgovlqPFyavSA&amp;e=\"><strong>http://www.ondeck.com/Barbara</strong></a><strong>)</strong>\u00a0</p>",
      "pub_date_ms": 1556596860147,
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
        "listen_score": 77,
        "listennotes_url": "https://www.listennotes.com/c/3a2a6ddd549f4df0b876e7315fa1a319/",
        "listen_score_global_rank": "0.01%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/philosophize-this-stephen-west-oSuiCW7Bz8T-ivQCfmkqM_h.300x300.jpg",
      "description": "<p>Today we talk about a famous debate from the early 20th century.\u00a0</p>",
      "pub_date_ms": 1556594432048,
      "guid_from_rss": "09cea1e8a32c49b383f85fff0f172a2e",
      "listennotes_url": "https://www.listennotes.com/e/8823f69978ac40899d4e7264206db89f/",
      "audio_length_sec": 1298,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/8823f69978ac40899d4e7264206db89f/#edit"
    },
    {
      "id": "d8ad1f1994654319a041e23d76d6b599",
      "link": "https://www.instagram.com/tboypod?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/d8ad1f1994654319a041e23d76d6b599/",
      "image": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-syLJP5rimSp-kmx0XIZTAys.1400x1400.jpg",
      "title": "Beyond Meat boots its meat-focused investor, Comcast (shockingly) hits record high, and one startup\u2019s worst 1st week",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-syLJP5rimSp-kmx0XIZTAys.1400x1400.jpg",
        "title": "The Best One Yet",
        "publisher": "Nick & Jack Studios",
        "thumbnail": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-YPWcDaHknUz-kmx0XIZTAys.300x300.jpg",
        "listen_score": 71,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-YPWcDaHknUz-kmx0XIZTAys.300x300.jpg",
      "description": "<p>Plant-based meat innovator Beyond Meat had an awkward investor: The world\u2019s 2nd biggest meat producer, Tyson Foods -- So Beyond Meat kicked it out before its upcoming IPO. Old school cable throwback Comcast is winning even though you cut the cord. And Luminary was supposed to be the future of podcasting, but its 1st week went really badly.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1556531760879,
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
            "description": "Podcast id, which can be used to further fetch detailed podcast metadata via `GET /podcasts/{id}`."
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
                "example": "https://podcasts.google.com/feed/aHR0cHM6Ly9yc3MuYXJ0MTkuY29tL2pvaG4tc29sb21vbi1yZXBvcnRz",
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
              "amazon_music_url": {
                "type": "string",
                "example": "https://music.amazon.com/podcasts/6fc6d683-9ef3-4850-9c35-8e8b1a42a147/the-lock-sportscast",
                "description": "Amazon Music url for this podcast"
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
          "audio_length_sec": {
            "type": "integer",
            "example": 1291,
            "description": "Average audio length of all episodes of this podcast. In seconds."
          },
          "explicit_content": {
            "type": "boolean",
            "example": false,
            "description": "Whether this podcast contains explicit language."
          },
          "latest_episode_id": {
            "type": "string",
            "example": "d057092e57cc4ced80e0efaa196593d9",
            "description": "The id of the most recently published episode of this podcast, which can be used to further fetch detailed episode metadata via `GET /episodes/{id}`."
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
          "update_frequency_hours": {
            "type": "integer",
            "example": 168,
            "description": "How frequently does this podcast release a new episode? In hours. For example, if the value is 166, then it's every 166 hours (or weekly)."
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
            "description": "Episode id, which can be used to further fetch detailed episode metadata via `GET /episodes/{id}`."
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
                "description": "Podcast id, which can be used to further fetch detailed podcast metadata via `GET /podcasts/{id}`."
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
  "id": "01d2b1f0b810448c8671407a7e02c969",
  "link": "https://www.cleartosend.net/cts-314-is-chatgpt-useful-to-a-wi-fi-engineer/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
  "audio": "https://www.listennotes.com/e/p/01d2b1f0b810448c8671407a7e02c969/",
  "image": "https://production.listennotes.com/podcasts/clear-to-send-wireless-network-engineering-DFGwRzxcMC4.1024x1024.jpg",
  "title": "CTS 314: Is ChatGPT useful to a Wi-Fi Engineer",
  "podcast": {
    "id": "e2afd72249f54625acc0d2a5cb364d9c",
    "image": "https://production.listennotes.com/podcasts/clear-to-send-wireless-network-engineering-DFGwRzxcMC4.1024x1024.jpg",
    "title": "Clear To Send: Wireless Network Engineering",
    "publisher": "Rowell Dionicio and Fran\u00e7ois Verg\u00e8s",
    "thumbnail": "https://production.listennotes.com/podcasts/clear-to-send-wireless-network-engineering-DFGwRzxcMC4.300x300.jpg",
    "listen_score": 38,
    "listennotes_url": "https://www.listennotes.com/c/e2afd72249f54625acc0d2a5cb364d9c/",
    "listen_score_global_rank": "2%"
  },
  "thumbnail": "https://production.listennotes.com/podcasts/clear-to-send-wireless-network-engineering-DFGwRzxcMC4.300x300.jpg",
  "description": "<p></p>\n\n\n\n<figure class=\"wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio\"><div class=\"wp-block-embed__wrapper\">\n\n</div></figure>\n\n\n\n<p><strong>Description</strong></p>\n\n\n\n<p> &#x1f4a1; Talk about the ChatGPT trend and discuss if it is useful to us as Wi-Fi Engineer</p>\n\n\n\n<p></p>\n\n\n\n<h3 class=\"wp-block-heading\">Talking Points</h3>\n\n\n\n<p><strong>Introduction</strong></p>\n\n\n\n<ul>\n<li>Chat GPT trend</li>\n\n\n\n<li>How is AI going to change the way we work (as Wi-Fi Engineer)</li>\n</ul>\n\n\n\n<p><strong>Main Topic</strong></p>\n\n\n\n<ul>\n<li>Is it really useful?</li>\n\n\n\n<li>What has been our experience</li>\n\n\n\n<li>What works\n<ul>\n<li>Programming (coding, converting, adjusting, debugging, creating)</li>\n\n\n\n<li>Fixing writing and spelling mistakes</li>\n\n\n\n<li>Translating</li>\n\n\n\n<li>Debug or fix issues (mtr)</li>\n</ul>\n</li>\n\n\n\n<li>What doesn\u2019t fully work\n<ul>\n<li>Research work</li>\n\n\n\n<li>Digging out information</li>\n</ul>\n</li>\n\n\n\n<li>What doesn\u2019t really work\n<ul>\n<li>Creating Wireshark 802.11 filters didn\u2019t work for me</li>\n\n\n\n<li>Hard to know if what it tells you is True of False (it always sound very confident)</li>\n</ul>\n</li>\n</ul>\n\n\n\n<p>Useful Chrome Extensions:</p>\n\n\n\n<ul>\n<li>Send all Google Search to ChatGPT \u2192 <a href=\"https://chrome.google.com/webstore/detail/chatgpt-for-google/jgjaeacdkonaoafenlfkkkmbaopkbilf\"></a><a href=\"https://chrome.google.com/webstore/detail/chatgpt-for-google/jgjaeacdkonaoafenlfkkkmbaopkbilf\">https://chrome.google.com/webstore/detail/chatgpt-for-google/jgjaeacdkonaoafenlfkkkmbaopkbilf</a></li>\n\n\n\n<li>Add access to Internet to ChatGPT \u2192 <a href=\"https://chrome.google.com/webstore/detail/webchatgpt-chatgpt-with-i/lpfemeioodjbpieminkklglpmhlngfcn\"></a><a href=\"https://chrome.google.com/webstore/detail/webchatgpt-chatgpt-with-i/lpfemeioodjbpieminkklglpmhlngfcn\">https://chrome.google.com/webstore/detail/webchatgpt-chatgpt-with-i/lpfemeioodjbpieminkklglpmhlngfcn</a></li>\n</ul>\n\n\n\n<p></p>\n<p>The post <a href=\"https://www.cleartosend.net/cts-314-is-chatgpt-useful-to-a-wi-fi-engineer/\" rel=\"nofollow\">CTS 314: Is ChatGPT useful to a Wi-Fi Engineer</a> appeared first on <a href=\"https://www.cleartosend.net\" rel=\"nofollow\">Clear To Send</a>.</p>",
  "pub_date_ms": 1681726740000,
  "guid_from_rss": "https://www.cleartosend.net/?p=4214",
  "listennotes_url": "https://www.listennotes.com/e/01d2b1f0b810448c8671407a7e02c969/",
  "audio_length_sec": 2071,
  "explicit_content": false,
  "maybe_audio_invalid": false,
  "listennotes_edit_url": "https://www.listennotes.com/e/01d2b1f0b810448c8671407a7e02c969/#edit"
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
      "description": "Episode id, which can be used to further fetch detailed episode metadata via `GET /episodes/{id}`."
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
          "description": "Podcast id, which can be used to further fetch detailed podcast metadata via `GET /podcasts/{id}`."
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
      "rss": "https://www.omnycontent.com/d/playlist/5d315e00-1c8d-435b-9a31-af0f01302c17/ffc313b5-b60e-492b-9db0-af1a0027aaf9/21999f5d-eb98-4f19-82f9-af1a0027ab0c/podcast.rss",
      "type": "episodic",
      "email": "maedinindia@gmail.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly93d3cub21ueWNvbnRlbnQuY29tL2QvcGxheWxpc3QvNWQzMTVlMDAtMWM4ZC00MzViLTlhMzEtYWYwZjAxMzAyYzE3L2ZmYzMxM2I1LWI2MGUtNDkyYi05ZGIwLWFmMWEwMDI3YWFmOS8yMTk5OWY1ZC1lYjk4LTRmMTktODJmOS1hZjFhMDAyN2FiMGMvcG9kY2FzdC5yc3M=",
        "spotify_url": "https://open.spotify.com/show/0QhzjA2zKdKgIQsd2ltHtp?si=1G6nu1YnRKiM9XPgjs3fyw",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "maedinindia",
        "facebook_handle": "maedinindia",
        "amazon_music_url": "",
        "instagram_handle": "maedinindia"
      },
      "image": "https://production.listennotes.com/podcasts/maed-in-india-maed-in-india-cC8sOFyVQzE-y2oQTwMN73p.1400x1400.jpg",
      "title": "Maed in India",
      "country": "United States",
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
      "thumbnail": "https://production.listennotes.com/podcasts/maed-in-india-maed-in-india-8mQ5zrupi0T-y2oQTwMN73p.300x300.jpg",
      "is_claimed": true,
      "description": "Maed in India - India's first indie music podcast that showcases the best Indian independent musicians from India and abroad. Each episode presents an interview with an artist/band along with an exclusive stripped down session or acoustic renditions of their original music. The weekly show prides itself on being the destination for new music, little known stories, and unreleased music never heard before.\n\nIt features all kinds of artists from new-comers to veterans and under a variety of genres from hip hop, blues, soul, to folk, punk, rock, and everything in between.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 43,
      "total_episodes": 323,
      "listennotes_url": "https://www.listennotes.com/c/c463d5980b8e480fb78db6b3ed6be115/",
      "audio_length_sec": 3059,
      "explicit_content": false,
      "latest_episode_id": "5b879b5d11724057bff453ac0bf3661c",
      "latest_pub_date_ms": 1681075800000,
      "earliest_pub_date_ms": 1434346200321,
      "update_frequency_hours": 167,
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
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-intersection-the-intersection-is1CILODdqm-LTmzMb05tFB.150x150.jpg",
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
      "thumbnail": "https://production.listennotes.com/podcasts/the-intersection-the-intersection-is1CILODdqm-LTmzMb05tFB.150x150.jpg",
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
      "audio_length_sec": 938,
      "explicit_content": false,
      "latest_episode_id": "a9e4b2872a3746c8a8df50f5fc53f9fa",
      "latest_pub_date_ms": 1545121747000,
      "earliest_pub_date_ms": 1427975825000,
      "update_frequency_hours": 751,
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
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/trial-by-error-the-aarushi-files-arre-HW5-PMrpJ6g--hleb0zIEPC.1400x1400.jpg",
      "title": "Trial by Error | The Aarushi Files",
      "country": "United States",
      "website": "https://www.arre.co.in/series/aarushi?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        122
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
      "listen_score": 39,
      "total_episodes": 16,
      "listennotes_url": "https://www.listennotes.com/c/10a1ff15904548978355ff69166b2578/",
      "audio_length_sec": 1276,
      "explicit_content": false,
      "latest_episode_id": "7d084c19d0184e30ade557a74af585fa",
      "latest_pub_date_ms": 1468183671000,
      "earliest_pub_date_ms": 1462135535000,
      "update_frequency_hours": 100,
      "listen_score_global_rank": "2%"
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
        "amazon_music_url": "",
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
      "audio_length_sec": 1979,
      "explicit_content": true,
      "latest_episode_id": "2ff91dbbf6e544468501e1af5c4b8e66",
      "latest_pub_date_ms": 1515393130000,
      "earliest_pub_date_ms": 1504590119004,
      "update_frequency_hours": 638,
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
        "spotify_url": "https://open.spotify.com/show/7tvnxtkeAYAtys53aqYAVs",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "amazon_music_url": "",
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
      "audio_length_sec": 2399,
      "explicit_content": false,
      "latest_episode_id": "71ef8a25d040413bb6ea4bd5cb7e57a7",
      "latest_pub_date_ms": 1459143000000,
      "earliest_pub_date_ms": 1453095676009,
      "update_frequency_hours": 167,
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
        "spotify_url": "https://open.spotify.com/show/3X8PKcM3Z5PTkWaw1H6Pua",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "amazon_music_url": "",
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
      "description": "f(q) = Where do dogs go to die? (#TLFD)\n\nSynTalk is a freewheeling interdisciplinary talk show with a philosophical approach to understanding the world from a long term perspective.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 31,
      "total_episodes": 179,
      "listennotes_url": "https://www.listennotes.com/c/c40188a1a51249a3bafb11793a011359/",
      "audio_length_sec": 4078,
      "explicit_content": false,
      "latest_episode_id": "0cbf27a83b364f5f9e7285db0e438f29",
      "latest_pub_date_ms": 1680912000000,
      "earliest_pub_date_ms": 1405191856173,
      "update_frequency_hours": 1212,
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
        "spotify_url": "https://open.spotify.com/show/0bZESriuxQ3XUVVN9EpsMw",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "Indianstartupsh",
        "facebook_handle": "indianstartupshow",
        "amazon_music_url": "",
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
      "description": "A Weekly Podcast Show About Indian Startups\nEntrepreneurs & More !\nHosted by Neil Patel & Friends",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 40,
      "total_episodes": 197,
      "listennotes_url": "https://www.listennotes.com/c/24ece1d0922d4d9a9659e9e6cb2b241e/",
      "audio_length_sec": 2241,
      "explicit_content": false,
      "latest_episode_id": "49765932639d452aac10672a82eba33a",
      "latest_pub_date_ms": 1678060800000,
      "earliest_pub_date_ms": 1439366880196,
      "update_frequency_hours": 688,
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
        "amazon_music_url": "",
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
      "audio_length_sec": 776,
      "explicit_content": false,
      "latest_episode_id": "c32a23ea5c624ca8a0d65a20cf554390",
      "latest_pub_date_ms": 1481272467000,
      "earliest_pub_date_ms": 1446055111000,
      "update_frequency_hours": 121,
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
        "spotify_url": "https://open.spotify.com/show/4ief9N2sznclDDHeqKZXqz",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "GeekFruitHQ",
        "facebook_handle": "ivmpodcasts",
        "amazon_music_url": "",
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
      "listen_score": 33,
      "total_episodes": 342,
      "listennotes_url": "https://www.listennotes.com/c/4151ce9377a6435c8aac7d23f306243d/",
      "audio_length_sec": 2641,
      "explicit_content": false,
      "latest_episode_id": "07bdb16df6d04ba783895ae96b941963",
      "latest_pub_date_ms": 1595810106000,
      "earliest_pub_date_ms": 1450868870327,
      "update_frequency_hours": 160,
      "listen_score_global_rank": "5%"
    },
    {
      "id": "2641ed2ce5524b3da43b8f19fe0f5ae9",
      "rss": "https://www.omnycontent.com/d/playlist/e0dce4b3-2eb8-48cb-822c-af1d00e03e20/9baef9c9-4ff2-4b4e-a3dd-af540094e334/270ddb3d-16c8-4190-81d4-af540094e347/podcast.rss",
      "type": "episodic",
      "email": "ivmshows@pratilipi.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly93d3cub21ueWNvbnRlbnQuY29tL2QvcGxheWxpc3QvZTBkY2U0YjMtMmViOC00OGNiLTgyMmMtYWYxZDAwZTAzZTIwLzliYWVmOWM5LTRmZjItNGI0ZS1hM2RkLWFmNTQwMDk0ZTMzNC8yNzBkZGIzZC0xNmM4LTQxOTAtODFkNC1hZjU0MDA5NGUzNDcvcG9kY2FzdC5yc3M=",
        "spotify_url": "https://open.spotify.com/show/4Njctb1AY3cTv0wOKZkRXE",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "cyrussaysin",
        "facebook_handle": "ivmpodcasts",
        "amazon_music_url": "",
        "instagram_handle": "ivmpodcasts"
      },
      "image": "https://production.listennotes.com/podcasts/cyrus-says-ivm-podcasts-uXBWJFhsMpU-1q2UDTO6ztZ.1400x1400.jpg",
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
      "thumbnail": "https://production.listennotes.com/podcasts/cyrus-says-ivm-podcasts-viLbUGYkS0x-1q2UDTO6ztZ.300x300.jpg",
      "is_claimed": true,
      "description": "<p>Broadcasting through the week with a rotating panel of guests, Cyrus Says is the definitive show on life in urban India, politics, sports, civic sense, traffic, kids, food, and everything that matters. Mostly.</p>",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 52,
      "total_episodes": 1157,
      "listennotes_url": "https://www.listennotes.com/c/2641ed2ce5524b3da43b8f19fe0f5ae9/",
      "audio_length_sec": 3211,
      "explicit_content": false,
      "latest_episode_id": "cf4b9c06a56747af89c131d3110c2009",
      "latest_pub_date_ms": 1681453800000,
      "earliest_pub_date_ms": 1426829401156,
      "update_frequency_hours": 83,
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
        "amazon_music_url": "",
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
      "audio_length_sec": 911,
      "explicit_content": false,
      "latest_episode_id": "1271132f42784834b9a176e8b497b066",
      "latest_pub_date_ms": 1485346229000,
      "earliest_pub_date_ms": 1429793450000,
      "update_frequency_hours": 355,
      "listen_score_global_rank": null
    },
    {
      "id": "bdeb94c7f7164b14837dcd0449f4a5ee",
      "rss": "https://feeds.feedburner.com/Allindiabakchod",
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
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/all-india-bakchod-all-india-bakchod-3MYkKPLD2fw-kgcdJ-xKmAL.1023x990.jpg",
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
      "thumbnail": "https://production.listennotes.com/podcasts/all-india-bakchod-all-india-bakchod-iS6oz1HF-A8-kgcdJ-xKmAL.300x290.jpg",
      "is_claimed": false,
      "description": "All India Bakchod is India's most widely heard, edgiest, comedy podcast - run by comedians Tanmay Bhat (www.tanmaybhat.com) and Gursimranjeet Khamba (www.gkhamba.com) - It's their take on everything that made it to the news. It's your fortnightly dose of entirely uncensored bakchod. Subscribe away! ",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 41,
      "total_episodes": 8,
      "listennotes_url": "https://www.listennotes.com/c/bdeb94c7f7164b14837dcd0449f4a5ee/",
      "audio_length_sec": 1135,
      "explicit_content": true,
      "latest_episode_id": "7b21625d3ca6411da3c5dff86243a87d",
      "latest_pub_date_ms": 1506436886000,
      "earliest_pub_date_ms": 1488805724007,
      "update_frequency_hours": 476,
      "listen_score_global_rank": "1.5%"
    },
    {
      "id": "d203864a67fb43b1a98b7107cabeaa4b",
      "rss": "http://feeds.feedburner.com/OurLastWeek",
      "type": "episodic",
      "email": null,
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
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/our-last-week-audiomatic-ed96Q4pHgsE.1400x1400.jpg",
      "title": "Our Last Week",
      "country": "United States",
      "website": "http://soundcloud.com/our-last-week?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        133
      ],
      "itunes_id": 992068781,
      "publisher": "Our Last Week",
      "thumbnail": "https://production.listennotes.com/podcasts/our-last-week-audiomatic-ed96Q4pHgsE.300x300.jpg",
      "is_claimed": false,
      "description": "Podcast by Our Last Week",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 35,
      "total_episodes": 45,
      "listennotes_url": "https://www.listennotes.com/c/d203864a67fb43b1a98b7107cabeaa4b/",
      "audio_length_sec": 1259,
      "explicit_content": false,
      "latest_episode_id": "75a2ece4538149e3bda45a163059496d",
      "latest_pub_date_ms": 1579417200000,
      "earliest_pub_date_ms": 1431062738044,
      "update_frequency_hours": 343,
      "listen_score_global_rank": "3%"
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
        "spotify_url": "https://open.spotify.com/show/4hCiisdImoP3csky5i13zE",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "historyofindiapodcast",
        "amazon_music_url": "",
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
      "listen_score": 55,
      "total_episodes": 142,
      "listennotes_url": "https://www.listennotes.com/c/83907f1577724ac1b2c6ab154f8e0566/",
      "audio_length_sec": 2618,
      "explicit_content": false,
      "latest_episode_id": "1b58cd0c4312421db376d2af5165f25e",
      "latest_pub_date_ms": 1610564400000,
      "earliest_pub_date_ms": 1437820995140,
      "update_frequency_hours": 623,
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
        "amazon_music_url": "",
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
      "audio_length_sec": 2321,
      "explicit_content": false,
      "latest_episode_id": "8473fbfb1c764b7f95169abfb497ec9c",
      "latest_pub_date_ms": 1495259445000,
      "earliest_pub_date_ms": 1337444762000,
      "update_frequency_hours": 1568,
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
        "spotify_url": "https://open.spotify.com/show/0lEkSBHhsiNnWeIWGajTjV",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "amazon_music_url": "",
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
      "audio_length_sec": 1694,
      "explicit_content": false,
      "latest_episode_id": "c416a3afee9f497b86f91e90df55dfb0",
      "latest_pub_date_ms": 1560299400000,
      "earliest_pub_date_ms": 1448286726564,
      "update_frequency_hours": 26,
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
      "description": "Curated list id, which can be used to further fetch detailed curated list metadata via `GET /curated_podcasts/{id}`."
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
            "description": "Podcast id, which can be used to further fetch detailed podcast metadata via `GET /podcasts/{id}`."
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
                "example": "https://podcasts.google.com/feed/aHR0cHM6Ly9yc3MuYXJ0MTkuY29tL2pvaG4tc29sb21vbi1yZXBvcnRz",
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
              "amazon_music_url": {
                "type": "string",
                "example": "https://music.amazon.com/podcasts/6fc6d683-9ef3-4850-9c35-8e8b1a42a147/the-lock-sportscast",
                "description": "Amazon Music url for this podcast"
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
          "audio_length_sec": {
            "type": "integer",
            "example": 1291,
            "description": "Average audio length of all episodes of this podcast. In seconds."
          },
          "explicit_content": {
            "type": "boolean",
            "example": false,
            "description": "Whether this podcast contains explicit language."
          },
          "latest_episode_id": {
            "type": "string",
            "example": "d057092e57cc4ced80e0efaa196593d9",
            "description": "The id of the most recently published episode of this podcast, which can be used to further fetch detailed episode metadata via `GET /episodes/{id}`."
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
          "update_frequency_hours": {
            "type": "integer",
            "example": 168,
            "description": "How frequently does this podcast release a new episode? In hours. For example, if the value is 166, then it's every 166 hours (or weekly)."
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
  "total": 4523,
  "has_next": true,
  "page_number": 2,
  "has_previous": true,
  "curated_lists": [
    {
      "id": "L415XAvPT7q",
      "title": "The Best Podcasts Like My Dad Wrote a Porno",
      "total": 6,
      "podcasts": [
        {
          "id": "6d9aadb8bcdd47248f81958bde7f610c",
          "image": "https://production.listennotes.com/podcasts/help-i-sexted-my-boss-audio-always-XGwzdTJRegO-LakX4pShTF9.1400x1400.jpg",
          "title": "Help I Sexted My Boss",
          "publisher": "Audio Always",
          "thumbnail": "https://production.listennotes.com/podcasts/help-i-sexted-my-boss-audio-always-F9pIdB5yal4-LakX4pShTF9.300x300.jpg",
          "listen_score": 65,
          "listennotes_url": "https://www.listennotes.com/c/6d9aadb8bcdd47248f81958bde7f610c/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "5135c34d884a47bba26472c1ecd39f23",
          "image": "https://production.listennotes.com/podcasts/the-mortified-podcast-mortified-media-and-6KzT8DM1iXc-oiAIBjZbt5r.1400x1400.jpg",
          "title": "The Mortified Podcast",
          "publisher": "Mortified Media and Radiotopia",
          "thumbnail": "https://production.listennotes.com/podcasts/the-mortified-podcast-mortified-media-and-B_NjkwSsy7q-oiAIBjZbt5r.300x300.jpg",
          "listen_score": 65,
          "listennotes_url": "https://www.listennotes.com/c/5135c34d884a47bba26472c1ecd39f23/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "7610fb06bdfb4a97913b8fbbd4e0549d",
          "image": "https://production.listennotes.com/podcasts/shxtsngigs-shxtsngigs-WEdcmPDxljC-xzNB5_7Tb1-.1400x1400.jpg",
          "title": "ShxtsNGigs",
          "publisher": "shxtsngigs",
          "thumbnail": "https://production.listennotes.com/podcasts/shxtsngigs-shxtsngigs-XHus6ymkh9N-xzNB5_7Tb1-.300x300.jpg",
          "listen_score": 64,
          "listennotes_url": "https://www.listennotes.com/c/7610fb06bdfb4a97913b8fbbd4e0549d/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "318c0919e1d44a409c8d7e6df3879585",
          "image": "https://production.listennotes.com/podcasts/beach-too-sandy-water-too-wet-forever-dog-6IFTGu9l0xj-eXcHhl2EMAF.1400x1400.jpg",
          "title": "Beach Too Sandy, Water Too Wet",
          "publisher": "Forever Dog",
          "thumbnail": "https://production.listennotes.com/podcasts/beach-too-sandy-water-too-wet-forever-dog-MziK3NWYaTe-eXcHhl2EMAF.300x300.jpg",
          "listen_score": 67,
          "listennotes_url": "https://www.listennotes.com/c/318c0919e1d44a409c8d7e6df3879585/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "be6b21ba8c1a49d1973df83a122699a6",
          "image": "https://production.listennotes.com/podcasts/how-did-this-get-made-earwolf-and-paul-JUagowIb7FC-Gdzh1-KwH27.1400x1400.jpg",
          "title": "How Did This Get Made?",
          "publisher": "Earwolf and Paul Scheer, June Diane Raphael, Jason Mantzoukas",
          "thumbnail": "https://production.listennotes.com/podcasts/how-did-this-get-made-earwolf-and-paul-NfjF8mHCh3n-Gdzh1-KwH27.300x300.jpg",
          "listen_score": 81,
          "listennotes_url": "https://www.listennotes.com/c/be6b21ba8c1a49d1973df83a122699a6/",
          "listen_score_global_rank": "0.01%"
        }
      ],
      "source_url": "https://www.denofgeek.com/podcasts/best-podcasts-like-my-dad-wrote-a-porno/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"Now that worldwide phenomenon My Dad Wrote a Porno has ended, here are some equally funny and scandalous podcasts to enjoy next.\"",
      "pub_date_ms": 1680407072378,
      "source_domain": "www.denofgeek.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/the-best-podcasts-like-my-dad-wrote-a-L415XAvPT7q/"
    },
    {
      "id": "6J1xiuD5Ar4",
      "title": "Top 10 car podcasts",
      "total": 10,
      "podcasts": [
        {
          "id": "9c048773daf9473ea41b66cc4b511f69",
          "image": "https://production.listennotes.com/podcasts/carexpert-carexpertcomau-b92uFdv4c5P-6G4TEZ2f8uD.1400x1400.jpg",
          "title": "CarExpert",
          "publisher": "CarExpert.com.au",
          "thumbnail": "https://production.listennotes.com/podcasts/carexpert-carexpertcomau-xMVpBIP4uK5-6G4TEZ2f8uD.300x300.jpg",
          "listen_score": null,
          "listennotes_url": "https://www.listennotes.com/c/9c048773daf9473ea41b66cc4b511f69/",
          "listen_score_global_rank": null
        },
        {
          "id": "f8439a06fa8b44cf9d3819cf8387d16d",
          "image": "https://production.listennotes.com/podcasts/the-smoking-tire-matt-farah-zack-klapman-K8p_sUTzeCq-8f-yWmvF9I3.1400x1400.jpg",
          "title": "The Smoking Tire",
          "publisher": "Zack Klapman, Matt Farah",
          "thumbnail": "https://production.listennotes.com/podcasts/the-smoking-tire-matt-farah-zack-klapman-6W4e9OMcEJG-8f-yWmvF9I3.300x300.jpg",
          "listen_score": 62,
          "listennotes_url": "https://www.listennotes.com/c/f8439a06fa8b44cf9d3819cf8387d16d/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "e0b6dae4f06e469fb23324bb1bbc3bc8",
          "image": "https://production.listennotes.com/podcasts/spikes-car-radio-spike-feresten-HQDkcE1imLb-7iCcqYe6lMf.1400x1400.jpg",
          "title": "Spike's Car Radio",
          "publisher": "Spike Feresten",
          "thumbnail": "https://production.listennotes.com/podcasts/spikes-car-radio-spike-feresten-0hYvtNx-_wn-7iCcqYe6lMf.300x300.jpg",
          "listen_score": 55,
          "listennotes_url": "https://www.listennotes.com/c/e0b6dae4f06e469fb23324bb1bbc3bc8/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "2be2157b8b1e470abadab4d1d13ebcb8",
          "image": "https://production.listennotes.com/podcasts/the-best-of-car-talk-npr-THOv5fJidPL-53jRscFSlMw.1400x1400.jpg",
          "title": "The Best of Car Talk",
          "publisher": "NPR",
          "thumbnail": "https://production.listennotes.com/podcasts/the-best-of-car-talk-npr-0jrfbFyY-oq-53jRscFSlMw.300x300.jpg",
          "listen_score": 74,
          "listennotes_url": "https://www.listennotes.com/c/2be2157b8b1e470abadab4d1d13ebcb8/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "dbff693d48784154a13d32af5ea22638",
          "image": "https://production.listennotes.com/podcasts/the-drivers-show-paul-maric-and-gordie-waters-DiLHyn1WYAC-swLJ9vhzrnx.1400x1400.jpg",
          "title": "The Driver's Show",
          "publisher": "Paul Maric and Gordie Waters",
          "thumbnail": "https://production.listennotes.com/podcasts/the-drivers-show-paul-maric-and-gordie-waters-wEnZguvDWUY-swLJ9vhzrnx.300x300.jpg",
          "listen_score": 39,
          "listennotes_url": "https://www.listennotes.com/c/dbff693d48784154a13d32af5ea22638/",
          "listen_score_global_rank": "1.5%"
        }
      ],
      "source_url": "https://www.carexpert.com.au/car-news/top-10-car-podcasts?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"These are listed in no particular order. Some are also marked as explicit (with a [E]), so probably best to not have your kids listening while these play in the background!\"",
      "pub_date_ms": 1680026211596,
      "source_domain": "www.carexpert.com.au",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/top-10-car-podcasts-6J1xiuD5Ar4/"
    },
    {
      "id": "znomXUlrsci",
      "title": "Nature Podcasts to Educate",
      "total": 5,
      "podcasts": [
        {
          "id": "184dc14ae8914c14a7fd43001c072610",
          "image": "https://production.listennotes.com/podcasts/birdnote-daily-birdnote-scmP8rvw0Gt-ADlda5NVyqz.1400x1400.jpg",
          "title": "BirdNote Daily",
          "publisher": "BirdNote",
          "thumbnail": "https://production.listennotes.com/podcasts/birdnote-daily-birdnote-TQolx8jWpgO-ADlda5NVyqz.300x300.jpg",
          "listen_score": 56,
          "listennotes_url": "https://www.listennotes.com/c/184dc14ae8914c14a7fd43001c072610/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "8aad569695ca4c0aa5a6b0be4658efee",
          "image": "https://production.listennotes.com/podcasts/bbc-earth-podcast-bbc-earth-Ft-d5cPm6l0-VjTIeYlNOyt.1400x1400.jpg",
          "title": "BBC Earth Podcast",
          "publisher": "BBC Earth",
          "thumbnail": "https://production.listennotes.com/podcasts/bbc-earth-podcast-bbc-earth-AGfiMkbo4-t-VjTIeYlNOyt.300x300.jpg",
          "listen_score": 55,
          "listennotes_url": "https://www.listennotes.com/c/8aad569695ca4c0aa5a6b0be4658efee/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "bb61723cb2464343aa4e835e62d8662b",
          "image": "https://production.listennotes.com/podcasts/park-predators-audiochuck--5KdinCMwxG-vLgRZSsIQ7o.1400x1400.jpg",
          "title": "Park Predators",
          "publisher": "audiochuck",
          "thumbnail": "https://production.listennotes.com/podcasts/park-predators-audiochuck-Y8KgAWXbkRQ-vLgRZSsIQ7o.300x300.jpg",
          "listen_score": 72,
          "listennotes_url": "https://www.listennotes.com/c/bb61723cb2464343aa4e835e62d8662b/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "ba10ceb784b642c0a234e96e8d39432f",
          "image": "https://production.listennotes.com/podcasts/tooth-claw-true-stories-of-animal-attacks-ksm3rlSdqL8-c5LijYmN1dE.1400x1400.jpg",
          "title": "Tooth & Claw: True Stories of Animal Attacks",
          "publisher": "Wes Larson, Jeff Larson, Mike Smith | QCODE",
          "thumbnail": "https://production.listennotes.com/podcasts/tooth-claw-true-stories-of-animal-attacks-95gpEs1A0Ta-c5LijYmN1dE.300x300.jpg",
          "listen_score": 62,
          "listennotes_url": "https://www.listennotes.com/c/ba10ceb784b642c0a234e96e8d39432f/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "8af72a8efd37477d9cbbfaede5c3042e",
          "image": "https://production.listennotes.com/podcasts/outside-voices-D0AdQ6shxNo-LKAp71aJ0zt.1400x1400.jpg",
          "title": "Outside Voices Podcast",
          "publisher": "Resource Media",
          "thumbnail": "https://production.listennotes.com/podcasts/outside-voices-gaIiC26QJvx-LKAp71aJ0zt.300x300.jpg",
          "listen_score": 39,
          "listennotes_url": "https://www.listennotes.com/c/8af72a8efd37477d9cbbfaede5c3042e/",
          "listen_score_global_rank": "2%"
        }
      ],
      "source_url": "https://www.greenmatters.com/living/nature-podcasts?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"From educational conservation-based series, to true crime, there's a wide range of genres on our list. And each will immerse you in the great outdoors \u2014 whether you're on a walk, commuting, or simply sitting on the couch.\"",
      "pub_date_ms": 1680026018088,
      "source_domain": "www.greenmatters.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/nature-podcasts-to-educate-znomXUlrsci/"
    },
    {
      "id": "TmLObBagd92",
      "title": "These Filmmaking Podcasts Will Change the Way You Make Movies",
      "total": 12,
      "podcasts": [
        {
          "id": "28be0efa943449019e6c305dc4a60c7f",
          "image": "https://production.listennotes.com/podcasts/the-a24-podcast-a24-2QLYrzFhvkU-vzW69M_g3jO.1400x1400.jpg",
          "title": "The A24 Podcast",
          "publisher": "A24",
          "thumbnail": "https://production.listennotes.com/podcasts/the-a24-podcast-a24-yfsQE5gvzVh-vzW69M_g3jO.300x300.jpg",
          "listen_score": 57,
          "listennotes_url": "https://www.listennotes.com/c/28be0efa943449019e6c305dc4a60c7f/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "64129ee64c4c4f89844cfaa3e9e69ab2",
          "image": "https://production.listennotes.com/podcasts/awards-chatter-the-hollywood-reporter-8gwM53CDbAr-bzympGoXZiw.1400x1400.jpg",
          "title": "Awards Chatter",
          "publisher": "The Hollywood Reporter",
          "thumbnail": "https://production.listennotes.com/podcasts/awards-chatter-the-hollywood-reporter-BwdEsHozn5q-bzympGoXZiw.300x300.jpg",
          "listen_score": 59,
          "listennotes_url": "https://www.listennotes.com/c/64129ee64c4c4f89844cfaa3e9e69ab2/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "59f99a54c3a94ab9813ffcf7d6ed17a7",
          "image": "https://production.listennotes.com/podcasts/write-on-a-screenwriting-podcast-final-draft-41_vhUxtske-hm5S4dBp917.1400x787.jpg",
          "title": "Write On: A Screenwriting Podcast",
          "publisher": "Final Draft",
          "thumbnail": "https://production.listennotes.com/podcasts/write-on-a-screenwriting-podcast-final-draft-P8AMFVT3Xn--hm5S4dBp917.300x168.jpg",
          "listen_score": 43,
          "listennotes_url": "https://www.listennotes.com/c/59f99a54c3a94ab9813ffcf7d6ed17a7/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "f77403bfbf0b4680a5bf19557342392f",
          "image": "https://production.listennotes.com/podcasts/the-rewatchables-the-ringer-cDsu24f8WTL-HV0-qYTQl3c.1400x1400.jpg",
          "title": "The Rewatchables",
          "publisher": "The Ringer",
          "thumbnail": "https://production.listennotes.com/podcasts/the-rewatchables-the-ringer-yHOrqaYxS_b-HV0-qYTQl3c.300x300.jpg",
          "listen_score": 76,
          "listennotes_url": "https://www.listennotes.com/c/f77403bfbf0b4680a5bf19557342392f/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "c7d57311a1174b94a37aa02cf7feb9e1",
          "image": "https://production.listennotes.com/podcasts/i-saw-what-you-did-exactly-right-3OMCBirQb2e-VpjLgZG7DTu.1400x1400.jpg",
          "title": "I Saw What You Did",
          "publisher": "Exactly Right",
          "thumbnail": "https://production.listennotes.com/podcasts/i-saw-what-you-did-exactly-right-Ufn8r5dAb1x-VpjLgZG7DTu.300x300.jpg",
          "listen_score": 62,
          "listennotes_url": "https://www.listennotes.com/c/c7d57311a1174b94a37aa02cf7feb9e1/",
          "listen_score_global_rank": "0.1%"
        }
      ],
      "source_url": "https://screencraft.org/blog/filmmaking-podcasts-change-the-way-you-make-movies/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"If you're not listening to these great filmmaking podcasts, you're seriously missing out.\"",
      "pub_date_ms": 1680025886383,
      "source_domain": "screencraft.org",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/these-filmmaking-podcasts-will-change-TmLObBagd92/"
    },
    {
      "id": "FUMor-0Tbdn",
      "title": "16 Tech Experts Share Their Favorite Tech-Focused Podcasts",
      "total": 16,
      "podcasts": [
        {
          "id": "c5ce6c02cbf1486496206829f7d42e8e",
          "image": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-syLJP5rimSp-kmx0XIZTAys.1400x1400.jpg",
          "title": "The Best One Yet",
          "publisher": "Nick & Jack Studios",
          "thumbnail": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-YPWcDaHknUz-kmx0XIZTAys.300x300.jpg",
          "listen_score": 71,
          "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "6564539c383449029020fb3c4dc8e8d1",
          "image": "https://production.listennotes.com/podcasts/build-with-blake-bartlett-openview-venture-3qsGIr1Mm2p-JY8xHQcOL7o.1400x1400.jpg",
          "title": "BUILD with Blake Bartlett",
          "publisher": "OpenView Venture Partners",
          "thumbnail": "https://production.listennotes.com/podcasts/build-with-blake-bartlett-openview-venture-bv1y5V_wUMl-JY8xHQcOL7o.300x300.jpg",
          "listen_score": 43,
          "listennotes_url": "https://www.listennotes.com/c/6564539c383449029020fb3c4dc8e8d1/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "e3794af26c2140e2ac74d00395e59201",
          "image": "https://production.listennotes.com/podcasts/darknet-diaries-jack-rhysider-8vOdxXD6QTr-ztuNyvC2F_O.1400x1400.jpg",
          "title": "Darknet Diaries",
          "publisher": "Jack Rhysider",
          "thumbnail": "https://production.listennotes.com/podcasts/darknet-diaries-jack-rhysider-2j15fXqn0w9-ztuNyvC2F_O.300x300.jpg",
          "listen_score": 74,
          "listennotes_url": "https://www.listennotes.com/c/e3794af26c2140e2ac74d00395e59201/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "0bb97ed16ae44434b8528d8d9a33ece2",
          "image": "https://production.listennotes.com/podcasts/drzerotrust-gW4J5Cn8Tej-DUzt2WO6rCK.1400x1400.jpg",
          "title": "DrZeroTrust",
          "publisher": "Chase Cunningham",
          "thumbnail": "https://production.listennotes.com/podcasts/drzerotrust-sgGTPUE7A4c-DUzt2WO6rCK.300x300.jpg",
          "listen_score": 25,
          "listennotes_url": "https://www.listennotes.com/c/0bb97ed16ae44434b8528d8d9a33ece2/",
          "listen_score_global_rank": "10%"
        },
        {
          "id": "c3c933b6d22d4a06b236e5493b4603cc",
          "image": "https://production.listennotes.com/podcasts/hard-fork-the-new-york-times-vEr0edDkOFp-M2AZCUFvHzY.1400x1400.jpg",
          "title": "Hard Fork",
          "publisher": "The New York Times",
          "thumbnail": "https://production.listennotes.com/podcasts/hard-fork-the-new-york-times-mwetHTuP2Az-M2AZCUFvHzY.300x300.jpg",
          "listen_score": 66,
          "listennotes_url": "https://www.listennotes.com/c/c3c933b6d22d4a06b236e5493b4603cc/",
          "listen_score_global_rank": "0.05%"
        }
      ],
      "source_url": "https://www.forbes.com/sites/forbestechcouncil/2023/03/28/16-tech-experts-share-their-favorite-tech-focused-podcasts/?sh=18504812655e&utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"From deep dives into the latest tech news to interviews with top tech experts, these podcasts offer a wealth of knowledge and insights for anyone interested in the tech industry.\"",
      "pub_date_ms": 1680025767630,
      "source_domain": "www.forbes.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/16-tech-experts-share-their-favorite-FUMor-0Tbdn/"
    },
    {
      "id": "ESjphawK0zN",
      "title": "Best Cryptocurrency Podcasts for Traders in 2023",
      "total": 10,
      "podcasts": [
        {
          "id": "3035855c61044f8cbb9cab4d6d4712e9",
          "image": "https://production.listennotes.com/podcasts/the-breakdown-nathaniel-whittemore-x9ET_6BWtse-WDqMy-FNJPp.1400x1400.jpg",
          "title": "The Breakdown",
          "publisher": "Nathaniel Whittemore",
          "thumbnail": "https://production.listennotes.com/podcasts/the-breakdown-nathaniel-whittemore-ZTD-gW4A2r5-WDqMy-FNJPp.300x300.jpg",
          "listen_score": 55,
          "listennotes_url": "https://www.listennotes.com/c/3035855c61044f8cbb9cab4d6d4712e9/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "e6907bd41a0f4ceca8edc81f305f4c93",
          "image": "https://production.listennotes.com/podcasts/unchained-laura-shin-F-rjz7XLZ9m-8W2AXkU7NYf.1400x1400.jpg",
          "title": "Unchained",
          "publisher": "Laura Shin",
          "thumbnail": "https://production.listennotes.com/podcasts/unchained-laura-shin-OcGLDAdz0wq-8W2AXkU7NYf.300x300.jpg",
          "listen_score": 62,
          "listennotes_url": "https://www.listennotes.com/c/e6907bd41a0f4ceca8edc81f305f4c93/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "4104fab13a6f4cb39b90a09a8c25d8d8",
          "image": "https://production.listennotes.com/podcasts/what-bitcoin-did-with-peter-mccormack-peter-LAGPzj25-Sn-4n2D3d67Yxk.1400x1400.jpg",
          "title": "What Bitcoin Did with Peter McCormack",
          "publisher": "Peter McCormack",
          "thumbnail": "https://production.listennotes.com/podcasts/what-bitcoin-did-with-peter-mccormack-peter-spBqw0l9CYg-4n2D3d67Yxk.300x300.jpg",
          "listen_score": 66,
          "listennotes_url": "https://www.listennotes.com/c/4104fab13a6f4cb39b90a09a8c25d8d8/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "dcd55e314de84730b43db674e562deb8",
          "image": "https://production.listennotes.com/podcasts/the-bad-crypto-podcast-joel-comm-and-travis-l0EOQqkspoi-mj-e0z67gol.1400x1400.jpg",
          "title": "The Bad Crypto Podcast",
          "publisher": "Joel Comm and Travis Wright",
          "thumbnail": "https://production.listennotes.com/podcasts/the-bad-crypto-podcast-joel-comm-and-travis-Sr0lj3RdZQ4-mj-e0z67gol.300x300.jpg",
          "listen_score": 61,
          "listennotes_url": "https://www.listennotes.com/c/dcd55e314de84730b43db674e562deb8/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "f405bce4ab6f43439892b80e3a2d34be",
          "image": "https://production.listennotes.com/podcasts/bankless-bankless-rGmB0uzeqLa-ukgFt3i7N-d.1400x1400.jpg",
          "title": "Bankless",
          "publisher": "Bankless",
          "thumbnail": "https://production.listennotes.com/podcasts/bankless-bankless-atflB2pFJ3Q-ukgFt3i7N-d.300x300.jpg",
          "listen_score": 59,
          "listennotes_url": "https://www.listennotes.com/c/f405bce4ab6f43439892b80e3a2d34be/",
          "listen_score_global_rank": "0.1%"
        }
      ],
      "source_url": "https://www.analyticsinsight.net/best-cryptocurrency-podcasts-for-traders-in-2023/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"Ready to learn about all things crypto? Check out these fantastic cryptocurrency podcasts that can educate and entertain you in 2023!\"",
      "pub_date_ms": 1680025467000,
      "source_domain": "www.analyticsinsight.net",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/best-cryptocurrency-podcasts-for-ESjphawK0zN/"
    },
    {
      "id": "OLQRys6phcb",
      "title": "10 best sports betting podcasts",
      "total": 10,
      "podcasts": [
        {
          "id": "d0137f7c41be40e6953614133f19762a",
          "image": "https://production.listennotes.com/podcasts/bet-the-board-payne-insider-and-todd-fuhrman-Nh7Qa2SKFdG-Ecgu326Tksl.1400x1400.jpg",
          "title": "Bet The Board",
          "publisher": "Payne Insider and Todd Fuhrman | Wondery",
          "thumbnail": "https://production.listennotes.com/podcasts/bet-the-board-payne-insider-and-todd-fuhrman-Q3hkM-mUTZo-Ecgu326Tksl.300x300.jpg",
          "listen_score": 59,
          "listennotes_url": "https://www.listennotes.com/c/d0137f7c41be40e6953614133f19762a/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "4cc0368263394cf8a75953f89860fba9",
          "image": "https://production.listennotes.com/podcasts/barstool-pick-em-barstool-sports-v1BKyGUFia9-cVCOy4UHWGv.1400x1400.jpg",
          "title": "Barstool Pick Em",
          "publisher": "Barstool Sports",
          "thumbnail": "https://production.listennotes.com/podcasts/barstool-pick-em-barstool-sports-OcsyUAmT3VN-cVCOy4UHWGv.300x300.jpg",
          "listen_score": 58,
          "listennotes_url": "https://www.listennotes.com/c/4cc0368263394cf8a75953f89860fba9/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "68c6bcb0bc1a4bc09076a5f760ac8ce7",
          "image": "https://production.listennotes.com/podcasts/you-better-you-bet-audacy-Gy2DT4lMZbk-8nlQeBCMPTh.1400x1400.jpg",
          "title": "You Better You Bet",
          "publisher": "Audacy",
          "thumbnail": "https://production.listennotes.com/podcasts/you-better-you-bet-audacy-5-j2r1E_TGa-8nlQeBCMPTh.300x300.jpg",
          "listen_score": 56,
          "listennotes_url": "https://www.listennotes.com/c/68c6bcb0bc1a4bc09076a5f760ac8ce7/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "c79bd0d06acb4fdfbbb0fa9f4f0d13f0",
          "image": "https://production.listennotes.com/podcasts/hammer-dahn-pat-mcafee-1nc-ntf2E8iH76U-xQyJHYCuDwO.1400x1400.jpg",
          "title": "Hammer Dahn - Sports Betting",
          "publisher": "Pat McAfee 1nc.",
          "thumbnail": "https://production.listennotes.com/podcasts/hammer-dahn-pat-mcafee-1nc-Euh24YaHAbC-xQyJHYCuDwO.300x300.jpg",
          "listen_score": 53,
          "listennotes_url": "https://www.listennotes.com/c/c79bd0d06acb4fdfbbb0fa9f4f0d13f0/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "1d0082302fa44cc3adb236ae8f5f44a3",
          "image": "https://production.listennotes.com/podcasts/bet-the-process-bet-the-process-a_BDF2UxMZY-Nys0TgDw4Ld.400x400.jpg",
          "title": "Bet The Process",
          "publisher": "Bet The Process",
          "thumbnail": "https://production.listennotes.com/podcasts/bet-the-process-bet-the-process-pmHcJIEFPbK-Nys0TgDw4Ld.300x300.jpg",
          "listen_score": 49,
          "listennotes_url": "https://www.listennotes.com/c/1d0082302fa44cc3adb236ae8f5f44a3/",
          "listen_score_global_rank": "0.5%"
        }
      ],
      "source_url": "https://franchisesports.co.uk/best-sports-betting-podcasts/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"The top sports gambling podcasts are a combination of expert analysis, entertainment, and information. Listening to these podcasts gives you insight into strategies that can help you make better-informed betting decisions. Moreover, these podcasts aren\u2019t just pure numbers. They can also be fun and entertaining.\"",
      "pub_date_ms": 1680025583956,
      "source_domain": "franchisesports.co.uk",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/10-best-sports-betting-podcasts-OLQRys6phcb/"
    },
    {
      "id": "aTHb63KI-eU",
      "title": "The Top 7 AI Podcasts You Need To Hear Now",
      "total": 7,
      "podcasts": [
        {
          "id": "51f6ce503750485ba02bb60193feef49",
          "image": "https://production.listennotes.com/podcasts/the-twiml-ai-podcast-formerly-this-week-in-jPedLfZBQmT-KCJYSHz9orX.1400x1400.jpg",
          "title": "The TWIML AI Podcast (formerly This Week in Machine Learning & Artificial Intelligence)",
          "publisher": "Sam Charrington",
          "thumbnail": "https://production.listennotes.com/podcasts/the-twiml-ai-podcast-formerly-this-week-in-Nv7hEIQFlrB-KCJYSHz9orX.300x300.jpg",
          "listen_score": 54,
          "listennotes_url": "https://www.listennotes.com/c/51f6ce503750485ba02bb60193feef49/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "72beb0c368ba4e9e97f6fdbf52d0094d",
          "image": "https://production.listennotes.com/podcasts/the-bad-ai-show-bxP3ROUwV54-a5FCxrt8PR9.1400x1400.jpg",
          "title": "The Bad AI Show",
          "publisher": "Joel Comm & Travis Wright",
          "thumbnail": "https://production.listennotes.com/podcasts/the-bad-ai-show-WeioFkIf5UO-a5FCxrt8PR9.300x300.jpg",
          "listen_score": 28,
          "listennotes_url": "https://www.listennotes.com/c/72beb0c368ba4e9e97f6fdbf52d0094d/",
          "listen_score_global_rank": "10%"
        },
        {
          "id": "fa06c55be2244e22a0e263c8560ece47",
          "image": "https://production.listennotes.com/podcasts/the-ai-podcast-nvidia-DCc4vTZ08s9-8WS6JPYmMvj.497x497.jpg",
          "title": "The AI Podcast",
          "publisher": "NVIDIA",
          "thumbnail": "https://production.listennotes.com/podcasts/the-ai-podcast-nvidia-Le_jn0a8UtG-8WS6JPYmMvj.300x300.jpg",
          "listen_score": 48,
          "listennotes_url": "https://www.listennotes.com/c/fa06c55be2244e22a0e263c8560ece47/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "dead7a0cea9548ebab9ed6596cd233aa",
          "image": "https://production.listennotes.com/podcasts/data-skeptic-kyle-polich-CeUYHpSbi-y-potOlIZJGuH.1400x1400.jpg",
          "title": "Data Skeptic",
          "publisher": "Kyle Polich",
          "thumbnail": "https://production.listennotes.com/podcasts/data-skeptic-kyle-polich-N25OG-PMf73-potOlIZJGuH.300x300.jpg",
          "listen_score": 55,
          "listennotes_url": "https://www.listennotes.com/c/dead7a0cea9548ebab9ed6596cd233aa/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "e8bbabc7446043d9b39132bf88eccdd8",
          "image": "https://production.listennotes.com/podcasts/ai-in-business-daniel-faggella-7MtEgSuUTOo-qfQ5EPYKyvk.1400x1400.jpg",
          "title": "The AI in Business Podcast",
          "publisher": "Daniel Faggella",
          "thumbnail": "https://production.listennotes.com/podcasts/ai-in-business-daniel-faggella-Vry0_2UpwQk-qfQ5EPYKyvk.300x300.jpg",
          "listen_score": 46,
          "listennotes_url": "https://www.listennotes.com/c/e8bbabc7446043d9b39132bf88eccdd8/",
          "listen_score_global_rank": "1%"
        }
      ],
      "source_url": "https://readwrite.com/the-top-ai-podcasts-you-need-to-hear-now/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"We\u2019ve brought together a list of seven of the top podcasts that track and explain the newest developments. They look behind the scenes at the technology behind the platforms, and they discuss how artificial intelligence is already upending business, marketing, data analysis, and more.\"",
      "pub_date_ms": 1679789132830,
      "source_domain": "readwrite.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/the-top-7-ai-podcasts-you-need-to-hear-aTHb63KI-eU/"
    },
    {
      "id": "wlv9bFuxUoq",
      "title": "Top Canadian Podcasts Ranked",
      "total": 8,
      "podcasts": [
        {
          "id": "d31a63613c5c461cb4b400f8f61d7362",
          "image": "https://production.listennotes.com/podcasts/dateline-nbc-nbc-news--jTk9Zr2z6Q-aSOM3Nln0KL.1400x1400.jpg",
          "title": "Dateline NBC",
          "publisher": "NBC News",
          "thumbnail": "https://production.listennotes.com/podcasts/dateline-nbc-nbc-news-24WUN1Ovahp-aSOM3Nln0KL.300x300.jpg",
          "listen_score": 81,
          "listennotes_url": "https://www.listennotes.com/c/d31a63613c5c461cb4b400f8f61d7362/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "0d3bc91908054d69b3d8aefc35258163",
          "image": "https://production.listennotes.com/podcasts/front-burner-cbc-podcasts-6xIQiLaG2qN-BkJbKvn2rh8.1400x1400.jpg",
          "title": "Front Burner",
          "publisher": "CBC Podcasts",
          "thumbnail": "https://production.listennotes.com/podcasts/front-burner-cbc-podcasts-xpy14G7YmzS-BkJbKvn2rh8.300x300.jpg",
          "listen_score": 63,
          "listennotes_url": "https://www.listennotes.com/c/0d3bc91908054d69b3d8aefc35258163/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "e656340496fb4b2f93a9382027ec1156",
          "image": "https://production.listennotes.com/podcasts/the-current-cbc-radio-efCbgdkuwqO-dM2uzYTI_56.1400x1400.jpg",
          "title": "The Current",
          "publisher": "CBC Radio",
          "thumbnail": "https://production.listennotes.com/podcasts/the-current-cbc-radio-EyX8PLbSwoq-dM2uzYTI_56.300x300.jpg",
          "listen_score": 58,
          "listennotes_url": "https://www.listennotes.com/c/e656340496fb4b2f93a9382027ec1156/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "68ed9ef3aef74d028cf0b2faf141b31d",
          "image": "https://production.listennotes.com/podcasts/cbc-news-the-world-this-hour-cbc-news-the-lTOXu8n-Eia-NneUcwhy_XB.1400x1400.jpg",
          "title": "CBC News: The World This Hour",
          "publisher": "CBC News: The World This Hour",
          "thumbnail": "https://production.listennotes.com/podcasts/cbc-news-the-world-this-hour-cbc-news-the-Qri-8DS5E9Y-NneUcwhy_XB.300x300.jpg",
          "listen_score": 51,
          "listennotes_url": "https://www.listennotes.com/c/68ed9ef3aef74d028cf0b2faf141b31d/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "60d38482c845400b9527c81bbebada50",
          "image": "https://production.listennotes.com/podcasts/f1-beyond-the-grid-formula-1-cKTdntQlOI8-UtYmp2y35cA.1400x1400.jpg",
          "title": "F1: Beyond The Grid",
          "publisher": "Formula 1",
          "thumbnail": "https://production.listennotes.com/podcasts/f1-beyond-the-grid-formula-1--D4FJpUfziG-UtYmp2y35cA.300x300.jpg",
          "listen_score": 68,
          "listennotes_url": "https://www.listennotes.com/c/60d38482c845400b9527c81bbebada50/",
          "listen_score_global_rank": "0.05%"
        }
      ],
      "source_url": "https://radioink.com/2023/03/22/top-canadian-podcasts-ranked/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"The latest Canada Podcast Ranker from Triton Digital\u00ae for the February 2023 reporting period has been released. There were 14.3 million average weekly podcast downloads for the month\"",
      "pub_date_ms": 1679789034123,
      "source_domain": "radioink.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/top-canadian-podcasts-ranked-wlv9bFuxUoq/"
    },
    {
      "id": "Z3EF7adI2up",
      "title": "Five best true crime podcasts in 2023",
      "total": 5,
      "podcasts": [
        {
          "id": "6d2ab9d90973430dbec3c5c24e689f00",
          "image": "https://production.listennotes.com/podcasts/serial-serial-productions-the-new-york-times-DUZXYIf3sqw-V1NRH-2wzoB.1400x1400.jpg",
          "title": "Serial",
          "publisher": "Serial Productions & The New York Times",
          "thumbnail": "https://production.listennotes.com/podcasts/serial-serial-productions-the-new-york-times-RgmG8YyL-nk-V1NRH-2wzoB.300x300.jpg",
          "listen_score": 89,
          "listennotes_url": "https://www.listennotes.com/c/6d2ab9d90973430dbec3c5c24e689f00/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "873414cf0efe4efebb20f467aa0f28b2",
          "image": "https://production.listennotes.com/podcasts/my-favorite-murder-with-karen-kilgariff-and-F3YIV0w2usX-nUHfdZot1PQ.1400x1400.jpg",
          "title": "My Favorite Murder with Karen Kilgariff and Georgia Hardstark",
          "publisher": "Exactly Right",
          "thumbnail": "https://production.listennotes.com/podcasts/my-favorite-murder-with-karen-kilgariff-and-MF9LXOkt-YT-nUHfdZot1PQ.300x300.jpg",
          "listen_score": 94,
          "listennotes_url": "https://www.listennotes.com/c/873414cf0efe4efebb20f467aa0f28b2/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "581fc67e281047d09fa90f7782c51feb",
          "image": "https://production.listennotes.com/podcasts/dirty-john-los-angeles-times-wondery-qHhortA1ZYR-1rJzL4wEyuY.1400x1400.jpg",
          "title": "Dirty John",
          "publisher": "Los Angeles Times | Wondery",
          "thumbnail": "https://production.listennotes.com/podcasts/dirty-john-los-angeles-times-wondery-qZAerlh56VY-1rJzL4wEyuY.300x300.jpg",
          "listen_score": 83,
          "listennotes_url": "https://www.listennotes.com/c/581fc67e281047d09fa90f7782c51feb/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "73771979c7ba4ed183129d7823210c17",
          "image": "https://production.listennotes.com/podcasts/welcome-to-your-fantasy-pineapple-street-FvIN9qApiOV-QlbekzVnCor.1400x1400.jpg",
          "title": "Welcome to Your Fantasy",
          "publisher": "Pineapple Street Studios / Gimlet",
          "thumbnail": "https://production.listennotes.com/podcasts/welcome-to-your-fantasy-pineapple-street-NTtiZ-WRulK-QlbekzVnCor.300x300.jpg",
          "listen_score": 50,
          "listennotes_url": "https://www.listennotes.com/c/73771979c7ba4ed183129d7823210c17/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "60b14e297a9142f4b2ab885bd3d1bfb8",
          "image": "https://production.listennotes.com/podcasts/someone-knows-something-cbc-podcasts-zks_Sm7HAW8-e9j723ECnps.1400x1400.jpg",
          "title": "Someone Knows Something",
          "publisher": "CBC Podcasts",
          "thumbnail": "https://production.listennotes.com/podcasts/someone-knows-something-cbc-podcasts-YiSf-XsBeF0-e9j723ECnps.300x300.jpg",
          "listen_score": 81,
          "listennotes_url": "https://www.listennotes.com/c/60b14e297a9142f4b2ab885bd3d1bfb8/",
          "listen_score_global_rank": "0.01%"
        }
      ],
      "source_url": "https://opoyi.com/entertainment/five-best-true-crime-podcasts-in-2023/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"Here are five of the best true crime podcasts to get you started:\"",
      "pub_date_ms": 1679788901902,
      "source_domain": "opoyi.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/five-best-true-crime-podcasts-in-2023-Z3EF7adI2up/"
    },
    {
      "id": "rPZ6yNWYIbm",
      "title": "Top 10 best Irish PODCASTS in 2023, RANKED",
      "total": 9,
      "podcasts": [
        {
          "id": "a148a10198bb4500b2ea40e33fadcab2",
          "image": "https://production.listennotes.com/podcasts/talking-bollox-podcast-goloud-CZXwlSRmpYa-d5gUwHTJXQo.1400x1400.jpg",
          "title": "Talking Bollox Podcast",
          "publisher": "GoLoud",
          "thumbnail": "https://production.listennotes.com/podcasts/talking-bollox-podcast-goloud--9GbSgluC71-d5gUwHTJXQo.300x300.jpg",
          "listen_score": 40,
          "listennotes_url": "https://www.listennotes.com/c/a148a10198bb4500b2ea40e33fadcab2/",
          "listen_score_global_rank": "1.5%"
        },
        {
          "id": "d9af2512490e4babbce52689af7525d4",
          "image": "https://production.listennotes.com/podcasts/that-chapter-podcast-that-chapter-5vkyP9hMSop-Y0VhXeDJrny.1400x1400.jpg",
          "title": "That Chapter Podcast",
          "publisher": "That Chapter",
          "thumbnail": "https://production.listennotes.com/podcasts/that-chapter-podcast-that-chapter-VesMm2pbnxO-Y0VhXeDJrny.300x300.jpg",
          "listen_score": 65,
          "listennotes_url": "https://www.listennotes.com/c/d9af2512490e4babbce52689af7525d4/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "d2fe4a103ee3441aafa8f3c94ad25341",
          "image": "https://production.listennotes.com/podcasts/mens-rea-a-true-crime-podcast-mens-rea-true-ydHXcrlM67F-nCLVlx2mQD-.1400x1400.jpg",
          "title": "Mens Rea: A true crime podcast",
          "publisher": "Mens Rea True Crime",
          "thumbnail": "https://production.listennotes.com/podcasts/mens-rea-a-true-crime-podcast-mens-rea-true-4P68i1udWbX-nCLVlx2mQD-.300x300.jpg",
          "listen_score": 60,
          "listennotes_url": "https://www.listennotes.com/c/d2fe4a103ee3441aafa8f3c94ad25341/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "605778a38ecd43f69ef844aead56d39d",
          "image": "https://production.listennotes.com/podcasts/im-grand-mam-kevin-twomey-and-pj-kirby-rH0XqL_t1ow-Ei8H_mcjp-J.1400x1400.jpg",
          "title": "I'm Grand Mam",
          "publisher": "Kevin Twomey and PJ Kirby",
          "thumbnail": "https://production.listennotes.com/podcasts/im-grand-mam-kevin-twomey-and-pj-kirby-jsQyNIi3B9S-Ei8H_mcjp-J.300x300.jpg",
          "listen_score": 52,
          "listennotes_url": "https://www.listennotes.com/c/605778a38ecd43f69ef844aead56d39d/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "df69a48cccca47049d64fde0c9137116",
          "image": "https://production.listennotes.com/podcasts/and-another-thing-with-dave-dave-smith--srY3VqziP8-93Qt5Vdw_G6.1400x1400.jpg",
          "title": "And Another Thing with Dave",
          "publisher": "Dave Smith",
          "thumbnail": "https://production.listennotes.com/podcasts/and-another-thing-with-dave-dave-smith-1rAdDeJRGiz-93Qt5Vdw_G6.300x300.jpg",
          "listen_score": 25,
          "listennotes_url": "https://www.listennotes.com/c/df69a48cccca47049d64fde0c9137116/",
          "listen_score_global_rank": "10%"
        }
      ],
      "source_url": "https://meanwhileinireland.com/best-irish-podcasts-2023/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"There\u2019s a podcast to suit everybody\u2019s tastes, so we\u2019ve ranked the best Irish podcasts of 2023. Read on and discover your next new audio obsession to binge listen.\"",
      "pub_date_ms": 1679788803261,
      "source_domain": "meanwhileinireland.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/top-10-best-irish-podcasts-in-2023-rPZ6yNWYIbm/"
    },
    {
      "id": "cZL3VHSvO2Y",
      "title": "Military podcasts you need in your life",
      "total": 13,
      "podcasts": [
        {
          "id": "fe87c2248762410eaf3b35d4a22869f2",
          "image": "https://production.listennotes.com/podcasts/military-matters-stars-and-stripes-WZaApVj1Ln6-ArtLhFJnS5j.1400x1400.jpg",
          "title": "Military Matters",
          "publisher": "Stars and Stripes",
          "thumbnail": "https://production.listennotes.com/podcasts/military-matters-stars-and-stripes-Y4FD17yN3Co-ArtLhFJnS5j.300x300.jpg",
          "listen_score": 38,
          "listennotes_url": "https://www.listennotes.com/c/fe87c2248762410eaf3b35d4a22869f2/",
          "listen_score_global_rank": "2%"
        },
        {
          "id": "c36aea82bf344a458f607c2859606838",
          "image": "https://production.listennotes.com/podcasts/defense-one-radio-defense-one-staff-Wf748xhqEOp-16qvBekwLS4.1400x1400.jpg",
          "title": "Defense One Radio",
          "publisher": "Defense One staff",
          "thumbnail": "https://production.listennotes.com/podcasts/defense-one-radio-defense-one-staff-PAUtRgL6Dz_-16qvBekwLS4.300x300.jpg",
          "listen_score": 40,
          "listennotes_url": "https://www.listennotes.com/c/c36aea82bf344a458f607c2859606838/",
          "listen_score_global_rank": "1.5%"
        },
        {
          "id": "658b13f1769449f89b937754c17feee4",
          "image": "https://production.listennotes.com/podcasts/dan-carlins-hardcore-history-dan-carlin-zJPGhpdXYZf-THDlEiZ9tbB.1400x1400.jpg",
          "title": "Dan Carlin's Hardcore History",
          "publisher": "Dan Carlin",
          "thumbnail": "https://production.listennotes.com/podcasts/dan-carlins-hardcore-history-dan-carlin-2U87isnyHrA-THDlEiZ9tbB.300x300.jpg",
          "listen_score": 88,
          "listennotes_url": "https://www.listennotes.com/c/658b13f1769449f89b937754c17feee4/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "241afd25f27c4c5e8775d2a6efd82f3c",
          "image": "https://production.listennotes.com/podcasts/dan-snows-history-hit-history-hit-fnxh-PJF291-Ps7dHtO6cDG.1400x1400.jpg",
          "title": "Dan Snow's History Hit",
          "publisher": "History Hit",
          "thumbnail": "https://production.listennotes.com/podcasts/dan-snows-history-hit-history-hit-O0SIPGFhu63-Ps7dHtO6cDG.300x300.jpg",
          "listen_score": 74,
          "listennotes_url": "https://www.listennotes.com/c/241afd25f27c4c5e8775d2a6efd82f3c/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "690e97c6c3704cf8a95272a8aafb1615",
          "image": "https://production.listennotes.com/podcasts/war-stories-official-podcast-war-stories-h2VUZgDEBGe-DEXdRlh-B7t.1400x1400.jpg",
          "title": "War Stories Official Podcast",
          "publisher": "War Stories Official",
          "thumbnail": "https://production.listennotes.com/podcasts/war-stories-official-podcast-war-stories-hWSpj1eDiZu-DEXdRlh-B7t.300x300.jpg",
          "listen_score": 46,
          "listennotes_url": "https://www.listennotes.com/c/690e97c6c3704cf8a95272a8aafb1615/",
          "listen_score_global_rank": "1%"
        }
      ],
      "source_url": "https://www.wearethemighty.com/mighty-culture/military-podcasts-you-need-in-your-life/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"We\u2019ve scoured the internet and compiled a list of the best military podcasts out there. From current events and policy to personal experiences and mental health, there\u2019s something for everyone. So, grab your headphones, tune in, and join the conversation!\"",
      "pub_date_ms": 1679788662256,
      "source_domain": "www.wearethemighty.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/military-podcasts-you-need-in-your-life-cZL3VHSvO2Y/"
    },
    {
      "id": "KYDhmAOnPNB",
      "title": "14 Black Podcasts To Listen To This Spring",
      "total": 14,
      "podcasts": [
        {
          "id": "40ab86e83ed944cca6ef76a7a3d6b0d4",
          "image": "https://production.listennotes.com/podcasts/side-hustle-pro-nicaila-matthews-okome-R4LUY7HtQr--LJrh0xVaAZ4.1400x1400.jpg",
          "title": "Side Hustle Pro",
          "publisher": "Nicaila Matthews Okome",
          "thumbnail": "https://production.listennotes.com/podcasts/side-hustle-pro-nicaila-matthews-okome-TM1qcWl-x3R-LJrh0xVaAZ4.300x300.jpg",
          "listen_score": 61,
          "listennotes_url": "https://www.listennotes.com/c/40ab86e83ed944cca6ef76a7a3d6b0d4/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "94fa1b17b53f4c938da1a1ce6a57b2db",
          "image": "https://production.listennotes.com/podcasts/girl-stop-playin-podcast-koereyelle-GZYtnWAbQC_-3YfLDGgO8uk.1400x1400.jpg",
          "title": "Girl Stop Playin Podcast",
          "publisher": "Koereyelle",
          "thumbnail": "https://production.listennotes.com/podcasts/girl-stop-playin-podcast-koereyelle-Ru4dnb-PgBk-3YfLDGgO8uk.300x300.jpg",
          "listen_score": 49,
          "listennotes_url": "https://www.listennotes.com/c/94fa1b17b53f4c938da1a1ce6a57b2db/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "ad780d7a26f248db87ed973c0a0e8990",
          "image": "https://production.listennotes.com/podcasts/pour-minds-podcast-85-south-media-nZgeCi6QMpN-LHcniIMB-VF.1400x1400.jpg",
          "title": "Pour Minds Podcast",
          "publisher": "85 South Media",
          "thumbnail": "https://production.listennotes.com/podcasts/pour-minds-podcast-85-south-media-1Bq-nc8XQer-LHcniIMB-VF.300x300.jpg",
          "listen_score": 58,
          "listennotes_url": "https://www.listennotes.com/c/ad780d7a26f248db87ed973c0a0e8990/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "53e61c0389f64fc7abcf8db90735fd23",
          "image": "https://production.listennotes.com/podcasts/sol-affirmations-black-love-podcast-network-BkctPgoV_af-CBHp0QMSuYD.1400x1400.jpg",
          "title": "SOL Affirmations with Karega & Felicia",
          "publisher": "Black Love Podcast Network",
          "thumbnail": "https://production.listennotes.com/podcasts/sol-affirmations-black-love-podcast-network-Zfpxd5aBkNM-CBHp0QMSuYD.300x300.jpg",
          "listen_score": 39,
          "listennotes_url": "https://www.listennotes.com/c/53e61c0389f64fc7abcf8db90735fd23/",
          "listen_score_global_rank": "2%"
        },
        {
          "id": "90527b9a3b7c496db81ba6aa4abadf5b",
          "image": "https://production.listennotes.com/podcasts/the-mamas-den-WDcj_04qZmY-ZY8ln1TgemM.1400x1400.jpg",
          "title": "The Mama's Den",
          "publisher": "Black Love Podcast Network",
          "thumbnail": "https://production.listennotes.com/podcasts/the-mamas-den-EKVwsWDiyN9-ZY8ln1TgemM.300x300.jpg",
          "listen_score": 46,
          "listennotes_url": "https://www.listennotes.com/c/90527b9a3b7c496db81ba6aa4abadf5b/",
          "listen_score_global_rank": "1%"
        }
      ],
      "source_url": "https://www.essence.com/gallery/14-black-podcasts-to-listen-to-this-spring-2023/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"There are plenty of other podcasts from creatives of color to listen to daily; it might even become difficult trying to choose which one is best. So, assist in your search, here are some of the best Black podcasts to listen to this spring.\"",
      "pub_date_ms": 1679787984536,
      "source_domain": "www.essence.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/14-black-podcasts-to-listen-to-this-KYDhmAOnPNB/"
    },
    {
      "id": "OgBoeNHSh4d",
      "title": "French podcasts to help improve your language skills",
      "total": 5,
      "podcasts": [
        {
          "id": "37bd6f5c49f149bca00b17f11bc12324",
          "image": "https://production.listennotes.com/podcasts/coffee-break-french-coffee-break-languages-6BLnrFGejTM-FP7RN9eTYIQ.1400x1400.jpg",
          "title": "Coffee Break French",
          "publisher": "Coffee Break Languages",
          "thumbnail": "https://production.listennotes.com/podcasts/coffee-break-french-coffee-break-languages-t6NydoRZs2F-FP7RN9eTYIQ.300x300.jpg",
          "listen_score": 67,
          "listennotes_url": "https://www.listennotes.com/c/37bd6f5c49f149bca00b17f11bc12324/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "d22ab4350b9e49dd9369514508b45f6a",
          "image": "https://production.listennotes.com/podcasts/grand-reportage-rfi-98NwA6vsc4b-6RnTHl0-NIP.1400x1400.jpg",
          "title": "Grand reportage",
          "publisher": "RFI",
          "thumbnail": "https://production.listennotes.com/podcasts/grand-reportage-rfi-qs6YMQ09gCf-6RnTHl0-NIP.300x300.jpg",
          "listen_score": 44,
          "listennotes_url": "https://www.listennotes.com/c/d22ab4350b9e49dd9369514508b45f6a/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "39e505db4e6f44c493614595a1507cac",
          "image": "https://production.listennotes.com/podcasts/news-in-slow-french-linguistica-360-DT1XtWoeny--rhitEn9USFY.1400x1400.jpg",
          "title": "News in Slow French",
          "publisher": "Linguistica 360",
          "thumbnail": "https://production.listennotes.com/podcasts/news-in-slow-french-linguistica-360-kGYQT96iEDU-rhitEn9USFY.300x300.jpg",
          "listen_score": 51,
          "listennotes_url": "https://www.listennotes.com/c/39e505db4e6f44c493614595a1507cac/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "91687847c5084c809097771c91e6dc2d",
          "image": "https://production.listennotes.com/podcasts/french-voices-podcast-learn-french-2dwqWGUxsbM-ItsWGmP8dbZ.1400x1400.jpg",
          "title": "French Voices Podcast | Learn French | Interviews with Native French Speakers | French Culture",
          "publisher": "Jessica: Native French teacher, founder of French Your Way",
          "thumbnail": "https://production.listennotes.com/podcasts/french-voices-podcast-learn-french-Fyim78Vuo_R-ItsWGmP8dbZ.300x300.jpg",
          "listen_score": 46,
          "listennotes_url": "https://www.listennotes.com/c/91687847c5084c809097771c91e6dc2d/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "8c62b6c76ed341e39b0f0a81a4958904",
          "image": "https://production.listennotes.com/podcasts/promenades-imaginaires-au-mus\u00e9e-dorsay-bt6YThw5FMa-SdpZ0InW3PX.1400x1400.jpg",
          "title": "Promenades imaginaires au mus\u00e9e d'Orsay",
          "publisher": "Musee Orsay",
          "thumbnail": "https://production.listennotes.com/podcasts/promenades-imaginaires-au-mus\u00e9e-dorsay-ZUCuWYKcTOs-SdpZ0InW3PX.300x300.jpg",
          "listen_score": 42,
          "listennotes_url": "https://www.listennotes.com/c/8c62b6c76ed341e39b0f0a81a4958904/",
          "listen_score_global_rank": "1.5%"
        }
      ],
      "source_url": "https://www.connexionfrance.com/article/Practical/Everyday-Life/French-podcasts-to-help-improve-your-language-skills?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"Podcasts are a great way to make progress in learning French. Do you know someone who might find this article helpful?\"",
      "pub_date_ms": 1679787713457,
      "source_domain": "www.connexionfrance.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/french-podcasts-to-help-improve-your-OgBoeNHSh4d/"
    },
    {
      "id": "0VjXWH4D8Cp",
      "title": "5 Leadership and Diversity Podcasts That Are Worth A Listen According To These Leading Corporate Execs",
      "total": 5,
      "podcasts": [
        {
          "id": "ef49ff5355134216917a8804ab2362b7",
          "image": "https://production.listennotes.com/podcasts/higher-learning-with-van-lathan-and-rachel-Qj4E-2hHvYu-E9YWsoQB3tH.1400x1400.jpg",
          "title": "Higher Learning with Van Lathan and Rachel Lindsay",
          "publisher": "The Ringer ",
          "thumbnail": "https://production.listennotes.com/podcasts/higher-learning-with-van-lathan-and-rachel-3_8RK5JyFgf-E9YWsoQB3tH.300x300.jpg",
          "listen_score": 70,
          "listennotes_url": "https://www.listennotes.com/c/ef49ff5355134216917a8804ab2362b7/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "f263c4cdd51b4b6db56bf1d90ec49b11",
          "image": "https://production.listennotes.com/podcasts/color-code-o6qUkb8_l5S-ugKI7EU1sHh.1400x1400.jpg",
          "title": "Color Code",
          "publisher": "STAT",
          "thumbnail": "https://production.listennotes.com/podcasts/color-code-gEqYkCl-JS4-ugKI7EU1sHh.300x300.jpg",
          "listen_score": 33,
          "listennotes_url": "https://www.listennotes.com/c/f263c4cdd51b4b6db56bf1d90ec49b11/",
          "listen_score_global_rank": "5%"
        },
        {
          "id": "b31ec935d0d748368daa0be2f498ccab",
          "image": "https://production.listennotes.com/podcasts/dei-after-5-with-sacha-sacha-thompson-zwLZeg1GiCv-2Vd6Ro5vCBh.1400x1400.jpg",
          "title": "DEI After 5 with Sacha",
          "publisher": "Sacha Thompson",
          "thumbnail": "https://production.listennotes.com/podcasts/dei-after-5-with-sacha-sacha-thompson-trHSRBf_1Ay-2Vd6Ro5vCBh.300x300.jpg",
          "listen_score": 24,
          "listennotes_url": "https://www.listennotes.com/c/b31ec935d0d748368daa0be2f498ccab/",
          "listen_score_global_rank": "10%"
        },
        {
          "id": "2856814619cd4a35b5b0307c38481575",
          "image": "https://production.listennotes.com/podcasts/gen-x-amplified-with-adrion-porter-adrion-wM-kp2HGF5d-8yEFMsKIL4Y.1400x1400.jpg",
          "title": "Gen X Amplified with Adrion Porter",
          "publisher": "Adrion Porter | Speaker. Mid-Career Mentor. Podcaster. Brand Strategist.",
          "thumbnail": "https://production.listennotes.com/podcasts/gen-x-amplified-with-adrion-porter-adrion-aXDN0x4V-zw-8yEFMsKIL4Y.300x300.jpg",
          "listen_score": 35,
          "listennotes_url": "https://www.listennotes.com/c/2856814619cd4a35b5b0307c38481575/",
          "listen_score_global_rank": "3%"
        },
        {
          "id": "976890b98fd14aef85d8be8735179d72",
          "image": "https://production.listennotes.com/podcasts/code-switch-npr-ukEBCRJM_P7-yORrA0KnwqZ.1400x1400.jpg",
          "title": "Code Switch",
          "publisher": "NPR",
          "thumbnail": "https://production.listennotes.com/podcasts/code-switch-npr-He1goOF9-Zu-yORrA0KnwqZ.300x300.jpg",
          "listen_score": 76,
          "listennotes_url": "https://www.listennotes.com/c/976890b98fd14aef85d8be8735179d72/",
          "listen_score_global_rank": "0.01%"
        }
      ],
      "source_url": "https://www.essence.com/news/money-career/leadership-diversity-podcasts-corporate-execs/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"For entrepreneurs, business people, and leaders who seek credible expertise, informed conversation, and nuanced takes from diverse perspectives, ESSENCE surveyed five executives to find out their podcast faves. Here\u2019s what they recommended.\"",
      "pub_date_ms": 1679787577970,
      "source_domain": "www.essence.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/5-leadership-and-diversity-podcasts-0VjXWH4D8Cp/"
    },
    {
      "id": "Ud7jFwSTofR",
      "title": "The 7 best wellness podcasts to inspire pure joy this spring",
      "total": 7,
      "podcasts": [
        {
          "id": "1ab5768ac559452cac624e9716c731aa",
          "image": "https://production.listennotes.com/podcasts/beauty-full-lives-madeleine-spencer-HtqWn_xZEAT-Idet9Ni3xLy.1400x1400.jpg",
          "title": "Beauty Full Lives",
          "publisher": "Madeleine Spencer",
          "thumbnail": "https://production.listennotes.com/podcasts/beauty-full-lives-madeleine-spencer-_lQ45zeTXsc-Idet9Ni3xLy.300x300.jpg",
          "listen_score": 45,
          "listennotes_url": "https://www.listennotes.com/c/1ab5768ac559452cac624e9716c731aa/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "943c2da80d3b42f99c266ad3f9c06b5d",
          "image": "https://production.listennotes.com/podcasts/ted-health-ted-Qu0GENswY3A-E-oUK8AZGa2.1400x1400.jpg",
          "title": "TED Health",
          "publisher": "TED",
          "thumbnail": "https://production.listennotes.com/podcasts/ted-health-ted-Huegz2ZU5_Q-E-oUK8AZGa2.300x300.jpg",
          "listen_score": 62,
          "listennotes_url": "https://www.listennotes.com/c/943c2da80d3b42f99c266ad3f9c06b5d/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "e1c66a542b8d4acfbc95b898c7ac710f",
          "image": "https://production.listennotes.com/podcasts/feel-better-live-more-with-dr-rangan-HCVm172lNcX-JKmSp6BXHVk.1400x1400.jpg",
          "title": "Feel Better, Live More with Dr Rangan Chatterjee",
          "publisher": "Dr Rangan Chatterjee: GP & Author",
          "thumbnail": "https://production.listennotes.com/podcasts/feel-better-live-more-with-dr-rangan-H1l2zKIPydb-JKmSp6BXHVk.300x300.jpg",
          "listen_score": 72,
          "listennotes_url": "https://www.listennotes.com/c/e1c66a542b8d4acfbc95b898c7ac710f/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "03d4da5853ef4f72b3ba215f573bc7aa",
          "image": "https://production.listennotes.com/podcasts/saturn-returns-with-caggie-feast-collective-iNOEGVeYpUb-3GjI4_TZREl.1400x1400.jpg",
          "title": "Saturn Returns with Caggie",
          "publisher": "Astrid Productions",
          "thumbnail": "https://production.listennotes.com/podcasts/saturn-returns-with-caggie-feast-collective-PBuElwy1D8g-3GjI4_TZREl.300x300.jpg",
          "listen_score": 52,
          "listennotes_url": "https://www.listennotes.com/c/03d4da5853ef4f72b3ba215f573bc7aa/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "e636a8dbde3f488a9ba76607f0491376",
          "image": "https://production.listennotes.com/podcasts/modern-love-the-new-york-times-8nDlEQ6Txy4-OBwDWs-Uv25.1400x1400.jpg",
          "title": "Modern Love",
          "publisher": "The New York Times",
          "thumbnail": "https://production.listennotes.com/podcasts/modern-love-the-new-york-times-cnhSIGxE_V3-OBwDWs-Uv25.300x300.jpg",
          "listen_score": 73,
          "listennotes_url": "https://www.listennotes.com/c/e636a8dbde3f488a9ba76607f0491376/",
          "listen_score_global_rank": "0.01%"
        }
      ],
      "source_url": "https://www.hellomagazine.com/hfm/20230320167226/best-wellness-podcasts/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"In honor of International Day of Happiness, check out these mood-boosting podcasts\u2026\"",
      "pub_date_ms": 1679442306683,
      "source_domain": "www.hellomagazine.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/the-7-best-wellness-podcasts-to-Ud7jFwSTofR/"
    },
    {
      "id": "WrXxzZPwmT-",
      "title": "True crime, \u2018Buffy,\u2019 and horror: 5 podcasts by \u2018Morbid\u2019 hosts Ash & Alaina",
      "total": 5,
      "podcasts": [
        {
          "id": "ddd0bba87bbe45be818a7dfc2113fba6",
          "image": "https://production.listennotes.com/podcasts/frozen-head-l3isXSpwykR-gXhufOAUm1P.1400x1400.jpg",
          "title": "Frozen Head",
          "publisher": "Wondery",
          "thumbnail": "https://production.listennotes.com/podcasts/frozen-head-cYR8giXNU1k-gXhufOAUm1P.300x300.jpg",
          "listen_score": 51,
          "listennotes_url": "https://www.listennotes.com/c/ddd0bba87bbe45be818a7dfc2113fba6/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "bf83fac23a294d339c3815994bf8b0a6",
          "image": "https://production.listennotes.com/podcasts/the-rewatcher-buffy-the-vampire-slayer-skKdof7qGH8-JHfxNXwoMRL.1400x1400.jpg",
          "title": "The Rewatcher: Buffy the Vampire Slayer",
          "publisher": "Wondery | Morbid Network",
          "thumbnail": "https://production.listennotes.com/podcasts/the-rewatcher-buffy-the-vampire-slayer-HIK2UNnmxMk-JHfxNXwoMRL.300x300.jpg",
          "listen_score": 55,
          "listennotes_url": "https://www.listennotes.com/c/bf83fac23a294d339c3815994bf8b0a6/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "abf3490be313490a8e21ded2f5f19742",
          "image": "https://production.listennotes.com/podcasts/scream-ash-alaina-caleb-morbid-network-ZREc3FyU5Ku-Jqc0rSg3OhN.1400x1400.jpg",
          "title": "Scream!",
          "publisher": "Ash, Alaina, & Caleb | Morbid Network | Wondery",
          "thumbnail": "https://production.listennotes.com/podcasts/scream-ash-alaina-caleb-morbid-network-TiSrl9V2EIe-Jqc0rSg3OhN.300x300.jpg",
          "listen_score": 54,
          "listennotes_url": "https://www.listennotes.com/c/abf3490be313490a8e21ded2f5f19742/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "08e7e64e80ac456a8ce0027f07dc40d0",
          "image": "https://production.listennotes.com/podcasts/morbid-morbid-network-wondery-q_fSJAu-WOB-krRXUPe1dbC.1400x1400.jpg",
          "title": "Morbid",
          "publisher": "Morbid Network | Wondery",
          "thumbnail": "https://production.listennotes.com/podcasts/morbid-morbid-network-wondery-YRN7M3rTyLo-krRXUPe1dbC.300x300.jpg",
          "listen_score": 87,
          "listennotes_url": "https://www.listennotes.com/c/08e7e64e80ac456a8ce0027f07dc40d0/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "5e4ad2b8edb841da88bb09b051e44887",
          "image": "https://production.listennotes.com/podcasts/crime-countdown-parcast-network-eqlXINviYmy-AFG5a7mNJ4-.1400x1400.jpg",
          "title": "Crime Countdown",
          "publisher": "Parcast Network",
          "thumbnail": "https://production.listennotes.com/podcasts/crime-countdown-parcast-network-ODgBxwZdIcV-AFG5a7mNJ4-.300x300.jpg",
          "listen_score": 63,
          "listennotes_url": "https://www.listennotes.com/c/5e4ad2b8edb841da88bb09b051e44887/",
          "listen_score_global_rank": "0.1%"
        }
      ],
      "source_url": "https://podsauce.com/articles/podcasts-hosted-by-morbid-hosts-ash-and-alaina/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "'We\u2019ve gathered the best podcasts hosted by Alaina and Ash. For more true crime, check out \u201cFrozen Head\u201d and \u201cCrime Countdown.\u201d Head to Hellmouth with the cohosts on a Buffy the Vampire Slayer rewatch show, a fun listen since Ash is watching the show for the first time ever. Horror fans will love \u201cScream!\u201d that covers classic and new films.'",
      "pub_date_ms": 1679442224647,
      "source_domain": "podsauce.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/true-crime-buffy-and-horror-5-podcasts-WrXxzZPwmT-/"
    },
    {
      "id": "qVGZ5e9fArO",
      "title": "\u2018The Last of Us\u2019 fan? Check out these 6 action survival podcasts set in post-apocalyptic worlds",
      "total": 6,
      "podcasts": [
        {
          "id": "3f658bb26b7843c4863277b0cadc7cc5",
          "image": "https://production.listennotes.com/podcasts/impact-winter-audible-originals-zboDgQO4dTH-4XyZ6QHgEU5.1400x1400.jpg",
          "title": "Impact Winter",
          "publisher": "Audible Originals",
          "thumbnail": "https://production.listennotes.com/podcasts/impact-winter-audible-originals-BWt9AeD_G1c-4XyZ6QHgEU5.300x300.jpg",
          "listen_score": 56,
          "listennotes_url": "https://www.listennotes.com/c/3f658bb26b7843c4863277b0cadc7cc5/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "99a8698b73a04e719178c9a9badfb241",
          "image": "https://production.listennotes.com/podcasts/hbos-the-last-of-us-podcast-hbo-uHhM4VasLFg-uWwptYigAhP.1400x1400.jpg",
          "title": "HBO's The Last of Us Podcast",
          "publisher": "HBO",
          "thumbnail": "https://production.listennotes.com/podcasts/hbos-the-last-of-us-podcast-hbo-ZqhUEXMHzji-uWwptYigAhP.300x300.jpg",
          "listen_score": 63,
          "listennotes_url": "https://www.listennotes.com/c/99a8698b73a04e719178c9a9badfb241/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "6b1834218d79442f948a0f0dbf37808c",
          "image": "https://production.listennotes.com/podcasts/the-white-vault-fool-and-scholar-productions-RO4PwMgu6Cd-T4gs5OEo0cl.1400x1400.jpg",
          "title": "The White Vault",
          "publisher": "Fool and Scholar Productions",
          "thumbnail": "https://production.listennotes.com/podcasts/the-white-vault-fool-and-scholar-productions-gC9GHfn1-ds-T4gs5OEo0cl.300x300.jpg",
          "listen_score": 67,
          "listennotes_url": "https://www.listennotes.com/c/6b1834218d79442f948a0f0dbf37808c/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "48ae8c05bb804158bf3838604bbd7d56",
          "image": "https://production.listennotes.com/podcasts/were-alive-wayland-productions-inc-5uCloLFfU9I-nC-XLuBMGHf.1400x1400.jpg",
          "title": "We're Alive",
          "publisher": "Wayland Productions Inc",
          "thumbnail": "https://production.listennotes.com/podcasts/were-alive-wayland-productions-inc-Qj-GYw5efID-nC-XLuBMGHf.300x300.jpg",
          "listen_score": 73,
          "listennotes_url": "https://www.listennotes.com/c/48ae8c05bb804158bf3838604bbd7d56/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "33efb964781b4314b95677d7d1c70f37",
          "image": "https://production.listennotes.com/podcasts/the-cleansed-a-post-apocalyptic-saga-realm-6eJlr9QsWbR-vzpW6-qhHSi.1400x1400.jpg",
          "title": "The Cleansed: A Post-Apocalyptic Saga",
          "publisher": "Realm",
          "thumbnail": "https://production.listennotes.com/podcasts/the-cleansed-a-post-apocalyptic-saga-realm-3CldcOaXVrL-vzpW6-qhHSi.300x300.jpg",
          "listen_score": 50,
          "listennotes_url": "https://www.listennotes.com/c/33efb964781b4314b95677d7d1c70f37/",
          "listen_score_global_rank": "0.5%"
        }
      ],
      "source_url": "https://podsauce.com/articles/best-apocalyptic-podcasts/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "'Shows on our list run the gamut of disasters from outbreaks to infections and beastly creatures who roam freely. Check out a sci-fi show by The Walking Dead\u2019s executive producers, \u201cImpact Winter.\u201d We\u2019ve also included \u201cHBO\u2019s The Last of Us Podcast,\u201d the long-running series \u201cWe\u2019re Alive,\u201d and \u201cBirds of Empire.\u201d'",
      "pub_date_ms": 1679442173134,
      "source_domain": "podsauce.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/the-last-of-us-fan-check-out-these-6-qVGZ5e9fArO/"
    },
    {
      "id": "W8lD_AG9dHf",
      "title": "The 15 Best Australian Podcasts To Zhush Up Your Listening Routine",
      "total": 15,
      "podcasts": [
        {
          "id": "12433c9821c045e5b67f84aca1cd30d8",
          "image": "https://production.listennotes.com/podcasts/coming-out-blak-coming-out-blak-6cBi0bOXzp5-d2e-W5IAzOo.1400x1400.jpg",
          "title": "Coming out, Blak",
          "publisher": "Coming Out, Blak",
          "thumbnail": "https://production.listennotes.com/podcasts/coming-out-blak-coming-out-blak-TAEmMdIXSyn-d2e-W5IAzOo.300x300.jpg",
          "listen_score": null,
          "listennotes_url": "https://www.listennotes.com/c/12433c9821c045e5b67f84aca1cd30d8/",
          "listen_score_global_rank": null
        },
        {
          "id": "5eeb8130da324b71802d2f94814262f9",
          "image": "https://production.listennotes.com/podcasts/its-a-lot-with-abbie-chatfield-listnr--NfMEPpHxbJ-OIlswEpiB1R.1400x1400.jpg",
          "title": "It's A Lot with Abbie Chatfield",
          "publisher": "LiSTNR",
          "thumbnail": "https://production.listennotes.com/podcasts/its-a-lot-with-abbie-chatfield-listnr-nyWfkFHg_Qj-OIlswEpiB1R.300x300.jpg",
          "listen_score": 60,
          "listennotes_url": "https://www.listennotes.com/c/5eeb8130da324b71802d2f94814262f9/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "0799169505824196b203fe612aee50b1",
          "image": "https://production.listennotes.com/podcasts/stop-everything-abc-radio-yWKC6S0XGrR-0LGoNiEqaBg.1400x1400.jpg",
          "title": "Stop Everything!",
          "publisher": "ABC Radio",
          "thumbnail": "https://production.listennotes.com/podcasts/stop-everything-abc-radio-Jd0fXqKobUO-0LGoNiEqaBg.300x300.jpg",
          "listen_score": 45,
          "listennotes_url": "https://www.listennotes.com/c/0799169505824196b203fe612aee50b1/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "02e194651c6240e6b95c8e38729af63b",
          "image": "https://production.listennotes.com/podcasts/casefile-true-crime-casefile-presents-KVzo_uljf5h-DG5lH8yuLgi.1400x1400.jpg",
          "title": "Casefile True Crime",
          "publisher": "Casefile Presents",
          "thumbnail": "https://production.listennotes.com/podcasts/casefile-true-crime-casefile-presents-NF1Sr8fb_B9-DG5lH8yuLgi.300x300.jpg",
          "listen_score": 87,
          "listennotes_url": "https://www.listennotes.com/c/02e194651c6240e6b95c8e38729af63b/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "2e672df8e97a4a5583cb5e888f9b31cd",
          "image": "https://production.listennotes.com/podcasts/the-briefing-listnr--E2XamwqAeo-Ca2Hb04qx8h.1400x1400.jpg",
          "title": "The Briefing",
          "publisher": "LiSTNR",
          "thumbnail": "https://production.listennotes.com/podcasts/the-briefing-listnr-zcCNdnHmpBh-Ca2Hb04qx8h.300x300.jpg",
          "listen_score": 53,
          "listennotes_url": "https://www.listennotes.com/c/2e672df8e97a4a5583cb5e888f9b31cd/",
          "listen_score_global_rank": "0.5%"
        }
      ],
      "source_url": "https://www.refinery29.com/en-au/best-australian-podcasts?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\u201cWe're here to help. Ahead, we've rounded up some of the best Australian podcasts that explore everything from entertainment, relationships, sexuality, news and current affairs and more.\u201d",
      "pub_date_ms": 1679442077822,
      "source_domain": "www.refinery29.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/the-15-best-australian-podcasts-to-W8lD_AG9dHf/"
    },
    {
      "id": "gscUpP7b9Tu",
      "title": "BBC Podcasts Premium Has Launched On Apple Podcasts",
      "total": 14,
      "podcasts": [
        {
          "id": "586687cfb0e34b26b9e37f691e12fa6c",
          "image": "https://production.listennotes.com/podcasts/the-infinite-monkey-cage-bbc-radio-4-xg7r9tjOPwA-4jEfIrdVmKg.1400x1400.jpg",
          "title": "The Infinite Monkey Cage",
          "publisher": "BBC Radio 4",
          "thumbnail": "https://production.listennotes.com/podcasts/the-infinite-monkey-cage-bbc-radio-4-zaLHRuM01hW-4jEfIrdVmKg.300x300.jpg",
          "listen_score": 73,
          "listennotes_url": "https://www.listennotes.com/c/586687cfb0e34b26b9e37f691e12fa6c/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "4fff38a6c6bc41ba8a54ebce4be0aa8c",
          "image": "https://production.listennotes.com/podcasts/in-our-time-bbc-radio-4-kr62xXmWgQy-NGaVjqYxhLn.1400x1400.jpg",
          "title": "In Our Time",
          "publisher": "BBC Radio 4",
          "thumbnail": "https://production.listennotes.com/podcasts/in-our-time-bbc-radio-4-bVy7ZgIG1mc-NGaVjqYxhLn.300x300.jpg",
          "listen_score": 73,
          "listennotes_url": "https://www.listennotes.com/c/4fff38a6c6bc41ba8a54ebce4be0aa8c/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "275deca7255f4de48abd0209b65c47b5",
          "image": "https://production.listennotes.com/podcasts/killing-victoria-bbc-radio-67qZs9TnaeC-BdqZgvPQbGx.1400x1400.jpg",
          "title": "Killing Victoria",
          "publisher": "BBC Radio",
          "thumbnail": "https://production.listennotes.com/podcasts/killing-victoria-bbc-radio-znDHR145pfq-BdqZgvPQbGx.300x300.jpg",
          "listen_score": 38,
          "listennotes_url": "https://www.listennotes.com/c/275deca7255f4de48abd0209b65c47b5/",
          "listen_score_global_rank": "2%"
        },
        {
          "id": "5f5e5e6553d6476da37defbd0b6c57a8",
          "image": "https://production.listennotes.com/podcasts/lady-killers-with-lucy-worsley-kdmLtTAIv1H-uQOhoWc6di-.1400x1400.jpg",
          "title": "Lady Killers with Lucy Worsley",
          "publisher": "BBC Radio 4",
          "thumbnail": "https://production.listennotes.com/podcasts/lady-killers-with-lucy-worsley-IP0l8-evUqZ-uQOhoWc6di-.300x300.jpg",
          "listen_score": 51,
          "listennotes_url": "https://www.listennotes.com/c/5f5e5e6553d6476da37defbd0b6c57a8/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "fa53c30c960a4b2283c8bdce64497534",
          "image": "https://production.listennotes.com/podcasts/global-news-podcast-bbc-world-service-WIXCzYQDTBJ-D65IdPgn-Y_.1400x1400.jpg",
          "title": "Global News Podcast",
          "publisher": "BBC World Service",
          "thumbnail": "https://production.listennotes.com/podcasts/global-news-podcast-bbc-world-service-2k-FqMgyEZR-D65IdPgn-Y_.300x300.jpg",
          "listen_score": 73,
          "listennotes_url": "https://www.listennotes.com/c/fa53c30c960a4b2283c8bdce64497534/",
          "listen_score_global_rank": "0.05%"
        }
      ],
      "source_url": "https://womenlovetech.com/bbc-podcasts-premium-has-launched-on-apple-podcasts/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"BBC Podcasts Premium is available from the BBC Podcasts channel on Apple Podcasts for $4.49 per month or at an annual price of $49.99 a year. Those who are looking to try before they buy can get a 7 day free trial.\"",
      "pub_date_ms": 1679332748879,
      "source_domain": "womenlovetech.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/bbc-podcasts-premium-has-launched-on-gscUpP7b9Tu/"
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
            "description": "Curated list id, which can be used to further fetch detailed curated list metadata via `GET /curated_podcasts/{id}`."
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
                  "description": "Podcast id, which can be used to further fetch detailed podcast metadata via `GET /podcasts/{id}`."
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

Podcast hosting services can use this endpoint to help your users directly submit a new podcast to Listen Notes database. If the podcast doesn&#x27;t exist in the database, &quot;status&quot; in the response will be &quot;in review&quot;, and we&#x27;ll review it within 12 hours. If the podcast exists, &quot;status&quot; in the response will be &quot;found&quot;. If this submission is rejected, &quot;status&quot; in the response will be &quot;rejected&quot;. You can use `POST /podcasts` to check if multiple podcasts exist in the database. If you want to get a notification once the podcast is accepted, you can either specify the &quot;email&quot; parameter or configure a webhook url in the dashboard: listennotes.com/api/dashboard/#webhooks


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
  "status": "in review",
  "podcast": {}
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
        "in review",
        "rejected"
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
          "description": "Podcast id, which can be used to further fetch detailed podcast metadata via `GET /podcasts/{id}`."
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
  "image": "https://production.listennotes.com/podcast-playlists/podcasts-about-podcasting-4bU7MZIlEVO-m1pe7z60bsw.1600x1600.jpg",
  "items": [
    {
      "id": 846112,
      "data": {
        "id": "f4d0feb5bed64c8fac67306e7ed6c6e3",
        "link": "https://podcasters.spotify.com/pod/show/thisweekinstartups/episodes/Revolutionizing-podcasting--standards-vs--innovation-with-Anchor-Co-Founder-Mike-Mignano--E1520-e1lqm2g?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/f4d0feb5bed64c8fac67306e7ed6c6e3/",
        "image": "https://production.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-d9kz8SVeAwn-EKckR36zrnA.1400x1400.jpg",
        "title": "Revolutionizing podcasting + standards vs. innovation with Anchor Co-Founder Mike Mignano | E1520",
        "podcast": {
          "id": "9a62e2581908415185dee35d2d19f9b5",
          "image": "https://production.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-d9kz8SVeAwn-EKckR36zrnA.1400x1400.jpg",
          "title": "This Week in Startups",
          "publisher": "Jason Calacanis",
          "thumbnail": "https://production.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-LZCcPIajWVQ-EKckR36zrnA.300x300.jpg",
          "listen_score": 64,
          "listennotes_url": "https://www.listennotes.com/c/9a62e2581908415185dee35d2d19f9b5/",
          "listen_score_global_rank": "0.05%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-LZCcPIajWVQ-EKckR36zrnA.300x300.jpg",
        "description": "<p>Today's show is a CLASSIC TWiST founder interview. Anchor Co-Founder Mike Mignano joins to tell Anchor's founding story (1:40), break down what it's like getting acquired by Spotify (15:32), and talk about how RSS standards might be stunting innovation in the podcasting space. (33:17)</p>\n<p><br /></p>\n<p>0:00 Jason intros today's guest: Anchor Co-Founder Mike Mignano</p>\n<p>1:40 Mike explains why he started Anchor, the original inspiration and first versions, finding PMF, building the nuts and bolts of a great podcast publishing experience</p>\n<p>14:23 Helpware - Go to https://helpware.com/TWIST to get $1000 off your first invoice</p>\n<p>15:32 Why Anchor sold to Spotify, the Series B term sheet they were considering at the time of acquisition, getting courted by Spotify CEO Daniel Ek, Anchor's first check story</p>\n<p>24:44 LinkedIn Jobs - Post your first job for free at https://linkedin.com/twist</p>\n<p>25:58 Why Apple hasn't innovated in podcasting, paid podcasts vs. advertising</p>\n<p>31:59 Babbel - Save up to 60% off your language learning subscription at https://babbel.com/twist&nbsp;</p>\n<p>33:17 Why Mike wrote his recent article: \u201cThe Standards Innovation Paradox\u201d, evolving standards to increase innovation, the Substack example</p>\n<p><br /></p>\n<p>Read Mike's article:</p>\n<p>https://mignano.medium.com/the-standards-innovation-paradox-e14cab521391</p>",
        "pub_date_ms": 1659036538192,
        "guid_from_rss": "44bc2eb9-2f3a-415e-9f7e-e8e4e16b30c8",
        "listennotes_url": "https://www.listennotes.com/e/f4d0feb5bed64c8fac67306e7ed6c6e3/",
        "audio_length_sec": 3220,
        "explicit_content": false,
        "maybe_audio_invalid": false,
        "listennotes_edit_url": "https://www.listennotes.com/e/f4d0feb5bed64c8fac67306e7ed6c6e3/#edit"
      },
      "type": "episode",
      "notes": "",
      "added_at_ms": 1659049802678
    },
    {
      "id": 830890,
      "data": {
        "id": "b6965b7bcdab4df1b108a93309cedfc6",
        "link": "https://podcasters.spotify.com/pod/show/anthony-pompliano3/episodes/1014-Oscar-Merry-On-Pioneering-Listen-To-Earn-With-Bitcoin-e1nag1l?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/b6965b7bcdab4df1b108a93309cedfc6/",
        "image": "https://production.listennotes.com/podcasts/the-pomp-podcast/1014-oscar-merry-on-0_Nv4FrTdO5-s5SUXWPM2IZ.1400x1400.jpg",
        "title": "#1014 Oscar Merry On Pioneering Listen To Earn With Bitcoin",
        "podcast": {
          "id": "537c372ad9c7470cb2be897a14a7c7f9",
          "image": "https://production.listennotes.com/podcasts/the-pomp-podcast-anthony-pompliano-HcF7NfuJCGE-f1na5MVD_Qz.1400x1400.jpg",
          "title": "The Pomp Podcast",
          "publisher": "Anthony Pompliano",
          "thumbnail": "https://production.listennotes.com/podcasts/the-pomp-podcast-anthony-pompliano-Fe1dRA7_gUW-f1na5MVD_Qz.300x300.jpg",
          "listen_score": 64,
          "listennotes_url": "https://www.listennotes.com/c/537c372ad9c7470cb2be897a14a7c7f9/",
          "listen_score_global_rank": "0.05%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/the-pomp-podcast/1014-oscar-merry-on-W-qrn7XULpm-s5SUXWPM2IZ.300x300.jpg",
        "description": "Oscar Merry is the Co-Founder of Fountain, a new podcast platform where viewers can get paid to listen to their favorite podcasts and is powered by the Bitcoin Lightning Network.\n\nIn this conversation, we talk about podcasting 2.0, how the Fountain product works, why podcasters should be interested in paying their listeners, and on-boarding people to the Bitcoin network through Fountain.\n=======================\nLMAX Digital - the market-leading solution for institutional crypto trading & custodial services - offers clients a regulated, transparent and secure trading environment, together with the deepest pool of crypto liquidity. LMAX Digital is also a primary price discovery venue, streaming real-time market data to the industry\u2019s leading analytics platforms. LMAX Digital - secure, liquid, trusted. Learn more at LMAXdigital.com/pomp\n=======================\nThe Pod Pro Cover by Eight Sleep is the most advanced solution on the market for thermoregulation. It pairs dynamic cooling and heating with biometric tracking. Go to https://www.eightsleep.com/Pomp to check out the Pod Pro Cover and save $150 at checkout. Eight Sleep currently ships within the USA, Canada, and the UK.\n=======================\nDeFi Technologies represents what\u2019s next in the digital economy -- providing simplified, trusted access to crypto, decentralized finance and Web 3.0 investment opportunities. Institutions and investors can gain diversified, secure, compliant, and easily tradable access to a diversified set of industry-leading equity products and protocols, through a single stock purchase on a regulated exchange. Currently listed on U.S. (OTC: DEFTF) and Canadian (NEO:DEFI) exchanges.\n\u00a0\nFor more information or to subscribe to receive company updates and financial information, visit our website at http://defi.tech\u00a0\n=======================",
        "pub_date_ms": 1655835471162,
        "guid_from_rss": "210c3350-f192-11ec-9037-036c07c848a8",
        "listennotes_url": "https://www.listennotes.com/e/b6965b7bcdab4df1b108a93309cedfc6/",
        "audio_length_sec": 1788,
        "explicit_content": false,
        "maybe_audio_invalid": false,
        "listennotes_edit_url": "https://www.listennotes.com/e/b6965b7bcdab4df1b108a93309cedfc6/#edit"
      },
      "type": "episode",
      "notes": "Listen Notes API powers this app :) Awesome to see another success story of our podcast api!",
      "added_at_ms": 1655882791242
    },
    {
      "id": 827612,
      "data": {
        "id": "202d91e59bd8460492a220886d177eea",
        "link": "https://www.vox.com/recode-media-podcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/202d91e59bd8460492a220886d177eea/",
        "image": "https://production.listennotes.com/podcasts/recode-media-recode-SNw3MlTLqjC-1iPwTajLXlS.1400x1400.jpg",
        "title": "Bill Simmons on podcasts, celebrity interviews and life at Spotify",
        "podcast": {
          "id": "2aba49dc3fc04e3e96fe89f79a261798",
          "image": "https://production.listennotes.com/podcasts/recode-media-recode-SNw3MlTLqjC-1iPwTajLXlS.1400x1400.jpg",
          "title": "Recode Media",
          "publisher": "Recode",
          "thumbnail": "https://production.listennotes.com/podcasts/recode-media-recode-ReV9rxkUvST-1iPwTajLXlS.300x300.jpg",
          "listen_score": 54,
          "listennotes_url": "https://www.listennotes.com/c/2aba49dc3fc04e3e96fe89f79a261798/",
          "listen_score_global_rank": "0.5%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/recode-media-recode-ReV9rxkUvST-1iPwTajLXlS.300x300.jpg",
        "description": "<p>The Bill Simmons Podcast is, by its own description, \"the most downloaded sports podcast of all time.\" This week, it hits its 1,000th episode.</p><p>Bill Simmons began his career as a Boston sportswriter and went on to found ESPN's sports and pop culture blog Grantland. After ESPN shut down the site, Simmons started the Ringer \u2014 which he sold to Spotify in 2020.</p><p>In this wide-ranging conversation, Recode\u2019s Peter Kafka talks to Simmons about how he became a podcasting pioneer, and when he realized nerditry about the NBA and Game of Thrones could both live under the same roof. Simmons also reflects on what he learned from his time as an employee of The Walt Disney Corporation and how things are different at Spotify. Plus, he reveals the number one dream guest he\u2019d love to have on his show.</p><p><br /></p><p><strong>Featuring</strong>: Bill Simmons (<a href=\"https://twitter.com/BillSimmons\">@BillSimmons</a>), Founder of The Ringer</p><p><strong>Host</strong>: Peter Kafka\u00a0(<a href=\"https://twitter.com/pkafka\">@pkafka</a>), Senior Editor at Recode</p><p><strong>More to explore</strong>: <a href=\"https://pod.link/1080467174\">Subscribe for free to Recode Media</a>, Peter Kafka, one of the media industry's most acclaimed reporters, talks to business titans, journalists, comedians, and more to get their take on today's media landscape.</p><p><strong>About Recode by Vox</strong>: Recode by Vox helps you understand how tech is changing the world \u2014 and changing us.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
        "pub_date_ms": 1655266568017,
        "guid_from_rss": "72fffa04-5221-11ec-ae31-23e900b8cde4",
        "listennotes_url": "https://www.listennotes.com/e/202d91e59bd8460492a220886d177eea/",
        "audio_length_sec": 3626,
        "explicit_content": false,
        "maybe_audio_invalid": false,
        "listennotes_edit_url": "https://www.listennotes.com/e/202d91e59bd8460492a220886d177eea/#edit"
      },
      "type": "episode",
      "notes": "",
      "added_at_ms": 1655274047437
    },
    {
      "id": 764336,
      "data": {
        "id": "aba7f2dd81a5408f96da8d70dfbefe36",
        "error": "This episode has been deleted from the podcast database. Possible reasons: 1) Podcast producers sometimes delete their old episodes. 2) Copyright issues.",
        "title": "Spotify\u2019s ad-tech acquisitions to take on YouTube with The Verge\u2019s Ashley Carman + Founder University Pitches | E1389",
        "status": "deleted"
      },
      "type": "episode",
      "notes": "",
      "added_at_ms": 1645211291773
    },
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
        "description": "<p><strong>How I Built The Tim Ferriss Show to 700+ Million Downloads \u2014 An Immersive Explanation of All Aspects and Key Decisions (Featuring Chris Hutchins) | Brought to you by </strong><a href=\"http://linkedin.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>LinkedIn Jobs</strong></a><strong>&nbsp;recruitment platform with 770M+ users</strong>, <a href=\"http://athleticgreens.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>Athletic Greens</strong></a><strong>&nbsp;all-in-one nutritional supplement,&nbsp;and </strong><a href=\"http://helixsleep.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>Helix Sleep</strong></a><strong>&nbsp;premium mattresses. More on all three below.</strong></p><p><strong>Chris Hutchins</strong>&nbsp;(<a href=\"https://twitter.com/hutchins\" rel=\"noopener noreferrer\" target=\"_blank\">@hutchins</a>) is an avid life hacker and financial optimizer. He\u2019s the host of&nbsp;<a href=\"https://www.allthehacks.com/\" rel=\"noopener noreferrer\" target=\"_blank\"><strong><em>All the Hacks</em></strong></a>&nbsp;podcast and the Head of New Product Strategy at&nbsp;<a href=\"https://www.wealthfront.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\">Wealthfront</a>.</p><p>Previously, Chris was co-founder and CEO of Grove (acquired by&nbsp;<a href=\"https://www.wealthfront.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\">Wealthfront</a>), co-founder of Milk (acquired by Google), and a partner at&nbsp;<a href=\"https://www.gv.com/\" rel=\"noopener noreferrer\" target=\"_blank\">Google Ventures</a>, where he focused on seed and early stage investments.</p><p>Chris reached out with many questions about podcasting. He had already read much of&nbsp;<a href=\"https://tim.blog/2016/04/11/tim-ferriss-podcast-business/\" rel=\"noopener noreferrer\" target=\"_blank\">what I had written</a> and&nbsp;<a href=\"https://rolfpotts.com/podcast/tim-ferriss/\" rel=\"noopener noreferrer\" target=\"_blank\">listened to several interviews</a>, and this is intended to be an updated guide to all things podcasting.</p><p>Please enjoy!</p><p><strong>This episode is brought to you by&nbsp;</strong><a href=\"https://www.athleticgreens.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>Athletic Greens</strong></a><strong>.</strong>&nbsp;I get asked all the time, \u201cIf you could only use one supplement, what would it be?\u201d My answer is usually&nbsp;<a href=\"https://www.athleticgreens.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\">Athletic&nbsp;Greens</a>, my all-in-one nutritional insurance. I recommended it in&nbsp;<em>The 4-Hour Body</em>&nbsp;in 2010 and did not get paid to do so. I do my best with nutrient-dense meals, of course, but&nbsp;<a href=\"https://www.athleticgreens.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\">AG</a>&nbsp;further covers my bases with vitamins, minerals, and whole-food-sourced micronutrients that support gut health and the immune system.&nbsp;</p><p><strong>Right now,&nbsp;</strong><a href=\"https://www.athleticgreens.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>Athletic Greens</strong></a><strong>&nbsp;is offering you their Vitamin D Liquid Formula free with your first subscription purchase</strong>\u2014a vital nutrient for a strong immune system and strong bones.&nbsp;<strong>Visit&nbsp;</strong><a href=\"https://www.athleticgreens.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>AthleticGreens.com/Tim</strong></a><strong>&nbsp;to claim this special offer today and receive the free Vitamin D Liquid Formula (and five free travel packs) with your first subscription purchase!&nbsp;</strong>That\u2019s up to a one-year supply of Vitamin D as added value when you try their delicious and comprehensive all-in-one daily greens product.</p><p>*</p><p><strong>This episode is also brought to you by&nbsp;</strong><a href=\"http://helixsleep.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>Helix Sleep</strong></a><strong>!&nbsp;</strong>Helix was selected as the #1 overall mattress of 2020 by&nbsp;<em>GQ&nbsp;</em>magazine<em>, Wired,&nbsp;</em>Apartment Therapy, and many others. With&nbsp;<a href=\"http://helixsleep.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\">Helix</a>, there\u2019s a specific mattress to meet each and every body\u2019s unique comfort needs. Just take their quiz\u2014<a href=\"http://helixsleep.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\">only two minutes to complete</a>\u2014that matches your body type and sleep preferences to the perfect mattress for you. They have a 10-year warranty, and you get to try it out for a hundred nights, risk free. They\u2019ll even pick it up from you if you don\u2019t love it.&nbsp;</p><p><strong>And now, to my dear listeners, Helix is offering up to 200 dollars off all mattress orders plus two free pillows at&nbsp;</strong><a href=\"http://helixsleep.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>HelixSleep.com/Tim</strong></a><strong>.</strong></p><p><strong>*</strong></p><p><strong>This episode is also brought to you by&nbsp;</strong><a href=\"https://linkedin.com/Tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>LinkedIn Jobs</strong></a><strong>.</strong>&nbsp;Whether you are looking to hire now for a critical role or thinking about needs that you may have in the future,&nbsp;<a href=\"https://linkedin.com/Tim\" rel=\"noopener noreferrer\" target=\"_blank\">LinkedIn Jobs</a>&nbsp;can help. LinkedIn screens candidates for the hard and soft skills you\u2019re looking for and puts your job in front of candidates looking for job opportunities that match what you have to offer.</p><p>Using LinkedIn\u2019s active community of more than 770 million professionals worldwide,&nbsp;<a href=\"https://linkedin.com/Tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>LinkedIn Jobs</strong></a>&nbsp;can help you find and hire the right person faster.&nbsp;<strong>When your business is ready to make that next hire, find the right person with LinkedIn Jobs. And now, you can post a job for free.</strong>&nbsp;<a href=\"https://linkedin.com/Tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>Just visit LinkedIn.com/Tim</strong></a><strong>.</strong></p><p><strong>*</strong></p><p><strong>If you enjoy the podcast, would you please consider&nbsp;</strong><a href=\"https://podcasts.apple.com/us/podcast/the-tim-ferriss-show/id863897795?mt=2\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>leaving a short&nbsp;review&nbsp;on Apple Podcasts</strong></a><strong>?</strong>&nbsp;It takes less than 60 seconds, and it really makes a difference in helping to convince hard-to-get guests. I also love reading the&nbsp;reviews!</p><p><strong>For show notes and past guests, please visit</strong>&nbsp;<a href=\"https://tim.blog/podcast/?utm_source=podcast&amp;utm_medium=podcast&amp;utm_campaign=podcast-description\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>tim.blog/podcast</strong></a><strong>.</strong></p><p><strong>Sign up for Tim\u2019s email newsletter (\u201c5-Bullet Friday\u201d) at&nbsp;</strong><a href=\"https://go.tim.blog/5-bullet-friday-1/\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>tim.blog/friday</strong></a><strong>.</strong></p><p><strong>For transcripts of episodes, go to&nbsp;</strong><a href=\"http://tim.blog/transcripts\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>tim.blog/transcripts</strong></a><strong>.</strong></p><p><strong>Discover Tim\u2019s books:&nbsp;</strong><a href=\"http://tim.blog/books\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>tim.blog/books</strong></a><strong>.</strong></p><p><strong>Follow Tim:</strong></p><p><strong>Twitter</strong>:&nbsp;<a href=\"https://twitter.com/tferriss\" rel=\"noopener noreferrer\" target=\"_blank\">twitter.com/tferriss</a>&nbsp;</p><p><strong>Instagram</strong>:&nbsp;<a href=\"https://instagram.com/timferriss/\" rel=\"noopener noreferrer\" target=\"_blank\">instagram.com/timferriss</a></p><p><strong>Facebook</strong>:&nbsp;<a href=\"https://www.facebook.com/TimFerriss/\" rel=\"noopener noreferrer\" target=\"_blank\">facebook.com/timferriss</a>&nbsp;</p><p><strong>YouTube</strong>:&nbsp;<a href=\"https://www.youtube.com/timferriss\" rel=\"noopener noreferrer\" target=\"_blank\">youtube.com/timferriss</a></p><p>Past guests on&nbsp;<a href=\"http://tim.blog/podcast\" rel=\"noopener noreferrer\" target=\"_blank\"><strong><em>The Tim Ferriss Show</em></strong></a>&nbsp;include&nbsp;<a href=\"https://tim.blog/2020/12/08/jerry-seinfeld/\" rel=\"noopener noreferrer\" target=\"_blank\">Jerry Seinfeld</a>,&nbsp;<a href=\"https://tim.blog/2020/06/26/hugh-jackman/\" rel=\"noopener noreferrer\" target=\"_blank\">Hugh Jackman</a>,&nbsp;<a href=\"https://tim.blog/2020/04/16/jane-goodall/\" rel=\"noopener noreferrer\" target=\"_blank\">Dr. Jane Goodall</a>,&nbsp;<a href=\"https://tim.blog/2018/11/27/lebron-james-mike-mancias/\" rel=\"noopener noreferrer\" target=\"_blank\">LeBron James</a>,&nbsp;<a href=\"https://tim.blog/2020/05/20/kevin-hart/\" rel=\"noopener noreferrer\" target=\"_blank\">Kevin Hart</a>,&nbsp;<a href=\"https://tim.blog/2018/09/07/doris-kearns-goodwin-leadership/\" rel=\"noopener noreferrer\" target=\"_blank\">Doris Kearns Goodwin</a>,&nbsp;<a href=\"https://tim.blog/2015/12/06/jamie-foxx/\" rel=\"noopener noreferrer\" target=\"_blank\">Jamie Foxx</a>,&nbsp;<a href=\"https://tim.blog/2020/10/19/matthew-mcconaughey/\" rel=\"noopener noreferrer\" target=\"_blank\">Matthew McConaughey</a>,&nbsp;<a href=\"https://tim.blog/2017/05/21/esther-perel/\" rel=\"noopener noreferrer\" target=\"_blank\">Esther Perel</a>,&nbsp;<a href=\"https://tim.blog/2020/05/08/elizabeth-gilbert/\" rel=\"noopener noreferrer\" target=\"_blank\">Elizabeth Gilbert</a>,&nbsp;<a href=\"https://tim.blog/2017/12/20/terry-crews-how-to-have-do-and-be-all-you-want/\" rel=\"noopener noreferrer\" target=\"_blank\">Terry Crews</a>,&nbsp;<a href=\"https://tim.blog/2020/08/12/sia/\" rel=\"noopener noreferrer\" target=\"_blank\">Sia</a>,&nbsp;<a href=\"https://tim.blog/2020/10/27/yuval-noah-harari/\" rel=\"noopener noreferrer\" target=\"_blank\">Yuval Noah Harari</a>,&nbsp;<a href=\"https://tim.blog/2016/06/21/malcolm-gladwell/\" rel=\"noopener noreferrer\" target=\"_blank\">Malcolm Gladwell</a>,&nbsp;<a href=\"https://tim.blog/2020/05/27/secretary-madeleine-albright/\" rel=\"noopener noreferrer\" target=\"_blank\">Madeleine Albright</a>,&nbsp;<a href=\"https://tim.blog/2017/03/30/cheryl-strayed/\" rel=\"noopener noreferrer\" target=\"_blank\">Cheryl Strayed</a>,&nbsp;<a href=\"https://tim.blog/2019/02/18/jim-collins/\" rel=\"noopener noreferrer\" target=\"_blank\">Jim Collins</a>,&nbsp;<a href=\"https://tim.blog/2020/11/11/mary-karr/\" rel=\"noopener noreferrer\" target=\"_blank\">Mary Karr,</a>&nbsp;<a href=\"https://tim.blog/2014/10/21/brain-pickings/\" rel=\"noopener noreferrer\" target=\"_blank\">Maria Popova</a>,&nbsp;<a href=\"https://tim.blog/2020/05/15/sam-harris-2/\" rel=\"noopener noreferrer\" target=\"_blank\">Sam Harris</a>,&nbsp;<a href=\"https://tim.blog/2021/01/21/michael-phelps-grant-hackett/\" rel=\"noopener noreferrer\" target=\"_blank\">Michael Phelps</a>,&nbsp;<a href=\"https://tim.blog/2020/01/16/bob-iger/\" rel=\"noopener noreferrer\" target=\"_blank\">Bob Iger</a>,&nbsp;<a href=\"https://tim.blog/2019/10/31/edward-norton-motherless-brooklyn/\" rel=\"noopener noreferrer\" target=\"_blank\">Edward Norton</a>,&nbsp;<a href=\"https://tim.blog/2015/02/02/arnold-schwarzenegger/\" rel=\"noopener noreferrer\" target=\"_blank\">Arnold Schwarzenegger</a>,&nbsp;<a href=\"https://tim.blog/2014/06/24/neil-strauss/\" rel=\"noopener noreferrer\" target=\"_blank\">Neil Strauss</a>,&nbsp;<a href=\"https://tim.blog/2019/09/12/ken-burns/\" rel=\"noopener noreferrer\" target=\"_blank\">Ken Burns</a>,&nbsp;<a href=\"https://tim.blog/2017/08/26/maria-sharapova/\" rel=\"noopener noreferrer\" target=\"_blank\">Maria Sharapova</a>,&nbsp;<a href=\"https://tim.blog/2016/05/29/marc-andreessen/\" rel=\"noopener noreferrer\" target=\"_blank\">Marc Andreessen</a>,&nbsp;<a href=\"https://tim.blog/2019/03/28/neil-gaiman/\" rel=\"noopener noreferrer\" target=\"_blank\">Neil Gaiman</a>,&nbsp;<a href=\"https://tim.blog/2019/10/03/neil-degrasse-tyson/\" rel=\"noopener noreferrer\" target=\"_blank\">Neil de Grasse Tyson</a>,&nbsp;<a href=\"https://tim.blog/2016/09/21/jocko-willink-on-discipline-leadership-and-overcoming-doubt/\" rel=\"noopener noreferrer\" target=\"_blank\">Jocko Willink</a>,&nbsp;<a href=\"https://tim.blog/2020/12/03/daniel-ek/\" rel=\"noopener noreferrer\" target=\"_blank\">Daniel Ek</a>,&nbsp;<a href=\"https://tim.blog/2020/09/08/kelly-slater/\" rel=\"noopener noreferrer\" target=\"_blank\">Kelly Slater</a>,&nbsp;<a href=\"https://tim.blog/2019/11/27/peter-attia-fasting-metformin-longevity/\" rel=\"noopener noreferrer\" target=\"_blank\">Dr. Peter Attia</a>,&nbsp;<a href=\"https://tim.blog/2016/02/10/seth-godin/\" rel=\"noopener noreferrer\" target=\"_blank\">Seth Godin</a>,&nbsp;<a href=\"https://tim.blog/2018/09/25/howard-marks/\" rel=\"noopener noreferrer\" target=\"_blank\">Howard Marks</a>,&nbsp;<a href=\"https://tim.blog/2020/02/06/brene-brown-striving-self-acceptance-saving-marriages/\" rel=\"noopener noreferrer\" target=\"_blank\">Dr. Bren\u00e9 Brown</a>,&nbsp;<a href=\"https://tim.blog/2019/04/09/eric-schmidt/\" rel=\"noopener noreferrer\" target=\"_blank\">Eric Schmidt</a>,&nbsp;<a href=\"https://tim.blog/2020/05/01/michael-lewis/\" rel=\"noopener noreferrer\" target=\"_blank\">Michael Lewis</a>,&nbsp;<a href=\"https://tim.blog/2018/03/08/joe-gebbia-co-founder-of-airbnb/\" rel=\"noopener noreferrer\" target=\"_blank\">Joe Gebbia</a>,&nbsp;<a href=\"https://tim.blog/2018/05/06/michael-pollan-how-to-change-your-mind/\" rel=\"noopener noreferrer\" target=\"_blank\">Michael Pollan</a>,&nbsp;<a href=\"https://tim.blog/2021/03/01/jordan-peterson/\" rel=\"noopener noreferrer\" target=\"_blank\">Dr. Jordan Peterson</a>,&nbsp;<a href=\"https://tim.blog/2017/05/31/vince-vaughn/\" rel=\"noopener noreferrer\" target=\"_blank\">Vince Vaughn</a>,&nbsp;<a href=\"https://tim.blog/2020/04/23/brian-koppelman/\" rel=\"noopener noreferrer\" target=\"_blank\">Brian Koppelman</a>,&nbsp;<a href=\"https://tim.blog/2019/05/07/ramit-sethi/\" rel=\"noopener noreferrer\" target=\"_blank\">Ramit Sethi</a>,&nbsp;<a href=\"https://tim.blog/2020/11/18/dax-shepard/\" rel=\"noopener noreferrer\" target=\"_blank\">Dax Shepard</a>,&nbsp;<a href=\"https://tim.blog/2014/10/15/money-master-the-game/\" rel=\"noopener noreferrer\" target=\"_blank\">Tony Robbins</a>,&nbsp;<a href=\"https://tim.blog/2020/05/18/jim-dethmer/\" rel=\"noopener noreferrer\" target=\"_blank\">Jim Dethmer</a>,&nbsp;<a href=\"https://tim.blog/2020/11/19/dan-harris/\" rel=\"noopener noreferrer\" target=\"_blank\">Dan Harris</a>,&nbsp;<a href=\"https://tim.blog/2017/09/13/ray-dalio/\" rel=\"noopener noreferrer\" target=\"_blank\">Ray Dalio</a>,&nbsp;<a href=\"https://tim.blog/2015/08/18/the-evolutionary-angel-naval-ravikant/\" rel=\"noopener noreferrer\" target=\"_blank\">Naval Ravikant</a>,&nbsp;<a href=\"https://tim.blog/2021/03/08/vitalik-buterin-naval-ravikant/\" rel=\"noopener noreferrer\" target=\"_blank\">Vitalik Buterin</a>,&nbsp;<a href=\"https://tim.blog/2021/03/16/elizabeth-lesser/\" rel=\"noopener noreferrer\" target=\"_blank\">Elizabeth Lesser</a>,&nbsp;<a href=\"https://tim.blog/2019/04/18/amanda-palmer-2/\" rel=\"noopener noreferrer\" target=\"_blank\">Amanda Palmer</a>,&nbsp;<a href=\"https://tim.blog/2021/02/18/katie-haun/\" rel=\"noopener noreferrer\" target=\"_blank\">Katie Haun</a>,&nbsp;<a href=\"https://tim.blog/2017/10/09/richard-branson/\" rel=\"noopener noreferrer\" target=\"_blank\">Sir Richard Branson</a>,&nbsp;<a href=\"https://tim.blog/2020/09/02/chuck-palahniuk/\" rel=\"noopener noreferrer\" target=\"_blank\">Chuck Palahniuk</a>,&nbsp;<a href=\"https://tim.blog/2017/10/18/arianna-huffington/\" rel=\"noopener noreferrer\" target=\"_blank\">Arianna Huffington</a>,&nbsp;<a href=\"https://tim.blog/2015/08/31/the-oracle-of-silicon-valley-reid-hoffman-plus-michael-mccullough/\" rel=\"noopener noreferrer\" target=\"_blank\">Reid Hoffman</a>,&nbsp;<a href=\"https://tim.blog/2017/09/17/bill-burr/\" rel=\"noopener noreferrer\" target=\"_blank\">Bill Burr</a>,&nbsp;<a href=\"https://tim.blog/2015/06/26/whitney-cummings/\" rel=\"noopener noreferrer\" target=\"_blank\">Whitney Cummings</a>,&nbsp;<a href=\"https://tim.blog/2015/05/15/rick-rubin/\" rel=\"noopener noreferrer\" target=\"_blank\">Rick Rubin</a>,&nbsp;<a href=\"https://tim.blog/2020/03/26/vivek-murthy/\" rel=\"noopener noreferrer\" target=\"_blank\">Dr. Vivek Murthy</a>,&nbsp;<a href=\"https://tim.blog/2017/09/09/darren-aronofsky/\" rel=\"noopener noreferrer\" target=\"_blank\">Darren Aronofsky</a>, and many more.</p><p>See Privacy Policy at <a href=\"https://art19.com/privacy\" rel=\"noopener noreferrer\" target=\"_blank\">https://art19.com/privacy</a> and California Privacy Notice at <a href=\"https://art19.com/privacy#do-not-sell-my-info\" rel=\"noopener noreferrer\" target=\"_blank\">https://art19.com/privacy#do-not-sell-my-info</a>.</p>",
        "pub_date_ms": 1634222633126,
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
        "link": "https://exponent.fm/episode-194-back-on-spotify/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/463b7db874c04c3ca66cefda3e9d4679/",
        "image": "https://production.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-xZm7IMnq5bR-OaJSjb4xQv3.1400x1400.jpg",
        "title": "Episode 194 \u2014 Back on Spotify",
        "podcast": {
          "id": "37589a3e121e40debe4cef3d9638932a",
          "image": "https://production.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-xZm7IMnq5bR-OaJSjb4xQv3.1400x1400.jpg",
          "title": "Exponent",
          "publisher": "Ben Thompson / James Allworth",
          "thumbnail": "https://production.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-8sx24A_0Jlk-OaJSjb4xQv3.300x300.jpg",
          "listen_score": 59,
          "listennotes_url": "https://www.listennotes.com/c/37589a3e121e40debe4cef3d9638932a/",
          "listen_score_global_rank": "0.1%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-8sx24A_0Jlk-OaJSjb4xQv3.300x300.jpg",
        "description": "<p>Ben and James discuss the history of podcasts and why Spotify&#8217;s recent announcements are so compelling for creators.</p>\n<p><strong>Links</strong></p>\n<ul>\n<li>Ben Thompson: Spotify&#8217;s Surprise \u2014 <a href=\"https://stratechery.com/2021/spotifys-surprise/\">Stratechery</a></li>\n<li>Episode 185 \u2014 Open, Free, and Spotify \u2014 <a href=\"https://exponent.fm/episode-185-open-free-and-spotify/\">Exponent</a></li>\n<li>Ben Thompson: Podcasts, Analytics, and Centralization \u2014 <a href=\"https://stratechery.com/2017/podcasts-analytics-and-centralization/\">Stratechery</a></li>\n<li>Ben Thompson: Spotify\u2019s Podcast Aggregation Play \u2014 <a href=\"https://stratechery.com/2019/spotifys-podcast-aggregation-play/\">Stratechery</a></li>\n<li>Ben Thompson: Dithering and Open Versus Free \u2014 <a href=\"https://stratechery.com/2020/dithering-and-the-open-web/\">Stratechery</a></li>\n<li>Ben Thompson: Spotify Earnings, Podcasts and Lifetime Value, The Ringer Acquisition \u2014 <a href=\"https://stratechery.com/2020/spotifys-earnings-podcasts-and-lifetime-value-the-ringer-acquisition/\">Stratechery</a></li>\n<li>Ben Thompson: The European Super League, Apple Music\u2019s Letter to Artists \u2014 <a href=\"https://stratechery.com/2021/the-european-super-league-apple-musics-letter-to-artists/\">Stratechery</a></li>\n<li>Ben Thompson: Podcast Subscriptions vs. the App Store \u2014 <a href=\"https://stratechery.com/2021/podcast-subscriptions-vs-the-app-store/\">Stratechery</a></li>\n<li>Ben Thompson: Fearing Spotify?, Apple\u2019s Earnings, Margins and Chips \u2014 <a href=\"https://stratechery.com/2021/fearing-spotify-apples-earnings-margins-and-chips/\">Stratechery</a></li>\n</ul>\n<p><strong>Hosts</strong></p>\n<p>\u00a0</p>\n<ul>\n<li>Ben Thompson, <a href=\"http://twitter.com/benthompson\">@benthompson</a>, <a href=\"http://stratechery.com\">Stratechery</a></li>\n<li>James Allworth, <a href=\"http://twitter.com/jamesallworth\">@jamesallworth</a>, <a href=\"https://hbr.org/search?term=James+Allworth&#038;sort=popularity_score\">Harvard Business Review</a></li>\n</ul>\n<p>\u00a0</p>\n<p><strong>Podcast Information</strong></p>\n<p>\u00a0</p>\n<ul>\n<li><a href=\"https://exponent.fm/feed/\">Feed</a></li>\n<li><a href=\"https://itunes.apple.com/us/podcast/exponent/id826420969\">iTunes</a></li>\n<li><a href=\"https://soundcloud.com/exponentfm\">SoundCloud</a></li>\n<li><a href=\"http://twitter.com/exponentfm\">Twitter</a></li>\n<li><a href=\"http://stratechery.com/exponent-feedback/\">Feedback</a></h2>\n</li>\n</ul>",
        "pub_date_ms": 1619771580003,
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
      "id": 475797,
      "data": {
        "id": "4c72c4dfac004ffca0867a70361f77ab",
        "link": "https://jas.simplecast.com/episodes/side-hustle-friday-why-should-you-start-a-podcast-and-monetize-your-podcast-through-ads-and-patreon-bY620w_A?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/4c72c4dfac004ffca0867a70361f77ab/",
        "image": "https://production.listennotes.com/podcasts/the-james-altucher/side-hustle-friday-why-x-OdlkHPweS-jDmTs6Nl-tr.1400x1400.jpg",
        "title": "Side Hustle Friday: Why should you START a podcast and MONETIZE your podcast through Ads and Patreon!",
        "podcast": {
          "id": "6dabf2f65c384e1f897bb606859309f4",
          "image": "https://production.listennotes.com/podcasts/the-james-altucher-show-james-altucher-50EFuIdlcY4-sSHocv8YjIe.1400x1400.jpg",
          "title": "The James Altucher Show",
          "publisher": "James Altucher",
          "thumbnail": "https://production.listennotes.com/podcasts/the-james-altucher-show-james-altucher-6q58dRHpmvW-sSHocv8YjIe.300x300.jpg",
          "listen_score": 67,
          "listennotes_url": "https://www.listennotes.com/c/6dabf2f65c384e1f897bb606859309f4/",
          "listen_score_global_rank": "0.05%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/the-james-altucher/side-hustle-friday-why-BpGUVA-oL_v-jDmTs6Nl-tr.300x300.jpg",
        "description": "<p>Another Side Hustle Friday! I sat down with Jay Yow, the Sound Engineer/ Producer of The James Altucher, to discuss ways to monetize a podcast, we spoke about why this is the best time to launch a podcast and our equipment set up for remote recording and interview. In this episode, we break down that's the different ways you can monetize through Ads, sponsors, affiliate deals, and Patreon! Part 2 will be coming soon Monday!</p>\n<hr />\n<p><strong>I write about all my podcasts! Check out the full post and learn what I learned at <a href=\"https://www.jamesaltucher.com/podcast\">jamesaltucher.com/podcast</a>.</strong></p>\n<p><strong>Thanks so much for listening! If you like this episode, please subscribe to \u201cThe James Altucher Show\u201d and rate and review wherever you get your podcasts:</strong></p>\n<p><a href=\"https://itunes.apple.com/us/podcast/the-james-altucher-show/id794030859?mt=2\">Apple Podcasts</a></p>\n<p><a href=\"https://www.stitcher.com/podcast/stansberry-radio-network/the-james-altucher-show/e/52735033\">Stitcher</a></p>\n<p><a href=\"https://www.iheart.com/podcast/232-The-James-Altucher-Show-27085086/episode/ep-298-ryan-holiday-competition-28789411/\">iHeart Radio</a></p>\n<p><a href=\"https://open.spotify.com/episode/0ABi9w3Qrb2EFNDeeXlHyz\">Spotify</a></p>\n<p> </p>\n<p><strong>Follow me on Social Media:</strong></p>\n<p><a href=\"https://www.youtube.com/channel/UCRQlx2klE_aNrPhz2OyKRdg\">YouTube</a></p>\n<p><a href=\"https://twitter.com/jaltucher\">Twitter</a></p>\n<p><a href=\"https://www.facebook.com/JAltucher.Blog/\">Facebook</a></p>\n<p><a href=\"https://www.linkedin.com/in/jamesaltucher\">Linkedin</a></p>",
        "pub_date_ms": 1602831600335,
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
        "link": "https://jas.simplecast.com/episodes/side-hustle-friday-monetize-your-podcast-right-now-LY_D4F1p?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/d5e2112643ac4d01baaa8eab6c7b7cae/",
        "image": "https://production.listennotes.com/podcasts/the-james-altucher/side-hustle-friday-monetize-nJaycZ39zdH-vZt0gi5hoDN.1400x1400.jpg",
        "title": "Side Hustle Friday: Monetize your podcast right now!",
        "podcast": {
          "id": "6dabf2f65c384e1f897bb606859309f4",
          "image": "https://production.listennotes.com/podcasts/the-james-altucher-show-james-altucher-50EFuIdlcY4-sSHocv8YjIe.1400x1400.jpg",
          "title": "The James Altucher Show",
          "publisher": "James Altucher",
          "thumbnail": "https://production.listennotes.com/podcasts/the-james-altucher-show-james-altucher-6q58dRHpmvW-sSHocv8YjIe.300x300.jpg",
          "listen_score": 67,
          "listennotes_url": "https://www.listennotes.com/c/6dabf2f65c384e1f897bb606859309f4/",
          "listen_score_global_rank": "0.05%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/the-james-altucher/side-hustle-friday-monetize-TGCj-9qP0Nw-vZt0gi5hoDN.300x300.jpg",
        "description": "<p>Part 2 on monetizing your podcast! In this episode, we talked about ways to monetize your podcast via merchandising, getting hired as a consultant through your podcast, speaking gigs, on and on! Also, enjoy Jay's episodic debut on the podcast! (Technically a second since this is a part of Friday's podcast!)</p>\n<hr />\n<p><strong>I write about all my podcasts! Check out the full post and learn what I learned at <a href=\"https://www.jamesaltucher.com/podcast\">jamesaltucher.com/podcast</a>.</strong></p>\n<p><strong>Thanks so much for listening! If you like this episode, please subscribe to \u201cThe James Altucher Show\u201d and rate and review wherever you get your podcasts:</strong></p>\n<p><a href=\"https://itunes.apple.com/us/podcast/the-james-altucher-show/id794030859?mt=2\">Apple Podcasts</a></p>\n<p><a href=\"https://www.stitcher.com/podcast/stansberry-radio-network/the-james-altucher-show/e/52735033\">Stitcher</a></p>\n<p><a href=\"https://www.iheart.com/podcast/232-The-James-Altucher-Show-27085086/episode/ep-298-ryan-holiday-competition-28789411/\">iHeart Radio</a></p>\n<p><a href=\"https://open.spotify.com/episode/0ABi9w3Qrb2EFNDeeXlHyz\">Spotify</a></p>\n<p> </p>\n<p><strong>Follow me on Social Media:</strong></p>\n<p><a href=\"https://www.youtube.com/channel/UCRQlx2klE_aNrPhz2OyKRdg\">YouTube</a></p>\n<p><a href=\"https://twitter.com/jaltucher\">Twitter</a></p>\n<p><a href=\"https://www.facebook.com/JAltucher.Blog/\">Facebook</a></p>\n<p><a href=\"https://www.linkedin.com/in/jamesaltucher\">Linkedin</a></p>",
        "pub_date_ms": 1603090800333,
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
        "link": "https://podcasters.spotify.com/pod/show/thisweekinstartups/episodes/E1096-Podcasting-State-of-the-Union-featuring-Overcasts-Marco-Arment--Oxford-Roads-Dan-Granger-e1cgtk4?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/3c311c8cf83448dea0463c69bfe61c75/",
        "image": "https://production.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-d9kz8SVeAwn-EKckR36zrnA.1400x1400.jpg",
        "title": "E1096: Podcasting State of the Union featuring Overcast\u2019s Marco Arment & Oxford Road\u2019s Dan Granger",
        "podcast": {
          "id": "9a62e2581908415185dee35d2d19f9b5",
          "image": "https://production.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-d9kz8SVeAwn-EKckR36zrnA.1400x1400.jpg",
          "title": "This Week in Startups",
          "publisher": "Jason Calacanis",
          "thumbnail": "https://production.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-LZCcPIajWVQ-EKckR36zrnA.300x300.jpg",
          "listen_score": 64,
          "listennotes_url": "https://www.listennotes.com/c/9a62e2581908415185dee35d2d19f9b5/",
          "listen_score_global_rank": "0.05%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-LZCcPIajWVQ-EKckR36zrnA.300x300.jpg",
        "description": "Follow Marco: https://twitter.com/marcoarment<br />\n<br />\nDownload Overcast: https://overcast.fm<br />\n<br />\nFollow Oxford Road: https://twitter.com/Oxford_Road<br />\n<br />\nFollow Jason: https://linktr.ee/calacanis<br />\n<br />\nThanks to our partners...<br />\nSendPro Online from Pitney Bowes - Try it free for 30 days and get a free 10-pound scale at https://pb.com/twist<br />\nLinkedIn Marketing - Get $100 off your first advertising campaign at https://linkedin.com/thisweekinstartups<br />\nVanta - $1k off your SOC 2 at https://vanta.com/twist",
        "pub_date_ms": 1597416466670,
        "guid_from_rss": "https://thisweekinstartups.com/?p=41080",
        "listennotes_url": "https://www.listennotes.com/e/3c311c8cf83448dea0463c69bfe61c75/",
        "audio_length_sec": 5249,
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
        "image": "https://production.listennotes.com/podcasts/the-casey-adams-show/elise-hu-hosting-ted-talks-Y6q40Ejr-ZX-wUV0p1Rd3zs.1400x1400.jpg",
        "title": "Elise Hu - Hosting \"TED Talks Daily\" & The Future of Podcasting",
        "podcast": {
          "id": "11362a0682e744b29ce5ea73c920132e",
          "image": "https://production.listennotes.com/podcasts/the-casey-adams-show-casey-adams-8wD2LP_N53x-YuarHs5lfDI.1400x1400.jpg",
          "title": "The Casey Adams Show",
          "publisher": "Casey Adams",
          "thumbnail": "https://production.listennotes.com/podcasts/the-casey-adams-show-casey-adams-3HEVj-Ons4h-YuarHs5lfDI.300x300.jpg",
          "listen_score": 53,
          "listennotes_url": "https://www.listennotes.com/c/11362a0682e744b29ce5ea73c920132e/",
          "listen_score_global_rank": "0.5%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/the-casey-adams-show/elise-hu-hosting-ted-talks-FbSdafYDC9N-wUV0p1Rd3zs.300x300.jpg",
        "description": "<p>Elise Hu is a host-at-large based at NPR West in Culver City, Calif. Previously, she explored the future with her video series, <a href=\"https://www.npr.org/2019/05/06/716414780/videos-future-you\"><em>Future You with Elise Hu</em></a>, and served as the founding bureau chief and International Correspondent for NPR's Seoul office. She was based in Seoul for nearly four years, responsible for the network's coverage of both Koreas and Japan, and filed from a dozen countries across Asia. Before joining NPR, she was one of the founding reporters at <a href=\"http://www.texastribune.org/\">The Texas Tribune</a>, a non-profit digital news startup devoted to politics and public policy. While at the Tribune, Hu oversaw television partnerships and multimedia projects, contributed to <em>The New York Times</em>' expanded Texas coverage, and pushed for editorial innovation across platforms.Her work at NPR has earned a DuPont-Columbia award and a Gracie Award from the Alliance for Women in Media for her video series, <em>Elise Tries</em>. Her previous work has earned a Gannett Foundation Award for Innovation in Watchdog Journalism, a National Edward R. Murrow award for best online video, and beat reporting awards from the Texas Associated Press. <em>The Austin Chronicle</em> once dubiously named her the \"<a href=\"http://www.austinchronicle.com/gyrobase/Awards/BestOfAustin?Award=660138\">Best TV Reporter Who Can Write</a>.\"</p>\n<p>Follow Elise Hu on Instagram: <a href=\"https://www.instagram.com/elisewho/?hl=en\">https://www.instagram.com/elisewho/?hl=en</a></p>\n<p>Learn more about Elise Hu: <a href=\"https://elisehu.com/\">https://elisehu.com/</a></p>\n<p>Listen to \"TED Talks Daily\" <a href=\"https://podcasts.apple.com/us/podcast/ted-talks-daily/id160904630\">https://podcasts.apple.com/us/podcast/ted-talks-daily/id160904630</a></p>\n<p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
        "pub_date_ms": 1586266731164,
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
        "link": "https://sites.libsyn.com/45546/167-cleanfeed-with-a-side-of-google-podcasts?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/8f51c8e8b19a4c638ecbce12f9322ba8/",
        "image": "https://production.listennotes.com/podcasts/the-feed-the/167-cleanfeed-with-a-side-of-_HxANWiUlRk-OS-PBaQKcgl.1400x1400.jpg",
        "title": "167 Cleanfeed With A Side of Google Podcasts",
        "podcast": {
          "id": "ce3754058c7a44a0abd574f86ff5c719",
          "image": "https://production.listennotes.com/podcasts/the-feed-the-official-libsyn-podcast-elsie-vpSizOJdtuG-2kOexVdGJIv.1400x1400.jpg",
          "title": "The Feed The Official Libsyn Podcast",
          "publisher": "Elsie Escobar and Rob Walch",
          "thumbnail": "https://production.listennotes.com/podcasts/the-feed-the-official-libsyn-podcast-elsie-1gCfKIP5XVy-2kOexVdGJIv.300x300.jpg",
          "listen_score": 44,
          "listennotes_url": "https://www.listennotes.com/c/ce3754058c7a44a0abd574f86ff5c719/",
          "listen_score_global_rank": "1%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/the-feed-the/167-cleanfeed-with-a-side-of-KEMJ65zVY4x-OS-PBaQKcgl.300x300.jpg",
        "description": "<p>Tons of details on all things Google Podcasts Manager! It\u2019s like Apple Podcasts connect but of course Google. Then, we move on to jobs in podcasting, so much about feedback about Cleanfeed, some very interesting Facebook updates, Libsyn player automation, what if someone uses YOUR podcast name, a massive breakdown of the podfader types and of course we\u2019ve got a crazy amount of stats!</p> <p>Audience feedback drives the show. We\u2019d love for you to email us and keep the conversation going! Email thefeed@libsyn.com or call 412\u2013573\u20131934. We\u2019d love to hear from you!</p> Quick Episode Summary <ul> <li><em>:07</em> Intro!</li> <li><em>3:04 PROMO 1: Sailing in the Mediterranean and Beyond</em></li> <li><em>3:34</em> Rob and Elsie conversation</li> <li>Announcement of Google Podcasts Manager!</li> <li>What it is, what it gives you and how it it different than Apple Podcasts analytics</li> <li>9:46 Apple is hiring for all kinds of podcasting positions</li> <li>13:56 Cleanfeed audio feedback from Carey Green</li> <li>Emails about Cleanfeed</li> <li>18:08 Cleanfeed audio feedback from CG</li> <li>Thoughts and processes about remote recording</li> <li>There\u2019s a new kid in town</li> <li>27:35 Facebook updates about charging for online events and listening to Faceboook Lives</li> <li>30:58 PROMO 2: The Naturist Living Show</li> <li>New version of Podcast Addict now with reviews</li> <li>Custom automation for the libsyn players</li> <li>Face ID and masks</li> <li>39:55 What if someone is using the name of your show? How do you go about dealing with it?</li> <li>A show appearing twice on some apps</li> <li>49:43 Podfading - the key main groups</li> <li>UK data from Rajar on internet delivery audio services via Neil!</li> <li>57:38 PROMO 3: The Europe Desk</li> <li>Stats, stats, stats: mean and median</li> <li>59:52 COVID\u201319 libsyn stats</li> <li>Where have we been?</li> <li>Where are we going?</li> </ul> Featured Podcast Promos + Audio <ul> <li><a href=\"https://www.medsailor.com/\">PROMO 1: Sailing in the Mediterranean and Beyond</a></li> <li><a href=\"https://www.naturistlivingshow.com/\">PROMO 2: The Naturist Living Show</a></li> <li><a href=\"https://cges.georgetown.edu/research/podcast/\">PROMO 3: The Europe Desk</a></li> <li><a href=\"https://podcastfasttrack.com/\">Carey Green from Podcast Fast Track</a></li> <li><a href=\"https://www.therocketryshow.com/\">CB from the Rocketry Show</a></li> </ul> <p>Thank you to Nick from <a href=\"http://micme.com\">MicMe</a> for our awesome intro!</p>  <p><em>Podcasting Articles and Links mentioned by Rob and Elsie</em></p> <ul> <li><a href=\"http://speakpipe.com/thefeed\">Our SpeakPipe Feedback page!</a> Leave us feedback :)</li> <li><a href=\"http://podcastsmanager.google.com\">Google Podcasts Podcast Manager</a></li> <li><a href=\"https://podcasts.google.com/manager/about\">Google Podcasts Manager About Page</a></li> <li><a href=\"https://support.google.com/podcast-publishers/answer/9479755?hl=en&amp;ref_topic=9476973&amp;authuser=0\"> Adding new and existing podcasts</a></li> <li><a href=\"https://search.google.com/devtools/podcast/preview\">Is your show already in Google Podcasts? Check here</a></li> <li><a href=\"https://support.google.com/podcast-publishers/answer/9696727?hl=en&amp;ref_topic=9476973&amp;authuser=0\"> Manage users and permissions on Google Podcasts Manager</a></li> <li><a href=\"https://support.google.com/podcast-publishers?hl=en&amp;authuser=0#topic=9476973\"> Google Podcasts Manager Support</a></li> <li><a href=\"https://jobs.apple.com/en-us/details/200164774/podcasts-operations-manager?team=MKTG\"> Podcasts Operations Manager</a></li> <li><a href=\"https://jobs.apple.com/en-us/details/200164287/program-manager-podcasts-apple-media-products?team=SFTWR\"> Program Manager, Podcasts, Apple Media Products</a></li> <li><a href=\"https://jobs.apple.com/en-us/details/200164774/podcasts-operations-manager?team=MKTG\"> UI Engineer, Apple Media Products (Podcasts)</a></li> <li><a href=\"https://youtu.be/DpRHSmJT_Vk\">Carey\u2019s Cleanfeed demo video</a></li> <li><a href=\"http://podcastification.com/in-search-of-the-best-way-to-record-an-interview-with-mark-hills-of-cleanfeed-ep-69\"> Carey\u2019s interview with Mark from Cleanfeed</a></li> <li><a href=\"https://podcastengineeringschool.com/marc-bakos-of-cleanfeed-pes-104/\"> Chris Curran\u2019s interview with Marc from Cleanfeed</a></li> <li><a href=\"https://www.reddit.com/r/podcasting/comments/flw9ae/services_and_applications_to_allow_remote/\"> Services and applications to allow remote recordings of remote guests and co-hosts. - Reddit</a></li> <li><a href=\"http://podcast411.com/mixer.pdf\">Rob\u2019s PDF</a></li> <li><a href=\"https://resonaterecordings.com/2020/04/voice-recorder\">Resonate Recordings new recorder</a></li> <li><a href=\"https://about.fb.com/news/2020/04/introducing-messenger-rooms/\">Facebook news</a></li> <li><a href=\"https://www.rajar.co.uk/docs/news/MIDAS_Spring_2020.pdf\">Rajar data for Measurement of Internet Delivery Audio Services</a></li> <li><a href=\"https://twitter.com/search?q=podcast411%20%23cmworld&amp;src=typed_query&amp;f=live\"> Rob\u2019s #CMWorld twitter chat</a></li> <li><a href=\"https://jacobsmedia.com/there-are-over-a-million-podcasts-in-apples-podcasts-app-what-does-it-mean/\"> There Are Over A Million Podcasts In Apple\u2019s Podcasts App, What Does It Mean?</a></li> <li><a href=\"http://www.insideradio.com/podcastnewsdaily/walch-podcast-downloads-aren-t-down-as-much-as-mobility-showing-medium-s-stickiness/article_394e057a-84ba-11ea-a6d0-a3defc713949.html\"> Walch: Proof Of Podcast \u2018Stickiness.\u2019</a></li> </ul>  <em>HELP US SPREAD THE WORD!</em> <p><em>We\u2019d love it if you could please share #TheFeed with your twitter followers. <a href=\"http://clicktotweet.com/9d2te\">Click here to post a tweet!</a></em></p> <p><em>If you dug this episode head on over to Apple Podcasts and kindly <a href=\"https://itunes.apple.com/us/podcast/feed-official-libsyn-podcast/id668413144\"> leave us a rating, a review and subscribe!</a></em></p> <em>Ways to subscribe to The Feed: The Official Libsyn Podcast</em> <ul> <li><em><a href=\"https://itunes.apple.com/us/podcast/feed-official-libsyn-podcast/id668413144\"> Click here to subscribe via Apple Podcasts</a></em></li> <li><em><a href=\"http://thefeed.libsyn.com/rss\">Click here to subscribe via RSS</a></em></li> <li><em><a href=\"http://www.stitcher.com/podcast/libsyn/the-feed\">You can also subscribe via Stitcher</a></em></li> </ul> FEEDBACK + PROMOTION <p><em>You can ask your questions, make comments and create a segment about podcasting for podcasters! Let your voice be heard.</em></p> <ul> <li>Download the FREE The Feed App for <a href=\"https://itunes.apple.com/us/app/the-feed-podcasting-tips-from-libsyn/id381787434?mt=8\"> iOS</a> and <a href=\"https://play.google.com/store/apps/details?id=com.libsyn.android.thefeed&amp;hl=en\"> Android</a> (you can send feedback straight from within the app)</li> <li>Call 412 573 1934</li> <li>Email thefeed@libsyn.com</li> <li>Use our <a href=\"http://speakpipe.com/thefeed\">SpeakPipe Page</a>!</li> </ul>",
        "pub_date_ms": 1588694700075,
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
        "link": "http://mschool.libsyn.com/spotify-acquired-the-ringer-podcast-15m-in-revenues-heres-what-it-means-ep-1306?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/dbd3d477dfc94128982b79e8152301b4/",
        "image": "https://production.listennotes.com/podcasts/marketing-school-digital-marketing-and-fY51JWywOLF-pHyiIJT4Lxl.1400x1400.jpg",
        "title": "Spotify Acquired 'The Ringer' Podcast ($15M In Revenues) - Here's What It Means  | Ep. #1306",
        "podcast": {
          "id": "9a2abf6b68b54554a60a32a2932febcb",
          "image": "https://production.listennotes.com/podcasts/marketing-school-digital-marketing-and-fY51JWywOLF-pHyiIJT4Lxl.1400x1400.jpg",
          "title": "Marketing School - Digital Marketing and Online Marketing Tips",
          "publisher": "Eric Siu & Neil Patel",
          "thumbnail": "https://production.listennotes.com/podcasts/marketing-school-digital-marketing-and-G-dNQec3V08-pHyiIJT4Lxl.300x300.jpg",
          "listen_score": 62,
          "listennotes_url": "https://www.listennotes.com/c/9a2abf6b68b54554a60a32a2932febcb/",
          "listen_score_global_rank": "0.1%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/marketing-school-digital-marketing-and-G-dNQec3V08-pHyiIJT4Lxl.300x300.jpg",
        "description": "<p>In episode #1306, we discuss Spotify\u2019s acquisition of The Ringer. The podcasting industry is growing exponentially and Spotify wanted to make an aggressive move toward growing its market share. Tune in to hear why this was a super smart decision on their part!</p> <p>TIME-STAMPED SHOW NOTES:</p> <ul> <li>[00:25] Today\u2019s topic: How Spotify Acquired The Ringer.\u00a0\u00a0</li> <li>[00:42] The solid financial results for Spotify in Q4 of 2019.</li> <li>[00:56] How Spotify recognized exponential growth in podcast hours streamed.</li> <li>[01:24] Realizing that they needed to acquire a big podcast to double down on opportunities.\u00a0\u00a0\u00a0</li> <li>[01:53] The impressive retention rates of the Marketing School podcast.</li> <li>[02:09] Why Spotify\u2019s decision makes a lot of sense.\u00a0</li> <li>[02:39] Keep in mind that all good channels eventually become crowded.\u00a0\u00a0</li> <li>[03:09] Spotify\u2019s market share around podcasting and how they\u2019re more aggressive than Apple.\u00a0</li> <li>[03:48] The number of downloads The Ringer podcast is getting.\u00a0</li> <li>[04:07] Start comparing your Apple Podcast and Spotify analytics for your podcast.\u00a0</li> <li>[04:50] How our podcasts and Eric\u2019s own podcast are performing.\u00a0\u00a0</li> <li>[05:56] The proposed price for The Ringer stated by Bill Simmons: $100 million.\u00a0</li> <li>[06:25] That\u2019s it for today!</li> <li>[06:26] To stay updated with events and learn more about our mastermind, go to the <a href=\"https://marketingschool.io/growth-accelerator-mastermind\"> Marketing School</a> site for more information.</li> </ul> <p>Links Mentioned in Today\u2019s Episode:</p> <ul> <li>\n<a href=\"https://www.spotify.com/\">Spotify</a>\u00a0</li> <li><a href=\"https://www.theringer.com\">The Ringer</a></li> <li><a href=\"https://www.apple.com\">Apple</a></li> <li><a href=\"https://growtheverywhere.com/podcast-player/\">Leveling Up Podcast</a></li> <li><a href=\"https://twitter.com/BillSimmons?ref_src\">Bill Simmons on Twitter</a></li> </ul> <p>Leave Some Feedback:</p> <p>\u00a0</p> <ul> <li>What should we talk about next?\u00a0Please let us know in the comments below</li> </ul> <ul> <li>Did you enjoy this episode?\u00a0If so, please leave a short review.</li> </ul> <p>\u00a0</p> <p>Connect with Us:\u00a0</p> <ul> <li><a href=\"http://neilpatel.com\">Neilpatel.com</a></li> <li>\n<a href=\"https://www.quicksprout.com/\">Quick Sprout</a>\u00a0</li> <li><a href=\"https://growtheverywhere.com/\">Growth Everywhere</a></li> <li><a href=\"https://www.singlegrain.com/\">Single Grain</a></li> <li>\n<a href=\"https://twitter.com/neilpatel\">Twitter @neilpatel</a>\u00a0</li> <li><a href=\"https://twitter.com/ericosiu\">Twitter @ericosiu</a></li> </ul><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://megaphone.fm/adchoices\">megaphone.fm/adchoices</a></p>",
        "pub_date_ms": 1582812001129,
        "guid_from_rss": "bf073240-9680-42e7-89aa-82a2338840dc",
        "listennotes_url": "https://www.listennotes.com/e/dbd3d477dfc94128982b79e8152301b4/",
        "audio_length_sec": 464,
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
        "image": "https://production.listennotes.com/podcasts/recode-media-recode-SNw3MlTLqjC-1iPwTajLXlS.1400x1400.jpg",
        "title": "Spotify, The Ringer and the future of podcasts",
        "podcast": {
          "id": "2aba49dc3fc04e3e96fe89f79a261798",
          "image": "https://production.listennotes.com/podcasts/recode-media-recode-SNw3MlTLqjC-1iPwTajLXlS.1400x1400.jpg",
          "title": "Recode Media",
          "publisher": "Recode",
          "thumbnail": "https://production.listennotes.com/podcasts/recode-media-recode-ReV9rxkUvST-1iPwTajLXlS.300x300.jpg",
          "listen_score": 54,
          "listennotes_url": "https://www.listennotes.com/c/2aba49dc3fc04e3e96fe89f79a261798/",
          "listen_score_global_rank": "0.5%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/recode-media-recode-ReV9rxkUvST-1iPwTajLXlS.300x300.jpg",
        "description": "<p>Spotify is buying Bill Simmons\u2019 sports and pop culture website and podcast network, The Ringer. It\u2019s Spotify\u2019s fourth podcast acquisition in a year. Recode\u2019s Peter Kafka (who broke the story) sits down with Vox Media Podcast Network producer and former Ringer staff member Zach Mack to discuss what this deal means for Spotify, The Ringer and the future of podcasts.</p><p><br /></p><p><strong>Featuring</strong>: Zach Mack (<a href=\"https://twitter.com/zachthemack\">@zachthemack</a>), Senior Podcast Producer at Vox Media Podcast Network</p><p><strong>Host</strong>: Peter Kafka\u00a0(<a href=\"https://twitter.com/pkafka\">@pkafka</a>), Senior Editor at Recode</p><p><strong>More to explore</strong>: <a href=\"https://pod.link/1080467174\">Subscribe for free to Recode Media</a>, Peter Kafka, one of the media industry's most acclaimed reporters, talks to business titans, journalists, comedians, and more to get their take on today's media landscape.</p><p><strong>About Recode by Vox</strong>: Recode by Vox helps you understand how tech is changing the world \u2014 and changing us.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
        "pub_date_ms": 1581021870154,
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
        "image": "https://production.listennotes.com/podcasts/a16z-podcast-andreessen-horowitz-avDtXyHJkNw-IWF2alEr-9h.1400x1400.jpg",
        "title": "How We Podcast",
        "podcast": {
          "id": "7c20388d8d7e45d6ae4b770c1fe36b6f",
          "image": "https://production.listennotes.com/podcasts/a16z-podcast-andreessen-horowitz-avDtXyHJkNw-IWF2alEr-9h.1400x1400.jpg",
          "title": "a16z Podcast",
          "publisher": "Andreessen Horowitz",
          "thumbnail": "https://production.listennotes.com/podcasts/a16z-podcast-andreessen-horowitz-ANgqlWfk7aB-IWF2alEr-9h.300x300.jpg",
          "listen_score": 61,
          "listennotes_url": "https://www.listennotes.com/c/7c20388d8d7e45d6ae4b770c1fe36b6f/",
          "listen_score_global_rank": "0.1%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/a16z-podcast-andreessen-horowitz-ANgqlWfk7aB-IWF2alEr-9h.300x300.jpg",
        "description": "<p>\"Hi everyone, welcome to the a16z Podcast...\" ... and welcome to our 500th episode, where, for the first time, we reveal behind-the-scenes details and the backstory of how we built this show, and the broader editorial operation. [You can also listen to episode 499, with head of marketing Margit Wennmachers, on building the a16z brand, <a href=\"https://a16z.com/2019/11/20/brand-building-a16z-ideas-people-marketing/\" target=\"_blank\">here</a>.]</p><p>We've talked a lot about the podcasting industry, and even done podcasts about podcasting, so for this special episode, editor-in-chief and showrunner Sonal Chokshi reveals the how, what, and why in conversation with a16z general partner (and guest-host for this special episode) <a href=\"https://a16z.com/2019/10/01/knowable-audio-startups/\" target=\"_blank\">podcasting</a> fan Connie Chan. We also answer some frequently asked questions that we often get (and recently <a href=\"https://twitter.com/smc90/status/1198026729421324289\" target=\"_blank\">got</a> via Twitter), such as:</p><ul><li>how we program podcasts</li><li>what's the process, from ideas to publishing</li><li>do we edit them and how!</li><li>do guests prep, do we have a script</li><li>technical stack</li></ul><p>...and much more. In fact, much of the conversation goes beyond the a16z Podcast and towards Sonal's broader principles of 'editorial content marketing', which hopefully helps those thinking about their own content operations and podcasts, too. Including where podcasting may be going.</p><p>Finally, we share some unexpected moments, and lessons learned along the way; our positions on \"tics\", swear-words, and talking too fast; failed experiments, and new directions. But most importantly, we share some of the people behind the scenes who help make the a16z Podcast what it was, is, and can be... with thanks most of all to *you*, our wonderful fans!</p>",
        "pub_date_ms": 1574838000212,
        "guid_from_rss": "2307c44b-8b88-4348-b4f5-3deaa204135e",
        "listennotes_url": "https://www.listennotes.com/e/eaa81f7bba344ae78bcf228b88e102a7/",
        "audio_length_sec": 2864,
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
        "link": "https://www.instagram.com/tboypod?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/1ca5d330311d4808a4dbc668680f565b/",
        "image": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-syLJP5rimSp-kmx0XIZTAys.1400x1400.jpg",
        "title": "*Live* at Spotify - Part II: Why Spotify is doing podcasts \u2014 Our interview with Max Cutler,  Founder & MD of podcasts at Spotify",
        "podcast": {
          "id": "c5ce6c02cbf1486496206829f7d42e8e",
          "image": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-syLJP5rimSp-kmx0XIZTAys.1400x1400.jpg",
          "title": "The Best One Yet",
          "publisher": "Nick & Jack Studios",
          "thumbnail": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-YPWcDaHknUz-kmx0XIZTAys.300x300.jpg",
          "listen_score": 71,
          "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
          "listen_score_global_rank": "0.05%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-YPWcDaHknUz-kmx0XIZTAys.300x300.jpg",
        "description": "<p>The 2nd half of our Snacks recording live from Spotify. We sit down with Max Cutler, the Founder &amp; MD of Parcast Studios at Spotify \u2014 his startup was acquired by Spotify earlier this year. We\u2019re asking about how he first pitched his company, whether podcasts will follow the Netflix strategy, and what his favorite pod is. Ever.</p><p><br /></p><p><br /></p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
        "pub_date_ms": 1574852400737,
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
        "link": "https://www.instagram.com/tboypod?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/df11c9fde8234140a705c4aedff2561e/",
        "image": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-syLJP5rimSp-kmx0XIZTAys.1400x1400.jpg",
        "title": "*Live* at Spotify - Part I: How we build this (every day)",
        "podcast": {
          "id": "c5ce6c02cbf1486496206829f7d42e8e",
          "image": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-syLJP5rimSp-kmx0XIZTAys.1400x1400.jpg",
          "title": "The Best One Yet",
          "publisher": "Nick & Jack Studios",
          "thumbnail": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-YPWcDaHknUz-kmx0XIZTAys.300x300.jpg",
          "listen_score": 71,
          "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
          "listen_score_global_rank": "0.05%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-YPWcDaHknUz-kmx0XIZTAys.300x300.jpg",
        "description": "<p>Spotify invited us to their NYC offices to record a live podcast \u2014 it\u2019s a podcast about podcasts for our podcast listening Snackers. We introduce to the Snackers how we got into podcasting, how we built this podcast (every day), and the 5 ingredients for a podcast that people will actually listen to.\u00a0</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
        "pub_date_ms": 1574420400740,
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
          "listen_score": 44,
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
        "link": "https://demandgenradio.com/e/129-how-to-build-your-brand-with-podcasting/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/44017cd438a24139a913a3e288a518fe/",
        "image": "https://production.listennotes.com/podcasts/demandgen-radio-bdo-digital-llc-HQsKlnZm_2T-oVByO3tuFwR.1400x1400.jpg",
        "title": "#129 How to Build your Brand with Podcasting",
        "podcast": {
          "id": "f446a0eaac2e481991e36467e4a4f96f",
          "image": "https://production.listennotes.com/podcasts/demandgen-radio-bdo-digital-llc-HQsKlnZm_2T-oVByO3tuFwR.1400x1400.jpg",
          "title": "DemandGen Radio",
          "publisher": "BDO Digital, LLC",
          "thumbnail": "https://production.listennotes.com/podcasts/demandgen-radio-bdo-digital-llc-dsf5BPZyLFi-oVByO3tuFwR.300x300.jpg",
          "listen_score": 35,
          "listennotes_url": "https://www.listennotes.com/c/f446a0eaac2e481991e36467e4a4f96f/",
          "listen_score_global_rank": "2.5%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/demandgen-radio-bdo-digital-llc-dsf5BPZyLFi-oVByO3tuFwR.300x300.jpg",
        "description": "<p></p>\n<p>Jordan Paris is a 21-year-old entrepreneur who runs a wildly successful podcast. In this episode, he shares how and why he started his podcast and how podcasting propelled the growth of his business and personal brand. Tune in as Jordan shares how he remains so driven and accomplished at an early age, what lessons he\u2019s learned from starting his podcast, and how you can benefit from starting your own podcast.</p>",
        "pub_date_ms": 1569146400140,
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
        "description": "<p>Harvard Business School professors <strong><a href=\"https://www.hbs.edu/faculty/Pages/profile.aspx?facId=6446\" rel=\"noopener\" target=\"_blank\">John Deighton</a></strong> and <strong><a href=\"https://www.hbs.edu/faculty/Pages/profile.aspx?facId=6536\" rel=\"noopener\" target=\"_blank\">Jeffrey Rayport</a></strong> discuss their case, &#8220;<a href=\"https://store.hbr.org/product/gimlet-media-a-podcasting-startup/918413?sku=918413-PDF-ENG\" rel=\"noopener\" target=\"_blank\">Gimlet Media: A Podcasting Startup</a>,&#8221; and how two former public radio producers launch a podcast network, entering the last frontier of digital media. Can they turn a content supplier into a disruptive platform?</p>",
        "pub_date_ms": 1569948476094,
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
        "image": "https://production.listennotes.com/podcasts/function-with-anil/the-wild-world-of-podcast-ads--OEJf2RUIkX-igyS-B5r24A.1400x1400.jpg",
        "title": "The Wild World of Podcast Ads",
        "podcast": {
          "id": "3b7c6c851ec14f40bb062b918942aa15",
          "image": "https://production.listennotes.com/podcasts/function-with-anil-dash-vox-media-3DjNoAIGtV_-pfqIzGD4odn.1400x1400.jpg",
          "title": "Function with Anil Dash",
          "publisher": "Vox Media",
          "thumbnail": "https://production.listennotes.com/podcasts/function-with-anil-dash-vox-media-yYP_8KQFk06-pfqIzGD4odn.300x300.jpg",
          "listen_score": 42,
          "listennotes_url": "https://www.listennotes.com/c/3b7c6c851ec14f40bb062b918942aa15/",
          "listen_score_global_rank": "1.5%"
        },
        "thumbnail": "https://production.listennotes.com/podcasts/function-with-anil/the-wild-world-of-podcast-ads-Rj6u3btNrmq-igyS-B5r24A.300x300.jpg",
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
    }
  ],
  "total": 38,
  "thumbnail": "https://production.listennotes.com/podcast-playlists/podcasts-about-podcasting-0LlKxjtQnf1-m1pe7z60bsw.300x300.jpg",
  "visibility": "public",
  "description": "A curated playlist of podcasts by Wenbin Fang.",
  "listennotes_url": "https://www.listennotes.com/playlists/podcasts-about-podcasting-m1pe7z60bsw/episodes/",
  "last_timestamp_ms": 1565460047367,
  "total_audio_length_sec": 111670
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
      "description": "A 11-character playlist id, which can be used to further fetch detailed playlist metadata via `GET /playlists/{id}`."
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
                    "description": "Episode id, which can be used to further fetch detailed episode metadata via `GET /episodes/{id}`."
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
                        "description": "Podcast id, which can be used to further fetch detailed podcast metadata via `GET /podcasts/{id}`."
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
                    "description": "Podcast id, which can be used to further fetch detailed podcast metadata via `GET /podcasts/{id}`."
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
                        "example": "https://podcasts.google.com/feed/aHR0cHM6Ly9yc3MuYXJ0MTkuY29tL2pvaG4tc29sb21vbi1yZXBvcnRz",
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
                      "amazon_music_url": {
                        "type": "string",
                        "example": "https://music.amazon.com/podcasts/6fc6d683-9ef3-4850-9c35-8e8b1a42a147/the-lock-sportscast",
                        "description": "Amazon Music url for this podcast"
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
                  "audio_length_sec": {
                    "type": "integer",
                    "example": 1291,
                    "description": "Average audio length of all episodes of this podcast. In seconds."
                  },
                  "explicit_content": {
                    "type": "boolean",
                    "example": false,
                    "description": "Whether this podcast contains explicit language."
                  },
                  "latest_episode_id": {
                    "type": "string",
                    "example": "d057092e57cc4ced80e0efaa196593d9",
                    "description": "The id of the most recently published episode of this podcast, which can be used to further fetch detailed episode metadata via `GET /episodes/{id}`."
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
                  "update_frequency_hours": {
                    "type": "integer",
                    "example": 168,
                    "description": "How frequently does this podcast release a new episode? In hours. For example, if the value is 166, then it's every 166 hours (or weekly)."
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
    },
    "total_audio_length_sec": {
      "type": "integer",
      "example": 234567,
      "description": "Total audio length of all episodes in this playlist, in seconds. It will have a valid value only when type is **episode_list**. In other words, it will be 0 if type is **podcast_list**."
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
      "image": "https://production.listennotes.com/podcast-playlists/wenbin-fangs-podcast-playlist-aIykg5GvmcA-kr3-ta28cJu.300x299.jpg",
      "thumbnail": "https://production.listennotes.com/podcast-playlists/wenbin-fangs-podcast-playlist-aIykg5GvmcA-kr3-ta28cJu.300x299.jpg",
      "visibility": "public",
      "description": "Wenbin Fang\u2019s master playlist. Just listen to individual episodes, rather than subscribing to tons of podcasts. How I listen to podcasts: https://lnns.co/6ArPszTwvDE",
      "episode_count": 6049,
      "podcast_count": 82,
      "listennotes_url": "https://www.listennotes.com/playlists/wenbin-fangs-podcast-playlist-kr3-ta28cJu/episodes/",
      "total_audio_length_sec": 18196784
    },
    {
      "id": "m1pe7z60bsw",
      "name": "Podcasts about podcasting",
      "image": "https://production.listennotes.com/podcast-playlists/podcasts-about-podcasting-4bU7MZIlEVO-m1pe7z60bsw.1600x1600.jpg",
      "thumbnail": "https://production.listennotes.com/podcast-playlists/podcasts-about-podcasting-0LlKxjtQnf1-m1pe7z60bsw.300x300.jpg",
      "visibility": "public",
      "description": "A curated playlist of podcasts by Wenbin Fang.",
      "episode_count": 38,
      "podcast_count": 2,
      "listennotes_url": "https://www.listennotes.com/playlists/podcasts-about-podcasting-m1pe7z60bsw/episodes/",
      "total_audio_length_sec": 111670
    },
    {
      "id": "uIK85BM6EWJ",
      "name": "There's a podcast for that",
      "image": "https://production.listennotes.com/podcast-playlists/theres-a-podcast-for-that-ROmWwgXrJhc-uIK85BM6EWJ.300x300.jpg",
      "thumbnail": "https://production.listennotes.com/podcast-playlists/theres-a-podcast-for-that-ROmWwgXrJhc-uIK85BM6EWJ.300x300.jpg",
      "visibility": "public",
      "description": "Inspired by \"There's an app for that\". Email me if you want to become a contributor of this list: hello@listennotes.com",
      "episode_count": 0,
      "podcast_count": 133,
      "listennotes_url": "https://www.listennotes.com/playlists/theres-a-podcast-for-that-uIK85BM6EWJ/podcasts/",
      "total_audio_length_sec": 0
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
            "description": "A 11-character playlist id, which can be used to further fetch detailed playlist metadata via `GET /playlists/{id}`."
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
          },
          "total_audio_length_sec": {
            "type": "integer",
            "example": 234567,
            "description": "Total audio length of all episodes in this playlist, in seconds."
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
    "\"Matt Taibbi\"",
    "Eliezer Yudkowsky",
    "Silicon Valley Bank",
    "\"Paul Bloom\"",
    "Holden Karnofsky",
    "Saagar Enjeti",
    "\"future of banking\"",
    "Kevin Conroy",
    "Mark Drager",
    "Brenda Davis"
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

Suggest related search terms. The results are more comprehensive than from `GET /typeahead`. This endpoint is available only in the PRO/ENTERPRISE plan.

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
    "evergrande group",
    "evergrande stock",
    "evergrande news",
    "evergrande default",
    "evergrande collapse",
    "evergrande crisis",
    "evergrande deadline",
    "evergrande debt"
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




### Fetch audience demographics for a podcast

Function Name: **fetch_audience_for_podcast**

Fetch audience demographics for a podcast - 1) directly measured on the Listen Notes platform; 2) only supports audience breakdown by regions for now; 3) not every podcast has data.

Example:
```python

from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)      

response = client.fetch_audience_for_podcast(id='25212ac3c53240a880dd5032e547047b')
            
print(response.json())

```

See all available parameters on the [API Docs page](https://www.listennotes.com/api/docs/#get-api-v2-podcasts-id-audience).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "by_regions": [
    {
      "ratio": "52.57%",
      "region": "us"
    },
    {
      "ratio": "6.53%",
      "region": "ca"
    },
    {
      "ratio": "5.94%",
      "region": "gb"
    },
    {
      "ratio": "4.62%",
      "region": "in"
    },
    {
      "ratio": "4.06%",
      "region": "au"
    },
    {
      "ratio": "3.14%",
      "region": "de"
    },
    {
      "ratio": "1.25%",
      "region": "fr"
    },
    {
      "ratio": "1.17%",
      "region": "nl"
    },
    {
      "ratio": "1.14%",
      "region": "sg"
    },
    {
      "ratio": "0.90%",
      "region": "es"
    },
    {
      "ratio": "0.80%",
      "region": "za"
    },
    {
      "ratio": "0.78%",
      "region": "br"
    },
    {
      "ratio": "0.77%",
      "region": "pl"
    },
    {
      "ratio": "0.71%",
      "region": "se"
    },
    {
      "ratio": "0.65%",
      "region": "hk"
    },
    {
      "ratio": "0.62%",
      "region": "nz"
    },
    {
      "ratio": "0.58%",
      "region": "id"
    },
    {
      "ratio": "0.56%",
      "region": "ie"
    },
    {
      "ratio": "0.54%",
      "region": "it"
    },
    {
      "ratio": "0.50%",
      "region": "kr"
    },
    {
      "ratio": "0.50%",
      "region": "ch"
    },
    {
      "ratio": "0.48%",
      "region": "no"
    },
    {
      "ratio": "0.48%",
      "region": "ph"
    },
    {
      "ratio": "0.45%",
      "region": "jp"
    },
    {
      "ratio": "0.42%",
      "region": "tw"
    },
    {
      "ratio": "0.41%",
      "region": "pt"
    },
    {
      "ratio": "0.41%",
      "region": "be"
    },
    {
      "ratio": "0.41%",
      "region": "mx"
    },
    {
      "ratio": "0.36%",
      "region": "ru"
    },
    {
      "ratio": "0.36%",
      "region": "ro"
    },
    {
      "ratio": "0.34%",
      "region": "at"
    },
    {
      "ratio": "0.33%",
      "region": "il"
    },
    {
      "ratio": "0.33%",
      "region": "fi"
    },
    {
      "ratio": "0.33%",
      "region": "gr"
    },
    {
      "ratio": "0.30%",
      "region": "pk"
    },
    {
      "ratio": "0.29%",
      "region": "dk"
    },
    {
      "ratio": "0.29%",
      "region": "cz"
    },
    {
      "ratio": "0.27%",
      "region": "th"
    },
    {
      "ratio": "0.26%",
      "region": "vn"
    },
    {
      "ratio": "0.24%",
      "region": "ae"
    },
    {
      "ratio": "0.23%",
      "region": "ua"
    },
    {
      "ratio": "0.21%",
      "region": "bg"
    },
    {
      "ratio": "0.20%",
      "region": "hr"
    },
    {
      "ratio": "0.20%",
      "region": "my"
    },
    {
      "ratio": "0.18%",
      "region": "tr"
    },
    {
      "ratio": "0.17%",
      "region": "sk"
    },
    {
      "ratio": "0.17%",
      "region": "sa"
    },
    {
      "ratio": "0.17%",
      "region": "ar"
    },
    {
      "ratio": "0.15%",
      "region": "ee"
    },
    {
      "ratio": "0.14%",
      "region": "hu"
    },
    {
      "ratio": "0.14%",
      "region": "co"
    },
    {
      "ratio": "0.13%",
      "region": "si"
    },
    {
      "ratio": "0.12%",
      "region": "ng"
    },
    {
      "ratio": "0.11%",
      "region": "ke"
    },
    {
      "ratio": "0.10%",
      "region": "rs"
    },
    {
      "ratio": "0.10%",
      "region": "cl"
    },
    {
      "ratio": "2.39%",
      "region": "others"
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
  "properties": {
    "by_regions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "ratio": {
            "type": "string",
            "example": "20.22%",
            "description": "percentage of audience from this specific region"
          },
          "region": {
            "type": "string",
            "example": "us",
            "description": "2-letter country code of a region."
          }
        }
      }
    }
  }
}
```   
</details>




### Fetch podcasts by a publisher&#x27;s domain name

Function Name: **fetch_podcasts_by_domain**

Fetch podcasts by a publisher&#x27;s domain name, e.g., nytimes.com, wondery.com, npr.org...
Each request will return up to 10 podcasts. You can use the `page` parameter to paginate.


Example:
```python

from listennotes import podcast_api

# If api_key is None, the sdk will connect to a mock server that'll
# return fake data for testing purpose            
api_key = 'a6a1f7ae6a4a4cf7a208e5ba********'

client = podcast_api.Client(api_key=api_key)      

response = client.fetch_podcasts_by_domain(domain_name='nytimes.com')
            
print(response.json())

```

See all available parameters on the [API Docs page](https://www.listennotes.com/api/docs/#get-api-v2-podcasts-domains-domain_name).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "has_next": true,
  "podcasts": [
    {
      "id": "5c6bf053fa6c4d03b4729dbf9cecdfef",
      "rss": "https://feeds.simplecast.com/W1rB_kgL",
      "type": "episodic",
      "email": "popcast@nytimes.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5zaW1wbGVjYXN0LmNvbS9XMXJCX2tnTA==",
        "spotify_url": "https://open.spotify.com/show/3ugDIELXIU7erW5Xp49tWp",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "nytimesarts",
        "facebook_handle": "ParelesNYTimes",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/popcast-the-new-york-times-nlOhfJ9TAt8-dVnjvqYg8ah.1400x1400.jpg",
      "title": "Popcast",
      "country": "United States",
      "website": "http://www.nytimes.com/podcasts/music-popcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        122,
        134
      ],
      "itunes_id": 120315823,
      "publisher": "The New York Times",
      "thumbnail": "https://production.listennotes.com/podcasts/popcast-the-new-york-times-6UPvZJzsd9e-dVnjvqYg8ah.300x300.jpg",
      "is_claimed": false,
      "description": "The Popcast is hosted by Jon Caramanica, a pop music critic for The New York Times. It covers the latest in popular music criticism, trends and news.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 58,
      "total_episodes": 399,
      "listennotes_url": "https://www.listennotes.com/c/5c6bf053fa6c4d03b4729dbf9cecdfef/",
      "audio_length_sec": 3039,
      "explicit_content": false,
      "latest_episode_id": "8fb65359055a4300a1ee0086793fea68",
      "latest_pub_date_ms": 1680809209000,
      "earliest_pub_date_ms": 1406865600397,
      "update_frequency_hours": 179,
      "listen_score_global_rank": "0.5%"
    },
    {
      "id": "f2eb196b20884b0490cc60a58b05bbb6",
      "rss": "https://feeds.simplecast.com/54nAGcIl",
      "type": "episodic",
      "email": "thedaily@nytimes.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5zaW1wbGVjYXN0LmNvbS81NG5BR2NJbA==",
        "spotify_url": "https://open.spotify.com/show/3IM0lmZxpFAY7CwMuv9H4g",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "mikiebarb",
        "facebook_handle": "nytimes",
        "amazon_music_url": "https://music.amazon.com/podcasts/65957f22-45da-431f-8090-83fae75e505a/the-daily",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-daily-the-new-york-times-wLJZBNmd5_Y-xp7nhsmSkX2.1400x1400.jpg",
      "title": "The Daily",
      "country": "United States",
      "website": "https://www.nytimes.com/the-daily?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        216,
        213,
        99,
        67
      ],
      "itunes_id": 1200361736,
      "publisher": "The New York Times",
      "thumbnail": "https://production.listennotes.com/podcasts/the-daily-the-new-york-times-lDnVGaIf7Ks-xp7nhsmSkX2.300x300.jpg",
      "is_claimed": true,
      "description": "This is what the news should sound like. The biggest stories of our time, told by the best journalists in the world. Hosted by Michael Barbaro and Sabrina Tavernise. Twenty minutes a day, five days a week, ready by 6 a.m.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 90,
      "total_episodes": 1810,
      "listennotes_url": "https://www.listennotes.com/c/f2eb196b20884b0490cc60a58b05bbb6/",
      "audio_length_sec": 1706,
      "explicit_content": false,
      "latest_episode_id": "06d63c83a30946fa8ad6b1167cd01f44",
      "latest_pub_date_ms": 1681724700000,
      "earliest_pub_date_ms": 1484687988755,
      "update_frequency_hours": 26,
      "listen_score_global_rank": "0.01%"
    },
    {
      "id": "4685e82279e84054a608c6364912ad73",
      "rss": "https://feeds.simplecast.com/Kctn1RDB",
      "type": "episodic",
      "email": "therunup@nytimes.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5zaW1wbGVjYXN0LmNvbS9LY3RuMVJEQg==",
        "spotify_url": "https://open.spotify.com/show/6mWcEpRBJ3hCMtcBQiKYVv",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-run-up-the-new-york-times-Qe1i-onFph5--Yp_oy2DA8J.1400x1400.jpg",
      "title": "The Run-Up",
      "country": "United States",
      "website": "https://the-run-up.simplecast.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        99
      ],
      "itunes_id": 1142083165,
      "publisher": "The New York Times",
      "thumbnail": "https://production.listennotes.com/podcasts/the-run-up-the-new-york-times-RYloHdW6KEA--Yp_oy2DA8J.300x300.jpg",
      "is_claimed": false,
      "description": "Because it's always about more than who wins and loses. And the next election has already started. Hosted by Astead W. Herndon.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 55,
      "total_episodes": 60,
      "listennotes_url": "https://www.listennotes.com/c/4685e82279e84054a608c6364912ad73/",
      "audio_length_sec": 2058,
      "explicit_content": false,
      "latest_episode_id": "417ff7e7697246cfa79da90a0d973c2c",
      "latest_pub_date_ms": 1681376400000,
      "earliest_pub_date_ms": 1470715200044,
      "update_frequency_hours": 168,
      "listen_score_global_rank": "0.5%"
    },
    {
      "id": "10904b22ae9a4311b2060002562b94aa",
      "rss": "https://feeds.simplecast.com/J6oAIHuK",
      "type": "episodic",
      "email": "tbrandpodcasts@nytimes.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5zaW1wbGVjYXN0LmNvbS9KNm9BSUh1Sw==",
        "spotify_url": "https://open.spotify.com/show/3U20MqXwrI3fZpDYquwH6m",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/built-for-change-bjTiNo0pY4c-sRZa48ULEk6.1400x1400.jpg",
      "title": "Built for Change",
      "country": "United States",
      "website": "https://www.accenture.com/us-en/insights/company/built-for-change-podcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        122,
        244,
        127,
        67,
        97,
        93
      ],
      "itunes_id": 1561378348,
      "publisher": "Accenture",
      "thumbnail": "https://production.listennotes.com/podcasts/built-for-change-peJclDT_HnO-sRZa48ULEk6.300x300.jpg",
      "is_claimed": false,
      "description": "Businesses today face challenges at a scale most leaders have never experienced \u2014 and never anticipated. Built for Change, hosted by broadcast journalist Elise Hu and technologist Josh Klein, explores how the global pandemic has not only forced radical changes in business, technology and human behavior, but also created incredible new opportunities for leaders to evolve and ultimately excel in this environment. Through compelling conversations with industry thought leaders, Built for Change dismantles shop-worn assumptions of how to meet customer needs; links a new model of employee well-being to company success; demonstrates how technology and sustainability can be part of a business\u2019s twin transformation \u2014 and more. Subscribe to Built for Change, a new podcast from Accenture.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 44,
      "total_episodes": 26,
      "listennotes_url": "https://www.listennotes.com/c/10904b22ae9a4311b2060002562b94aa/",
      "audio_length_sec": 1592,
      "explicit_content": false,
      "latest_episode_id": "841cc001e8f04724a35df4809ba60709",
      "latest_pub_date_ms": 1680681600000,
      "earliest_pub_date_ms": 1617375600024,
      "update_frequency_hours": 638,
      "listen_score_global_rank": "1%"
    },
    {
      "id": "f9f8aa526f1e498286f205d66cf9e524",
      "rss": "https://feeds.simplecast.com/82FI35Px",
      "type": "episodic",
      "email": "ezrakleinshow@nytimes.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5zaW1wbGVjYXN0LmNvbS84MkZJMzVQeA==",
        "spotify_url": "https://open.spotify.com/show/3oB5noYIwEB2dMAREj2F7S",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "ezraklein",
        "facebook_handle": "",
        "amazon_music_url": "https://music.amazon.com/podcasts/c4a3b1da-5433-49e6-8c14-0e1da53be78c/the-ezra-klein-show",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-ezra-klein-show-new-york-times-opinion-wo89m7aPWxu-uirbhjX_SZ9.1400x1400.jpg",
      "title": "The Ezra Klein Show",
      "country": "United States",
      "website": "https://www.nytimes.com/ezra-klein-podcast?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        99,
        122,
        67
      ],
      "itunes_id": 1548604447,
      "publisher": "New York Times Opinion",
      "thumbnail": "https://production.listennotes.com/podcasts/the-ezra-klein-show-new-york-times-opinion-TqWs8-_zMvn-uirbhjX_SZ9.300x300.jpg",
      "is_claimed": false,
      "description": "*** Named a best podcast of 2021 by Time, Vulture, Esquire and The Atlantic. ***\nEach Tuesday and Friday, Ezra Klein invites you into a conversation on something that matters. How do we address climate change if the political system fails to act? Has the logic of markets infiltrated too many aspects of our lives? What is the future of the Republican Party? What do psychedelics teach us about consciousness? What does sci-fi understand about our present that we miss? Can our food system be just to humans and animals alike?",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 71,
      "total_episodes": 225,
      "listennotes_url": "https://www.listennotes.com/c/f9f8aa526f1e498286f205d66cf9e524/",
      "audio_length_sec": 4098,
      "explicit_content": false,
      "latest_episode_id": "f99392010b964a7fa3ff931d3c9a2bb4",
      "latest_pub_date_ms": 1681462800000,
      "earliest_pub_date_ms": 1610502169195,
      "update_frequency_hours": 76,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "c3c933b6d22d4a06b236e5493b4603cc",
      "rss": "https://feeds.simplecast.com/l2i9YnTd",
      "type": "episodic",
      "email": "hardfork@nytimes.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5zaW1wbGVjYXN0LmNvbS9sMmk5WW5UZA==",
        "spotify_url": "https://open.spotify.com/show/44fllCS2FTFr2x2kjP9xeT",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/hard-fork-the-new-york-times-vEr0edDkOFp-M2AZCUFvHzY.1400x1400.jpg",
      "title": "Hard Fork",
      "country": "United States",
      "website": "https://www.nytimes.com/column/hard-fork?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        122,
        67,
        127
      ],
      "itunes_id": 1528594034,
      "publisher": "The New York Times",
      "thumbnail": "https://production.listennotes.com/podcasts/hard-fork-the-new-york-times-mwetHTuP2Az-M2AZCUFvHzY.300x300.jpg",
      "is_claimed": false,
      "description": "\u201cHard Fork\u201d is a show about the future that\u2019s already here. Each week, journalists Kevin Roose and Casey Newton explore and make sense of the latest in the rapidly changing world of tech.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 66,
      "total_episodes": 223,
      "listennotes_url": "https://www.listennotes.com/c/c3c933b6d22d4a06b236e5493b4603cc/",
      "audio_length_sec": 2329,
      "explicit_content": false,
      "latest_episode_id": "0a06b69ce15f4312b9639d475dc068c6",
      "latest_pub_date_ms": 1681462800000,
      "earliest_pub_date_ms": 1599624000194,
      "update_frequency_hours": 159,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "5437a383b2e74bc195ba6adde2e996eb",
      "rss": "https://feeds.simplecast.com/wHqls8d1",
      "type": "serial",
      "email": "serialshows@nytimes.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "",
        "spotify_url": "https://open.spotify.com/show/0Z4uNINH9BXtmGpuf7DkQL",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-coldest-case-in-laramie-b5SykAzGiCK-gQWy-5mrHO_.1400x1400.jpg",
      "title": "The Coldest Case In Laramie",
      "country": "United States",
      "website": "https://the-coldest-case-in-laramie.simplecast.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        122,
        99,
        135,
        67
      ],
      "itunes_id": 1664273280,
      "publisher": "Serial Productions & The New York Times",
      "thumbnail": "https://production.listennotes.com/podcasts/the-coldest-case-in-laramie-2XEkKJlzTsb-gQWy-5mrHO_.300x300.jpg",
      "is_claimed": false,
      "description": "Kim Barker, a Pulitzer Prize-winning investigative reporter for The New York Times, revisits an unsolved murder that took place while she was in high school in Laramie, Wyoming, nearly 40 years ago. She confronts the conflicting stories people have told themselves about the crime because of an unexpected development: the arrest of a former Laramie police officer accused in the murder.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 62,
      "total_episodes": 9,
      "listennotes_url": "https://www.listennotes.com/c/5437a383b2e74bc195ba6adde2e996eb/",
      "audio_length_sec": 1661,
      "explicit_content": false,
      "latest_episode_id": "fd5110a3747c4e15a365faadb73d89f2",
      "latest_pub_date_ms": 1677148500000,
      "earliest_pub_date_ms": 1676523600000,
      "update_frequency_hours": 0,
      "listen_score_global_rank": "0.1%"
    },
    {
      "id": "ea36396fab7d47a8b6c578decfc81834",
      "rss": "https://feeds.simplecast.com/MssIhx9y",
      "type": "episodic",
      "email": "books@nytimes.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5zaW1wbGVjYXN0LmNvbS9Nc3NJaHg5eQ==",
        "spotify_url": "https://open.spotify.com/show/1q3tsOS9XhqgSslnyZyKV6",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "nytimesbooks",
        "facebook_handle": "",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-book-review-the-new-york-times-K0shf57H1FS-nbG5CgVhJKz.1400x1400.jpg",
      "title": "The Book Review",
      "country": "United States",
      "website": "https://the-book-review.simplecast.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        100,
        122,
        104
      ],
      "itunes_id": 120315179,
      "publisher": "The New York Times",
      "thumbnail": "https://production.listennotes.com/podcasts/the-book-review-the-new-york-times-EmN1vCyg95q-nbG5CgVhJKz.300x300.jpg",
      "is_claimed": false,
      "description": "The world's top authors and critics join host Gilbert Cruz and editors at The New York Times Book Review to talk about the week's top books, what we're reading and what's going on in the literary world.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 66,
      "total_episodes": 439,
      "listennotes_url": "https://www.listennotes.com/c/ea36396fab7d47a8b6c578decfc81834/",
      "audio_length_sec": 3123,
      "explicit_content": false,
      "latest_episode_id": "7db4100d7f5e4d698b3788f2b9aeb8a3",
      "latest_pub_date_ms": 1681501720000,
      "earliest_pub_date_ms": 1418360400434,
      "update_frequency_hours": 189,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "b1091fb5382e4112b0f260b242e22b07",
      "rss": "https://feeds.simplecast.com/2xzUiHxw",
      "type": "episodic",
      "email": "argument@nytimes.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5zaW1wbGVjYXN0LmNvbS8yeHpVaUh4dw==",
        "spotify_url": "https://open.spotify.com/show/6bmhSFLKtApYClEuSH8q42",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/the-argument-new-york-times-opinion-Re_TLX2kCZ5-Xn9BoFDx4ZR.1400x1400.jpg",
      "title": "The Argument",
      "country": "United States",
      "website": "https://www.nytimes.com/the-argument?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        99,
        122,
        216
      ],
      "itunes_id": 1438024613,
      "publisher": "New York Times Opinion",
      "thumbnail": "https://production.listennotes.com/podcasts/the-argument-new-york-times-opinion-zGp5dUt_a14-Xn9BoFDx4ZR.300x300.jpg",
      "is_claimed": false,
      "description": "Strongly-held opinions. Open-minded debates. A weekly ideas show, hosted by Jane Coaston.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 68,
      "total_episodes": 216,
      "listennotes_url": "https://www.listennotes.com/c/b1091fb5382e4112b0f260b242e22b07/",
      "audio_length_sec": 2146,
      "explicit_content": false,
      "latest_episode_id": "64d4ccb89d134f88993d57572d570117",
      "latest_pub_date_ms": 1671012000000,
      "earliest_pub_date_ms": 1538652714213,
      "update_frequency_hours": 167,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "6206f07f04084407864dd8d7885a201c",
      "rss": "https://feeds.simplecast.com/ksGYZ_Z3",
      "type": "episodic",
      "email": "firstperson@nytimes.com",
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
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://production.listennotes.com/podcasts/first-person-xduohs6nrU8-STqd9okE5CJ.1400x1400.jpg",
      "title": "First Person",
      "country": "United States",
      "website": "https://first-person.simplecast.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        122,
        99,
        67
      ],
      "itunes_id": 1624946521,
      "publisher": "New York Times Opinion",
      "thumbnail": "https://production.listennotes.com/podcasts/first-person-PWpaRBEIL1K-STqd9okE5CJ.300x300.jpg",
      "is_claimed": false,
      "description": "Every opinion starts with a story. Intimate conversations about the big ideas shaping our world, hosted by journalist Lulu Garcia-Navarro. From New York Times Opinion.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 52,
      "total_episodes": 33,
      "listennotes_url": "https://www.listennotes.com/c/6206f07f04084407864dd8d7885a201c/",
      "audio_length_sec": 2010,
      "explicit_content": false,
      "latest_episode_id": "7d8ee10cf59c481aba4afebbb02eecfa",
      "latest_pub_date_ms": 1681376400000,
      "earliest_pub_date_ms": 1652882400030,
      "update_frequency_hours": 167,
      "listen_score_global_rank": "0.5%"
    }
  ],
  "page_number": 1,
  "has_previous": false,
  "next_page_number": 2
}
```   
</details>



<details>
  <summary>Click to see response schema</summary>
  
```json
{
  "type": "object",
  "properties": {
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
            "description": "Podcast id, which can be used to further fetch detailed podcast metadata via `GET /podcasts/{id}`."
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
                "example": "https://podcasts.google.com/feed/aHR0cHM6Ly9yc3MuYXJ0MTkuY29tL2pvaG4tc29sb21vbi1yZXBvcnRz",
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
              "amazon_music_url": {
                "type": "string",
                "example": "https://music.amazon.com/podcasts/6fc6d683-9ef3-4850-9c35-8e8b1a42a147/the-lock-sportscast",
                "description": "Amazon Music url for this podcast"
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
          "audio_length_sec": {
            "type": "integer",
            "example": 1291,
            "description": "Average audio length of all episodes of this podcast. In seconds."
          },
          "explicit_content": {
            "type": "boolean",
            "example": false,
            "description": "Whether this podcast contains explicit language."
          },
          "latest_episode_id": {
            "type": "string",
            "example": "d057092e57cc4ced80e0efaa196593d9",
            "description": "The id of the most recently published episode of this podcast, which can be used to further fetch detailed episode metadata via `GET /episodes/{id}`."
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
          "update_frequency_hours": {
            "type": "integer",
            "example": 168,
            "description": "How frequently does this podcast release a new episode? In hours. For example, if the value is 166, then it's every 166 hours (or weekly)."
          },
          "listen_score_global_rank": {
            "type": "string",
            "example": "0.5%",
            "description": "The estimated popularity ranking of a podcast compared to all other rss-based public podcasts in the world.\nFor example, if the value is 0.5%, then this podcast is one of the top 0.5% most popular shows out of all podcasts globally, ranked by Listen Score.\nIf the ranking is not available, it'll be null. Learn more at listennotes.com/listen-score\n"
          }
        }
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



