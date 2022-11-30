from taipy import Config


node_initial_dataset = Config.configure_data_node(id="initial_dataset")

node_X = Config.configure_data_node(id="X")

node_Y = Config.configure_data_node(id="Y")

node_prediction_model = Config.configure_data_node(id="prediction_model")

node_prediction = Config.configure_data_node(id="prediction")
