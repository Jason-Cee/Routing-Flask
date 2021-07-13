from flask import Flask, redirect, url_for  # ALL IMPORTANT IMPORTS
app = Flask(__name__)


# CREATING DEFAULT PAGE
@app.route("/")
def user():
    return "This is the user page"


# CREATING VERIFY PAGE
@app.route("/verify/<name>")
def verify_page(name):
    if name == "Jason":
        return redirect(url_for("student", name=name))
    elif name == "Godwin":
        return redirect(url_for("admin", name=name))
    else:
        return redirect(url_for("guest", name=name))


# CREATING STUDENT PAGE
@app.route("/student/<name>")
def student(name):
    return "I am a student at Lifechoices Academy, my name is %s" % name


# CREATING ADMIN PAGE
@app.route("/admin/<name>")
def admin(name):
    return "I am admin at Lifechoices Academy, my name is: %s" % name


# CREATING GUEST PAGE
@app.route("/guest/<name>")
def guest(name):
    return "I am a guest at Lifechoices Academy, my name is : %s" % name


@app.route("/payment/<int:sal>")
def payment(sal):
    if sal <= 5000:
        return redirect("https://www.fnb.co.za")
    else:
        return redirect("https://sahomeloans.com")


# RUNNING MY APP
if __name__ == '__main__':
    app.debug = True
    app.run()
