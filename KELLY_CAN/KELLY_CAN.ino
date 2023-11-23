#include <ESP32CAN.h>
#include <CAN_config.h>

CAN_device_t CAN_cfg;               // CAN Config
unsigned long previousMillis = 0;   // will store last time a CAN Message was send
const int interval = 1000;          // interval at which send CAN Messages (milliseconds)
const int rx_queue_size = 10;       // Receive Queue size

void setup() {
  Serial.begin(115200);
  CAN_cfg.speed = CAN_SPEED_250KBPS;
  CAN_cfg.tx_pin_id = GPIO_NUM_5;
  CAN_cfg.rx_pin_id = GPIO_NUM_4;
  CAN_cfg.rx_queue = xQueueCreate(rx_queue_size, sizeof(CAN_frame_t));
  // Init CAN Module
  ESP32Can.CANInit();
}

void loop() {
  CAN_frame_t rx_frame;

  
  if (xQueueReceive(CAN_cfg.rx_queue, &rx_frame, 3 * portTICK_PERIOD_MS) == pdTRUE) {

    if (rx_frame.FIR.B.RTR == CAN_RTR) {
      //printf(" RTR from 0x%08X, DLC %d\r\n", rx_frame.MsgID,  rx_frame.FIR.B.DLC);
    }
    else {
     // printf(" from 0x%08X, DLC %d, Data ", rx_frame.MsgID,  rx_frame.FIR.B.DLC);
    if (rx_frame.MsgID == 0x0CF11E05) {
        //printf("\n");
        int speed1 = ((rx_frame.data.u8[1] * 256) + rx_frame.data.u8[0]);
        int current = (((rx_frame.data.u8[3] * 256) + rx_frame.data.u8[2]) / 10);
        int voltage = (((rx_frame.data.u8[5] * 256) + rx_frame.data.u8[4]) / 10);
        //Serial.print("speed =");
        Serial.println(speed1);
        Serial.println(current);
        Serial.println(voltage);





        
       
       
    }
    }}  }
