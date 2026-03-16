import esphome.codegen as cg
import esphome.config_validation as cv
from esphome import automation
from esphome.components import i2c
from esphome.const import CONF_ID

DEPENDENCIES = ["i2c"]

dfrobot_ns = cg.esphome_ns.namespace("dfrobot_visual_encoder")

DFRobotVisualEncoder = dfrobot_ns.class_(
    "DFRobotVisualEncoder",
    cg.Component,
    i2c.I2CDevice,
)

CONF_ON_CLOCKWISE = "on_clockwise"
CONF_ON_COUNTER_CLOCKWISE = "on_counter_clockwise"
CONF_ON_PRESS = "on_press"
CONF_ON_LONG_PRESS = "on_long_press"

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(CONF_ID): cv.declare_id(DFRobotVisualEncoder),
            cv.Optional(CONF_ON_CLOCKWISE): automation.validate_automation(single=True),
            cv.Optional(CONF_ON_COUNTER_CLOCKWISE): automation.validate_automation(single=True),
            cv.Optional(CONF_ON_PRESS): automation.validate_automation(single=True),
            cv.Optional(CONF_ON_LONG_PRESS): automation.validate_automation(single=True),
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
    .extend(i2c.i2c_device_schema(0x54))
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])

    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)

    if CONF_ON_CLOCKWISE in config:
        await automation.build_automation(
            config[CONF_ON_CLOCKWISE], [], var.get_clockwise_trigger()
        )

    if CONF_ON_COUNTER_CLOCKWISE in config:
        await automation.build_automation(
            config[CONF_ON_COUNTER_CLOCKWISE], [], var.get_counter_trigger()
        )

    if CONF_ON_PRESS in config:
        await automation.build_automation(
            config[CONF_ON_PRESS], [], var.get_press_trigger()
        )

    if CONF_ON_LONG_PRESS in config:
        await automation.build_automation(
            config[CONF_ON_LONG_PRESS], [], var.get_long_press_trigger()
        )
