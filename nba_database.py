# 🏀 NBA Database (User-Friendly Version)
#Jin Schmitt October 15 2025
# -------------------------------------------------------------------




import matplotlib.pyplot as plt
import pandas as pd
import os
import requests, os
from dotenv import load_dotenv
import seaborn as sns
import matplotlib.dates as mdates

load_dotenv()


folder_path = "Data/NBA_database_csv"



# Only load files that end with .csv and are not hidden
csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv") and not f.startswith(".")]

dataframes = {os.path.splitext(f)[0]: pd.read_csv(os.path.join(folder_path, f)) for f in csv_files}

#print(dataframes.keys())
#dict_keys(['play_by_play', 'game_info', 'player', 'team_history', 'team_info_common', 'inactive_players', 
# 'other_stats', 'officials', 'game_summary', 'draft_combine_stats', 'team_details', 'draft_history', 
# 'line_score', 'common_player_info', 'team', 'game'])
def preview_dataset(key: str):
    if key not in dataframes.keys():
        print("Please select a valid dictionary key from the list above")
    else:
        print(f"\n Here is the preview: \n")
        print(dataframes[key].head())
        print(f"\n📊 Shape: {dataframes[key].shape[0]} rows x {dataframes[key].shape[1]} columns")
    
    '''
def base_function_error_check():
    file_path = "Data/NBA_database_csv/PlayerStatistics.csv"

    df = pd.read_csv(file_path)

    # Create a combined full name column for matching
    df["full_name"] = (df["firstName"].astype(str) + " " + df["lastName"].astype(str)).str.lower()

    # Case-insensitive match
    name = name.lower().strip()
    player_data = df[df["full_name"] == name]


    if player_data.empty:
        print(f"No stats found for '{name.title()}'.")
        return None
    else:
        print(f"Found stats for {name.title()}:")
        #return player_data
        player_data = player_data.sort_values("gameDate")

'''
    
def get_player_career_stats(name: str):
    file_path = "Data/NBA_database_csv/PlayerStatistics.csv"

    df = pd.read_csv(file_path)

    # Create a combined full name column for matching
    df["full_name"] = (df["firstName"].astype(str) + " " + df["lastName"].astype(str)).str.lower()

    # Case-insensitive match
    name = name.lower().strip()
    player_data = df[df["full_name"] == name]

    if player_data.empty:
        print(f"No stats found for '{name.title()}'.")
        return None
    else:
        print(f"Found stats for {name.title()}:")
        #return player_data

    # Convert the stat columns to numeric
    stat_cols = ["points", "assists", "reboundsTotal", "steals", "blocks"]

    for col in stat_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')  # invalid strings -> NaN

# Fill NaNs with 0
    df[stat_cols] = df[stat_cols].fillna(0)
    
# Filter the DataFrame to only include rows where the player's full name matches the input name.
# This gives us a smaller DataFrame containing only the games played by that player.
    player_games = df[df["full_name"] == name]
    career_player_stats = {
        "Total Games Played": 0,
        "Total Points": 0,
        "Total Assists": 0,
        "Total Rebounds": 0,
        "Total Steals": 0,
        "Total Blocks": 0,

        }
    for _, row in player_games.iterrows():
        career_player_stats["Total Games Played"] += 1
        career_player_stats["Total Points"] += row["points"]
        career_player_stats["Total Assists"] += row["assists"]
        career_player_stats["Total Rebounds"] += row["reboundsTotal"]
        career_player_stats["Total Steals"] += row["steals"]
        career_player_stats["Total Blocks"] += row["blocks"]

    return career_player_stats



