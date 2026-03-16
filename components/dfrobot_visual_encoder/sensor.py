import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_ID

from . import DFRobotVisualEncoder

DEPENDENCIES = ["dfrobot_visual_encoder"]

CONF_ENCODER_ID = "encoder_id"

CONFIG_SCHEMA = sensor.sensor_schema().extend(
    {
        cv.GenerateID(CONF_ENCODER_ID): cv.use_id(DFRobotVisualEncoder),
    }
)

async def to_code(config):
    var = await sensor.new_sensor(config)

    encoder = await cg.get_variable(config[CONF_ENCODER_ID])
    cg.add(encoder.set_rotation_sensor(var))
