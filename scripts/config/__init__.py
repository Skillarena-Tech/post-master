from pydantic_settings import BaseSettings

class _AWSConfig(BaseSettings):
    creds: bool = True
    aws_access_key: str | None = None
    aws_secret_key: str | None = None
    aws_region: str = 'ap-south-1'

AWSConfig = _AWSConfig()