def get_player_season_stats(name: str):
    file_path = "Data/NBA_database_csv/PlayerStatistics.csv"

    df = pd.read_csv(file_path)

    # Create a combined full name column for matching
    df["full_name"] = (df["firstName"].astype(str) + " " + df["lastName"].astype(str)).str.lower()

    # Case-insensitive match
    name = name.lower().strip()
    player_data = df[df["full_name"] == name]

    if player_data.empty:
        print(f"No stats found for '{name.title()}'.")
        return None
    else:
        print(f"Found stats for {name.title()}:")
        #return player_data

    # Convert the stat columns to numeric
    stat_cols = ["points", "assists", "reboundsTotal", "steals", "blocks"]

    for col in stat_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')  # invalid strings -> NaN

    # Fill NaNs with 0
    df[stat_cols] = df[stat_cols].fillna(0)
    
    # Filter the DataFrame to only include rows where the player's full name matches the input name.
    # This gives us a smaller DataFrame containing only the games played by that player.
    player_games = df[df["full_name"] == name]
    career_player_stats = {
        "Total Games Played": 0,
        "Total Points": 0,
        "Total Assists": 0,
        "Total Rebounds": 0,
        "Total Steals": 0,
        "Total Blocks": 0,

        }
    for _, row in player_games.iterrows():
        career_player_stats["Total Games Played"] += 1
        career_player_stats["Total Points"] += row["points"]
        career_player_stats["Total Assists"] += row["assists"]
        career_player_stats["Total Rebounds"] += row["reboundsTotal"]
        career_player_stats["Total Steals"] += row["steals"]
        career_player_stats["Total Blocks"] += row["blocks"]
    
    points_per_game = career_player_stats["Total Points"] / career_player_stats["Total Games Played"]
    rounded_points_per_game = round(points_per_game, 1)

    assists_per_game = career_player_stats["Total Assists"] / career_player_stats["Total Games Played"]
    rounded_assists_per_game = round(assists_per_game, 1)

    rebounds_per_game = career_player_stats["Total Rebounds"] / career_player_stats["Total Games Played"]
    rounded_rebounds_per_game = round(rebounds_per_game, 1)

    steals_per_game = career_player_stats["Total Steals"] / career_player_stats["Total Games Played"]
    rounded_steals_per_game = round(steals_per_game, 1)

    blocks_per_game = career_player_stats["Total Blocks"] / career_player_stats["Total Games Played"]
    rounded_blocks_per_game = round(blocks_per_game, 1)


    season_player_stats = {
        "Points Per Game": rounded_points_per_game,
        "Assists Per Game": rounded_assists_per_game,
        "Rebounds Per Game": rounded_rebounds_per_game,
        "Steals Per Game": rounded_steals_per_game,
        "Blocks Per Game": rounded_blocks_per_game,

    }

    return season_player_stats



def player_comparison(name1: str, name2: str):
    # Get stats
    player1_season = get_player_season_stats(name1)
    player1_career = get_player_career_stats(name1)
    
    player2_season = get_player_season_stats(name2)
    player2_career = get_player_career_stats(name2)
    
    if not all([player1_season, player1_career, player2_season, player2_career]):
        return None

    # Build formatted comparison dicts
    season_comparison = []
    for stat in player1_season:
        season_comparison.append({
            "stat": stat,
            name1: player1_season[stat],
            name2: player2_season[stat]
        })
    
    career_comparison = []
    for stat in player1_career:
        career_comparison.append({
            "stat": stat,
            name1: player1_career[stat],
            name2: player2_career[stat]
        })

    return {
        "season": season_comparison,
        "career": career_comparison
    }



def efficiency(name: str, silent: bool = False):
    file_path = "Data/NBA_database_csv/PlayerStatistics.csv"

    df = pd.read_csv(file_path)

    # Create a combined full name column for matching
    df["full_name"] = (df["firstName"].astype(str) + " " + df["lastName"].astype(str)).str.lower()

    # Case-insensitive match
    name = name.lower().strip()
    player_data = df[df["full_name"] == name]

    if player_data.empty:
        print(f"No stats found for '{name.title()}'.")
        return None
    else:
        print(f"Found stats for {name.title()}:")
        #return player_data

    # Convert the stat columns to numeric
    stat_cols = ["points", "assists", "reboundsTotal", "steals", "blocks"]

    for col in stat_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')  # invalid strings -> NaN

    # Fill NaNs with 0
    df[stat_cols] = df[stat_cols].fillna(0)


    player_games = df[df["full_name"] == name]

    

    player_efficiency = {
        "Field Goal %": 0.0,
        "Three Point %": 0.0,
        "Two Point %": 0.0,
        "Free Throw %": 0.0,

    }

    two_point_fg = (
        (player_games["fieldGoalsMade"] - player_games["threePointersMade"]).sum()
        / (player_games["fieldGoalsAttempted"] - player_games["threePointersAttempted"]).sum()
    )
    #for _, row in player_games.iterrows():
    player_efficiency["Field Goal %"] = player_games["fieldGoalsPercentage"].mean()
    player_efficiency["Three Point %"] = player_games["threePointersPercentage"].mean()
    player_efficiency["Two Point %"] = two_point_fg
    player_efficiency["Free Throw %"] = player_games["freeThrowsPercentage"].mean()


    player_efficiency = {k: round(v * 100, 1) for k, v in player_efficiency.items()}

    '''print(f"\n\n==== {name.title()} Career Efficiency ====\n")
    for stat, value in player_efficiency.items():
        print(f"{stat}: {value:.1f}")'''

    return player_efficiency


