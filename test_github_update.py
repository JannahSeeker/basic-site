import requests
import json
import base64

# GitHub repository details
github_token = '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'  # Replace with your GitHub Personal Access Token
repo_owner = 'JannahSeeker'
repo_name = 'Posts'
file_path = 'Entries.json'  # Path to the file in your repository
api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}'

def update_github_file():
    try:
        # Fetch data or perform operations to get content to write to file
        content = 'New content to write to file'

        # Base64 encode content
        encoded_content = base64.b64encode(content.encode()).decode()

        # Fetch current file data from GitHub
        response = requests.get(api_url, headers={'Authorization': f'token {github_token}'})

        if not response.ok:
            response.raise_for_status()

        data = response.json()
        sha = data['sha']

        # Update file on GitHub
        update_data = {
            'message': 'Update file via Python script',
            'content': encoded_content,
            'sha': sha
        }
        update_response = requests.put(api_url, headers={'Authorization': f'token {github_token}'}, json=update_data)

        if not update_response.ok:
            update_response.raise_for_status()

        print('File updated successfully on GitHub!')

    except requests.exceptions.RequestException as e:
        print(f'Error updating file on GitHub: {e}')

# Execute the function to update the file
update_github_file()
