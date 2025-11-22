from flask import Flask, request, jsonify
import razorpay
import os

app = Flask(__name__)

razorpay_client = razorpay.Client(
    auth=(os.getenv("KEY_ID"), os.getenv("KEY_SECRET"))
)

@app.route("/create-order", methods=["POST"])
def create_order():
    data = request.get_json() or {}
    amount = data.get("amount", 5000)
    currency = "INR"

    order = razorpay_client.order.create({
        "amount": int(amount),
        "currency": currency
    })

    return jsonify(order)

@app.route("/", methods=["GET"])
def home():
    return "Razorpay Python Backend Running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
