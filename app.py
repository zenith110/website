from flask import Flask, render_template, request, redirect
import requests
app = Flask(__name__, static_url_path='/static')
@app.route("/")
def index():
    if(requests.post == "GET"):
        print("test")
    return render_template("index.html", pstyleColor = "#F3EFE0", style = "display:none")

@app.route("/commands/", methods = ["POST"])
def command_route():
    input = request.form["command-text"]
    
    if(input == "commands"):
        return render_template("index.html", pstyleColor = "#F3EFE0", style = "display:none", result = "The following commands are available: Gofetch, Pokemon, and clear.")

    elif(input == "clear"):
        return render_template("index.html", pstyleColor = "#F3EFE0", style = "display:none", result = "")

    elif(input == "Gofetch"):
        return render_template("index.html", 
        style = "flex", pstyleColor = "#F3EFE0",
        projectName = "Gofetch", 
        goal = "Goal: To create a platform that allows users to recieve Instagram pictures of pets through various mediums.", 
        languages = "Languages used: Python, and Golang",
        frameworks = "Frameworks and libraries used: DiscordGo, Flask, Selenium, BeautifulSoup4, Click, and Requests.",
        cloud = "Cloud and database used: Microsoft's Azure, and PostgreSQL",
        githubLink = "https://github.com/zenith110/Gofetch",
        buttonstyle = "display:none;",
        demoText = "Demo",
        githubText = "Github Repo",
        githubalign = "center")
    elif(input == "Pokemon"):
        return render_template("index.html", 
        style = "flex", pstyleColor = "#F3EFE0",
        projectName = "Pokemon Battle sim", 
        goal = "Goal: Create a Peer to Peer battle simulator based off the popular Pokemon franchise", 
        languages = "Languages used: Python",
        frameworks = "Frameworks and libraries used: Pygame, PySide2",
        cloud = "",
        cloudbutton = "display:none;",
        githubLink = "https://github.com/zenith110/pokemon_battle_sim",
        buttonstyle = "display:none;color: black",
        demoText = "Demo",
        githubText = "Github Repo",
        githubalign = "center")
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)