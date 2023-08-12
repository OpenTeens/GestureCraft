import os
import requests

username = "frobertpixto"
repository = "hand-drawn-shapes-dataset"

folder_path = "data"

# GitHub API to get the contents of a folder
# api_url = "https://api.github.com/repos/{username}/{repository}/contents/{folder_path}"
shapes = ['triangle', 'rectangle', 'ellipse']
for i in range(3):
    shape = shapes[i]
    print(shape)
    api_url = f"https://api.github.com/repos/frobertpixto/hand-drawn-shapes-dataset/contents/data/user.frt/images/{shape}"

    response = requests.get(api_url)
    print(response)
    print(response.status_code)
    if response.status_code == requests.codes.ok:
        contents = response.json()

        for item in contents:
            if item["type"] == "file" and item["name"].lower().endswith(".png"):
                download_url = item["download_url"]
                response = requests.get(download_url)
                if response.status_code == requests.codes.ok:
                    filename = item["name"]
                    shape2 = shape[0].upper() + shape[1:]
                    directory = f"dataCNN/{shape2}"
                    file_path = os.path.join(directory, filename)

                    with open(file_path, "wb") as f:
                        f.write(response.content)
                    print(f"File '{filename}' downloaded successfully.")
                else:
                    print(f"Failed to download the file '{item['name']}'")
    else:
        print("Failed to get the contents of the folder.")