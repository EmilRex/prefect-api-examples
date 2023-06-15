from prefect.settings import PREFECT_API_URL, PREFECT_UI_URL

from utils import get_cloud, post


def get_diagnostics():
    print("Prefect Cloud Diagnostics")
    print("========================\n")

    print(f"Prefect API URL: {PREFECT_API_URL.value()}")
    print(f"Prefect UI URL: {PREFECT_UI_URL.value()}")
    print("========================\n")

    me = get_cloud("/me/")
    print(f"User: {me['handle']} ({me['email']})")
    print(f"User ID: {me['id']}")
    print("========================\n")

    workspaces = get_cloud("/me/workspaces")
    current_workspace = [
        w for w in workspaces if w["workspace_id"] in PREFECT_API_URL.value()
    ]
    assert len(current_workspace) == 1
    print(f"Found {len(workspaces)} workspaces")
    print(f"Current workspace: {current_workspace[0]['workspace_handle']}")
    print(f"Current workspace ID: {current_workspace[0]['workspace_id']}")
    print("========================\n")

    print(f"Automations: {post('/automations/count')}")
    print(f"Deployments: {post('/deployments/count')}")
    print(f"Flows: {post('/flows/count')}")
    print(f"Flows Runs: {post('/flow_runs/count')}")
    print("========================\n")


if __name__ == "__main__":
    get_diagnostics()
