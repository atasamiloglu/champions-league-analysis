from src.load_data import load_matches,load_players
from src.analysis import (
    total_goals,
    top_scoring_teams,
    top_conceded_teams,
    home_advantage,
    average_attendance,
    top_attendance_matches,
    goals_by_season,
    matches_by_season,
    average_goals_by_season,
    average_attendance_by_season,
    average_height,
    tallest_players,
    average_height_by_position,
    average_age,
    average_age_by_position,
    

    
)
from src.visualization import (
    plot_top_teams,
    plot_home_advantage,
    plot_top_attendance_matches,
    plot_average_goals_by_season,
    plot_average_attendance_by_season,
    plot_average_height_by_position,
    plot_average_age_by_position,
    
)


def main():
    # Load data
    df = load_matches()

    # Total goals analysis
    total, average = total_goals(df)
    #print(f"Total goals: {total}")
    #print(f"Average goals per match: {average:.2f}")

    # Top scoring teams
    top_teams = top_scoring_teams(df)
    #print("\nTop 10 Teams by Goals")
    #print(top_teams.head(10))

    # Plot top scoring teams
    plot_top_teams(top_teams.head(10))

    # Teams that conceded the most goals
    conceded = top_conceded_teams(df)
    #print("\nTop 10 Teams by Goals Conceded")
    #print(conceded.head(10))

    # Home advantage analysis
    home_wins, draws, away_wins = home_advantage(df)

    #print("\nMatch Outcomes")
    #print(f"Home Wins: {home_wins}")
    #print(f"Draws: {draws}")
    #print(f"Away Wins: {away_wins}")

    # Plot home advantage
    plot_home_advantage(home_wins, draws, away_wins)

    attendance = average_attendance(df)

    #print(f"\nAverage Attendance: {attendance:.2f}")

    top_matches = top_attendance_matches(df)
    #print("\nTop 10 Matches by Attendance")
    #print(top_matches)

    plot_top_attendance_matches(top_matches)

    season_goals = goals_by_season(df)

    #print("\nGoals by Season")
    #print(season_goals)

    season_matches = matches_by_season(df)

    #print("\nMatches by Season")
    #print(season_matches)

    average_goals = average_goals_by_season(df)

    #print("\nAverage Goals per Match by Season")
    #print(average_goals.round(2))

    plot_average_goals_by_season(average_goals)

    average_attendance_season = average_attendance_by_season(df)

    #print("\nAverage Attendance by Season")
    #print(average_attendance_season.round(1))

    plot_average_attendance_by_season(average_attendance_season)

    players_df = load_players()

    average_player_height = average_height(players_df)

    #print(f"\nAverage Player Height: {average_player_height:.2f} cm")

    tallest = tallest_players(players_df)

    #print("\nTop 10 Tallest Players")
    #print(tallest)

    height_by_position = average_height_by_position(players_df)

    #print("\nAverage Height by Position")
    #print(height_by_position.round(2))

    height_by_position = average_height_by_position(players_df)

    #print("\nAverage Height by Position")
    #print(height_by_position)

    plot_average_height_by_position(height_by_position)

    average_player_age = average_age(players_df)

    #print(f"\nAverage Player Age: {average_player_age:.2f} years")

    print(players_df["DOB"].head())

    age_by_position = average_age_by_position(players_df)

    print("\nAverage Age by Position")
    print(age_by_position)

    plot_average_age_by_position(age_by_position)
    


if __name__ == "__main__":
    main()