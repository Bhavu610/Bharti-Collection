from flask import Flask, render_template

app = Flask(__name__)

SHOP_INFO = {
    "shop_name": "Bharti Collection",
    "tagline": "Tradition Woven Into Every Thread",
    "address": "123 Vaishali Nagar, Jaipur, Rajasthan 302021",
    "phone": "+91 9352200732",
    "whatsapp": "919352200732"
}

PRODUCTS = [
    {
        "name": "Designer Sarees",
        "image": "https://images.unsplash.com/photo-1610030469983-98e550d6193c",
        "description": "Premium Banarasi, Silk & Georgette Sarees"
    },
    {
        "name": "Elegant Suits",
        "image": "https://images.unsplash.com/photo-1583391733981-8492b1c8f5b2",
        "description": "Designer Salwar Suits for Every Occasion"
    },
    {
        "name": "Bridal Lehengas",
        "image": "https://medias.utsavfashion.com/media/catalog/product/cache/1/image/1000x/040ec09b1e35df139433887a97daa66f/e/m/embroidered-net-lehenga-in-sky-blue-v1-lht73.jpg",
        "description": "Luxury Bridal & Party Wear Lehengas"
    },
    {
        "name": "Stylish Kurtis",
        "image": "https://th.bing.com/th/id/OIP.8RY3Mn53qm58frv67rZ23QHaMz?w=202&h=324&c=7&r=0&o=7&dpr=1.5&pid=1.7&rm=3",
        "description": "Daily Wear & Festive Kurti Collection"
    }
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        shop=SHOP_INFO,
        products=PRODUCTS
    )

if __name__ == "__main__":
    app.run(debug=True)