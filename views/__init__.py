from socket import fromfd
from .animal_requests import get_all_animals, get_single_animal, create_animal, delete_animal, update_animal
from .location_requests import create_location, get_all_locations, get_single_location, update_location
from .employee_requests import get_all_employees, get_single_employee, create_employee, update_employee
from .customer_requests import get_all_customers, get_single_customer, create_customer, update_customer