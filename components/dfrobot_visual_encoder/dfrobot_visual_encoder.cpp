#include "dfrobot_visual_encoder.h"
#include "esphome/core/log.h"

namespace esphome {
namespace dfrobot_visual_encoder {

static const char *TAG = "dfrobot_visual_encoder";

static const uint8_t REG_STATUS = 0x01;
static const uint8_t REG_LED = 0x02;

void DFRobotVisualEncoder::setup() {
  ESP_LOGI(TAG, "DFRobot Visual Encoder starting");
}

void DFRobotVisualEncoder::dump_config() {
  ESP_LOGCONFIG(TAG, "DFRobot Visual Encoder");
}

void DFRobotVisualEncoder::loop() {

  uint32_t now = millis();

  // poll hardware only every 5ms (reduces I²C traffic heavily)
  static uint32_t last_poll = 0;

  if (now - last_poll > 5) {
    last_poll = now;

    uint8_t status;

    if (this->read_byte(REG_STATUS, &status) == i2c::ERROR_OK) {

      if (status != last_status_) {

        handle_rotation_(status);
        handle_button_(status);

        last_status_ = status;
      }
    }
  }

  update_led_animation_();
}

void DFRobotVisualEncoder::handle_rotation_(uint8_t status) {

  if (status == 1) {
    ESP_LOGD(TAG, "Clockwise");
    clockwise_trigger_.trigger();
  }

  if (status == 2) {
    ESP_LOGD(TAG, "Counter Clockwise");
    counter_trigger_.trigger();
  }
}

void DFRobotVisualEncoder::handle_button_(uint8_t status) {

  bool pressed = (status == 3);

  if (pressed && !button_pressed_) {
    press_time_ = millis();
    button_pressed_ = true;
  }

  if (!pressed && button_pressed_) {

    uint32_t duration = millis() - press_time_;
    button_pressed_ = false;

    if (duration > 800) {
      ESP_LOGD(TAG, "Long press");
      long_press_trigger_.trigger();
    } else {
      ESP_LOGD(TAG, "Press");
      press_trigger_.trigger();
    }
  }
}

void DFRobotVisualEncoder::set_led_level(uint8_t brightness) {

  target_led_level_ = brightness;
}

void DFRobotVisualEncoder::update_led_animation_() {

  uint32_t now = millis();

  if (now - last_led_update_ < 20)
    return;

  last_led_update_ = now;

  if (current_led_level_ == target_led_level_)
    return;

  if (current_led_level_ < target_led_level_)
    current_led_level_++;
  else
    current_led_level_--;

  uint8_t leds = (current_led_level_ * 12) / 255;

  uint16_t mask = 0;

  for (int i = 0; i < leds; i++)
    mask |= (1 << i);

  uint8_t data[2];

  data[0] = mask & 0xFF;
  data[1] = mask >> 8;

  this->write(REG_LED, data, 2);
}

}
}