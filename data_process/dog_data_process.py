import pandas as pd
from thefuzz import process

region_dict = {
    2: "臺北市", 13: "雲林縣",
    3: "新北市", 14: "嘉義縣",
    4: "基隆市", 15: "嘉義市",
    5: "宜蘭縣", 16: "臺南市",
    6: "桃園縣", 17: "高雄市",
    7: "新竹縣", 18: "屏東縣",
    8: "新竹市", 19: "花蓮縣",
    9: "苗栗縣", 20: "臺東縣",
    10: "臺中市", 21: "澎湖縣",
    11: "彰化縣", 22: "金門縣",
    12: "南投縣", 23: "連江縣"
}

shelter_dict = {
    48: "基隆市寵物銀行", 71: "嘉義市流浪犬收容中心",
    49: "臺北市動物之家", 72: "嘉義縣流浪犬中途之家",
    50: "新北市板橋區公立動物之家", 73: "臺南市動物之家灣裡站",
    51: "新北市新店區公立動物之家", 74: "臺南市動物之家善化站",
    53: "新北市中和區公立動物之家", 75: "高雄市壽山動物保護教育園區",
    55: "新北市淡水區公立動物之家", 76: "高雄市燕巢動物保護關愛園區",
    56: "新北市瑞芳區公立動物之家", 77: "屏東縣流浪動物收容所",
    58: "新北市五股區公立動物之家", 78: "宜蘭縣流浪動物中途之家",
    59: "新北市八里區公立動物之家", 79: "花蓮縣流浪犬中途之家",
    60: "新北市三芝區公立動物之家", 80: "臺東縣動物收容中心",
    61: "桃園市動物保護教育園區", 81: "連江縣流浪犬收容中心",
    62: "新竹市動物收容所", 82: "金門縣動物收容中心",
    63: "新竹縣動物收容所", 83: "澎湖縣流浪動物收容中心",
    67: "臺中市動物之家南屯園區", 89: "雲林縣流浪動物收容所",
    68: "臺中市動物之家后里園區", 92: "新北市政府動物保護防疫處",
    69: "彰化縣流浪狗中途之家", 96: "苗栗縣生態保育教育中心",
    70: "南投縣公立動物收容所"
}

breed_standard_list = [
    '混種犬', '拉不拉多貴賓犬', '貴賓犬', '瑪爾貴賓混種犬', '瑪爾濟斯犬', '博美犬', '狐狸博美', '柴犬',
    '臘腸犬', '長毛臘腸', '吉娃娃犬', '長毛吉娃娃', '台灣犬', '約克夏', '西施犬', '迷你雪納瑞',
    '大型雪納瑞', '黃金獵犬', '雪納瑞', '米格魯犬', '拉不拉多犬', '哈士奇(西伯利亞雪橇犬)',
    '法國鬥牛犬', '威爾斯柯基犬', '日本狐狸犬', '鬥牛犬(英國)', '德國狼犬(德國牧羊犬)',
    '喜樂蒂牧羊犬', '比熊犬', '英國古代牧羊犬', '邊境牧羊犬', '哈瓦那犬', '可卡獵犬', '可卡犬(美系)',
    '澳洲牧羊犬', '可卡犬(英系)', '比利時牧羊犬(格羅安達/馬利諾/坦比連)', '迷你品(迷你杜賓)',
    '可麗牧羊犬(蘇格蘭牧羊犬)', '中亞牧羊犬', '巴哥犬', '馬瑞馬牧羊犬', '加泰隆尼亞牧羊犬',
    '迷你美國牧羊犬', '邊境梗', '白毛(瑞士)牧羊犬', '德國剛毛指示犬', '秋田犬', '美系秋田犬', '鬆獅犬',
    '西高地白梗', '大麥町', '諾福克梗犬', '北京犬', '獒犬', '杜賓犬', '洛威納犬(羅威那犬)',
    '傑克羅素梗', '拉薩犬', '日本狆', '蝴蝶犬', '牛頭梗', '波士頓梗', '沙皮犬', '英國獵狐犬', '獵狐梗',
    '史必茲(史畢諾犬)', '阿茲卡爾', '巴吉度犬', '高山犬', '騎士比熊', '喜樂蒂柯基', '奧斯卡貴賓犬',
    '黃金貴賓犬', '查理士犬', '美國惡霸犬', '標準貴賓犬', '迷你貴賓犬', '惠比特犬', '玩具貴賓犬',
    '拳師犬', '大白熊(庇里牛斯山犬)', '大丹狗', '薩摩耶犬', '伯恩山犬', '蘇格蘭梗', '阿富汗獵犬',
    '波音達指示犬(英系)', '靈提', '阿拉斯加雪橇犬', '高加索犬', '西藏獒犬', '騎士查理王獵犬',
    '馬士提夫犬', '聖伯納犬', '鬥牛獒犬', '萬能梗', '澳洲(絲毛)梗', '紐波利頓犬(拿波里獒犬)',
    '中國冠毛犬', '愛斯基摩犬', '日本土佐犬', '甲斐犬', '紀州犬', '灰狗(靈提)', '紐芬蘭犬', '西藏梗',
    '波利犬', '阿根廷杜告犬', '貝生吉犬', '貝靈頓梗', '波爾多獒犬', '小型獅子犬', '斯塔福郡鬥牛梗',
    '四國犬', '史賓格犬(激飛犬)', '伯瑞犬', '義大利獒犬', '巴西菲勒犬', '威瑪獵犬', '泰國脊背', '比特犬', '其他犬'
]

data = pd.read_csv('./data/dog_data.csv', index_col=0)
df = data.copy()
df = df.drop_duplicates()
df = df.dropna(how='all', axis=1)

# 以 animal_createtime 作為拾獲日期
df['year'] = df['animal_createtime'].apply(lambda x: x.split('/')[0])
df['month'] = df['animal_createtime'].apply(lambda x: x.split('/')[1])
df['day'] = df['animal_createtime'].apply(lambda x: x.split('/')[2])

def fuzzy_match_breed(breed: str) -> str:
    breed = breed.replace('敖', '獒')
    breed = breed.replace('馬爾濟斯', '瑪爾濟斯')
    match, _score = process.extractOne(breed+'犬', breed_standard_list)
    if match == '混種犬':
        return '米克斯'
    else:
        return match

df['animal_Variety'] = df['animal_Variety'].fillna('')
df['animal_Variety_converted'] = df['animal_Variety'].apply(fuzzy_match_breed)

df['animal_area'] = df['animal_area_pkid'].apply(lambda x: region_dict.get(x))
df['animal_shelter'] = df['animal_shelter_pkid'].apply(lambda x: shelter_dict.get(x))
df.to_csv('./data/dog_data_transformed.csv')