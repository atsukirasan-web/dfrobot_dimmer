#pragma once
#include "esphome.h"

namespace esphome {
namespace dfrobot_visual_encoder {

class DFRobotVisualEncoder : public Component, public i2c::I2CDevice {
 public:
  void setup() override;
  void dump_config() override;
  void loop() override;

  void set_led_level(uint8_t brightness);

 protected:
  uint8_t last_status_{0};

  bool button_pressed_{false};
  uint32_t press_time_{0};

  uint8_t current_led_level_{0};
  uint8_t target_led_level_{0};

  uint32_t last_led_update_{0};
};

}
}
