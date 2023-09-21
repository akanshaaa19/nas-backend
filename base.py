from pydantic import BaseModel

class Otp(BaseModel):
    email: str
    otp: int

class Doctor(BaseModel):
    email: str
    first_name: str
    last_name: str
    suffix: str
    phone_number: int
    speciality: list
    clinic_name: str


