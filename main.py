import pandas as pd

df = pd.read_excel(
    "data/ChampionsLeague/ucl_data.xlsx",
    sheet_name="matches"
)

#print(df.head())
#print(df.shape)
#print(df.columns)
#print(df.info())

home_goals = df["HOME_TEAM_SCORE"].sum()        # ev sahibi takımın gollerini toplar
away_goals = df["AWAY_TEAM_SCORE"].sum()        # deplasman takımının gollerini toplar

total_goals = home_goals + away_goals

#print(f"Total goals scored in the Champions League: {total_goals}")

total_goals_per_match = total_goals / df.shape[0]   # maç başına ortalama gol sayısı
#print(f"Average goals scored per match: {total_goals_per_match:.2f}")

#print(df["HOME_TEAM"].head()) # ev sahibi takımların ilk 5 satırını gösterir

home_goals_by_team = df.groupby("HOME_TEAM")["HOME_TEAM_SCORE"].sum() # ev sahibi takımların topladığı goller

#print(home_goals_by_team)

home_goals_by_team = home_goals_by_team.sort_values(ascending=False) # ev sahibi takımların topladığı golleri azalan sıraya göre sıralar

#print(home_goals_by_team)

# Ev sahibi olarak atılan goller
home_goals = df.groupby("HOME_TEAM")["HOME_TEAM_SCORE"].sum()

# Deplasmanda atılan goller
away_goals = df.groupby("AWAY_TEAM")["AWAY_TEAM_SCORE"].sum()

# İkisini takım isimlerine göre topla
total_goals_by_team = home_goals.add(away_goals, fill_value=0)

# Büyükten küçüğe sırala
total_goals_by_team = total_goals_by_team.sort_values(ascending=False)

#print("\nToplam goller (Ev sahibi + Deplasman):")
#print(total_goals_by_team)

top_10_teams = total_goals_by_team.head(10)

#print(top_10_teams)

# Ev sahibiyken yenilen goller
home_conceded = df.groupby("HOME_TEAM")["AWAY_TEAM_SCORE"].sum()

# Deplasmandayken yenilen goller
away_conceded = df.groupby("AWAY_TEAM")["HOME_TEAM_SCORE"].sum()

# Toplam yenilen goller
total_conceded = home_conceded.add(away_conceded, fill_value=0)

# Büyükten küçüğe sırala
total_conceded = total_conceded.sort_values(ascending=False)

#print(total_conceded.head(10))

home_wins = (df["HOME_TEAM_SCORE"] > df["AWAY_TEAM_SCORE"]).sum()
draws = (df["HOME_TEAM_SCORE"] == df["AWAY_TEAM_SCORE"]).sum()
away_wins = (df["HOME_TEAM_SCORE"] < df["AWAY_TEAM_SCORE"]).sum()

print (f"Home wins: {home_wins}")
print (f"Draws: {draws}")
print (f"Away wins: {away_wins}")

import matplotlib.pyplot as plt

#plt.figure(figsize=(10, 6))

#plt.bar(top_10_teams.index, top_10_teams.values)

#plt.title("Top 10 Teams by Total Goals")
#plt.xlabel("Teams")
#plt.ylabel("Goals")

#plt.xticks(rotation=45)

#plt.tight_layout()

#plt.savefig("images/top_10_teams_by_goals.png", dpi=300)

# plt.show() 

labels = ['Home Wins', 'Draws', 'Away Wins']
sizes = [home_wins, draws, away_wins]

plt.figure(figsize=(7, 7))

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

plt.title("Match Outcomes in UEFA Champions League (2016-2022)")

plt.savefig("images/home_advantage_pie.png", dpi=300)

plt.show()
