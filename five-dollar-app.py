from flask import Flask, render_template
from pymongo import MongoClient


MONGODB_URI = "mongodb+srv://michellevillagomez9_db_user:jR2ooWuBCbH6rETu@lunch-db.wwffuvo.mongodb.net/?appName=lunch-db"
client = MongoClient(MONGODB_URI)

db = client["5-dollar"]
collection = db["food"]
app = Flask(__name__)

"""
data = [
    {
    "name": "Subway",
    "price" : 8.99,
    "image_url" : "https://www.bing.com/images/search?view=detailV2&ccid=g70ALVcC&id=C1EE3A1E5FF2DF9FE089BB4D08ED294063D51C32&thid=OIP.g70ALVcCgFYVIm1Drkof1AHaFV&mediaurl=https%3a%2f%2fassets3.thrillist.com%2fv1%2fimage%2f3076005%2f1200x600%2fscale%3b%3bwebp%3dauto%3bjpeg_quality%3d85.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.83bd002d5702805615226d43ae4a1fd4%3frik%3dMhzVY0Ap7QhNuw%26pid%3dImgRaw%26r%3d0&exph=600&expw=833&q=subway&FORM=IRPRST&ck=6ADF647616E0F81A1116F4B2C8AA1B6F&selectedIndex=1&itb=0"
    },
    {
    "name": "Starbucks",
    "price" : 4.99,
    "image_url" : "https://www.bing.com/images/search?view=detailV2&ccid=JPmj3sVS&id=D830D5F5FE2C8895E778FA1FA34E8261C4806397&thid=OIP.JPmj3sVSXsVLc2zQ6BD15gHaFu&mediaurl=https%3a%2f%2fabout.starbucks.com%2fuploads%2fsites%2f9%2f2025%2f07%2fSBX20250327_06495_Sum25_InStore_FrappColdFoamTrio-ToGo_CMYK-1.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.24f9a3dec5525ec54b736cd0e810f5e6%3frik%3dl2OAxGGCTqMf%252bg%26pid%3dImgRaw%26r%3d0&exph=1205&expw=1558&q=starbucks&FORM=IRPRST&ck=5003A5D17907A5D05C34BF213A0EB166&selectedIndex=1&itb=0"
    },
    {
    "name": "Roundtable Pizza",
    "price" : 5.99,
    "image_url" : "https://www.bing.com/images/search?view=detailV2&ccid=mDBXeIGZ&id=31D9507644E10B2080E1AC34644F37246DE720A5&thid=OIP.mDBXeIGZekWHfgqaP3vg7AHaHa&mediaurl=https%3a%2f%2fimages.sirved.com%2fChIJU_pgs18ZnlQRaaOV6n1VApE%2f4b9BT61cHq.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.9830577881997a45877e0a9a3f7be0ec%3frik%3dpSDnbSQ3T2Q0rA%26pid%3dImgRaw%26r%3d0&exph=1080&expw=1080&q=rountable+pizza&FORM=IRPRST&ck=2204A5258EFAC4F40F0AC29F60469A02&selectedIndex=17&itb=0"
    },
    {
    "name": "Panda Express",
    "price" : 10.99,
    "image_url" : "https://www.bing.com/images/search?view=detailV2&ccid=bNire9PJ&id=25D1DEFA346F46AF63451BCCF425D8A8AD31B0B2&thid=OIP.bNire9PJ2FxhAEuLuaG3HgHaF7&mediaurl=https%3a%2f%2ftb-static.uber.com%2fprod%2fimage-proc%2fprocessed_images%2f90929af4384b30c368b4e7a13e98d2f7%2f885ba8620d45ab36746a0e8c7b85ee66.jpeg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.6cd8ab7bd3c9d85c61004b8bb9a1b71e%3frik%3dsrAxrajYJfTMGw%26pid%3dImgRaw%26r%3d0&exph=2304&expw=2880&q=panda+express&FORM=IRPRST&ck=AF13EB68089D5E3744F28D938E33BE34&selectedIndex=0&itb=0"
    },

]
"""


@app.route("/")
def start_index():
    return render_template("index.html")

@app.route("/welcome") # mapping
def welcome():
    return "Welcome to CS4800"


@app.route("/search/<budget>") # mapping
def search_food_items(budget):
    budget = float(budget)
    result = []
    for food in collection.find():
        if food['price'] <= budget:
            food["_id"] = str(food["_id"])
            result.append(food)
    print(result)
    return result

app.run(host = "0.0.0.0")