#pragma once

#include "esphome.h"
#include "esphome/components/i2c/i2c.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/binary_sensor/binary_sensor.h"

namespace esphome {
namespace dfrobot_visual_encoder {

class DFRobotVisualEncoder : public Component, public i2c::I2CDevice {
 public:
  void setup() override;
  void dump_config() override;
  void loop() override;

  void set_led_level(uint8_t brightness);

  void set_rotation_sensor(sensor::Sensor *sensor) { rotation_sensor_ = sensor; }
  void set_button_sensor(binary_sensor::BinarySensor *sensor) { button_sensor_ = sensor; }

 protected:
  void handle_rotation_(uint8_t status);
  void handle_button_(uint8_t status);
  void update_led_animation_();

  sensor::Sensor *rotation_sensor_{nullptr};
  binary_sensor::BinarySensor *button_sensor_{nullptr};

  uint8_t last_status_{0};

  bool button_pressed_{false};
  uint32_t press_time_{0};

  uint8_t current_led_level_{0};
  uint8_t target_led_level_{0};

  uint32_t last_led_update_{0};
};

}  
}
