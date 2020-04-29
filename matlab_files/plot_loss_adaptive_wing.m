Epochs = 1:38;

Losses = [1639 39 9 19 12 1.57 2.04 1.66 1.26 1 24 1.22 5 1.64 1.64 2.06 1.33 1.18 1.74 1.79 2.72 1.82 32 9 12 12 9.28 3.06 1.67 1.77 14 9 22 13 2.03 6.85 1.6 1.34];

figure;
plot(Epochs, Losses);
ylim([0 200]);

title('Total Adaptive Wing Loss per Epoch');
ylabel('Total Loss');
xlabel('Epoch');
grid on;