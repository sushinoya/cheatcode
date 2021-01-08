import requests
from bs4 import BeautifulSoup

devpost_link = "https://hacknroll2020.devpost.com"


def get_all_entries(devpost_hackathon_link:str):
    submissions_link_by_page = lambda page_num: f"{devpost_hackathon_link}/project-gallery?page={page_num}"
    all_entries = []
    curr_page = 1

    while True:
        page = requests.get(submissions_link_by_page(curr_page)).text
        soup = BeautifulSoup(page, 'html.parser')
        entries_a_tags = soup.findAll("a", {"class": "link-to-software"})
        curr_page_entries = [tag.attrs['href'] for tag in entries_a_tags]
        all_entries.extend(curr_page_entries)
        curr_page += 1

        if not curr_page_entries:
            break

    return all_entries


def get_github_link_from_devpost_user_page(devpost_url: str):
    page = requests.get(devpost_url).text
    soup = BeautifulSoup(page, 'html.parser')
    octocat_logo = soup.find("span", {"class": "ss-octocat"})

    if not octocat_logo:
        return None
    else:
        return octocat_logo.find_next('a').attrs['href']


def get_github_link_from_devpost_entry_page(devpost_url: str):
    page = requests.get(devpost_url).text
    soup = BeautifulSoup(page, 'html.parser')
    github_a_tags = soup.select("a[href*=github]")

    if not github_a_tags:
        return None
    else:
        return github_a_tags[0].attrs['href']


def get_team_devpost_links_from_entry_page(devpost_url: str):
    page = requests.get(devpost_url).text
    soup = BeautifulSoup(page, 'html.parser')
    teammates_list_items = soup.find_all("li", {"class": "software-team-member"})
    teammates_devpost_links = [item.find("a").attrs["href"] for item in teammates_list_items]
    return teammates_devpost_links


def collate_submissions(devpost_hackathon_link: str, out_file: str):
    print("Collating all hackathon submissions...")
    submission_links = get_all_entries(devpost_hackathon_link)

    with open(out_file, "w+") as submissions_out_file:
        submissions_out_file.write("devpost_url\trepo_url\tauthors\n")

        for i, submission_link in enumerate(submission_links[:5]):
            print(f"Processing entry {i + 1} of {len(submission_links)}")
            github_link = get_github_link_from_devpost_entry_page(submission_link)
            team_devpost_links = get_team_devpost_links_from_entry_page(submission_link)
            team_github_links = list(filter(None, [get_github_link_from_devpost_user_page(link) for link in team_devpost_links]))
            team_github_usernames = ",".join([link.split("github.com/")[1].rstrip("/") for link in team_github_links])
            submissions_out_file.write(f"{submission_link}\t{github_link}\t{team_github_usernames}\n")

# collate_submissions(devpost_link, "random.tsv")