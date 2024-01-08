from flask import Flask, request
import os
from dotenv import load_dotenv
#from azure.identity import DefaultAzureCredential
from azure.core.credentials import AzureKeyCredential
from azure.eventgrid import EventGridPublisherClient, EventGridEvent
from flask import Flask, request

load_dotenv()

topic_key = os.getenv("EVENTGRID_TOPIC_KEY")
endpoint = os.getenv("EVENTGRID_TOPIC_ENDPOINT")

app = Flask(__name__)

@app.route('/create_eventgrid_topic', methods=['POST'])
def create_eventgrid_topic():
    topic_name = request.json.get('topic_name')
    resource_group_name = request.json.get('resource_group_name')
    location = request.json.get('location')

    #credential = DefaultAzureCredential(topic_key)
    credential = AzureKeyCredential(topic_key)
    eventgrid_client = EventGridPublisherClient(endpoint, credential)

    event = EventGridEvent(
        subject=topic_name,
        data=request.json,
        event_type="Testing",
        data_version="1.0"
    )

    eventgrid_client.send([event])

    return {"message": "Event sent successfully"}

@app.route('/')
def hello_world():
        return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    app.run()
