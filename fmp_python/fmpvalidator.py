import os
from fmp_python.constants import SUPPORTED_CATEGORIES

class FMPValidator():
    
    @classmethod
    def is_valid_category(cls,category):
        return category and category in SUPPORTED_CATEGORIES
