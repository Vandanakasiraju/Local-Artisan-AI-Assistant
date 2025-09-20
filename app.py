from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- 1. Simulated AI Logic for Listing Creation ---
def generate_listing(keywords):
    """Generates a title and description based on input keywords."""
    keywords_lower = keywords.lower()
    
    # Simple, hardcoded generation logic based on keywords
    if "walnut" in keywords_lower and "bowl" in keywords_lower:
        title = "Sustainable Hand-Carved Walnut Wood Bowl"
        description = "Elevate your kitchen with this stunning, food-safe walnut wood bowl. Hand-carved by local artisans, it makes a perfect centerpiece or gift."
    elif "silver" in keywords_lower and "necklace" in keywords_lower:
        title = "Sterling Silver Initial Pendant Necklace - Custom Artisan Jewelry"
        description = "A minimalist and elegant sterling silver necklace. This piece is handcrafted with care and can be customized with your initial."
    else:
        title = "Unique Handcrafted Artisan Item"
        description = "A beautiful item crafted with care by a local artisan. Input more details for a better description!"

    return title, description

# --- 2. Simulated AI Logic for FAQ Chatbot ---
faq_responses = {
    "shipping": "We typically ship within 2-3 business days. Standard delivery takes 5-7 days domestically.",
    "return": "Yes, we accept returns within 30 days for unused items. Please include your order number.",
    "material": "This product is made from locally sourced, sustainable materials as listed in the description.",
    "default": "I'm the Marketplace Assistant! I can answer questions about shipping, returns, or materials. How can I help?"
}

def get_faq_response(user_input):
    """Returns a canned response based on keywords in the user's message."""
    input_lower = user_input.lower()
    if "ship" in input_lower or "delivery" in input_lower:
        return faq_responses["shipping"]
    elif "return" in input_lower or "refund" in input_lower:
        return faq_responses["return"]
    elif "material" in input_lower or "made of" in input_lower:
        return faq_responses["material"]
    else:
        return faq_responses["default"]

# --- Flask Routes ---
@app.route('/')
def index():
    """Renders the main HTML page."""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def handle_generate():
    """Endpoint for the listing creation tool."""
    keywords = request.form['keywords']
    title, description = generate_listing(keywords)
    return jsonify({'title': title, 'description': description})

@app.route('/chat', methods=['POST'])
def handle_chat():
    """Endpoint for the chatbot."""
    user_message = request.json['message']
    response = get_faq_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    # Set debug=True for easy development
    app.run(debug=True)
