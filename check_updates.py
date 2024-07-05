import requests

def check_updates(version, type, name="core"):
    if type == "wordpress":
        url = "https://api.wordpress.org/core/version-check/1.7/"
    elif type == "plugin":
        url = f"https://api.wordpress.org/plugins/info/1.0/{name}.json"
    else:
        raise ValueError("Le type doit être 'wordpress' ou 'plugin'")

    response = requests.get(url)
    data = response.json()

    if type == "wordpress":
        # on vérifier que la clé "offers" existe dans le dictionnaire data
        if "offers" in data:
            # on vient récupérer la version majeure
            major, minor, _ = version.split(".")
            latest_major = data["offers"][0]["version"]

            # On vient recuperer la version mineur
            latest_minor = max([v for v in data["offers"] if v["version"].startswith(f"{major}.{minor}.")], key=lambda v: v["version"])["version"]

            return {"minor": latest_minor, "major": latest_major}
        else:
            raise KeyError("La clé 'offers' n'a pas été trouvée dans les données")

    elif type == "plugin":
        # On vient vérifier que la clé "version" existe dans le dictionnaire data
        if "version" in data:
            latest_major = data["version"]
        else:
            raise KeyError("La clé 'version' n'a pas été trouvée dans les données")

        # on vient extraire la version mineure
        if "." in version:
            major, minor, _ = version.split(".")
            latest_minor = max([v for v in data["versions"] if v.startswith(f"{major}.{minor}.")], key=lambda v: v)
        else:
            latest_minor = None

        return {"minor": latest_minor, "major": latest_major}
