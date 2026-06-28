import sqlite3

conn = sqlite3.connect('youtube_video.db')

cursor = conn.cursor()

cursor.execute('''
      CREATE TABLE IF NOT EXISTS Videos(
          id INTEGER PRIMARY KEY,
          name TEXT NOT NULL,
          time TEXT NOT NULL
      )


''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES(?, ?)", (name, time) )
    conn.commit()

def update_video(video_id, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ?  WHERE ID = ?", (name, time, video_id))
    conn.commit()
   

def remove_video(video_id):
    cursor.execute("REMOVE FROM video where id = ?", (video_id, )) # , bhot jaru hn bhai yadd rak ya var na tuple retuekar ga 
    conn.commit()

def main():
   while True:
       print("\n Youtube manger app with DB")
       print("1. List videos")
       print("2. Add videos")
       print("3. Remove videos")
       print("4. Save videos")
       print("5. exit app")
       choice = input("Enter  you choice: ")
       
       if choice == '1':
           list_videos()
       elif choice == '2':
          name  = input("Enter the video name")
          time = input("Enter the video time")
          add_video(name, time)
     
       elif choice == '3':
          video_id = input("Enter video ID to Add ")
          name  = input("Enter the video name: ")
          time = input("Enter the video time: ")
          update_video = add_video(video_id, name, time)
       elif choice == '4':
          video_id = input("Enter video ID to Remove ")
          name  = input("Enter the video name: ")
          time = input("Enter the video time: ")
          remove_video = add_video(remove_video)
       elif choice == '5':
          break
       else:
          print("Invalid choice ")
     
     
   conn.close()




if __name__ == "__main__":
    main()  