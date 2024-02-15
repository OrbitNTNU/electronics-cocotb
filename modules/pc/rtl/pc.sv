module pc #(
    parameter WIDTH = 8
) (
    input wire clk, rst, inc,
    output logic [WIDTH-1:0] out
);

reg[(WIDTH/2)-1:0] pc;

always_ff @(posedge clk, posedge rst) begin
    if (rst) begin
       pc <= 3'b0;
    end else if (inc) begin
       pc <= pc + 1;
    end
end

assign out = pc;

//Dump waves
initial begin
    $dumpfile("pc.vcd");
    $dumpvars(1, pc);
end

endmodule
