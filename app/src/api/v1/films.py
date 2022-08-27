import math
from enum import Enum
from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import Union, List
from fastapi_cache.decorator import cache


router = APIRouter()

