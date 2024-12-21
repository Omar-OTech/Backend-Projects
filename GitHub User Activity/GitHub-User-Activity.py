#!/usr/bin/python3

import sys
import json
from datetime import datetime
import requests

def fetch_github_activity(username):
    """
    Fetch GitHub activity for a given username using the GitHub API.
    Returns the parsed JSON response or raises an exception on error.
    """
    url = f"https://api.github.com/users/{username}/events"
    headers = {
        'User-Agent': 'GitHub-Activity-CLI/1.0',
        'Accept': 'application/vnd.github.v3+json'
    }
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()  # Raises an HTTPError for bad responses
        return res.json()
    except requests.exceptions.HTTPError as err:
        if res.status_code == 404:
            raise ValueError(f"User '{username}' not found on GitHub.")
        elif res.status_code == 403:
            raise RuntimeError("API rate limit exceeded. Try again later.")
        else:
            raise RuntimeError(f"HTTP error: {res.status_code} - {err}")
    except requests.exceptions.ConnectionError as err:
        raise RuntimeError(f"Failed to connect to GitHub API: {err}")
    except requests.exceptions.RequestException as err:
        raise RuntimeError(f"Request failed: {str(err)}")
    
def format_event(event):
    """
    Format a GitHub event into a human-readable string.
    """
    event_type = event['type']
    repo_name = event['repo']['name']
    created_at = datetime.strptime(event['created_at'], "%Y-%m-%dT%H:%M:%SZ")
    time_str = created_at.strftime("%Y-%m-%d %H:%M:%S")
    
    if event_type == 'PushEvent':
        commits = event['payload'].get('commits', [])
        return f"- [{time_str}] Pushed {len(commits)} commit(s) to {repo_name}"
    elif event_type == 'CreateEvent':
        ref_type = event['payload'].get('ref_type', 'unknown')
        return f"- [{time_str}] Created {ref_type} in {repo_name}"
    elif event_type == 'IssuesEvent':
        actions = event['payload'].get('action', 'unknown')
        issue_number = event['payload'].get('issue', {}).get('number', 'unknown')
        return f"- [{time_str}] {actions.capitalize()} issue #{issue_number} in {repo_name}"
    elif event_type == 'PullRequestEvent':
        actions = event['payload'].get('action', 'unknown')
        pr_number = event['payload'].get('pull_request', {}).get('number', 'unknown')
        return f"- [{time_str}] {actions.capitalize()} pull request #{pr_number} in {repo_name}"
    elif event_type == 'WatchEvent':
        return f"- [{time_str}] Starred {repo_name}"
    elif event_type == 'ForkEvent':
        return f"- [{time_str}] Forked {repo_name}"
    else:
        return f"- [{time_str}] {event_type} on {repo_name}"

def main():
    """
    Main function to run the GitHub activity CLI.
    """
    if len(sys.argv) != 2:
        print("Usage: python github_activity.py <username>")
        sys.exit(1)
        
    username = sys.argv[1]
    print(f"Fetching recent GitHub activity for user: {username}")
    print("-" * 60)
    try:
        events = fetch_github_activity(username=username)
        if not events:
            print("No recent activity found.")
            return
        
        for event in events[:10]:  # Display only the 10 most recent events
            try:
                print(format_event(event))
            except KeyError as err:
                print(f"Error formatting event: {err}")
    except ValueError as err:
        print(f"Error: {err}")
    except RuntimeError as err:
        print(f"Error: {err}")
    except Exception as err:
        print(f"Error: {err}")
    print("-" * 60)
    print("Done.")
    
if __name__ == "__main__":
    main()