def compare_efficiency(name1: str, name2: str):
    player1_efficiency = efficiency(name1, silent=True)
    player2_efficiency = efficiency(name2, silent=True)
    print(f"\n=== Efficiency Comparison ===")
    print(f"{'Stat':<20}{name1:<15}{name2:<15}")
    for stat in player1_efficiency:
        print(f"{stat:<20}{player1_efficiency[stat]:<15}{player2_efficiency[stat]:<15}")
    

def get_player_year_by_year_ppg(name: str):
    file_path = "Data/NBA_database_csv/PlayerStatistics.csv"

    df = pd.read_csv(file_path)

    # Create a combined full name column for matching
    df["full_name"] = (df["firstName"].astype(str) + " " + df["lastName"].astype(str)).str.lower()

    # Case-insensitive match
    name = name.lower().strip()
    player_data = df[df["full_name"] == name]


    if player_data.empty:
        print(f"No stats found for '{name.title()}'.")
        return None
    else:
        print(f"Found stats for {name.title()}:")
        #return player_data
        player_data = player_data.sort_values("gameDate")

    ###Actual Logic Begins
    season_stats = get_player_season_stats(name)
    ppg = season_stats["Points Per Game"]

            
            


def plot_player_ppg(name: str):
    file_path = "Data/NBA_database_csv/PlayerStatistics.csv"

    df = pd.read_csv(file_path)

    # Create a combined full name column for matching
    df["full_name"] = (df["firstName"].astype(str) + " " + df["lastName"].astype(str)).str.lower()

    # Case-insensitive match
    name = name.lower().strip()
    player_data = df[df["full_name"] == name]


    if player_data.empty:
        print(f"No stats found for '{name.title()}'.")
        return None
    else:
        print(f"Found stats for {name.title()}:")
        #return player_data
        player_data = player_data.sort_values("gameDate")

    # Ensure 'gameDate' is datetime
    player_data["gameDate"] = pd.to_datetime(player_data["gameDate"], errors="coerce")
    player_data = player_data.sort_values("gameDate")

    # Plot regression line
    sns.lineplot(x="numMinutes", y="points", data=player_data, )
    # Add labels and title
    plt.title(f"Points vs Minutes Played — {name.title()}")
    plt.xlabel("Minutes Played")
    plt.ylabel("Points Scored")

    plt.xlim(0,60)
    plt.ylim(0,player_data["points"].max() + 5)

    # Show the plot
    plt.show()
    


def main_menu():
    while True:
        print("\n=== NBA Database Menu ===")
        print("*DISCLAIMER* Stats are as of the 2023-24 NBA Season")
        print("1. Get player stats")
        print("2. Compare Players")
        print("3. Player Efficiency")
        print("4. Compare Player Efficiency")
        print("5. Plot Player")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            player_name = input("Enter full player name: ")
            career_or_season = input("Enter career or season stats(career is totals and season is career averages): ").lower().strip()

            while career_or_season not in ["career", "season"]:
                career_or_season = input("Please enter valid input (career or season): ").lower().strip()

            if career_or_season == "career":
                career_stats = get_player_career_stats(player_name)
                if career_stats:
                    print(f"\nCareer totals for {player_name}:")
                    for k, v in career_stats.items():
                        print(f"{k}: {v}")

            elif career_or_season == "season":
                season_stats = get_player_season_stats(player_name)
                if season_stats:
                    print(f"\nSeason stats for {player_name}:")
                    for k, v in season_stats.items():
                        print(f"\n{k}: {v}")

        elif choice == "2":
            player_list = [x.strip() for x in input("Enter players you want to compare(ex. Lebron James, Kevin Durant): ").split(",")]
            player_comparison(player_list[0], player_list[1])

            compare_efficiency(player_list[0], player_list[1])

        elif choice == "3":
            player_name = input("Enter player's name for career efficiency: ")
            player_efficiency = efficiency(player_name)
            for k, v in player_efficiency.items():
                print(f"{k}: {v:.1f}")
        

    ##FIXME--FIX 
        elif choice == "4":
            player_list = [x for x in input("Enter players you want to compare(ex. Lebron James, Kevin Durant): ").split(",")]
            compare_efficiency(player_list[0], player_list[1])

        elif choice == "5":
            player_name = input("Enter player's name for plot: ")
            get_player_year_by_year_ppg(player_name)
            plot_player_ppg(player_name)

        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")
if __name__ == "__main__":
    main_menu()