import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_ID

from . import dfrobot_ns, DFRobotVisualEncoder

DEPENDENCIES = ["dfrobot_visual_encoder"]

RotationSensor = dfrobot_ns.class_("RotationSensor", sensor.Sensor)

CONFIG_SCHEMA = sensor.sensor_schema().extend(
    {
        cv.GenerateID(): cv.declare_id(RotationSensor),
        cv.GenerateID("encoder_id"): cv.use_id(DFRobotVisualEncoder),
    }
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])

    await sensor.register_sensor(var, config)

    encoder = await cg.get_variable(config["encoder_id"])
    cg.add(encoder.set_rotation_sensor(var))
