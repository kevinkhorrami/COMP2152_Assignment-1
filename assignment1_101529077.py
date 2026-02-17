"""
Author: Kevin Khorrami
Assignment: #1
"""

# Step b: Create 4 variables

character_name: "Galarec"
player_current_level = 65
player_goal_level = 70
avg_quest_xp = 12000 # mins spent per quest

# Step c: Create a dictionary named xp_required_per_level

xp_required_per_level = {
    "60-61": 494000,
    "61-62": 574700,
    "62-63": 614400,
    "63-64": 650300,
    "64-65": 682300,
    "65-66": 710200,
    "66-67": 734100,
    "67-68": 753700,
    "68-69": 768900,
    "69-70": 779700
}

# Step d: Calculate total quests needed using a loop and add to dictionary

total_xp_needed = 0

for level in range(player_current_level, player_goal_level):
    level_key = f"{level}-{level+1}"
    total_xp_needed += xp_required_per_level[level_key]
    
xp_required_per_level["total_xp_to_goal"] = total_xp_needed # total xp needed

quests_needed = total_xp_needed // avg_quest_xp
xp_required_per_level["quests_needed"] = quests_needed # quests needed
print(f"Quests needed {quests_needed}")

# Step e: Create a 2D nested list called character_list

character_list = [
    ["Galarec", "Paladin", 65, 70],
    ["Shadowmend", "Priest", 63, 70],
    ["Tankzilla", "Warrior", 67, 70],
    ["Pewpew", "Hunter", 61, 65],
    ["Healbot", "Druid", 70, 70]
]

# Step f: Slice the workout_list

first_chars = character_list[0:3]

# Step g: Check if any friend's is less than level 70

for char in character_list:
    if char[2] >= 70:  # check char's current level
        print(f"{char[0]} has reached max level!")
        
# Step h: User input to look up a friend

search_name = input("Enter character name to search: ")

for char in character_list:
    if char[0] == search_name:
        print(f"Found {char[0]} - {char[1]}, Level {char[2]}, Goal: {char[3]}")
        break
else:
    print(f"Character {search_name} not found")
    
# Step i: Friend with highest and lowest level

highest_level_char = character_list[0]
lowest_level_char = character_list[0]

for char in character_list:
    if char[2] > highest_level_char[2]:  # char[2] is current_level
        highest_level_char = char
    if char[2] < lowest_level_char[2]:
        lowest_level_char = char

print(f"Highest level: {highest_level_char[0]} at level {highest_level_char[2]}")
print(f"Lowest level: {lowest_level_char[0]} at level {lowest_level_char[2]}")