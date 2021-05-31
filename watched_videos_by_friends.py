# Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2
# Output: ["D"]
# Explanation: 
# You have id = 0 (green color in the figure) and the only friend of your friends is the person with id = 3 (yellow color in the figure).
# def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
from collections import Counter

def find_mutual_friends(friends, id, mutual_id):
    # print('id, mutual_id', id, mutual_id)
    mutual = []
    # print('in separate function',friends[mutual_id])

    if len(friends[mutual_id]) == 0:
        return []
    if mutual_id != id:
        return friends[mutual_id]

    
def find_watched_videos(watchedVideos, mutual_friends):
    video = []
    for i in mutual_friends:
        video.append(watchedVideos[i])
    print(video)
    return video

def find_frequency_videos(videos):
    video = []
    for i in video:
        for j in i:
            video.append(j)
    print(Counter(video).items())
    # video_dict = Counter(video)
    # print(video_dict.items())

def watchedVideosByFriends(watchedVideos, friends, id, level):
    friends_dict = {}
    mutual_friends = []
    mutual = []
    video = []
    searched_friends = []
    for i in range(len(friends)):
        friends_dict[i] = friends[i]
        # print(friends_dict)
    
    if level == 1:
        mutual_friends = friends_dict[id]
        video = find_watched_videos(watchedVideos, mutual_friends)
        find_frequency_videos(video)
    else:
        mutual_friends = friends_dict[id]
        searched_friends.append(id)
        # print(level)
        while level > 0:
            # print('level', level)
            # print('mutual friend', mutual_friends)
            for mutual_id in mutual_friends:
                # print(mutual_id)
                if not mutual_id in searched_friends:
                    # print('not in search')
                    mutual = find_mutual_friends(friends_dict, id, mutual_id)
                    searched_friends.append(mutual_id)
                    # print('searched friends',searched_friends)
                    # print('mutual', mutual)
                    
            level = level - 1    
        return
    print(mutual_friends)

watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
friends = [[1,2],[0,3],[0,3],[1,2]]
id = 0
level = 1
watchedVideosByFriends(watchedVideos, friends, id, level)
# print(find_mutual_friends(friends, id, level))
