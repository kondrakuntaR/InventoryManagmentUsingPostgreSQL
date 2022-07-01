import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method=='POST':
        if request.form['manage_inv_btn'] == "Manage Inventory":
            return render_template('manage.html')
        else:
            inv_name=request.form['inv_name']
            print(inv_name)

            # #establish connection to postgresql server
            conn = psycopg2.connect("dbname=kitchen user=postgres password=Ramya2209 port=5401")

            print("Successfully connected to database!")

            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS {table_name}(
                ITEM_ID INT NOT NULL PRIMARY KEY,
                ITEM CHAR(50) NOT NULL,
                ITEM_TYPE CHAR(10),
                CATEGORY CHAR(50),
                ITEM_COUNT INT NOT NULL
            );'''.format(table_name=inv_name))

            print("Table created!")

            conn.commit()
            conn.close()

            return render_template('update.html')


if __name__ == '__main__':
    app.debug = True
    app.run()