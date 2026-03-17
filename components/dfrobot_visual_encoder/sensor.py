import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_ID

DEPENDENCIES = ["dfrobot_visual_encoder"]

dfrobot_ns = cg.esphome_ns.namespace("dfrobot_visual_encoder")
DFRobotVisualEncoder = dfrobot_ns.class_("DFRobotVisualEncoder", cg.Component)

CONFIG_SCHEMA = sensor.sensor_schema(
    unit_of_measurement="steps",
    accuracy_decimals=0,
).extend(
    {
        cv.GenerateID(): cv.use_id(DFRobotVisualEncoder),
    }
)


async def to_code(config):
    parent = await cg.get_variable(config[CONF_ID])
    sens = await sensor.new_sensor(config)
    cg.add(parent.set_rotation_sensor(sens))
