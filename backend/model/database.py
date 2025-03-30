from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import io
from PIL import Image
import datetime

class DB_blog:
    def __init__(self):
        load_dotenv()
        #logint the env stuff for the database URI for security reasons
        uri = os.getenv("MONGODB_URI")

        # Making a client to do the CRUD stuff 
        # P.S. the doc is kinda trash
        client = MongoClient(uri, server_api=ServerApi('1'))


        # initialising the blog database which stores the
        # .md and the image bson and metadata for the blog posts
        db= client["blog_db"]

        #the blog text and metadata are kept in a seperate collection
        self.blog_coll = db["blog"]
        self.img_coll = db["blog_img"]

    def test_connection(self) -> None:
        try:
            # Send a ping to confirm a successful connection
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

        #the test_connection code is lifted straight from doc...

    def insert_images_pil(self,pil_img:Image.Image, title:str) -> str:
        # Pil to bson conversion
        img_byte = io.BytesIO()

        #add to a virtual file object

        pil_img.save(img_byte, format='PNG')

        img_byte = img_byte.getvalue()

        #dictionay formation

        img_dic = {
            "title": title,
            "img": img_byte,
            "timestamp": datetime.datetime.now()
        }


        return str(self.img_coll.insert_one(img_dic))
    
    def blog_dictionary_construction(self, title:str, content:str, img_id:list[str], writting_date:datetime.datetime) -> dict:

        #formatting and making the dictionary that will be later inserted to
        # to the blog collection in the database

        blog_dic = {
            "title":title,
            "content":content,
            "img_id":img_id,
            "writting_date":writting_date,
            "timestamp_of_insertion":datetime.datetime.now()
        }


        return blog_dic
    
    def insert_blog(self,**kwargs) -> str:
        if ["image_id", "title", "content", "writting_date"] in kwargs:
            blog_dic = self.blog_dictionary_construction(kwargs["title"], kwargs["content"], kwargs["image_id"], kwargs["writting_date"])
        elif blog_dic in kwargs:
            blog_dic = kwargs["blog_dic"]
        else:
            raise ValueError("Please provide the blog dictionary or required fields.")
        
        



