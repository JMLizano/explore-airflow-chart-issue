# Airflow chart issue with git-sync and DAGs persistence

This repository reproduces a bug when enabling both git-sync and dags persistence in the
official Airflow Helm chart.
When you have a DAG inside a package, that is importing some other module from the package,
like:

```python
from mypackage.lib.mylib import lib_method
```

the import will fail at DAG execution time if both git-sync and dag persistence are enabled.
The DAG is still displayed in the Web UI, and airflow list it as correctly imported (i.e. 
it is displayed in the output of `airflow dags list`).
When you try to execute the DAG, it will fail right away, without any log output since it fails
before even starting the execution, but if you check the worker logs you will see a message like this:

```bash
Traceback (most recent call last):
  File "/home/airflow/.local/lib/python3.7/site-packages/airflow/models/dagbag.py", line 339, in parse
    loader.exec_module(new_module)
  File "<frozen importlib._bootstrap_external>", line 728, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/opt/airflow/dags/repo/dags/mypackage/mydags/mydag.py", line 6, in <module>
    from mypackage.lib.mylib import lib_method
ModuleNotFoundError: No module named 'mypackage'
```

# Steps to reproduce

1. Create a local K8s cluster:

```bash
$ ./create_cluster.sh
```

2. Install the Airflow chart with both git-sync and dag persistence enabled:

```bash
$ ./install.sh
```

3. Try to execute the DAG, it should fail. You can check the worker logs:

```bash
$ kubectl logs -f sync-error-worker-0
```

4. Update the release, with dags persistence disabled:

```bash
$ ./update.sh
```

5. Try to execute the DAG again, it should work.

