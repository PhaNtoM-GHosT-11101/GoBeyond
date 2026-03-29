import urllib.request
import json
import urllib.error

def get_github_info(username):
    user_url = f"https://api.github.com/users/{username}"
    # Setting per_page=100 to get a good chunk of repos, sorted by recently updated
    repos_url = f"https://api.github.com/users/{username}/repos?per_page=100&sort=updated"
    
    # GitHub requires a User-Agent header for API requests
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

    try:
        # 1. Fetch Basic User Information
        user_req = urllib.request.Request(user_url, headers=headers)
        with urllib.request.urlopen(user_req) as response:
            user_data = json.loads(response.read().decode())

        print("=" * 60)
        print(f"   GITHUB PROFILE: {user_data.get('name', username)} (@{user_data.get('login')})")
        print("=" * 60)
        if user_data.get('bio'):
            print(f"Bio: {user_data.get('bio')}")
        print(f"Location: {user_data.get('location', 'N/A')}")
        print(f"Followers: {user_data.get('followers')} | Following: {user_data.get('following')}")
        print(f"Total Public Repositories: {user_data.get('public_repos')}")
        print("=" * 60)

        # 2. Fetch Repository/Project Information
        print("\nFetching portfolio / projects...\n")
        repos_req = urllib.request.Request(repos_url, headers=headers)
        with urllib.request.urlopen(repos_req) as response:
            repos_data = json.loads(response.read().decode())

        if not repos_data:
            print("This user has no public repositories.")
            return

        print("REPOSITORIES:")
        print("-" * 60)
        for i, repo in enumerate(repos_data, 1):
            name = repo.get('name')
            description = repo.get('description') or "No description provided."
            language = repo.get('language') or "N/A"
            stars = repo.get('stargazers_count', 0)
            forks = repo.get('forks_count', 0)
            url = repo.get('html_url')
            
            print(f"{i}. 📁 {name} (⭐ {stars} | 🍴 {forks} | 💻 {language})")
            print(f"   📝 Description: {description}")
            print(f"   🔗 URL: {url}\n")
            
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"❌ Error: The GitHub user '{username}' could not be found.")
        elif e.code == 403:
            print("❌ Error: API rate limit exceeded. GitHub allows 60 requests/hour for unauthorized users.")
        else:
            print(f"❌ HTTP Error fetching data: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"❌ Network Error: Could not connect to GitHub API. {e.reason}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    print("🚀 Welcome to the GitHub Profile Scraper 🚀")
    while True:
        target_username = input("\nEnter a GitHub username (or 'q' to quit): ").strip()
        
        if target_username.lower() == 'q':
            print("Goodbye!")
            break
        elif not target_username:
            print("Username cannot be empty. Try again.")
            continue
            
        get_github_info(target_username)
