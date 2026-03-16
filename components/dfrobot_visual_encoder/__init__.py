import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c, automation
from esphome.const import CONF_ID

DEPENDENCIES = ["i2c"]

my_encoder_ns = cg.esphome_ns.namespace("my_dfrobot_encoder")

MyDFRobotEncoder = my_encoder_ns.class_(
    "MyDFRobotEncoder",
    cg.Component,
    i2c.I2CDevice,
)

# Trigger keys
CONF_ON_CLOCKWISE = "on_clockwise"
CONF_ON_COUNTER_CLOCKWISE = "on_counter_clockwise"
CONF_ON_PRESS = "on_press"
CONF_ON_LONG_PRESS = "on_long_press"

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(MyDFRobotEncoder),

            cv.Optional(CONF_ON_CLOCKWISE): automation.validate_automation(),
            cv.Optional(CONF_ON_COUNTER_CLOCKWISE): automation.validate_automation(),
            cv.Optional(CONF_ON_PRESS): automation.validate_automation(),
            cv.Optional(CONF_ON_LONG_PRESS): automation.validate_automation(),
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