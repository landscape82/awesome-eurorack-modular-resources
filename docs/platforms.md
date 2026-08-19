# Platforms

CPU/platform families currently referenced in `data/modules.yaml`. This list is
descriptive, not exhaustive — add a new platform here when you add the first
module that uses it.

| Platform | Notes |
| --- | --- |
| STM32 | Most common MCU family in Eurorack firmware (Mutable Instruments, 4ms). |
| Teensy | Popular for hobbyist/community firmware (Ornament & Crime, Radio Music). |
| RP2040 | Used by MicroPython-based platforms (EuroPi). |
| ESP32 | Used where Wi-Fi/BLE connectivity is relevant. |
| FPGA | Used for platforms doing DSP in gateware rather than firmware (Tiliqua). |

See `data/tags.yaml` for the `type` taxonomy and `docs/schema.md` for the full
metadata schema.
