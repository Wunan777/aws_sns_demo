from flask import Flask, request
import requests

app = Flask(__name__)


@app.route("/sns/callback/confirmation", methods=["POST"])
def callback_confirmation():
    # Get the data from the POST request
    try:

        print(request)
        data = request.get_json()
        print(data)
        # Extract the SubscribeURL from the data
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

    except Exception as err:
        print("callback_confirmation err: {}".format(err))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8170")
