default_mode = "ARAM"
lolalytics_url = ""

current_data_version = "14.22.1"

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
# so Wukong is MonkeyKing, Cho'Gath is Chogath, Renata Glasc is Renata,
# Xin Zhao is XinZhao

champion_portrait_url = (
    "https://ddragon.leagueoflegends.com/cdn/{version}/img/champion/{champion}.png"
)
