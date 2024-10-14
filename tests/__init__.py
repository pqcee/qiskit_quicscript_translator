# SPDX-FileCopyrightText: 2024-present pQCee <pQCee.com>
#
# SPDX-License-Identifier: MIT
from qiskit_quicscript_translator import get_quic_circuit_string, get_quic_circuit_file_string
import qiskit

def test_h():
    qiskit_circuit = qiskit.QuantumCircuit(2)
    qiskit_circuit.h(0)
    assert get_quic_circuit_string(qiskit_circuit) == "H"