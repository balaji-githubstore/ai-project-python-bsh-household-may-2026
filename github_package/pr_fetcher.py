"""
pip install PyGithub
"""
from github import Github
from github.Auth import Token

GITHUB_TOKEN = "***"


def load_pr_code(repo_detail, pr_number):
    auth = Token(GITHUB_TOKEN)
    gb = Github(auth=auth)
    repo = gb.get_repo(repo_detail)

    pr = repo.get_pull(pr_number)

    files = pr.get_files()
    all_code = ""
    for file in files:
        if not file.filename.endswith(".java"):
            continue
        # print(file.filename)

        patch = file.patch
        all_code += f"""
            file: {file.filename}
            {patch}
        """
    return all_code


# result=load_pr_code()
# print(result)
