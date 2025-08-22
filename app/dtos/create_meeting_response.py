from typing import Annotated

from pydantic import BaseModel, Field

# 기존 default_config 대신 frozen_config 사용
from app.dtos.frozen_config import FROZEN_CONFIG


class CreateMeetingResponse(BaseModel):
    model_config = FROZEN_CONFIG

    url_code: Annotated[str, Field(description="회의 URL 코드. unique 합니다.")]
