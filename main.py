import requests
import pprint
import os
import constants as const
import properties as props


def get_current_data_version(url, last_data_version):

    response = requests.get(url)

    if response.status_code == 200:
        print(
            f"Latest data version on ddragon: {response.json()[0]}"
            f"\nLocal data version: {last_data_version}"
        )

    else:
        print(
            f"Failed to get data version; Status code: {response.status_code}"
            f"\nLocal data version: {last_data_version}"
        )


def download_portrait(url, target_dir, filename):

    full_filename = filename + const.PORTRAIT_FILE_EXT

    file_path = os.path.join(target_dir, full_filename)

    if not os.path.exists(file_path):

        os.makedirs(target_dir, exist_ok=True)
        response = requests.get(url)

        if response.status_code == 200:

            """
            xb' mode means exclusive creation of binary file
            if file exists, should skip writing
            maybe it would be better to
            1) check before request by checking if file exists
            2) put request inside of 'with open', but not sure if its safe
            3) don't proceed with downloading portraits if current_version == last_version
                except of some foobar case when data 'refresh' is required
            """

            with open(file_path, "xb") as file:
                file.write(response.content)

            print(f"Champion portrait for {filename} saved at {file_path}")

        else:
            print(f"Failed to download image; Status code: {response.status_code}")


def download_portraits(url, champions_dict):
    # could use os.makedirs(path, exist_ok=True)

    # os.makedirs(const.PORTRAITS_PATH, exist_ok=True)

    if not os.path.exists(const.PORTRAITS_PATH):
        os.mkdir(const.PORTRAITS_PATH)

    for champ in champions_dict:
        champion_id = champions_dict[champ]["id"]
        champ_portrait_path = const.PORTRAITS_PATH + "/" + champion_id
        if not os.path.exists(champ_portrait_path):
            os.mkdir(champ_portrait_path)

        download_portrait(
            props.champion_portrait_url.format(
                version=props.current_data_version, champion=champion_id
            ),
            champ_portrait_path,
            champion_id,
        )


def main():

    get_current_data_version(props.data_version_list_url, props.current_data_version)

    current_champion_list_url = props.champions_list_url.format(
        version=props.current_data_version
    )
    print(current_champion_list_url)

    champion_list_response = requests.get(current_champion_list_url)

    if champion_list_response.status_code == 200:
        champion_list_json = champion_list_response.json()

        champions_dict = {
            info["id"]: {
                "id": info["id"],
                "name": info["name"],
                "lolalytics_id": info["id"].lower(),
            }
            for champion, info in champion_list_json["data"].items()
        }
        pprint.pprint(champions_dict)
        # replace data where api id does not match lolalytics id
        # print(const.ID_EXCEPTIONS).items()

        for key, value in const.ID_EXCEPTIONS.items():
            if key in champions_dict:
                champions_dict[key].update("lolalytics_id", value)

        pprint.pp(champions_dict)

        # download_portraits(props.champion_portrait_url, champions_dict)

    else:
        print(f"Request failed, status code: {champion_list_response.status_code}")


if __name__ == "__main__":
    main()
