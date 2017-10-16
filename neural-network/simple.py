from numpy import exp, array, random, dot
#输入
ts_inputs = array([[0, 0, 0], [0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
#输出
ts_outputs = array([[0, 0, 0, 1, 1]]).T

unk_input = array([1, 0, 0])

# initialize synapse_weights
random.seed(1)
sy_weights = 2 * random.random((3, 1)) - 1

# output without untrained neuron
# print(1 / (1 + exp(-(dot(unk_input, sy_weights)))))
for i in range(10000):
    output = 1 / (1 + exp(-(dot(ts_inputs, sy_weights)))) # Calculate the value for the each of the examples
    sy_weights += dot(ts_inputs.T, (ts_outputs - output) * output * (1 - output)) # Run the adjustments

# Weights after training
# print(sy_weights)
print(1 / (1 + exp(-(dot(unk_input, sy_weights)))))