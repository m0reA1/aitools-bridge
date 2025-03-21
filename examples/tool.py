import requests


def get_stars(reponame: str) -> int:
    """Retrieve GitHub repository star count via REST API

    Args:
        reponame: Repository name in "owner/repo" format

    Returns:
        Current stargazers count as integer
    """
    try:
        response = requests.get(
            f"https://api.github.com/repos/{reponame}",
        )
        return response.json()["stargazers_count"]
    except Exception as _:
        return 0


def run():
    print(get_stars("ollama/ollama"))


if __name__ == "__main__":
    run()
