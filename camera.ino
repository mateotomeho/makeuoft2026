#include "esp_camera.h"
#include <WiFi.h>
#define CAMERA_MODEL_AI_THINKER
#include "camera_pins.h"
// ===========================
// Select camera model in board_config.h
// ===========================
#include "esp_wpa2.h"  // Make sure this is included


// ===========================
// Enter your WiFi credentials
// ===========================
const char* ssid = "UofT";
const char* username = "***";
const char* password = "***";

// Forward declarations
void startCameraServer();
void setupLedFlash();

void setup() {
  Serial.begin(115200);
  Serial.setDebugOutput(true);
  Serial.println();
  
  // Camera configuration
  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sccb_sda = SIOD_GPIO_NUM;
  config.pin_sccb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG;

    // Frame buffer and PSRAM setup
  config.frame_size = FRAMESIZE_SVGA;  // UXGA may fail without PSRAM
  config.fb_location = CAMERA_FB_IN_PSRAM;
  config.jpeg_quality = 12;
  config.fb_count = 2;
  config.grab_mode = CAMERA_GRAB_LATEST;

  // Initialize camera
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x\n", err);
    return;
  }

  setupLedFlash();

  // Flip settings if needed
  sensor_t* s = esp_camera_sensor_get();
  s->set_vflip(s, 1);  // Flip vertically if your image is upside down

  // Connect to UofT Wi-Fi (WPA2 Enterprise)
  WiFi.mode(WIFI_STA);  // Station mode
  esp_wifi_sta_wpa2_ent_set_identity((uint8_t*)username, strlen(username));
  esp_wifi_sta_wpa2_ent_set_username((uint8_t*)username, strlen(username));
  esp_wifi_sta_wpa2_ent_set_password((uint8_t*)password, strlen(password));
  esp_wifi_sta_wpa2_ent_enable();
  WiFi.begin(ssid);
  WiFi.setSleep(false);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWi-Fi connected");
  Serial.print("Camera ready! Use 'http://");
  Serial.print(WiFi.localIP());
  Serial.println("' to connect");

  // Start web server
  startCameraServer();
}

void loop() {
  // All handled by web server task
  delay(10000);
}

