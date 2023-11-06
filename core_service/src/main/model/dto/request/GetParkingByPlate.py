from pydantic import BaseModel;

class GetParkingByPlateBodyRequest (BaseModel):
    plate: str;