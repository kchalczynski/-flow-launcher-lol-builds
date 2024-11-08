current_data_version = "14.22.1"

default_mode = "ARAM"

# champion name, usually like champions_dict.champion[id] parameter, lower case
# So no spaces or special characters
# I.e. Xin Zhao is xinzhao, Cho'Gath is chogath, Renata Glasc is renata
# Only exception is Wukong, his id = "MonkeyKing", but "wukong" on lolalytics

lolalytics_url = "https://lolalytics.com/lol/{champion}/aram/build/"

# this url is basically const, but I'll leave it here for now

data_version_list_url = "https://ddragon.leagueoflegends.com/api/versions.json"

# champion json and/or dictionary (and portraits) should be stored in some file
# as cache
# if version number changes, champion list is updated
# portraits can be updated manually, or same as champion list
# no point in comparing images, it's downloaded anyways I guess

champions_list_url = (
    "https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json"
)


# champion name in this url is champions_dict.champion[id] parameter, case sensitive
# I.e. Wukong is MonkeyKing, Cho'Gath is Chogath, Renata Glasc is Renata,
# Xin Zhao is XinZhao

champion_portrait_url = (
    "https://ddragon.leagueoflegends.com/cdn/{version}/img/champion/{champion}.png"
)
