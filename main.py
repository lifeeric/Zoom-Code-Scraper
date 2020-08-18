import os
import requests

os.system('title [Zoom Code Scraper]')
scraped = 0


def save(text):
    print(text)
    with open('Codes.txt', 'a', encoding='UTF-8', errors='replace') as f:
        f.write(f'{text}\n')


HEADERS = {
    'x-twitter-client-language': 'en',
    'x-csrf-token': 'a750acadd9ea047b147bc355e4b912dc',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-active-user': 'yes',
    'accept': '*/*',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAA...',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/84.0.4147.125 Safari/537.36',
    'cookie': '...'  # Make sure the "ct0" cookie has the same value as the x-csrf-token header.
}

response = requests.get(
    'https://api.twitter.com/2/search/adaptive.json?include_profile_interstitial_type=1&include_blo'
    'cking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1'
    '&include_can_dm=1&include_can_media_tag=1&skip_status=1&cards_platform=Web-12&include_cards=1&'
    'include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&i'
    'nclude_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media'
    '_availability=true&send_error_codes=true&simple_quoted_tweet=true&q=zoom%20code&tweet_search_m'
    'ode=live&count=20&query_source=typed_query&pc=1&spelling_corrections=1&ext=mediaStats%2Chighli'
    'ghtedLabel', headers=HEADERS
)

for i in response.json()['globalObjects']['tweets'].values():
    content = i['full_text']
    if any(i in content for i in ['pass', 'code', 'raid', 'join']) and all(
        i not in content for i in ['#', '@']
    ):
        save(
            '[POSSIBLE]\n'
            f'{content}\n'
            '----------------------------------'
        )
        scraped += 1

    try:
        url = i['entities']['urls'][0]['expanded_url']
    except Exception:
        continue
    if 'us04web.zoom.us' in url and '?pwd=' in url:
        save(
            '[URL]\n'
            f'{url}\n'
            '----------------------------------'
        )
        scraped += 1
    elif 'us04web.zoom.us' in url and '?pwd=' not in url:
        save(
            '[URL AND TEXT]\n'
            f'URL: {url}\n'
            f'TEXT: {content}\n'
            '----------------------------------'
        )
        scraped += 1

os.system(f'title [Zoom Code Scraper] - Scraped: {scraped} && pause >NUL')
