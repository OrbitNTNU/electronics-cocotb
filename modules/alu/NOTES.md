# Delays
Some ALU functions have an extended time delay (in clock cycles)
in order to ensure proper output values:
(These time values are *guarantees* of proper values based on
simulations)

- Add: 2 cycles
- Add w. carry: 3 cycles
- Sub: 2 cycles
- Sub w. zero: 3 cycles
