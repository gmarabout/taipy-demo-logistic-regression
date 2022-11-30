from taipy import Config
from config.tasks import task_make_X, task_make_Y, task_train, task_predict

pipeline_train = Config.configure_pipeline(
    id="train", task_configs=[task_make_X, task_make_Y, task_train]
)

pipeline_predict = Config.configure_pipeline(id="predict", task_configs=[task_predict])
