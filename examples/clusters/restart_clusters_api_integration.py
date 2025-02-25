import os
import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

latest = w.clusters.select_spark_version(latest=True)

cluster_name = f'sdk-{time.time_ns()}'

clstr = w.clusters.create(cluster_name=cluster_name,
                          spark_version=latest,
                          instance_pool_id=os.environ["TEST_INSTANCE_POOL_ID"],
                          autotermination_minutes=15,
                          num_workers=1).result()

_ = w.clusters.restart(cluster_id=clstr.cluster_id).result()

# cleanup
w.clusters.permanent_delete(permanent_delete=clstr.cluster_id)
