from fastapi import Depends, UploadFile

from ..service import Service, get_service
from . import router


@router.post("/file")
def upload_file(
    file: UploadFile,
    svc: Service = Depends(get_service),
):
 
 svc.s3_service.upload_file(file.file, file.filename)

 return { "msg": file.filename }