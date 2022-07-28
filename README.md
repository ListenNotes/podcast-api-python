# Podcast API Python Library

[![Python CI](https://github.com/ListenNotes/podcast-api-python/actions/workflows/python.yml/badge.svg)](https://github.com/ListenNotes/podcast-api-python/actions/workflows/python.yml)

The Podcast API Python library provides convenient access to the [Listen Notes Podcast API](https://www.listennotes.com/podcast-api/) from
applications written in the Python language.

Simple and no-nonsense podcast search & directory API. Search the meta data of all podcasts and episodes by people, places, or topics. It's the same API that powers [the best podcast search engine Listen Notes](https://www.listennotes.com/).

If you have any questions, please contact [hello@listennotes.com](hello@listennotes.com?subject=Questions+about+the+Python+SDK+of+Listen+API)

<a href="https://www.listennotes.com/podcast-api/"><img src="https://raw.githubusercontent.com/ListenNotes/ListenApiDemo/master/web/src/powered_by_listennotes.png" width="300" /></a>


**Table of Contents**
- [Podcast API Python Library](#podcast-api-python-library)
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
    - [Fetch audience demographics for a podcast](#fetch-audience-demographics-for-a-podcast)




## API Reference

Each function is a wrapper to send an HTTP request to the corresponding endpoint on the
[API Docs](https://www.listennotes.com/podcast-api/docs/).



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

See all available parameters on the [API Docs page](https://www.listennotes.com/podcast-api/docs/#get-api-v2-search).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "took": 0.966,
  "count": 10,
  "total": 9278,
  "results": [
    {
      "id": "c877bf360bda4c74adea2ba066df6929",
      "rss": "https://feeds.megaphone.fm/ROOSTER7199250968",
      "link": "https://supercarlinbrothers.libsyn.com/star-wars-theory-the-great-star-wars-ice-cream-conspiracy?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/c877bf360bda4c74adea2ba066df6929/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-Fyq7cYS9NOs-BodDr7iIAR3.1400x1400.jpg",
      "podcast": {
        "id": "8bdbb906eef04e5d8b391e947998e9af",
        "image": "https://cdn-images-1.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-Fyq7cYS9NOs-BodDr7iIAR3.1400x1400.jpg",
        "genre_ids": [
          68,
          214,
          265,
          99
        ],
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-TSfxiBaqOwK-BodDr7iIAR3.300x300.jpg",
        "listen_score": 53,
        "title_original": "Super Carlin Brothers",
        "listennotes_url": "https://www.listennotes.com/c/8bdbb906eef04e5d8b391e947998e9af/",
        "title_highlighted": "Super Carlin Brothers",
        "publisher_original": "J and Ben Carlin",
        "publisher_highlighted": "J and Ben Carlin",
        "listen_score_global_rank": "0.5%"
      },
      "itunes_id": 1479112798,
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-TSfxiBaqOwK-BodDr7iIAR3.300x300.jpg",
      "pub_date_ms": 1574355600262,
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
      "id": "42b1898db6a84973b41879618002937b",
      "rss": "https://thevintagerpgpodcast.libsyn.com/rss",
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
        "listen_score": 47,
        "title_original": "The Vintage RPG Podcast",
        "listennotes_url": "https://www.listennotes.com/c/f3094a0b14684300a3d6b69a1063e708/",
        "title_highlighted": "The Vintage RPG Podcast",
        "publisher_original": "Vintage RPG",
        "publisher_highlighted": "Vintage RPG",
        "listen_score_global_rank": "1%"
      },
      "itunes_id": 1409477830,
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-vintage-rpg-podcast-vintage-rpg-Mg-2ZYcmERT-eq8uGUY6vXN.300x300.jpg",
      "pub_date_ms": 1575867600122,
      "guid_from_rss": "9861105d-bf98-4684-871a-5cbe11484159",
      "title_original": "Star Wars Galaxy Guides",
      "listennotes_url": "https://www.listennotes.com/e/42b1898db6a84973b41879618002937b/",
      "audio_length_sec": 1519,
      "explicit_content": false,
      "title_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Galaxy Guides",
      "description_original": "<p>Because Star Wars is hitting the critical mass point for 2019, we figured we'd add to the fun with an episode that looks at the Galaxy Guides series of sourcebooks for the West End Games Star Wars Role Playing Game. We take a quick tour through each of the twelve volumes and chat about what they added to the RPG experience and how they formed the backbone of the greater Star Wars Expanded Universe.</p> <p style=\"text-align: center;\">* * *</p> <p>If\u00a0 you dig what we do, join us on the <a href=\"https://www.patreon.com/vintagerpg\">Vintage RPG Patreon</a> for more roleplaying fun and surprises! Patrons keep us going!</p> <p>Like, Rate, Subscribe and Review the Vintage RPG Podcast!</p> <p>Send questions, comments or corrections to\u00a0<a href=\"mailto:vintagerpg@unwinnable.com\">info@vintagerpg.com</a>.</p> <p>Follow\u00a0Vintage RPG\u00a0on\u00a0<a href=\"https://www.instagram.com/vintagerpg/\">Instagram</a>,\u00a0<a href=\"https://vintagerpg.tumblr.com/\">Tumblr</a>\u00a0and\u00a0<a href=\"https://www.facebook.com/vintagerpg\">Facebook</a>. Learn more at the\u00a0<a href=\"https://vintagerpg.com/vintage-rpg-faq/\">Vintage RPG FAQ</a>.</p> <p>Follow\u00a0<a href=\"https://twitter.com/StuHorvath\">Stu Horvath</a>,\u00a0<a href=\"https://twitter.com/Hambreaker\">John McGuire</a>,\u00a0<a href=\"https://twitter.com/Vintage_RPG\">VintageRPG</a>\u00a0and\u00a0<a href=\"https://twitter.com/unwinnable\">Unwinnable</a>\u00a0on Twitter.</p> <p>Intro music by\u00a0<a href=\"https://www.deadgowest.com/\">George Collazo</a>.</p> <p>The Vintage RPG illustration is by\u00a0<a href=\"http://www.shaferbrown.com/\">Shafer Brown</a>. Follow\u00a0<a href=\"https://twitter.com/shaferbrown\">him on Twitter</a>.</p> <p>Tune in next week for the next episode. Until then, may the dice always roll in your favor!</p>",
      "description_highlighted": "...Because <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> is hitting the critical mass point for 2019, we figured we'd add to the fun with an episode that looks at the Galaxy Guides series of sourcebooks for the West End Games <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Role...",
      "transcripts_highlighted": []
    },
    {
      "id": "9cfb4901a891449aa30553cddfa582f8",
      "rss": "http://sw7x7.libsyn.com/rss",
      "link": "https://sw7x7.libsyn.com/1945-answering-star-wars-questions-from-star-wars-77-patrons?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/9cfb4901a891449aa30553cddfa582f8/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-HN08OoDE7pc-AIg3cZVKCsL.1400x1400.jpg",
      "podcast": {
        "id": "4d3fe717742d4963a85562e9f84d8c79",
        "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-HN08OoDE7pc-AIg3cZVKCsL.1400x1400.jpg",
        "genre_ids": [
          86,
          68,
          82,
          100,
          101,
          160,
          138
        ],
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-2LryqMj-sGP-AIg3cZVKCsL.300x300.jpg",
        "listen_score": 48,
        "title_original": "Star Wars 7x7: The Daily Star Wars Podcast",
        "listennotes_url": "https://www.listennotes.com/c/4d3fe717742d4963a85562e9f84d8c79/",
        "title_highlighted": "Star Wars 7x7: The Daily Star Wars Podcast",
        "publisher_original": "Star Wars 7x7",
        "publisher_highlighted": "Star Wars 7x7",
        "listen_score_global_rank": "1%"
      },
      "itunes_id": 896354638,
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-2LryqMj-sGP-AIg3cZVKCsL.300x300.jpg",
      "pub_date_ms": 1572505200911,
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
        "listen_score_global_rank": "1%"
      },
      "itunes_id": 1133381225,
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/saturday-night-live-snl-afterparty-john-wm1CtQVkRfy-_iOE4lLZ2pD.300x300.jpg",
      "pub_date_ms": 1576989000066,
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
        "listen_score": 60,
        "title_original": "Marvel Cinematic Universe Podcast",
        "listennotes_url": "https://www.listennotes.com/c/593c42e343ba44e7b6f8634a946f0b52/",
        "title_highlighted": "Marvel Cinematic Universe Podcast",
        "publisher_original": "Stranded Panda",
        "publisher_highlighted": "Stranded Panda",
        "listen_score_global_rank": "0.5%"
      },
      "itunes_id": 907175322,
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/marvel-cinematic-universe-podcast-wVDeHrdxZJh-aXR7VuG2z4p.300x300.jpg",
      "pub_date_ms": 1575521386284,
      "guid_from_rss": "https://api.spreaker.com/episode/20495415",
      "title_original": "Star Wars is better than Star Trek",
      "listennotes_url": "https://www.listennotes.com/e/39746ccfc0d64f62aea8e96641366109/",
      "audio_length_sec": 734,
      "explicit_content": false,
      "title_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> is better than <span class=\"ln-search-highlight\">Star</span> Trek",
      "description_original": "A just for fun episode.  Time to punish Matt for his sins against baby yoda",
      "description_highlighted": "...A just for fun episode.  Time to punish Matt for his sins against baby yoda...",
      "transcripts_highlighted": []
    },
    {
      "id": "f13d8c2343e748858464167b426fe67b",
      "rss": "https://feeds.megaphone.fm/ROOSTER7199250968",
      "link": "https://supercarlinbrothers.libsyn.com/star-wars-theory-the-white-saber-theory?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/f13d8c2343e748858464167b426fe67b/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-Fyq7cYS9NOs-BodDr7iIAR3.1400x1400.jpg",
      "podcast": {
        "id": "8bdbb906eef04e5d8b391e947998e9af",
        "image": "https://cdn-images-1.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-Fyq7cYS9NOs-BodDr7iIAR3.1400x1400.jpg",
        "genre_ids": [
          68,
          214,
          265,
          99
        ],
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-TSfxiBaqOwK-BodDr7iIAR3.300x300.jpg",
        "listen_score": 53,
        "title_original": "Super Carlin Brothers",
        "listennotes_url": "https://www.listennotes.com/c/8bdbb906eef04e5d8b391e947998e9af/",
        "title_highlighted": "Super Carlin Brothers",
        "publisher_original": "J and Ben Carlin",
        "publisher_highlighted": "J and Ben Carlin",
        "listen_score_global_rank": "0.5%"
      },
      "itunes_id": 1479112798,
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-TSfxiBaqOwK-BodDr7iIAR3.300x300.jpg",
      "pub_date_ms": 1576602000255,
      "guid_from_rss": "1a2b9678-7879-4480-94c7-afa1493e9ef9",
      "title_original": "Star Wars Theory: The White Saber Theory",
      "listennotes_url": "https://www.listennotes.com/e/f13d8c2343e748858464167b426fe67b/",
      "audio_length_sec": 807,
      "explicit_content": false,
      "title_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Theory: The White Saber Theory",
      "description_original": "<p>With Star Wars Episode 9 The Rise of Skywalker just days away J dives into the Star Wars Galaxy to discuss the future of Kylo Ren\u2019s Lightsaber and the White Saber theory!</p>",
      "description_highlighted": "...With <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Episode 9 The Rise of Skywalker just days away J dives into the <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Galaxy to discuss the future of Kylo Ren\u2019s Lightsaber and the White Saber theory!...",
      "transcripts_highlighted": []
    },
    {
      "id": "ea09b575d07341599d8d5b71f205517b",
      "rss": "https://theroughcut.libsyn.com/rss",
      "link": "http://theroughcutpod.com/?p=786&utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/ea09b575d07341599d8d5b71f205517b/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-rough-cut-matt-feury-YMha8DxnUbc-53MLh7NpAwm.1400x1400.jpg",
      "podcast": {
        "id": "8758da9be6c8452884a8cab6373b007c",
        "image": "https://cdn-images-1.listennotes.com/podcasts/the-rough-cut-matt-feury-YMha8DxnUbc-53MLh7NpAwm.1400x1400.jpg",
        "genre_ids": [
          68,
          264
        ],
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-rough-cut-matt-feury-DEkF_8ybj6A-53MLh7NpAwm.300x300.jpg",
        "listen_score": 39,
        "title_original": "The Rough Cut",
        "listennotes_url": "https://www.listennotes.com/c/8758da9be6c8452884a8cab6373b007c/",
        "title_highlighted": "The Rough Cut",
        "publisher_original": "Matt Feury",
        "publisher_highlighted": "Matt Feury",
        "listen_score_global_rank": "2%"
      },
      "itunes_id": 1471556007,
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-rough-cut-matt-feury-DEkF_8ybj6A-53MLh7NpAwm.300x300.jpg",
      "pub_date_ms": 1579507216132,
      "guid_from_rss": "004f03c8-cdf9-4ff5-9d89-b2147f8d55cf",
      "title_original": "Star Wars - The Force Awakens",
      "listennotes_url": "https://www.listennotes.com/e/ea09b575d07341599d8d5b71f205517b/",
      "audio_length_sec": 1694,
      "explicit_content": false,
      "title_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> - The Force Awakens",
      "description_original": "<p>In this episode of The Rough Cut we close out our study of the final Skywalker trilogy with a look back on the film that helped the dormant franchise make the jump to lightspeed, <a href=\"https://www.imdb.com/title/tt2488496/\">Episode VII - The Force Awakens</a>.\u00a0 Recorded in Amsterdam in front of a festival audience in 2018, editor <a href=\"https://www.imdb.com/name/nm0104783/?ref_=nv_sr_srsg_0\">Maryann Brandon ACE</a> recounts her work on <em>The Force Awakens</em> just as she was about to begin editing what would come to be known as <a href=\"https://www.imdb.com/title/tt2527338/?ref_=nm_flmg_edt_1\">Episode IX - The Rise of Skywalker</a>.</p> <p>\u00a0</p> <p>Go back to the beginning and listen to our <a href=\"http://theroughcutpod.com/paul-hirsch/\">podcast with Star Wars and 'Empire' editor, Paul Hirsch</a>.</p> <p>Hear editor Bob Ducsay talk about cutting <a href=\"http://theroughcutpod.com/last-jedi/\">The Last Jedi</a>.</p> <p>Listen to Maryann Brandon talk about her work on <a href=\"http://theroughcutpod.com/star-wars/\">The Rise of Skywalker</a>.</p> <p>Get your hands on the non-linear editor behind the latest Skywalker trilogy,\u00a0 <a href=\"https://www.avid.com/video-editor-right-for-you\">Avid Media Composer!</a></p> <p><a href=\"http://theroughcutpod.com/subscribe/\">Subscribe to The Rough Cut</a> for more great interviews with the heroes of the editing room!</p> <p>\u00a0</p> <p>\u00a0</p>",
      "description_highlighted": "...Go back to the beginning and listen to our podcast with <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> and 'Empire' editor, Paul Hirsch. Hear editor Bob Ducsay talk about cutting The Last Jedi....",
      "transcripts_highlighted": []
    },
    {
      "id": "de8677b8ccfb4eddbf457242050f9d43",
      "rss": "http://sw7x7.libsyn.com/rss",
      "link": "https://sw7x7.libsyn.com/1973-expressions-of-gratitude-in-star-wars?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/de8677b8ccfb4eddbf457242050f9d43/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-HN08OoDE7pc-AIg3cZVKCsL.1400x1400.jpg",
      "podcast": {
        "id": "4d3fe717742d4963a85562e9f84d8c79",
        "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-HN08OoDE7pc-AIg3cZVKCsL.1400x1400.jpg",
        "genre_ids": [
          86,
          68,
          82,
          100,
          101,
          160,
          138
        ],
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-2LryqMj-sGP-AIg3cZVKCsL.300x300.jpg",
        "listen_score": 48,
        "title_original": "Star Wars 7x7: The Daily Star Wars Podcast",
        "listennotes_url": "https://www.listennotes.com/c/4d3fe717742d4963a85562e9f84d8c79/",
        "title_highlighted": "Star Wars 7x7: The Daily Star Wars Podcast",
        "publisher_original": "Star Wars 7x7",
        "publisher_highlighted": "Star Wars 7x7",
        "listen_score_global_rank": "1%"
      },
      "itunes_id": 896354638,
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-2LryqMj-sGP-AIg3cZVKCsL.300x300.jpg",
      "pub_date_ms": 1574928000883,
      "guid_from_rss": "cfc0c931-354d-4752-aa59-a27dcfeffc81",
      "title_original": "1,973. Expressions of Gratitude in Star Wars",
      "listennotes_url": "https://www.listennotes.com/e/de8677b8ccfb4eddbf457242050f9d43/",
      "audio_length_sec": 709,
      "explicit_content": false,
      "title_highlighted": "Expressions of Gratitude in <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span>",
      "description_original": "<p>There are pages of things online about people grateful *for* Star Wars, but nothing I could find about expressions of gratitude *within* Star Wars movies. And so on this Thanksgiving Day in the US, I'm looking at which era of Star Wars movies is the most grateful, which movies have the most expressions of thanks, which ones are the most heartbreaking, and which one is the most touching. Punch it!</p> <p>***I'm listener supported! Join the community at http://Patreon.com/sw7x7 to get access to bonus episodes and other insider rewards.***\u00a0</p>",
      "description_highlighted": "...There are pages of things online about people grateful *for* <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span>, but nothing I could find about expressions of gratitude *within* <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> movies....",
      "transcripts_highlighted": []
    },
    {
      "id": "a34693ebf8b04a64b448208281965298",
      "rss": "https://feeds.megaphone.fm/ROOSTER7199250968",
      "link": "https://supercarlinbrothers.libsyn.com/star-wars-theory-was-han-solo-force-sensitive?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/a34693ebf8b04a64b448208281965298/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-Fyq7cYS9NOs-BodDr7iIAR3.1400x1400.jpg",
      "podcast": {
        "id": "8bdbb906eef04e5d8b391e947998e9af",
        "image": "https://cdn-images-1.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-Fyq7cYS9NOs-BodDr7iIAR3.1400x1400.jpg",
        "genre_ids": [
          68,
          214,
          265,
          99
        ],
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-TSfxiBaqOwK-BodDr7iIAR3.300x300.jpg",
        "listen_score": 53,
        "title_original": "Super Carlin Brothers",
        "listennotes_url": "https://www.listennotes.com/c/8bdbb906eef04e5d8b391e947998e9af/",
        "title_highlighted": "Super Carlin Brothers",
        "publisher_original": "J and Ben Carlin",
        "publisher_highlighted": "J and Ben Carlin",
        "listen_score_global_rank": "0.5%"
      },
      "itunes_id": 1479112798,
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-TSfxiBaqOwK-BodDr7iIAR3.300x300.jpg",
      "pub_date_ms": 1575997200257,
      "guid_from_rss": "a3f1ff19-7ce1-4069-8efe-ae7727fb0b98",
      "title_original": "Star Wars Theory: Was Han Solo Force Sensitive?",
      "listennotes_url": "https://www.listennotes.com/e/a34693ebf8b04a64b448208281965298/",
      "audio_length_sec": 900,
      "explicit_content": false,
      "title_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Theory: Was Han Solo Force Sensitive?",
      "description_original": "<p>Today J dives into the Star Wars Galaxy to try and answer an age old question: Could Han Solo use The Force? We meet Han Solo as a somewhat overconfident pilot who seems to make his way through the galaxy thanks to his charm, a bit of wit, and a lot of luck. But today we examine whether or not all of that luck behind Han\u2019s success is simply luck OR is it something else?!</p>",
      "description_highlighted": "...Today J dives into the <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Galaxy to try and answer an age old question: Could Han Solo use The Force?...",
      "transcripts_highlighted": []
    },
    {
      "id": "8d6fdee228dc452bbfc422af1ced5e68",
      "rss": "https://feeds.megaphone.fm/ROOSTER7199250968",
      "link": "https://traffic.libsyn.com/secure/supercarlinbrothers/Lil_Yoda.mp3?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/8d6fdee228dc452bbfc422af1ced5e68/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-Fyq7cYS9NOs-BodDr7iIAR3.1400x1400.jpg",
      "podcast": {
        "id": "8bdbb906eef04e5d8b391e947998e9af",
        "image": "https://cdn-images-1.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-Fyq7cYS9NOs-BodDr7iIAR3.1400x1400.jpg",
        "genre_ids": [
          68,
          214,
          265,
          99
        ],
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-TSfxiBaqOwK-BodDr7iIAR3.300x300.jpg",
        "listen_score": 53,
        "title_original": "Super Carlin Brothers",
        "listennotes_url": "https://www.listennotes.com/c/8bdbb906eef04e5d8b391e947998e9af/",
        "title_highlighted": "Super Carlin Brothers",
        "publisher_original": "J and Ben Carlin",
        "publisher_highlighted": "J and Ben Carlin",
        "listen_score_global_rank": "0.5%"
      },
      "itunes_id": 1479112798,
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/super-carlin-brothers-j-and-ben-carlin-TSfxiBaqOwK-BodDr7iIAR3.300x300.jpg",
      "pub_date_ms": 1574365061261,
      "guid_from_rss": "095b0add-db46-452b-af45-4bd1eed34bdd",
      "title_original": "Star Wars Theory: Where Does Yoda Come From!?",
      "listennotes_url": "https://www.listennotes.com/e/8d6fdee228dc452bbfc422af1ced5e68/",
      "audio_length_sec": 794,
      "explicit_content": false,
      "title_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Theory: Where Does Yoda Come From!?",
      "description_original": "<p>The Mandalorian has introduced us to an ADORABLE tiny little Yoda creature. We keep calling it a \"Yoda Creature\" because despite the vast Star Wars expanded universe... Yoda's species has intentionally remained a mystery. Today we dive in to find out more!\u00a0</p>",
      "description_highlighted": "...We keep calling it a \"Yoda Creature\" because despite the vast <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> expanded universe... Yoda's species has intentionally remained a mystery. Today we dive in to find out more!\u00a0...",
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

See all available parameters on the [API Docs page](https://www.listennotes.com/podcast-api/docs/#get-api-v2-typeahead).


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
      "image": "https://cdn-images-1.listennotes.com/podcasts/rebel-force-radio-star-wars-podcast-star-wars-GSQTPOZCqAx-4v5pRaEg1Ub.1400x1400.jpg",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/rebel-force-radio-star-wars-podcast-star-wars-Na1ogntxKO_-4v5pRaEg1Ub.300x300.jpg",
      "title_original": "Rebel Force Radio: Star Wars Podcast",
      "explicit_content": false,
      "title_highlighted": "Rebel Force Radio: <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Podcast",
      "publisher_original": "Star Wars",
      "publisher_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span>"
    },
    {
      "id": "8e90b8f0c9eb4c11b13f9dc331ed747c",
      "image": "https://cdn-images-1.listennotes.com/podcasts/inside-star-wars-wondery-F8ZBEqObITM-e8ydUYnAOJv.1400x1400.jpg",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/inside-star-wars-wondery-2Ep_n06B8ad-e8ydUYnAOJv.300x300.jpg",
      "title_original": "Inside Star Wars",
      "explicit_content": false,
      "title_highlighted": "Inside <span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span>",
      "publisher_original": "Wondery",
      "publisher_highlighted": "Wondery"
    },
    {
      "id": "46c50b17a1c6474fb77e21f438ccd78d",
      "image": "https://cdn-images-1.listennotes.com/podcasts/skytalkers-charlotte-caitlin-star-wars-S7L8tE_nIaZ--hNC10LzS4A.1400x1400.jpg",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/skytalkers-charlotte-caitlin-star-wars-DEIoXLeJOM9--hNC10LzS4A.300x300.jpg",
      "title_original": "Skytalkers",
      "explicit_content": false,
      "title_highlighted": "Skytalkers",
      "publisher_original": "Star Wars",
      "publisher_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span>"
    },
    {
      "id": "ff1938a1747c4698976943bf5f685600",
      "image": "https://cdn-images-1.listennotes.com/podcasts/children-of-the-watch-obi-wan-kenobi-star-rpmeRxzvJhQ-lt7yMQIx2fP.567x567.jpg",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/children-of-the-watch-obi-wan-kenobi-star-rzWamMJkKOi-lt7yMQIx2fP.300x300.jpg",
      "title_original": "Children of the Watch: Obi-Wan Kenobi",
      "explicit_content": false,
      "title_highlighted": "Children of the Watch: Obi-Wan Kenobi",
      "publisher_original": "Star Wars",
      "publisher_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span>"
    },
    {
      "id": "912f36444ea6475693ab3ab899cc3782",
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-theory-jigowatt-media-glassbox-ejn-hv_OCqw-FGYt8XM-sIK.1400x1400.jpg",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-theory-jigowatt-media-glassbox-xMb5E7DvAYj-FGYt8XM-sIK.300x300.jpg",
      "title_original": "Star Wars Theory",
      "explicit_content": false,
      "title_highlighted": "<span class=\"ln-search-highlight\">Star</span> <span class=\"ln-search-highlight\">Wars</span> Theory",
      "publisher_original": "Jigowatt Media & Glassbox Media ",
      "publisher_highlighted": "Jigowatt Media & Glassbox Media "
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

See all available parameters on the [API Docs page](https://www.listennotes.com/podcast-api/docs/#get-api-v2-podcasts-id).


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
  "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the-daily-star-wars-podcast-HN08OoDE7pc-AIg3cZVKCsL.1400x1400.jpg",
  "title": "Star Wars 7x7: The Daily Star Wars Podcast",
  "country": "United States",
  "website": "https://sw7x7.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
  "episodes": [
    {
      "id": "4e7c59e10e4640b98f2f3cb1777dbb43",
      "link": "https://sw7x7.libsyn.com/864-part-2-of-my-new-conversation-with-bobby-roberts?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/4e7c59e10e4640b98f2f3cb1777dbb43/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the/864-part-2-of-my-new--vDBMTjY_mK-2WVsxtU0f3m.600x315.jpg",
      "title": "864: Part 2 of My (New) Conversation With Bobby Roberts",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the/864-part-2-of-my-new-yqjrzNDEXaS-2WVsxtU0f3m.300x157.jpg",
      "description": "<p>The second half of my latest conversation with Bobby Roberts, Podcast Emeritus from Full of Sith and now Star Wars \"Podcast Force Ghost at Large.\" Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1479110401853,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the/863-a-new-conversation-with-e_vHo9SM7ft-0YRBTlgiVeU.600x315.jpg",
      "title": "863: A (New) Conversation With Bobby Roberts, Part 1",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the/863-a-new-conversation-with-lcQsDS5uvYb-0YRBTlgiVeU.300x157.jpg",
      "description": "<p>An in-depth conversation about the Star Wars \"Story\" movies and so much more, featuring Bobby Roberts, Star Wars \"Podcast Force Ghost at Large.\" Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1479024001854,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the/862-assassin-clone-wars-lP94b2q5iOz-jEcMAdTntzs.600x315.jpg",
      "title": "862: \"Assassin\" - Clone Wars Briefing, Season 3, Episode 7",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the/862-assassin-clone-wars-Uh3E0GwOQRX-jEcMAdTntzs.300x157.jpg",
      "description": "<p>The beginnings of the true power of the Force, revealed in \"Assassin,\" season 3, episode 7 of the Star Wars: The Clone Wars cartoon series. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478937601855,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the/861-rogue-one-international-6rZOEiJHPpx-nGxaRC95V6o.600x315.jpg",
      "title": "861: Rogue One International Trailer Breakdown",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the/861-rogue-one-international-AFlEBXPHG6d-nGxaRC95V6o.300x157.jpg",
      "description": "<p>Surprise! An international trailer for Rogue One has dropped, and it includes new scenes, new dialogue, and some heavy foreshadowing about Jyn Erso's fate. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478851457856,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the/860-will-jyn-and-cassian-VHAJQ1N57hE-l_3qXNfHAU0.600x315.jpg",
      "title": "860: Will Jyn and Cassian Survive Rogue One?",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the/860-will-jyn-and-cassian-k-2Si6HYjTP-l_3qXNfHAU0.300x157.jpg",
      "description": "<p>Today I conclude a two-episode set looking at the odds of survival for major Rogue One characters. Today: Jyn Erso, Cassian Andor, Bodhi Rook, and K-2SO. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478764801857,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the/859-the-odds-who-will-nM7l1BNPbIa-kprAXUCS8uQ.600x315.jpg",
      "title": "859: The Odds: Who Will Survive Rogue One?",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the/859-the-odds-who-will-RlXojiI5Wm6-kprAXUCS8uQ.300x157.jpg",
      "description": "<p>Will Galen Erso, Lyra Erso, Saw Gerrera, and Orson Krennic survive the events of Rogue One: A Star Wars Story? Starting a mini-series to look at the odds... Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478678401858,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the/858-together-new-rogue-one-TsLghBq5enX-WpFSsNUOzcL.600x315.jpg",
      "title": "858: \"Together\" - New Rogue One Commercial Dialogue",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the/858-together-new-rogue-one-dJF6XLmfYl4-WpFSsNUOzcL.300x157.jpg",
      "description": "<p>A new Rogue One commercial dropped Sunday, with some new dialogue that hints at the relationship between Jyn Erso, Saw Gerrera, the Rebellion, and the Partisans. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478592001859,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the/857-imperial-supercommandos-d0c7L1grbaI-L6bAOKCmyqt.600x315.jpg",
      "title": "857: \"Imperial Supercommandos\" - Star Wars Rebels Season 3, Episode 7",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the/857-imperial-supercommandos-OFpdNki02M_-L6bAOKCmyqt.300x157.jpg",
      "description": "<p>\"Imperial Supercommandos\" is Season 3, episode 7 of Star Wars Rebels, referring to Mandalorians serving the Empire. But can Fenn Rau be trusted, either? Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478505601860,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the/856-the-academy-clone-wars-6-EXfkbp4Sz-l6QpC-2RDTH.600x315.jpg",
      "title": "856: \"The Academy\" - Clone Wars Briefing, Season 3, Episode 6",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the/856-the-academy-clone-wars-x6_sqVGe-KS-l6QpC-2RDTH.300x157.jpg",
      "description": "<p>\"The Academy,\" Season 3 Episode 6 of the Clone Wars cartoon series, is a quieter episode that highlights the importance of Mandalore to the Star Wars franchise. Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478415601861,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the/855-episode-viii-and-han-3Wkgr82DBxf-9vz38ko_X2s.600x315.jpg",
      "title": "855: Episode VIII and Han Solo Movie Updates",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/star-wars-7x7-the/855-episode-viii-and-han-naM8NWQxR19-9vz38ko_X2s.300x157.jpg",
      "description": "<p>Daisy Ridley says wait for Episode VIII for answers about Rey's parents. Bradford Young says the Han Solo movie won't be what you expect. Updates here... Punch it!</p> <p>***We\u2019re listener supported! Go to http://Patreon.com/sw7x7 to donate to the Star Wars 7x7 podcast, and you\u2019ll get some fabulous rewards for your pledge.***\u00a0</p> <p>Check out SW7x7.com for full Star Wars 7x7 show notes and links, and to comment on any of the content of this episode! If you like what you've heard, please leave us a rating or review on iTunes or Stitcher, which will also help more people discover this Star Wars podcast.</p> <p>Don't forget to join the Star Wars 7x7 fun on Facebook at Facebook.com/SW7x7, and follow the breaking news Twitter feed at Twitter.com/SW7x7Podcast. We're also on Pinterest and Instagram as \"SW7x7\" too, and we'd love to connect with you there!</p>",
      "pub_date_ms": 1478329201862,
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
  "total_episodes": 3006,
  "listennotes_url": "https://www.listennotes.com/c/4d3fe717742d4963a85562e9f84d8c79/",
  "audio_length_sec": 597,
  "explicit_content": false,
  "latest_episode_id": "67f706d176fe490086d544b4266b9856",
  "latest_pub_date_ms": 1658905200000,
  "earliest_pub_date_ms": 1404637200000,
  "next_episode_pub_date": 1478329201862,
  "update_frequency_hours": 24,
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

See all available parameters on the [API Docs page](https://www.listennotes.com/podcast-api/docs/#get-api-v2-episodes-id).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "id": "6b6d65930c5a4f71b254465871fed370",
  "link": "https://audioboom.com/posts/7742178?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
  "audio": "https://www.listennotes.com/e/p/6b6d65930c5a4f71b254465871fed370/",
  "image": "https://cdn-images-1.listennotes.com/podcasts/a-winning-mindset/16-arly-velasquez-on-xPbM1hpZqFK-c5khPVKzowB.1400x1400.jpg",
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
    "image": "https://cdn-images-1.listennotes.com/podcasts/a-winning-mindset-a-winning-mindset-lessons-f06IOp3gkZq-BktA4YUzNbu.1400x1400.jpg",
    "title": "A Winning Mindset",
    "country": "Germany",
    "website": "https://www.paralympic.org/a-winning-mindset-lessons-from-the-paralympics?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
    "language": "English",
    "genre_ids": [
      124,
      122,
      67,
      111,
      77,
      181,
      78,
      217,
      88,
      191,
      90
    ],
    "itunes_id": 1527733477,
    "publisher": "A Winning Mindset: Lessons From The Paralympics",
    "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/a-winning-mindset-a-winning-mindset-lessons-DHlfCBAqXh6-BktA4YUzNbu.300x300.jpg",
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
  "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/a-winning-mindset/16-arly-velasquez-on-ftCxqnUg0Sr-c5khPVKzowB.300x300.jpg",
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

See all available parameters on the [API Docs page](https://www.listennotes.com/podcast-api/docs/#get-api-v2-languages).


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

See all available parameters on the [API Docs page](https://www.listennotes.com/podcast-api/docs/#get-api-v2-genres).


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
      "id": 127,
      "name": "Technology",
      "parent_id": 67
    },
    {
      "id": 168,
      "name": "Fiction",
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
      "id": 122,
      "name": "Society & Culture",
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
      "id": 100,
      "name": "Arts",
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

See all available parameters on the [API Docs page](https://www.listennotes.com/podcast-api/docs/#get-api-v2-best_podcasts).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "id": 93,
  "name": "Business",
  "total": 705,
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
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/startup-podcast-gimlet-14zU0c_MOmv-n9PpCBTQvoJ.1400x1400.jpg",
      "title": "StartUp Podcast",
      "country": "United States",
      "website": "https://www.gimletmedia.com/startup?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        171,
        67,
        93,
        127,
        68,
        97,
        94,
        157
      ],
      "itunes_id": 913805339,
      "publisher": "Gimlet",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/startup-podcast-gimlet-8If7QBKU5jb-n9PpCBTQvoJ.300x300.jpg",
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
      "audio_length_sec": 2176,
      "explicit_content": false,
      "latest_episode_id": "3663e1ba8f944df7956378ab332bf12b",
      "latest_pub_date_ms": 1598004000000,
      "earliest_pub_date_ms": 1396742400151,
      "update_frequency_hours": 253,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/worklife-with-adam-grant-ted-KgaXjFPEoVc.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/worklife-with-adam-grant-ted-KgaXjFPEoVc.300x300.jpg",
      "is_claimed": false,
      "description": "\n      <p>You spend a quarter of your life at work. You should enjoy it! Organizational psychologist Adam Grant takes you inside the minds of some of the world\u2019s most unusual professionals to discover the keys to a better work life. From learning how to love your rivals to harnessing the power of frustration, one thing\u2019s for sure: You\u2019ll never see your job the same way again. Produced in partnership with Transmitter Media.</p>\n    ",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 76,
      "total_episodes": 75,
      "listennotes_url": "https://www.listennotes.com/c/34beae8ad8fd4b299196f413b8270a30/",
      "audio_length_sec": 2331,
      "explicit_content": false,
      "latest_episode_id": "e0ec782e61224c55bb79800ac62781f9",
      "latest_pub_date_ms": 1656388800000,
      "earliest_pub_date_ms": 1518044524074,
      "update_frequency_hours": 167,
      "listen_score_global_rank": "0.01%"
    },
    {
      "id": "ee84d7d11875465fb89487675ff5425d",
      "rss": "https://feeds.simplecast.com/J2ZDFXoI",
      "type": "episodic",
      "email": "edwardmylett@yahoo.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5zaW1wbGVjYXN0LmNvbS9KMlpERlhvSQ==",
        "spotify_url": "https://open.spotify.com/show/19TdDBlFkqh7uevYO0jFSW",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "EdMylett",
        "facebook_handle": "",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-ed-mylett-show-ed-mylett-lguQyVETCI8-PEUIT9RBhZD.1400x1400.jpg",
      "title": "THE ED MYLETT SHOW",
      "country": "United States",
      "website": "https://the-ed-mylett-show.simplecast.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-ed-mylett-show-ed-mylett-sM8Scyi-YQr-PEUIT9RBhZD.300x300.jpg",
      "is_claimed": false,
      "description": "The Ed Mylett Show showcases the greatest peak-performers across all industries in one place, sharing their journey, knowledge and thought leadership. With Ed Mylett and featured guests in almost every industry including business, health, collegiate and professional sports, politics, entrepreneurship, science, and entertainment, you'll find motivation, inspiration and practical steps to help you become the best version of you!",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 75,
      "total_episodes": 249,
      "listennotes_url": "https://www.listennotes.com/c/ee84d7d11875465fb89487675ff5425d/",
      "audio_length_sec": 3081,
      "explicit_content": false,
      "latest_episode_id": "050da2b3ac704f01895e502884179729",
      "latest_pub_date_ms": 1658829600000,
      "earliest_pub_date_ms": 1480363465242,
      "update_frequency_hours": 163,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-indicator-from-planet-money-npr-uFAcdQm6ILr-G2EDjFO-TLA.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-indicator-from-planet-money-npr-67Cryeo5VYn-G2EDjFO-TLA.300x300.jpg",
      "is_claimed": false,
      "description": "A little show about big ideas. From the people who make <em>Planet Money</em>, <em>The Indicator</em> helps you make sense of what's happening today. It's a quick hit of insight into work, business, the economy, and everything else. Listen weekday afternoons.<br /><br /><em>Got money on your mind? Try Planet Money+ \u2014 a new way to support the show you love, get a sponsor-free feed of the podcast, *and* get access to bonus content. A subscription also gets you access to The Indicator and Planet Money Summer School, both without interruptions. </em>",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 75,
      "total_episodes": 1050,
      "listennotes_url": "https://www.listennotes.com/c/5f237b79824e4dfb8355f6dff9b1c542/",
      "audio_length_sec": 576,
      "explicit_content": false,
      "latest_episode_id": "bb68d631601d4bfbbd8148d37a80bbdd",
      "latest_pub_date_ms": 1658971503000,
      "earliest_pub_date_ms": 1527108300299,
      "update_frequency_hours": 28,
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
        "youtube_url": "https://www.youtube.com/user/LifeChurchtv",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "lifechurch",
        "facebook_handle": "life.church",
        "amazon_music_url": "",
        "instagram_handle": "life.church"
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/craig-groeschel-leadership-podcast-lifechurch--_K8zgsM0x1-dy-uJsHC_9T.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/craig-groeschel-leadership-podcast-lifechurch-OU5cY0mgjsb-dy-uJsHC_9T.300x300.jpg",
      "is_claimed": false,
      "description": "The Craig Groeschel Leadership Podcast offers personal, practical coaching lessons that take the mystery out of leadership. In each episode of the Craig Groeschel Leadership Podcast, Craig brings you empowering insights and easy-to-understand takeaways you can use to lead yourself and lead your team. You\u2019ll learn effective ways to grow as a leader, optimize your time, develop your team, and structure your organization.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 74,
      "total_episodes": 113,
      "listennotes_url": "https://www.listennotes.com/c/2184bada602d431689dbb4c6c1bc5839/",
      "audio_length_sec": 1667,
      "explicit_content": false,
      "latest_episode_id": "30ba73f39830427ca2458ae14aea6486",
      "latest_pub_date_ms": 1657188000000,
      "earliest_pub_date_ms": 1452675180111,
      "update_frequency_hours": 470,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-tony-robbins-podcast-tony-robbins-eh9wNFJcP1W.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-tony-robbins-podcast-tony-robbins-eh9wNFJcP1W.300x300.jpg",
      "is_claimed": false,
      "description": "\u201cWhy live an ordinary life, when you can live an extraordinary one?\u201d Tony Robbins, the #1 Life and Business Strategist, has helped over 50 million people from 100 countries create real and lasting change in their lives. In this podcast, he shares proven strategies and tactics so you, too, can achieve massive results in your business, relationships, health and finances. In addition to excerpts from his signature events and other exclusive, never-before-released audio content, Tony and his team also conduct deeply insightful interviews with the most prominent masterminds and experts on the global stage.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 74,
      "total_episodes": 151,
      "listennotes_url": "https://www.listennotes.com/c/fc6d33e22b7f4db38df3bb64a9a8c227/",
      "audio_length_sec": 2726,
      "explicit_content": false,
      "latest_episode_id": "6edbd759651748ad9b679b4893b33709",
      "latest_pub_date_ms": 1657156824000,
      "earliest_pub_date_ms": 1459373820099,
      "update_frequency_hours": 813,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-life-coach-school-podcast-brooke-castillo-vKhkd4qFUuw-V5of7JlG_RD.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-life-coach-school-podcast-brooke-castillo-Yl3ObVSwKEi-V5of7JlG_RD.300x300.jpg",
      "is_claimed": false,
      "description": "The Life Coach School Podcast is your go-to resource for learning, growing, and becoming certified as a Life Coach & Weight Loss Coach. Through this podcast, you'll hear directly from the Master Coach Brooke Castillo to help you better understand life coaching, the required skills and mindsets, and how we focus on serving the client to get them the results they seek.  At The Life Coach School, we offer a thorough and intense certification course that produces some of the most successful coaches coaching today. Learn more at TheLifeCoachSchool.com.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 74,
      "total_episodes": 464,
      "listennotes_url": "https://www.listennotes.com/c/ed79b615ed074204bc4702b56a264a78/",
      "audio_length_sec": 1934,
      "explicit_content": false,
      "latest_episode_id": "d57b7de0a4bf4f06909a5eecc775ff86",
      "latest_pub_date_ms": 1658394031000,
      "earliest_pub_date_ms": 1398606925438,
      "update_frequency_hours": 148,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-Yw2Q5dIpK3A-kmx0XIZTAys.1400x1400.jpg",
      "title": "The Best One Yet",
      "country": "United States",
      "website": "https://www.instagram.com/tboypod?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        67,
        99,
        98,
        95
      ],
      "itunes_id": 1386234384,
      "publisher": "Nick & Jack Studios",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-KlIFOa-dpRW-kmx0XIZTAys.300x300.jpg",
      "is_claimed": false,
      "description": "The daily pop-biz news show making today\u2019s top stories your business. 15 minutes on the 3 biz stories you need, with fresh takes you can pretend you came up with \u2014 Pairs perfectly with your morning oatmeal ritual. Hosted by Jack Crivici-Kramer & Nick Martell.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 73,
      "total_episodes": 789,
      "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
      "audio_length_sec": 1060,
      "explicit_content": false,
      "latest_episode_id": "dc03b637c7b440e8a0c47abf75c8bcea",
      "latest_pub_date_ms": 1658912400000,
      "earliest_pub_date_ms": 1553519100785,
      "update_frequency_hours": 28,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/masters-of-scale-with-reid-hoffman-waitwhat-PJGeHLMmxa6-mYoV0CUyxTD.1400x1400.jpg",
      "title": "Masters of Scale",
      "country": "United States",
      "website": "http://www.mastersofscale.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        171,
        67,
        93,
        157,
        127,
        173,
        149,
        97,
        122
      ],
      "itunes_id": 1227971746,
      "publisher": "WaitWhat ",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/masters-of-scale-with-reid-hoffman-waitwhat-XJs3WwmUrx7-mYoV0CUyxTD.300x300.jpg",
      "is_claimed": false,
      "description": "\n      <p>Award-winning business advice from Silicon Valley and beyond. Iconic CEOs, from Nike to Netflix, Starbucks to Slack, share the strategies that helped them grow from startups into global brands \u2014 and to weather crisis when it strikes.&nbsp;</p><p>Our two formats help tell the complete story of how a business grows, survives and thrives, and the mindsets of growth that keep leaders in the game.</p><p>On each episode of our classic format, host Reid Hoffman \u2014 LinkedIn cofounder, Greylock partner and legendary Silicon Valley investor \u2014 proves an unconventional theory about how businesses scale, asking his guests to share their stories of entrepreneurship, leadership, strategy, management, fundraising. You\u2019ll hear the human journey too \u2014 failures, setbacks, learnings.&nbsp;</p><p>From our Rapid Response format, you can expect real-time wisdom from business leaders in fast-changing situations. Hosted by Bob Safian, past editor in chief of Fast Company, these episodes tackle crisis response, rebuilding, diversity &amp; inclusion, leadership change and much more.&nbsp;</p>\n    ",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 73,
      "total_episodes": 311,
      "listennotes_url": "https://www.listennotes.com/c/d863da7f921e435fb35f512b54e774d6/",
      "audio_length_sec": 2061,
      "explicit_content": false,
      "latest_episode_id": "5cc487d7a5d64a0187dbe13dcbb524d3",
      "latest_pub_date_ms": 1658826000000,
      "earliest_pub_date_ms": 1492543297306,
      "update_frequency_hours": 79,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/marketplace-marketplace-WHc17NQy23S-Jing2WtK5UE.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/marketplace-marketplace-_YVywHeR0-S-Jing2WtK5UE.300x300.jpg",
      "is_claimed": false,
      "description": "<p>Every weekday, host Kai Ryssdal helps you make sense of the day\u2019s business and economic news \u2014 no econ degree or finance background required. \u201cMarketplace\u201d takes you beyond the numbers, bringing you context. Our team of reporters all over the world speak with CEOs, policymakers and regular people just trying to get by.</p>\n",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 73,
      "total_episodes": 155,
      "listennotes_url": "https://www.listennotes.com/c/5590cb1318054bceb942564a4f067eb6/",
      "audio_length_sec": 1646,
      "explicit_content": false,
      "latest_episode_id": "e12b15bb72b740acb3d4922f86a2340e",
      "latest_pub_date_ms": 1658964586000,
      "earliest_pub_date_ms": 1640304971049,
      "update_frequency_hours": 28,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "73bebcbe52654d1cb94cd1639f736be3",
      "rss": "https://www.omnycontent.com/d/playlist/9b7dacdf-a925-4f95-84dc-ac46003451ff/7029f3ae-fc09-45dd-9e7a-ac5400edbc2f/7cd3d0a4-5749-4d43-9400-ac5400edbc3d/podcast.rss",
      "type": "episodic",
      "email": "info@kastmedia.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly93d3cub21ueWNvbnRlbnQuY29tL2QvcGxheWxpc3QvOWI3ZGFjZGYtYTkyNS00Zjk1LTg0ZGMtYWM0NjAwMzQ1MWZmLzcwMjlmM2FlLWZjMDktNDVkZC05ZTdhLWFjNTQwMGVkYmMyZi83Y2QzZDBhNC01NzQ5LTRkNDMtOTQwMC1hYzU0MDBlZGJjM2QvcG9kY2FzdC5yc3M=",
        "spotify_url": "https://open.spotify.com/show/34gFfhLCtfg7GTNo841SuK",
        "youtube_url": "https://www.youtube.com/user/tailopezofficial",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "tailopez",
        "facebook_handle": "TaiLopezOfficial",
        "amazon_music_url": "",
        "instagram_handle": "tailopez"
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-tai-lopez-show-tai-lopez-509rFHaG-1o-kTnaZBogLC0.1400x1400.jpg",
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
      "publisher": "Kast Media",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-tai-lopez-show-tai-lopez-GYBslgCVEa2-kTnaZBogLC0.300x300.jpg",
      "is_claimed": false,
      "description": "<p>The Tai Lopez podcast brings you the best business education straight from the world's top entrepreneurs. I will also review the best books in health, wealth, love and happiness that will help you achieve your maximum potential and live the best life possible. </p>",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 72,
      "total_episodes": 609,
      "listennotes_url": "https://www.listennotes.com/c/73bebcbe52654d1cb94cd1639f736be3/",
      "audio_length_sec": 2024,
      "explicit_content": true,
      "latest_episode_id": "9c7e4cd73e194f6c8772290dda856981",
      "latest_pub_date_ms": 1657649234000,
      "earliest_pub_date_ms": 1400098196605,
      "update_frequency_hours": 276,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-smart-passive-income-online-business-jN-aR6qdYuo-NDa6-ySp9kw.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-smart-passive-income-online-business-sF24owQHYWy-NDa6-ySp9kw.300x300.jpg",
      "is_claimed": false,
      "description": "\n      Pat Flynn from The Smart Passive Income Blog reveals all of his online business and blogging strategies, income sources and killer marketing tips and tricks so you can be ahead of the curve with your online business or blog. Discover how you can create multiple passive income streams that work for you so that you can have the time and freedom to do what you love, whether it's traveling the world, or just living comfortably at home. Since 2008, he's been supporting his family with his many online businesses, and he's been openly sharing his wins, his losses, and all the lessons in between with the community of energetic but humble entrepreneurs who follow him. Self-proclaimed \"crash test dummy of online business\", you'll learn about building authority online, email marketing, building a team and outsourcing, content marketing, podcasting, search engine optimization, niche sites, social media strategies, how to get more traffic, creating online courses, affiliate marketing, and productivity tips so that you create something amazing without burning yourself out. It's a mix of interviews, special co-hosts and solo shows from Pat you're not going to want to miss. Hit subscribe, and get ready to change your life.\n    ",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 72,
      "total_episodes": 609,
      "listennotes_url": "https://www.listennotes.com/c/499661f3589f42aaa1532673e0e0aedf/",
      "audio_length_sec": 2626,
      "explicit_content": false,
      "latest_episode_id": "c4c94efd1e1a4553902d7874e9c01370",
      "latest_pub_date_ms": 1658905200000,
      "earliest_pub_date_ms": 1279551600594,
      "update_frequency_hours": 84,
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
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/call-me-candid-haley-pham-lilly-ann-_dSsBumNY9x-LY-c8VNnzRO.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/call-me-candid-haley-pham-lilly-ann-wbmDUyde8-A-LY-c8VNnzRO.300x300.jpg",
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
      "audio_length_sec": 2683,
      "explicit_content": false,
      "latest_episode_id": "0c9b9045f27b4a0bbc206807a7f6cc2f",
      "latest_pub_date_ms": 1600063200000,
      "earliest_pub_date_ms": 1579047805031,
      "update_frequency_hours": 167,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/scam-goddess-earwolf-laci-mosley-pMX-87Jicaq-PstEMgqXCUd.1400x1400.jpg",
      "title": "Scam Goddess",
      "country": "United States",
      "website": "https://www.earwolf.com/show/scam-goddess/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        135,
        67,
        133,
        93
      ],
      "itunes_id": 1479455008,
      "publisher": "Earwolf & Laci Mosley",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/scam-goddess-earwolf-laci-mosley-fy8Bs4RlT06-PstEMgqXCUd.300x300.jpg",
      "is_claimed": false,
      "description": "\u201cScam Goddess is a podcast dedicated to fraud and all those who practice it! Each week host Laci Mosley (aka Scam Goddess) keeps listeners up to date on current rackets, digs deep into the latest scams, and breaks down historic hoodwinks alongside some of your favorite comedians! It's like true crime only without all the death! True fun crime!\u201d",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 71,
      "total_episodes": 86,
      "listennotes_url": "https://www.listennotes.com/c/23bd4f3432c2452d93f525e2446a5878/",
      "audio_length_sec": 3895,
      "explicit_content": true,
      "latest_episode_id": "1d1907dee399436bb5c2b18a371797cb",
      "latest_pub_date_ms": 1658808000000,
      "earliest_pub_date_ms": 1420099200036,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/earn-your-leisure-the-black-effect-and-tGoV3nNpfCS-CSRy4Lz625Y.1400x1400.jpg",
      "title": "Earn Your Leisure",
      "country": "United States",
      "website": "https://www.iheart.com/podcast/256-earn-your-leisure-31087183/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        67
      ],
      "itunes_id": 1450211392,
      "publisher": "The Black Effect and iHeartPodcasts",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/earn-your-leisure-the-black-effect-and-kVA_ctJU0yZ-CSRy4Lz625Y.300x300.jpg",
      "is_claimed": false,
      "description": "Welcome to The Earn Your Leisure Podcast. Rashad Bilal and Troy Millings will be your host. Earn Your Leisure will be giving you behind the scenes financial views into the entertainment and sports industries as well as highlighting back stories of entrepreneurs. We will also be breaking down business models and examining the latest trends in finance. Earn Your Leisure is a college business class mixed with pop culture. We blend the two together for a unique and exciting look into the world of business. Let\u2019s go!! #earnyourleisurepodcast",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 71,
      "total_episodes": 377,
      "listennotes_url": "https://www.listennotes.com/c/c73271d55ffa4e2d9b529220072fbd79/",
      "audio_length_sec": 3132,
      "explicit_content": false,
      "latest_episode_id": "7f0f6d095e6c497a9d92ba5966790b42",
      "latest_pub_date_ms": 1658878200000,
      "earliest_pub_date_ms": 1548186120375,
      "update_frequency_hours": 55,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/online-marketing-made-easy-with-amy--Idu4myEQGo-jXUyf4vBV20.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/online-marketing-made-easy-with-amy-8ns5W6RkdPl-jXUyf4vBV20.300x300.jpg",
      "is_claimed": false,
      "description": "Ever wish you had a business mentor with over a decade of experience whispering success secrets in your ear? That\u2019s exactly what you\u2019ll get when you tune into the top-ranked Online Marketing Made Easy Podcast with your host, 9 to 5er turned CEO of a multi-million dollar business, Amy Porterfield. Her specialty? Breaking down big ideas and strategies into actionable step-by-step processes designed to get you results with a whole lot less stress. Tune in, get inspired, and get ready to discover why hundreds of thousands of online business owners turn to Amy for guidance when it comes to all things online business including digital courses, list building, social media, content, webinars, and so much more. Whether you're a budding entrepreneur, have a comfy side-hustle, or are looking to take your business to the next level, each episode is designed to help you take immediate action on the most important strategies for starting and growing your online business today.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 71,
      "total_episodes": 513,
      "listennotes_url": "https://www.listennotes.com/c/fbecfdd4116e4e7a954bd6bc4cb0b406/",
      "audio_length_sec": 2391,
      "explicit_content": false,
      "latest_episode_id": "1ee506db94ea403bbb1daf81fefef291",
      "latest_pub_date_ms": 1658905359000,
      "earliest_pub_date_ms": 1358200867495,
      "update_frequency_hours": 84,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/by-the-book-stitcher-jolenta-greenberg-VJ1gq8zXAma--sCyAljv4BT.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/by-the-book-stitcher-jolenta-greenberg-KqpS3TeQW6i--sCyAljv4BT.300x300.jpg",
      "is_claimed": false,
      "description": "Half reality show, half self-help podcast, and one wild social experiment. Join comedian Jolenta Greenberg and culture critic Kristen Meinzer as they live by the rules of a different self-help book each episode to figure out which ones might actually be life changing.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 71,
      "total_episodes": 215,
      "listennotes_url": "https://www.listennotes.com/c/4e272a4cec844b32be6ad2048d614b28/",
      "audio_length_sec": 2051,
      "explicit_content": true,
      "latest_episode_id": "15bf218502fa4b299231c19da3e8b531",
      "latest_pub_date_ms": 1658980800000,
      "earliest_pub_date_ms": 1489787580213,
      "update_frequency_hours": 251,
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
        "amazon_music_url": "",
        "instagram_handle": "wnycstudios"
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/trump-inc-wnyc-studios-KfHE1-pj3iw-r2THU0gu3fB.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/trump-inc-wnyc-studios-Luv2o8CKclT-r2THU0gu3fB.300x300.jpg",
      "is_claimed": false,
      "description": "He\u2019s the President, yet we\u2019re still trying to answer basic questions about how his business works: What deals are happening, who they\u2019re happening with, and if the President and his family are keeping their promise to separate the Trump Organization from the Trump White House. \u201cTrump, Inc.\u201d is a joint reporting project from WNYC Studios and ProPublica that digs deep into these questions. We\u2019ll be layout out what we know, what we don\u2019t and how you can help us fill in the gaps. \r\nWNYC Studios is a listener-supported producer of other leading podcasts, including On the Media, Radiolab, Death, Sex & Money, Here\u2019s the Thing with Alec Baldwin, Nancy and many others. ProPublica is a non-profit investigative newsroom.\r\n\u00a9 WNYC Studios",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 71,
      "total_episodes": 98,
      "listennotes_url": "https://www.listennotes.com/c/295925e24d5a478f8478ee1026560efc/",
      "audio_length_sec": 1743,
      "explicit_content": false,
      "latest_episode_id": "59bae7f9481148cda40b6f1a68d52e4b",
      "latest_pub_date_ms": 1651593600000,
      "earliest_pub_date_ms": 1517806800000,
      "update_frequency_hours": 276,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/entrepreneurs-on-fire-john-lee-dumas-of-rmRvnlE2Lp9-1WOhT7u6VQb.1400x1400.jpg",
      "title": "Entrepreneurs on Fire",
      "country": "United States",
      "website": "https://www.eofire.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        171,
        67,
        93,
        173,
        157,
        169,
        88,
        111,
        90,
        94,
        97
      ],
      "itunes_id": 564001633,
      "publisher": "John Lee Dumas of EOFire",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/entrepreneurs-on-fire-john-lee-dumas-of-KdVcHArxN1E-1WOhT7u6VQb.300x300.jpg",
      "is_claimed": true,
      "description": "John Lee Dumas is the founder and host of the award winning podcast, Entrepreneurs On Fire. With over 100 million listens of his 3000+ episodes, JLD has turned Entrepreneurs On Fire into a media empire that generates over a million listens every month and 7-figures of NET annual revenue 8-years in a row. His first traditionally published book, The Common Path to Uncommon Success is the modern day version of Think and Grow Rich with a revolutionary 17-step roadmap to financial freedom and fulfillment. Learn more at UncommonSuccessBook.com",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 71,
      "total_episodes": 3060,
      "listennotes_url": "https://www.listennotes.com/c/a409b8bb93f44054a7be2d6b30843899/",
      "audio_length_sec": 1823,
      "explicit_content": false,
      "latest_episode_id": "93ea326f8311402da8d959aee7b40218",
      "latest_pub_date_ms": 1658910600000,
      "earliest_pub_date_ms": 1348297203040,
      "update_frequency_hours": 24,
      "listen_score_global_rank": "0.05%"
    },
    {
      "id": "53e9a98a9e18406aafef8ccd66369fcb",
      "rss": "http://feeds.feedburner.com/ThePeterSchiffShowPodcast",
      "type": "episodic",
      "email": "customerservice@schiffradio.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cDovL2ZlZWRzLmZlZWRidXJuZXIuY29tL1RoZVBldGVyU2NoaWZmU2hvd1BvZGNhc3Q=",
        "spotify_url": "https://open.spotify.com/show/77ckqkx3MbP1cKhjDjAbDY",
        "youtube_url": "",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "",
        "facebook_handle": "",
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-peter-schiff-show-podcast-peter-schiff-Lb2jqs-41rJ-jY5-XW4QLf_.924x924.jpg",
      "title": "The Peter Schiff Show Podcast",
      "country": "United States",
      "website": "https://schiffradio.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        144,
        98,
        67,
        93
      ],
      "itunes_id": 404963432,
      "publisher": "Peter Schiff",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-peter-schiff-show-podcast-peter-schiff-Vx7JloDK5Ew-jY5-XW4QLf_.300x300.jpg",
      "is_claimed": true,
      "description": "Peter Schiff is an economist, financial broker/dealer, author, frequent guest on national news, and host of the Peter Schiff Show Podcast. The podcast focuses on economic data analysis and unbiased coverage of financial news, both in the U.S. and global markets. As entertaining as he is informative, Peter packs decades of brilliant insight into every news item. Join the thousands of fans who have benefited from Peter\u2019s commitment to getting the real story out to the world.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 71,
      "total_episodes": 923,
      "listennotes_url": "https://www.listennotes.com/c/53e9a98a9e18406aafef8ccd66369fcb/",
      "audio_length_sec": 2905,
      "explicit_content": false,
      "latest_episode_id": "2f9400ca75c741f092ab5e773c233ca0",
      "latest_pub_date_ms": 1658682678000,
      "earliest_pub_date_ms": 1450401062000,
      "update_frequency_hours": 98,
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

See all available parameters on the [API Docs page](https://www.listennotes.com/podcast-api/docs/#get-api-v2-regions).


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

See all available parameters on the [API Docs page](https://www.listennotes.com/podcast-api/docs/#get-api-v2-podcasts-id-recommendations).


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
        "amazon_music_url": "",
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
      "listen_score": 37,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-tim-ferriss-show-5-minute-podcast-mpqMa73u08D-mYx8LcSkhz1.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-tim-ferriss-show-5-minute-podcast-XMuN8q2Jorb-mYx8LcSkhz1.300x300.jpg",
      "is_claimed": false,
      "description": "5 minute summaries of The Tim Ferriss Show's podcast episodes. Get the best insights and ideas in much less time, more at owltail.com<br /><br />Written summaries: <a href=\"https://www.owltail.com/summaries/75553-the-tim-ferriss-show\" rel=\"noopener\">https://www.owltail.com/summaries/75553-the-tim-ferriss-show</a><br /><br />Other podcast summaries in Apple Podcasts: <a href=\"http://bit.ly/5-min-summaries\" rel=\"noopener\">http://bit.ly/5-min-summaries</a><br /><br />Other podcast summaries In other apps, search 'podcast summaries'.<br /><br />Tim Ferriss is a self-experimenter and bestselling author, best known for The 4-Hour Workweek, which has been translated into 40+ languages. Newsweek calls him \"the world's best human guinea pig,\" and The New York Times calls him \"a cross between Jack Welch and a Buddhist monk.\" In this show, he deconstructs world-class performers from eclectic areas (investing, chess, pro sports, etc.), digging deep to find the tools, tactics, and tricks that listeners can use.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 33,
      "total_episodes": 12,
      "listennotes_url": "https://www.listennotes.com/c/7060b5d48b3440ba9668f9af2a90fa7f/",
      "audio_length_sec": 221,
      "explicit_content": false,
      "latest_episode_id": "9163fe8fdfc34710af8d41b575023e07",
      "latest_pub_date_ms": 1625881044000,
      "earliest_pub_date_ms": 1619229600011,
      "update_frequency_hours": 165,
      "listen_score_global_rank": "5%"
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/how-i-built-this-with-guy-raz-guy-raz-wondery-7krpVtcCzMB-UC0qH23iP9T.1400x1400.jpg",
      "title": "How I Built This with Guy Raz",
      "country": "United States",
      "website": "https://wondery.com/shows/how-i-built-this?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        171,
        67,
        93,
        127,
        106,
        94,
        173,
        90,
        157
      ],
      "itunes_id": 1150510297,
      "publisher": "Guy Raz | Wondery",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/how-i-built-this-with-guy-raz-guy-raz-wondery--t38KFIqlAi-UC0qH23iP9T.300x300.jpg",
      "is_claimed": false,
      "description": "\n      <p>Guy Raz dives into the stories behind some of the world's best known companies. <em>How I Built This</em> weaves a narrative journey about innovators, entrepreneurs and idealists\u2014and the movements they built. Order the <em>How I Built This</em> book at https://www.guyraz.com</p>\n    ",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 85,
      "total_episodes": 433,
      "listennotes_url": "https://www.listennotes.com/c/f9d5885d7cf7485d891e82dea3186640/",
      "audio_length_sec": 2890,
      "explicit_content": false,
      "latest_episode_id": "77d1cd8d096a434ea2c7a6d8cc276d70",
      "latest_pub_date_ms": 1658733000000,
      "earliest_pub_date_ms": 1472828160429,
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
        "amazon_music_url": "",
        "instagram_handle": "garyvee"
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-garyvee-audio-experience-gary-vaynerchuk-3dCqxBQZSX9-X0Dfm7O_o3y.1400x1400.jpg",
      "title": "The GaryVee Audio Experience",
      "country": "United States",
      "website": "http://www.garyvaynerchuk.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        67,
        171,
        93,
        98,
        173,
        157,
        97,
        78,
        169,
        127,
        95
      ],
      "itunes_id": 928159684,
      "publisher": "Gary Vaynerchuk",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-garyvee-audio-experience-gary-vaynerchuk-G6zR28cWvB1-X0Dfm7O_o3y.300x300.jpg",
      "is_claimed": false,
      "description": "Welcome to The GaryVee Audio Experience, hosted by entrepreneur, CEO, investor, content creator, and public speaker Gary Vaynerchuk. On this podcast you'll find a mix of the #AskGaryVee show episodes, keynote speeches on marketing and business, segments from my DAILYVEE video series, interviews and fireside chats I've given, as well as new and current thoughts I record originally for this audio experience!\n\n",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 82,
      "total_episodes": 2308,
      "listennotes_url": "https://www.listennotes.com/c/fe6864628066420c8103c94e91e72eb3/",
      "audio_length_sec": 1844,
      "explicit_content": true,
      "latest_episode_id": "5a9054bf8169488a863366c0c0705f1d",
      "latest_pub_date_ms": 1658916050000,
      "earliest_pub_date_ms": 1412179202290,
      "update_frequency_hours": 23,
      "listen_score_global_rank": "0.01%"
    },
    {
      "id": "9f6ee51adfb046cc9936490abd2666ce",
      "rss": "https://rss.art19.com/the-school-of-greatness",
      "type": "episodic",
      "email": "podcast@schoolofgreatness.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9yc3MuYXJ0MTkuY29tL3RoZS1zY2hvb2wtb2YtZ3JlYXRuZXNz",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-school-of-greatness-lewis-howes-O2ujtdq34n7-H1zdqljixbp.1400x1400.jpg",
      "title": "The School of Greatness",
      "country": "United States",
      "website": "http://lewishowes.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        88,
        67,
        91,
        111,
        181,
        171,
        94,
        97,
        89,
        77,
        78,
        90
      ],
      "itunes_id": 596047499,
      "publisher": "Lewis Howes",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-school-of-greatness-lewis-howes-CS5yJWeoMpq-H1zdqljixbp.300x300.jpg",
      "is_claimed": false,
      "description": "\n      <p>Lewis Howes is a New York Times best-selling author, 2x All-American athlete, keynote speaker, and entrepreneur. The School of Greatness shares inspiring interviews from the most successful people on the planet\u2014world-renowned leaders in business, entertainment, sports, science, health, and literature\u2014to inspire YOU to unlock your inner greatness and live your best life.</p>\n    ",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 80,
      "total_episodes": 1298,
      "listennotes_url": "https://www.listennotes.com/c/9f6ee51adfb046cc9936490abd2666ce/",
      "audio_length_sec": 3022,
      "explicit_content": false,
      "latest_episode_id": "d721ee16a6604741818384db5ef1a9ad",
      "latest_pub_date_ms": 1658905200000,
      "earliest_pub_date_ms": 1358928001274,
      "update_frequency_hours": 55,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/entrepreneurs-on-fire-john-lee-dumas-of-rmRvnlE2Lp9-1WOhT7u6VQb.1400x1400.jpg",
      "title": "Entrepreneurs on Fire",
      "country": "United States",
      "website": "https://www.eofire.com/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        171,
        67,
        93,
        173,
        157,
        169,
        88,
        111,
        90,
        94,
        97
      ],
      "itunes_id": 564001633,
      "publisher": "John Lee Dumas of EOFire",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/entrepreneurs-on-fire-john-lee-dumas-of-KdVcHArxN1E-1WOhT7u6VQb.300x300.jpg",
      "is_claimed": true,
      "description": "John Lee Dumas is the founder and host of the award winning podcast, Entrepreneurs On Fire. With over 100 million listens of his 3000+ episodes, JLD has turned Entrepreneurs On Fire into a media empire that generates over a million listens every month and 7-figures of NET annual revenue 8-years in a row. His first traditionally published book, The Common Path to Uncommon Success is the modern day version of Think and Grow Rich with a revolutionary 17-step roadmap to financial freedom and fulfillment. Learn more at UncommonSuccessBook.com",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 71,
      "total_episodes": 3060,
      "listennotes_url": "https://www.listennotes.com/c/a409b8bb93f44054a7be2d6b30843899/",
      "audio_length_sec": 1823,
      "explicit_content": false,
      "latest_episode_id": "93ea326f8311402da8d959aee7b40218",
      "latest_pub_date_ms": 1658910600000,
      "earliest_pub_date_ms": 1348297203040,
      "update_frequency_hours": 24,
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
        "spotify_url": "https://open.spotify.com/show/4rOoJ6Egrf8K2IrywzwOMk",
        "youtube_url": "https://www.youtube.com/channel/UCzQUP1qoWDoEbmsQxvdjxgQ",
        "linkedin_url": "",
        "wechat_handle": "",
        "patreon_handle": "",
        "twitter_handle": "joerogan",
        "facebook_handle": "JOEROGAN",
        "amazon_music_url": "",
        "instagram_handle": "joerogan"
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-joe-rogan-experience-joe-rogan-aEnyMQet6ig-s_ML5QqPi0v.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-joe-rogan-experience-joe-rogan-Q2x5HywaS-O-s_ML5QqPi0v.300x300.jpg",
      "is_claimed": false,
      "description": "Conduit to the Gaian Mind",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 97,
      "total_episodes": 1,
      "listennotes_url": "https://www.listennotes.com/c/cba6cf06a87140bc9226efc8d530ed4d/",
      "audio_length_sec": 7355,
      "explicit_content": true,
      "latest_episode_id": "db83a67e183a4cce95967f3afe713f2c",
      "latest_pub_date_ms": 1524695830000,
      "earliest_pub_date_ms": 1524695830000,
      "update_frequency_hours": 0,
      "listen_score_global_rank": "0.01%"
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-smart-passive-income-online-business-jN-aR6qdYuo-NDa6-ySp9kw.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-smart-passive-income-online-business-sF24owQHYWy-NDa6-ySp9kw.300x300.jpg",
      "is_claimed": false,
      "description": "\n      Pat Flynn from The Smart Passive Income Blog reveals all of his online business and blogging strategies, income sources and killer marketing tips and tricks so you can be ahead of the curve with your online business or blog. Discover how you can create multiple passive income streams that work for you so that you can have the time and freedom to do what you love, whether it's traveling the world, or just living comfortably at home. Since 2008, he's been supporting his family with his many online businesses, and he's been openly sharing his wins, his losses, and all the lessons in between with the community of energetic but humble entrepreneurs who follow him. Self-proclaimed \"crash test dummy of online business\", you'll learn about building authority online, email marketing, building a team and outsourcing, content marketing, podcasting, search engine optimization, niche sites, social media strategies, how to get more traffic, creating online courses, affiliate marketing, and productivity tips so that you create something amazing without burning yourself out. It's a mix of interviews, special co-hosts and solo shows from Pat you're not going to want to miss. Hit subscribe, and get ready to change your life.\n    ",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 72,
      "total_episodes": 609,
      "listennotes_url": "https://www.listennotes.com/c/499661f3589f42aaa1532673e0e0aedf/",
      "audio_length_sec": 2626,
      "explicit_content": false,
      "latest_episode_id": "c4c94efd1e1a4553902d7874e9c01370",
      "latest_pub_date_ms": 1658905200000,
      "earliest_pub_date_ms": 1279551600594,
      "update_frequency_hours": 84,
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

See all available parameters on the [API Docs page](https://www.listennotes.com/podcast-api/docs/#get-api-v2-episodes-id-recommendations).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "recommendations": [
    {
      "id": "05534e9d98a1469c8e402b7103d77015",
      "link": "https://www.coindesk.com/podcasts/markets-daily?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/05534e9d98a1469c8e402b7103d77015/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/markets-daily-crypto-roundup-coindeskcom-s6p-SAaKNWj-VTiDtLAInyo.1400x1400.jpg",
      "title": "Most Influential 2021: Roham Gharegozlou (Pt. 1)",
      "podcast": {
        "id": "6c7ed315628b441c8a1bf0e331da2ba9",
        "image": "https://cdn-images-1.listennotes.com/podcasts/markets-daily-crypto-roundup-coindeskcom-s6p-SAaKNWj-VTiDtLAInyo.1400x1400.jpg",
        "title": "Markets Daily Crypto Roundup",
        "publisher": "CoinDesk",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/markets-daily-crypto-roundup-coindeskcom-X34wW5_n1Zp-VTiDtLAInyo.300x300.jpg",
        "listen_score": 42,
        "listennotes_url": "https://www.listennotes.com/c/6c7ed315628b441c8a1bf0e331da2ba9/",
        "listen_score_global_rank": "1.5%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/markets-daily-crypto-roundup-coindeskcom-X34wW5_n1Zp-VTiDtLAInyo.300x300.jpg",
      "description": "<p>On today's show CoinDesk Columnist and author of 7 books, Jeff Wilser, picks Roham Gharegozlou as one of CoinDesk's Most Influential in 2021. The man behind CryptoKitties and NBA Top Shot has big plans for digital sports and the open metaverse.&nbsp;(Part 1)</p><p><a href=\"https://www.coindesk.com/business/2021/12/07/most-influential-2021-roham-gharegozlou/\" rel=\"noopener noreferrer\" target=\"_blank\">Read the story here.</a></p><p><br /></p><p><em>This episode is sponsored by&nbsp;</em><a href=\"https://www.kava.io/marketsdaily?utm_campaign=Ad%20Affiliates&amp;utm_source=markets_daily&amp;utm_medium=banner_ad&amp;utm_term=home\" rel=\"noopener noreferrer\" target=\"_blank\"><em>Kava</em></a>,&nbsp;<a href=\"https://nexo.io/?%20utm_source=coindesk&amp;utm_medium=fixed&amp;utm_campaign=coindesk_sponsoredline_%20nov21\" rel=\"noopener noreferrer\" target=\"_blank\"><em>Nexo.io</em></a><em>&nbsp;and&nbsp;</em><a href=\"https://markets.chainalysis.com/?utm_source=coindesk&amp;utm_medium=podcast\" rel=\"noopener noreferrer\" target=\"_blank\"><em>Market Intel by Chainalysis</em></a><em>.</em></p><p><br /></p><p><em>This episode was edited &amp; produced by&nbsp;</em><a href=\"https://www.coindesk.com/author/adrian-blust\" rel=\"noopener noreferrer\" target=\"_blank\"><em>Adrian Blust</em></a><em>.&nbsp;</em></p><p><em>-</em></p><p><a href=\"https://www.kava.io/marketsdaily?utm_campaign=Ad%20Affiliates&amp;utm_source=markets_daily&amp;utm_medium=banner_ad&amp;utm_term=home\" rel=\"noopener noreferrer\" target=\"_blank\"><strong><em>Kava</em></strong></a><em>&nbsp;lets you mint stablecoins, lend, borrow, earn and swap safely across the world\u2019s biggest crypto assets. Connect to the world's largest cryptocurrencies, ecosystems and financial applications on DeFi\u2019s most trusted, scalable and secure earning platform with&nbsp;</em><a href=\"https://www.kava.io/marketsdaily?utm_campaign=Ad%20Affiliates&amp;utm_source=markets_daily&amp;utm_medium=banner_ad&amp;utm_term=home\" rel=\"noopener noreferrer\" target=\"_blank\"><em>kava.io</em></a><em>.</em></p><p><em>-</em></p><p><a href=\"https://nexo.io/?%20utm_source=coindesk&amp;utm_medium=fixed&amp;utm_campaign=coindesk_sponsoredline_%20nov21\" rel=\"noopener noreferrer\" target=\"_blank\"><strong><em>Nexo</em></strong></a><em>&nbsp;is a powerful, all-in-one crypto platform where you can securely store your assets.&nbsp;Invest, borrow, exchange and earn up to 12% APR on Bitcoin and 20+ other top coins.&nbsp;Insured for $375M and audited in real-time by Armanino, Nexo is rated excellent on Trustpilot. Get started today at&nbsp;</em><a href=\"https://nexo.io/?%20utm_source=coindesk&amp;utm_medium=fixed&amp;utm_campaign=coindesk_sponsoredline_%20nov21\" rel=\"noopener noreferrer\" target=\"_blank\"><em>nexo.io</em></a><em>.</em></p><p><em>-</em></p><p><a href=\"https://markets.chainalysis.com/?utm_source=coindesk&amp;utm_medium=podcast\" rel=\"noopener noreferrer\" target=\"_blank\"><strong><em>Market Intel by Chainalysis</em></strong></a><em>\u2014the Blockchain Data Platform\u2014arms your team with the most complete on-chain dataset to make informed crypto investments, deliver original research, and identify and confidently fund emerging players in the market. See Chainalysis&nbsp;</em><a href=\"https://markets.chainalysis.com/?utm_source=coindesk&amp;utm_medium=podcast\" rel=\"noopener noreferrer\" target=\"_blank\"><em>Market Intel in action now</em></a><em>.</em></p><p>See Privacy Policy at <a href=\"https://art19.com/privacy\" rel=\"noopener noreferrer\" target=\"_blank\">https://art19.com/privacy</a> and California Privacy Notice at <a href=\"https://art19.com/privacy#do-not-sell-my-info\" rel=\"noopener noreferrer\" target=\"_blank\">https://art19.com/privacy#do-not-sell-my-info</a>.</p>",
      "pub_date_ms": 1640430000102,
      "guid_from_rss": "gid://art19-episode-locator/V0/qTL8NjCdWoTCfTWkK6E-ErwcwkPWKVNIhOlwHZH7Cbg",
      "listennotes_url": "https://www.listennotes.com/e/05534e9d98a1469c8e402b7103d77015/",
      "audio_length_sec": 574,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/05534e9d98a1469c8e402b7103d77015/#edit"
    },
    {
      "id": "9aaeb046a07042d09ca5214a94f999b4",
      "link": "https://www.coindesk.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/9aaeb046a07042d09ca5214a94f999b4/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/coindesk-reports/money-reimagined-inside-what-iJhcYnat3KX-CHxWD0gME75.1400x1400.jpg",
      "title": "MONEY REIMAGINED: Inside What Could Be NFTs 'Mainstream Moment' with Dapper Labs CEO Roham Gharegozlou",
      "podcast": {
        "id": "188eb6965eb048469400414acb5749ae",
        "image": "https://cdn-images-1.listennotes.com/podcasts/coindesk-reports-coindeskcom-2ZC6ING-TrD-TElxWfYmVpQ.1400x1400.jpg",
        "title": "CoinDesk Reports",
        "publisher": "CoinDesk",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/coindesk-reports-coindeskcom-vcYaEq5G_Ox-TElxWfYmVpQ.300x300.jpg",
        "listen_score": 29,
        "listennotes_url": "https://www.listennotes.com/c/188eb6965eb048469400414acb5749ae/",
        "listen_score_global_rank": "10%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/coindesk-reports/money-reimagined-inside-what-ezmdK02jRlc-CHxWD0gME75.300x300.jpg",
      "description": "<p>At the end of a high-energy week in the burgeoning digital art world, \u201cMoney Reimagined\u201d brings you the third and (for now) final edition of our NFT series.&nbsp;</p><p>In between recording this episode and publishing it two days later, a non-fungible token attached to a piece of digital art sold for a whopping $69.3 million. The sale, orchestrated by Christie\u2019s, turned the digital creator known as Beeple into the third-highest paid living artist. It also represented a high point in the media attention now swirling around this new, crypto-based technology.&nbsp;</p><p>So, it\u2019s appropriate we end on a note that grounds things in the reality of the technology and its potential to transform the creator economy generally, rather than being caught up in the celebrity story and media sensations. To do so, we talk with Roham Gharegozlou, the CEO and founder of Dapper Labs, the startup that in many respects is responsible for kicking off the entire NFT phenomenon.&nbsp;</p><p>We talk about the early days when Dapper created the ERC-721 standard on Ethereum and launched the popular CryptoKitties program. We talk about why the team made the decision to build its own blockchain, known as Flow, and to migrate the business there away from Ethereum. And we talk about where this rapidly evolving industry, with its competing platforms and wild debates over rights and opportunities, is going.</p><p>Join us for the conversation.&nbsp;</p><p><br /></p><p><em>Image credit:&nbsp;</em>&nbsp;<a href=\"https://unsplash.com/@benjaminjsuter?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText\" rel=\"noopener noreferrer\" target=\"_blank\">Benjamin Suter</a>&nbsp;on&nbsp;<a href=\"https://unsplash.com/s/photos/basketball?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText\" rel=\"noopener noreferrer\" target=\"_blank\">Unsplash</a>,&nbsp;<em>modified by CoinDesk</em></p><p><br /></p><p><br /></p><p>See Privacy Policy at <a href=\"https://art19.com/privacy\" rel=\"noopener noreferrer\" target=\"_blank\">https://art19.com/privacy</a> and California Privacy Notice at <a href=\"https://art19.com/privacy#do-not-sell-my-info\" rel=\"noopener noreferrer\" target=\"_blank\">https://art19.com/privacy#do-not-sell-my-info</a>.</p>",
      "pub_date_ms": 1615573111180,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/whats-next-samsung-next-BOU80jWegKh-kG8U3EdxHWo.1400x1400.jpg",
      "title": "Building blockchain collectibles with Dapper Labs founder Roham Gharegozlou",
      "podcast": {
        "id": "0615f79f64de4f1989d4ad1bac7cbc9e",
        "image": "https://cdn-images-1.listennotes.com/podcasts/whats-next-samsung-next-BOU80jWegKh-kG8U3EdxHWo.1400x1400.jpg",
        "title": "What's NEXT",
        "publisher": "Samsung NEXT",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/whats-next-samsung-next-RaNEz68Vhc0-kG8U3EdxHWo.300x300.jpg",
        "listen_score": 28,
        "listennotes_url": "https://www.listennotes.com/c/0615f79f64de4f1989d4ad1bac7cbc9e/",
        "listen_score_global_rank": "10%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/whats-next-samsung-next-RaNEz68Vhc0-kG8U3EdxHWo.300x300.jpg",
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
      "id": "45d99d5e71434c6fadc451f2eafb2515",
      "link": "https://outlierventures.podbean.com/e/from-cryptokitties-to-mainstreaming-non-fungible-tokens-roham-gharegozlou-of-dapper-labs/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/45d99d5e71434c6fadc451f2eafb2515/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-metaverse-podcast-outlierventures-JVXn7QCbS_k-m5zMBFCfEGK.1400x1400.jpg",
      "title": "From CryptoKitties to Mainstreaming Non Fungible Tokens, Roham Gharegozlou of Dapper Labs",
      "podcast": {
        "id": "cea5a5bf6fbc40aa8c11518b59a4e22b",
        "image": "https://cdn-images-1.listennotes.com/podcasts/the-metaverse-podcast-outlierventures-JVXn7QCbS_k-m5zMBFCfEGK.1400x1400.jpg",
        "title": "The Metaverse Podcast",
        "publisher": "OutlierVentures",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-metaverse-podcast-outlierventures-WnVUbZ6XiGd-m5zMBFCfEGK.300x300.jpg",
        "listen_score": 38,
        "listennotes_url": "https://www.listennotes.com/c/cea5a5bf6fbc40aa8c11518b59a4e22b/",
        "listen_score_global_rank": "2.5%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-metaverse-podcast-outlierventures-WnVUbZ6XiGd-m5zMBFCfEGK.300x300.jpg",
      "description": "<p>Roham Gharegozlou, Co-Inventor of CryptoKitties and Founder of Dapper Labs talks about scaling NFTs to billions of users and how the Metaverse, as an emergent ecosystem, will not be designed: it will be open fluid and anchored on a blockchain.</p>",
      "pub_date_ms": 1594644554098,
      "guid_from_rss": "outlierventures.podbean.com/ec278cab-b978-5e33-bac0-76f88e587698",
      "listennotes_url": "https://www.listennotes.com/e/45d99d5e71434c6fadc451f2eafb2515/",
      "audio_length_sec": 1891,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/45d99d5e71434c6fadc451f2eafb2515/#edit"
    },
    {
      "id": "774e65cead6e4b548f09a1a7bf7c55af",
      "link": "https://www.coindesk.com/podcasts/markets-daily?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/774e65cead6e4b548f09a1a7bf7c55af/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/markets-daily-crypto-roundup-coindeskcom-s6p-SAaKNWj-VTiDtLAInyo.1400x1400.jpg",
      "title": "Most Influential 2021: Roham Gharegozlou (Pt. 2)",
      "podcast": {
        "id": "6c7ed315628b441c8a1bf0e331da2ba9",
        "image": "https://cdn-images-1.listennotes.com/podcasts/markets-daily-crypto-roundup-coindeskcom-s6p-SAaKNWj-VTiDtLAInyo.1400x1400.jpg",
        "title": "Markets Daily Crypto Roundup",
        "publisher": "CoinDesk",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/markets-daily-crypto-roundup-coindeskcom-X34wW5_n1Zp-VTiDtLAInyo.300x300.jpg",
        "listen_score": 42,
        "listennotes_url": "https://www.listennotes.com/c/6c7ed315628b441c8a1bf0e331da2ba9/",
        "listen_score_global_rank": "1.5%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/markets-daily-crypto-roundup-coindeskcom-X34wW5_n1Zp-VTiDtLAInyo.300x300.jpg",
      "description": "<p>On today's show CoinDesk Columnist and author of 7 books, Jeff Wilser, picks Roham Gharegozlou as one of CoinDesk's Most Influential in 2021. The man behind CryptoKitties and NBA Top Shot has big plans for digital sports and the open metaverse.&nbsp;(Part 2)</p><p><a href=\"https://www.coindesk.com/business/2021/12/07/most-influential-2021-roham-gharegozlou/\" rel=\"noopener noreferrer\" target=\"_blank\">Read the story here.</a></p><p><br /></p><p><em>This episode is sponsored by&nbsp;</em><a href=\"https://www.kava.io/marketsdaily?utm_campaign=Ad%20Affiliates&amp;utm_source=markets_daily&amp;utm_medium=banner_ad&amp;utm_term=home\" rel=\"noopener noreferrer\" target=\"_blank\"><em>Kava</em></a>,&nbsp;<a href=\"https://nexo.io/?%20utm_source=coindesk&amp;utm_medium=fixed&amp;utm_campaign=coindesk_sponsoredline_%20nov21\" rel=\"noopener noreferrer\" target=\"_blank\"><em>Nexo.io</em></a><em>&nbsp;and&nbsp;</em><a href=\"https://markets.chainalysis.com/?utm_source=coindesk&amp;utm_medium=podcast\" rel=\"noopener noreferrer\" target=\"_blank\"><em>Market Intel by Chainalysis</em></a><em>.</em></p><p><br /></p><p><em>This episode was edited &amp; produced by&nbsp;</em><a href=\"https://www.coindesk.com/author/adrian-blust\" rel=\"noopener noreferrer\" target=\"_blank\"><em>Adrian Blust</em></a><em>.&nbsp;&nbsp;</em></p><p><em>-</em></p><p><a href=\"https://www.kava.io/marketsdaily?utm_campaign=Ad%20Affiliates&amp;utm_source=markets_daily&amp;utm_medium=banner_ad&amp;utm_term=home\" rel=\"noopener noreferrer\" target=\"_blank\"><strong><em>Kava</em></strong></a><em>&nbsp;lets you mint stablecoins, lend, borrow, earn and swap safely across the world\u2019s biggest crypto assets. Connect to the world's largest cryptocurrencies, ecosystems and financial applications on DeFi\u2019s most trusted, scalable and secure earning platform with&nbsp;</em><a href=\"https://www.kava.io/marketsdaily?utm_campaign=Ad%20Affiliates&amp;utm_source=markets_daily&amp;utm_medium=banner_ad&amp;utm_term=home\" rel=\"noopener noreferrer\" target=\"_blank\"><em>kava.io</em></a><em>.</em></p><p><em>-</em></p><p><a href=\"https://nexo.io/?%20utm_source=coindesk&amp;utm_medium=fixed&amp;utm_campaign=coindesk_sponsoredline_%20nov21\" rel=\"noopener noreferrer\" target=\"_blank\"><strong><em>Nexo</em></strong></a><em>&nbsp;is a powerful, all-in-one crypto platform where you can securely store your assets.&nbsp;Invest, borrow, exchange and earn up to 12% APR on Bitcoin and 20+ other top coins.&nbsp;Insured for $375M and audited in real-time by Armanino, Nexo is rated excellent on Trustpilot. Get started today at&nbsp;</em><a href=\"https://nexo.io/?%20utm_source=coindesk&amp;utm_medium=fixed&amp;utm_campaign=coindesk_sponsoredline_%20nov21\" rel=\"noopener noreferrer\" target=\"_blank\"><em>nexo.io</em></a><em>.</em></p><p><em>-</em></p><p><a href=\"https://markets.chainalysis.com/?utm_source=coindesk&amp;utm_medium=podcast\" rel=\"noopener noreferrer\" target=\"_blank\"><strong><em>Market Intel by Chainalysis</em></strong></a><em>\u2014the Blockchain Data Platform\u2014arms your team with the most complete on-chain dataset to make informed crypto investments, deliver original research, and identify and confidently fund emerging players in the market. See Chainalysis&nbsp;</em><a href=\"https://markets.chainalysis.com/?utm_source=coindesk&amp;utm_medium=podcast\" rel=\"noopener noreferrer\" target=\"_blank\"><em>Market Intel in action now</em></a><em>.</em></p><p>See Privacy Policy at <a href=\"https://art19.com/privacy\" rel=\"noopener noreferrer\" target=\"_blank\">https://art19.com/privacy</a> and California Privacy Notice at <a href=\"https://art19.com/privacy#do-not-sell-my-info\" rel=\"noopener noreferrer\" target=\"_blank\">https://art19.com/privacy#do-not-sell-my-info</a>.</p>",
      "pub_date_ms": 1640516400101,
      "guid_from_rss": "gid://art19-episode-locator/V0/r2o71PPmrHUyC-poZTVb_1aRNHd2tBCgIe_UrksQ3Gk",
      "listennotes_url": "https://www.listennotes.com/e/774e65cead6e4b548f09a1a7bf7c55af/",
      "audio_length_sec": 733,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/774e65cead6e4b548f09a1a7bf7c55af/#edit"
    },
    {
      "id": "8c9fcee265fc4f54bbca6afafcb8c28c",
      "link": "https://anchor.fm/thefirstmint/episodes/Roham-e15g29r?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/8c9fcee265fc4f54bbca6afafcb8c28c/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-first-mint-nft-podcast-the-first-mint-OVRGp9hjWeE-NuBwOlnV0bt.1400x1400.jpg",
      "title": "Roham",
      "podcast": {
        "id": "fbdf83bb46ac4e0b9e807991719e210f",
        "image": "https://cdn-images-1.listennotes.com/podcasts/the-first-mint-nft-podcast-the-first-mint-OVRGp9hjWeE-NuBwOlnV0bt.1400x1400.jpg",
        "title": "The First Mint :: NFT Podcast",
        "publisher": "The First Mint",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-first-mint-nft-podcast-the-first-mint-NbhLRadOHEt-NuBwOlnV0bt.300x300.jpg",
        "listen_score": 46,
        "listennotes_url": "https://www.listennotes.com/c/fbdf83bb46ac4e0b9e807991719e210f/",
        "listen_score_global_rank": "1%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-first-mint-nft-podcast-the-first-mint-NbhLRadOHEt-NuBwOlnV0bt.300x300.jpg",
      "description": "<p>Episode 83 of The First Mint.</p>\n<p>Roham.</p>\n<p>To kick off First Mint Fest, LG Doucet sat down with Roham Gharegozlou, the Founder &amp; CEO of Dapper Labs, the company behind NBA Top Shot and the Flow Blockchain.&nbsp;</p>",
      "pub_date_ms": 1628143512095,
      "guid_from_rss": "f148e49b-dfbf-4a94-8e3a-19bcb4ff1c17",
      "listennotes_url": "https://www.listennotes.com/e/8c9fcee265fc4f54bbca6afafcb8c28c/",
      "audio_length_sec": 3738,
      "explicit_content": false,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/8c9fcee265fc4f54bbca6afafcb8c28c/#edit"
    },
    {
      "id": "3663e1ba8f944df7956378ab332bf12b",
      "link": "https://www.gimletmedia.com/startup?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/3663e1ba8f944df7956378ab332bf12b/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/startup-podcast-gimlet-14zU0c_MOmv-n9PpCBTQvoJ.1400x1400.jpg",
      "title": "Introducing How to Save a Planet",
      "podcast": {
        "id": "0d362b13399240de97602ef614acdcbc",
        "image": "https://cdn-images-1.listennotes.com/podcasts/startup-podcast-gimlet-14zU0c_MOmv-n9PpCBTQvoJ.1400x1400.jpg",
        "title": "StartUp Podcast",
        "publisher": "Gimlet",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/startup-podcast-gimlet-8If7QBKU5jb-n9PpCBTQvoJ.300x300.jpg",
        "listen_score": 76,
        "listennotes_url": "https://www.listennotes.com/c/0d362b13399240de97602ef614acdcbc/",
        "listen_score_global_rank": "0.01%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/startup-podcast-gimlet-8If7QBKU5jb-n9PpCBTQvoJ.300x300.jpg",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/software-defined-interviews-software-yFixmv_8KZq-y7KRi_flj8t.1400x1400.jpg",
      "title": "Misaligned Incentives Episode 4: You get what you pay for - compensating tech staff is often done poorly",
      "podcast": {
        "id": "13350cb77ad548bc8991dac9657f45b7",
        "image": "https://cdn-images-1.listennotes.com/podcasts/software-defined-interviews-software-yFixmv_8KZq-y7KRi_flj8t.1400x1400.jpg",
        "title": "Software Defined Interviews",
        "publisher": "Software Defined Talk",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/software-defined-interviews-software-N8fPcvt0JmU-y7KRi_flj8t.300x300.jpg",
        "listen_score": null,
        "listennotes_url": "https://www.listennotes.com/c/13350cb77ad548bc8991dac9657f45b7/",
        "listen_score_global_rank": null
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/software-defined-interviews-software-N8fPcvt0JmU-y7KRi_flj8t.300x300.jpg",
      "description": "<pre><code>    &lt;p&gt;We discuss compensation, particularly how people in the IT department (&amp;quot;developers,&amp;quot; etc.) are so disconnected from the actual business that compensating them based on business performance is near impossible. Not good if you&amp;#39;re an IT person and like money.&lt;/p&gt;\n</code></pre>\n\n<p>There&#39;s other types of comp. then money, obviously, and those are fine too. In particular, we discuss participation in open source and more recognition. But, still: money is the best.</p>",
      "pub_date_ms": 1594980000000,
      "guid_from_rss": "efb05656-d9ef-4fe7-b583-3c49d929fb6c",
      "listennotes_url": "https://www.listennotes.com/e/b03b9f59a5df4d31bf44e1828353c8e6/",
      "audio_length_sec": 3057,
      "explicit_content": true,
      "maybe_audio_invalid": false,
      "listennotes_edit_url": "https://www.listennotes.com/e/b03b9f59a5df4d31bf44e1828353c8e6/#edit"
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

See all available parameters on the [API Docs page](https://www.listennotes.com/podcast-api/docs/#post-api-v2-episodes).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "episodes": [
    {
      "id": "0f34a9099579490993eec9e8c8cebb82",
      "link": "https://cms.megaphone.fm/channel/business-unusual-with-barbara-corcoran?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/0f34a9099579490993eec9e8c8cebb82/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-MtJ2fOBSuTp-aZPn3Ic47rx.1400x1400.jpg",
      "title": "35: Don\u2019t Make Your Landlord Rich",
      "podcast": {
        "id": "68faf62be97149c280ebcc25178aa731",
        "image": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-MtJ2fOBSuTp-aZPn3Ic47rx.1400x1400.jpg",
        "title": "Business Unusual with Barbara Corcoran",
        "publisher": "Barbara Corcoran",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-x2LQVPknMsc-aZPn3Ic47rx.300x300.jpg",
        "listen_score": 58,
        "listennotes_url": "https://www.listennotes.com/c/68faf62be97149c280ebcc25178aa731/",
        "listen_score_global_rank": "0.5%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-x2LQVPknMsc-aZPn3Ic47rx.300x300.jpg",
      "description": "<p>If you\u2019re starting a new business, you need to keep costs low \u2013 so renting is the way to go, right?\n\nI say no! I\u2019ll tell you why you should scrape together the cash to buy your business headquarters from the get-go.\u00a0\n\nAlso, I\u2019ll answer some more of your great questions about how to get the press to pay attention to your little mom and pop shop and what to do about a toxic work environment.\n\nGot a business question you want to ask me? Tweet it @BarbaraCorcoran and I may just answer it on a future episode!\n\nFollow Business Unusual with Barbara Corcoran on iHeartRadio, or subscribe wherever you listen to podcasts.\n\nThis episode of Business Unusual with Barbara Corcoran is presented by\u00a0On Deck Business Loans\u00a0(http://www.ondeck.com/barbara).\u00a0\u00a0\u00a0</p>",
      "pub_date_ms": 1546232460115,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/listen-money-matters-free-your-inner-lPXW7V_6n0C-SJEHNr84kVg.1400x1400.jpg",
      "title": "Do Things That Scale: Starting a Business That Will Take Off",
      "podcast": {
        "id": "3302bc71139541baa46ecb27dbf6071a",
        "image": "https://cdn-images-1.listennotes.com/podcasts/listen-money-matters-free-your-inner-lPXW7V_6n0C-SJEHNr84kVg.1400x1400.jpg",
        "title": "Listen Money Matters - Free your inner financial badass. All the stuff you should know about personal finance.",
        "publisher": "ListenMoneyMatters.com | Andrew Fiebert and Matt Giovanisci",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/listen-money-matters-free-your-inner-d5If074qkhz-SJEHNr84kVg.300x300.jpg",
        "listen_score": 66,
        "listennotes_url": "https://www.listennotes.com/c/3302bc71139541baa46ecb27dbf6071a/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/listen-money-matters-free-your-inner-d5If074qkhz-SJEHNr84kVg.300x300.jpg",
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

See all available parameters on the [API Docs page](https://www.listennotes.com/podcast-api/docs/#post-api-v2-podcasts).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "podcasts": [
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-MtJ2fOBSuTp-aZPn3Ic47rx.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-x2LQVPknMsc-aZPn3Ic47rx.300x300.jpg",
      "is_claimed": false,
      "description": "I\u2019m smart at getting to where I want to go, and I can teach you how to do it! I had 22 jobs before starting my real estate company with a $1000 loan and built it into a $5 billion business. Today I\u2019m a \u2019Shark\u2019 on ABC\u2019s hit show \"Shark Tank.\" It didn\u2019t take a fancy degree to get here but took street smarts and a lot of courage. Life is too short to waste your time practicing someone else\u2019s fancy theory on success. I give you the straight talk and the confidence to get there. Got a question? Call me at 888-BARBARA. Subscribe to Business Unusual with Barbara Corcoran wherever you listen to podcasts.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 58,
      "total_episodes": 156,
      "listennotes_url": "https://www.listennotes.com/c/68faf62be97149c280ebcc25178aa731/",
      "audio_length_sec": 1407,
      "explicit_content": false,
      "latest_episode_id": "d2ed0894db0c446c8aef4f4ca5853892",
      "latest_pub_date_ms": 1658808000000,
      "earliest_pub_date_ms": 1525202794150,
      "update_frequency_hours": 167,
      "listen_score_global_rank": "0.5%"
    },
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-L8QBusAiaXq-OaJSjb4xQv3.1400x1400.jpg",
      "title": "Exponent",
      "country": "United States",
      "website": "https://exponent.fm?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-IrgMw5cPALF-OaJSjb4xQv3.300x300.jpg",
      "is_claimed": false,
      "description": "A podcast about tech and society, hosted by Ben Thompson and James Allworth",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 61,
      "total_episodes": 197,
      "listennotes_url": "https://www.listennotes.com/c/37589a3e121e40debe4cef3d9638932a/",
      "audio_length_sec": 3739,
      "explicit_content": false,
      "latest_episode_id": "997c4db8bd224df78f0716a3a8c05f5d",
      "latest_pub_date_ms": 1636118076000,
      "earliest_pub_date_ms": 1392899826197,
      "update_frequency_hours": 940,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/binge-mode-marvel-the-ringer-QZoDCyP6hev-BdPpshCaFDu.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/binge-mode-marvel-the-ringer-bqVntBmw3ij-BdPpshCaFDu.300x300.jpg",
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
      "audio_length_sec": 7086,
      "explicit_content": true,
      "latest_episode_id": "349b3385606147b8b29d5aa653563669",
      "latest_pub_date_ms": 1616634120000,
      "earliest_pub_date_ms": 1496277060040,
      "update_frequency_hours": 103,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/listen-money-matters-free-your-inner-lPXW7V_6n0C-SJEHNr84kVg.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/listen-money-matters-free-your-inner-d5If074qkhz-SJEHNr84kVg.300x300.jpg",
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
      "audio_length_sec": 2787,
      "explicit_content": true,
      "latest_episode_id": "d044a9f0fb304c148f4f4e9e3ad27dd6",
      "latest_pub_date_ms": 1589169600000,
      "earliest_pub_date_ms": 1383138000504,
      "update_frequency_hours": 201,
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
        "amazon_music_url": "",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-Yw2Q5dIpK3A-kmx0XIZTAys.1400x1400.jpg",
      "title": "The Best One Yet",
      "country": "United States",
      "website": "https://www.instagram.com/tboypod?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        93,
        67,
        99,
        98,
        95
      ],
      "itunes_id": 1386234384,
      "publisher": "Nick & Jack Studios",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-KlIFOa-dpRW-kmx0XIZTAys.300x300.jpg",
      "is_claimed": false,
      "description": "The daily pop-biz news show making today\u2019s top stories your business. 15 minutes on the 3 biz stories you need, with fresh takes you can pretend you came up with \u2014 Pairs perfectly with your morning oatmeal ritual. Hosted by Jack Crivici-Kramer & Nick Martell.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 73,
      "total_episodes": 789,
      "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
      "audio_length_sec": 1060,
      "explicit_content": false,
      "latest_episode_id": "dc03b637c7b440e8a0c47abf75c8bcea",
      "latest_pub_date_ms": 1658912400000,
      "earliest_pub_date_ms": 1553519100785,
      "update_frequency_hours": 28,
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
      "total_episodes": 168,
      "listennotes_url": "https://www.listennotes.com/c/3a2a6ddd549f4df0b876e7315fa1a319/",
      "audio_length_sec": 1734,
      "explicit_content": false,
      "latest_episode_id": "225c072de1fb4e339a2110a981e50b17",
      "latest_pub_date_ms": 1657686675000,
      "earliest_pub_date_ms": 1370556600165,
      "update_frequency_hours": 654,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/espionage-parcast-network-X9AT-uYo8Nq-ReK0QUN-VP_.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/espionage-parcast-network-j-WLEmNQ4PB-ReK0QUN-VP_.300x300.jpg",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/formosa-files-lh-INvDesSm-EV8ID9SeJ1d.1400x1400.jpg",
      "title": " Formosa Files:\nThe History of Taiwan ",
      "country": "United States",
      "website": "https://www.formosafiles.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        125,
        67
      ],
      "itunes_id": 1588477096,
      "publisher": "John Ross and Eryk Michael Smith",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/formosa-files-qMZyeXN3uxL-EV8ID9SeJ1d.300x300.jpg",
      "is_claimed": false,
      "description": "The history of Taiwan (1600 C.E. - 2000) told through interesting stories in a non-chronological order. John Ross is an author and publisher of works on Taiwan and China, while Eryk Michael Smith has worked as a writer and journalist for several media outlets in Taiwan. Both hosts have lived in Taiwan for well over 20 years and call the island home. Email: formosafiles@gmail.com ",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 28,
      "total_episodes": 49,
      "listennotes_url": "https://www.listennotes.com/c/8579c3f5d11f479d939396b1f36f30a4/",
      "audio_length_sec": 1524,
      "explicit_content": false,
      "latest_episode_id": "148a5a63251d466caac99f3038d05a82",
      "latest_pub_date_ms": 1658288026000,
      "earliest_pub_date_ms": 1630893086048,
      "update_frequency_hours": 158,
      "listen_score_global_rank": "10%"
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/sports-card-investor-sports-card-investor-GmY_9vaPHMi-vZSFLzx3p10.1400x1400.jpg",
      "title": "Sports Card Investor",
      "country": "United States",
      "website": "https://www.sportscardinvestor.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        82,
        67
      ],
      "itunes_id": 1473711424,
      "publisher": "Sports Card Investor",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/sports-card-investor-sports-card-investor-1oWHa8cJfRk-vZSFLzx3p10.300x300.jpg",
      "is_claimed": false,
      "description": "Profit from the hobby you love. What are the best baseball, basketball and football cards to invest in today? How is the market trending? How can you profit? In each episode, we tackle these questions and more.\n\nSports Card Investor is brought to you by eBay, your number one spot for cards and collectibles. With the largest inventory of sports cards from basketball to soccer, and buyers from all over the globe, eBay is the leading place to buy, sell and invest your cards. Search eBay trading cards here: https://www.ebay.com/b/Trading-Cards/bn_7116496578",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 48,
      "total_episodes": 373,
      "listennotes_url": "https://www.listennotes.com/c/f46aac143841488b89c76923e5812846/",
      "audio_length_sec": 1368,
      "explicit_content": false,
      "latest_episode_id": "13f3e57546de4169a91e612e7400c4e2",
      "latest_pub_date_ms": 1658871013000,
      "earliest_pub_date_ms": 1563549867365,
      "update_frequency_hours": 113,
      "listen_score_global_rank": "1%"
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/already-gone-nina-innsted-B_G1zDt-Hlq-MoexDp6EKra.1400x1400.jpg",
      "title": "Already Gone",
      "country": "United States",
      "website": "https://alreadygonepodcast.com?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "language": "English",
      "genre_ids": [
        135,
        67,
        99,
        122
      ],
      "itunes_id": 1335405710,
      "publisher": "Nina Innsted",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/already-gone-nina-innsted-gKl825FPNk0-MoexDp6EKra.300x300.jpg",
      "is_claimed": false,
      "description": "<p>Great Lakes. True Crime. Host Nina Innsted covers lesser known crimes, digging beneath the media and back page to tell their stories and find the truth. #Michigan #Ohio #Pennsylvania #NewYork #Wisconsin #Illinois #TrueCrime&nbsp;</p>\n<p>Find me on Twitter: @Alreadygonepod (https://twitter.com/alreadygonepod) and Instagram https://www.instagram.com/ninainnsted/</p>",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": null,
      "total_episodes": 267,
      "listennotes_url": "https://www.listennotes.com/c/1c956b42302a488bbac0595e1922ea86/",
      "audio_length_sec": 1878,
      "explicit_content": false,
      "latest_episode_id": "a691d9c0831a44c1a70311a552f8b066",
      "latest_pub_date_ms": 1658765520000,
      "earliest_pub_date_ms": 1462730088191,
      "update_frequency_hours": 267,
      "listen_score_global_rank": null
    }
  ],
  "latest_episodes": [
    {
      "id": "9447ce07dd2345618054b04b733e4ad5",
      "link": "https://www.instagram.com/tboypod?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "audio": "https://www.listennotes.com/e/p/9447ce07dd2345618054b04b733e4ad5/",
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-Yw2Q5dIpK3A-kmx0XIZTAys.1400x1400.jpg",
      "title": "Google\u2019s $399 smartphone, Crocs\u2019 comeback, and GM\u2019s robotaxi Cruise snags $1B",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-Yw2Q5dIpK3A-kmx0XIZTAys.1400x1400.jpg",
        "title": "The Best One Yet",
        "publisher": "Nick & Jack Studios",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-KlIFOa-dpRW-kmx0XIZTAys.300x300.jpg",
        "listen_score": 73,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-KlIFOa-dpRW-kmx0XIZTAys.300x300.jpg",
      "description": "<p>Google\u2019s I/O event day enjoyed protests, AI tech to screen fake\u00a0calls, and a $399 Pixel phone. General Motors acquired self-driving car startup Cruise when it was worth $1B \u2014 Now it\u2019s worth $19B, and wants robotaxis on streets this year. And Crocs shares have nearly doubled in the past year, so we look at why.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1557309360754,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-Yw2Q5dIpK3A-kmx0XIZTAys.1400x1400.jpg",
      "title": "Big Trade War update, Apple\u2019s bought 20+ companies in 6 months, and the largest VC investment in Latin America ever",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-Yw2Q5dIpK3A-kmx0XIZTAys.1400x1400.jpg",
        "title": "The Best One Yet",
        "publisher": "Nick & Jack Studios",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-KlIFOa-dpRW-kmx0XIZTAys.300x300.jpg",
        "listen_score": 73,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-KlIFOa-dpRW-kmx0XIZTAys.300x300.jpg",
      "description": "<p>The Trade War was supposed to end this week with a peace\u00a0deal. That\u2019s not looking likely, and we\u2019ll tell you why. Apple\u2019s CEO casually dropped that the company\u2019s bought over 20 startups over the last six months. And super delivery app Rappi just raised $1B from Softbank, making it the biggest Latin American venture\u00a0investment ever.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1557222960755,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-MtJ2fOBSuTp-aZPn3Ic47rx.1400x1400.jpg",
      "title": "53: Something About Mary",
      "podcast": {
        "id": "68faf62be97149c280ebcc25178aa731",
        "image": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-MtJ2fOBSuTp-aZPn3Ic47rx.1400x1400.jpg",
        "title": "Business Unusual with Barbara Corcoran",
        "publisher": "Barbara Corcoran",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-x2LQVPknMsc-aZPn3Ic47rx.300x300.jpg",
        "listen_score": 58,
        "listennotes_url": "https://www.listennotes.com/c/68faf62be97149c280ebcc25178aa731/",
        "listen_score_global_rank": "0.5%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-x2LQVPknMsc-aZPn3Ic47rx.300x300.jpg",
      "description": "<p><strong>CNBC Producer Mary Hanan has the TV business dream job. I met Mary when she interviewed me for CNBC's \"The Brave Ones\" and I knew immediately I had to have her on the show. So I turned the tables on Mary and put her in the hot seat to learn how she worked her way up to the top, and she shared many of the interesting situations she found herself in along the way.Got a question for me? Call me at 888-BARBARA to ask a question for a future episode. Follow Business Unusual with Barbara Corcoran on iHeartRadio, or subscribe wherever you listen to podcasts. </strong>\u00a0<strong>This episode of Business Unusual with Barbara Corcoran is presented by OnDeck Business Loans (</strong><a href=\"https://urldefense.proofpoint.com/v2/url?u=http-3A__www.ondeck.com_Barbara&amp;d=DwMFaQ&amp;c=GC0NZZhaEw6GOQSjMHI2g15k_drElRoPmOYiK2k0eZ8&amp;r=xy9pRdG6lpZ6ogtRUMNvODnG4DdmLUxjZ2d9xbUZdbU5UshE20nENw68An-bhaS4&amp;m=b7G5z-S4fY6jYnVJoDD0IxLhdkIPrFOrNN2yLnt3Odc&amp;s=ecKEHfTJ9QtY2QfvkGL3kNIB-ZJ848-poG_hR6akhwQ&amp;e=\"><strong>http://www.ondeck.com/Barbara</strong></a><strong>)</strong></p>",
      "pub_date_ms": 1557201660097,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-Yw2Q5dIpK3A-kmx0XIZTAys.1400x1400.jpg",
      "title": "Warren Buffett\u2019s epic annual event, Planet Fitness\u2019 innovative real estate strategy, and almond milk vs. Dean Foods dairy",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-Yw2Q5dIpK3A-kmx0XIZTAys.1400x1400.jpg",
        "title": "The Best One Yet",
        "publisher": "Nick & Jack Studios",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-KlIFOa-dpRW-kmx0XIZTAys.300x300.jpg",
        "listen_score": 73,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-KlIFOa-dpRW-kmx0XIZTAys.300x300.jpg",
      "description": "<p>The annual Berkshire Hathaway shareholder meeting showcased\u00a088-year-old legendary investor Warren Buffett, so we broke down his 6 hours of one-liner business takeaways. Planet Fitness shares are up 75% in the last year, so we\u2019re focused on its innovative real estate strategy that feeds off the retail-pocalypse. And Dean Foods is America\u2019s biggest dairy company, but the stock is down 62% in 2019 because of alt-milk.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1557136560756,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/listen-money-matters-free-your-inner-lPXW7V_6n0C-SJEHNr84kVg.1400x1400.jpg",
      "title": "All Things Gold",
      "podcast": {
        "id": "3302bc71139541baa46ecb27dbf6071a",
        "image": "https://cdn-images-1.listennotes.com/podcasts/listen-money-matters-free-your-inner-lPXW7V_6n0C-SJEHNr84kVg.1400x1400.jpg",
        "title": "Listen Money Matters - Free your inner financial badass. All the stuff you should know about personal finance.",
        "publisher": "ListenMoneyMatters.com | Andrew Fiebert and Matt Giovanisci",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/listen-money-matters-free-your-inner-d5If074qkhz-SJEHNr84kVg.300x300.jpg",
        "listen_score": 66,
        "listennotes_url": "https://www.listennotes.com/c/3302bc71139541baa46ecb27dbf6071a/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/listen-money-matters-free-your-inner-d5If074qkhz-SJEHNr84kVg.300x300.jpg",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-Yw2Q5dIpK3A-kmx0XIZTAys.1400x1400.jpg",
      "title": "The Taser CEO gets $246M in stock comp, Beyond Meat surges 163%, and Wayfair drops 7% because you\u2019re expensive",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-Yw2Q5dIpK3A-kmx0XIZTAys.1400x1400.jpg",
        "title": "The Best One Yet",
        "publisher": "Nick & Jack Studios",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-KlIFOa-dpRW-kmx0XIZTAys.300x300.jpg",
        "listen_score": 73,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-KlIFOa-dpRW-kmx0XIZTAys.300x300.jpg",
      "description": "<p>Axon Enterprises is the company behind the taser, and it just awarded its CEO $246M in compensation \u2014 So we look in to how it\u2019s set up to incentivize him. Beyond Meat surged 163% on its IPO day. And Wayfair is the biggest online furniture platform whose stock fell 7%, but it\u2019s got a fascinating relationship with 80 \u201chouse brands.\u201d</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1556877360757,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/espionage-parcast-network-X9AT-uYo8Nq-ReK0QUN-VP_.1400x1400.jpg",
      "title": "Henri D\u00e9ricourt Pt. 2: Triple Agent",
      "podcast": {
        "id": "bacb2f7ca7a04ed0b21efd21192f5014",
        "image": "https://cdn-images-1.listennotes.com/podcasts/espionage-parcast-network-X9AT-uYo8Nq-ReK0QUN-VP_.1400x1400.jpg",
        "title": "Espionage",
        "publisher": "Parcast Network",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/espionage-parcast-network-j-WLEmNQ4PB-ReK0QUN-VP_.300x300.jpg",
        "listen_score": 64,
        "listennotes_url": "https://www.listennotes.com/c/bacb2f7ca7a04ed0b21efd21192f5014/",
        "listen_score_global_rank": "0.1%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/espionage-parcast-network-j-WLEmNQ4PB-ReK0QUN-VP_.300x300.jpg",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-Yw2Q5dIpK3A-kmx0XIZTAys.1400x1400.jpg",
      "title": "Molson Coors falls 8% on mid-beer crisis, Royal Caribbean becomes pricing power superhero, and Fitbit is our \u201cSurvivor of the Day\u201d",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-Yw2Q5dIpK3A-kmx0XIZTAys.1400x1400.jpg",
        "title": "The Best One Yet",
        "publisher": "Nick & Jack Studios",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-KlIFOa-dpRW-kmx0XIZTAys.300x300.jpg",
        "listen_score": 73,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-KlIFOa-dpRW-kmx0XIZTAys.300x300.jpg",
      "description": "<p>With beer sales slowing, Molson Coors is desperately\u00a0focused on innovation (aka non-alcohol drinks), but shares fell because of its beer battles. Fitbit used to be profitable, now it\u2019s using partnerships to survive. And Royal Caribbean jumped 7% as it realizes it can charge a lot more for cruises.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1556790960758,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-Yw2Q5dIpK3A-kmx0XIZTAys.1400x1400.jpg",
      "title": "Facebook\u2019s new \u201cFB5\u201d redesign (and dating feature), Apple\u2019s past-dependent business model, and Merck\u2019s profits quadruple",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-Yw2Q5dIpK3A-kmx0XIZTAys.1400x1400.jpg",
        "title": "The Best One Yet",
        "publisher": "Nick & Jack Studios",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-KlIFOa-dpRW-kmx0XIZTAys.300x300.jpg",
        "listen_score": 73,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-KlIFOa-dpRW-kmx0XIZTAys.300x300.jpg",
      "description": "<p>Apple\u2019s earnings report was critical for what it didn\u2019t say, just as much as what it did \u2014 And it reveals that Apple\u2019s transformation. Facebook\u2019s F8 event revealed new features (dating and crushes), but the big focus was its app redesign. And Merck\u2019s profits quadrupled because a measles vaccine and a new cancer drug have become its profit puppies.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1556704560759,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/already-gone-nina-innsted-B_G1zDt-Hlq-MoexDp6EKra.1400x1400.jpg",
      "title": "The Mother's Day Murders",
      "podcast": {
        "id": "1c956b42302a488bbac0595e1922ea86",
        "image": "https://cdn-images-1.listennotes.com/podcasts/already-gone-nina-innsted-B_G1zDt-Hlq-MoexDp6EKra.1400x1400.jpg",
        "title": "Already Gone",
        "publisher": "Nina Innsted",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/already-gone-nina-innsted-gKl825FPNk0-MoexDp6EKra.300x300.jpg",
        "listen_score": null,
        "listennotes_url": "https://www.listennotes.com/c/1c956b42302a488bbac0595e1922ea86/",
        "listen_score_global_rank": null
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/already-gone-nina-innsted-gKl825FPNk0-MoexDp6EKra.300x300.jpg",
      "description": "<p>Mother's Day 1982, high school students David Cole and Timothy Fowler die in a fiery blaze at the Cole home in Deerfield Michigan. This episode features an interview with the sister of Tim Fowler.&nbsp; <a href=\"https://www.facebook.com/timfowlerdavidcole/\">https://www.facebook.com/timfowlerdavidcole/</a><br /><br />If you have information on this unsolved case, please contact the Lenawee County Sheriff's Department at <strong>517-266-6161 </strong>or, submit an anonymous tip via CrimeStoppers, Online at:&nbsp;<a href=\"http://www.tipsubmit.com\">www.tipsubmit.com</a> or via text &nbsp;274637 Start Tip \"LENAWEE\"</p>\n<p><br />Visit our sponsor! Green Chef - For $50 off your first box of Green Chef visit Greenchef.US/alreadygone <br /><strong><br /></strong>Additional Music provided by RFM: <a href=\"https://www.youtube.com/watch?v=dPEoasBHNiA\">https://youtu.be/dPEoasBHNiA</a><strong><br /></strong></p><p><a href=\"https://www.patreon.com/AlreadyGone\" rel=\"payment\">Support the show: https://www.patreon.com/AlreadyGone</a></p><p>See <a href=\"https://omnystudio.com/listener\">omnystudio.com/listener</a> for privacy information.</p>",
      "pub_date_ms": 1556683500082,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-Yw2Q5dIpK3A-kmx0XIZTAys.1400x1400.jpg",
      "title": "Spotify hits 217M profitless users, Airbnb & Marriott\u2019s twin announcements, and Chewy.com\u2019s \u201cpet humanization\u201d IPO",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-Yw2Q5dIpK3A-kmx0XIZTAys.1400x1400.jpg",
        "title": "The Best One Yet",
        "publisher": "Nick & Jack Studios",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-KlIFOa-dpRW-kmx0XIZTAys.300x300.jpg",
        "listen_score": 73,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-KlIFOa-dpRW-kmx0XIZTAys.300x300.jpg",
      "description": "<p>Spotify now boasts 100M paying subscribers, so we looked\u00a0into why it\u2019s still losing so much money (hint: It\u2019s betting on podcasts). Airbnb and Marriott both revealed new services that look a lot like each other (awkward). And PetSmart\u2019s digital brand Chewy.com will IPO thanks to \u201cpet humanization\u201d trends.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1556618160760,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-MtJ2fOBSuTp-aZPn3Ic47rx.1400x1400.jpg",
      "title": "52: What I Learned From Bad Bosses",
      "podcast": {
        "id": "68faf62be97149c280ebcc25178aa731",
        "image": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-MtJ2fOBSuTp-aZPn3Ic47rx.1400x1400.jpg",
        "title": "Business Unusual with Barbara Corcoran",
        "publisher": "Barbara Corcoran",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-x2LQVPknMsc-aZPn3Ic47rx.300x300.jpg",
        "listen_score": 58,
        "listennotes_url": "https://www.listennotes.com/c/68faf62be97149c280ebcc25178aa731/",
        "listen_score_global_rank": "0.5%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/business-unusual-with-barbara-corcoran-x2LQVPknMsc-aZPn3Ic47rx.300x300.jpg",
      "description": "<p><strong>I had 23 bosses before starting my business and I know that a bad one is sure to kill your confidence. So what do you do when you don't see eye to eye? I answer your questions about dealing with a bad boss and becoming a better leader. </strong>\u00a0<strong>Want to hear your question on Business Unusual? Call me at 888-BARBARA or tweet at @barbaracorcoran to ask a question for a future episode. Follow Business Unusual with Barbara Corcoran on iHeartRadio, or subscribe wherever you listen to podcasts. </strong>\u00a0<strong>This episode of Business Unusual with Barbara Corcoran is presented by OnDeck Business Loans (</strong><a href=\"https://urldefense.proofpoint.com/v2/url?u=http-3A__www.ondeck.com_Barbara&amp;d=DwMFaQ&amp;c=GC0NZZhaEw6GOQSjMHI2g15k_drElRoPmOYiK2k0eZ8&amp;r=xy9pRdG6lpZ6ogtRUMNvODnG4DdmLUxjZ2d9xbUZdbU5UshE20nENw68An-bhaS4&amp;m=iyzCy3KkByFDhAZKPNnXfRZDwVi9wa4vgtkjqAegOYo&amp;s=AR-0E6fCOSktW28rNgQpCe-kEyu1odFgovlqPFyavSA&amp;e=\"><strong>http://www.ondeck.com/Barbara</strong></a><strong>)</strong>\u00a0</p>",
      "pub_date_ms": 1556596860098,
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
      "pub_date_ms": 1556594432036,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-Yw2Q5dIpK3A-kmx0XIZTAys.1400x1400.jpg",
      "title": "Beyond Meat boots its meat-focused investor, Comcast (shockingly) hits record high, and one startup\u2019s worst 1st week",
      "podcast": {
        "id": "c5ce6c02cbf1486496206829f7d42e8e",
        "image": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-Yw2Q5dIpK3A-kmx0XIZTAys.1400x1400.jpg",
        "title": "The Best One Yet",
        "publisher": "Nick & Jack Studios",
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-KlIFOa-dpRW-kmx0XIZTAys.300x300.jpg",
        "listen_score": 73,
        "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
        "listen_score_global_rank": "0.05%"
      },
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-KlIFOa-dpRW-kmx0XIZTAys.300x300.jpg",
      "description": "<p>Plant-based meat innovator Beyond Meat had an awkward investor: The world\u2019s 2nd biggest meat producer, Tyson Foods -- So Beyond Meat kicked it out before its upcoming IPO. Old school cable throwback Comcast is winning even though you cut the cord. And Luminary was supposed to be the future of podcasting, but its 1st week went really badly.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
      "pub_date_ms": 1556531760761,
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

See all available parameters on the [API Docs page](https://www.listennotes.com/podcast-api/docs/#get-api-v2-just_listen).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "id": "a62a0cb1b27b452190a2db339da56d41",
  "link": "https://abzfootballpodcast.podbean.com/e/ep54-raith-rovers-review-celtic-preview-abzfp-season-2223-predictor/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
  "audio": "https://www.listennotes.com/e/p/a62a0cb1b27b452190a2db339da56d41/",
  "image": "https://cdn-images-1.listennotes.com/podcasts/the-abz-football-podcast-bBS4Pk62_RO-R6-zb9vskMh.1400x1400.jpg",
  "title": "EP54: Raith Rovers Review / Celtic Preview / ABZFP Season 22/23 Predictor",
  "podcast": {
    "id": "976cbeed9b03489394377668480586dd",
    "image": "https://cdn-images-1.listennotes.com/podcasts/the-abz-football-podcast-bBS4Pk62_RO-R6-zb9vskMh.1400x1400.jpg",
    "title": "The ABZ Football Podcast",
    "publisher": "The ABZ Football Podcast",
    "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-abz-football-podcast-N4QzpeI3oit-R6-zb9vskMh.300x300.jpg",
    "listen_score": 29,
    "listennotes_url": "https://www.listennotes.com/c/976cbeed9b03489394377668480586dd/",
    "listen_score_global_rank": "10%"
  },
  "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-abz-football-podcast-N4QzpeI3oit-R6-zb9vskMh.300x300.jpg",
  "description": "<p style=\"text-align: justify;\">It's Wednesday and you know what that means!</p>\n<p style=\"text-align: justify;\">\u00a0</p>\n<p style=\"text-align: justify;\">Welcome to Episode 54 of the ABZ Football Podcast as Gary (<a href=\"https://twitter.com/tchocky83?s=20&amp;t=E_fLuWHRSLQTKBtUZ5nO2w\">@tchocky83</a>), Gavin (<a href=\"https://twitter.com/TheRogue87\">@TheRogue87</a>) and a well-rested, returning Graham Steele look back over Sunday's 3-0 win over Raith Rovers to round off our Premier Sports Cup Group Stage escapades.</p>\n<p style=\"text-align: justify;\">\u00a0</p>\n<p style=\"text-align: justify;\">We then take our regular look at all of the news coming out of AB24 in the last week (beautifully recorded prior to the news that the Dons had signed Cal Roberts (see EP53.95) and Hayden Coulson (see EP54.25)).</p>\n<p style=\"text-align: justify;\">\u00a0</p>\n<p style=\"text-align: justify;\">After the break, we turn our attention to the return of the cinch as the SPFL Premiership kicks off this coming weekend and we preview our trip to Celtic Park and ask if we can catch the champions cold and ruin flag day before we put our expert footballing knowledge to the test as we bring you our very own 22/23 season predictions!</p>\n<p style=\"text-align: justify;\">\u00a0</p>\n<p style=\"text-align: justify;\">Like what we do?\u00a0 Keep us fueled for future episodes by buying us a beer or coffee over at - <a href=\"https://ko-fi.com/abzfootballpodcast\">https://ko-fi.com/abzfootballpodcast</a>!</p>\n<p style=\"text-align: justify;\">\u00a0</p>\n<p style=\"text-align: justify;\">Support our Aberdeen to Gothenburg challenge by visiting:- <a href=\"http://www.justgiving.com/crowdfunding/abzfootballpodcast\">ABZFP Aberdeen to Gothenburg Challenge</a></p>\n<p style=\"text-align: justify;\">\u00a0</p>\n<p style=\"text-align: justify;\">Want to enter our latest fundraising raffle where you can win either (1) Hospitality for 4 in the Teddy Scott Lounge for a home game of your choosing this season* or (2) A signed 22/23 AFC shirt?\u00a0 Simply e-mail <a href=\"mailto:abzfootballpodcast@gmail.com\">abzfootballpodcast@gmail.com</a> to enter.</p>\n<p style=\"text-align: justify;\">\u00a0</p>\n<p style=\"text-align: justify;\">Follow the us on our social media channels:-</p>\n<p style=\"text-align: justify;\">\u00a0</p>\n<p style=\"text-align: justify;\">Twitter - <a href=\"https://twitter.com/AbzPodcast?s=20&amp;t=xF7KGq1lZEV2lJonPxKwjA\">@AbzPodcast</a></p>\n<p style=\"text-align: justify;\">Facebook - <a href=\"https://www.facebook.com/ABZFootballPodcast\">@ABZFootballPodcast</a></p>\n<p style=\"text-align: justify;\">Instagram - <a href=\"https://www.instagram.com/abzfootballpodcast/\">@abzfootballpodcast</a></p>",
  "pub_date_ms": 1658899500000,
  "guid_from_rss": "abzfootballpodcast.podbean.com/cd3208f0-44db-31a1-8a51-ddb1868da02c",
  "listennotes_url": "https://www.listennotes.com/e/a62a0cb1b27b452190a2db339da56d41/",
  "audio_length_sec": 6400,
  "explicit_content": true,
  "maybe_audio_invalid": false,
  "listennotes_edit_url": "https://www.listennotes.com/e/a62a0cb1b27b452190a2db339da56d41/#edit"
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

See all available parameters on the [API Docs page](https://www.listennotes.com/podcast-api/docs/#get-api-v2-curated_podcasts-id).


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
        "amazon_music_url": "",
        "instagram_handle": "maedinindia"
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/maed-in-india-maed-in-india-7fgzAQsCRmy-y2oQTwMN73p.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/maed-in-india-maed-in-india-p9P2YIfeQl3-y2oQTwMN73p.300x300.jpg",
      "is_claimed": true,
      "description": "Maed in India - India's first indie music podcast that showcases the best Indian independent musicians from India and abroad. Each episode presents an interview with an artist/band along with an exclusive stripped down session or acoustic renditions of their original music. The weekly show prides itself on being the destination for new music, little known stories, and unreleased music never heard before.\n\nIt features all kinds of artists from new-comers to veterans and under a variety of genres from hip hop, blues, soul, to folk, punk, rock, and everything in between.",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 45,
      "total_episodes": 296,
      "listennotes_url": "https://www.listennotes.com/c/c463d5980b8e480fb78db6b3ed6be115/",
      "audio_length_sec": 3087,
      "explicit_content": false,
      "latest_episode_id": "d7f8ac0272334c7689cfb9f34f1e5a36",
      "latest_pub_date_ms": 1658093426000,
      "earliest_pub_date_ms": 1434346200284,
      "update_frequency_hours": 168,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-intersection-the-intersection-is1CILODdqm-LTmzMb05tFB.150x150.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-intersection-the-intersection-is1CILODdqm-LTmzMb05tFB.150x150.jpg",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/trial-by-error-the-aarushi-files-arre-HW5-PMrpJ6g--hleb0zIEPC.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/trial-by-error-the-aarushi-files-arre-PdHUYLlQq1T--hleb0zIEPC.300x300.jpg",
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
      "audio_length_sec": 1276,
      "explicit_content": false,
      "latest_episode_id": "7d084c19d0184e30ade557a74af585fa",
      "latest_pub_date_ms": 1468183671000,
      "earliest_pub_date_ms": 1462135535000,
      "update_frequency_hours": 100,
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
        "amazon_music_url": "",
        "instagram_handle": ""
      },
      "image": "https://cdn-images-1.listennotes.com/podcasts/adventures-of-cheap-beer-adventures-of-_JAB4btwguP-vkZfSh-TJCt.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/adventures-of-cheap-beer-adventures-of-tszxiBTflqc-vkZfSh-TJCt.300x300.jpg",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/syntalk-syntalk-O_8qKgy0eWd-j2nFBUVDzq_.1006x1006.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/syntalk-syntalk-AscbMPzh92d-j2nFBUVDzq_.300x300.jpg",
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
      "audio_length_sec": 4059,
      "explicit_content": false,
      "latest_episode_id": "09d454a5e9a24e7f8c21c657d84479d9",
      "latest_pub_date_ms": 1626048000000,
      "earliest_pub_date_ms": 1405191856171,
      "update_frequency_hours": 469,
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/the-indian-startup-show-neil-patel-QWdjyCBTwPr-9574y1CKU8j.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-indian-startup-show-neil-patel-etrHT24KoXq-9574y1CKU8j.300x300.jpg",
      "is_claimed": false,
      "description": "A Weekly Podcast Show About Indian Startups\nEntrepreneurs & More !\nHosted by Neil Patel & Friends",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 42,
      "total_episodes": 193,
      "listennotes_url": "https://www.listennotes.com/c/24ece1d0922d4d9a9659e9e6cb2b241e/",
      "audio_length_sec": 2241,
      "explicit_content": false,
      "latest_episode_id": "ce150cc765254d1898b0cb2d7dd85cf9",
      "latest_pub_date_ms": 1658271600000,
      "earliest_pub_date_ms": 1439366880191,
      "update_frequency_hours": 442,
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
      "rss": "https://static.adorilabs.com/feed/cyrus-says.xml",
      "type": "episodic",
      "email": "ivmshows@pratilipi.com",
      "extra": {
        "url1": "",
        "url2": "",
        "url3": "",
        "google_url": "https://podcasts.google.com/feed/aHR0cHM6Ly9zdGF0aWMuYWRvcmlsYWJzLmNvbS9mZWVkL2N5cnVzLXNheXMueG1s",
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
      "image": "https://cdn-images-1.listennotes.com/podcasts/cyrus-says-ivm-podcasts-bH2WSyT4-gM-1q2UDTO6ztZ.1400x1400.jpg",
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
      "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/cyrus-says-ivm-podcasts-BHSw4MVEzfg-1q2UDTO6ztZ.300x300.jpg",
      "is_claimed": true,
      "description": "<p>Broadcasting through the week with a rotating panel of guests, Cyrus Says is the definitive show on life in urban India, politics, sports, civic sense, traffic, kids, food, and everything that matters. Mostly.</p>",
      "looking_for": {
        "guests": false,
        "cohosts": false,
        "sponsors": false,
        "cross_promotion": false
      },
      "listen_score": 53,
      "total_episodes": 1011,
      "listennotes_url": "https://www.listennotes.com/c/2641ed2ce5524b3da43b8f19fe0f5ae9/",
      "audio_length_sec": 3146,
      "explicit_content": false,
      "latest_episode_id": "0deec1f1a0914687bba8ca0c3ed84e3e",
      "latest_pub_date_ms": 1658968503000,
      "earliest_pub_date_ms": 1426829401006,
      "update_frequency_hours": 29,
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
        "amazon_music_url": "",
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
        "amazon_music_url": "",
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
      "listen_score": 37,
      "total_episodes": 45,
      "listennotes_url": "https://www.listennotes.com/c/d203864a67fb43b1a98b7107cabeaa4b/",
      "audio_length_sec": 1259,
      "explicit_content": false,
      "latest_episode_id": "75a2ece4538149e3bda45a163059496d",
      "latest_pub_date_ms": 1579417200000,
      "earliest_pub_date_ms": 1431062738044,
      "update_frequency_hours": 343,
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
      "listen_score": 58,
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

See all available parameters on the [API Docs page](https://www.listennotes.com/podcast-api/docs/#get-api-v2-curated_podcasts).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "total": 4130,
  "has_next": true,
  "page_number": 2,
  "has_previous": true,
  "curated_lists": [
    {
      "id": "AcewQx6MbYg",
      "title": "7 tech podcasts to binge this summer",
      "total": 7,
      "podcasts": [
        {
          "id": "13ac66dc943a4a28b8bced71e5a64690",
          "image": "https://cdn-images-1.listennotes.com/podcasts/oxycast-ZcfrHjghV7y-dhsobHiWpRv.1400x1400.jpg",
          "title": "OxyCast",
          "publisher": "Oxylabs",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/oxycast-HpML2u4hjTo-dhsobHiWpRv.300x300.jpg",
          "listen_score": null,
          "listennotes_url": "https://www.listennotes.com/c/13ac66dc943a4a28b8bced71e5a64690/",
          "listen_score_global_rank": null
        },
        {
          "id": "f9d5885d7cf7485d891e82dea3186640",
          "image": "https://cdn-images-1.listennotes.com/podcasts/how-i-built-this-with-guy-raz-guy-raz-wondery-7krpVtcCzMB-UC0qH23iP9T.1400x1400.jpg",
          "title": "How I Built This with Guy Raz",
          "publisher": "Guy Raz | Wondery",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/how-i-built-this-with-guy-raz-guy-raz-wondery--t38KFIqlAi-UC0qH23iP9T.300x300.jpg",
          "listen_score": 85,
          "listennotes_url": "https://www.listennotes.com/c/f9d5885d7cf7485d891e82dea3186640/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "6687dafe753b4c9baee7a4d3f1df6431",
          "image": "https://cdn-images-1.listennotes.com/podcasts/thoughtworks-technology-podcast-thoughtworks-T80k9-4qv_K-lc7g2BxjK6q.1400x1400.jpg",
          "title": "Thoughtworks Technology Podcast",
          "publisher": "Thoughtworks",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/thoughtworks-technology-podcast-thoughtworks-nfAa2mLywoZ-lc7g2BxjK6q.300x300.jpg",
          "listen_score": 40,
          "listennotes_url": "https://www.listennotes.com/c/6687dafe753b4c9baee7a4d3f1df6431/",
          "listen_score_global_rank": "2%"
        },
        {
          "id": "b586d7de2a8e49b687fa5ab8506f713c",
          "image": "https://cdn-images-1.listennotes.com/podcasts/in-machines-we-trust-mit-technology-review-2XrNhCFYELg-HBIyhzYn8qF.1400x1400.jpg",
          "title": "In Machines We Trust",
          "publisher": "MIT Technology Review",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/in-machines-we-trust-mit-technology-review-vS40qpJzUIZ-HBIyhzYn8qF.300x300.jpg",
          "listen_score": 50,
          "listennotes_url": "https://www.listennotes.com/c/b586d7de2a8e49b687fa5ab8506f713c/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "d863da7f921e435fb35f512b54e774d6",
          "image": "https://cdn-images-1.listennotes.com/podcasts/masters-of-scale-with-reid-hoffman-waitwhat-PJGeHLMmxa6-mYoV0CUyxTD.1400x1400.jpg",
          "title": "Masters of Scale",
          "publisher": "WaitWhat ",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/masters-of-scale-with-reid-hoffman-waitwhat-XJs3WwmUrx7-mYoV0CUyxTD.300x300.jpg",
          "listen_score": 73,
          "listennotes_url": "https://www.listennotes.com/c/d863da7f921e435fb35f512b54e774d6/",
          "listen_score_global_rank": "0.05%"
        }
      ],
      "source_url": "https://thenextweb.com/news/7-tech-podcasts-binge-2022?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"These tech podcasts feature the brightest minds in programming, science, and engineering.\"",
      "pub_date_ms": 1657820361034,
      "source_domain": "thenextweb.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/7-tech-podcasts-to-binge-this-summer-AcewQx6MbYg/"
    },
    {
      "id": "h0gIMarSc7U",
      "title": "Cults, reality TV, and tigers: Nine of the best podcasts to listen to this summer",
      "total": 9,
      "podcasts": [
        {
          "id": "bf6bcdfc5f90498fac6a6694783e44f7",
          "image": "https://cdn-images-1.listennotes.com/podcasts/unreal-a-critical-history-of-reality-tv-Brbf5RF2tPa-IunKEjXVOUq.1400x1400.jpg",
          "title": "Unreal: A Critical History of Reality TV",
          "publisher": "BBC Radio 4",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/unreal-a-critical-history-of-reality-tv-Q5_-pdMGFfU-IunKEjXVOUq.300x300.jpg",
          "listen_score": 47,
          "listennotes_url": "https://www.listennotes.com/c/bf6bcdfc5f90498fac6a6694783e44f7/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "b02bb74838be4d06ac28db8b520e65c8",
          "image": "https://cdn-images-1.listennotes.com/podcasts/wild-things-siegfried-roy-5ugdctE1WG0-qIfvadzkOp_.1400x1400.jpg",
          "title": "Wild Things: Siegfried & Roy",
          "publisher": "Apple TV+ / AT WILL MEDIA",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/wild-things-siegfried-roy-fSPX5aAeVKi-qIfvadzkOp_.300x300.jpg",
          "listen_score": 58,
          "listennotes_url": "https://www.listennotes.com/c/b02bb74838be4d06ac28db8b520e65c8/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "529bc03c537e477495544f7ae747e5d7",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-antidote-071y4aKvgdJ-uCtT_s0Nq7D.1400x1400.jpg",
          "title": "The Antidote",
          "publisher": "American Public Media",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-antidote-ngd-mfztyas-uCtT_s0Nq7D.300x300.jpg",
          "listen_score": 47,
          "listennotes_url": "https://www.listennotes.com/c/529bc03c537e477495544f7ae747e5d7/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "643ecdeabea748aa88e75f56a8950be0",
          "image": "https://cdn-images-1.listennotes.com/podcasts/rob-beckett-and-josh-widdicombes-parenting-cQWolsRDLJ0-yrwdC_s2iQP.1400x1400.jpg",
          "title": "Rob Beckett and Josh Widdicombe's Parenting Hell",
          "publisher": "Keep It Light Media",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/rob-beckett-and-josh-widdicombes-parenting-kQCfeG9pl0u-yrwdC_s2iQP.300x300.jpg",
          "listen_score": 76,
          "listennotes_url": "https://www.listennotes.com/c/643ecdeabea748aa88e75f56a8950be0/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "75bd6a6a4dc246f8a2066ff8342bb399",
          "image": "https://cdn-images-1.listennotes.com/podcasts/dead-eyes-headgum-6yQO5dTJZRE-iz08Qb9CcvT.1400x1400.jpg",
          "title": "Dead Eyes",
          "publisher": "Headgum",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/dead-eyes-headgum-qL3DQZrmWE1-iz08Qb9CcvT.300x300.jpg",
          "listen_score": 63,
          "listennotes_url": "https://www.listennotes.com/c/75bd6a6a4dc246f8a2066ff8342bb399/",
          "listen_score_global_rank": "0.1%"
        }
      ],
      "source_url": "https://www.euronews.com/culture/2022/07/11/cults-reality-tv-and-tigers-nine-of-the-best-podcasts-to-listen-to-this-summer?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"But whether you\u2019re sunbathing on vacation or trapped in the office, there\u2019s a podcast to soundtrack your summer. Here are the nine of the best, compiled by the Euronews Culture team.\"",
      "pub_date_ms": 1657754706056,
      "source_domain": "www.euronews.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/cults-reality-tv-and-tigers-nine-of-h0gIMarSc7U/"
    },
    {
      "id": "axM1gbmtCpX",
      "title": "6 of the Best Podcasts About Radical American Movements",
      "total": 6,
      "podcasts": [
        {
          "id": "c444aa2396e742f0bea54ed0cdd3cbbe",
          "image": "https://cdn-images-1.listennotes.com/podcasts/mother-country-radicals-CF9chtrSsiH-vj_uCpD5K4A.1400x1400.jpg",
          "title": "Mother Country Radicals",
          "publisher": "Crooked Media",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/mother-country-radicals-JavbOuiqC1R-vj_uCpD5K4A.300x300.jpg",
          "listen_score": 52,
          "listennotes_url": "https://www.listennotes.com/c/c444aa2396e742f0bea54ed0cdd3cbbe/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "4e77bef5a6174beb8264e0017f809474",
          "image": "https://cdn-images-1.listennotes.com/podcasts/cool-people-who-did-cool-stuff-bXqNhFsr_5m-KUQF_uk5eVx.1400x1400.jpg",
          "title": "Cool People Who Did Cool Stuff",
          "publisher": "iHeartPodcasts and Cool Zone Media",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/cool-people-who-did-cool-stuff-I8N4efV5k2F-KUQF_uk5eVx.300x300.jpg",
          "listen_score": 46,
          "listennotes_url": "https://www.listennotes.com/c/4e77bef5a6174beb8264e0017f809474/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "d620156577fe4408972a29aa2675e628",
          "image": "https://cdn-images-1.listennotes.com/podcasts/american-radical-msnbc-Pl6VZSsQpCw-ZscLB0wq5_7.1400x1400.jpg",
          "title": "American Radical",
          "publisher": "MSNBC",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/american-radical-msnbc-GZeyAVmb0LX-ZscLB0wq5_7.300x300.jpg",
          "listen_score": 67,
          "listennotes_url": "https://www.listennotes.com/c/d620156577fe4408972a29aa2675e628/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "2c35e716fd6b4c0c8de0e661f4638933",
          "image": "https://cdn-images-1.listennotes.com/podcasts/will-be-wild-YZXKslxW0Pv-bP62LCJYxKc.1400x1400.jpg",
          "title": "Will Be Wild",
          "publisher": "Pineapple Street Studios | Wondery | Amazon Music ",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/will-be-wild-fxk9tMDb7g0-bP62LCJYxKc.300x300.jpg",
          "listen_score": 61,
          "listennotes_url": "https://www.listennotes.com/c/2c35e716fd6b4c0c8de0e661f4638933/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "7325987bf997478180d92556b4d5db10",
          "image": "https://cdn-images-1.listennotes.com/podcasts/imperfect-paradise-laist-studios-m3-aGWyvZoi-2uxcmvje7ZP.1400x1400.jpg",
          "title": "Imperfect Paradise",
          "publisher": "LAist Studios",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/imperfect-paradise-laist-studios-E9Hi1JtcNx3-2uxcmvje7ZP.300x300.jpg",
          "listen_score": 44,
          "listennotes_url": "https://www.listennotes.com/c/7325987bf997478180d92556b4d5db10/",
          "listen_score_global_rank": "1.5%"
        }
      ],
      "source_url": "https://www.lifehacker.com.au/2022/07/6-of-the-best-podcasts-about-radical-american-movements/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"As the United States enters a new era of even more divisive politics, looking to the past can help us find a way forward. Here are 6 recent podcasts that take us through the history of radical groups, searching for answers in their unearthing of obscured history. Most are told in the voices of the people closest to the events being documented.\"",
      "pub_date_ms": 1657754523074,
      "source_domain": "www.lifehacker.com.au",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/6-of-the-best-podcasts-about-radical-axM1gbmtCpX/"
    },
    {
      "id": "XlZUJGdK0oO",
      "title": "8 Faculty Members Recommend Their Favorite Podcasts",
      "total": 10,
      "podcasts": [
        {
          "id": "b63bc0ae41c742a58b6f43f133ef6019",
          "image": "https://cdn-images-1.listennotes.com/podcasts/two-guys-on-your-head-kut-kutx-studios-dr-IidTJAUkcE_-rWjEcLz2nYs.1400x1400.jpg",
          "title": "Two Guys on Your Head",
          "publisher": "KUT & KUTX Studios, Dr. Art Markman & Dr. Bob Duke",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/two-guys-on-your-head-kut-kutx-studios-dr-gq1Z8SIOEVj-rWjEcLz2nYs.300x300.jpg",
          "listen_score": 47,
          "listennotes_url": "https://www.listennotes.com/c/b63bc0ae41c742a58b6f43f133ef6019/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "eb5661f5be5b4994ade0b8bacbdd62f6",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-age-of-napoleon-podcast-everett-rummage-7M6UX3COo2d-xlNBH-s0ULJ.1400x1400.jpg",
          "title": "The Age of Napoleon Podcast",
          "publisher": "Everett Rummage",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-age-of-napoleon-podcast-everett-rummage-vPc8j6nJSsg-xlNBH-s0ULJ.300x300.jpg",
          "listen_score": 63,
          "listennotes_url": "https://www.listennotes.com/c/eb5661f5be5b4994ade0b8bacbdd62f6/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "66f2fc83fc6b411fa556928a6309a2f0",
          "image": "https://cdn-images-1.listennotes.com/podcasts/know-your-enemy-matthew-sitman-mlevuFOC907-BrzUGaeiHEX.1400x1400.jpg",
          "title": "Know Your Enemy",
          "publisher": "Matthew Sitman ",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/know-your-enemy-matthew-sitman-dkhFL8XPcfI-BrzUGaeiHEX.300x300.jpg",
          "listen_score": 60,
          "listennotes_url": "https://www.listennotes.com/c/66f2fc83fc6b411fa556928a6309a2f0/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "cd32dce10ca24ab89e977ceb5f78dc97",
          "image": "https://cdn-images-1.listennotes.com/podcasts/culture-happens-hubspot-tdQXOcI6mUJ-Jneg5HDGs9u.1400x1400.jpg",
          "title": "Culture Happens",
          "publisher": "HubSpot",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/culture-happens-hubspot-nTv4lVxBdmP-Jneg5HDGs9u.300x300.jpg",
          "listen_score": 36,
          "listennotes_url": "https://www.listennotes.com/c/cd32dce10ca24ab89e977ceb5f78dc97/",
          "listen_score_global_rank": "3%"
        },
        {
          "id": "f925b390147a47519f91a9c1381a1560",
          "image": "https://cdn-images-1.listennotes.com/podcasts/make-it-thrive-the-company-culture-podcast-R5qlA2QmFLH-QgP0-djr9hS.1400x1400.jpg",
          "title": "Make It Thrive: The Company Culture Podcast",
          "publisher": "Lizzie Benton",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/make-it-thrive-the-company-culture-podcast-yh2ndH6xGER-QgP0-djr9hS.300x300.jpg",
          "listen_score": null,
          "listennotes_url": "https://www.listennotes.com/c/f925b390147a47519f91a9c1381a1560/",
          "listen_score_global_rank": null
        }
      ],
      "source_url": "https://www.gsb.stanford.edu/insights/8-faculty-members-recommend-their-favorite-podcasts?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"Maybe you\u2019re taking a long-awaited road trip and need something to pass the time. Or perhaps you\u2019re opting for a staycation and want something to listen to as you relax at home. As summer kicks off and schedules (hopefully) slow down, we asked Stanford GSB faculty members to recommend shows they listen to in their free time.\"",
      "pub_date_ms": 1657642890430,
      "source_domain": "www.gsb.stanford.edu",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/8-faculty-members-recommend-their-XlZUJGdK0oO/"
    },
    {
      "id": "LnF8skAUHb_",
      "title": "The 9 best business podcasts",
      "total": 9,
      "podcasts": [
        {
          "id": "f9d5885d7cf7485d891e82dea3186640",
          "image": "https://cdn-images-1.listennotes.com/podcasts/how-i-built-this-with-guy-raz-guy-raz-wondery-7krpVtcCzMB-UC0qH23iP9T.1400x1400.jpg",
          "title": "How I Built This with Guy Raz",
          "publisher": "Guy Raz | Wondery",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/how-i-built-this-with-guy-raz-guy-raz-wondery--t38KFIqlAi-UC0qH23iP9T.300x300.jpg",
          "listen_score": 85,
          "listennotes_url": "https://www.listennotes.com/c/f9d5885d7cf7485d891e82dea3186640/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "a6848cf9cd7e449689768836b34bf106",
          "image": "https://cdn-images-1.listennotes.com/podcasts/world-business-report-bbc-world-service-Txft_dobeZF-ajpWzVh_yYE.1400x1400.jpg",
          "title": "World Business Report",
          "publisher": "BBC",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/world-business-report-bbc-world-service-hHGou8aq2Nl-ajpWzVh_yYE.300x300.jpg",
          "listen_score": 54,
          "listennotes_url": "https://www.listennotes.com/c/a6848cf9cd7e449689768836b34bf106/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "fc131f1086ee4eadb3fd9ea968fcf307",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-introvert-entrepreneur-beth-buelow-the-qr6CYFNA02W.1400x1400.jpg",
          "title": "The Introvert Entrepreneur",
          "publisher": "Beth Buelow, The Introvert Entrepreneur",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-introvert-entrepreneur-beth-buelow-the-qr6CYFNA02W.300x300.jpg",
          "listen_score": 44,
          "listennotes_url": "https://www.listennotes.com/c/fc131f1086ee4eadb3fd9ea968fcf307/",
          "listen_score_global_rank": "1.5%"
        },
        {
          "id": "4357fb92e1c74c7bb4527a14353da6bf",
          "image": "https://cdn-images-1.listennotes.com/podcasts/ask-martin-lewis-podcast-bbc-radio-5-live-YdAqblOktKC-QbdkTFw613O.1400x1400.jpg",
          "title": "Ask Martin Lewis Podcast",
          "publisher": "BBC Radio 5 live",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/ask-martin-lewis-podcast-bbc-radio-5-live-873vofwQGxJ-QbdkTFw613O.300x300.jpg",
          "listen_score": 51,
          "listennotes_url": "https://www.listennotes.com/c/4357fb92e1c74c7bb4527a14353da6bf/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "a409b8bb93f44054a7be2d6b30843899",
          "image": "https://cdn-images-1.listennotes.com/podcasts/entrepreneurs-on-fire-john-lee-dumas-of-rmRvnlE2Lp9-1WOhT7u6VQb.1400x1400.jpg",
          "title": "Entrepreneurs on Fire",
          "publisher": "John Lee Dumas of EOFire",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/entrepreneurs-on-fire-john-lee-dumas-of-KdVcHArxN1E-1WOhT7u6VQb.300x300.jpg",
          "listen_score": 71,
          "listennotes_url": "https://www.listennotes.com/c/a409b8bb93f44054a7be2d6b30843899/",
          "listen_score_global_rank": "0.05%"
        }
      ],
      "source_url": "https://www.timeoutabudhabi.com/things-to-do/the-9-best-business-podcasts?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"From sober news to inspiring tales of success, these are the best podcasts to keep business minds informed and focused.\"",
      "pub_date_ms": 1657554877438,
      "source_domain": "www.timeoutabudhabi.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/the-9-best-business-podcasts-LnF8skAUHb_/"
    },
    {
      "id": "_hB6OVRPlLF",
      "title": "The best true crime podcasts to binge this summer \u2013 from Who Killed Daphne to No Strings Attached",
      "total": 3,
      "podcasts": [
        {
          "id": "064972c7ee0c4e88840e5c678490ff74",
          "image": "https://cdn-images-1.listennotes.com/podcasts/who-killed-daphne-wondery-58mVGp6A7Hj-94a_ym8ZvEU.1400x1400.jpg",
          "title": "Who Killed Daphne?",
          "publisher": "Wondery",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/who-killed-daphne-wondery-b8cBXipz4Sn-94a_ym8ZvEU.300x300.jpg",
          "listen_score": 50,
          "listennotes_url": "https://www.listennotes.com/c/064972c7ee0c4e88840e5c678490ff74/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "a6af6902d720495f9957582bc8abaa7c",
          "image": "https://cdn-images-1.listennotes.com/podcasts/no-strings-attached-itv-news-I6y13-0ECAQ-2uFreaZcnV4.1400x1400.jpg",
          "title": "No Strings Attached",
          "publisher": "ITV News",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/no-strings-attached-itv-news-Ql2yrGTRAEh-2uFreaZcnV4.300x300.jpg",
          "listen_score": 51,
          "listennotes_url": "https://www.listennotes.com/c/a6af6902d720495f9957582bc8abaa7c/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "5a5b57a5ccd24cd1a476556f40936135",
          "image": "https://cdn-images-1.listennotes.com/podcasts/murder-with-my-husband-cloud10-and-hKCMf32bSAD-MlZ5h2fxkIe.1400x1400.jpg",
          "title": "Murder With My Husband",
          "publisher": "Cloud10 and iHeartPodcasts",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/murder-with-my-husband-cloud10-and-DVQA8NcXoJe-MlZ5h2fxkIe.300x300.jpg",
          "listen_score": 73,
          "listennotes_url": "https://www.listennotes.com/c/5a5b57a5ccd24cd1a476556f40936135/",
          "listen_score_global_rank": "0.05%"
        }
      ],
      "source_url": "https://www.the-sun.com/entertainment/tv/5714690/best-true-crime-podcasts-summer-who-killed-daphne-no-strings-attached/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"So, grab your detective hats and your headphones, because these true crimes will have you hooked from the first to last episode.\"",
      "pub_date_ms": 1657554811845,
      "source_domain": "www.the-sun.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/the-best-true-crime-podcasts-to-binge-_hB6OVRPlLF/"
    },
    {
      "id": "nqkgQ-HmbMy",
      "title": "5 Influencer Hosted Podcasts You Need to Listen To Right Now",
      "total": 4,
      "podcasts": [
        {
          "id": "0102d3f8e0a84e1d8fd845e874650088",
          "image": "https://cdn-images-1.listennotes.com/podcasts/saving-grace-294DlptCPNa-Gtv3nFh0cY2.1400x1400.jpg",
          "title": "Saving Grace",
          "publisher": "The Fellas Studios",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/saving-grace-SnTt6o7A8g2-Gtv3nFh0cY2.300x300.jpg",
          "listen_score": 54,
          "listennotes_url": "https://www.listennotes.com/c/0102d3f8e0a84e1d8fd845e874650088/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "0b76678c576e4ddba292cfd976cf438d",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-girls-bathroom-sophia-cinzia-E8PprAIbM5s-jXxG-V9qMvd.1400x1400.jpg",
          "title": "The Girls Bathroom",
          "publisher": "Sophia & Cinzia",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-girls-bathroom-sophia-cinzia-6ImfjNKgtcQ-jXxG-V9qMvd.300x300.jpg",
          "listen_score": 70,
          "listennotes_url": "https://www.listennotes.com/c/0b76678c576e4ddba292cfd976cf438d/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "c7b48218be8e48ec9791a60c1795ac7b",
          "image": "https://cdn-images-1.listennotes.com/podcasts/anything-goes-with-emma-chamberlain-emma-0lB2K3mEiQj-7z1YesgG3Pf.1400x1400.jpg",
          "title": "Anything Goes with Emma Chamberlain",
          "publisher": "Emma Chamberlain and Ramble",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/anything-goes-with-emma-chamberlain-emma-awODSYrshL_-7z1YesgG3Pf.300x300.jpg",
          "listen_score": 83,
          "listennotes_url": "https://www.listennotes.com/c/c7b48218be8e48ec9791a60c1795ac7b/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "7128296333414c87bb27ae07a3a82aaf",
          "image": "https://cdn-images-1.listennotes.com/podcasts/not-to-be-dramatic-podcast-ashleigh-louise-7vKGXuSwD_j-7mrZFUWOkYc.1400x1400.jpg",
          "title": "Not To Be Dramatic Podcast",
          "publisher": "Ashleigh Louise",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/not-to-be-dramatic-podcast-ashleigh-louise-kQrUgN14TBY-7mrZFUWOkYc.300x300.jpg",
          "listen_score": 26,
          "listennotes_url": "https://www.listennotes.com/c/7128296333414c87bb27ae07a3a82aaf/",
          "listen_score_global_rank": "10%"
        }
      ],
      "source_url": "https://talkinginfluence.com/2022/07/08/5-influencer-hosted-podcasts-you-need-to-listen-to-right-now/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"Podcasts are extremely popular amongst the creator community. Alongside photo and video content, long-form audio presents a great opportunity for influencers and creators to speak candidly with their audiences.\"",
      "pub_date_ms": 1657554713348,
      "source_domain": "talkinginfluence.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/5-influencer-hosted-podcasts-you-need-nqkgQ-HmbMy/"
    },
    {
      "id": "3cpA0-Xnyh2",
      "title": "6 of the Best Podcasts About Radical American Movements",
      "total": 6,
      "podcasts": [
        {
          "id": "c444aa2396e742f0bea54ed0cdd3cbbe",
          "image": "https://cdn-images-1.listennotes.com/podcasts/mother-country-radicals-CF9chtrSsiH-vj_uCpD5K4A.1400x1400.jpg",
          "title": "Mother Country Radicals",
          "publisher": "Crooked Media",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/mother-country-radicals-JavbOuiqC1R-vj_uCpD5K4A.300x300.jpg",
          "listen_score": 52,
          "listennotes_url": "https://www.listennotes.com/c/c444aa2396e742f0bea54ed0cdd3cbbe/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "4e77bef5a6174beb8264e0017f809474",
          "image": "https://cdn-images-1.listennotes.com/podcasts/cool-people-who-did-cool-stuff-bXqNhFsr_5m-KUQF_uk5eVx.1400x1400.jpg",
          "title": "Cool People Who Did Cool Stuff",
          "publisher": "iHeartPodcasts and Cool Zone Media",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/cool-people-who-did-cool-stuff-I8N4efV5k2F-KUQF_uk5eVx.300x300.jpg",
          "listen_score": 46,
          "listennotes_url": "https://www.listennotes.com/c/4e77bef5a6174beb8264e0017f809474/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "d620156577fe4408972a29aa2675e628",
          "image": "https://cdn-images-1.listennotes.com/podcasts/american-radical-msnbc-Pl6VZSsQpCw-ZscLB0wq5_7.1400x1400.jpg",
          "title": "American Radical",
          "publisher": "MSNBC",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/american-radical-msnbc-GZeyAVmb0LX-ZscLB0wq5_7.300x300.jpg",
          "listen_score": 67,
          "listennotes_url": "https://www.listennotes.com/c/d620156577fe4408972a29aa2675e628/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "2c35e716fd6b4c0c8de0e661f4638933",
          "image": "https://cdn-images-1.listennotes.com/podcasts/will-be-wild-YZXKslxW0Pv-bP62LCJYxKc.1400x1400.jpg",
          "title": "Will Be Wild",
          "publisher": "Pineapple Street Studios | Wondery | Amazon Music ",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/will-be-wild-fxk9tMDb7g0-bP62LCJYxKc.300x300.jpg",
          "listen_score": 61,
          "listennotes_url": "https://www.listennotes.com/c/2c35e716fd6b4c0c8de0e661f4638933/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "7325987bf997478180d92556b4d5db10",
          "image": "https://cdn-images-1.listennotes.com/podcasts/imperfect-paradise-laist-studios-m3-aGWyvZoi-2uxcmvje7ZP.1400x1400.jpg",
          "title": "Imperfect Paradise",
          "publisher": "LAist Studios",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/imperfect-paradise-laist-studios-E9Hi1JtcNx3-2uxcmvje7ZP.300x300.jpg",
          "listen_score": 44,
          "listennotes_url": "https://www.listennotes.com/c/7325987bf997478180d92556b4d5db10/",
          "listen_score_global_rank": "1.5%"
        }
      ],
      "source_url": "https://lifehacker.com/6-of-the-best-podcasts-about-radical-american-movements-1849158055?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"As the United States enters a new era of even more divisive politics, looking to the past can help us find a way forward. Here are 6 recent podcasts that take us through the history of radical groups, searching for answers in their unearthing of obscured history. Most are told in the voices of the people closest to the events being documented.\"",
      "pub_date_ms": 1657409034984,
      "source_domain": "lifehacker.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/6-of-the-best-podcasts-about-radical-3cpA0-Xnyh2/"
    },
    {
      "id": "XJQaUkqveTM",
      "title": "Four of the best podcasts about women and society",
      "total": 3,
      "podcasts": [
        {
          "id": "bd3ee3d769354c56ad4eb080211688cf",
          "image": "https://cdn-images-1.listennotes.com/podcasts/visible-women-with-caroline-criado-perez-leSgZyAG_vf-w3CZDgn_cFK.1400x1400.jpg",
          "title": "Visible Women with Caroline Criado Perez",
          "publisher": "Tortoise Media",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/visible-women-with-caroline-criado-perez-H3A0hvBn4sC-w3CZDgn_cFK.300x300.jpg",
          "listen_score": 42,
          "listennotes_url": "https://www.listennotes.com/c/bd3ee3d769354c56ad4eb080211688cf/",
          "listen_score_global_rank": "1.5%"
        },
        {
          "id": "6a76c3b9844b4445be34c1fdbfdfb0aa",
          "image": "https://cdn-images-1.listennotes.com/podcasts/28ish-days-later-bbc-radio-4-6hiOEjWPHRw-Z6kMh_vB23N.1400x1400.jpg",
          "title": "28ish Days Later",
          "publisher": "BBC Radio 4",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/28ish-days-later-bbc-radio-4-1b_6iNvpR8F-Z6kMh_vB23N.300x300.jpg",
          "listen_score": 43,
          "listennotes_url": "https://www.listennotes.com/c/6a76c3b9844b4445be34c1fdbfdfb0aa/",
          "listen_score_global_rank": "1.5%"
        },
        {
          "id": "49f87e9c7eb54dcb9a97500ce1c3bac7",
          "image": "https://cdn-images-1.listennotes.com/podcasts/ki-dee-the-podcast-chiara-hunter-diana-nqrTbSBktzM-Ijv0QgtJnMm.1400x1400.jpg",
          "title": "Ki & Dee: The Podcast",
          "publisher": "Chiara Hunter & Diana Vickers",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/ki-dee-the-podcast-chiara-hunter-diana-5mR-yGZ3A7E-Ijv0QgtJnMm.300x300.jpg",
          "listen_score": 37,
          "listennotes_url": "https://www.listennotes.com/c/49f87e9c7eb54dcb9a97500ce1c3bac7/",
          "listen_score_global_rank": "2.5%"
        }
      ],
      "source_url": "https://www.theweek.co.uk/arts-life/culture/957300/best-podcasts-women-society?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"A classic example was her discovery that women are twice as likely to become trapped in cars during an accident, because crash test dummies are modelled on men\u2019s bodies.\"",
      "pub_date_ms": 1657409202145,
      "source_domain": "www.theweek.co.uk",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/four-of-the-best-podcasts-about-women-XJQaUkqveTM/"
    },
    {
      "id": "sf75zZSHdap",
      "title": "7 of the best beauty podcasts to binge right now",
      "total": 5,
      "podcasts": [
        {
          "id": "0425240febe9436a8c8e9822d487210b",
          "image": "https://cdn-images-1.listennotes.com/podcasts/outspoken-beauty-global-media-entertainment-mWrGuv4B9al-ElI_bH2A7ip.1400x1400.jpg",
          "title": "Outspoken Beauty",
          "publisher": "Global Media & Entertainment",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/outspoken-beauty-global-media-entertainment-ciflJ3XMILt-ElI_bH2A7ip.300x300.jpg",
          "listen_score": 54,
          "listennotes_url": "https://www.listennotes.com/c/0425240febe9436a8c8e9822d487210b/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "5d9c6db81d124ae5861b64ace9f99647",
          "image": "https://cdn-images-1.listennotes.com/podcasts/british-beauty-council-career-insights-9Qj-MLmTRS2-7gyL8OPxSDp.1400x1400.jpg",
          "title": "British Beauty Council - Career Insights",
          "publisher": "British Beauty Council",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/british-beauty-council-career-insights-9xlLU2_ynpH-7gyL8OPxSDp.300x300.jpg",
          "listen_score": null,
          "listennotes_url": "https://www.listennotes.com/c/5d9c6db81d124ae5861b64ace9f99647/",
          "listen_score_global_rank": null
        },
        {
          "id": "9bbb587fecd144dba275f0c5154b7c35",
          "image": "https://cdn-images-1.listennotes.com/podcasts/breaking-beauty-podcast-breaking-beauty-LcjqUCi3JpD-BIaMtbCvm_i.1400x1400.jpg",
          "title": "Breaking Beauty Podcast Breaking Beauty Jill Dunn Jill Dunn",
          "publisher": "Dear Media, Jill Dunn and Carlene Higgins",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/breaking-beauty-podcast-breaking-beauty-r07FRxnsoQC-BIaMtbCvm_i.300x300.jpg",
          "listen_score": 61,
          "listennotes_url": "https://www.listennotes.com/c/9bbb587fecd144dba275f0c5154b7c35/",
          "listen_score_global_rank": "0.5%"
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
          "id": "9fc0aaa255704368a98c7b99056c9942",
          "image": "https://cdn-images-1.listennotes.com/podcasts/fat-mascara-fat-mascara-vP-LCJ5FhzH-tmMdf5wFklo.1400x1400.jpg",
          "title": "Fat Mascara",
          "publisher": "Fat Mascara",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/fat-mascara-fat-mascara-KL9WAXmexsc-tmMdf5wFklo.300x300.jpg",
          "listen_score": 64,
          "listennotes_url": "https://www.listennotes.com/c/9fc0aaa255704368a98c7b99056c9942/",
          "listen_score_global_rank": "0.1%"
        }
      ],
      "source_url": "https://www.cosmopolitanme.com/life/best-beauty-podcasts-binge?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"Of course, with the internet being the black hole it is, you may find it difficult to scout out said beauty podcasts, however, fear not, for I have rounded up seven favourites (which really are the best of the best). Whether you\u2019re looking for product recommendations from the industry\u2019s most well-known experts, or are interested in hearing about their career paths, there\u2019s something for everyone in the below list.\"",
      "pub_date_ms": 1657239005831,
      "source_domain": "www.cosmopolitanme.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/7-of-the-best-beauty-podcasts-to-binge-sf75zZSHdap/"
    },
    {
      "id": "XiyJ-4sOVAQ",
      "title": "Top 5 feel-good podcasts to brighten up your day",
      "total": 5,
      "podcasts": [
        {
          "id": "e3343f7f251c475eb9acf5e5f1daec13",
          "image": "https://cdn-images-1.listennotes.com/podcasts/my-therapist-ghosted-me-global-hbPfVSFl0v3-86nsBeIiKbE.1400x1400.jpg",
          "title": "My Therapist Ghosted Me",
          "publisher": "Global",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/my-therapist-ghosted-me-global-RK3zLBmjNJ4-86nsBeIiKbE.300x300.jpg",
          "listen_score": 68,
          "listennotes_url": "https://www.listennotes.com/c/e3343f7f251c475eb9acf5e5f1daec13/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "643ecdeabea748aa88e75f56a8950be0",
          "image": "https://cdn-images-1.listennotes.com/podcasts/rob-beckett-and-josh-widdicombes-parenting-cQWolsRDLJ0-yrwdC_s2iQP.1400x1400.jpg",
          "title": "Rob Beckett and Josh Widdicombe's Parenting Hell",
          "publisher": "Keep It Light Media",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/rob-beckett-and-josh-widdicombes-parenting-kQCfeG9pl0u-yrwdC_s2iQP.300x300.jpg",
          "listen_score": 76,
          "listennotes_url": "https://www.listennotes.com/c/643ecdeabea748aa88e75f56a8950be0/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "adbeec8ec43e4957bb63b9f0b7489991",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-diary-of-a-ceo-with-steven-bartlett-QONYo7d50TG-Gflmgre3zuU.1400x1400.jpg",
          "title": "The Diary Of A CEO with Steven Bartlett",
          "publisher": "Steven Bartlett ",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-diary-of-a-ceo-with-steven-bartlett-7IQW0RnwKzC-Gflmgre3zuU.300x300.jpg",
          "listen_score": null,
          "listennotes_url": "https://www.listennotes.com/c/adbeec8ec43e4957bb63b9f0b7489991/",
          "listen_score_global_rank": null
        },
        {
          "id": "0102d3f8e0a84e1d8fd845e874650088",
          "image": "https://cdn-images-1.listennotes.com/podcasts/saving-grace-294DlptCPNa-Gtv3nFh0cY2.1400x1400.jpg",
          "title": "Saving Grace",
          "publisher": "The Fellas Studios",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/saving-grace-SnTt6o7A8g2-Gtv3nFh0cY2.300x300.jpg",
          "listen_score": 54,
          "listennotes_url": "https://www.listennotes.com/c/0102d3f8e0a84e1d8fd845e874650088/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "45c3e5058b0f4016b67978375fbcb04b",
          "image": "https://cdn-images-1.listennotes.com/podcasts/nearlyweds-bn0VkPhDHZJ--n3uIBHrOGb.1400x1400.jpg",
          "title": "NearlyWeds",
          "publisher": "JamPot Productions",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/nearlyweds-gbvR3IrGX8U--n3uIBHrOGb.300x300.jpg",
          "listen_score": 52,
          "listennotes_url": "https://www.listennotes.com/c/45c3e5058b0f4016b67978375fbcb04b/",
          "listen_score_global_rank": "0.5%"
        }
      ],
      "source_url": "https://www.shemazing.net/top-5-feel-good-podcasts-to-brighten-up-your-day/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"Finding a good podcast that you get lost in can be a difficult choice these days because Spotify and Apple Podcasts are saturated with celebrities and influencers starting their own shows. That\u2019s why we\u2019ve made a list of some feel-good podcasts that touch on topics from relationships and girl talk, to parenting and life advice.\"",
      "pub_date_ms": 1657149980128,
      "source_domain": "www.shemazing.net",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/top-5-feel-good-podcasts-to-brighten-XiyJ-4sOVAQ/"
    },
    {
      "id": "ykopI5ebwcO",
      "title": "8 Must-Listen Podcasts by First Nations Creators",
      "total": 7,
      "podcasts": [
        {
          "id": "8d601a11bbe54656988e5a5542de88e8",
          "image": "https://cdn-images-1.listennotes.com/podcasts/awaye-full-program-podcast-abc-radio-qNPRjr4YWxo-48HUMJkuYle.1400x1400.jpg",
          "title": "AWAYE! - Full program podcast",
          "publisher": "ABC Radio",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/awaye-full-program-podcast-abc-radio-N0qoMzFhex4-48HUMJkuYle.300x300.jpg",
          "listen_score": 39,
          "listennotes_url": "https://www.listennotes.com/c/8d601a11bbe54656988e5a5542de88e8/",
          "listen_score_global_rank": "2%"
        },
        {
          "id": "07dfed64e4fa45a2b380aea88319b7fb",
          "image": "https://cdn-images-1.listennotes.com/podcasts/black-magic-woman-mundanara-bayles-zfE_VLk8v0B-QdrJMBIR1oC.1400x1400.jpg",
          "title": "Black Magic Woman",
          "publisher": "Mundanara Bayles",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/black-magic-woman-mundanara-bayles-wFGz5hRVoUM-QdrJMBIR1oC.300x300.jpg",
          "listen_score": 43,
          "listennotes_url": "https://www.listennotes.com/c/07dfed64e4fa45a2b380aea88319b7fb/",
          "listen_score_global_rank": "1.5%"
        },
        {
          "id": "12433c9821c045e5b67f84aca1cd30d8",
          "image": "https://cdn-images-1.listennotes.com/podcasts/coming-out-blak-coming-out-blak-6cBi0bOXzp5-d2e-W5IAzOo.1400x1400.jpg",
          "title": "Coming out, Blak",
          "publisher": "Coming Out, Blak",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/coming-out-blak-coming-out-blak-TAEmMdIXSyn-d2e-W5IAzOo.300x300.jpg",
          "listen_score": null,
          "listennotes_url": "https://www.listennotes.com/c/12433c9821c045e5b67f84aca1cd30d8/",
          "listen_score_global_rank": null
        },
        {
          "id": "8947d70e53b348dd9013aa6f1a65f54e",
          "image": "https://cdn-images-1.listennotes.com/podcasts/curtain-the-podcast-curtainthepodcast-28HsAfphTOZ-wjJlucqUMKi.1400x1400.jpg",
          "title": "Curtain The Podcast",
          "publisher": "CurtainThePodcast",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/curtain-the-podcast-curtainthepodcast-ubh4851YtJ--wjJlucqUMKi.300x300.jpg",
          "listen_score": 43,
          "listennotes_url": "https://www.listennotes.com/c/8947d70e53b348dd9013aa6f1a65f54e/",
          "listen_score_global_rank": "1.5%"
        },
        {
          "id": "e441c328bb1447049ebc63446d4aea86",
          "image": "https://cdn-images-1.listennotes.com/podcasts/sbs-nitv-radio-nitv-5z-EIAQvuyW--ZFIhzB4CQ7.1400x1400.jpg",
          "title": "SBS NITV Radio",
          "publisher": "NITV",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/sbs-nitv-radio-nitv-x1r2uqwROYd--ZFIhzB4CQ7.300x300.jpg",
          "listen_score": 28,
          "listennotes_url": "https://www.listennotes.com/c/e441c328bb1447049ebc63446d4aea86/",
          "listen_score_global_rank": "10%"
        }
      ],
      "source_url": "https://thelatch.com.au/first-nations-podcasts/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"The more we listen and learn, the better informed we\u2019ll be to get up, stand up, and show up for the people whose land we live on. Read on for a list of great, informative podcasts you can add to your routine.\"",
      "pub_date_ms": 1657041321532,
      "source_domain": "thelatch.com.au",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/8-must-listen-podcasts-by-first-ykopI5ebwcO/"
    },
    {
      "id": "jgLSs3c_YmP",
      "title": "Top 23 Motivational Podcasts to Listen to in 2022",
      "total": 23,
      "podcasts": [
        {
          "id": "f9d5885d7cf7485d891e82dea3186640",
          "image": "https://cdn-images-1.listennotes.com/podcasts/how-i-built-this-with-guy-raz-guy-raz-wondery-7krpVtcCzMB-UC0qH23iP9T.1400x1400.jpg",
          "title": "How I Built This with Guy Raz",
          "publisher": "Guy Raz | Wondery",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/how-i-built-this-with-guy-raz-guy-raz-wondery--t38KFIqlAi-UC0qH23iP9T.300x300.jpg",
          "listen_score": 85,
          "listennotes_url": "https://www.listennotes.com/c/f9d5885d7cf7485d891e82dea3186640/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "6d01c4e63c5349099ea5c6e617c646e6",
          "image": "https://cdn-images-1.listennotes.com/podcasts/therapy-for-black-girls-joy-harden-bradford-_OFSak06eMi-Jw_CUaBj1GI.1400x1400.jpg",
          "title": "Therapy for Black Girls",
          "publisher": "iHeartPodcasts and Joy Harden Bradford, Ph.D.",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/therapy-for-black-girls-joy-harden-bradford-pIt2s-Z4_3R-Jw_CUaBj1GI.300x300.jpg",
          "listen_score": 71,
          "listennotes_url": "https://www.listennotes.com/c/6d01c4e63c5349099ea5c6e617c646e6/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "943c2da80d3b42f99c266ad3f9c06b5d",
          "image": "https://cdn-images-1.listennotes.com/podcasts/ted-health-ted-Qu0GENswY3A-E-oUK8AZGa2.1400x1400.jpg",
          "title": "TED Health",
          "publisher": "TED",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/ted-health-ted-Huegz2ZU5_Q-E-oUK8AZGa2.300x300.jpg",
          "listen_score": 64,
          "listennotes_url": "https://www.listennotes.com/c/943c2da80d3b42f99c266ad3f9c06b5d/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "0f84fdf4db0340c494830bd659e33a7a",
          "image": "https://cdn-images-1.listennotes.com/podcasts/beyond-the-to-do-list-erik-fisher-dt1vxyMYABr-dOgqt1ApC8G.1400x1400.jpg",
          "title": "Beyond the To-Do List",
          "publisher": "Erik Fisher",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/beyond-the-to-do-list-erik-fisher-MzL_DhBJ92K-dOgqt1ApC8G.300x300.jpg",
          "listen_score": 59,
          "listennotes_url": "https://www.listennotes.com/c/0f84fdf4db0340c494830bd659e33a7a/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "f941e8d12ee2496eb91fef658d93a1c9",
          "image": "https://cdn-images-1.listennotes.com/podcasts/financial-feminist-her-first-100k-28icn7KOfvX-qDudc5SM-CF.1400x1400.jpg",
          "title": "Financial Feminist",
          "publisher": "Her First $100K",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/financial-feminist-her-first-100k-YB7npUfq2QS-qDudc5SM-CF.300x300.jpg",
          "listen_score": 66,
          "listennotes_url": "https://www.listennotes.com/c/f941e8d12ee2496eb91fef658d93a1c9/",
          "listen_score_global_rank": "0.05%"
        }
      ],
      "source_url": "https://www.themanual.com/podcast/best-motivational-podcasts/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"These shows can cover everything from career advice to health and how to keep your house clean, but what makes them great is how often they leave the listener inspired and ready to better their own life.\"",
      "pub_date_ms": 1656735127779,
      "source_domain": "www.themanual.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/top-23-motivational-podcasts-to-listen-jgLSs3c_YmP/"
    },
    {
      "id": "Oy6laVpS5kK",
      "title": "The 18 best new podcasts of 2022, so far",
      "total": 18,
      "podcasts": [
        {
          "id": "abc9e389701643b0ae3b57dc571c02d5",
          "image": "https://cdn-images-1.listennotes.com/podcasts/ghost-church-by-jamie-loftus-4DXVpTbeJrY-s7Y6tDlwj2h.1400x1400.jpg",
          "title": "Ghost Church by Jamie Loftus",
          "publisher": "iHeartPodcasts and Cool Zone Media",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/ghost-church-by-jamie-loftus-JlhaxVA6Pbm-s7Y6tDlwj2h.300x300.jpg",
          "listen_score": 49,
          "listennotes_url": "https://www.listennotes.com/c/abc9e389701643b0ae3b57dc571c02d5/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "ddf65fc2fb014ab79d444d953fe45f59",
          "image": "https://cdn-images-1.listennotes.com/podcasts/kuper-island-ebfN4hy7oRu-UqSeFGouRPC.1400x1400.jpg",
          "title": "Kuper Island",
          "publisher": "CBC Podcasts",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/kuper-island-alHXBtOKGPN-UqSeFGouRPC.300x300.jpg",
          "listen_score": 55,
          "listennotes_url": "https://www.listennotes.com/c/ddf65fc2fb014ab79d444d953fe45f59/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "9ba79f84dcf1418a9e0584ed978f6155",
          "image": "https://cdn-images-1.listennotes.com/podcasts/this-is-dating-fFzxB5Vq7LR-75w3jkiupPG.1400x1400.jpg",
          "title": "This Is Dating",
          "publisher": "Magnificent Noise",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/this-is-dating-UsItNxaHJ82-75w3jkiupPG.300x300.jpg",
          "listen_score": 47,
          "listennotes_url": "https://www.listennotes.com/c/9ba79f84dcf1418a9e0584ed978f6155/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "96b622e6c7d345f695bfdca0bbb67e29",
          "image": "https://cdn-images-1.listennotes.com/podcasts/harsh-reality-the-story-of-miriam-rivera-Dtk8WLN-lvw-b0ExUcGMQdA.1400x1400.jpg",
          "title": "Harsh Reality: The Story of Miriam Rivera",
          "publisher": "Wondery",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/harsh-reality-the-story-of-miriam-rivera-9M7vs3upS2B-b0ExUcGMQdA.300x300.jpg",
          "listen_score": 58,
          "listennotes_url": "https://www.listennotes.com/c/96b622e6c7d345f695bfdca0bbb67e29/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "fc1f1bb85b3745d7b81d0c718fe67031",
          "image": "https://cdn-images-1.listennotes.com/podcasts/cover-story-WRgqV13szOe-uyNLeUglVpW.1400x1400.jpg",
          "title": "Cover Story",
          "publisher": "New York Magazine",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/cover-story-RZs9v0IXYf1-uyNLeUglVpW.300x300.jpg",
          "listen_score": 53,
          "listennotes_url": "https://www.listennotes.com/c/fc1f1bb85b3745d7b81d0c718fe67031/",
          "listen_score_global_rank": "0.5%"
        }
      ],
      "source_url": "https://mashable.com/article/best-podcasts-2022?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"From Serial Productions' investigative journalism with a personal touch, or hard-hitting and vital reporting on the January 6 insurrection, to an audio virtual dating show from PRX, and even a fictional story about real-world superhero vigilantes \u2014 you'll find yourself binging these exceptional shows back-to-back if you're not careful.\"",
      "pub_date_ms": 1656734995682,
      "source_domain": "mashable.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/the-18-best-new-podcasts-of-2022-so-far-Oy6laVpS5kK/"
    },
    {
      "id": "brRaNcMPljq",
      "title": "5 Great Podcasts for Kids on Short Drives",
      "total": 5,
      "podcasts": [
        {
          "id": "85c353adfab143f99261ab0afddbfb74",
          "image": "https://cdn-images-1.listennotes.com/podcasts/flip-mozis-guide-to-how-to-be-an-earthling-qpRzAPMDdcK-twEjmNJH2r9.1400x1400.jpg",
          "title": "Flip & Mozi's Guide to How To Be An Earthling ",
          "publisher": "Tinkercast | Wondery",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/flip-mozis-guide-to-how-to-be-an-earthling-KouHiRpBb1Y-twEjmNJH2r9.300x300.jpg",
          "listen_score": 54,
          "listennotes_url": "https://www.listennotes.com/c/85c353adfab143f99261ab0afddbfb74/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "5b16a9da0e7d4d648d66db0f12731b1e",
          "image": "https://cdn-images-1.listennotes.com/podcasts/who-when-wow-RxOqswfh2AI-xXdB3VOg4tk.1400x1400.jpg",
          "title": "Who, When, Wow!",
          "publisher": "Tinkercast | Wondery",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/who-when-wow-oUZFCwpQcvx-xXdB3VOg4tk.300x300.jpg",
          "listen_score": 53,
          "listennotes_url": "https://www.listennotes.com/c/5b16a9da0e7d4d648d66db0f12731b1e/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "3f8526b30ffc44c99743374a57dec2d4",
          "image": "https://cdn-images-1.listennotes.com/podcasts/little-stories-everywhere-wondery-TXJ1FktLoyN-r3J-XGkbauV.1400x1400.jpg",
          "title": "Little Stories Everywhere",
          "publisher": "Wondery",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/little-stories-everywhere-wondery-bmMjkvCOuLG-r3J-XGkbauV.300x300.jpg",
          "listen_score": 56,
          "listennotes_url": "https://www.listennotes.com/c/3f8526b30ffc44c99743374a57dec2d4/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "b4db8b97c88f42d391eabe566780ed7f",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-two-princes-gimlet-AkMyGBILlHs-LksQBNO_U5J.1400x1400.jpg",
          "title": "The Two Princes",
          "publisher": "Gimlet",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-two-princes-gimlet-6aS1EBGCP4Q-LksQBNO_U5J.300x300.jpg",
          "listen_score": 68,
          "listennotes_url": "https://www.listennotes.com/c/b4db8b97c88f42d391eabe566780ed7f/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "1081b063b6574a9ba47d0ce906cbf54e",
          "image": "https://cdn-images-1.listennotes.com/podcasts/girl-tales-cordelia-studios-dKu6MB298zq-LtvWw4HQsYO.1400x1400.jpg",
          "title": "Girl Tales",
          "publisher": "Cordelia Studios",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/girl-tales-cordelia-studios-WXSli38UJIh-LtvWw4HQsYO.300x300.jpg",
          "listen_score": 60,
          "listennotes_url": "https://www.listennotes.com/c/1081b063b6574a9ba47d0ce906cbf54e/",
          "listen_score_global_rank": "0.5%"
        }
      ],
      "source_url": "https://cafemom.com/parenting/podcasts-for-kids-short-drives?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"Here is a roundup of some new podcasts to listen to with your late preschool and early elementary aged kids in the car.\"",
      "pub_date_ms": 1656734779350,
      "source_domain": "cafemom.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/5-great-podcasts-for-kids-on-short-brRaNcMPljq/"
    },
    {
      "id": "mJdE_chWr4K",
      "title": "10 expert-approved kid podcasts to hit play on right now",
      "total": 10,
      "podcasts": [
        {
          "id": "ccb4d2754b614307b2e0c537601d81fb",
          "image": "https://cdn-images-1.listennotes.com/podcasts/circle-round-wbur-f9EwvGNYt6I-N-qUjOX26J3.1400x1400.jpg",
          "title": "Circle Round",
          "publisher": "WBUR",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/circle-round-wbur-DcWar9ieTqw-N-qUjOX26J3.300x300.jpg",
          "listen_score": 74,
          "listennotes_url": "https://www.listennotes.com/c/ccb4d2754b614307b2e0c537601d81fb/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "a59496c8a05545e1a16924dff0b36d46",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-story-seeds-podcast-literary-safari-m1NJ6pvPZe3-MTvLG-xWIaB.1400x1400.jpg",
          "title": "The Story Seeds Podcast",
          "publisher": "Literary Safari",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-story-seeds-podcast-literary-safari-kun_3YzpTLg-MTvLG-xWIaB.300x300.jpg",
          "listen_score": 48,
          "listennotes_url": "https://www.listennotes.com/c/a59496c8a05545e1a16924dff0b36d46/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "cefc4c5cefd44617a5030b372ce67368",
          "image": "https://cdn-images-1.listennotes.com/podcasts/newsy-pooloozi-the-news-pod-for-kids-leela-zrmlcZDxhTy-a4WvfDeRXZP.1400x1400.jpg",
          "title": "Newsy Pooloozi - The News Pod for Kids",
          "publisher": "Leela Sivasankar Prickitt, Lyndee Prickitt",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/newsy-pooloozi-the-news-pod-for-kids-leela-7yhTKZzI3NR-a4WvfDeRXZP.300x300.jpg",
          "listen_score": 43,
          "listennotes_url": "https://www.listennotes.com/c/cefc4c5cefd44617a5030b372ce67368/",
          "listen_score_global_rank": "1.5%"
        },
        {
          "id": "96f1e59700a14a26b42c236ca9c9f6b0",
          "image": "https://cdn-images-1.listennotes.com/podcasts/good-night-stories-for-rebel-girls-rebel-fHtsp8ZYP5i-iqvBmI-nWsx.1400x1400.jpg",
          "title": "Good Night Stories for Rebel Girls",
          "publisher": "Rebel Girls",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/good-night-stories-for-rebel-girls-rebel-RGpke_QKBWY-iqvBmI-nWsx.300x300.jpg",
          "listen_score": 72,
          "listennotes_url": "https://www.listennotes.com/c/96f1e59700a14a26b42c236ca9c9f6b0/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "22af223644c44979b9df34e287d68757",
          "image": "https://cdn-images-1.listennotes.com/podcasts/stoopkid-stories-mel-victor-FMvC-qV0oHX-azVJio0CGmr.1400x1400.jpg",
          "title": "Stoopkid Stories",
          "publisher": "Mel Victor",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/stoopkid-stories-mel-victor-B3t8Z24bRMX-azVJio0CGmr.300x300.jpg",
          "listen_score": 55,
          "listennotes_url": "https://www.listennotes.com/c/22af223644c44979b9df34e287d68757/",
          "listen_score_global_rank": "0.5%"
        }
      ],
      "source_url": "https://mashable.com/article/podcasts-families-children-teens?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"Check out a few notable picks below, and then visit CommonSense's website for the full list of approved and reviewed Common Sense Selections when searching for your families' next audio adventure.\"",
      "pub_date_ms": 1656734702580,
      "source_domain": "mashable.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/10-expert-approved-kid-podcasts-to-hit-mJdE_chWr4K/"
    },
    {
      "id": "kl0FRDtSbuY",
      "title": "Fill Up Your Empty TV Space With These Podcasts About TV Shows",
      "total": 7,
      "podcasts": [
        {
          "id": "ff21e18029cf4430b96596c3caf46c84",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-always-sunny-podcast-charlie-day-glenn-v87LNaDz0Wi-x6gQlJ9qZCn.1400x1400.jpg",
          "title": "The Always Sunny Podcast",
          "publisher": "Charlie Day, Glenn Howerton, Rob McElhenney",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-always-sunny-podcast-charlie-day-glenn-BD-Isr4b96t-x6gQlJ9qZCn.300x300.jpg",
          "listen_score": 70,
          "listennotes_url": "https://www.listennotes.com/c/ff21e18029cf4430b96596c3caf46c84/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "b07809d6350e48a2ae076072f46f4b79",
          "image": "https://cdn-images-1.listennotes.com/podcasts/office-ladies-earwolf-jenna-fischer-and-aryRebflgIq-xnwRMFfrdUh.1400x1400.jpg",
          "title": "Office Ladies",
          "publisher": "Earwolf & Jenna Fischer and Angela Kinsey",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/office-ladies-earwolf-jenna-fischer-and-Nc67mWsEgaz-xnwRMFfrdUh.300x300.jpg",
          "listen_score": 89,
          "listennotes_url": "https://www.listennotes.com/c/b07809d6350e48a2ae076072f46f4b79/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "15d5c9f5fbff416a94ba67a6b32a91d9",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-good-place-ZiOp6ICNESH-v6sjduR_5ea.1400x1400.jpg",
          "title": "The Good Place",
          "publisher": "Agn\u00e8s Dreyfus",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-good-place-OH-xZEloj4e-v6sjduR_5ea.300x300.jpg",
          "listen_score": 35,
          "listennotes_url": "https://www.listennotes.com/c/15d5c9f5fbff416a94ba67a6b32a91d9/",
          "listen_score_global_rank": "3%"
        },
        {
          "id": "1b7f0125f4524022b8a750bcc5f75e51",
          "image": "https://cdn-images-1.listennotes.com/podcasts/buffering-the-vampire-slayer-a-buffy-the-mAbvZugfHG6-7RWxaMHSqcY.1400x1400.jpg",
          "title": "Buffering the Vampire Slayer | A Buffy the Vampire Slayer Podcast",
          "publisher": "Jenny Owen Youngs & Kristin Russo",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/buffering-the-vampire-slayer-a-buffy-the-YgAvhXnxDmq-7RWxaMHSqcY.300x300.jpg",
          "listen_score": 65,
          "listennotes_url": "https://www.listennotes.com/c/1b7f0125f4524022b8a750bcc5f75e51/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "423b771523ff4e888eff384bb7821cce",
          "image": "https://cdn-images-1.listennotes.com/podcasts/rob-has-a-podcast-survivor-big-brother-sS8PeHrzyLU-nA6OVb1UeDY.1400x1400.jpg",
          "title": "Rob Has a Podcast | Survivor / Big Brother / Amazing Race - RHAP",
          "publisher": "Rob Has a Podcast",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/rob-has-a-podcast-survivor-big-brother-vljMhPWu-pa-nA6OVb1UeDY.300x300.jpg",
          "listen_score": 69,
          "listennotes_url": "https://www.listennotes.com/c/423b771523ff4e888eff384bb7821cce/",
          "listen_score_global_rank": "0.05%"
        }
      ],
      "source_url": "https://www.distractify.com/p/best-podcasts-about-tv-shows?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"It\u2019s been the golden age of podcasting for quite some time, and now, podcasts and television are joining forces. Some podcasts are being adapted into television shows, whereas some television shows are getting podcasts to accompany each episode. So we\u2019ve made a list of some of the best podcasts to listen to while we rewatch our favorite television series.\"",
      "pub_date_ms": 1656734597297,
      "source_domain": "www.distractify.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/fill-up-your-empty-tv-space-with-these-kl0FRDtSbuY/"
    },
    {
      "id": "ek3SQxBhRvW",
      "title": "9 of the Best Travel Podcasts to Take You Away",
      "total": 9,
      "podcasts": [
        {
          "id": "2e25ade92a8a4ea391b19dcc170a06d6",
          "image": "https://cdn-images-1.listennotes.com/podcasts/not-lost-pushkin-industries-59PXu2wjzWh-nRNGYZ8UFpr.1400x1400.jpg",
          "title": "Not Lost",
          "publisher": "iHeartPodcasts and Pushkin Industries",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/not-lost-pushkin-industries-1RBEzH-gfYW-nRNGYZ8UFpr.300x300.jpg",
          "listen_score": 48,
          "listennotes_url": "https://www.listennotes.com/c/2e25ade92a8a4ea391b19dcc170a06d6/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "16a2947237ed4ce3a19ec5294427c1b5",
          "image": "https://cdn-images-1.listennotes.com/podcasts/rough-translation-npr-d7BKFJRNDaH-iVGbUFeZ1XE.1400x1400.jpg",
          "title": "Rough Translation",
          "publisher": "NPR",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/rough-translation-npr-jvidAZ9KfuM-iVGbUFeZ1XE.300x300.jpg",
          "listen_score": 73,
          "listennotes_url": "https://www.listennotes.com/c/16a2947237ed4ce3a19ec5294427c1b5/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "94aec9e455b84a1cb7f15490e3fb47cf",
          "image": "https://cdn-images-1.listennotes.com/podcasts/far-flung-with-saleem-reshamwala-ted-4jqhNlYgWLV-ZGukNAVCYsW.1400x1400.jpg",
          "title": "Far Flung with Saleem Reshamwala",
          "publisher": "TED",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/far-flung-with-saleem-reshamwala-ted-LU12JT-GCKu-ZGukNAVCYsW.300x300.jpg",
          "listen_score": 56,
          "listennotes_url": "https://www.listennotes.com/c/94aec9e455b84a1cb7f15490e3fb47cf/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "2142354612de48329dbd5f74c70391e8",
          "image": "https://cdn-images-1.listennotes.com/podcasts/vanishing-postcards-evan-stern-biQI-ZzS0LE-nKIw-McYlHX.1400x1400.jpg",
          "title": "Vanishing Postcards",
          "publisher": "Evan Stern",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/vanishing-postcards-evan-stern-3O_r-dTVDbh-nKIw-McYlHX.300x300.jpg",
          "listen_score": 45,
          "listennotes_url": "https://www.listennotes.com/c/2142354612de48329dbd5f74c70391e8/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "6553c529eb50435e86f9f91bd59bd32e",
          "image": "https://cdn-images-1.listennotes.com/podcasts/greetings-from-somewhere-a-travel-show-zach-it5cxSzjJBm-UADsGpZiMoR.1400x1400.jpg",
          "title": "Greetings from Somewhere | A Travel Show",
          "publisher": "Zach Mack",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/greetings-from-somewhere-a-travel-show-zach-SP6FwJ3cs8a-UADsGpZiMoR.300x300.jpg",
          "listen_score": 45,
          "listennotes_url": "https://www.listennotes.com/c/6553c529eb50435e86f9f91bd59bd32e/",
          "listen_score_global_rank": "1%"
        }
      ],
      "source_url": "https://www.lifehacker.com.au/2022/06/9-of-the-best-travel-podcasts-to-take-you-away/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"The following nine shows explore places you\u2019ve always dreamed of visiting, cities you\u2019ve never heard of, and towns not easily found on maps. Each one has a unique spin on the travelog format \u2014 in Not Lost, Brendan Francis Newnam is on a mission to get invited to dinner parties by strangers all over the world; Evan Stern\u2019s Vanishing Postcards takes you on a 11,016 km journey down Route 66 \u2014 and will fuel and sate your wanderlust in equal measure. Let\u2019s go!\"",
      "pub_date_ms": 1656602015137,
      "source_domain": "www.lifehacker.com.au",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/9-of-the-best-travel-podcasts-to-take-ek3SQxBhRvW/"
    },
    {
      "id": "6VrOAfltqe_",
      "title": "8 Wellbeing Podcasts To Give You A Little Life Boost",
      "total": 7,
      "podcasts": [
        {
          "id": "9dc9fdd724c24ac4a497788b19064f1e",
          "image": "https://cdn-images-1.listennotes.com/podcasts/unlocking-us-with-bren\u00e9-brown-parcast-network-w4qKzY5OpyB-3BLhH_1OXfZ.1400x1400.jpg",
          "title": "Unlocking Us with Bren\u00e9 Brown",
          "publisher": "Parcast Network",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/unlocking-us-with-bren\u00e9-brown-parcast-network-e-UfCqLn2yi-3BLhH_1OXfZ.300x300.jpg",
          "listen_score": 81,
          "listennotes_url": "https://www.listennotes.com/c/9dc9fdd724c24ac4a497788b19064f1e/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "c0a15898aa604cdd9651e76470e000b8",
          "image": "https://cdn-images-1.listennotes.com/podcasts/health-check-bbc-world-service-cIS7ksHfY4R-326vAf9ktqT.1400x1400.jpg",
          "title": "Health Check",
          "publisher": "BBC World Service",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/health-check-bbc-world-service-WUvT53V_mJP-326vAf9ktqT.300x300.jpg",
          "listen_score": 47,
          "listennotes_url": "https://www.listennotes.com/c/c0a15898aa604cdd9651e76470e000b8/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "fb1fdf95a8954a6c8e1be8793069bc5f",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-michelle-obama-podcast-BWyVvpK56dD-4Mk7bWl3whX.1400x1400.jpg",
          "title": "The Michelle Obama Podcast",
          "publisher": "Higher Ground & Spotify ",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-michelle-obama-podcast-5h9UQokIzub-4Mk7bWl3whX.300x300.jpg",
          "listen_score": 72,
          "listennotes_url": "https://www.listennotes.com/c/fb1fdf95a8954a6c8e1be8793069bc5f/",
          "listen_score_global_rank": "0.05%"
        },
        {
          "id": "85c0e9f89f7c41aaa7420cd3b2424a26",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-happiness-lab-with-dr-laurie-santos-G5IoOPjZFNK-hB3PAqrH5Eu.1400x1400.jpg",
          "title": "The Happiness Lab with Dr. Laurie Santos",
          "publisher": "Pushkin Industries",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-happiness-lab-with-dr-laurie-santos-12V8EGwUR9Y-hB3PAqrH5Eu.300x300.jpg",
          "listen_score": 78,
          "listennotes_url": "https://www.listennotes.com/c/85c0e9f89f7c41aaa7420cd3b2424a26/",
          "listen_score_global_rank": "0.01%"
        },
        {
          "id": "8139a48d57ea40f0b2fa8a5bde6facf6",
          "image": "https://cdn-images-1.listennotes.com/podcasts/power-hour-adrienne-herbert-0UyS-cixht8-Xgq7SOmRzC_.1400x1400.jpg",
          "title": "Power Hour",
          "publisher": "Adrienne Herbert",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/power-hour-adrienne-herbert-U3WGLPeDluH-Xgq7SOmRzC_.300x300.jpg",
          "listen_score": 57,
          "listennotes_url": "https://www.listennotes.com/c/8139a48d57ea40f0b2fa8a5bde6facf6/",
          "listen_score_global_rank": "0.5%"
        }
      ],
      "source_url": "https://www.thehandbook.com/the-best-wellbeing-podcasts-you-can-listen-to/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"We\u2019ve put together a list of some of the best wellbeing podcasts there are, some which focus on happiness, others on relationships and friendships, and some on pursuing our goals, and they\u2019re all there to help make you feel better.\"",
      "pub_date_ms": 1656601922337,
      "source_domain": "www.thehandbook.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/8-wellbeing-podcasts-to-give-you-a-6VrOAfltqe_/"
    },
    {
      "id": "Sx607azrB5_",
      "title": "10 Best Historical Podcasts Like Behind The Bastards",
      "total": 10,
      "podcasts": [
        {
          "id": "9a8a0bd0630044c0a79b179137d52c59",
          "image": "https://cdn-images-1.listennotes.com/podcasts/lions-led-by-donkeys-podcast-lions-led-by-JuW9BQ-_EwG-R4r7pE2MniS.1400x1400.jpg",
          "title": "Lions Led By Donkeys Podcast",
          "publisher": "Lions Led By Donkeys",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/lions-led-by-donkeys-podcast-lions-led-by-SOlHeBAcqxk-R4r7pE2MniS.300x300.jpg",
          "listen_score": 57,
          "listennotes_url": "https://www.listennotes.com/c/9a8a0bd0630044c0a79b179137d52c59/",
          "listen_score_global_rank": "0.5%"
        },
        {
          "id": "4e77bef5a6174beb8264e0017f809474",
          "image": "https://cdn-images-1.listennotes.com/podcasts/cool-people-who-did-cool-stuff-bXqNhFsr_5m-KUQF_uk5eVx.1400x1400.jpg",
          "title": "Cool People Who Did Cool Stuff",
          "publisher": "iHeartPodcasts and Cool Zone Media",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/cool-people-who-did-cool-stuff-I8N4efV5k2F-KUQF_uk5eVx.300x300.jpg",
          "listen_score": 46,
          "listennotes_url": "https://www.listennotes.com/c/4e77bef5a6174beb8264e0017f809474/",
          "listen_score_global_rank": "1%"
        },
        {
          "id": "eb5661f5be5b4994ade0b8bacbdd62f6",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-age-of-napoleon-podcast-everett-rummage-7M6UX3COo2d-xlNBH-s0ULJ.1400x1400.jpg",
          "title": "The Age of Napoleon Podcast",
          "publisher": "Everett Rummage",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-age-of-napoleon-podcast-everett-rummage-vPc8j6nJSsg-xlNBH-s0ULJ.300x300.jpg",
          "listen_score": 63,
          "listennotes_url": "https://www.listennotes.com/c/eb5661f5be5b4994ade0b8bacbdd62f6/",
          "listen_score_global_rank": "0.1%"
        },
        {
          "id": "182a62a08251491b8812649e09424131",
          "image": "https://cdn-images-1.listennotes.com/podcasts/megacorp-iheartpodcasts-b3MWqRL0Tkf-h7jswkzQVbH.1400x1400.jpg",
          "title": "Megacorp",
          "publisher": "iHeartPodcasts",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/megacorp-iheartpodcasts-AmS9b7Y0XDM-h7jswkzQVbH.300x300.jpg",
          "listen_score": 44,
          "listennotes_url": "https://www.listennotes.com/c/182a62a08251491b8812649e09424131/",
          "listen_score_global_rank": "1.5%"
        },
        {
          "id": "e40da44a41964bea91ef8750c3f82fdd",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-dollop-with-dave-anthony-and-gareth-KQqhLyZS3pO-z3QpGrFfyxE.1400x1400.jpg",
          "title": "The Dollop with Dave Anthony and Gareth Reynolds",
          "publisher": "All Things Comedy",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-dollop-with-dave-anthony-and-gareth-rCWgKPy4G2t-z3QpGrFfyxE.300x300.jpg",
          "listen_score": 81,
          "listennotes_url": "https://www.listennotes.com/c/e40da44a41964bea91ef8750c3f82fdd/",
          "listen_score_global_rank": "0.01%"
        }
      ],
      "source_url": "https://screenrant.com/best-historical-podcasts-behind-the-bastards/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
      "description": "\"When it comes to discussing about history's greatest and most powerful monsters, which podcasts series can compare to Behind the Bastards?\"",
      "pub_date_ms": 1656601795707,
      "source_domain": "screenrant.com",
      "listennotes_url": "https://www.listennotes.com/curated-podcasts/10-best-historical-podcasts-like-Sx607azrB5_/"
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

See all available parameters on the [API Docs page](https://www.listennotes.com/podcast-api/docs/#post-api-v2-podcasts-submit).


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

See all available parameters on the [API Docs page](https://www.listennotes.com/podcast-api/docs/#delete-api-v2-podcasts-id).


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

See all available parameters on the [API Docs page](https://www.listennotes.com/podcast-api/docs/#get-api-v2-playlists-id).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "id": "m1pe7z60bsw",
  "name": "Podcasts about podcasting",
  "type": "episode_list",
  "image": "https://cdn-images-1.listennotes.com/podcast-playlists/podcasts-about-podcasting-4bU7MZIlEVO-m1pe7z60bsw.1600x1600.jpg",
  "items": [
    {
      "id": 830890,
      "data": {
        "id": "b6965b7bcdab4df1b108a93309cedfc6",
        "link": "https://anthonypompliano.com/podcast/?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/b6965b7bcdab4df1b108a93309cedfc6/",
        "image": "https://cdn-images-1.listennotes.com/podcasts/the-pomp-podcast/1014-oscar-merry-on-0_Nv4FrTdO5-s5SUXWPM2IZ.1400x1400.jpg",
        "title": "#1014 Oscar Merry On Pioneering Listen To Earn With Bitcoin",
        "podcast": {
          "id": "537c372ad9c7470cb2be897a14a7c7f9",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-pomp-podcast-anthony-pompliano-Bm_CSdnOjHA-f1na5MVD_Qz.1400x1400.jpg",
          "title": "The Pomp Podcast",
          "publisher": "Anthony Pompliano",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-pomp-podcast-anthony-pompliano-UexQLc20lJR-f1na5MVD_Qz.300x300.jpg",
          "listen_score": 65,
          "listennotes_url": "https://www.listennotes.com/c/537c372ad9c7470cb2be897a14a7c7f9/",
          "listen_score_global_rank": "0.1%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-pomp-podcast/1014-oscar-merry-on-W-qrn7XULpm-s5SUXWPM2IZ.300x300.jpg",
        "description": "<p>Oscar Merry is the Co-Founder of Fountain, a new podcast platform where viewers can get paid to listen to their favorite podcasts and is powered by the Bitcoin Lightning Network.</p><p><br /></p><p>In this conversation, we talk about podcasting 2.0, how the Fountain product works, why podcasters should be interested in paying their listeners, and on-boarding people to the Bitcoin network through Fountain.</p><p>=======================</p><p>LMAX Digital - the market-leading solution for institutional crypto trading &amp; custodial services - offers clients a regulated, transparent and secure trading environment, together with the deepest pool of crypto liquidity. LMAX Digital is also a primary price discovery venue, streaming real-time market data to the industry\u2019s leading analytics platforms. LMAX Digital - secure, liquid, trusted. Learn more at <a href=\"http://lmaxdigital.com/pomp\">LMAXdigital.com/pomp</a></p><p>=======================</p><p>The Pod Pro Cover by Eight Sleep is the most advanced solution on the market for thermoregulation. It pairs dynamic cooling and heating with biometric tracking. Go to<a href=\"https://www.eightsleep.com/pomp\"> </a><a href=\"https://www.eightsleep.com/pomp\">https://www.eightsleep.com/Pomp</a> to check out the Pod Pro Cover and save $150 at checkout. Eight Sleep currently ships within the USA, Canada, and the UK.</p><p>=======================</p><p>DeFi Technologies represents what\u2019s next in the digital economy -- providing simplified, trusted access to crypto, decentralized finance and Web 3.0 investment opportunities. Institutions and investors can gain diversified, secure, compliant, and easily tradable access to a diversified set of industry-leading equity products and protocols, through a single stock purchase on a regulated exchange. Currently listed on U.S. (OTC: DEFTF) and Canadian (NEO:DEFI) exchanges.</p><p>\u00a0</p><p>For more information or to subscribe to receive company updates and financial information, visit our website at<a href=\"http://defi.tech/\"> </a><a href=\"http://defi.tech/\">http://defi.tech</a>\u00a0</p><p>=======================</p>",
        "pub_date_ms": 1655835471034,
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/recode-media-recode-h9zPK_1UkdB-1iPwTajLXlS.1400x1400.jpg",
        "title": "Bill Simmons on podcasts, celebrity interviews and life at Spotify",
        "podcast": {
          "id": "2aba49dc3fc04e3e96fe89f79a261798",
          "image": "https://cdn-images-1.listennotes.com/podcasts/recode-media-recode-h9zPK_1UkdB-1iPwTajLXlS.1400x1400.jpg",
          "title": "Recode Media",
          "publisher": "Recode",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/recode-media-recode-eHTVnkiXyu9-1iPwTajLXlS.300x300.jpg",
          "listen_score": 55,
          "listennotes_url": "https://www.listennotes.com/c/2aba49dc3fc04e3e96fe89f79a261798/",
          "listen_score_global_rank": "0.5%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/recode-media-recode-eHTVnkiXyu9-1iPwTajLXlS.300x300.jpg",
        "description": "<p>The Bill Simmons Podcast is, by its own description, \"the most downloaded sports podcast of all time.\" This week, it hits its 1,000th episode.</p><p>Bill Simmons began his career as a Boston sportswriter and went on to found ESPN's sports and pop culture blog Grantland. After ESPN shut down the site, Simmons started the Ringer \u2014 which he sold to Spotify in 2020.</p><p>In this wide-ranging conversation, Recode\u2019s Peter Kafka talks to Simmons about how he became a podcasting pioneer, and when he realized nerditry about the NBA and Game of Thrones could both live under the same roof. Simmons also reflects on what he learned from his time as an employee of The Walt Disney Corporation and how things are different at Spotify. Plus, he reveals the number one dream guest he\u2019d love to have on his show.</p><p><br /></p><p><strong>Featuring</strong>: Bill Simmons (<a href=\"https://twitter.com/BillSimmons\">@BillSimmons</a>), Founder of The Ringer</p><p><strong>Host</strong>: Peter Kafka\u00a0(<a href=\"https://twitter.com/pkafka\">@pkafka</a>), Senior Editor at Recode</p><p><strong>More to explore</strong>: <a href=\"https://pod.link/1080467174\">Subscribe for free to Recode Media</a>, Peter Kafka, one of the media industry's most acclaimed reporters, talks to business titans, journalists, comedians, and more to get their take on today's media landscape.</p><p><strong>About Recode by Vox</strong>: Recode by Vox helps you understand how tech is changing the world \u2014 and changing us.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
        "pub_date_ms": 1655266568000,
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/the-tim-ferriss-show-tim-ferriss-7NwMpUz5o0S.1400x1400.jpg",
        "title": "#538: How I Built The Tim Ferriss Show to 700+ Million Downloads \u2014 An Immersive Explanation of All Aspects and Key Decisions (Featuring Chris Hutchins)",
        "podcast": {
          "id": "25212ac3c53240a880dd5032e547047b",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-tim-ferriss-show-tim-ferriss-7NwMpUz5o0S.1400x1400.jpg",
          "title": "The Tim Ferriss Show",
          "publisher": "Tim Ferriss: Bestselling Author, Human Guinea Pig",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-tim-ferriss-show-tim-ferriss-7NwMpUz5o0S.300x300.jpg",
          "listen_score": 81,
          "listennotes_url": "https://www.listennotes.com/c/25212ac3c53240a880dd5032e547047b/",
          "listen_score_global_rank": "0.01%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-tim-ferriss-show-tim-ferriss-7NwMpUz5o0S.300x300.jpg",
        "description": "<p><strong>How I Built The Tim Ferriss Show to 700+ Million Downloads \u2014 An Immersive Explanation of All Aspects and Key Decisions (Featuring Chris Hutchins) | Brought to you by </strong><a href=\"http://linkedin.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>LinkedIn Jobs</strong></a><strong>&nbsp;recruitment platform with 770M+ users</strong>, <a href=\"http://athleticgreens.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>Athletic Greens</strong></a><strong>&nbsp;all-in-one nutritional supplement,&nbsp;and </strong><a href=\"http://helixsleep.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>Helix Sleep</strong></a><strong>&nbsp;premium mattresses. More on all three below.</strong></p><p><strong>Chris Hutchins</strong>&nbsp;(<a href=\"https://twitter.com/hutchins\" rel=\"noopener noreferrer\" target=\"_blank\">@hutchins</a>) is an avid life hacker and financial optimizer. He\u2019s the host of&nbsp;<a href=\"https://www.allthehacks.com/\" rel=\"noopener noreferrer\" target=\"_blank\"><strong><em>All the Hacks</em></strong></a>&nbsp;podcast and the Head of New Product Strategy at&nbsp;<a href=\"https://www.wealthfront.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\">Wealthfront</a>.</p><p>Previously, Chris was co-founder and CEO of Grove (acquired by&nbsp;<a href=\"https://www.wealthfront.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\">Wealthfront</a>), co-founder of Milk (acquired by Google), and a partner at&nbsp;<a href=\"https://www.gv.com/\" rel=\"noopener noreferrer\" target=\"_blank\">Google Ventures</a>, where he focused on seed and early stage investments.</p><p>Chris reached out with many questions about podcasting. He had already read much of&nbsp;<a href=\"https://tim.blog/2016/04/11/tim-ferriss-podcast-business/\" rel=\"noopener noreferrer\" target=\"_blank\">what I had written</a> and&nbsp;<a href=\"https://rolfpotts.com/podcast/tim-ferriss/\" rel=\"noopener noreferrer\" target=\"_blank\">listened to several interviews</a>, and this is intended to be an updated guide to all things podcasting.</p><p>Please enjoy!</p><p><strong>This episode is brought to you by&nbsp;</strong><a href=\"https://www.athleticgreens.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>Athletic Greens</strong></a><strong>.</strong>&nbsp;I get asked all the time, \u201cIf you could only use one supplement, what would it be?\u201d My answer is usually&nbsp;<a href=\"https://www.athleticgreens.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\">Athletic&nbsp;Greens</a>, my all-in-one nutritional insurance. I recommended it in&nbsp;<em>The 4-Hour Body</em>&nbsp;in 2010 and did not get paid to do so. I do my best with nutrient-dense meals, of course, but&nbsp;<a href=\"https://www.athleticgreens.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\">AG</a>&nbsp;further covers my bases with vitamins, minerals, and whole-food-sourced micronutrients that support gut health and the immune system.&nbsp;</p><p><strong>Right now,&nbsp;</strong><a href=\"https://www.athleticgreens.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>Athletic Greens</strong></a><strong>&nbsp;is offering you their Vitamin D Liquid Formula free with your first subscription purchase</strong>\u2014a vital nutrient for a strong immune system and strong bones.&nbsp;<strong>Visit&nbsp;</strong><a href=\"https://www.athleticgreens.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>AthleticGreens.com/Tim</strong></a><strong>&nbsp;to claim this special offer today and receive the free Vitamin D Liquid Formula (and five free travel packs) with your first subscription purchase!&nbsp;</strong>That\u2019s up to a one-year supply of Vitamin D as added value when you try their delicious and comprehensive all-in-one daily greens product.</p><p>*</p><p><strong>This episode is also brought to you by&nbsp;</strong><a href=\"http://helixsleep.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>Helix Sleep</strong></a><strong>!&nbsp;</strong>Helix was selected as the #1 overall mattress of 2020 by&nbsp;<em>GQ&nbsp;</em>magazine<em>, Wired,&nbsp;</em>Apartment Therapy, and many others. With&nbsp;<a href=\"http://helixsleep.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\">Helix</a>, there\u2019s a specific mattress to meet each and every body\u2019s unique comfort needs. Just take their quiz\u2014<a href=\"http://helixsleep.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\">only two minutes to complete</a>\u2014that matches your body type and sleep preferences to the perfect mattress for you. They have a 10-year warranty, and you get to try it out for a hundred nights, risk free. They\u2019ll even pick it up from you if you don\u2019t love it.&nbsp;</p><p><strong>And now, to my dear listeners, Helix is offering up to 200 dollars off all mattress orders plus two free pillows at&nbsp;</strong><a href=\"http://helixsleep.com/tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>HelixSleep.com/Tim</strong></a><strong>.</strong></p><p><strong>*</strong></p><p><strong>This episode is also brought to you by&nbsp;</strong><a href=\"https://linkedin.com/Tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>LinkedIn Jobs</strong></a><strong>.</strong>&nbsp;Whether you are looking to hire now for a critical role or thinking about needs that you may have in the future,&nbsp;<a href=\"https://linkedin.com/Tim\" rel=\"noopener noreferrer\" target=\"_blank\">LinkedIn Jobs</a>&nbsp;can help. LinkedIn screens candidates for the hard and soft skills you\u2019re looking for and puts your job in front of candidates looking for job opportunities that match what you have to offer.</p><p>Using LinkedIn\u2019s active community of more than 770 million professionals worldwide,&nbsp;<a href=\"https://linkedin.com/Tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>LinkedIn Jobs</strong></a>&nbsp;can help you find and hire the right person faster.&nbsp;<strong>When your business is ready to make that next hire, find the right person with LinkedIn Jobs. And now, you can post a job for free.</strong>&nbsp;<a href=\"https://linkedin.com/Tim\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>Just visit LinkedIn.com/Tim</strong></a><strong>.</strong></p><p><strong>*</strong></p><p><strong>If you enjoy the podcast, would you please consider&nbsp;</strong><a href=\"https://podcasts.apple.com/us/podcast/the-tim-ferriss-show/id863897795?mt=2\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>leaving a short&nbsp;review&nbsp;on Apple Podcasts</strong></a><strong>?</strong>&nbsp;It takes less than 60 seconds, and it really makes a difference in helping to convince hard-to-get guests. I also love reading the&nbsp;reviews!</p><p><strong>For show notes and past guests, please visit</strong>&nbsp;<a href=\"https://tim.blog/podcast/?utm_source=podcast&amp;utm_medium=podcast&amp;utm_campaign=podcast-description\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>tim.blog/podcast</strong></a><strong>.</strong></p><p><strong>Sign up for Tim\u2019s email newsletter (\u201c5-Bullet Friday\u201d) at&nbsp;</strong><a href=\"https://go.tim.blog/5-bullet-friday-1/\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>tim.blog/friday</strong></a><strong>.</strong></p><p><strong>For transcripts of episodes, go to&nbsp;</strong><a href=\"http://tim.blog/transcripts\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>tim.blog/transcripts</strong></a><strong>.</strong></p><p><strong>Discover Tim\u2019s books:&nbsp;</strong><a href=\"http://tim.blog/books\" rel=\"noopener noreferrer\" target=\"_blank\"><strong>tim.blog/books</strong></a><strong>.</strong></p><p><strong>Follow Tim:</strong></p><p><strong>Twitter</strong>:&nbsp;<a href=\"https://twitter.com/tferriss\" rel=\"noopener noreferrer\" target=\"_blank\">twitter.com/tferriss</a>&nbsp;</p><p><strong>Instagram</strong>:&nbsp;<a href=\"https://instagram.com/timferriss/\" rel=\"noopener noreferrer\" target=\"_blank\">instagram.com/timferriss</a></p><p><strong>Facebook</strong>:&nbsp;<a href=\"https://www.facebook.com/TimFerriss/\" rel=\"noopener noreferrer\" target=\"_blank\">facebook.com/timferriss</a>&nbsp;</p><p><strong>YouTube</strong>:&nbsp;<a href=\"https://www.youtube.com/timferriss\" rel=\"noopener noreferrer\" target=\"_blank\">youtube.com/timferriss</a></p><p>Past guests on&nbsp;<a href=\"http://tim.blog/podcast\" rel=\"noopener noreferrer\" target=\"_blank\"><strong><em>The Tim Ferriss Show</em></strong></a>&nbsp;include&nbsp;<a href=\"https://tim.blog/2020/12/08/jerry-seinfeld/\" rel=\"noopener noreferrer\" target=\"_blank\">Jerry Seinfeld</a>,&nbsp;<a href=\"https://tim.blog/2020/06/26/hugh-jackman/\" rel=\"noopener noreferrer\" target=\"_blank\">Hugh Jackman</a>,&nbsp;<a href=\"https://tim.blog/2020/04/16/jane-goodall/\" rel=\"noopener noreferrer\" target=\"_blank\">Dr. Jane Goodall</a>,&nbsp;<a href=\"https://tim.blog/2018/11/27/lebron-james-mike-mancias/\" rel=\"noopener noreferrer\" target=\"_blank\">LeBron James</a>,&nbsp;<a href=\"https://tim.blog/2020/05/20/kevin-hart/\" rel=\"noopener noreferrer\" target=\"_blank\">Kevin Hart</a>,&nbsp;<a href=\"https://tim.blog/2018/09/07/doris-kearns-goodwin-leadership/\" rel=\"noopener noreferrer\" target=\"_blank\">Doris Kearns Goodwin</a>,&nbsp;<a href=\"https://tim.blog/2015/12/06/jamie-foxx/\" rel=\"noopener noreferrer\" target=\"_blank\">Jamie Foxx</a>,&nbsp;<a href=\"https://tim.blog/2020/10/19/matthew-mcconaughey/\" rel=\"noopener noreferrer\" target=\"_blank\">Matthew McConaughey</a>,&nbsp;<a href=\"https://tim.blog/2017/05/21/esther-perel/\" rel=\"noopener noreferrer\" target=\"_blank\">Esther Perel</a>,&nbsp;<a href=\"https://tim.blog/2020/05/08/elizabeth-gilbert/\" rel=\"noopener noreferrer\" target=\"_blank\">Elizabeth Gilbert</a>,&nbsp;<a href=\"https://tim.blog/2017/12/20/terry-crews-how-to-have-do-and-be-all-you-want/\" rel=\"noopener noreferrer\" target=\"_blank\">Terry Crews</a>,&nbsp;<a href=\"https://tim.blog/2020/08/12/sia/\" rel=\"noopener noreferrer\" target=\"_blank\">Sia</a>,&nbsp;<a href=\"https://tim.blog/2020/10/27/yuval-noah-harari/\" rel=\"noopener noreferrer\" target=\"_blank\">Yuval Noah Harari</a>,&nbsp;<a href=\"https://tim.blog/2016/06/21/malcolm-gladwell/\" rel=\"noopener noreferrer\" target=\"_blank\">Malcolm Gladwell</a>,&nbsp;<a href=\"https://tim.blog/2020/05/27/secretary-madeleine-albright/\" rel=\"noopener noreferrer\" target=\"_blank\">Madeleine Albright</a>,&nbsp;<a href=\"https://tim.blog/2017/03/30/cheryl-strayed/\" rel=\"noopener noreferrer\" target=\"_blank\">Cheryl Strayed</a>,&nbsp;<a href=\"https://tim.blog/2019/02/18/jim-collins/\" rel=\"noopener noreferrer\" target=\"_blank\">Jim Collins</a>,&nbsp;<a href=\"https://tim.blog/2020/11/11/mary-karr/\" rel=\"noopener noreferrer\" target=\"_blank\">Mary Karr,</a>&nbsp;<a href=\"https://tim.blog/2014/10/21/brain-pickings/\" rel=\"noopener noreferrer\" target=\"_blank\">Maria Popova</a>,&nbsp;<a href=\"https://tim.blog/2020/05/15/sam-harris-2/\" rel=\"noopener noreferrer\" target=\"_blank\">Sam Harris</a>,&nbsp;<a href=\"https://tim.blog/2021/01/21/michael-phelps-grant-hackett/\" rel=\"noopener noreferrer\" target=\"_blank\">Michael Phelps</a>,&nbsp;<a href=\"https://tim.blog/2020/01/16/bob-iger/\" rel=\"noopener noreferrer\" target=\"_blank\">Bob Iger</a>,&nbsp;<a href=\"https://tim.blog/2019/10/31/edward-norton-motherless-brooklyn/\" rel=\"noopener noreferrer\" target=\"_blank\">Edward Norton</a>,&nbsp;<a href=\"https://tim.blog/2015/02/02/arnold-schwarzenegger/\" rel=\"noopener noreferrer\" target=\"_blank\">Arnold Schwarzenegger</a>,&nbsp;<a href=\"https://tim.blog/2014/06/24/neil-strauss/\" rel=\"noopener noreferrer\" target=\"_blank\">Neil Strauss</a>,&nbsp;<a href=\"https://tim.blog/2019/09/12/ken-burns/\" rel=\"noopener noreferrer\" target=\"_blank\">Ken Burns</a>,&nbsp;<a href=\"https://tim.blog/2017/08/26/maria-sharapova/\" rel=\"noopener noreferrer\" target=\"_blank\">Maria Sharapova</a>,&nbsp;<a href=\"https://tim.blog/2016/05/29/marc-andreessen/\" rel=\"noopener noreferrer\" target=\"_blank\">Marc Andreessen</a>,&nbsp;<a href=\"https://tim.blog/2019/03/28/neil-gaiman/\" rel=\"noopener noreferrer\" target=\"_blank\">Neil Gaiman</a>,&nbsp;<a href=\"https://tim.blog/2019/10/03/neil-degrasse-tyson/\" rel=\"noopener noreferrer\" target=\"_blank\">Neil de Grasse Tyson</a>,&nbsp;<a href=\"https://tim.blog/2016/09/21/jocko-willink-on-discipline-leadership-and-overcoming-doubt/\" rel=\"noopener noreferrer\" target=\"_blank\">Jocko Willink</a>,&nbsp;<a href=\"https://tim.blog/2020/12/03/daniel-ek/\" rel=\"noopener noreferrer\" target=\"_blank\">Daniel Ek</a>,&nbsp;<a href=\"https://tim.blog/2020/09/08/kelly-slater/\" rel=\"noopener noreferrer\" target=\"_blank\">Kelly Slater</a>,&nbsp;<a href=\"https://tim.blog/2019/11/27/peter-attia-fasting-metformin-longevity/\" rel=\"noopener noreferrer\" target=\"_blank\">Dr. Peter Attia</a>,&nbsp;<a href=\"https://tim.blog/2016/02/10/seth-godin/\" rel=\"noopener noreferrer\" target=\"_blank\">Seth Godin</a>,&nbsp;<a href=\"https://tim.blog/2018/09/25/howard-marks/\" rel=\"noopener noreferrer\" target=\"_blank\">Howard Marks</a>,&nbsp;<a href=\"https://tim.blog/2020/02/06/brene-brown-striving-self-acceptance-saving-marriages/\" rel=\"noopener noreferrer\" target=\"_blank\">Dr. Bren\u00e9 Brown</a>,&nbsp;<a href=\"https://tim.blog/2019/04/09/eric-schmidt/\" rel=\"noopener noreferrer\" target=\"_blank\">Eric Schmidt</a>,&nbsp;<a href=\"https://tim.blog/2020/05/01/michael-lewis/\" rel=\"noopener noreferrer\" target=\"_blank\">Michael Lewis</a>,&nbsp;<a href=\"https://tim.blog/2018/03/08/joe-gebbia-co-founder-of-airbnb/\" rel=\"noopener noreferrer\" target=\"_blank\">Joe Gebbia</a>,&nbsp;<a href=\"https://tim.blog/2018/05/06/michael-pollan-how-to-change-your-mind/\" rel=\"noopener noreferrer\" target=\"_blank\">Michael Pollan</a>,&nbsp;<a href=\"https://tim.blog/2021/03/01/jordan-peterson/\" rel=\"noopener noreferrer\" target=\"_blank\">Dr. Jordan Peterson</a>,&nbsp;<a href=\"https://tim.blog/2017/05/31/vince-vaughn/\" rel=\"noopener noreferrer\" target=\"_blank\">Vince Vaughn</a>,&nbsp;<a href=\"https://tim.blog/2020/04/23/brian-koppelman/\" rel=\"noopener noreferrer\" target=\"_blank\">Brian Koppelman</a>,&nbsp;<a href=\"https://tim.blog/2019/05/07/ramit-sethi/\" rel=\"noopener noreferrer\" target=\"_blank\">Ramit Sethi</a>,&nbsp;<a href=\"https://tim.blog/2020/11/18/dax-shepard/\" rel=\"noopener noreferrer\" target=\"_blank\">Dax Shepard</a>,&nbsp;<a href=\"https://tim.blog/2014/10/15/money-master-the-game/\" rel=\"noopener noreferrer\" target=\"_blank\">Tony Robbins</a>,&nbsp;<a href=\"https://tim.blog/2020/05/18/jim-dethmer/\" rel=\"noopener noreferrer\" target=\"_blank\">Jim Dethmer</a>,&nbsp;<a href=\"https://tim.blog/2020/11/19/dan-harris/\" rel=\"noopener noreferrer\" target=\"_blank\">Dan Harris</a>,&nbsp;<a href=\"https://tim.blog/2017/09/13/ray-dalio/\" rel=\"noopener noreferrer\" target=\"_blank\">Ray Dalio</a>,&nbsp;<a href=\"https://tim.blog/2015/08/18/the-evolutionary-angel-naval-ravikant/\" rel=\"noopener noreferrer\" target=\"_blank\">Naval Ravikant</a>,&nbsp;<a href=\"https://tim.blog/2021/03/08/vitalik-buterin-naval-ravikant/\" rel=\"noopener noreferrer\" target=\"_blank\">Vitalik Buterin</a>,&nbsp;<a href=\"https://tim.blog/2021/03/16/elizabeth-lesser/\" rel=\"noopener noreferrer\" target=\"_blank\">Elizabeth Lesser</a>,&nbsp;<a href=\"https://tim.blog/2019/04/18/amanda-palmer-2/\" rel=\"noopener noreferrer\" target=\"_blank\">Amanda Palmer</a>,&nbsp;<a href=\"https://tim.blog/2021/02/18/katie-haun/\" rel=\"noopener noreferrer\" target=\"_blank\">Katie Haun</a>,&nbsp;<a href=\"https://tim.blog/2017/10/09/richard-branson/\" rel=\"noopener noreferrer\" target=\"_blank\">Sir Richard Branson</a>,&nbsp;<a href=\"https://tim.blog/2020/09/02/chuck-palahniuk/\" rel=\"noopener noreferrer\" target=\"_blank\">Chuck Palahniuk</a>,&nbsp;<a href=\"https://tim.blog/2017/10/18/arianna-huffington/\" rel=\"noopener noreferrer\" target=\"_blank\">Arianna Huffington</a>,&nbsp;<a href=\"https://tim.blog/2015/08/31/the-oracle-of-silicon-valley-reid-hoffman-plus-michael-mccullough/\" rel=\"noopener noreferrer\" target=\"_blank\">Reid Hoffman</a>,&nbsp;<a href=\"https://tim.blog/2017/09/17/bill-burr/\" rel=\"noopener noreferrer\" target=\"_blank\">Bill Burr</a>,&nbsp;<a href=\"https://tim.blog/2015/06/26/whitney-cummings/\" rel=\"noopener noreferrer\" target=\"_blank\">Whitney Cummings</a>,&nbsp;<a href=\"https://tim.blog/2015/05/15/rick-rubin/\" rel=\"noopener noreferrer\" target=\"_blank\">Rick Rubin</a>,&nbsp;<a href=\"https://tim.blog/2020/03/26/vivek-murthy/\" rel=\"noopener noreferrer\" target=\"_blank\">Dr. Vivek Murthy</a>,&nbsp;<a href=\"https://tim.blog/2017/09/09/darren-aronofsky/\" rel=\"noopener noreferrer\" target=\"_blank\">Darren Aronofsky</a>, and many more.</p><p>See Privacy Policy at <a href=\"https://art19.com/privacy\" rel=\"noopener noreferrer\" target=\"_blank\">https://art19.com/privacy</a> and California Privacy Notice at <a href=\"https://art19.com/privacy#do-not-sell-my-info\" rel=\"noopener noreferrer\" target=\"_blank\">https://art19.com/privacy#do-not-sell-my-info</a>.</p>",
        "pub_date_ms": 1634222633061,
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-L8QBusAiaXq-OaJSjb4xQv3.1400x1400.jpg",
        "title": "Episode 194 \u2014 Back on Spotify",
        "podcast": {
          "id": "37589a3e121e40debe4cef3d9638932a",
          "image": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-L8QBusAiaXq-OaJSjb4xQv3.1400x1400.jpg",
          "title": "Exponent",
          "publisher": "Ben Thompson / James Allworth",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-IrgMw5cPALF-OaJSjb4xQv3.300x300.jpg",
          "listen_score": 61,
          "listennotes_url": "https://www.listennotes.com/c/37589a3e121e40debe4cef3d9638932a/",
          "listen_score_global_rank": "0.5%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/exponent-ben-thompson-james-allworth-IrgMw5cPALF-OaJSjb4xQv3.300x300.jpg",
        "description": "<p>Ben and James discuss the history of podcasts and why Spotify&#8217;s recent announcements are so compelling for creators.</p>\n<p><strong>Links</strong></p>\n<ul>\n<li>Ben Thompson: Spotify&#8217;s Surprise \u2014 <a href=\"https://stratechery.com/2021/spotifys-surprise/\">Stratechery</a></li>\n<li>Episode 185 \u2014 Open, Free, and Spotify \u2014 <a href=\"https://exponent.fm/episode-185-open-free-and-spotify/\">Exponent</a></li>\n<li>Ben Thompson: Podcasts, Analytics, and Centralization \u2014 <a href=\"https://stratechery.com/2017/podcasts-analytics-and-centralization/\">Stratechery</a></li>\n<li>Ben Thompson: Spotify\u2019s Podcast Aggregation Play \u2014 <a href=\"https://stratechery.com/2019/spotifys-podcast-aggregation-play/\">Stratechery</a></li>\n<li>Ben Thompson: Dithering and Open Versus Free \u2014 <a href=\"https://stratechery.com/2020/dithering-and-the-open-web/\">Stratechery</a></li>\n<li>Ben Thompson: Spotify Earnings, Podcasts and Lifetime Value, The Ringer Acquisition \u2014 <a href=\"https://stratechery.com/2020/spotifys-earnings-podcasts-and-lifetime-value-the-ringer-acquisition/\">Stratechery</a></li>\n<li>Ben Thompson: The European Super League, Apple Music\u2019s Letter to Artists \u2014 <a href=\"https://stratechery.com/2021/the-european-super-league-apple-musics-letter-to-artists/\">Stratechery</a></li>\n<li>Ben Thompson: Podcast Subscriptions vs. the App Store \u2014 <a href=\"https://stratechery.com/2021/podcast-subscriptions-vs-the-app-store/\">Stratechery</a></li>\n<li>Ben Thompson: Fearing Spotify?, Apple\u2019s Earnings, Margins and Chips \u2014 <a href=\"https://stratechery.com/2021/fearing-spotify-apples-earnings-margins-and-chips/\">Stratechery</a></li>\n</ul>\n<p><strong>Hosts</strong></p>\n<p>\u00a0</p>\n<ul>\n<li>Ben Thompson, <a href=\"http://twitter.com/benthompson\">@benthompson</a>, <a href=\"http://stratechery.com\">Stratechery</a></li>\n<li>James Allworth, <a href=\"http://twitter.com/jamesallworth\">@jamesallworth</a>, <a href=\"https://hbr.org/search?term=James+Allworth&#038;sort=popularity_score\">Harvard Business Review</a></li>\n</ul>\n<p>\u00a0</p>\n<p><strong>Podcast Information</strong></p>\n<p>\u00a0</p>\n<ul>\n<li><a href=\"https://exponent.fm/feed/\">Feed</a></li>\n<li><a href=\"https://itunes.apple.com/us/podcast/exponent/id826420969\">iTunes</a></li>\n<li><a href=\"https://soundcloud.com/exponentfm\">SoundCloud</a></li>\n<li><a href=\"http://twitter.com/exponentfm\">Twitter</a></li>\n<li><a href=\"http://stratechery.com/exponent-feedback/\">Feedback</a></h2>\n</li>\n</ul>",
        "pub_date_ms": 1619771580002,
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/the-james-altucher/side-hustle-friday-why-x-OdlkHPweS-jDmTs6Nl-tr.1400x1400.jpg",
        "title": "Side Hustle Friday: Why should you START a podcast and MONETIZE your podcast through Ads and Patreon!",
        "podcast": {
          "id": "6dabf2f65c384e1f897bb606859309f4",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-james-altucher-show-james-altucher-50EFuIdlcY4-sSHocv8YjIe.1400x1400.jpg",
          "title": "The James Altucher Show",
          "publisher": "James Altucher",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-james-altucher-show-james-altucher-6q58dRHpmvW-sSHocv8YjIe.300x300.jpg",
          "listen_score": 67,
          "listennotes_url": "https://www.listennotes.com/c/6dabf2f65c384e1f897bb606859309f4/",
          "listen_score_global_rank": "0.05%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-james-altucher/side-hustle-friday-why-BpGUVA-oL_v-jDmTs6Nl-tr.300x300.jpg",
        "description": "<p>Another Side Hustle Friday! I sat down with Jay Yow, the Sound Engineer/ Producer of The James Altucher, to discuss ways to monetize a podcast, we spoke about why this is the best time to launch a podcast and our equipment set up for remote recording and interview. In this episode, we break down that's the different ways you can monetize through Ads, sponsors, affiliate deals, and Patreon! Part 2 will be coming soon Monday!</p>\n<hr />\n<p><strong>I write about all my podcasts! Check out the full post and learn what I learned at <a href=\"https://www.jamesaltucher.com/podcast\">jamesaltucher.com/podcast</a>.</strong></p>\n<p><strong>Thanks so much for listening! If you like this episode, please subscribe to \u201cThe James Altucher Show\u201d and rate and review wherever you get your podcasts:</strong></p>\n<p><a href=\"https://itunes.apple.com/us/podcast/the-james-altucher-show/id794030859?mt=2\">Apple Podcasts</a></p>\n<p><a href=\"https://www.stitcher.com/podcast/stansberry-radio-network/the-james-altucher-show/e/52735033\">Stitcher</a></p>\n<p><a href=\"https://www.iheart.com/podcast/232-The-James-Altucher-Show-27085086/episode/ep-298-ryan-holiday-competition-28789411/\">iHeart Radio</a></p>\n<p><a href=\"https://open.spotify.com/episode/0ABi9w3Qrb2EFNDeeXlHyz\">Spotify</a></p>\n<p> </p>\n<p><strong>Follow me on Social Media:</strong></p>\n<p><a href=\"https://www.youtube.com/channel/UCRQlx2klE_aNrPhz2OyKRdg\">YouTube</a></p>\n<p><a href=\"https://twitter.com/jaltucher\">Twitter</a></p>\n<p><a href=\"https://www.facebook.com/JAltucher.Blog/\">Facebook</a></p>\n<p><a href=\"https://www.linkedin.com/in/jamesaltucher\">Linkedin</a></p>",
        "pub_date_ms": 1602831600286,
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/the-james-altucher/side-hustle-friday-monetize-nJaycZ39zdH-vZt0gi5hoDN.1400x1400.jpg",
        "title": "Side Hustle Friday: Monetize your podcast right now!",
        "podcast": {
          "id": "6dabf2f65c384e1f897bb606859309f4",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-james-altucher-show-james-altucher-50EFuIdlcY4-sSHocv8YjIe.1400x1400.jpg",
          "title": "The James Altucher Show",
          "publisher": "James Altucher",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-james-altucher-show-james-altucher-6q58dRHpmvW-sSHocv8YjIe.300x300.jpg",
          "listen_score": 67,
          "listennotes_url": "https://www.listennotes.com/c/6dabf2f65c384e1f897bb606859309f4/",
          "listen_score_global_rank": "0.05%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-james-altucher/side-hustle-friday-monetize-TGCj-9qP0Nw-vZt0gi5hoDN.300x300.jpg",
        "description": "<p>Part 2 on monetizing your podcast! In this episode, we talked about ways to monetize your podcast via merchandising, getting hired as a consultant through your podcast, speaking gigs, on and on! Also, enjoy Jay's episodic debut on the podcast! (Technically a second since this is a part of Friday's podcast!)</p>\n<hr />\n<p><strong>I write about all my podcasts! Check out the full post and learn what I learned at <a href=\"https://www.jamesaltucher.com/podcast\">jamesaltucher.com/podcast</a>.</strong></p>\n<p><strong>Thanks so much for listening! If you like this episode, please subscribe to \u201cThe James Altucher Show\u201d and rate and review wherever you get your podcasts:</strong></p>\n<p><a href=\"https://itunes.apple.com/us/podcast/the-james-altucher-show/id794030859?mt=2\">Apple Podcasts</a></p>\n<p><a href=\"https://www.stitcher.com/podcast/stansberry-radio-network/the-james-altucher-show/e/52735033\">Stitcher</a></p>\n<p><a href=\"https://www.iheart.com/podcast/232-The-James-Altucher-Show-27085086/episode/ep-298-ryan-holiday-competition-28789411/\">iHeart Radio</a></p>\n<p><a href=\"https://open.spotify.com/episode/0ABi9w3Qrb2EFNDeeXlHyz\">Spotify</a></p>\n<p> </p>\n<p><strong>Follow me on Social Media:</strong></p>\n<p><a href=\"https://www.youtube.com/channel/UCRQlx2klE_aNrPhz2OyKRdg\">YouTube</a></p>\n<p><a href=\"https://twitter.com/jaltucher\">Twitter</a></p>\n<p><a href=\"https://www.facebook.com/JAltucher.Blog/\">Facebook</a></p>\n<p><a href=\"https://www.linkedin.com/in/jamesaltucher\">Linkedin</a></p>",
        "pub_date_ms": 1603090800284,
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
        "link": "https://anchor.fm/this-week-in-startups/episodes/E1096-Podcasting-State-of-the-Union-featuring-Overcasts-Marco-Arment--Oxford-Roads-Dan-Granger-e1cgtk4?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/3c311c8cf83448dea0463c69bfe61c75/",
        "image": "https://cdn-images-1.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-x2RL7ujsCWm-EKckR36zrnA.1400x1400.jpg",
        "title": "E1096: Podcasting State of the Union featuring Overcast\u2019s Marco Arment & Oxford Road\u2019s Dan Granger",
        "podcast": {
          "id": "9a62e2581908415185dee35d2d19f9b5",
          "image": "https://cdn-images-1.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-x2RL7ujsCWm-EKckR36zrnA.1400x1400.jpg",
          "title": "This Week in Startups",
          "publisher": "Jason Calacanis",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-e9OjnJ3rBt_-EKckR36zrnA.300x300.jpg",
          "listen_score": 63,
          "listennotes_url": "https://www.listennotes.com/c/9a62e2581908415185dee35d2d19f9b5/",
          "listen_score_global_rank": "0.1%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/this-week-in-startups-jason-calacanis-e9OjnJ3rBt_-EKckR36zrnA.300x300.jpg",
        "description": "Follow Marco: https://twitter.com/marcoarment<br />\n<br />\nDownload Overcast: https://overcast.fm<br />\n<br />\nFollow Oxford Road: https://twitter.com/Oxford_Road<br />\n<br />\nFollow Jason: https://linktr.ee/calacanis<br />\n<br />\nThanks to our partners...<br />\nSendPro Online from Pitney Bowes - Try it free for 30 days and get a free 10-pound scale at https://pb.com/twist<br />\nLinkedIn Marketing - Get $100 off your first advertising campaign at https://linkedin.com/thisweekinstartups<br />\nVanta - $1k off your SOC 2 at https://vanta.com/twist",
        "pub_date_ms": 1597416466467,
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/the-casey-adams-show/elise-hu-hosting-ted-talks-Y6q40Ejr-ZX-wUV0p1Rd3zs.1400x1400.jpg",
        "title": "Elise Hu - Hosting \"TED Talks Daily\" & The Future of Podcasting",
        "podcast": {
          "id": "11362a0682e744b29ce5ea73c920132e",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-casey-adams-show-casey-adams-1QTF8tJKOUn-YuarHs5lfDI.1400x1400.jpg",
          "title": "The Casey Adams Show",
          "publisher": "Casey Adams",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-casey-adams-show-casey-adams-T2EsmXiCuvD-YuarHs5lfDI.300x300.jpg",
          "listen_score": 55,
          "listennotes_url": "https://www.listennotes.com/c/11362a0682e744b29ce5ea73c920132e/",
          "listen_score_global_rank": "0.5%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-casey-adams-show/elise-hu-hosting-ted-talks-FbSdafYDC9N-wUV0p1Rd3zs.300x300.jpg",
        "description": "<p>Elise Hu is a host-at-large based at NPR West in Culver City, Calif. Previously, she explored the future with her video series, <a href=\"https://www.npr.org/2019/05/06/716414780/videos-future-you\"><em>Future You with Elise Hu</em></a>, and served as the founding bureau chief and International Correspondent for NPR's Seoul office. She was based in Seoul for nearly four years, responsible for the network's coverage of both Koreas and Japan, and filed from a dozen countries across Asia. Before joining NPR, she was one of the founding reporters at <a href=\"http://www.texastribune.org/\">The Texas Tribune</a>, a non-profit digital news startup devoted to politics and public policy. While at the Tribune, Hu oversaw television partnerships and multimedia projects, contributed to <em>The New York Times</em>' expanded Texas coverage, and pushed for editorial innovation across platforms.Her work at NPR has earned a DuPont-Columbia award and a Gracie Award from the Alliance for Women in Media for her video series, <em>Elise Tries</em>. Her previous work has earned a Gannett Foundation Award for Innovation in Watchdog Journalism, a National Edward R. Murrow award for best online video, and beat reporting awards from the Texas Associated Press. <em>The Austin Chronicle</em> once dubiously named her the \"<a href=\"http://www.austinchronicle.com/gyrobase/Awards/BestOfAustin?Award=660138\">Best TV Reporter Who Can Write</a>.\"</p>\n<p>Follow Elise Hu on Instagram: <a href=\"https://www.instagram.com/elisewho/?hl=en\">https://www.instagram.com/elisewho/?hl=en</a></p>\n<p>Learn more about Elise Hu: <a href=\"https://elisehu.com/\">https://elisehu.com/</a></p>\n<p>Listen to \"TED Talks Daily\" <a href=\"https://podcasts.apple.com/us/podcast/ted-talks-daily/id160904630\">https://podcasts.apple.com/us/podcast/ted-talks-daily/id160904630</a></p>\n<p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
        "pub_date_ms": 1586266731132,
        "guid_from_rss": "9aeee818-e72c-4928-8149-7cae42595d82",
        "listennotes_url": "https://www.listennotes.com/e/50d0110bec79414eac61cb472c3c1de2/",
        "audio_length_sec": 2520,
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
          "listen_score_global_rank": "1%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-feed-the/167-cleanfeed-with-a-side-of-KEMJ65zVY4x-OS-PBaQKcgl.300x300.jpg",
        "description": "<p>Tons of details on all things Google Podcasts Manager! It\u2019s like Apple Podcasts connect but of course Google. Then, we move on to jobs in podcasting, so much about feedback about Cleanfeed, some very interesting Facebook updates, Libsyn player automation, what if someone uses YOUR podcast name, a massive breakdown of the podfader types and of course we\u2019ve got a crazy amount of stats!</p> <p>Audience feedback drives the show. We\u2019d love for you to email us and keep the conversation going! Email thefeed@libsyn.com or call 412\u2013573\u20131934. We\u2019d love to hear from you!</p> Quick Episode Summary <ul> <li><em>:07</em> Intro!</li> <li><em>3:04 PROMO 1: Sailing in the Mediterranean and Beyond</em></li> <li><em>3:34</em> Rob and Elsie conversation</li> <li>Announcement of Google Podcasts Manager!</li> <li>What it is, what it gives you and how it it different than Apple Podcasts analytics</li> <li>9:46 Apple is hiring for all kinds of podcasting positions</li> <li>13:56 Cleanfeed audio feedback from Carey Green</li> <li>Emails about Cleanfeed</li> <li>18:08 Cleanfeed audio feedback from CG</li> <li>Thoughts and processes about remote recording</li> <li>There\u2019s a new kid in town</li> <li>27:35 Facebook updates about charging for online events and listening to Faceboook Lives</li> <li>30:58 PROMO 2: The Naturist Living Show</li> <li>New version of Podcast Addict now with reviews</li> <li>Custom automation for the libsyn players</li> <li>Face ID and masks</li> <li>39:55 What if someone is using the name of your show? How do you go about dealing with it?</li> <li>A show appearing twice on some apps</li> <li>49:43 Podfading - the key main groups</li> <li>UK data from Rajar on internet delivery audio services via Neil!</li> <li>57:38 PROMO 3: The Europe Desk</li> <li>Stats, stats, stats: mean and median</li> <li>59:52 COVID\u201319 libsyn stats</li> <li>Where have we been?</li> <li>Where are we going?</li> </ul> Featured Podcast Promos + Audio <ul> <li><a href=\"https://www.medsailor.com/\">PROMO 1: Sailing in the Mediterranean and Beyond</a></li> <li><a href=\"https://www.naturistlivingshow.com/\">PROMO 2: The Naturist Living Show</a></li> <li><a href=\"https://cges.georgetown.edu/research/podcast/\">PROMO 3: The Europe Desk</a></li> <li><a href=\"https://podcastfasttrack.com/\">Carey Green from Podcast Fast Track</a></li> <li><a href=\"https://www.therocketryshow.com/\">CB from the Rocketry Show</a></li> </ul> <p>Thank you to Nick from <a href=\"http://micme.com\">MicMe</a> for our awesome intro!</p>  <p><em>Podcasting Articles and Links mentioned by Rob and Elsie</em></p> <ul> <li><a href=\"http://speakpipe.com/thefeed\">Our SpeakPipe Feedback page!</a> Leave us feedback :)</li> <li><a href=\"http://podcastsmanager.google.com\">Google Podcasts Podcast Manager</a></li> <li><a href=\"https://podcasts.google.com/manager/about\">Google Podcasts Manager About Page</a></li> <li><a href=\"https://support.google.com/podcast-publishers/answer/9479755?hl=en&amp;ref_topic=9476973&amp;authuser=0\"> Adding new and existing podcasts</a></li> <li><a href=\"https://search.google.com/devtools/podcast/preview\">Is your show already in Google Podcasts? Check here</a></li> <li><a href=\"https://support.google.com/podcast-publishers/answer/9696727?hl=en&amp;ref_topic=9476973&amp;authuser=0\"> Manage users and permissions on Google Podcasts Manager</a></li> <li><a href=\"https://support.google.com/podcast-publishers?hl=en&amp;authuser=0#topic=9476973\"> Google Podcasts Manager Support</a></li> <li><a href=\"https://jobs.apple.com/en-us/details/200164774/podcasts-operations-manager?team=MKTG\"> Podcasts Operations Manager</a></li> <li><a href=\"https://jobs.apple.com/en-us/details/200164287/program-manager-podcasts-apple-media-products?team=SFTWR\"> Program Manager, Podcasts, Apple Media Products</a></li> <li><a href=\"https://jobs.apple.com/en-us/details/200164774/podcasts-operations-manager?team=MKTG\"> UI Engineer, Apple Media Products (Podcasts)</a></li> <li><a href=\"https://youtu.be/DpRHSmJT_Vk\">Carey\u2019s Cleanfeed demo video</a></li> <li><a href=\"http://podcastification.com/in-search-of-the-best-way-to-record-an-interview-with-mark-hills-of-cleanfeed-ep-69\"> Carey\u2019s interview with Mark from Cleanfeed</a></li> <li><a href=\"https://podcastengineeringschool.com/marc-bakos-of-cleanfeed-pes-104/\"> Chris Curran\u2019s interview with Marc from Cleanfeed</a></li> <li><a href=\"https://www.reddit.com/r/podcasting/comments/flw9ae/services_and_applications_to_allow_remote/\"> Services and applications to allow remote recordings of remote guests and co-hosts. - Reddit</a></li> <li><a href=\"http://podcast411.com/mixer.pdf\">Rob\u2019s PDF</a></li> <li><a href=\"https://resonaterecordings.com/2020/04/voice-recorder\">Resonate Recordings new recorder</a></li> <li><a href=\"https://about.fb.com/news/2020/04/introducing-messenger-rooms/\">Facebook news</a></li> <li><a href=\"https://www.rajar.co.uk/docs/news/MIDAS_Spring_2020.pdf\">Rajar data for Measurement of Internet Delivery Audio Services</a></li> <li><a href=\"https://twitter.com/search?q=podcast411%20%23cmworld&amp;src=typed_query&amp;f=live\"> Rob\u2019s #CMWorld twitter chat</a></li> <li><a href=\"https://jacobsmedia.com/there-are-over-a-million-podcasts-in-apples-podcasts-app-what-does-it-mean/\"> There Are Over A Million Podcasts In Apple\u2019s Podcasts App, What Does It Mean?</a></li> <li><a href=\"http://www.insideradio.com/podcastnewsdaily/walch-podcast-downloads-aren-t-down-as-much-as-mobility-showing-medium-s-stickiness/article_394e057a-84ba-11ea-a6d0-a3defc713949.html\"> Walch: Proof Of Podcast \u2018Stickiness.\u2019</a></li> </ul>  <em>HELP US SPREAD THE WORD!</em> <p><em>We\u2019d love it if you could please share #TheFeed with your twitter followers. <a href=\"http://clicktotweet.com/9d2te\">Click here to post a tweet!</a></em></p> <p><em>If you dug this episode head on over to Apple Podcasts and kindly <a href=\"https://itunes.apple.com/us/podcast/feed-official-libsyn-podcast/id668413144\"> leave us a rating, a review and subscribe!</a></em></p> <em>Ways to subscribe to The Feed: The Official Libsyn Podcast</em> <ul> <li><em><a href=\"https://itunes.apple.com/us/podcast/feed-official-libsyn-podcast/id668413144\"> Click here to subscribe via Apple Podcasts</a></em></li> <li><em><a href=\"http://thefeed.libsyn.com/rss\">Click here to subscribe via RSS</a></em></li> <li><em><a href=\"http://www.stitcher.com/podcast/libsyn/the-feed\">You can also subscribe via Stitcher</a></em></li> </ul> FEEDBACK + PROMOTION <p><em>You can ask your questions, make comments and create a segment about podcasting for podcasters! Let your voice be heard.</em></p> <ul> <li>Download the FREE The Feed App for <a href=\"https://itunes.apple.com/us/app/the-feed-podcasting-tips-from-libsyn/id381787434?mt=8\"> iOS</a> and <a href=\"https://play.google.com/store/apps/details?id=com.libsyn.android.thefeed&amp;hl=en\"> Android</a> (you can send feedback straight from within the app)</li> <li>Call 412 573 1934</li> <li>Email thefeed@libsyn.com</li> <li>Use our <a href=\"http://speakpipe.com/thefeed\">SpeakPipe Page</a>!</li> </ul>",
        "pub_date_ms": 1588694700057,
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/marketing-school-digital-marketing-and-knLzBPreqYx-pHyiIJT4Lxl.1400x1400.jpg",
        "title": "Spotify Acquired 'The Ringer' Podcast ($15M In Revenues) - Here's What It Means  | Ep. #1306",
        "podcast": {
          "id": "9a2abf6b68b54554a60a32a2932febcb",
          "image": "https://cdn-images-1.listennotes.com/podcasts/marketing-school-digital-marketing-and-knLzBPreqYx-pHyiIJT4Lxl.1400x1400.jpg",
          "title": "Marketing School - Digital Marketing and Online Marketing Tips",
          "publisher": "Eric Siu & Neil Patel",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/marketing-school-digital-marketing-and-9FS5Tsvab0Q-pHyiIJT4Lxl.300x300.jpg",
          "listen_score": 64,
          "listennotes_url": "https://www.listennotes.com/c/9a2abf6b68b54554a60a32a2932febcb/",
          "listen_score_global_rank": "0.1%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/marketing-school-digital-marketing-and-9FS5Tsvab0Q-pHyiIJT4Lxl.300x300.jpg",
        "description": "<p>In episode #1306, we discuss Spotify\u2019s acquisition of The Ringer. The podcasting industry is growing exponentially and Spotify wanted to make an aggressive move toward growing its market share. Tune in to hear why this was a super smart decision on their part!</p> <p>TIME-STAMPED SHOW NOTES:</p> <ul> <li>[00:25] Today\u2019s topic: How Spotify Acquired The Ringer.\u00a0\u00a0</li> <li>[00:42] The solid financial results for Spotify in Q4 of 2019.</li> <li>[00:56] How Spotify recognized exponential growth in podcast hours streamed.</li> <li>[01:24] Realizing that they needed to acquire a big podcast to double down on opportunities.\u00a0\u00a0\u00a0</li> <li>[01:53] The impressive retention rates of the Marketing School podcast.</li> <li>[02:09] Why Spotify\u2019s decision makes a lot of sense.\u00a0</li> <li>[02:39] Keep in mind that all good channels eventually become crowded.\u00a0\u00a0</li> <li>[03:09] Spotify\u2019s market share around podcasting and how they\u2019re more aggressive than Apple.\u00a0</li> <li>[03:48] The number of downloads The Ringer podcast is getting.\u00a0</li> <li>[04:07] Start comparing your Apple Podcast and Spotify analytics for your podcast.\u00a0</li> <li>[04:50] How our podcasts and Eric\u2019s own podcast are performing.\u00a0\u00a0</li> <li>[05:56] The proposed price for The Ringer stated by Bill Simmons: $100 million.\u00a0</li> <li>[06:25] That\u2019s it for today!</li> <li>[06:26] To stay updated with events and learn more about our mastermind, go to the <a href=\"https://marketingschool.io/growth-accelerator-mastermind\"> Marketing School</a> site for more information.</li> </ul> <p>Links Mentioned in Today\u2019s Episode:</p> <ul> <li><a href=\"https://www.spotify.com/\">Spotify</a>\u00a0</li> <li><a href=\"https://www.theringer.com\">The Ringer</a></li> <li><a href=\"https://www.apple.com\">Apple</a></li> <li><a href=\"https://growtheverywhere.com/podcast-player/\">Leveling Up Podcast</a></li> <li><a href=\"https://twitter.com/BillSimmons?ref_src\">Bill Simmons on Twitter</a></li> </ul> <p>Leave Some Feedback:</p> <p>\u00a0</p> <ul> <li>What should we talk about next?\u00a0Please let us know in the comments below</li> </ul> <ul> <li>Did you enjoy this episode?\u00a0If so, please leave a short review.</li> </ul> <p>\u00a0</p> <p>Connect with Us:\u00a0</p> <ul> <li style=\"font-weight: 400;\"><a href=\"http://neilpatel.com\">Neilpatel.com</a></li> <li style=\"font-weight: 400;\"><a href=\"https://www.quicksprout.com/\">Quick Sprout</a>\u00a0</li> <li style=\"font-weight: 400;\"><a href=\"https://growtheverywhere.com/\">Growth Everywhere</a></li> <li style=\"font-weight: 400;\"><a href=\"https://www.singlegrain.com/\">Single Grain</a></li> <li style=\"font-weight: 400;\"><a href=\"https://twitter.com/neilpatel\">Twitter @neilpatel</a>\u00a0</li> <li style=\"font-weight: 400;\"><a href=\"https://twitter.com/ericosiu\">Twitter @ericosiu</a></li> </ul>",
        "pub_date_ms": 1582812000850,
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/recode-media-recode-h9zPK_1UkdB-1iPwTajLXlS.1400x1400.jpg",
        "title": "Spotify, The Ringer and the future of podcasts",
        "podcast": {
          "id": "2aba49dc3fc04e3e96fe89f79a261798",
          "image": "https://cdn-images-1.listennotes.com/podcasts/recode-media-recode-h9zPK_1UkdB-1iPwTajLXlS.1400x1400.jpg",
          "title": "Recode Media",
          "publisher": "Recode",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/recode-media-recode-eHTVnkiXyu9-1iPwTajLXlS.300x300.jpg",
          "listen_score": 55,
          "listennotes_url": "https://www.listennotes.com/c/2aba49dc3fc04e3e96fe89f79a261798/",
          "listen_score_global_rank": "0.5%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/recode-media-recode-eHTVnkiXyu9-1iPwTajLXlS.300x300.jpg",
        "description": "<p>Spotify is buying Bill Simmons\u2019 sports and pop culture website and podcast network, The Ringer. It\u2019s Spotify\u2019s fourth podcast acquisition in a year. Recode\u2019s Peter Kafka (who broke the story) sits down with Vox Media Podcast Network producer and former Ringer staff member Zach Mack to discuss what this deal means for Spotify, The Ringer and the future of podcasts.</p><p><br /></p><p><strong>Featuring</strong>: Zach Mack (<a href=\"https://twitter.com/zachthemack\">@zachthemack</a>), Senior Podcast Producer at Vox Media Podcast Network</p><p><strong>Host</strong>: Peter Kafka\u00a0(<a href=\"https://twitter.com/pkafka\">@pkafka</a>), Senior Editor at Recode</p><p><strong>More to explore</strong>: <a href=\"https://pod.link/1080467174\">Subscribe for free to Recode Media</a>, Peter Kafka, one of the media industry's most acclaimed reporters, talks to business titans, journalists, comedians, and more to get their take on today's media landscape.</p><p><strong>About Recode by Vox</strong>: Recode by Vox helps you understand how tech is changing the world \u2014 and changing us.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
        "pub_date_ms": 1581021870132,
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
          "listen_score_global_rank": "0.1%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/a16z-podcast-andreessen-horowitz-3bPEYm06XuR-IWF2alEr-9h.300x300.jpg",
        "description": "<p>\"Hi everyone, welcome to the a16z Podcast...\" ... and welcome to our 500th episode, where, for the first time, we reveal behind-the-scenes details and the backstory of how we built this show, and the broader editorial operation. [You can also listen to episode 499, with head of marketing Margit Wennmachers, on building the a16z brand, <a href=\"https://a16z.com/2019/11/20/brand-building-a16z-ideas-people-marketing/\" target=\"_blank\">here</a>.]</p><p>We've talked a lot about the podcasting industry, and even done podcasts about podcasting, so for this special episode, editor-in-chief and showrunner Sonal Chokshi reveals the how, what, and why in conversation with a16z general partner (and guest-host for this special episode) <a href=\"https://a16z.com/2019/10/01/knowable-audio-startups/\" target=\"_blank\">podcasting</a> fan Connie Chan. We also answer some frequently asked questions that we often get (and recently <a href=\"https://twitter.com/smc90/status/1198026729421324289\" target=\"_blank\">got</a> via Twitter), such as:</p><ul><li>how we program podcasts</li><li>what's the process, from ideas to publishing</li><li>do we edit them and how!</li><li>do guests prep, do we have a script</li><li>technical stack</li></ul><p>...and much more. In fact, much of the conversation goes beyond the a16z Podcast and towards Sonal's broader principles of 'editorial content marketing', which hopefully helps those thinking about their own content operations and podcasts, too. Including where podcasting may be going.</p><p>Finally, we share some unexpected moments, and lessons learned along the way; our positions on \"tics\", swear-words, and talking too fast; failed experiments, and new directions. But most importantly, we share some of the people behind the scenes who help make the a16z Podcast what it was, is, and can be... with thanks most of all to *you*, our wonderful fans!</p>",
        "pub_date_ms": 1574838000168,
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
        "link": "https://www.instagram.com/tboypod?utm_source=listennotes.com&utm_campaign=Listen+Notes&utm_medium=website",
        "audio": "https://www.listennotes.com/e/p/1ca5d330311d4808a4dbc668680f565b/",
        "image": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-Yw2Q5dIpK3A-kmx0XIZTAys.1400x1400.jpg",
        "title": "*Live* at Spotify - Part II: Why Spotify is doing podcasts \u2014 Our interview with Max Cutler,  Founder & MD of podcasts at Spotify",
        "podcast": {
          "id": "c5ce6c02cbf1486496206829f7d42e8e",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-Yw2Q5dIpK3A-kmx0XIZTAys.1400x1400.jpg",
          "title": "The Best One Yet",
          "publisher": "Nick & Jack Studios",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-KlIFOa-dpRW-kmx0XIZTAys.300x300.jpg",
          "listen_score": 73,
          "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
          "listen_score_global_rank": "0.05%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-KlIFOa-dpRW-kmx0XIZTAys.300x300.jpg",
        "description": "<p>The 2nd half of our Snacks recording live from Spotify. We sit down with Max Cutler, the Founder &amp; MD of Parcast Studios at Spotify \u2014 his startup was acquired by Spotify earlier this year. We\u2019re asking about how he first pitched his company, whether podcasts will follow the Netflix strategy, and what his favorite pod is. Ever.</p><p><br /></p><p><br /></p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
        "pub_date_ms": 1574852400619,
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-Yw2Q5dIpK3A-kmx0XIZTAys.1400x1400.jpg",
        "title": "*Live* at Spotify - Part I: How we build this (every day)",
        "podcast": {
          "id": "c5ce6c02cbf1486496206829f7d42e8e",
          "image": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-Yw2Q5dIpK3A-kmx0XIZTAys.1400x1400.jpg",
          "title": "The Best One Yet",
          "publisher": "Nick & Jack Studios",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-KlIFOa-dpRW-kmx0XIZTAys.300x300.jpg",
          "listen_score": 73,
          "listennotes_url": "https://www.listennotes.com/c/c5ce6c02cbf1486496206829f7d42e8e/",
          "listen_score_global_rank": "0.05%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/the-best-one-yet-nick-jack-studios-KlIFOa-dpRW-kmx0XIZTAys.300x300.jpg",
        "description": "<p>Spotify invited us to their NYC offices to record a live podcast \u2014 it\u2019s a podcast about podcasts for our podcast listening Snackers. We introduce to the Snackers how we got into podcasting, how we built this podcast (every day), and the 5 ingredients for a podcast that people will actually listen to.\u00a0</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://podcastchoices.com/adchoices\">podcastchoices.com/adchoices</a></p>",
        "pub_date_ms": 1574420400622,
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
          "listen_score": 45,
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/demandgen-radio-bdo-digital-llc-ufxFwTAZDqp-oVByO3tuFwR.1400x1400.jpg",
        "title": "#129 How to Build your Brand with Podcasting",
        "podcast": {
          "id": "f446a0eaac2e481991e36467e4a4f96f",
          "image": "https://cdn-images-1.listennotes.com/podcasts/demandgen-radio-bdo-digital-llc-ufxFwTAZDqp-oVByO3tuFwR.1400x1400.jpg",
          "title": "DemandGen Radio",
          "publisher": "BDO Digital, LLC",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/demandgen-radio-bdo-digital-llc-Q8LPFuqxXwN-oVByO3tuFwR.300x300.jpg",
          "listen_score": 37,
          "listennotes_url": "https://www.listennotes.com/c/f446a0eaac2e481991e36467e4a4f96f/",
          "listen_score_global_rank": "2.5%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/demandgen-radio-bdo-digital-llc-Q8LPFuqxXwN-oVByO3tuFwR.300x300.jpg",
        "description": "<p></p>\n\n<p>Jordan Paris is a 21-year-old entrepreneur who runs a wildly successful podcast. In this episode, he shares how and why he started his podcast and how podcasting propelled the growth of his business and personal brand. Tune in as Jordan shares how he remains so driven and accomplished at an early age, what lessons he\u2019s learned from starting his podcast, and how you can benefit from starting your own podcast.</p>",
        "pub_date_ms": 1569146400123,
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
          "listen_score": 49,
          "listennotes_url": "https://www.listennotes.com/c/841eca7a25c64420b2bd0b536d35108d/",
          "listen_score_global_rank": "1%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/cold-call-hbr-presents-brian-kenny-egRtK2b1Odo-sC2kfX7gM0D.300x300.jpg",
        "description": "<p>Harvard Business School professors <strong><a href=\"https://www.hbs.edu/faculty/Pages/profile.aspx?facId=6446\" rel=\"noopener\" target=\"_blank\">John Deighton</a></strong> and <strong><a href=\"https://www.hbs.edu/faculty/Pages/profile.aspx?facId=6536\" rel=\"noopener\" target=\"_blank\">Jeffrey Rayport</a></strong> discuss their case, &#8220;<a href=\"https://store.hbr.org/product/gimlet-media-a-podcasting-startup/918413?sku=918413-PDF-ENG\" rel=\"noopener\" target=\"_blank\">Gimlet Media: A Podcasting Startup</a>,&#8221; and how two former public radio producers launch a podcast network, entering the last frontier of digital media. Can they turn a content supplier into a disruptive platform?</p>",
        "pub_date_ms": 1569948476075,
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/function-with-anil/the-wild-world-of-podcast-ads--OEJf2RUIkX-igyS-B5r24A.1400x1400.jpg",
        "title": "The Wild World of Podcast Ads",
        "podcast": {
          "id": "3b7c6c851ec14f40bb062b918942aa15",
          "image": "https://cdn-images-1.listennotes.com/podcasts/function-with-anil-dash-vox-media-3DjNoAIGtV_-pfqIzGD4odn.1400x1400.jpg",
          "title": "Function with Anil Dash",
          "publisher": "Vox Media",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/function-with-anil-dash-vox-media-yYP_8KQFk06-pfqIzGD4odn.300x300.jpg",
          "listen_score": 44,
          "listennotes_url": "https://www.listennotes.com/c/3b7c6c851ec14f40bb062b918942aa15/",
          "listen_score_global_rank": "1.5%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/function-with-anil/the-wild-world-of-podcast-ads-Rj6u3btNrmq-igyS-B5r24A.300x300.jpg",
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
        "image": "https://cdn-images-1.listennotes.com/podcasts/chinatalk/learning-to-listen-chinas-XMHm1o4TaF7-LoO0UAa_G4e.1400x1400.jpg",
        "title": "Learning to listen: China's billion-dollar podcast industry",
        "podcast": {
          "id": "5cd3fe3fc0c04c8da9abf4a6fb897a31",
          "image": "https://cdn-images-1.listennotes.com/podcasts/chinatalk-jordan-schneider-G41S7oZEiN6-Jz4DAyqm9ZV.1400x1400.jpg",
          "title": "ChinaTalk",
          "publisher": "Jordan Schneider",
          "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/chinatalk-jordan-schneider-6qKWn7IxJPT-Jz4DAyqm9ZV.300x300.jpg",
          "listen_score": 37,
          "listennotes_url": "https://www.listennotes.com/c/5cd3fe3fc0c04c8da9abf4a6fb897a31/",
          "listen_score_global_rank": "2.5%"
        },
        "thumbnail": "https://cdn-images-1.listennotes.com/podcasts/chinatalk/learning-to-listen-chinas-IH4eKfwDyT6-LoO0UAa_G4e.300x300.jpg",
        "description": "While it may be a pipe dream for ChinaEconTalk to ever merit a billion-dollar price tag, in China, podcast \u201cunicorns\u201d are everywhere. Companies like Ximalaya and Yudao have multibillion-dollar valuations, but feature startlingly different content from what consumers expect in the West. What drives these differences, and what does the future hold for spoken audio in China? To answer these questions, Yi Yang, a young podcast host and founder of the Mandarin-language podcast startup JustPod \u64ad\u5ba2\u4e00\u4e0b, joins Jordan to explain how, after the advent of podcasts in China, people are finally \u201clearning to listen.\u201d Yi Yang's original podcast is called LeftRight\u00a0\u5ffd\u5de6\u5ffd\u53f3. His two branded podcasts are\u00a0Startup Insider\u00a0\u521b\u4e1a\u5185\u5e55 and Bessie\u2019s Notes\u00a0\u8d1d\u671b\u5f55. ChinaEconTalk's newsletter is dope. Sign up here at\u00a0www.chinaecontalk.substack.com. The latest issues include an analysis of why Amazon lost in China and learn about the bane of China\u2019s automobile industry. <a href=\"https://open.acast.com/public/patreon/fanSubscribe/1959352\">Get bonus content on Patreon</a><br /><p> See <a href=\"https://acast.com/privacy\">acast.com/privacy</a> for privacy and opt-out information.</p><p> </p><p>Learn more about your ad choices. Visit <a href=\"https://megaphone.fm/adchoices\">megaphone.fm/adchoices</a></p>",
        "pub_date_ms": 1562795773162,
        "guid_from_rss": "807301962fd14ffdbd8392824f6f1e5f",
        "listennotes_url": "https://www.listennotes.com/e/89765fa2bee24603a93b4098830c4efa/",
        "audio_length_sec": 3000,
        "explicit_content": false,
        "maybe_audio_invalid": false,
        "listennotes_edit_url": "https://www.listennotes.com/e/89765fa2bee24603a93b4098830c4efa/#edit"
      },
      "type": "episode",
      "notes": "",
      "added_at_ms": 1564614350360
    }
  ],
  "total": 37,
  "thumbnail": "https://cdn-images-1.listennotes.com/podcast-playlists/podcasts-about-podcasting-0LlKxjtQnf1-m1pe7z60bsw.300x300.jpg",
  "visibility": "public",
  "description": "A curated playlist of podcasts by Wenbin Fang.",
  "listennotes_url": "https://www.listennotes.com/playlists/podcasts-about-podcasting-m1pe7z60bsw/episodes/",
  "last_timestamp_ms": 1564614350360,
  "total_audio_length_sec": 108657
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

See all available parameters on the [API Docs page](https://www.listennotes.com/podcast-api/docs/#get-api-v2-playlists).


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
      "image": "https://cdn-images-1.listennotes.com/podcast-playlists/wenbin-fangs-podcast-playlist-aIykg5GvmcA-kr3-ta28cJu.300x299.jpg",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcast-playlists/wenbin-fangs-podcast-playlist-aIykg5GvmcA-kr3-ta28cJu.300x299.jpg",
      "visibility": "public",
      "description": "Wenbin Fang\u2019s master playlist. Just listen to individual episodes, rather than subscribing to tons of podcasts. How I listen to podcasts: https://lnns.co/6ArPszTwvDE",
      "episode_count": 5536,
      "podcast_count": 70,
      "listennotes_url": "https://www.listennotes.com/playlists/wenbin-fangs-podcast-playlist-kr3-ta28cJu/episodes/",
      "total_audio_length_sec": 16465279
    },
    {
      "id": "m1pe7z60bsw",
      "name": "Podcasts about podcasting",
      "image": "https://cdn-images-1.listennotes.com/podcast-playlists/podcasts-about-podcasting-4bU7MZIlEVO-m1pe7z60bsw.1600x1600.jpg",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcast-playlists/podcasts-about-podcasting-0LlKxjtQnf1-m1pe7z60bsw.300x300.jpg",
      "visibility": "public",
      "description": "A curated playlist of podcasts by Wenbin Fang.",
      "episode_count": 37,
      "podcast_count": 2,
      "listennotes_url": "https://www.listennotes.com/playlists/podcasts-about-podcasting-m1pe7z60bsw/episodes/",
      "total_audio_length_sec": 108657
    },
    {
      "id": "uIK85BM6EWJ",
      "name": "There's a podcast for that",
      "image": "https://cdn-images-1.listennotes.com/podcast-playlists/theres-a-podcast-for-that-ROmWwgXrJhc-uIK85BM6EWJ.300x300.jpg",
      "thumbnail": "https://cdn-images-1.listennotes.com/podcast-playlists/theres-a-podcast-for-that-ROmWwgXrJhc-uIK85BM6EWJ.300x300.jpg",
      "visibility": "public",
      "description": "Inspired by \"There's an app for that\". Email me if you want to become a contributor of this list: hello@listennotes.com",
      "episode_count": 0,
      "podcast_count": 132,
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

See all available parameters on the [API Docs page](https://www.listennotes.com/podcast-api/docs/#get-api-v2-trending_searches).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "terms": [
    "Donald Hoffman",
    "Judith Barsi",
    "Peter Santenello",
    "Mark Bowden",
    "Aswath Damodaran",
    "Jenny Odell",
    "Lex Fridman",
    "Chelsea Handler",
    "Digital Nomad",
    "Sheryl Sandberg"
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

See all available parameters on the [API Docs page](https://www.listennotes.com/podcast-api/docs/#get-api-v2-related_searches).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "terms": [
    "evergrande stock",
    "evergrande news",
    "evergrande default",
    "evergrande china",
    "evergrande crisis",
    "evergrande collapse",
    "evergrande stock price",
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

See all available parameters on the [API Docs page](https://www.listennotes.com/podcast-api/docs/#get-api-v2-spellcheck).


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

See all available parameters on the [API Docs page](https://www.listennotes.com/podcast-api/docs/#get-api-v2-podcasts-id-audience).


<details>
  <summary>Click to see example response</summary>
  
```json
{
  "by_regions": [
    {
      "ratio": "52.77%",
      "region": "us"
    },
    {
      "ratio": "6.60%",
      "region": "ca"
    },
    {
      "ratio": "6.03%",
      "region": "gb"
    },
    {
      "ratio": "4.79%",
      "region": "in"
    },
    {
      "ratio": "4.13%",
      "region": "au"
    },
    {
      "ratio": "2.93%",
      "region": "de"
    },
    {
      "ratio": "1.33%",
      "region": "fr"
    },
    {
      "ratio": "1.23%",
      "region": "sg"
    },
    {
      "ratio": "1.18%",
      "region": "nl"
    },
    {
      "ratio": "0.88%",
      "region": "es"
    },
    {
      "ratio": "0.85%",
      "region": "za"
    },
    {
      "ratio": "0.81%",
      "region": "br"
    },
    {
      "ratio": "0.71%",
      "region": "pl"
    },
    {
      "ratio": "0.69%",
      "region": "se"
    },
    {
      "ratio": "0.61%",
      "region": "nz"
    },
    {
      "ratio": "0.60%",
      "region": "hk"
    },
    {
      "ratio": "0.59%",
      "region": "ie"
    },
    {
      "ratio": "0.53%",
      "region": "it"
    },
    {
      "ratio": "0.51%",
      "region": "ch"
    },
    {
      "ratio": "0.49%",
      "region": "ph"
    },
    {
      "ratio": "0.47%",
      "region": "jp"
    },
    {
      "ratio": "0.44%",
      "region": "id"
    },
    {
      "ratio": "0.44%",
      "region": "ru"
    },
    {
      "ratio": "0.42%",
      "region": "pt"
    },
    {
      "ratio": "0.41%",
      "region": "mx"
    },
    {
      "ratio": "0.39%",
      "region": "tw"
    },
    {
      "ratio": "0.38%",
      "region": "be"
    },
    {
      "ratio": "0.37%",
      "region": "ro"
    },
    {
      "ratio": "0.36%",
      "region": "fi"
    },
    {
      "ratio": "0.34%",
      "region": "at"
    },
    {
      "ratio": "0.34%",
      "region": "no"
    },
    {
      "ratio": "0.33%",
      "region": "il"
    },
    {
      "ratio": "0.33%",
      "region": "pk"
    },
    {
      "ratio": "0.31%",
      "region": "cz"
    },
    {
      "ratio": "0.30%",
      "region": "dk"
    },
    {
      "ratio": "0.30%",
      "region": "gr"
    },
    {
      "ratio": "0.27%",
      "region": "vn"
    },
    {
      "ratio": "0.27%",
      "region": "th"
    },
    {
      "ratio": "0.25%",
      "region": "ua"
    },
    {
      "ratio": "0.24%",
      "region": "ae"
    },
    {
      "ratio": "0.20%",
      "region": "bg"
    },
    {
      "ratio": "0.20%",
      "region": "my"
    },
    {
      "ratio": "0.19%",
      "region": "kr"
    },
    {
      "ratio": "0.18%",
      "region": "sk"
    },
    {
      "ratio": "0.18%",
      "region": "sa"
    },
    {
      "ratio": "0.18%",
      "region": "tr"
    },
    {
      "ratio": "0.17%",
      "region": "hr"
    },
    {
      "ratio": "0.17%",
      "region": "ar"
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
      "region": "ee"
    },
    {
      "ratio": "0.11%",
      "region": "cl"
    },
    {
      "ratio": "0.11%",
      "region": "ng"
    },
    {
      "ratio": "0.11%",
      "region": "ke"
    },
    {
      "ratio": "0.11%",
      "region": "si"
    },
    {
      "ratio": "0.10%",
      "region": "md"
    },
    {
      "ratio": "0.10%",
      "region": "rs"
    },
    {
      "ratio": "2.26%",
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



