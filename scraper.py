# %%
import pandas as pd
from apify_client import ApifyClient

apify_client = ApifyClient('TOKEN')  # use APIFY token
df = pd.read_csv("twitter_handles_random.csv")  # read the file with handles
handle_list = df['Twitter Handle'].values.tolist()
# %%
# set the config for search
for handle in handle_list:
    search_param = {
        "handle": [handle],
        "searchMode": "live",  # Getting Latest Post
        "tweetsDesired": 10000,  # max amount of tweeters for one profile
        "mode": "own",  # "own" for tweets only, "replies" for tweets and replies
        "profilesDesired": 200  # max amount of handles
    }

    # Run the search and get the result
    actor_call = apify_client.actor('quacker/twitter-scraper').call(run_input=search_param)
    dataset_items = apify_client.dataset(actor_call['defaultDatasetId']).list_items().items
    df_result = pd.DataFrame(dataset_items)
    df_result.to_csv(f"{handle[1:]}.csv")

