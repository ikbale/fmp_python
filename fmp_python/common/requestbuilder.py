from fmp_python.common.fmpdecorator import FMPDecorator
from fmp_python.common.constants import BASE_URL
from fmp_python.common.fmpvalidator import FMPValidator
from fmp_python.common.fmpexception import FMPException


class RequestBuilder(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.__base_url = BASE_URL
        self.__category = None
        self.__subcategories = []
        self.__query_params = {}


    def __build_category(self):
        if self.__category is None:
            raise FMPException("Category should not be empty !") 
        return ''.join(['/', self.__category])

    def __build_subcategories(self):
        subcategories = '/'.join(self.__subcategories)
        return ''.join(['/', subcategories]) if subcategories else ''
    
    def __build_query_params(self):
        if len(self.__query_params) ==  0:
            return ''
    
        query_params_dict = self.__query_params.copy()                

        query_string = '?'
        while len(query_params_dict) > 0:
            item = query_params_dict.popitem()
            pair_string = ''.join([item[0], '=', str(item[1])])           
            query_string = ''.join([query_string, pair_string])
            
            if len(query_params_dict) != 0:
                query_string = ''.join([query_string, '&'])
        
        return query_string
    
    def set_category(self, category):
        if FMPValidator.is_valid_category(category):
            self.__category = category
        else:
            raise FMPException("Category is not valid !", RequestBuilder.set_category.__name__) 
    
    def add_sub_category(self, subcategory):
        if subcategory:
            self.__subcategories.append(subcategory)

    def set_query_params(self, query_params):
        self.__query_params = query_params
    
    def add_query_param(self, query_param):
        if query_param:
            self.__query_params.update(query_param)

    @FMPDecorator.inject_api_key
    def compile_request(self):
        category = self.__build_category()
        subcategories = self.__build_subcategories()
        query_params = self.__build_query_params()

        return ''.join([self.__base_url, category, subcategories, query_params])
        
