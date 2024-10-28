from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import numpy as np

def create_resonance_circuit(resonance_phase=4.40*np.pi, num_qubits=4):
    # Create registers and circuit
    qr = QuantumRegister(num_qubits, 'q')
    cr = ClassicalRegister(num_qubits, 'c')
    qc = QuantumCircuit(qr, cr)

    # Create superposition
    qc.h(qr[0])

    # Apply controlled phase rotations
    for i in range(num_qubits-1):
        qc.cp(resonance_phase/num_qubits, qr[i], qr[i+1])
        qc.cx(qr[i], qr[i+1])

    # Add measurement
    qc.measure(qr, cr)
    
    return qc

def simulate_circuit(qc, shots=1000):
    from qiskit import Aer, execute
    
    # Use the Aer simulator
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=shots)
    result = job.result()
    counts = result.get_counts(qc)
    
    # Calculate fidelity
    total_counts = sum(counts.values())
    entanglement_fidelity = max(counts.values()) / total_counts
    
    return counts, entanglement_fidelity
