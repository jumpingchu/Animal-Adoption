from base_api import APIBaseModel


class PetFoodAPI(APIBaseModel):
    """
    Parameters:
    - fitem: 食品種類
    - fsource: 產品來源
    - fusage1: 適用寵物種類
    - forigin: 原產地
    - flegalname: 廠商名稱
    - Page: 頁碼控制
    - api_key: API key
    - $filter: 模糊字詞搜尋
    """

    def __init__(
        self,
        fitem=None,
        fsource=None,
        fusage1=None,
        forigin=None,
        flegalname=None,
        Page=None,
        api_key=None,
        fuzzy_search_dict=None,
    ):
        super().__init__()
        self.params_dict = {
            "fitem": fitem,
            "fsource": fsource,
            "fusage1": fusage1,
            "forigin": forigin,
            "flegalname": flegalname,
            "Page": Page,
            "api_key": api_key,
            "$filter": self.fuzzy_search_param(fuzzy_search_dict),
        }

    # def __repr__(self):
    #     return f"{self.__class__.__name__}(fitem={self.fitem}, fsource={self.fsource}, fusage1={self.fusage1}, forigin={self.forigin}, flegalname={self.flegalname}, Page={self.Page}, api_key={self.api_key}, fuzzy_search_dict={self.fuzzy_search_dict})"
