from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
# import datetime
from pydantic import BaseModel
from typing import List

#defining the data model for blog summaries
class Blog_summary(BaseModel):
    title: str
    uid: str
    content: str


class blog(BaseModel):
    title: str
    uid: str
    content: str



'''
Blog summary response example:
[
    {
        title: "Blog 1",
        content: `
        $ sqrt() O(log_2(n)) $
        `
        
    },
    {
        title: "Blog 2",
        content: "==Blog 2==\n\n :smile: This is~the~content of blog 2 $\\sqrt{3x-1} + (1+x)^2$"
    },
    {
        title: "Blog 3",
        content: "# Blog 3\n\nThis is the content of blog 3 Check out this website: ![test_img](https://www.gstatic.com/images/branding/googlelogo/svg/googlelogo_clr_74x24px.svg)"
    }
]
'''


class DB_blog:
    def __init__(self):
        load_dotenv()
 
 
        #getting db uri 
        uri = os.getenv("MONGODB_URI")
        self.client = MongoClient(uri, server_api=ServerApi('1'))
 
 
        db= self.client["blog_db"]
 
 
        self.blog_collection = db["blog"]
        self.blog_summary_collection = db["blog_summary"]
 


        
        if not self.test_connection():
            raise Exception("Failed to connect to MongoDB. Please check your connection string.")
        

    def test_connection(self) -> bool:
        try:
            # Send a ping to confirm a successful connection
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            return True
        
        
        except Exception as e:
            print(e)
            return False

    def get_blog_summary(self) -> List[Blog_summary]:
        blog_summaries = self.blog_summary_collection.find()
        return [Blog_summary(**blog) for blog in blog_summaries]

    
    def get_blog_uid(self, uid:str) -> blog:
        try:
            blog_ = self.blog_collection.find_one({"uid": uid})
            return blog(**blog_) if blog_ else None
        except Exception as e:
            print(e)
            return None

    def add_blog_and_summary(self, blog_:blog, summary_:Blog_summary) -> bool:
        try:
            self.blog_collection.insert_one(blog_.model_dump())
            self.blog_summary_collection.insert_one(summary_.model_dump())
            return True
        except Exception as e:
            print(f"Error inserting blog or summary: {e}")
            return False

    def delete_blog(self, uid: str) -> None:
        try:
            self.blog_collection.delete_one({"uid": uid})
            self.blog_summary_collection.delete_one({"uid": uid})
        except Exception as e:
            print(f"Error deleting blog or summary: {e}")

    
    def update_blog(self, uid: str, updated_blog: blog) -> None:
        try:
            self.blog_collection.update_one({"uid": uid}, {"$set": updated_blog.model_dump()})
            self.blog_summary_collection.update_one({"uid": uid}, {"$set": {"title": updated_blog.title, "content": updated_blog.content}})
        except Exception as e:
            print(f"Error updating blog or summary: {e}")


    def update_blog_summary(self, uid: str, updated_summary: Blog_summary) -> None:
        try:
            self.blog_summary_collection.update_one({"uid": uid}, {"$set": updated_summary.model_dump()})
        except Exception as e:
            print(f"Error updating blog summary: {e}")



if __name__ == "__main__":
    db = DB_blog()
    #check for the presence of dummy blog
    if not db.get_blog_summary() and not db.get_blog_uid("1"):
        print("No blog summaries found. Adding dummy data...")
        dummy_blogs = [
            blog(title="Hello world", uid="1", content="==Blog 1==This is the content of blog 1 with math $\\sqrt{n}$ and ==highlight==."),
            blog(title="Blog 2", uid="2", content="==Blog 2==\n\n:smile: This is~the~content of blog 2 $\\sqrt{3x-1} + (1+x)^2$"),
            blog(title="Blog 3", uid="3", content="==Blog 3==\n\n![test_img](https://www.gstatic.com/images/branding/googlelogo/svg/googlelogo_clr_74x24px.svg)")
        ]
        dummy_summaries = [
            Blog_summary(title=b.title, uid=b.uid, content=b.content) for b in dummy_blogs
        ]
        for b, s in zip(dummy_blogs, dummy_summaries):
            db.add_blog_and_summary(b, s)
        print("Dummy data added.")
    else:
        print("Blog summaries found.")
