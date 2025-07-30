# Clear as Day

Clear as day is a custom, open source 75% keyboard with a rotary encoder and underlighting. 

<img width="1325" height="744" alt="Image" src="https://github.com/user-attachments/assets/01590692-02aa-4581-b610-edc6e1d0b6ae" />

# PCB

The schematic consists of a basic keyboard matrix, which includes a rotary encoder, and also sk6812minis all wired toa raspberry pico. 
<img width="1514" height="1216" alt="Image" src="https://github.com/user-attachments/assets/cb5a9266-c11c-4a6d-9d44-32157fe84fff" />

The raspberry pico is placed on the right side edge to make it easy to plug in and for it to blend nicely in a case

<img width="1712" height="831" alt="Image" src="https://github.com/user-attachments/assets/6b2e637b-ac9c-41eb-b915-5e24fdd8da05" />

# Firmware

I used KMK firmware to program the keyboard as well as the LEDs. 

# CAD

The case consists of 2 parts, and the pcb rests on a frame built on the bottom. I avoided the use of screws in the design because I wanted to make it clear, and I though including screws might take away how clean the design might look. Currently, I plan to use hotglue/a 3d pen to keep the case together. 

<img width="1877" height="1132" alt="Image" src="https://github.com/user-attachments/assets/33def16f-1549-45a5-b809-2dcc2a1bbca6" />

<img width="1325" height="744" alt="Image" src="https://github.com/user-attachments/assets/01590692-02aa-4581-b610-edc6e1d0b6ae" />

# BOM

