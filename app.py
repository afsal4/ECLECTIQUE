from cs50 import SQL
from flask import Flask, render_template, request, session, redirect


db = SQL("sqlite:////workspaces/ECLECTIQUE/and.db")

app = Flask(__name__)

# -----------------administrator---------------------


@app.route("/")
def home():
    return render_template("admin/index.html")


@app.route("/login")
def login():
    return render_template("admin/login.html")

@app.route("/post", methods=["POST"])
def login_post():
    username = request.form['login']
    password = request.form['pass']
    # db.execute("INSERT INTO login(username, password) VALUES(?, ?)", username, password)

    res = db.execute("SELECT * FROM login WHERE username = ? AND password = ?", username, password)

    try:
        if res != None:
            if res[0]["username"] == "debugging":
                # session["name"] == "deb"
                return redirect("/deb_view")

            elif res[0]["username"] == "coding":
                return redirect("/cod_view")

            elif res[0]["username"] == "treasure":
                return redirect("/treasure_view")

            elif res[0]["username"] == "it":
                return redirect("/it_view")

            elif res[0]["username"] == "digital":
                return redirect("/digital_view")

            elif res[0]["username"] == "puzzle":
                return redirect("/puzzle_view")

            elif res[0]["username"] == "all":
                return redirect("/all")

            elif res[0]["username"] == "ui":
                return redirect("/ui_view")

            elif res[0]["username"] == "games":
                return redirect("/games_view")

            elif res[0]["username"] == "typing":
                return redirect("/typing_view")

            elif res[0]["username"] == "vr":
                return redirect("/vr_view")

            elif res[0]["username"] == "vfx":
                return redirect("/vfx_view")

            else:
                return redirect("/login")
    except IndexError:
        return render_template("admin/login.html")







@app.route("/deb_view")
def deb_view():
    res = db.execute("SELECT * FROM user WHERE event = ? ORDER BY status DESC", "debugging")
    return render_template("admin/deb.html", data=res)

@app.route("/deb_view_post", methods=["post"])
def deb_view_post():
    name = request.form["name"]
    name = "%" + name + "%"
    res = db.execute("SELECT * FROM user WHERE name LIKE ? ORDER BY status DESC", name)
    return render_template("admin/deb.html", data=res)

@app.route("/cod_view_post", methods=["post"])
def cod_view_post():
    name = request.form["name"]
    name = "%" + name + "%"
    res = db.execute("SELECT * FROM user WHERE name LIKE ? ORDER BY status DESC", name)
    return render_template("admin/cod.html", data=res)

@app.route("/cod_view")
def cod_view():
    res = db.execute("SELECT * FROM user WHERE event = ? ORDER BY status DESC", "coding")
    return render_template("admin/cod.html", data=res)

@app.route("/it_view")
def it_view():
    res = db.execute("SELECT * FROM user WHERE event = ? ORDER BY status DESC", "it")
    return render_template("admin/it.html", data=res)

@app.route("/it_view_post", methods=["post"])
def it_view_post():
    name = request.form["name"]
    name = "%" + name + "%"
    res = db.execute("SELECT * FROM user WHERE name LIKE ? ORDER BY status DESC", name)
    return render_template("admin/it.html", data=res)

@app.route("/digital_view")
def digital_view():
    res = db.execute("SELECT * FROM user WHERE event = ? ORDER BY status DESC", "digital")
    return render_template("admin/digital.html", data=res)

@app.route("/digital_view_post", methods=["post"])
def digital_view_post():
    name = request.form["name"]
    name = "%" + name + "%"
    res = db.execute("SELECT * FROM user WHERE name LIKE ? ORDER BY status DESC", name)
    return render_template("admin/digital.html", data=res)

@app.route("/treasure_view")
def treasure_view():
    res = db.execute("SELECT * FROM user WHERE event = ? ORDER BY status DESC", "treasure")
    return render_template("admin/treasure.html", data=res)

@app.route("/trasure_view_post", methods=["post"])
def treasure_view_post():
    name = request.form["name"]
    name = "%" + name + "%"
    res = db.execute("SELECT * FROM user WHERE name LIKE ? ORDER BY status DESC", name)
    return render_template("admin/treasure.html", data=res)

@app.route("/puzzle_view")
def puzzle_view():
    res = db.execute("SELECT * FROM user WHERE event = ? ORDER BY status DESC", "puzzle")
    return render_template("admin/puzzle.html", data=res)

@app.route("/puzzle_view_post", methods=["post"])
def puzzle_view_post():
    name = request.form["name"]
    name = "%" + name + "%"
    res = db.execute("SELECT * FROM user WHERE name LIKE ? ORDER BY status DESC", name)
    return render_template("admin/puzzle.html", data=res)

@app.route("/all")
def all():
    res = db.execute("SELECT * FROM user ORDER BY status DESC")
    return render_template("admin/all.html", data=res)

@app.route("/all_post", methods=["post"])
def all_post():
    name = request.form["name"]
    name = "%" + name + "%"
    res = db.execute("SELECT * FROM user WHERE name LIKE ? ORDER BY status DESC", name)
    return render_template("admin/all.html", data=res)

@app.route("/ui_view")
def ui_view():
    res = db.execute("SELECT * FROM user WHERE event = ? ORDER BY status DESC", "ui")
    return render_template("admin/ui.html", data=res)

@app.route("/ui_view_post", methods=["post"])
def ui_view_post():
    name = request.form["name"]
    name = "%" + name + "%"
    res = db.execute("SELECT * FROM user WHERE name LIKE ? ORDER BY status DESC", name)
    return render_template("admin/ui.html", data=res)

