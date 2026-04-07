# from sentence_transformers import SentenceTransformer

# model = SentenceTransformer('all-MiniLM-L6-v2')

# def get_embeddings(chunks):
#     return model.encode(chunks)



# def get_embedding(text: str):
#     return model.encode(text)


model = None

def get_model():
    global model

    if model is None:
        try:
            from sentence_transformers import SentenceTransformer
            print("Loading embedding model... ⏳")
            model = SentenceTransformer('all-MiniLM-L6-v2')
            print("Model loaded ✅")
        except Exception as e:
            print("Error loading model:", e)

    return model