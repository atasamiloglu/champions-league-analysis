def total_goals(df):
    home_goals = df["HOME_TEAM_SCORE"].sum()
    away_goals = df["AWAY_TEAM_SCORE"].sum()

    total_goals = home_goals + away_goals
    average_goals = total_goals / df.shape[0]

    return total_goals, average_goals


def top_scoring_teams(df):
    home_goals = df.groupby("HOME_TEAM")["HOME_TEAM_SCORE"].sum()
    away_goals = df.groupby("AWAY_TEAM")["AWAY_TEAM_SCORE"].sum()

    total_goals_by_team = home_goals.add(away_goals, fill_value=0)
    total_goals_by_team = total_goals_by_team.sort_values(ascending=False)

    return total_goals_by_team


def top_conceded_teams(df):
    home_conceded = df.groupby("HOME_TEAM")["AWAY_TEAM_SCORE"].sum()
    away_conceded = df.groupby("AWAY_TEAM")["HOME_TEAM_SCORE"].sum()

    total_conceded = home_conceded.add(away_conceded, fill_value=0)
    total_conceded = total_conceded.sort_values(ascending=False)

    return total_conceded


def home_advantage(df):
    home_wins = (df["HOME_TEAM_SCORE"] > df["AWAY_TEAM_SCORE"]).sum()
    draws = (df["HOME_TEAM_SCORE"] == df["AWAY_TEAM_SCORE"]).sum()
    away_wins = (df["HOME_TEAM_SCORE"] < df["AWAY_TEAM_SCORE"]).sum()

    return home_wins, draws, away_wins

def average_attendance(df):
    average_attendance = df["ATTENDANCE"].mean()

    return average_attendance

def top_attendance_matches(df):
    top_matches = df.sort_values(
        by="ATTENDANCE",
        ascending=False
    ).head(10)

    return top_matches[
        ["HOME_TEAM", "AWAY_TEAM", "STADIUM", "ATTENDANCE"]
    ]