@app.route("/games_view")
def games_view():
    res = db.execute("SELECT * FROM user WHERE event = ? ORDER BY status DESC", "games")
    return render_template("admin/games.html", data=res)

@app.route("/games_view_post", methods=["post"])
def games_view_post():
    name = request.form["name"]
    name = "%" + name + "%"
    res = db.execute("SELECT * FROM user WHERE name LIKE ? ORDER BY status DESC", name)
    return render_template("admin/games.html", data=res)

@app.route("/typing_view")
def typing_view():
    res = db.execute("SELECT * FROM user WHERE event = ? ORDER BY status DESC", "typing")
    return render_template("admin/typing.html", data=res)

@app.route("/typing_view_post", methods=["post"])
def typing_view_post():
    name = request.form["name"]
    name = "%" + name + "%"
    res = db.execute("SELECT * FROM user WHERE name LIKE ? ORDER BY status DESC", name)
    return render_template("admin/typing.html", data=res)

@app.route("/vfx_view")
def vfx_view():
    res = db.execute("SELECT * FROM user WHERE event = ? ORDER BY status DESC", "vfx")
    return render_template("admin/vfx.html", data=res)

@app.route("/vfx_view_post", methods=["post"])
def vfx_view_post():
    name = request.form["name"]
    name = "%" + name + "%"
    res = db.execute("SELECT * FROM user WHERE name LIKE ? ORDER BY status DESC", name)
    return render_template("admin/vfx.html", data=res)

@app.route("/vr_view")
def vr_view():
    res = db.execute("SELECT * FROM user WHERE event = ? ORDER BY status DESC", "vr")
    return render_template("admin/vr.html", data=res)

@app.route("/vr_view_post", methods=["post"])
def vr_view_post():
    name = request.form["name"]
    name = "%" + name + "%"
    res = db.execute("SELECT * FROM user WHERE name LIKE ? ORDER BY status DESC", name)
    return render_template("admin/vr.html", data=res)












@app.route("/c_participate/<id>")
def c_participate(id):
    res = db.execute("UPDATE user SET status = 'checked' WHERE user_id = ?", id)
    return redirect("/cod_view")

@app.route("/d_participate/<id>")
def d_participate(id):
    res = db.execute("UPDATE user SET status = 'checked' WHERE user_id = ?", id)
    return redirect("/deb_view")

@app.route("/t_participate/<id>")
def t_participate(id):
    res = db.execute("UPDATE user SET status = 'checked' WHERE user_id = ?", id)
    return redirect("/treasure_view")

@app.route("/i_participate/<id>")
def i_participate(id):
    res = db.execute("UPDATE user SET status = 'checked' WHERE user_id = ?", id)
    return redirect("/it_view")

@app.route("/p_participate/<id>")
def p_participate(id):
    res = db.execute("UPDATE user SET status = 'checked' WHERE user_id = ?", id)
    return redirect("/puzzle_view")

@app.route("/di_participate/<id>")
def di_participate(id):
    res = db.execute("UPDATE user SET status = 'checked' WHERE user_id = ?", id)
    return redirect("/digital_view")

@app.route("/u_participate/<id>")
def u_participate(id):
    res = db.execute("UPDATE user SET status = 'checked' WHERE user_id = ?", id)
    return redirect("/ui_view")

@app.route("/g_participate/<id>")
def g_participate(id):
    res = db.execute("UPDATE user SET status = 'checked' WHERE user_id = ?", id)
    return redirect("/games_view")

@app.route("/ty_participate/<id>")
def ty_participate(id):
    res = db.execute("UPDATE user SET status = 'checked' WHERE user_id = ?", id)
    return redirect("/typing_view")


@app.route("/v_participate/<id>")
def v_participate(id):
    db.execute("UPDATE user SET status = 'checked' WHERE user_id = ?", id)
    return redirect("/vfx_view")

@app.route("/vr_participate/<id>")
def vr_participate(id):
    db.execute("UPDATE user SET status = 'checked' WHERE user_id = ?", id)
    return redirect("/vr_view")

@app.route("/a_participate/<id>")
def a_participate(id):
    res = db.execute("UPDATE user SET status = 'checked' WHERE user_id = ?", id)
    return redirect("/all")



# -----------------------user----------------

@app.route("/register")
def register():
    return render_template("admin/registration.html")

@app.route("/register_post", methods=["POST"])
def register_post():
    name = request.form['name']
    class1 = request.form['class']
    event = request.form['event']
    status = "pending"
    a = {"IT Quiz": "it", "Coding": "coding", "Debugging": "debugging", "Digital Painting": "digital", "Puzzles": "puzzle", "Treasure Hunt": "treasure", "UI Designing": "ui", "Other Games": "games", "Typing Competition": "typing", "VFX": "vfx", "VR": "vr"}
    db.execute("insert into user(name,class,event,status) values (?, ?, ?, ?)", name, class1, a[event], status)
    token1 = db.execute("SELECT * FROM user WHERE name = ? AND event = ? AND class = ?", name , a[event], class1)
    tkn = token1[0]
    return token(tkn)


@app.route("/token", methods=["POST"])
def token(tkn):
    a = {"it": "IT Quiz", "coding": "Coding", "debugging": "Debugging", "digital": "Digital Painting", "puzzle": "Puzzles", "treasure": "Treasure Hunt", "ui": "UI Designing", "games": "Other Games", "typing": "Typing Competition", "vfx": "VFX", "vr": "VR"}
    return render_template("admin/token.html", data=tkn, event=a[tkn["event"]])


if __name__ == '__main__':
    app.run()