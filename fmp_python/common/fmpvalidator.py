import os
from fmp_python.common.constants import SUPPORTED_CATEGORIES, SUPPORTED_INTERVALS

class FMPValidator():
    
    @classmethod
    def is_valid_category(cls,category):
        return category and category in SUPPORTED_CATEGORIES

    @classmethod
    def is_valid_interval(cls,interval):
        return interval and interval in SUPPORTED_INTERVALS
