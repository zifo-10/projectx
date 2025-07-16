import uuid
from typing import List, Optional

from pydantic import BaseModel, Field


class MetaDataSchema(BaseModel):
    name: str = Field(..., description="The name of the skill or objective")
    id: str = Field(..., description="Skill ID")


class VideoRequestSchema(BaseModel):
    video: str = Field(..., description="Video URL or path to the video file")
    video_id: Optional[str] = Field(uuid.uuid4(), description="Video ID")
    objective: List[MetaDataSchema] = Field(..., description="List of objectives associated with the video")
    skills: List[MetaDataSchema] = Field(..., description="List of skills associated with the video")
    language: str = Field(..., description="Language of the video")
