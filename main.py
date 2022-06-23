from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('Home.html')


@app.route("/hire")
def hire():
    return render_template('Hire Me.html')


@app.route("/about")
def about():
    return render_template('About Me.html')


@app.route("/work")
def work():
    return render_template('Work.html')


@app.route("/parallax pages")
def parallax():
    return render_template('Parallax Pages.html')


@app.route("/creativity pages")
def creativity():
    return render_template('Creativity Pages.html')


@app.route("/javascript pages")
def javascript():
    return render_template('Javascript Pages.html')


@app.route("/FontAwesome Background Image Effect")
def creativity1():
    return render_template('Creativity Page 1.html')


@app.route("/services")
def services():
    return render_template('Services.html')


@app.route("/social")
def social():
    return render_template('Social.html')


@app.route("/testimonial")
def testimonial():
    return render_template('Testimonial.html')


@app.route("/resume")
def resume():
    return render_template('Resume.html')


@app.route("/contact")
def contact():
    return render_template('Contact.html')


if __name__ == "__main__":
    app.run(debug=True)