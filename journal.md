Title: 75% keyboard
Slack Username: bug
Description: A custom 75% keyboard with a clear case, rotary encoder, and backlighting.
Created at: 6/29/2025

# July 25th

I originally just started searching for what kind of keyboard I wanted, and what i needed. 
I was completely new to building keyboards, so i assembled a rough BOM. I decided to go with 75% since it wouldn't be overwhelming,
but still include everything that I needed. I went with a raspberry pico since I was somewhat familiar with it, 
and decided to include a knob for volume and backlighting. 
I also decided to make the case of the keyboard clear, to display the PCB. 
Not gonna lie, this day mainly consisted of scrolling pinterest and reddit to get a vague idea of what I was doing. 
I included one of my inspiration pictures below a design I liked

<img width="726" height="572" alt="Image" src="https://github.com/user-attachments/assets/0a9f7c8d-1f64-4fcd-93ce-3fd98704bf43" />

Time spent: 1h

#July 26th

Created the original schematic for the keyboard. I went back and forth with including the LEDs due to power usage, 
but i included them in the final design. Basic math tells me that it won't explode, chatGPT says it will. Oh well.
The second schematic I've made. I somehow managed to mess up the amount of keys around 5 times, which slowed the 
process quite a bit. 

<img width="1514" height="1216" alt="Image" src="https://github.com/user-attachments/assets/ecafe855-e85c-45ba-87ba-283ae8d7da1b" />

Time spent: 3h

# July 27th

I somehow managed to do the entire PCB setup and routing in one day. Unfortunately, the footprint for the pico I was using was inaccurate and didn't actually support through-hole soldering, so I had to go back and fix it after finishing the whole thing. I was trying to be careful about the layout, considering the case might expose how bad it looked if it was a train wreck. I included a picture of when i was still moving the footprints.

<img width="1680" height="1175" alt="Image" src="https://github.com/user-attachments/assets/3b0856bb-89e9-4cc6-80e4-23c2d755e1a4" />

Time spent: 6h

# July 28th

Now that all that was left was CAD and firmware, I was back in my comfort zone and was able to get through the case relatively fast. It did take a nit longer than I intended since Kicad wasn't cooperating with me, and I had to add all the switches and keycaps manually during cad. Thank god for the pattern tool. Firmware only took about 20 minutes, I found the base kmk code and just adjusted it. 

<img width="1763" height="1170" alt="Image" src="https://github.com/user-attachments/assets/052a3f02-bf1a-4378-9482-3c0b5cc7373e" />




