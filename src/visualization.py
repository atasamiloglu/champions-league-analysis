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