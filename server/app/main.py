# COMMIT INTENT: feat(server): minimal FastAPI app + health endpoint

# FastAPI app class
from fastapi import FastAPI                         

# create an application instance with a title
app = FastAPI(title="The Shelf API")               

# simple probe for uptime checks
@app.get("/health")                                 
def health():
    # returns 200 with a JSON body
    return {"status": "ok"}                         
