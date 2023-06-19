# Import the FastAPI class from the fastapi module.
from fastapi import FastAPI

app = FastAPI(debug=True)

from orders.api import api
