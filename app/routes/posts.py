from fastapi import APIRouter, HTTPException

from app.schemas.PostsSchema import *

from app.db.mongodb import *

route = APIRouter()

@route.get("/get_db_health")
def db_health():
    return {
        "database" : str(db.name),
        "status" : "running"
    }


@route.post("/post")
def create_post(post: createPost)->returnPost:

    result = post_collection.insert_one({
        "title" : post.title,
        "content" : post.content
    })

    return {
        "id": str(result.inserted_id),
        "message": "Post created"
    }




## below is hardcoded CRUD

# text_post = {
#     1:{"title": "first post1", "content": "cool content"},
#     2:{"title": "first post2", "content": "cool content"},
#     3:{"title": "first post3", "content": "cool content"},
#     4:{"title": "first post4", "content": "cool content"}
#     }

# @route.get("/post")
# def get_all_post(limit: int=None):
#     if limit:
#         return list(text_post.values())[:limit]
#     else:
#         return text_post

# @route.post("/post")
# def CreatePost(post: createPost)->returnPost:
#     new_post={"title":post.title, "content":post.content}
#     text_post[max(text_post.keys())+1]=new_post
#     return new_post

# @route.put("/post/{id}")
# def updatePost(id: int,post: updatepost):
#     if id not in text_post:
#         raise HTTPException(status_code=404, detail="Post not found")
    
#     update_post = {"title": post.title, "content": post.content}
#     text_post[id]=update_post
#     return update_post


# @route.delete("/post/{id}")
# def deletePost(id:int):
#     if id not in text_post:
#         raise HTTPException(status_code=404, detail="Post not found")
    
#     deleted_post=text_post[id]
#     del text_post[id]
#     return {"message": deleted_post}