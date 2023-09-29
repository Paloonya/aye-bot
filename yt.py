import yandex_tracker_client
from yandex_tracker_client import TrackerClient

client = TrackerClient(token="y0_AgAAAAAye5SAAAqT1gAAAADt5kn3O3k0EFH0S32JfFv5spfjGRJhVV0", cloud_org_id="bpflan7qab3v2um9dton")

issue=client.issues['RBZG-1']
status = bytes.decode(issue.status)
print (status.encode("utf-8"))