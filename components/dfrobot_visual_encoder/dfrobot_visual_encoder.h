#pragma once
#include "esphome.h"

class DFRobotVisualEncoder : public Component, public i2c::I2CDevice {
 public:
  // Automation triggers as member objects (fixes MockObj)
  Trigger<void()> clockwise_trigger_;
  Trigger<void()> counter_trigger_;
  Trigger<void()> press_trigger_;
  Trigger<void()> long_press_trigger_;

  // Accessor methods
  Trigger<void()>* get_clockwise_trigger() { return &clockwise_trigger_; }
  Trigger<void()>* get_counter_trigger() { return &counter_trigger_; }
  Trigger<void()>* get_press_trigger() { return &press_trigger_; }
  Trigger<void()>* get_long_press_trigger() { return &long_press_trigger_; }

  void setup() override {
    // Initialize I2C encoder and LED ring
  }

  void loop() override {
    // Read encoder state and call triggers:
    // Example:
    // if (rotated_clockwise()) clockwise_trigger_.trigger();
    // if (rotated_counter()) counter_trigger_.trigger();
    // if (pressed()) press_trigger_.trigger();
    // if (long_pressed()) long_press_trigger_.trigger();
  }

  void set_led_level(float level) {
    // level = 0-100, scale to LED ring
  }
};
