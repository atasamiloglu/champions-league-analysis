import matplotlib.pyplot as plt


def plot_top_teams(top_teams):
    plt.figure(figsize=(10, 6))

    plt.bar(top_teams.index, top_teams.values)

    plt.title("Top 10 Teams by Total Goals")
    plt.xlabel("Teams")
    plt.ylabel("Goals")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("images/top_10_teams_by_goals.png", dpi=300)

    plt.show()


def plot_home_advantage(home_wins, draws, away_wins):
    labels = ["Home Wins", "Draws", "Away Wins"]
    sizes = [home_wins, draws, away_wins]

    plt.figure(figsize=(7, 7))

    plt.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Match Outcomes in UEFA Champions League (2016-2022)")

    plt.savefig("images/home_advantage_pie.png", dpi=300)

    plt.show()


def plot_top_attendance_matches(top_matches):
    
    match_names = (
        top_matches["HOME_TEAM"] + " vs " + top_matches["AWAY_TEAM"]
    )

    plt.figure(figsize=(12, 6))

    plt.bar(match_names, top_matches["ATTENDANCE"])

    plt.title("Top 10 Matches by Attendance")
    plt.xlabel("Matches")
    plt.ylabel("Attendance")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()

    plt.savefig("images/top_10_attendance_matches.png", dpi=300)

    plt.show()

def plot_average_goals_by_season(average_goals):
    plt.figure(figsize=(8, 5))

    plt.plot(
        average_goals.index,
        average_goals.values,
        marker="o",
        linewidth=2
    )

    plt.title("Average Goals per Match by Season")
    plt.xlabel("Season")
    plt.ylabel("Average Goals")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig("images/average_goals_by_season.png", dpi=300)

    plt.show()    



    
    