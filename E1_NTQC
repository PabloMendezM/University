import qiskit
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import StatevectorSimulator, QasmSimulator
from qiskit.visualization import array_to_latex, plot_histogram

circuit=QuantumCircuit(3,3)
circuit.h(1)
circuit.cx(1,2)
circuit.cx(0,1)
circuit.h(0)


#Simulation-like to obtain the state vector
simulator = StatevectorSimulator()
job = simulator.run(circuit)
result = job.result()
statevector = result.get_statevector()
display(statevector.draw(output='latex'))


circuit.measure(0, 0)
circuit.measure(1, 1)
circuit.measure(2, 2)


#Simulation of a measurement
simulator = QasmSimulator()
job = simulator.run(circuit,shots=100000)
result = job.result()
counts = result.get_counts()
display(plot_histogram(counts))


