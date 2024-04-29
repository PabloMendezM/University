import qiskit
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import QasmSimulator
from qiskit.quantum_info import Pauli
from qiskit.visualization import array_to_latex, plot_histogram
# Imports needed for simulating noisy quantum computation
from qiskit import transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Kraus, SuperOp
from qiskit_aer.noise import (NoiseModel, QuantumError)
from qiskit.circuit import ParameterVector
from qiskit.quantum_info import SparsePauliOp
import matplotlib.pyplot as plt

circuit=QuantumCircuit(3,3)
circuit.rz(np.pi/2,0)
circuit.cx(0,1)
circuit.cx(1,2)
circuit.rz(np.pi/2,1)

#the measurements
circuit.measure(0,0)
circuit.measure(1,1)
circuit.measure(2,2)

#display(circuit.draw('mpl'))
#only in IDLE

#Implementation of the error
p = 0.1
error_1 = [(Pauli('I'), (1-3/4*p)), (Pauli('X'), p/4), (Pauli('Y'), p/4), (Pauli('Z'), p/4)]

# Create an empty noise model
noise_model = NoiseModel()

# Add bit flip error to H, X, and R_Z gates
noise_model.add_all_qubit_quantum_error(error_1, ['rz'])

# Create noisy simulator backend
sim_noise = AerSimulator(noise_model=noise_model)

# Transpile circuit for noisy basis gates
circuit_with_noise = transpile(circuit, sim_noise)

# Run and get counts
result = (sim_noise.run(circuit_with_noise)).result()
counts = result.get_counts()

# Plot noisy output
plot_histogram(counts)
plt.savefig('results.pdf')
