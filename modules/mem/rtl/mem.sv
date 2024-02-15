module mem #(
    parameter WIDTH = 8
) (
    input logic clk, rst,
    input logic load,
    input logic [WIDTH-1:0] bus,
    output logic [WIDTH-1:0] out
);

initial begin
	$readmemh("program.bin", ram);
end

reg[3:0] mar;
//Reg ram[0:15];
reg[7:0] ram[0:15];

always @(posedge clk, posedge rst) begin
	if (rst) begin
		mar <= 4'b0;
	end else if (load) begin
		mar <= bus[3:0];
	end

end

assign out = ram[mar];

//Dump waves
//initial begin
//    $dumpfile("mem.vcd");
//    $dumpvars(1, mem);
//end

endmodule

