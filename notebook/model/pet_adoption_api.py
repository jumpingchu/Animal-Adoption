from .base_api import APIBaseModel


class PetAdoptionAPI(APIBaseModel):
    """
    Parameters:
    - animal_id: 動物的流水編號
    - animal_subid: 動物的區域編號
    - animal_area_pkid: 動物所屬縣市代碼
    - animal_shelter_pkid: 動物所屬收容所代碼
    - animal_place: 動物的實際所在地
    - animal_kind: 動物的類型
    - animal_sex: 動物性別
    - animal_bodytype: 動物體型 [SMALL | MEDIUM | BIG]
    - animal_colour: 動物毛色
    - animal_age: 動物年紀
    - animal_sterilization: 是否絕育
    - animal_bacterin: 是否施打狂犬病疫苗
    - animal_foundplace: 動物尋獲地
    - animal_title: 動物網頁標題
    - animal_status: 動物狀態 [NONE | OPEN | ADOPTED | OTHER | DEAD]
    - animal_remark: 資料備註
    - animal_caption: 其他說明
    - animal_opendate: 開放認養時間(起)
    - animal_closeddate: 開放認養時間(迄)
    - animal_update: 動物資料異動時間
    - animal_createtime: 動物資料建立時間
    - shelter_name: 動物所屬收容所名稱
    - album_file: 圖片名稱
    - album_update: 資料更新時間
    - cDate: 資料建立時間
    - shelter_address: 地址
    - shelter_tel: 聯絡電話
    - $top: 取得前幾筆
    - Page: 頁碼 (Y)
    - $filter: 模糊字詞搜尋
    """

    def __init__(
        self,
        animal_id=None,
        animal_subid=None,
        animal_area_pkid=None,
        animal_shelter_pkid=None,
        animal_place=None,
        animal_kind=None,
        animal_sex=None,
        animal_bodytype=None,
        animal_colour=None,
        animal_age=None,
        animal_sterilization=None,
        animal_bacterin=None,
        animal_foundplace=None,
        animal_title=None,
        animal_status=None,
        animal_remark=None,
        animal_caption=None,
        animal_opendate=None,
        animal_closeddate=None,
        animal_update=None,
        animal_createtime=None,
        shelter_name=None,
        album_file=None,
        album_update=None,
        cDate=None,
        shelter_address=None,
        shelter_tel=None,
        top=None,
        Page=None,
        fuzzy_search_dict=None,
    ):
        super().__init__()
        self.params_dict = {
            "animal_id": animal_id,
            "animal_subid": animal_subid,
            "animal_area_pkid": animal_area_pkid,
            "animal_shelter_pkid": animal_shelter_pkid,
            "animal_place": animal_place,
            "animal_kind": animal_kind,
            "animal_sex": animal_sex,
            "animal_bodytype": animal_bodytype,
            "animal_colour": animal_colour,
            "animal_age": animal_age,
            "animal_sterilization": animal_sterilization,
            "animal_bacterin": animal_bacterin,
            "animal_foundplace": animal_foundplace,
            "animal_title": animal_title,
            "animal_status": animal_status,
            "animal_remark": animal_remark,
            "animal_caption": animal_caption,
            "animal_opendate": animal_opendate,
            "animal_closeddate": animal_closeddate,
            "animal_update": animal_update,
            "animal_createtime": animal_createtime,
            "shelter_name": shelter_name,
            "album_file": album_file,
            "album_update": album_update,
            "cDate": cDate,
            "shelter_address": shelter_address,
            "shelter_tel": shelter_tel,
            "top": top,
            "Page": Page,
            "$filter": self.fuzzy_search_param(fuzzy_search_dict),
        }
