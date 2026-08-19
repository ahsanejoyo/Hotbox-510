# Swapbox-510

<!-- Main Hero Image -->
<p align="center">
  <img src="https://github.com/user-attachments/assets/b1e31542-3be3-44ab-8a25-183d2569582b" alt="Swapbox-510 Physical Build" width="650" />
</p>

<!-- 2-Column Side-by-Side Table -->
<table align="center">
  <tr>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/f1004bc5-6793-46dc-8934-4f2187bfbaaa" alt="CAD Design" width="100%" />
      <br><sub><b>3D CAD Enclosure Model</b></sub>
    </td>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/acd06389-a84e-4d46-8d64-c3e5a114f6b8" alt="OLED Display Hardware" width="100%" />
      <br><sub><b>Assembled Model</b></sub>
    </td>
  </tr>
</table>

The Swapbox-510 is an embedded variable voltage controller powered by the Raspberry Pi Pico (RP2040). It features a custom user interface driven by a 128x64 OLED display and buttons, delivering modular power regulation over a high-current, 510-threaded magnetic interface. 

The system utilizes Pulse-Width Modulation (PWM) through a power MOSFET driver circuit to deliver precise, regulated energy bursts to modular attachments—including micro-soldering tips, high-intensity LED light tools, and custom resistive heating elements.

| Parameter | Specification |
| :--- | :--- |
| **Microcontroller** | Raspberry Pi Pico (RP2040 @ 133MHz w/ 8MB FLASH) |
| **Display** | 0.96" SSD1306 OLED (128x64, I2C Interface) |
| **Power Switch** | Logic-Level N-Channel MOSFET driven by PWM |
| **Input Voltage** | 1.8V – 5.0V Li-Ion / USB Power |
| **Connector Standard** | 510-Threaded Magnetic Connector |
| **Firmware Language** | CircuitPython |
