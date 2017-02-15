from flask import Flask, render_template, request,jsonify
import sqlite3
app = Flask(__name__)

DB = 'database.db'

@app.route("/")
def index():
    return render_template('home.html')


@app.route("/enternew/")
def food():
    return render_template('food.html')

@app.route("/addfood/",methods = ['POST'])
def add_food():
    try:
        food = (request.form['name'].lower(),
                request.form['calories'],
                request.form['cuisine'].lower(),
                request.form['is_vegetarian'].lower(),
                request.form['is_gluten_free'].lower(), )
        conn = sqlite3.connect(DB)
        cur = conn.cursor()
        cur.execute('INSERT INTO foods VALUE (?,?,?,?,?)',food)
        conn.commit()
        conn.close()
    except:
        pass
    finally:
        message = 'Added record: {0}'.format(food)
        return render_template('result.html',message = message)




if __name__ == "__main__":
    app.run()
