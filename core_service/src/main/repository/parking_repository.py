
"""
SELECT 
    A.vehicle_plate, 
    A.parking_in,
    A.detected_vehicle_category
    C.latitude,
    C.longitude
FROM 
    pms_tbl_parking A
    LEFT JOIN mst_tbl_plate_config B
        ON A.detected_vehicle_plate_config_id = B.plate_config_id
    JOIN mst_tbl_region C
        ON B.region_id = C.region_id
WHERE
    vehicle_plate = plate
"""
def get_parking_data_by_vehicle_plate(plate: str):
    # 
    return {
        "vehicle_plate": "",
        "parking_in": "2023-11-08 14:12:05",
        "lat": -6.241586,
        "lng": 106.992416,
        "vehicle_category": 1
    };