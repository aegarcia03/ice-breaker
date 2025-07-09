import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False ):
    """scrape information from LinkedIn profiles,
    manually scrape the information from LinkedIn."""
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/aegarcia03/da750fc178f46b3b71432a1c4a31ef2d/raw/9669a25adfaaaa3688fc89d8f452311630385635/scrapin_linkedin_profile.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile_url,
        }
        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10,
        )

    data = response.json().get("person")
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None) and k not in ["certifications"]
    }
    return data

if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/angela-enriquez-garcia19/"
        ),
    )