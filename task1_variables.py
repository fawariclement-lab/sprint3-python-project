# Task 1: Variables and Arithmetic
# Sprint Project: Video Game Sales Analysis
#
# This file works with a dataset of the 20 best-selling video games.
# Each game is a list with this layout:
# [rank, name, platform, year, genre, publisher, na_sales, eu_sales, jp_sales, global_sales]
# All sales figures are in millions of copies.

# Column index constants: names for the positions in each game's list,
# so the code below reads clearly instead of using bare numbers.
RANK = 0
NAME = 1
PLATFORM = 2
YEAR = 3
GENRE = 4
PUBLISHER = 5
NA = 6
EU = 7
JP = 8
GLOBAL = 9

# The dataset: 20 best-selling video games of all time.
games = [
    [1, 'Wii Sports', 'Wii', 2006, 'Sports', 'Nintendo', 41.49, 29.02, 3.77, 82.74],
    [2, 'Super Mario Bros.', 'NES', 1985, 'Platform', 'Nintendo', 29.08, 3.58, 6.81, 40.24],
    [3, 'Mario Kart Wii', 'Wii', 2008, 'Racing', 'Nintendo', 15.85, 12.88, 3.79, 35.82],
    [4, 'Wii Sports Resort', 'Wii', 2009, 'Sports', 'Nintendo', 15.75, 11.01, 3.28, 33.00],
    [5, 'Pokemon Red/Pokemon Blue', 'GB', 1996, 'Role-Playing', 'Nintendo', 11.27, 8.89, 10.22, 31.37],
    [6, 'Tetris', 'GB', 1989, 'Puzzle', 'Nintendo', 23.20, 2.26, 4.22, 30.26],
    [7, 'New Super Mario Bros.', 'DS', 2006, 'Platform', 'Nintendo', 11.38, 9.23, 6.50, 30.01],
    [8, 'Wii Play', 'Wii', 2006, 'Misc', 'Nintendo', 14.03, 9.20, 2.93, 29.02],
    [9, 'New Super Mario Bros. Wii', 'Wii', 2009, 'Platform', 'Nintendo', 14.59, 7.06, 4.70, 28.62],
    [10, 'Duck Hunt', 'NES', 1984, 'Shooter', 'Nintendo', 26.93, 0.63, 0.28, 28.31],
    [11, 'Nintendogs', 'DS', 2005, 'Simulation', 'Nintendo', 9.07, 11.00, 1.93, 24.76],
    [12, 'Mario Kart DS', 'DS', 2005, 'Racing', 'Nintendo', 9.81, 7.57, 4.13, 23.42],
    [13, 'Wii Fit', 'Wii', 2008, 'Sports', 'Nintendo', 8.94, 8.03, 3.60, 22.72],
    [14, 'Kinect Adventures!', 'X360', 2010, 'Misc', 'Microsoft Game Studios', 14.97, 4.94, 0.24, 21.82],
    [15, 'Grand Theft Auto V', 'PS3', 2013, 'Action', 'Take-Two Interactive', 7.01, 9.27, 0.97, 21.40],
    [16, 'Grand Theft Auto: San Andreas', 'PS2', 2004, 'Action', 'Take-Two Interactive', 9.43, 0.40, 0.41, 20.81],
    [17, 'Super Mario World', 'SNES', 1990, 'Platform', 'Nintendo', 12.78, 3.75, 3.54, 20.61],
    [18, 'Brain Age: Train Your Brain in Minutes a Day', 'DS', 2006, 'Misc', 'Nintendo', 4.75, 9.26, 4.16, 20.22],
    [19, 'Pokemon Diamond/Pokemon Pearl', 'DS', 2006, 'Role-Playing', 'Nintendo', 6.42, 4.52, 7.38, 20.16],
    [20, 'Super Mario Bros. 3', 'NES', 1988, 'Platform', 'Nintendo', 9.54, 3.44, 3.84, 17.28],
]

# --- Variables ---

# How many games are in the dataset (len() counts the rows).
total_games = len(games)

# The first row (index 0) is the #1 best seller.
top_game_row = games[0]
top_game = top_game_row[NAME]

# --- Arithmetic ---

# Add up the global sales of every game with a loop.
total_global_sales = 0
for game in games:
    total_global_sales = total_global_sales + game[GLOBAL]

# Average global sales per game = total divided by the number of games.
avg_global_sales = total_global_sales / total_games

# The #1 game's share of all global sales, as a percentage.
top_game_share = top_game_row[GLOBAL] / total_global_sales * 100

# --- Results ---
print('Total games:', total_games)
print('Total global sales: $' + str(round(total_global_sales, 2)) + 'M')
print('Average global sales per game: $' + str(round(avg_global_sales, 2)) + 'M')
print('Top game:', top_game)
print('Top game share of global sales:', str(round(top_game_share, 2)) + '%')
