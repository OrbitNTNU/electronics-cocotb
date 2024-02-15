import random
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue

@cocotb.test()
async def add(dut):
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())  # Start the clock
    dut.rst = 1
    dut.add = dut.sub = dut.fi = 0
    dut.load_a = dut.load_b = dut.en_a = dut.en_b = 0
    await Timer(10, units="us")
    dut.rst = 0

    # Load A/B
    dut.load_a = dut.load_b = 1
    dut.a = dut.b = 2
    await Timer(10, units="us")
    dut.load_a = dut.load_b = 0

    # Execute ALU
    dut.add = 1
    dut.en_a = dut.en_b = 1
    await Timer(10, units="us")
    dut.en_a = dut.en_b = 0

    # Check output
    await Timer(20, units="us")
    await RisingEdge(dut.clk)
    print(dut.out.value.binstr)
    assert dut.out.value == 4, "Mismatch in addition"

@cocotb.test()
async def add_carry(dut):
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())  # Start the clock
    dut.add = dut.sub = dut.fi = 0
    dut.load_a = dut.load_b = dut.en_a = dut.en_b = 0

    dut.rst = 1
    await Timer(10, units="us")
    dut.rst = 0

    # Load A/B
    dut.load_a = dut.load_b = 1
    dut.a = 255
    dut.b = 1
    await Timer(10, units="us")
    dut.load_a = dut.load_b = 0

    # Execute ALU
    dut.fi = 1;
    dut.add = 1
    dut.en_a = dut.en_b = 1
    await Timer(10, units="us")
    dut.en_a = dut.en_b = 0

    # Check output
    await Timer(30, units="us")
    await RisingEdge(dut.clk)
    print(dut.out.value.binstr)
    assert dut.carry.value == 1, "No carry flag"


@cocotb.test()
async def sub(dut):
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())  # Start the clock
    dut.rst = 1
    dut.add = dut.sub = dut.fi = 0
    dut.load_a = dut.load_b = 0
    await Timer(10, units="us")
    dut.rst = 0

    # Load A/B
    dut.load_a = dut.load_b = 1
    dut.a = 6
    dut.b = 2
    await Timer(10, units="us")
    dut.load_a = dut.load_b = 0

    # Execute ALU
    dut.en_a = dut.en_b = 1
    dut.sub = 1
    await Timer(10, units="us")
    dut.en_a = dut.en_b = 0

    # Check output
    await Timer(20, units="us")
    await RisingEdge(dut.clk)
    print(dut.out.value.binstr)
    assert dut.out.value == 4, "Mismatch in subtraction"

@cocotb.test()
async def sub_zero(dut):
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())  # Start the clock
    dut.rst = 1
    dut.add = dut.sub = dut.fi = 0
    dut.load_a = dut.load_b = 0
    await Timer(10, units="us")
    dut.rst = 0

    # Load A/B
    dut.load_a = dut.load_b = 1
    dut.a = 2
    dut.b = 2
    await Timer(10, units="us")
    dut.load_a = dut.load_b = 0

    # Execute ALU
    dut.fi = 1
    dut.sub = 1
    dut.en_a = dut.en_b = 1
    await Timer(10, units="us")
    dut.en_a = dut.en_b = 0

    # Check output
    await Timer(30, units="us")
    await RisingEdge(dut.clk)
    print(dut.out.value.binstr)
    assert dut.zero.value == 1, "No zero flag"

