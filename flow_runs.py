from prefect import get_client, get_cloud_client
from prefect.server.schemas.filters import (
    FlowRunFilter,
    FlowRunFilterState,
    FlowRunFilterStateName,
)
from prefect.utilities.asyncutils import sync_compatible


BAD_STATES = [
    "Cancelled",
    "Cancelling",
    "Failed",
]


@sync_compatible
async def list_flow_runs_with_state(states: list[str]):
    async with get_client() as client:
        flow_runs = await client.read_flow_runs(
            flow_run_filter=FlowRunFilter(
                state=FlowRunFilterState(name=FlowRunFilterStateName(any_=states))
            )
        )
    return flow_runs


@sync_compatible
async def delete_flow_runs(flow_runs: list[str]):
    async with get_client() as client:
        for flow_run in flow_runs:
            await client.delete_flow_run(flow_run_id=flow_run.id)


def bulk_delete_flow_runs(states: list[str] = BAD_STATES):
    flow_runs = list_flow_runs_with_state(states)

    if len(flow_runs) == 0:
        print(f"There are no flow runs in state(s) {states}")
        return

    print(f"There are {len(flow_runs)} flow runs with state(s) {states}\n")

    for idx, flow_run in enumerate(flow_runs):
        print(f"[{idx + 1}] Flow '{flow_run.name}' with ID '{flow_run.id}'")

    if input("\n[Y/n] Do you wish to proceed: ") == "Y":
        print(f"Deleting {len(flow_runs)} flow runs...")
        delete_flow_runs(flow_runs)
        print("Done.")
    else:
        print("Aborting...")


if __name__ == "__main__":
    bulk_delete_flow_runs()
