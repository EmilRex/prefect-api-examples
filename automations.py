import yaml

from utils import post, put


def create_or_update_automation(path: str = "automation.yaml"):
    """Create or update an automation from a local YAML file"""
    # Load the definition
    with open(path, "r") as fh:
        payload = yaml.safe_load(fh)

    # Find existing automations by name
    # TODO: Assumes unique names which isn't true
    automations = post("/automations/filter")
    existing_automation = [a["id"] for a in automations if a["name"] == payload["name"]]
    automation_exists = len(existing_automation) > 0

    # Create or update the automation
    if automation_exists:
        print(f"Automation '{payload['name']}' already exists and will be updated")
        put(f"/automations/{existing_automation[0]}", payload=payload)
    else:
        print(f"Creating automation '{payload['name']}'")
        post("/automations/", payload=payload)


if __name__ == "__main__":
    create_or_update_automation()
