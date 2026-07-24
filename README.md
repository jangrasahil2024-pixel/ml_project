## End to End ML project
import dagshub
dagshub.init(repo_owner='jangrasahil2024-pixel', repo_name='ml_project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)