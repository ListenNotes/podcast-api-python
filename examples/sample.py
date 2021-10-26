import json
import os

from listennotes import podcast_api, errors

# Get your api key here: https://www.listennotes.com/api/dashboard/
api_key = os.environ.get("LISTEN_API_KEY", None)

client = podcast_api.Client(api_key=api_key)

#
# Boilerplate to make an api call
#
try:
    response = client.typeahead(q="startup", show_podcasts=1)
    print(json.dumps(response.json(), indent=2))
except errors.APIConnectionError:
    print("Failed ot connect to Listen API servers")
except errors.AuthenticationError:
    print("Wrong api key, or your account has been suspended!")
except errors.InvalidRequestError:
    print("Wrong parameters!")
except errors.NotFoundError:
    print("Endpoint not exist or the podcast / episode not exist!")
except errors.RateLimitError:
    print("You have reached your quota limit!")
except errors.ListenApiError:
    print("Something wrong on Listen Notes servers")
except Exception:
    print("Other errors that may not be related to Listen API")
else:
    headers = response.headers
    print("\n=== Some account info ===")
    print(
        "Free Quota this month: %s requests"
        % headers.get("X-ListenAPI-FreeQuota")
    )
    print("Usage this month: %s requests" % headers.get("X-ListenAPI-Usage"))
    print("Next billing date: %s" % headers.get("X-Listenapi-NextBillingDate"))

# response = client.search(q='startup')
# print(response.json())

# response = client.spellcheck(q='evergrand stok')
# print(response.json())

# response = client.fetch_related_searches(q='evergrande')
# print(response.json())

# response = client.fetch_trending_searches()
# print(response.json())

# response = client.fetch_best_podcasts()
# print(response.json())

# response = client.fetch_best_podcasts()
# print(response.json())

# response = client.fetch_podcast_by_id(id='4d3fe717742d4963a85562e9f84d8c79')
# print(response.json())

# response = client.fetch_episode_by_id(id='6b6d65930c5a4f71b254465871fed370')
# print(response.json())

# response = client.batch_fetch_episodes(ids='c577d55b2b2b483c969fae3ceb58e362,0f34a9099579490993eec9e8c8cebb82')
# print(response.json())

# response = client.batch_fetch_podcasts(ids='3302bc71139541baa46ecb27dbf6071a,68faf62be97149c280ebcc25178aa731,'
#                                            '37589a3e121e40debe4cef3d9638932a,9cf19c590ff0484d97b18b329fed0c6a')
# print(response.json())

# response = client.fetch_curated_podcasts_list_by_id(id='SDFKduyJ47r')
# print(response.json())

# response = client.fetch_curated_podcasts_lists(page=2)
# print(response.json())

# response = client.fetch_curated_podcasts_lists(page=2)
# print(response.json())

# response = client.fetch_podcast_genres(top_level_only=0)
# print(response.json())

# response = client.fetch_podcast_regions()
# print(response.json())

# response = client.fetch_podcast_languages()
# print(response.json())

# response = client.just_listen()
# print(response.json())

# response = client.fetch_recommendations_for_podcast(id='25212ac3c53240a880dd5032e547047b', safe_mode=1)
# print(response.json())

# response = client.fetch_recommendations_for_episode(id='914a9deafa5340eeaa2859c77f275799', safe_mode=1)
# print(response.json())

# response = client.fetch_playlist_by_id(id='m1pe7z60bsw', type='podcast_list')
# print(response.json())

# response = client.fetch_my_playlists()
# print(response.json())

# response = client.submit_podcast(rss='https://feeds.megaphone.fm/committed')
# print(response.json())

# response = client.delete_podcast(
#     id='4d3fe717742d4963a85562e9f84d8c79', reason='the podcaster wants to delete it')
# print(response.json())
