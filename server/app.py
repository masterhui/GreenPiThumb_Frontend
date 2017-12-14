import flask

import json_encoder


def create(image_indexer_full_res, image_indexer_reduced_res, temperature_store, water_level_store, light_store, soil_moisture_store,
           humidity_store, watering_event_store):
    """Creates a new GreenPiThumb flask app.

    Creates a GreenPiThumb app capable of servicing requests to the GreenPiThumb
    frontend's dynamic resources.

    Args:
        image_indexer_full_res: Interface for indexing full resolution GreenPiThumb images.
        image_indexer_reduced_res: Interface for indexing reduced resolution GreenPiThumb images.
        temperature_store: Interface for retrieving temperature records.
        water_level_store: Interface for retrieving water level records.
        light_store: Interface for retrieving light records.
        soil_moisture_store: Interface for retrieving soil moisture records.
        humidity_store: Interface for retrieving humidity records.
        watering_event_store: Interface for retrieving watering event records.

    Returns:
        A Flask app that can serve HTTP requests.
    """
    app = flask.Flask(__name__)
    encoder = json_encoder.Encoder()

    @app.route('/temperatureHistory.json')
    def temperature_history():
        return encoder.encode(temperature_store.get())
        
    @app.route('/waterLevelHistory.json')
    def water_level_history():
        return encoder.encode(water_level_store.get())        

    @app.route('/lightHistory.json')
    def light_history():
        return encoder.encode(light_store.get())

    @app.route('/soilMoistureHistory.json')
    def soil_moisture_history():
        return encoder.encode(soil_moisture_store.get())

    @app.route('/humidityHistory.json')
    def humidity_history():
        return encoder.encode(humidity_store.get())

    @app.route('/wateringEventHistory.json')
    def watering_event_history():
        return encoder.encode(watering_event_store.get())
 
    @app.route('/images_full_res.json')
    def image_index_full_res():
        return encoder.encode(image_indexer_full_res.index())   
        
    @app.route('/images_reduced_res.json')
    def image_index_reduced_res():
        return encoder.encode(image_indexer_reduced_res.index())           

    return app
