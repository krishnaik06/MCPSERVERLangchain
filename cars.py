from mcp.server.fastmcp import FastMCP

mcp = FastMCP("cars")

@mcp.tool()
def get_cars()->list[str]:
    """
    Get list of cars avilable in the showroom 
    """
    return ["Toyota","Honda","Ford"]

@mcp.tool()
def get_car_details(car_name:str)->dict:
    """
    Get details of a car
    """
    if car_name=="Toyota":
        return {
            "data": {
                "car_name": "toyota",
                "models": ["Corolla", "Camry", "Rav4"],
                "year": 2023,
                "features": ["Reliable engine", "Advanced safety features", "Fuel efficiency"],
                "manufacturing_country": "Japan"
            }
        }
    elif car_name=="Honda":
        return {
            "data": {
                "car_name": "honda",
                "models": ["Civic", "Accord", "CR-V"],
                "year": 2023,
                "features": ["Reliable engine", "Advanced safety features", "Fuel efficiency"],
                "manufacturing_country": "Japan"
            }
        }
    elif car_name=="Ford":
        return {
            "data": {
                "car_name": "ford",
                "models": ["F150", "Mustang", "Explorer"],
                "year": 2023,
                "features": ["Reliable engine", "Advanced safety features", "Fuel efficiency"],
                "manufacturing_country": "USA"
            }
        }
    
@mcp.tool()
def get_car_price(car_name:str)->float:
    """
    Get price of a car
    """
    if car_name=="Toyota":
        return 100000
    elif car_name=="Honda":
        return 150000
    elif car_name=="Ford":
        return 200000

if __name__=="__main__":
    mcp.run(transport="stdio")
