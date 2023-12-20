class APIBaseModel:
    """農業資料開放平臺網址 & 每個 API 都會用到的模糊搜尋和組合 API URL"""

    def __init__(self):
        self.BASE_URL = (
            "https://data.moa.gov.tw/Service/OpenData/TransService.aspx?UnitId="
        )
        self.api_url_dict = {
            "PetFoodAPI": self.BASE_URL + "wxV177kLhEE3",
            "PetAdoptionAPI": self.BASE_URL + "QcbUEzN6E6DL",
        }

    def fuzzy_search_param(self, fuzzy_search_dict):
        if fuzzy_search_dict:
            params = {k: v for k, v in fuzzy_search_dict.items() if v is not None}
            params = "+and+".join(
                [
                    f"{param_name}+like+{condition}"
                    for param_name, condition in params.items()
                ]
            )
            return params
        return None

    def build_api_url(self):
        api_url = self.api_url_dict.get(self.__class__.__name__)

        # 移除值為 None 的參數
        params = {k: v for k, v in self.params_dict.items() if v is not None}

        # 組合參數成 URL
        query_string = "&".join([f"{key}={value}" for key, value in params.items()])

        return f"{api_url}&{query_string}"
