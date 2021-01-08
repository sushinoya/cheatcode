# cheatcode
A tool to check plagiarism and code reuse at hackathons

## Setup 
1. Add your github token to the `GITHUB_ACCESS_TOKEN` environment variable
2. Update hackathon information in config.yaml and add submissions to submissions.tsv
3. Run:
    ```bash
    python3 -m venv .cheatcode-env
    source .cheatcode-env/bin/activate
    pip install -r requirements.txt
    ```

## Usage
```bash
python3 main.py <path-to-config-file> <path-to-submissions-file>
```

If the config file contains a `devpost_link` of the hackathon such as `https://hacknroll2020.devpost.com`, then the script automatically scrapes all the submissions from the hackathon's devpost page and finds the github repos and its contributors for code check.

If a submissions file is provided, then devpost will not be scraped and the submissions file will be used for analysis.