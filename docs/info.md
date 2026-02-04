<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This is a 4-bit digital counter that counts from 0 to 15 and then wraps around to 0.

The counter has an enable input on ui[0]. When enabled (ui[0]=1), the counter increments by 1 on each clock cycle. When disabled (ui[0]=0), the counter holds its current value.

The 4-bit count value is output on uo[0:3], where uo[0] is the least significant bit and uo[3] is the most significant bit.

## How to test

1. Reset the design by asserting rst_n low
2. Set ui[0] to 1 to enable the counter
3. Observe the count value incrementing on uo[0:3] with each clock cycle
4. The counter will count from 0 to 15 (0x0 to 0xF) and then wrap back to 0
5. Set ui[0] to 0 to disable counting - the counter will hold its current value

## External hardware

No external hardware required. You can observe the counter outputs directly with LEDs or a logic analyzer.
