import random
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue

@cocotb.test()
async def test_mem(dut):
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())  # Start the clock

    dut.rst = 1 # Reset 
    await Timer(10, units="us")
    dut.rst = 0

    for i in range(0, 16):
        dut.bus = i
        dut.load = 1
        await Timer(20, units="us")
        dut.load = 0
        await Timer(10, units="us")
        await RisingEdge(dut.clk)
        # print(dut.out.value.binstr)
        print(dut.out.value)
        assert dut.out.value == i, "Mismatch in subtraction"