| # | Item | Amount | Link | Cost |
|---|------|--------|------|-------------|
| 1 | Raspberry pico | 1 | [aliexpress](https://www.aliexpress.us/item/3256803521775546.html?spm=a2g0o.productlist.main.22.6478lNgJlNgJEx&algo_pvid=eb010e16-b8d5-433e-b930-93ddb07e16ff&algo_exp_id=eb010e16-b8d5-433e-b930-93ddb07e16ff-21&pdp_ext_f=%7B%22order%22%3A%22178%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21USD%216.18%210.99%21%21%2144.08%217.04%21%402103245417538992995887740e4f41%2112000034536362461%21sea%21US%210%21ABX&curPageLogUid=blshBSuqtFpH&utparam-url=scene%3Asearch%7Cquery_from%3A) | 1 usd
| 2 | 1n4148 diodes | 83 | [Amazon](https://www.amazon.com/100pcs-High-Speed-Switching-DO-204AH-Package/dp/B081JKJM6N/ref=sr_1_10?crid=1HC0FF60FQC6V&dib=eyJ2IjoiMSJ9.8C1ebcszlPAbe4ldgX4jaM9nlgUAEZPfJqUMbjw_Zdo3jiIInZo87Hw9RQLWkePHKBARSxjQtoO8uGubd_VJ1mYoJtvN5hdTdvzuUxTuOJops0Via8YoDJjmkyxSQkFo9_Hi7yoCu73wjmn946A8soaoz5Ob1P2tAcWaZHEzCKSBqiEjrTCESDe0pqKqnBkI23rPIbMjMLc63Ia-rzfjxKeO4fNg4qbYUfYIWbYIkTM.WgoYdmka-GUoqAGNLC_Uoa-XBuPIClIMXHSbIhYjF6k&dib_tag=se&keywords=1n4148+diodes+100+pc&qid=1753899635&sprefix=1n4148+diodes+100+pc%2Caps%2C125&sr=8-10) | 3.68 USD |
| 3 | Cherry MX switches | 83 | [Amazon](https://www.amazon.com/GLORIOUS-Gateron-Mechanical-Keyboard-Switches/dp/B07CVQ7ZRL/ref=sr_1_4_sspa?crid=10XHCKI24AHF1&keywords=clear%2Bred%2Bcherry%2Bmx%2Bswitches%2B100pc&qid=1753900124&sprefix=clear%2Bred%2Bcherry%2Bmx%2Bswitches%2B100pc%2Caps%2C106&sr=8-4-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&th=1) | 35 USD |
| 4 | ec11 rotary encoder | 1 | [AliExpress](https://www.aliexpress.us/item/3256807457768762.html?spm=a2g0o.productlist.main.3.417bjQLojQLoFM&algo_pvid=5f74a285-dd91-4134-b04f-86eff7bfe1f1&algo_exp_id=5f74a285-dd91-4134-b04f-86eff7bfe1f1-2&pdp_ext_f=%7B%22order%22%3A%22509%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21USD%212.12%210.99%21%21%212.12%210.99%21%402103273e17539009433327470eab0f%2112000041630839428%21sea%21US%210%21ABX&curPageLogUid=wlRKuFiINxac&utparam-url=scene%3Asearch%7Cquery_from%3A) | 1 USD |
| 5 | Stabilizers | 4 of 2u, 1 6.25u | [AliExpress](https://www.aliexpress.us/item/3256803026138061.html?spm=a2g0o.productlist.main.6.5f4bl8Oml8Ompe&algo_pvid=0d6ef425-5bf0-474d-a050-13df98aca940&algo_exp_id=0d6ef425-5bf0-474d-a050-13df98aca940-5&pdp_ext_f=%7B%22order%22%3A%2247%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21USD%2123.10%214.16%21%21%2123.10%214.16%21%402101c72a17539012644845638e9800%2112000036718262540%21sea%21US%210%21ABX&curPageLogUid=cqGHHmNfo124&utparam-url=scene%3Asearch%7Cquery_from%3A) | 4.16 USD |
| 6 | SK6812 mini LEDS | 38 | [Amazon](https://www.amazon.com/100pcs-WS2812B-WS2812-Individually-Addressable/dp/B09X1K1NMT/ref=sr_1_23?crid=DMPZ1YVDZRIA&dib=eyJ2IjoiMSJ9.wgR4tgvU_wqke989tL1lWFADbdpZP0S6KwMg6vvgEUV1T_wJPGbmOjxaFa_ZfuVNXvwUUN_S5bUk5ai7bqh5rozRhZ8HtkwuSRSb9YluuFAD3cb_EdOuGAzl_WConqrSCEO_kWmjRQrrXBiCbF5o95xsjtQvaYWRTjnZvGCWG5Q4HmALSPQt-sC18PSJ-sKxYbzMb6gLwb0ELw8vOOiBw7knYvHeuhy20SytMA9MkiQuI2eBuv0ndo3xHH7-LxpJszkpAl3mKpZx8c6YtR3yiDqc3pNA3yjIrs6vUZmV6-A.o54e5xVs7eDCx2u05ezCwSiXbvmN61aKqktlkiNEdaw&dib_tag=se&keywords=sk6812+mini-e+leds+50+pc&qid=1753901730&sprefix=sk6812+mini-e+leds+50+pc%2Caps%2C110&sr=8-23) | 8.50 USD |
| 7 | Keycaps | 83 | [Amazon](https://www.amazon.com/OHY-Through-Keycaps-Mechanical-Keyboards/dp/B0F1CR1Q2T/ref=sr_1_26?crid=1SQ8HX2ZY26P6&dib=eyJ2IjoiMSJ9.ErL3CYsqRj2o1Vzo5t0v-Cw6ytb7Whop7YJup4xPkkAPg-AZGXlnHSBiU3csK4GP5eJSychynDTXCBz6fH83o4zBf11hgBfe4CjMMg59yxTZejJ_CKzQalQY4Syohy2--pfvfsorrXG1XhHPt1MjlWKm45tgc0LR3KWr98kRsApmQzCUjwzcxOiDGTtwpYYu7ahYog8krL2WOpsudRBMIqJFdSMo6NuVqEguNjt-VrxV9HxMlcKWn_RxqjJ5kbpuA9Sd599GHszGTmsGyX8w7_UbPZ7z2wYyhtFSnADqnYM.Acx-Q1RIv1-P2nWTFBNTOSC5HDBR-XDIjx0R2-EHqmo&dib_tag=se&keywords=blue%2Bkeycaps&qid=1753902254&s=electronics&sprefix=blue%2Bkeycaps%2Celectronics%2C143&sr=1-26&th=1) | 25.99 USD |
| 8 | Case | bottom and top | Self made| |
| 9 | PCB | 1 | JBL PCB | 23 USD |
| 10 | Rotary encoder knob | 1 | 3D printed | |
|Total price: (including tax+shipping)|  120.67 USD | Total price (No tax): | 102.33 | 
