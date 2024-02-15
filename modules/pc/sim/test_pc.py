import random
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue

# input wire clk, rst, inc,
# output logic [WIDTH-1:0] out

@cocotb.test()
async def test_pc(dut):
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())  # Start the clock

    dut.rst = 1
    await Timer(10, units="us")
    dut.rst = 0
    assert dut.out.value == 0, "PC mismatch"
    for i in range(1, 16):
        dut.inc = 1
        await Timer(10, units="us")
        await RisingEdge(dut.clk)
        print(dut.out.value.binstr)
        assert dut.out.value == i, "No output match!"
