from core_service.src.main.model.dto.base_response import BaseResponse;
from fastapi import APIRouter;
from core_service.src.main.model.dto.request.GetParkingByPlate import GetParkingByPlateBodyRequest;
from core_service.src.main.model.dto.response.GetParkingByPlate import GetParkingByPlateBodyResponse;

class ParkingController:

    router = APIRouter();

    """
    1. Get parking price data from plate number (POST)

    Header:
    Content-Type: application/json

    Request:

    ```
    {
        "plate": "B1100FF"
    }

    Response

    ```
    {
        "parking_in_time": "2023-10-19 14:00:00",
        "parking_out_time": "2023-10-19 15:00:00", // Get from current date
        "price": 10000
    }
    ```

    """
    @router.post('/')
    def test(request: GetParkingByPlateBodyRequest):
        # Missing business logic

        response = GetParkingByPlateBodyResponse();
        response.parking_in_time = "2023-11-23 00:00:05";
        response.parking_out_time = "2023-11-23 00:01:13";
        response.price = 10000;
        return BaseResponse.ok(message = "Hello World", data=response);

    """
    2. Mock parking payment (POST)

    This API intended to simulate payment process.

    Header:
    Content-Type: application/json

    Request:

    ```
    {
        "plate": "B1100FF"
    }

    Response

    ```
    null
    ```

    """
    @router.post('/receipt')
    def test_2(self):
        return BaseResponse.ok(message = "Hello World", data={"data": 1});
