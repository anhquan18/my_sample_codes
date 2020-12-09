right_kick_noise = [(2.500, 0.100), (2.800, 0.300), (1.950, 0.050), (1.950, 0.060), (1.970, 0.600), (2.000, 0.080), (1.930, 0.110), (2.100, 0.0120), (1.820, 0.200),
                    (2.250, 0.140), (2.170, 0.130), (2.050, 0.500), (1.900, 0.400), (1.600, 0.440), (1.900, 0.070), (1.740, 0.070), (2.300, 0.0070), (2.250, 0.060),
                    (1.410, 0.510), (2.220, 0.140), (2.230, 0.070), (2.170, 0.070), (2.310, 0.070), (2.210, 0.090), (2.160, 0.060), (1.980, 0.0050), (1.540, 0.340), 
                    (1.940, 0.140), (2.040, 0.060), (1.620, 0.070), (1.640, 0.200), (2.330, 0.140), (1.660, 0.200), (2.230, 0.060), (2.435, 0.0070), (2.260, 0.080),
                    (2.140, 0.300), (1.645, 0.040), (1.775, 0.080), (2.250, 0.040), (2.002, 0.050), (1.715, 0.060), (2.070, 0.190), (2.140, 0.0050), (2.050, 0.090),
                    (2.010, 0.060), (2.140, 0.130), (2.560, 0.040), (2.130, 0.030), (2.230, 0.120)   ] #メートル

x_distance_list = [r[0] for r in right_kick_noise]
y_distance_list = [r[1] for r in right_kick_noise]

mean_x = sum(x_distance_list)/len(right_kick_noise)
mean_y = sum(y_distance_list)/len(right_kick_noise)

deviation2_list_x = [(d - mean_x)**2 for d in x_distance_list]
deviation2_list_y = [(d - mean_y)**2 for d in y_distance_list]

variance_x = sum(deviation2_list_x)/ len(deviation2_list_x)
variance_y = sum(deviation2_list_y)/ len(deviation2_list_y)

print("mean distance x:", round(mean_x, 3))
print("mean distance y:", round(mean_y, 3))

print("variance_x:", round(variance_x, 3))
print("variance_y:", round(variance_y, 3))
