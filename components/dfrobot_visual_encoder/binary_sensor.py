import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from esphome.const import CONF_ID

from . import dfrobot_ns, DFRobotVisualEncoder

DEPENDENCIES = ["dfrobot_visual_encoder"]

ButtonSensor = dfrobot_ns.class_("ButtonSensor", binary_sensor.BinarySensor)

CONFIG_SCHEMA = binary_sensor.binary_sensor_schema().extend(
    {
        cv.GenerateID(): cv.declare_id(ButtonSensor),
        cv.GenerateID("encoder_id"): cv.use_id(DFRobotVisualEncoder),
    }
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])

    await binary_sensor.register_binary_sensor(var, config)

    encoder = await cg.get_variable(config["encoder_id"])
    cg.add(encoder.set_button_sensor(var))
