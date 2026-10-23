# Task 4: Loops
# Sprint Project: Video Game Sales Analysis
#
# Same dataset layout as Task 1:
# [rank, name, platform, year, genre, publisher, na_sales, eu_sales, jp_sales, global_sales]
# All sales figures are in millions of copies.

# Column index constants.
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

# --- Games with global sales over 25 million ---

big_sellers = []
for game in games:
    if game[GLOBAL] > 25:
        big_sellers.append(game[NAME])

print('Games with global sales over 25M (' + str(len(big_sellers)) + ' games):')
for name in big_sellers:
    print(' -', name)

# --- Games released before the year 2000 ---

pre_2000_count = 0
for game in games:
    if game[YEAR] < 2000:
        pre_2000_count = pre_2000_count + 1

print('Games released before 2000:', pre_2000_count)

# --- Total North America sales and total Japan sales ---

total_na_sales = 0
total_jp_sales = 0
for game in games:
    total_na_sales = total_na_sales + game[NA]
    total_jp_sales = total_jp_sales + game[JP]

print('Total North America sales: $' + str(round(total_na_sales, 2)) + 'M')
print('Total Japan sales: $' + str(round(total_jp_sales, 2)) + 'M')

# --- Games published by Nintendo ---

nintendo_games = []
for game in games:
    if game[PUBLISHER] == 'Nintendo':
        nintendo_games.append(game[NAME])

print('Nintendo games (' + str(len(nintendo_games)) + ' of ' + str(len(games)) + '):')
for name in nintendo_games:
    print(' -', name)
