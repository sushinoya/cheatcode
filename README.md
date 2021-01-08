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