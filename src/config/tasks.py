from config.nodes import (
    node_initial_dataset,
    node_prediction,
    node_prediction_model,
    node_X,
    node_Y,
)
from models.data import make_X, make_Y
from models.predict import train, predict
from taipy import Config


task_make_X = Config.configure_task(
    id="make_X",
    input=[node_initial_dataset],
    output=node_X,
    function=make_X,
)

task_make_Y = Config.configure_task(
    id="make_Y",
    input=[node_initial_dataset],
    output=node_Y,
    function=make_Y,
)

task_train = Config.configure_task(
    id="train", input=[node_X, node_Y], output=node_prediction_model, function=train
)

task_predict = Config.configure_task(
    id="predict", input=[node_X, node_Y], output=node_prediction, function=predict
)
