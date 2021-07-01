from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    items = [
    {'id': 1, 'name': 'Acer Swift 3', 'image': 'https://images-na.ssl-images-amazon.com/images/I/71W5ZdS%2BsEL._AC_SL1500_.jpg', 'html': 'https://www.amazon.com/Acer-Octa-Core-Graphics-Fingerprint-SF314-42-R9YN/dp/B086KKKT15/ref=lp_16225007011_1_6', 'price': 592.25},
    {'id': 2, 'name': 'CYBERPOWERPC Tracer IV Edge Pro', 'image': 'https://images-na.ssl-images-amazon.com/images/I/71vH6cfdWyL._AC_SL1500_.jpg', 'html': 'https://www.amazon.com/CYBERPOWERPC-Notebook-i7-10875H-Bluetooth-GTEP99821/dp/B08YD9P2K2/ref=sr_1_2_sspa?dchild=1&keywords=gaming+laptop&qid=1625114290&s=computers-intl-ship&sr=1-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyTUNUWFZYSDZYQ0VQJmVuY3J5cHRlZElkPUEwMTk2ODQ3M05FQ0xNTU9LV0xWVyZlbmNyeXB0ZWRBZElkPUEwODQ0ODg5MUNPQk1LVEVRUERMNCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=', 'price':1849.99},
    {'id': 3, 'name': 'MSI GL75 Leopard', 'image': 'https://images-na.ssl-images-amazon.com/images/I/81d1fpxXBcS._AC_SL1500_.jpg', 'html': 'https://www.amazon.com/MSI-GL75-Leopard-Gaming-Laptop/dp/B091265XFT/ref=sr_1_3?dchild=1&keywords=gaming+laptop&qid=1625114343&s=computers-intl-ship&sr=1-3', 'price': 1149.00},
    {'id': 4, 'name': 'Razer Blade 15', 'image': 'https://images-na.ssl-images-amazon.com/images/I/71wF7YDIQkL._AC_SL1500_.jpg', 'html': 'https://www.amazon.com/Razer-Blade-Base-Gaming-Laptop/dp/B08LZYN1ZF/ref=sr_1_4?dchild=1&keywords=gaming+laptop&qid=1625114588&s=computers-intl-ship&sr=1-4', 'price': 1299.99},
    {'id': 4, 'name': 'Acer Nitro 5', 'image': 'https://images-na.ssl-images-amazon.com/images/I/71s1LRpaprL._AC_SL1500_.jpg', 'html': 'https://www.amazon.com/Acer-i5-9300H-GeForce-Keyboard-AN515-54-5812/dp/B086KJBKDW/ref=sr_1_6?dchild=1&keywords=gaming+laptop&qid=1625114615&s=computers-intl-ship&sr=1-6', 'price': 813.00},
    {'id': 4, 'name': 'Acer Predator Helios 300', 'image': 'https://images-na.ssl-images-amazon.com/images/I/7183SjkrSnL._AC_SL1500_.jpg', 'html': 'https://www.amazon.com/Acer-Predator-i7-10750H-Keyboard-PH315-53-71HN/dp/B08VKV5WQ1/ref=sr_1_7?dchild=1&keywords=gaming+laptop&qid=1625114640&s=computers-intl-ship&sr=1-7', 'price': 1349.99},
    {'id': 4, 'name': 'Acer Predator Triton 500 PT515-52-73L3', 'image': 'https://images-na.ssl-images-amazon.com/images/I/71HWQq7dX2L._AC_SL1500_.jpg', 'html': 'https://www.amazon.com/Acer-Predator-PT515-52-73L3-i7-10750H-Dual-Channel/dp/B08CNLPDXV/ref=sr_1_8?dchild=1&keywords=gaming+laptop&qid=1625114663&s=computers-intl-ship&sr=1-8', 'price': 1449.00},
    {'id': 4, 'name': 'HP Pavilion Gaming', 'image': 'https://images-na.ssl-images-amazon.com/images/I/810gynDZHzL._AC_SL1500_.jpg', 'html': 'https://www.amazon.com/HP-Pavilion-Micro-EDGE-Processor-15-dk0020nr/dp/B07SC6HG74/ref=sr_1_10?dchild=1&keywords=gaming+laptop&qid=1625114692&s=computers-intl-ship&sr=1-10', 'price': 729.95},
    {'id': 4, 'name': 'LG Gram 14Z90P', 'image': 'https://images-na.ssl-images-amazon.com/images/I/91T5e50WCJS._AC_SL1500_.jpg', 'html': 'https://www.amazon.com/LG-Gram-14Z90P-Ultra-Lightweight-Built/dp/B08SW4D29M/ref=sr_1_11_sspa?dchild=1&keywords=gaming+laptop&qid=1625114717&s=computers-intl-ship&sr=1-11-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFOUEtGQTFYSEFWOU8mZW5jcnlwdGVkSWQ9QTA3MDU0ODAzNEFSOTNJR0VRNzg2JmVuY3J5cHRlZEFkSWQ9QTA2NzE3OTkxMFFWRTJETDA3U05IJndpZGdldE5hbWU9c3BfbXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==', 'price': 1046.99},
    {'id': 4, 'name': 'ASUS ROG Strix Scar 15', 'image': 'https://images-na.ssl-images-amazon.com/images/I/81aIviy7YZL._AC_SL1500_.jpg', 'html': 'https://www.amazon.com/ASUS-GeForce-i7-10875H-Windows-G532LWS-DS76/dp/B0876M6CG9/ref=sr_1_15?dchild=1&keywords=gaming+laptop&qid=1625114747&s=computers-intl-ship&sr=1-15', 'price': 2049.00}
]
    return render_template('home.html', items=items)

