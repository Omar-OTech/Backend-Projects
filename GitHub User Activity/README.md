# GitHub Activity CLI

A command-line interface tool that fetches and displays recent GitHub activity for any user. This tool provides a quick way to view a user's latest actions on GitHub, including commits, pull requests, issues, and other events.

[GitHub User Activity](https://roadmap.sh/projects/github-user-activity)

## Features

- Fetch recent GitHub activity for any public GitHub user
- Display the 10 most recent events
- Support for multiple event types:
  - Push events (commits)
  - Pull request activities
  - Issue interactions
  - Repository creation
  - Repository starring
  - Repository forking
- Clean, timestamped output format
- Error handling for common scenarios
- No API authentication required for basic usage

## Installation

### Prerequisites

- Python 3.6 or higher
- `requests` library

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/github-activity-cli.git
cd github-activity-cli
```

2. Install required dependencies:
```bash
pip install requests
```

3. Make the script executable (Unix-based systems):
```bash
chmod +x github_activity.py
```

## Usage

Basic usage:
```bash
./github_activity.py <username>
```

Example:
```bash
./github_activity.py torvalds
```

Output example:
```
Fetching recent GitHub activity for user: torvalds
------------------------------------------------------------
- [2024-12-21 15:30:45] Pushed 3 commit(s) to torvalds/linux
- [2024-12-21 14:20:30] Created issue #123 in torvalds/linux
- [2024-12-21 12:15:10] Commented on pull request #456 in torvalds/linux
------------------------------------------------------------
Done.
```

## Error Handling

The tool handles various error scenarios:

- Invalid username
- API rate limiting
- Network connection issues
- Malformed API responses

Error messages are clearly displayed with specific information about the issue.

## API Rate Limiting

This tool uses the GitHub API without authentication, which has a rate limit of 60 requests per hour per IP address. If you need higher rate limits, consider using GitHub API authentication.

## Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## Future Improvements

Potential enhancements for future versions:

- Add GitHub API authentication support
- Implement filtering by event type
- Add support for custom date ranges
- Include more detailed event information
- Add output formatting options (JSON, CSV)
- Implement caching to avoid rate limiting

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Omar
- GitHub: [@Omar](https://github.com/Omar-OTech)

## Acknowledgments

- Thanks to GitHub for providing the public API
- Inspired by the need for a simple command-line tool to track GitHub activity

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/Omar-OTech/github-activity-cli/issues) on the GitHub repository.
