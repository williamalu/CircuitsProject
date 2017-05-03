clear;
S1 = tdfread('postlab9.txt');
S2 = tdfread('postlab9_mid.txt');
S3 = tdfread('postlab9_Vdd.txt');

time1 = S1.time;
Vout1 = S1.V0x28v0x29;
Vin1  = S1.V0x28v10x29;

time2 = S2.time;
Vout2 = S2.V0x28v0x29;
Vin2  = S2.V0x28v10x29;

time3 = S3.time;
Vout3 = S3.V0x28v0x29;
Vin3  = S3.V0x28v10x29;

figure;
hold on;
plot(time1, Vout1);
plot(time1, Vin1);
xlabel('Time (s)');
ylabel('Voltage (V)');
legend('V_{out}', 'V_{in}');
text(9e-6, 0.57, 'RC = 6.848e-7');
title('Circuit Step Response, Steps near 0V');
% 5RC = 3.424e-6

figure;
hold on;
plot(time2, Vout2);
plot(time2, Vin2);
xlabel('Time (s)');
ylabel('Voltage (V)');
legend('V_{out}', 'V_{in}');
text(9e-6, 2.517, 'RC = 3.176e-7');
title('Circuit Step Response, Steps near 2.5V');
% 5RC = 1.588e-6

figure;
hold on;
plot(time3, Vout3);
plot(time3, Vin3);
xlabel('Time (s)');
ylabel('Voltage (V)');
legend('V_{out}', 'V_{in}');
text(9e-6, 4.533, 'RC = 4.324e-7');
title('Circuit Step Response, Steps near V_{dd}');
% 5RC = 2.162e-6