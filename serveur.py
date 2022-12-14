from flask import Flask, render_template, request, redirect, url_for

articles=[]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ajout",methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        article = request.form['article']
        description = request.form['description']
        prix = request.form['prix']
        quantite = request.form['quantite']
        print(article,description,prix,quantite)
        articles.append({"nom":article,"description":description,"prix":prix,"quantite":quantite})
        return redirect(url_for('stock'))
    else:
        return render_template("ajout.html")

@app.route("/stock",methods = ['GET'])
def stock():
    return render_template("stock.html",listeArticles=articles)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)