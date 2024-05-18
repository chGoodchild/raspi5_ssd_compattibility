| Test name         | Reliability Recommendation | Datarate Read | Datarate Write | Cooling                                                    | Display      | Peripherals                                      | SSD Type                                              | SSD Connection                                                     | Power supply                                             |
|-------------------|----------------------------|----------------|----------------|------------------------------------------------------------|--------------|-------------------------------------------------|-------------------------------------------------------|---------------------------------------------------------------------|-----------------------------------------------------------|
| intenso_ssd       | Good                       |                |                | [Geekworm Raspberry Pi 5 Case Aluminium Passive Cooling (P122-C)](https://www.amazon.de/dp/B0CN9D62QS?ref_=cm_sw_r_apann_dp_FDH5S1R5MJXP1M30CEQ2&starsLeft=1) | HDMI cable   | Keyboard & mouse with USB hub and without external power | [Intenso 2.5 inch 2TB performance SSD, SATAIII](https://amzn.eu/d/fKQrdeG) | [Geekworm x1100 2.5 inch SATA HDD/SSD shield for raspberry pi](https://geekworm.com/products/x1100) | [Raspberry Pi Power Adapter Model 27W, Output 5.1 V, 5A (25.5 W)](https://amzn.eu/d/cXItfaE) |
| m2_sata_ssd_usb   | Terrible                   |                |                | [Geekworm Raspberry Pi 5 Case Aluminium Passive Cooling (P122-C)](https://www.amazon.de/dp/B0CN9D62QS?ref_=cm_sw_r_apann_dp_FDH5S1R5MJXP1M30CEQ2&starsLeft=1) | HDMI cable   | Keyboard & mouse with USB hub and without external power | [Lexar NM610PRO 2TB SSD, M.2 2280 PCIe Gen3x4 NVMe 1.4 Internal](https://amzn.eu/d/aVbfLyy) | [Beikell M.2 NVME Enclosure, USB 3.2 Gen 2 NVMe to USB Adapter](https://amzn.eu/d/6bk5P0S) | [Raspberry Pi Power Adapter Model 27W, Output 5.1 V, 5A (25.5 W)](https://amzn.eu/d/cXItfaE) |
| m2_sata_ssd_N04   | Good                       |                |                | [Geekworm Raspberry Pi 5 Case Aluminium Passive Cooling (P122-C)](https://www.amazon.de/dp/B0CN9D62QS?ref_=cm_sw_r_apann_dp_FDH5S1R5MJXP1M30CEQ2&starsLeft=1) | None / SSH   | None / SSH                                       | [Lexar NM610PRO 2TB SSD, M.2 2280 PCIe Gen3x4 NVMe 1.4 Internal](https://amzn.eu/d/aVbfLyy) | [GeeekPi N04 M.2 2280 NVMe SSD Shield for Raspberry Pi 5](https://amzn.eu/d/b2wVg35)             | [Raspberry Pi Power Adapter Model 27W, Output 5.1 V, 5A (25.5 W)](https://amzn.eu/d/cXItfaE) |
| m2_sata_ssd_X1001 |                            |                |                | None                                                       | None / SSH   | None / SSH                                       | [Lexar NM610PRO 2TB SSD, M.2 2280 PCIe Gen3x4 NVMe 1.4 Internal](https://amzn.eu/d/aVbfLyy) | [Mumuve X1001 PCIe M.2 NVMe Board](https://amzn.eu/d/h8xsdEp)                                        | [Raspberry Pi Power Adapter Model 27W, Output 5.1 V, 5A (25.5 W)](https://amzn.eu/d/cXItfaE) |


-----------------------------------------------------------

* Science experiment: raspiblitz reliability
https://github.com/chGoodchild/raspi5_ssd_compattibility/tree/main

* Scratch my own itch: streamlined hardware testing and posting to nostr?
https://github.com/chGoodchild/raspiFlasher

* Next steps: dockerized OpenWRT + OpenNDS or CoovaChilli + e-cash


Thoughts:
* I dropped the reticulum relay for the time being.
* Can IPV6 replace reticulum? 
IPV6 also supports overlay network properties: https://datatracker.ietf.org/doc/html/rfc4843
Maybe centralization is mitigated by Stateless Address Autoconfiguration: https://en.wikipedia.org/wiki/IPv6_address#Stateless_address_autoconfiguration_(SLAAC)

* Where does IPV6 sit on the privacy, centralization and security triangle?

