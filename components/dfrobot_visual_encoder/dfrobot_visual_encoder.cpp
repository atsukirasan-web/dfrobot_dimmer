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

  static uint32_t last_poll = 0;

  if (millis() - last_poll < 5)
    return;

  last_poll = millis();

  uint8_t status;

  if (this->read_byte(REG_STATUS, &status) != i2c::ERROR_OK)
    return;

  if (status == last_status_)
    return;

  ESP_LOGD(TAG, "Encoder status: %d", status);

  last_status_ = status;

  if (millis() - last_led_update_ < 20)
    return;

  last_led_update_ = millis();

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

void DFRobotVisualEncoder::set_led_level(uint8_t brightness) {
  target_led_level_ = brightness;
}

}
}
