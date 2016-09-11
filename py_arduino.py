import json
from pprint import pprint
import pymongo

#open txt
#with open('2014_data.txt') as data_file:
#    data = json.load(data_file)

#store as votes #year, id, rest of fields
dict_new = []
#for key,value in data.iteritems():
#    for zz in value['votes']:
#        dict_new.append({
#            'year':2014,
#            'voting_session':key,
#            'voter_name':zz[0],
#            'voter_id':zz[1],
#            'voter_party':zz[2],
#            'voter_state':zz[3],
#            'voter_vote': zz[4],
#        })



#store in Mlab
#connection = pymongo.MongoClient('mongodb://hello123:hello123@ds023664.mlab.com:23664/votes123')
connection = pymongo.MongoClient('ds059284.mlab.com', 59284)
db = connection['articles']
db.authenticate('techfest', 'techfest')


db = connection.articles.test




#db.insert(dict1)