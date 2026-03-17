import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from esphome.const import CONF_ID

DEPENDENCIES = ["dfrobot_visual_encoder"]

dfrobot_ns = cg.esphome_ns.namespace("dfrobot_visual_encoder")
DFRobotVisualEncoder = dfrobot_ns.class_("DFRobotVisualEncoder", cg.Component)

CONFIG_SCHEMA = binary_sensor.binary_sensor_schema().extend(
    {
        cv.GenerateID(): cv.use_id(DFRobotVisualEncoder),
    }
)


async def to_code(config):
    parent = await cg.get_variable(config[CONF_ID])
    sens = await binary_sensor.new_binary_sensor(config)
    cg.add(parent.set_button_sensor(sens))
