from pydantic import BaseModel

class PropertyRequest(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    age: int
    location: str
    property_type: str
    floor: int
