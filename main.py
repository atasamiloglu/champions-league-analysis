from src.load_data import load_matches
from src.analysis import (
    total_goals,
    top_scoring_teams,
    top_conceded_teams,
    home_advantage,
    average_attendance,
    top_attendance_matches,
    
)
from src.visualization import (
    plot_top_teams,
    plot_home_advantage,
    plot_top_attendance_matches,
)


def main():
    # Load data
    df = load_matches()

    # Total goals analysis
    total, average = total_goals(df)
    print(f"Total goals: {total}")
    print(f"Average goals per match: {average:.2f}")

    # Top scoring teams
    top_teams = top_scoring_teams(df)
    print("\nTop 10 Teams by Goals")
    print(top_teams.head(10))

    # Plot top scoring teams
    plot_top_teams(top_teams.head(10))

    # Teams that conceded the most goals
    conceded = top_conceded_teams(df)
    print("\nTop 10 Teams by Goals Conceded")
    print(conceded.head(10))

    # Home advantage analysis
    home_wins, draws, away_wins = home_advantage(df)

    print("\nMatch Outcomes")
    print(f"Home Wins: {home_wins}")
    print(f"Draws: {draws}")
    print(f"Away Wins: {away_wins}")

    # Plot home advantage
    plot_home_advantage(home_wins, draws, away_wins)

    attendance = average_attendance(df)

    print(f"\nAverage Attendance: {attendance:.2f}")

    top_matches = top_attendance_matches(df)
    print("\nTop 10 Matches by Attendance")
    print(top_matches)

    plot_top_attendance_matches(top_matches)

    


if __name__ == "__main__":
    main()