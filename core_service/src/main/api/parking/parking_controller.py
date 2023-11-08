from core_service.src.main.model.dto.base_response import BaseResponse;
from fastapi import APIRouter;
from core_service.src.main.model.dto.request.GetParkingByPlate import GetParkingByPlateBodyRequest;
from core_service.src.main.model.dto.response.GetParkingByPlate import GetParkingByPlateBodyResponse;
from core_service.src.main.api.parking.parking_controller_handler import handle_issue_parking_price;

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
        "price_issued_at": "2023-10-19 15:00:00", // Get from current date
        "price": 10000
    }
    ```

    """
    @router.post('/')
    def issue_parking_price(request: GetParkingByPlateBodyRequest):
        parking_data = handle_issue_parking_price(request.plate);

        response = GetParkingByPlateBodyResponse();
        response.parking_in_time = parking_data["parking_in_time"];
        response.price_issued_at = parking_data["price_issued_at"];
        response.price = parking_data["price"];
        return BaseResponse.ok(message = "Successfully issuing parking price", data = response);

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
