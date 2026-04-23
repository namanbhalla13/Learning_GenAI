from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional, Literal

load_dotenv()

model = ChatOpenAI(model="gpt-4o")


class Review(BaseModel):
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg", "neutral"] = Field(
        default=None,
        description="Return the sentiment of the review as positive, negative, or neutral"
    )
    key_theme: list[str] = Field(
        default=None,
        description="Write all the key themes discussed in the review as a list"
    )
    pros: Optional[list[str]] = Field(
        default=None,
        description="Write all the pros in a list"
    )
    cons: Optional[list[str]] = Field(
        default=None,
        description="Write all the cons in a list"
    )


structured_model = model.with_structured_output(Review)

review_string = """
This phone has a clean and modern design.
It feels comfortable to hold in hand.
The display is bright and clear.
Colors look vibrant and sharp.
The screen size is good for daily use.
Performance is smooth for most tasks.
Apps open quickly without much lag.
It handles multitasking well.
Gaming performance is decent.
Heavy games may show slight lag.
The camera takes good photos in daylight.
Low light photos are average.
Video recording quality is good.
The front camera is fine for selfies.
Battery life lasts a full day.
Charging speed is decent.
The build quality feels solid.
The phone is lightweight.
Software experience is simple and easy.
There are not many unnecessary apps.
Storage is enough for regular users.
Sound quality is clear and loud.
Call quality is good.
Fingerprint sensor works fast.
Face unlock is quick.
The phone supports fast internet.
Connectivity is stable.
Price is reasonable for features.
Overall, it is a good value for money.
It is a good choice for everyday use.
"""

result = structured_model.invoke(review_string)

print(result)
print(result.model_dump())
