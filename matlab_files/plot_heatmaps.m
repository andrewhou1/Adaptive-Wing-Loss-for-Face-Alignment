%heatmap = load('predicted_heatmaps_adaptive_wing_loss/HELEN_30427236_1_0.png.mat');
heatmap = load('predicted_heatmaps_adaptive_wing_loss/IBUG_image_004_1_0.png.mat');
heatmap = heatmap.predicted_heatmaps;
%img = imread('tmp_AFW_Flip/image/HELEN/HELEN_30427236_1_0.png');
img = imread('tmp_AFW_Flip/image/IBUG/IBUG_image_004_1_0.png');
figure;
imshow(img);
hold on;

predicted_landmarks = zeros(68, 2);
for i = 1:68
    a = heatmap(:, 4, :, :, i);
    a = reshape(a, [64 64]);
    maximum = max(max(a));
    [x, y] = find(a == maximum);
    predicted_landmarks(i, 1) = y;
    predicted_landmarks(i, 2) = x;
end

predicted_landmarks = predicted_landmarks*4;

scatter(predicted_landmarks(:, 1), predicted_landmarks(:, 2));

figure;
all_heatmaps = heatmap(:, 4, :, :, :);
all_heatmaps = reshape(all_heatmaps, [64 64 68]);
%sum_heatmap = sum(all_heatmaps, 3);
%sum_heatmap = sum_heatmap/max(max(sum_heatmap));
%sum_heatmap = imresize(sum_heatmap, [256 256]);
max_heatmap = max(all_heatmaps, [], 3);
max_heatmap = imresize(max_heatmap, [256, 256]);

imshow(max_heatmap);
