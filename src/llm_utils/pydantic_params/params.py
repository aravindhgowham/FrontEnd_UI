from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional


class UserChatRequest(BaseModel):
    user_id:str = Field(
        ...,
        title="User ID",
        description="Unique ID of User",
        examples=["u9ca0cb0-d529-469d-b894-98a9"]
    )
    user_input: str = Field(
        ...,
        title="User Input",
        description="User Input for the chat",
        examples=["Hello, How are you?"]
    )

    



