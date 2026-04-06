import sys, os
sys.path.insert(0, os.path.expanduser("~/.local/pipx/venvs/google-ads-mcp/lib/python3.14/site-packages"))
import google.auth
from google.ads.googleads.client import GoogleAdsClient

credentials, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/adwords"])
client = GoogleAdsClient(credentials=credentials, developer_token=os.environ["GOOGLE_ADS_DEVELOPER_TOKEN"], login_customer_id="9609634096")

CUSTOMER_ID = "3271061793"

service = client.get_service("AdGroupCriterionService")

KEYWORDS = [
    # (ad_group_id, keyword_text, match_type)
    (192035967734, "threat intelligence for fortinet", "PHRASE"),     # Fortinet
    (192035967734, "firewall threat feed provider", "PHRASE"),        # Fortinet
    (193441711876, "opnsense suricata threat feeds", "PHRASE"),       # OPNsense
]

if "--execute" not in sys.argv:
    print("=== DRY RUN ===")
    for ag_id, kw, mt in KEYWORDS:
        print(f"  Ad Group {ag_id}: [{mt}] \"{kw}\"")
    print(f"\n{len(KEYWORDS)} keywords to add. Run with --execute to apply.")
    sys.exit(0)

print("=== EXECUTING ===")
operations = []
for ag_id, kw_text, match_type in KEYWORDS:
    op = client.get_type("AdGroupCriterionOperation")
    criterion = op.create
    criterion.ad_group = client.get_service("AdGroupService").ad_group_path(CUSTOMER_ID, ag_id)
    criterion.keyword.text = kw_text
    criterion.keyword.match_type = getattr(client.enums.KeywordMatchTypeEnum, match_type)
    operations.append(op)

response = service.mutate_ad_group_criteria(customer_id=CUSTOMER_ID, operations=operations)
print(f"Added {len(response.results)} keywords:")
for r in response.results:
    print(f"  {r.resource_name}")
