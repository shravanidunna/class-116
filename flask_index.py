from flask import Flask, render_template
app = Flask(__name__,template_folder='template')
#in the function return render_template(‘index.html’)
@app.route("/index")
def first_webpage():

    # Pass the variable in the template
    return render_template('index.html')
app.run(debug=True)



