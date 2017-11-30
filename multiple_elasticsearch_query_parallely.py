import thread
import time
import json
from elasticsearch import Elasticsearch

# Define a function for the thread
def print_time( name, delay):
    time.sleep(delay)
    result = es.search(index="new", body={"size": 500, "query": {"match_phrase": {"Name": name}}})
    for i in result['hits']['hits']:
        print "Age : " + i['_source']['Age']

# Create threads as follows
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
result = es.search(index="new", body={"size": 10, "query": {"match_all": {}}})

try:
    thread.start_new_thread( print_time, (result['hits']['hits'][0]['_source']['Name'], 2 ) )
    print result['hits']['hits'][0]['_source']['Name']
    thread.start_new_thread( print_time, (result['hits']['hits'][1]['_source']['Name'], 2 ) )
    print result['hits']['hits'][1]['_source']['Name']
    thread.start_new_thread( print_time, (result['hits']['hits'][2]['_source']['Name'], 2 ) )
    print result['hits']['hits'][2]['_source']['Name']
    thread.start_new_thread( print_time, (result['hits']['hits'][3]['_source']['Name'], 2 ) )
    print result['hits']['hits'][3]['_source']['Name']
    thread.start_new_thread( print_time, (result['hits']['hits'][4]['_source']['Name'], 2 ) )
    print result['hits']['hits'][4]['_source']['Name']
    thread.start_new_thread( print_time, (result['hits']['hits'][5]['_source']['Name'], 2 ) )
    print result['hits']['hits'][5]['_source']['Name']
except:
    print "Error: unable to start thread"

while 1:
    pass