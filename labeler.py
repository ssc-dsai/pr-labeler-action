from github import Github
import os


# Load environment variables
GITHUB_TOKEN    = os.getenv('GITHUB_TOKEN')
REPO_NAME       = os.getenv('REPO_NAME')
PULL_REQUEST_ID = os.getenv('PULL_REQUEST_ID')
COMMAND         = os.getenv('COMMAND')
LABEL_NAME      = os.getenv('LABEL_NAME')
LABEL_COLOUR    = os.getenv('LABEL_COLOUR')

def find_label(labels):
    foundLabel = False
    for label in labels:
         if label.name == LABEL_NAME:
             foundLabel = True
    return foundLabel

def main():
    github = Github(GITHUB_TOKEN)
    repo = github.get_repo(REPO_NAME)
    pull_request = repo.get_pull(int(PULL_REQUEST_ID))

    # Verify COMMAND
    if COMMAND == "ADD":
        # Check if the Label already exist
        labels = repo.get_labels()
        label_exist = find_label(labels)

        if label_exist:
            # Set label to PR
            pull_request.set_labels(LABEL_NAME)
        else:
            # Create Label to use
            label = repo.create_label(name=LABEL_NAME, color=LABEL_COLOUR, description="Github Action Label")
            # Set label to PR
            pull_request.set_labels(label)

    elif COMMAND == "REMOVE":
        # Removing label from PR
        pull_request.delete_labels()

if __name__ == "__main__":
    main()