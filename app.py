from flask import Flask, render_template, request
from nba_database import get_player_career_stats, get_player_season_stats, efficiency, player_comparison, plot_player_ppg

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/career", methods=["POST"])
def career():
    player_name = request.form["player_name"]
    stats = get_player_career_stats(player_name)
    return render_template("player.html", stats=stats, mode="Career", player=player_name)

@app.route("/season", methods=["POST"])
def season():
    player_name = request.form["player_name"]
    stats = get_player_season_stats(player_name)
    return render_template("player.html", stats=stats, mode="Season", player=player_name)

@app.route("/efficiency", methods=["POST"])
def player_efficiency():
    player_name = request.form["player_name"]
    stats = efficiency(player_name, silent=True)  # silent=True prevents print spam
    return render_template("player.html", stats=stats, mode="Efficiency", player=player_name)

@app.route("/compare_players", methods=["POST"])
def compare_player():
    player1 = request.form["player1"]
    player2 = request.form["player2"]    
    stats = player_comparison(player1, player2)
    #return render_template("player.html", stats=stats, player1=player1, player2=player2)


    return render_template("player_comparison.html", stats=stats, player1=player1, player2=player2)
if __name__ == "__main__":
    app.run(debug=True, port=5001)