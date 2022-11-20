from fastapi import FastAPI, File, Depends, HTTPException, status
import uvicorn
from primary import if_prime
from invert_image import invert
from login import User, get_current_user, Token, users_db, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from fastapi.responses import StreamingResponse
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime, timedelta

app = FastAPI()

@app.get("/prime/{number}")
async def check_if_prime(number: int):
    if isinstance(number, int) and number < 9223372036854775807 and number >= 2:
        return if_prime(number)
    else:
        return { 'Given parameter is not integer value between 0 - 9223372036854775807' }

@app.post("/picture/invert")
async def invert_image(file: bytes = File(...)):
    return StreamingResponse(invert(file), media_type="image/jpeg")

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/time")
async def get_time(current_user: User = Depends(get_current_user)):
    return datetime.now().strftime("%H:%M:%S")

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)



