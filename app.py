# from typing import List
# from sentence_transformers import SentenceTransformer, util
# import os






# model = SentenceTransformer("all-MiniLM-L6-v2")




    

# @app.get("/")
# async def root():
#     return {"message": "Welcome to the Post Search API"}


# @app.post("/search")
# def search_posts():
#     prompt = data.prompt
#     posts = data.posts
    

#     if not posts:
#         return {"message": "No posts provided", "results": []}
    
#     if data.ApiKey != os.getenv("API_KEY"):
#         return {"message":"API key is missing !"}

#     def flatten(post: Post):
#         return f"{post.title} {post.description} {' '.join(post.filters)}"

#     flattened_posts = [flatten(post) for post in posts]
#     post_embeddings = model.encode(flattened_posts, convert_to_tensor=True)
#     prompt_embedding = model.encode(prompt, convert_to_tensor=True)

#     similarities = util.cos_sim(prompt_embedding, post_embeddings)[0]
#     similarity_scores = similarities.tolist()

#     top_indices = sorted(range(len(similarity_scores)), key=lambda i: similarity_scores[i], reverse=True)
#     threshold = 0.5
#     top_results = []

#     for idx in top_indices[]:
#         score = similarity_scores[idx]
#         if score >= threshold:
#             top_results.append({
#                 posts[idx].postId,
#             })

#     if top_results:
#         return {"results": top_results}
#     else:
#         return {"results": []}


