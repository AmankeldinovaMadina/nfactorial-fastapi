from adapters.s3_service import S3Service

from app.config import database

from .repository.repository import ShanyrakRepository


class Service:
    def __init__(
        self,repository: ShanyrakRepository,
        
    ):
        self.repository = repository
        self.s3_service = S3Service()

def get_service():
    repository = ShanyrakRepository(database)
    return Service(repository)