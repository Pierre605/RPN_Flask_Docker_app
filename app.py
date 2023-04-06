from flask import Flask, render_template, request, g, make_response, redirect, flash, url_for
import sqlite3, os, datetime, csv
from markupsafe import Markup
from pni_calc import pni_calculator
from io import StringIO


app = Flask(__name__)

DATABASE = 'app.db'

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
		return db


@app.route("/", methods=['POST', 'GET', 'DELETE'])
def index():
	if request.method == 'GET':
		return render_template('index.html')

	if request.method == 'POST':
		db = get_db()

		operation_form = request.form
		content_type = request.content_type
		query = operation_form["query"]
		result = None

		out = pni_calculator(query=query)
		res = None
		try:
			res = float(out)
		except Exception:
			pass

		if res or out == 'null':
			result = out

		cur_preced = db.execute("SELECT * FROM operations ORDER BY id DESC LIMIT 10")
		precedents = cur_preced.fetchall()

		if result:
			date = datetime.datetime.now(tz=None)
			date = date.strftime('%Y-%m-%d %H:%M:%S')
			db.execute("INSERT INTO operations (query, result, sent) VALUES (?, ?, ?)", [query, result, date])
			db.commit()

			if "multipart/form-data" in content_type:
				return render_template('index.html', res= Markup("<strong>" + query + "&ensp;=&ensp;" + str(result) + "</strong>"), precedents= precedents)
			else:
				return (query + " = " + str(result))
		else:
			if "multipart/form-data" in content_type:
				return render_template('index.html', info=Markup(out), precedents= precedents)
			else:
				return Markup(out).striptags()


@app.route("/export/", methods=['POST'])
def export():
	if request.method == 'POST':
		click_export = request.form
		content_type = request.content_type

		if click_export["export"] == "executeExportCSV":
			print(click_export["export"])
			db = get_db()
			si = StringIO()
			cw = csv.writer(si)

			cur_all_operations = db.execute('SELECT * FROM operations ORDER BY id')
			rows = cur_all_operations.fetchall()
			if rows:
				cw.writerow([i[0] for i in cur_all_operations.description])
				cw.writerows(rows)
				response = make_response(si.getvalue())
				response.headers['Content-Disposition'] = 'attachment; filename=PNI_calaculations_report.csv'
				response.headers["Content-type"] = "text/csv"
				return response
			else:
				if "multipart/form-data" in content_type:
					return redirect('/')
				else:
					response = "None"
					print(response)
					return response


@app.route("/delete/", methods=['POST'])
def clear_history():
	if request.method == 'POST':
		clear_order = request.form
		content_type = request.content_type

		if clear_order["clear"] == "deleteDB":
			print(clear_order["clear"])
			db = get_db()
			db.execute("DELETE FROM operations")
			db.commit()

			if "multipart/form-data" in content_type:
				return redirect('/')
			else:
				response = 'DELETED'
				return response



if __name__ == "__main__":
	app.run()
