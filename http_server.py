from flask import Flask, request
import requests
import argparse
import json
from src.sns_message_verification import valid_sns_message

app = Flask(__name__)


def handle_event_subscribe_confirmation(data):
    subscribe_url = data.get("SubscribeURL")
    print(subscribe_url)
    if subscribe_url:

        # Make a GET request to the SubscribeURL
        response = requests.get(subscribe_url)

        # Check the response status
        if response.status_code == 200:
            return "Subscription confirmed successfully!"
        else:
            return "Failed to confirm subscription."

    else:
        return "SubscribeURL not found in the request data."


def handle_event_subscribe_unconfirmation(data):
    print(
        "recv event subscribe_unconfirmation.\
        topic: {}, message_id: {}, message: {}".format(
            data.get("TopicArn"), data.get("MessageId"), data.get("Message")
        )
    )


def handle_event_notification(data):

    topic = data.get("TopicArn")
    subject = data.get("Subject")
    message_id = data.get("MessageId")
    message = data.get("Message")
    print(
        "recv topic: {}, subject: {} message_id : {}, message: {}.".format(
            topic, subject, message_id, message
        )
    )
    return "Recive notification successfully!"


@app.route("/", methods=["GET"])
def say_hi():
    return "hi"


@app.route("/sns/event", methods=["POST"])
def callback_confirmation():
    # Get the data from the POST request
    try:

        # x-amz-sns-message-type
        data = None
        content_type = request.headers["Content-Type"]
        if "text/plain" in content_type.lower():
            data = json.loads(request.data.decode("utf-8"))
        elif "application/json" in content_type.lower():
            data = request.get_json()
        else:
            raise Exception("UNHandle Content-Type: {}".format(content_type))

        # 1, Sign Verification.
        if not valid_sns_message(data):
            print("data not valid. data: {}".format(data))

        # 2, Handle sns event
        message_type = data.get("Type")
        # Event Enum:
        #   SubscriptionConfirmation
        #   Notification
        #   UnsubscribeConfirmation
        if message_type == "SubscriptionConfirmation":
            return handle_event_subscribe_confirmation(data)
        elif message_type == "UnsubscribeConfirmation":
            return handle_event_subscribe_unconfirmation(data)
        elif message_type == "Notification":
            return handle_event_notification(data)

    except Exception as err:
        print("callback_confirmation err: {}".format(err))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HTTP SERVER FOR Handling SNS EVENT")
    parser.add_argument("--port", help="Htpp Server Port.", required=True)

    args = parser.parse_args()
    app.run(debug=True, host="0.0.0.0", port=int(args.port))
