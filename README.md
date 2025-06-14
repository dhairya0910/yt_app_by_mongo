# 🎥 YouTube Video Manager (MongoDB + Python)

This is a simple terminal-based Python app that lets you **manage YouTube video records** (name and time) using a **MongoDB Atlas database**.

## 📦 Features

- List all saved videos
- Add a new video (name + duration)
- Update existing video details
- Delete a video
- Clean CLI-based menu system

---

## 🚀 Tech Stack

- 🐍 Python 3.10+
- 🍃 MongoDB Atlas (Cloud DB)
- 📦 `pymongo` for MongoDB interaction

---

## 📁 Project Structure

yt_app_mongo.py # Main application file


---

## 🔧 Setup Instructions

### 1. Clone this repository

🔗 **GitHub Repository**: [yt_app_by_mongo](https://github.com/dhairya0910/yt_app_by_mongo)


2). Install required packages
Make sure pymongo is installed:


pip install pymongo

3. Set up MongoDB Atlas

Create a free cluster on MongoDB Atlas

Add your IP to the allowlist (0.0.0.0 for all)

Get your connection string and update it in the script:


client = MongoClient("your_connection_string")
▶️ How to Run


python yt_app_mongo.py
💡 Sample Commands
Enter 1 to list all videos

Enter 2 to add a new video

Enter 3 to update an existing one (requires _id)

Enter 4 to delete by _id

Enter 5 to exit the app

🧹 Example Output


Youtube Manager App | Choose an option:
1. List all YouTube videos
2. Add a YouTube Video
3. Update a YouTube Video's Details
4. Delete a YouTube Video
5. Exit App

🙋‍♂️ Author
Made with ❤️ by Dhairya Gupta

📜 License
This project is open-source and free to use for exploring purposes.

