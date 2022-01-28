from tkinter import Label
from github import Github, Label
import os


# Load environment variables
GITHUB_TOKEN    = os.getenv('GITHUB_TOKEN')
REPO_NAME       = os.getenv('REPO_NAME')
PULL_REQUEST_ID = os.getenv('PULL_REQUEST_ID')
COMMAND         = os.getenv('COMMAND')
LABEL_NAME      = os.getenv('LABEL_NAME')
LABEL_COLOUR    = os.getenv('LABEL_COLOUR')

def main():
    github = Github(GITHUB_TOKEN)
    repo = github.get_repo(REPO_NAME)
    pull_request = repo.get_pull(int(PULL_REQUEST_ID))

    # Verify COMMAND
    if COMMAND == "ADD":
        label = Label(color=LABEL_COLOUR, name=LABEL_NAME)
        pull_request.set_labels(label)
    elif COMMAND == "REMOVE":
        pull_request.delete_labels()

if __name__ == "__main__":
    main()