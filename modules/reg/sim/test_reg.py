import random
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue

@cocotb.test()
async def test_reg(dut):
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())  # Start the clock
    reg_check = 255
    dut.load = dut.enable = 0

    dut.rst = 1
    await Timer(10, units="us")
    dut.rst = 0

    dut.load = 1
    dut.reg_in = reg_check
    await Timer(10, units="us")
    
    dut.load = 0
    dut.enable = 1
    await Timer(10, units="us")
    await RisingEdge(dut.clk)
    print(dut.reg_out.value.binstr)
    assert dut.reg_out.value == reg_check, "No output match!"
