# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = 'YOUR ACCESS TOKEN"'
ACCESS_SECRET = 'YOUR ACCESS TOKEN SECRET'
CONSUMER_KEY = 'YOUR API KEY'
CONSUMER_SECRET = 'ENTER YOUR API SECRET'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter REST API
twitter = Twitter(auth=oauth)

###############################################
# Search API            
# Search for latest tweets about "#nlproc"
twitter.search.tweets(q='#nlproc')

# Search for 10 latest tweets about “#nlproc” in English
twitter.search.tweets(q='#nlproc', result_type='recent', lang='en', count=10)

###############################################
# Trends API
# Request worldwide trends
world_trends = twitter.trends.available(_woeid=1)

# Get all (it's always 10) trending topics in San Francisco (its WOEID is 2487956)
sfo_trends = twitter.trends.place(_id = 2487956)
print json.dumps(sfo_trends, indent=4))

###############################################
# User API
# Get a list of followers of a particular user
twitter.followers.ids(screen_name="cocoweixu")

# Get a particular user's timeline (up to 3,200 of his/her most recent tweets)
twitter.statuses.user_timeline(screen_name="billybob")

###############################################
# Check your remaining quota (rate limit)
twitter.application.rate_limit_status()
