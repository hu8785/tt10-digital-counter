/*
 * Copyright (c) 2024 Mislamihf Hu8785
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_Akanksha_hu8785_counter (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

   // 4-bit counter
  reg [3:0] count;
  
  // Enable signal from ui_in[0]
  wire enable;
  assign enable = ui_in[0];
  
  // Counter logic
  always @(posedge clk) begin
    if (!rst_n) begin
      count <= 4'b0000;
    end else begin
      if (enable) begin
        count <= count + 1;
      end
      // If enable is 0, count holds its value
    end
  end
  
  // Output assignments
  assign uo_out[3:0] = count;    // Count outputs on uo[0:3]
  assign uo_out[7:4] = 4'b0000;  // Unused outputs

  // Output assignments
  assign uo_out[3:0] = count;    // Count outputs on uo[0:3]
  assign uo_out[7:4] = 4'b0000;  // Unused outputs
  
  // All IOs configured as inputs (not used)
  assign uio_out = 8'b00000000;
  assign uio_oe  = 8'b00000000;

  // Avoid unused signal warnings
  wire _unused = &{ena, ui_in[7:1], uio_in, 1'b0};

endmodule

