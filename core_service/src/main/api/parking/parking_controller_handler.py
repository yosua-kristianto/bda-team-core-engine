import time;
from datetime import datetime;
from math import radians, cos, sin, asin, sqrt, ceil, floor;
from core_service.src.main.repository.parking_repository import get_parking_data_by_vehicle_plate;

"""
    distance_counter
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees). This function based on haversine formula.

    @link https://stackoverflow.com/a/4913653
"""
def distance_counter(lat1, lng1, lat2, lng2):
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lng1, lat1, lng2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.

    return c * r

"""
    Since Indonesian Rupiah can only paid in hundreds in cash, 
    this function normalize all rupiah payment by flooring the number by nearest hundreds.

    Example:
    current_price 9060
    
"""
def normalize_rupiah(current_price: int):
    # Convert current price to str
    converted_price = str(current_price);
    hundreds = int(converted_price[-2:]);

    return current_price - hundreds;

"""
    handle_issue_parking_price
    This function handle parking price calculation with formula of:

    # Total parking hour
    total_parking_hour  = convert_to_epoch(current_time) - convert_to_epoch(parking_in)
                        = (total_parking_hour / 3600)
    
    # Motorcycle
    base_price = (2000 * round_up(total_parking_hour)) 

    # Car
    base_price = (5000) + (4000 * round_down(total_parking_hour))

    # Truck
    base_price = (7000) + (3000 * round_down(total_parking_hour)) 

    # Penalty
    penalty = 30 / (distance_between_current_coordinate_to_region_plate_in_km) * (The first base price 2000 / 5000 / 7000) 

    # Parking price
    parking_price = base_price + penalty

"""
def handle_issue_parking_price(vehicle_plate: str):
    # Get parking data from the database
    calculation_cfg = get_parking_data_by_vehicle_plate(plate = vehicle_plate);


    # total_parking_hour
    parking_in_epoch = datetime.strptime(calculation_cfg["parking_in"], "%Y-%m-%d %H:%M:%S").strftime("%s");
    current_epoch = datetime.now().strftime("%s");

    total_parking_hour = (int(current_epoch) - int(parking_in_epoch)) / 3600;

    # calculate base price
    base_price = 0;

    match(calculation_cfg["vehicle_category"]):
        case 1:
            # Car
            base_price = 5000 + (4000 * floor(total_parking_hour));
    
        case 2:
            # Truck
            base_price = 7000 + (3000 * floor(total_parking_hour));
    
        case 3:
            # Motorcycle
            base_price = 2000 * ceil(total_parking_hour);
    
    # Current region lat lng is
    current_lat = -6.21462000;
    current_lng = 106.84513000;

    distance = distance_counter(current_lat, current_lng, calculation_cfg["lat"], calculation_cfg["lng"]);

    # Penalty counter
    penalty = 30 / distance;

    match(calculation_cfg["vehicle_category"]):
        case 1:
            # Car
            penalty = penalty * 5000;
    
        case 2:
            # Truck
            penalty = penalty * 7000;
    
        case 3:
            # Motorcycle
            penalty = penalty * 2000;
    
    print("Raw Penalty: ", penalty);
    penalty = normalize_rupiah(floor(penalty));
    
    print("Distance between: ", distance)
    print("Penalty: ", penalty)
    print("Base Price: ", base_price)
    
    return {
        "parking_in_time": calculation_cfg["parking_in"],
        "price_issued_at": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(current_epoch))),
        "price": base_price + penalty
    }
    