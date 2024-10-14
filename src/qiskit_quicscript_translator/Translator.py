from numpy import pi
from qiskit import QuantumCircuit
from qiskit_quicscript_translator.QuiCGate import QuiCGate

__all__ = ["get_quic_circuit_string", "get_quic_circuit_file_string"]

def transpile_circuit(circuit: QuantumCircuit) -> QuantumCircuit:
    r"""
    Transpile a circuit.

    Args:
        circuit: The circuit to transpile.

    Returns:
        The transpiled circuit.
    """
    # delete measure gates
    circuit = circuit.copy()
    # TODO hard problem to add back the measurements at
    # the right time and the right qubits
    circuit.data = [
        gate for gate in circuit.data
        if gate.operation.name != "measure"]
    # get the pass manager no optimisations
    # pass_manager = generate_preset_pass_manager(0, self)
    # if self._approximation_pass_manager is not None:
    #     pass_manager.pre_layout = self._approximation_pass_manager
    # circuit = pass_manager.run(circuit)
    return circuit


def get_quic_circuit_file_string(circuit: QuantumCircuit) -> str:
    """Convert a circuit to a string for filebased quic format

    :param circuit: QuantumCircuit
    :returns: formatted string
    :rtype: [str]
    """
    circuit = transpile_circuit(circuit)

    # compute the maximum num qubits
    circuit_num_qubits = max(
        [
            circuit.find_bit(qubit).index
            for gate in circuit.data
            for qubit in gate.qubits
        ] + [0]) + 1
    circuit_string: str = ""
    circuit_string_list: list[str] = []

    for gate in circuit.data:
        # get gate name
        gate_name = gate.operation.name
        # get the number of qubits
        gate_num_qubits = gate.operation.num_qubits
        # get gate qubits
        gate_qubits = gate.qubits
        # string to add
        # initialise with identity gates
        gate_string_list = ["I" for _ in range(circuit_num_qubits)]

        if gate_name == "barrier":
            continue

        quic_gate = QuiCGate.from_qiskit_name(gate_name)

        # get the quic representation
        quic_representation = quic_gate.get_quic_representation()
        # modify the gate string list
        for qubit_no in range(gate_num_qubits):
            index = circuit.find_bit(gate_qubits[qubit_no]).index
            gate_string_list[index] = quic_representation[qubit_no]
        # join the list to get the gate string
        gate_string = "".join(gate_string_list)

        # For File Based
        params = None
        # Extra processing for Ry, Rx, Rz and U gate
        if (gate_name in {"cu", "u", "ry", "cp"}):
            params = gate.params
            if (gate_name == "ry"):
                params.extend([0, 0])
            elif (gate_name == "cp"):
                params = [0, 0, params[0]]
            elif (len(params) == 4):
                params.pop()

        # add parameter
        if (params is not None):
            ustring = "{U "+f"{params[0]} {params[1]} {params[2]}" + "}\n"
            gate_string = ustring + gate_string

        # add the gate string to the circuit string list
        circuit_string_list.append(gate_string)
    # join the circuit string list to get the circuit string
    header = f"# {len(circuit.qubits)}\n"
    circuit_string = header + ",\n".join(circuit_string_list)
    return circuit_string + ":"


def get_quic_circuit_string(circuit: QuantumCircuit) -> str:
    """Translate qiskit circuit to quic circuit string

    :param circuit: QuantumCircuit
    :returns: formatted string
    :rtype: [str]
    """
    circuit_string = get_quic_circuit_file_string(circuit)

    # delete first line from the circuit string
    circuit_string = circuit_string.split("\n")[1:]

    circuit_arr = []
    for line in circuit_string:
        if line[0] == "{":
            continue
        circuit_arr.append(line)

    # join the circuit string to get the circuit string
    return "".join(circuit_arr)