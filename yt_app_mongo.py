from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://yt_with_mongo:yt_with_mongo@cluster0.c4r3ium.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")


db= client["yt_manager"]
video_collection=db['videos']
print(video_collection)

def list_all_videos():
    for video in video_collection.find():
        print(f"VideoId: {video['_id']},Name:{video['name']},Time:{video['time']}")
    

   
def add_video(name,time):
   video_collection.insert_one({"name":name, 'time':time})

def update_video(new_name, new_time, video_id):
    video_collection.update_one({'_id':ObjectId(video_id)},
                                {'$set':{'name':new_name,'time':new_time}})

def delete_video(video_id):
    video_collection.delete_one({'_id':ObjectId(video_id)})



def exit_app():
    pass


def main():
    while True :
        print("Youtube Manager App| Choose One among options which are getting printed")
        print("1.List all youtube videos")
        print("2. Add a Youtube Video")
        print("3. Update a youtube video Details")
        print("4.Delete A Youtube Video")
        print("5. Exit this bullshit App")
        choice = input("Enter ur choice: ")
        print()

        # NEW SYNTAX ALERT
        match choice:
            case "1":
                list_all_videos()
            
            case "2":
                name=input("Enter the video name: ")
                time=input("Enter the video time: ")
                add_video(name,time)

            case "3":
                video_id=(input("Enter video Id: "))
                new_name=input("Enter new video name: ")
                new_time=input("Enter new video time: ")
                update_video(new_name, new_time, video_id)

            case "4":
                video_id=(input("Enter video Id: "))
                delete_video(video_id)

            case "5":
                break
            case _:
                print("Invalid Response")
    
    

     

if __name__== "__main__":
  main()
