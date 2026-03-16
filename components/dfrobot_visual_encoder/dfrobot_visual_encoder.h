#pragma once
#include "esphome.h"

namespace esphome {
namespace dfrobot_visual_encoder {

class DFRobotVisualEncoder : public Component, public i2c::I2CDevice {
 public:
  Trigger<void()> clockwise_trigger_;
  Trigger<void()> counter_trigger_;
  Trigger<void()> press_trigger_;
  Trigger<void()> long_press_trigger_;

  Trigger<void()>* get_clockwise_trigger() { return &clockwise_trigger_; }
  Trigger<void()>* get_counter_trigger() { return &counter_trigger_; }
  Trigger<void()>* get_press_trigger() { return &press_trigger_; }
  Trigger<void()>* get_long_press_trigger() { return &long_press_trigger_; }

  void setup() override;
  void loop() override;

  void set_led_level(uint8_t brightness);

 protected:
  void handle_rotation_(uint8_t status);
  void handle_button_(uint8_t status);
  void update_led_animation_();

  uint8_t last_status_{0};
  bool button_pressed_{false};
  uint32_t press_time_{0};

  uint8_t current_led_level_{0};
  uint8_t target_led_level_{0};
  uint32_t last_led_update_{0};
};

}  // namespace dfrobot_visual_encoder
}  // namespace esphome
