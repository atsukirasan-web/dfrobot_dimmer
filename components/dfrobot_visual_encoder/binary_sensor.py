import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from esphome.const import CONF_ID

from . import DFRobotVisualEncoder

DEPENDENCIES = ["dfrobot_visual_encoder"]

CONF_ENCODER_ID = "encoder_id"

CONFIG_SCHEMA = binary_sensor.binary_sensor_schema().extend(
    {
        cv.GenerateID(CONF_ENCODER_ID): cv.use_id(DFRobotVisualEncoder),
    }
)

async def to_code(config):
    var = await binary_sensor.new_binary_sensor(config)

    encoder = await cg.get_variable(config[CONF_ENCODER_ID])
    cg.add(encoder.set_button_sensor(var))
