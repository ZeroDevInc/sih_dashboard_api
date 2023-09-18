# main.py
from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta
import firebase_admin
from firebase_admin import credentials , auth
import pymongo
import firebase


app = FastAPI()



cred = credentials.Certificate("./firebase.json")
firebase_admin.initialize_app(cred)

# MongoDB Initialization
client = pymongo.MongoClient("mongodb+srv://mongo:mongo@cluster0.4cvm33l.mongodb.net/?retryWrites=true&w=majority")
db = client["sih"]
users_collection = db["users"]

# JWT Settings
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password Hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2PasswordBearer for token retrieval
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# User model
class User(BaseModel):
    username: str
    email: str
    password: str
    # uid : str


# JWT Token Data
class TokenData(BaseModel):
    tokens:list

@app.get('/')
def f1():
    return "Hello"



# User Registration
@app.post("/register/")
async def register_user(request: Request):
    body =await request.json()
    user = body
    # Create user in Firebase Authentication

    print('called')

    try:
        user_record =  auth.create_user(
            email=user["email"],
            password=user["password"],
            display_name=user["username"],
        )
        users_collection.insert_one({"username": user["username"],
  "email": user["email"],
  "vehicles": []})
        
        return {"status":200,"detail":"User created with UID:"+user_record.uid}
        
    except Exception as e:
        return {"status":401, "detail":str(e)}





# User Login
@app.post("/login/", response_model=dict)
async def login_for_access_token(request: Request):
    print(request)
    body =await request.json()
    id_token  = body["token"]
    try:
        print(id_token)
        decoded_token =  auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        user = auth.get_user(uid)
        email = user.email
        
        user_data = users_collection.find_one({"email": email})
        
        user_data["_id"]=str(user_data["_id"])

       
        return {"status":200, "data":user_data}
    
    # add email and token mapping
    
    except auth.ExpiredIdTokenError:
        # Handle token expiration
        return HTTPException(status_code=403,detail="Token Expired")
    except auth.InvalidIdTokenError:
        # Handle invalid token
        return HTTPException(status_code=401,detail="Invalid token")
    except : 
        return HTTPException(status_code=404,detail="Something went wrong")




# Function to get current user from JWT token
async def get_current_user(request : Request):
    token = request.headers.get("Authorization")
    if token is None:
        # go to login page 
        return {"status":401,"detail" : "toekn expired"}
    
    id_token = token.replace("Bearer ", "")
    try:
        decoded_token =  auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        user = auth.get_user(uid)
        email = user.email
        
        if email is None:
            return {"status":401,"detail":"could not validate credentials"}
        
        # Fetch user from MongoDB (you may want to add error handling here)
        user_data = users_collection.find_one({"email": email})
        if user_data is None:
            return {"status":401,"detail":"User not found"}
        return user_data
    except JWTError:
        return {"status":401,"detail":"could not validate credentials"}
    


@app.post("/logout")
async def logout_user(request : Request):
    token = request.headers.get("Authorization")
    return {"status":2000,"detail":"hello"}
    if token is None:
        # go to login page 
        return {"status":401,"detail" : "toekn expired"}
    
    id_token = token.replace("Bearer ", "")
    try:
        # Revoke the user's authentication token
        decoded_token =  auth.verify_id_token(id_token)
        user_id = decoded_token['uid']
        await auth.revoke_refresh_tokens(user_id)
        return {"status" : 200 , "message": "User logged out successfully"}
    except firebase_admin.auth.AuthError as e:
        # Handle any authentication errors here
        return {"status": 50000, "detail":str(e)}



# Get user profile (protected route)
@app.get("/profile/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

