from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.models import User, Auth
from app.config import get_db
from datetime import datetime
import random, os
from app.utils.crypto import crypto, get_public_ip
from firebase_admin import auth, credentials, firebase_admin

router = APIRouter()

script_dir = os.path.dirname(os.path.realpath(__file__))
json_file_path = os.path.join(script_dir, "firebase_key")

try:
    # Initialize Firebase Admin with the service account JSON file
    cred = credentials.Certificate(json_file_path)
    firebase_admin.initialize_app(cred)
    print("Firebase Admin initialized successfully")
except Exception as e:
    print(f"Error initializing Firebase Admin: {e}")

__all__ = (
    "login",
    "logout"
)

@router.post("/login")
async def login(token: str, db: Session = Depends(get_db)):
    try:
        # Verify the Firebase ID token
        decoded_token = auth.verify_id_token(token.token)
        user_id = decoded_token['uid']
    except auth.InvalidIdTokenError as invalid_token_error:
        return {"message": f"Invalid token: {str(invalid_token_error)}"}
    except Exception as other_error:
        return {"message": f"An error occurred: {str(other_error)}"}

    try:
        existing_user = db.query(User).filter(User.firebase_id == user_id).first()

        if existing_user:
            # User already exists, update the user
            password = "".join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=8))
            hashed_password = crypto.create_hash(password)

            login_with = "Email" if "@" in existing_user.email else "Contact number"

            public_ip = get_public_ip()

            # Update user information
            db.query(User).filter(User.firebase_id == user_id).update({
                "status": 'Active',
                "password": hashed_password
            })

            # Create Auth record
            save_auth_to_db = Auth(firebase_id=user_id, status='Active', login_with=login_with, ip_address=public_ip)
            db.add(save_auth_to_db)

            db.commit()

            updated_password_id = f"{existing_user.user_id}:{password}"

            return {"message": "Updated", "new_id": updated_password_id}

        else:
            return {"Error": "User not found"}

    except Exception as error:
        return {"Error": f"An error occurred: {str(error)}"}


@router.post("/create_user")
async def create_user(token: str, db: Session = Depends(get_db)):
    try:
        # Verify the Firebase ID token
        decoded_token = auth.verify_id_token(token.token)
        get_user = auth.get_user(decoded_token['uid'])

        existing_user = db.query(User).filter(User.email == get_user.email).first()

        if existing_user:
            return {"message": "User already exists"}

        # Prepare user data for database insertion
        unique_user_id = "".join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=8))
        user_password = "".join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=8))
        hashed_password = crypto.create_hash(user_password)

        today_date = datetime.now().date()

        login_with = "Email" if "@" in get_user.email else "Contact number"

        public_ip = get_public_ip()

        # Save user data to the database
        save_to_db = User(
            user_id=unique_user_id,
            firebase_id=get_user.uid,
            password=hashed_password,
            name=get_user.display_name,
            email=get_user.email,
            status='Active',
            phone_no=get_user.phone_number,
            img_url=get_user.photo_url,
            gender="F",
            dob=today_date
        )

        save_auth_to_db = Auth(firebase_id=get_user.uid, status='Active', login_with=login_with, ip_address=public_ip)

        db.add(save_to_db)
        db.add(save_auth_to_db)
        db.commit()

        user_id_password = f"{unique_user_id}:{user_password}"

        return {"message": "Created", "KEY": user_id_password}

    except auth.InvalidIdTokenError as invalid_token_error:
        return {"message": f"Invalid token: {str(invalid_token_error)}"}
    except Exception as other_error:
        return {"message": f"An error occurred: {str(other_error)}"}
