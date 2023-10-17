import numpy as np
from qiskit import QuantumCircuit

# Define the matrices for U and CX gates
U_gate = np.array([[1, 0], [0, np.exp(1j * np.pi/2)]])  # U gate (π/2 phase gate)
CX_gate = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])  # CX gate

# Compute the CCX gate by multiplying the matrices
CCX_gate = np.kron(CX_gate, np.kron(U_gate, np.kron(CX_gate, np.kron(U_gate, CX_gate))))

# Print the resulting CCX gate matrix
print("Resulting CCX gate matrix:")
print(CCX_gate)



# Create a quantum circuit with 3 qubits
qc = QuantumCircuit(3)

# Apply the CCX (Toffoli) gate using CX and U gates
qc.cx(0, 2)  # CX gate (controlled-X) with qubit 0 as control and qubit 2 as target
qc.u(0, 0, np.pi, 2)  # U gate (π phase gate) on qubit 2
qc.cx(1, 2)  # CX gate with qubit 1 as control and qubit 2 as target
qc.u(0, 0, np.pi, 2)  # U gate on qubit 2
qc.cx(0, 2)  # CX gate with qubit 0 as control and qubit 2 as target
qc.u(0, 0, np.pi, 2)  # U gate on qubit 2

# Print the circuit
print(qc)
