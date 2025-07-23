import logging

from infrahub_sdk import InfrahubClient


async def run(
    client: InfrahubClient,
    log: logging.Logger,
    branch: str,
):
    log.info(f"Running example script on {branch}...")
    group = await client.create(kind="CoreStandardGroup", name="Device Group")
    await group.save(allow_upsert=True)

    device = await client.all(kind="DcimDevice")
    device = device[0]
    log.info(f"Got device {device.name.value} with ID {device.id}")

    await group.members.fetch()
    group.members.add(device)
    await group.save(allow_upsert=True)
    print("hi")
