import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c
from esphome.const import CONF_ID

# Define trigger keys
CONF_ON_CLOCKWISE = "on_clockwise"
CONF_ON_COUNTER_CLOCKWISE = "on_counter_clockwise"
CONF_ON_PRESS = "on_press"
CONF_ON_LONG_PRESS = "on_long_press"

# Component namespace
dfrobot_visual_encoder_ns = cg.esphome_ns.namespace("dfrobot_visual_encoder")
DFRobotVisualEncoder = dfrobot_visual_encoder_ns.class_("DFRobotVisualEncoder", cg.Component, i2c.I2CDevice)

# Configuration schema
CONFIG_SCHEMA = cv.Schema({
    cv.Required(CONF_ID): cv.declare_id(DFRobotVisualEncoder),
    cv.Optional(CONF_ON_CLOCKWISE): cv.All(cv.ensure_list(cv.Any()), cv.ensure_list),
    cv.Optional(CONF_ON_COUNTER_CLOCKWISE): cv.All(cv.ensure_list(cv.Any()), cv.ensure_list),
    cv.Optional(CONF_ON_PRESS): cv.All(cv.ensure_list(cv.Any()), cv.ensure_list),
    cv.Optional(CONF_ON_LONG_PRESS): cv.All(cv.ensure_list(cv.Any()), cv.ensure_list),
}).extend(i2c.i2c_device_schema(DFRobotVisualEncoder))

async def to_code(config):
    # Step 1: Create component variable
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)

    # Step 2: Register automation triggers AFTER component exists
    if CONF_ON_CLOCKWISE in config:
        await cg.register_automation(var.get_clockwise_trigger(), config[CONF_ON_CLOCKWISE])
    if CONF_ON_COUNTER_CLOCKWISE in config:
        await cg.register_automation(var.get_counter_trigger(), config[CONF_ON_COUNTER_CLOCKWISE])
    if CONF_ON_PRESS in config:
        await cg.register_automation(var.get_press_trigger(), config[CONF_ON_PRESS])
    if CONF_ON_LONG_PRESS in config:
        await cg.register_automation(var.get_long_press_trigger(), config[CONF_ON_LONG_PRESS])
