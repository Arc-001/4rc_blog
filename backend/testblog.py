from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

from model.database import *



# #defining the data model for blog summaries
# class Blog_summary(BaseModel):
#     title: str
#     uid: str
#     content_summary: str

# class Blog_summary_list(BaseModel):
#     blog_list: List[Blog_summary] | None = None

# class blog(BaseModel):
#     title: str
#     uid: str
#     content: str

# class blog_uid_dic(BaseModel):
#     blog_list: dict[str, blog] | None = None



# # Dummy data for testing purposes
# Blog_summary_list_ = Blog_summary_list(blog_list=[
#     Blog_summary(title="Blog 1", uid="1", content_summary="This is the content of blog 1"),
#     Blog_summary(title="Blog 2", uid="2", content_summary="This is the content of blog 2"),
#     Blog_summary(title="Blog 3", uid="3", content_summary="This is the content of blog 3")
# ])

# blog_list_= [blog(title="Blog 1", uid="1", content="This is the full content of blog 1"),
#              blog(title="Blog 2", uid="2", content="This is the full content of blog 2"),
#              blog(title="Blog 3", uid="3", content="This is the full content of blog 3")]

# blog_list_ = blog_uid_dic(blog_list= {blog.uid: blog for blog in blog_list_})


# # Blog_summary_list= Blog_summary_list(blog_list=dummy_blog_list)



app = FastAPI(
    title="Blog API",
    description="API for managing blog summaries",
    version="1.0.0",
    port=5000
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

db = DB_blog()

@app.get("/api/blogs/") 
async def get_blog_summaries() -> List[Blog_summary]:
    return db.get_blog_summary()

@app.get("/api/blog/{uid}", response_model=blog)
async def get_blog(uid: str) -> blog:
    return db.get_blog_uid(uid)



# @app.get("/api/blogs", response_model=Blog_summary_list)
# async def get_blog_summaries():
#     """
#     Get a list of blog summaries.
#     """
#     return Blog_summary_list_


# @app.get("/api/blog/{uid}", response_model=blog)
# async def get_blog(uid: str) :
#     """
#     Get the full content of a blog by its UID.
#     """
#     if blog_list_.blog_list[uid]:
#         return blog_list_.blog_list[uid]
#     else:
#         return blog(title="error", content="error", uid="invalid")
