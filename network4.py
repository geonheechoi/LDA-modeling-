import csv
from collections import defaultdict

input_file = './all_textandidedit.csv'

# A dictionary to store the network information
network = defaultdict(lambda: defaultdict(int))

# A dictionary to store the users and the videos they commented on
users = defaultdict(set)

count = 0
with open(input_file, encoding='utf-8', errors='replace') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        user_id = row[0]
        video_id = row[1]

        # Add the video to the user's set of commented videos
        previous_videos = users[user_id]
        users[user_id].add(video_id)

        # Update the network with the new user's video comment
        for prev_video in previous_videos:
            network[video_id][prev_video] += 1
            network[prev_video][video_id] += 1
        count += 1
        if count == 100:
            break

print(len(network), network['12RnY3Rka8k'])

'''
number of users watched a video in the ranges of user counts
Number of users 0-10, 10-20, 20-30, 40-X
Number of videos 30,   12,    5,    1 


'''

'''
print("Network:")
for video1, edges in network.items():
    for video2, weight in edges.items():
        if weight > 1:
            print(f"Video {video1} and Video {video2} have an edge with weight {weight}")
'''