#pragma once
#include "esphome.h"

class DFRobotVisualEncoder : public Component, public i2c::I2CDevice {
 public:
  // Automation triggers — declared as member objects
  Trigger<void()> clockwise_trigger_;
  Trigger<void()> counter_trigger_;
  Trigger<void()> press_trigger_;
  Trigger<void()> long_press_trigger_;

  // Accessor methods for Python to_code()
  Trigger<void()>* get_clockwise_trigger() { return &clockwise_trigger_; }
  Trigger<void()>* get_counter_trigger() { return &counter_trigger_; }
  Trigger<void()>* get_press_trigger() { return &press_trigger_; }
  Trigger<void()>* get_long_press_trigger() { return &long_press_trigger_; }

  void setup() override {
    // Initialize I2C encoder, LED ring, etc.
  }

  void loop() override {
    // Encoder logic example:
    // int change = read_encoder();
    // if (change > 0) clockwise_trigger_.trigger();
    // if (change < 0) counter_trigger_.trigger();
    // if (button_pressed()) press_trigger_.trigger();
    // if (button_long_pressed()) long_press_trigger_.trigger();
  }

  void set_led_level(float level) {
    // Update LED ring brightness (0-100)
  }
};
