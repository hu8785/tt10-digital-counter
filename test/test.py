# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_counter(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test counter without enable")
    dut.ui_in.value = 0  # enable = 0
    await ClockCycles(dut.clk, 10)
    assert dut.uo_out.value == 0, "Counter should not increment when enable is 0"

    dut._log.info("Test counter with enable")
    dut.ui_in.value = 1  # enable = 1
    
    # Test counting from 0 to 15
    for i in range(16):
        await ClockCycles(dut.clk, 1)
        expected = (i + 1) & 0xF
        actual = int(dut.uo_out.value) & 0xF
        dut._log.info(f"Clock cycle {i+1}: Expected {expected}, Got {actual}")
        assert actual == expected, f"Counter mismatch: expected {expected}, got {actual}"

    # Test wrap around
    await ClockCycles(dut.clk, 1)
    actual = int(dut.uo_out.value) & 0xF
    dut._log.info(f"After wrap: Expected 0, Got {actual}")
    assert actual == 0, f"Counter should wrap to 0, got {actual}"

    dut._log.info("Test counter disable")
    current_value = int(dut.uo_out.value) & 0xF
    dut.ui_in.value = 0  # disable counter
    await ClockCycles(dut.clk, 10)
    final_value = int(dut.uo_out.value) & 0xF
    assert current_value == final_value, "Counter should not change when disabled"
