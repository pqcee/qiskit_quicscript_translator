import enum
import qiskit
import numpy as np

# instruction for special pqcee gates
def p45_instruction() -> qiskit.circuit.Instruction:
    qc = qiskit.QuantumCircuit(1, name='p45')
    qc.p(np.pi/4, 0)
    return qc.to_instruction()


def pdg45_instruction() -> qiskit.circuit.Instruction:
    qc = qiskit.QuantumCircuit(1, name='pdg45')
    qc.p(-np.pi/4, 0)
    return qc.to_instruction()


def cp45_instruction() -> qiskit.circuit.Instruction:
    qc = qiskit.QuantumCircuit(2, name='cp45')
    qc.cp(np.pi/4, 0, 1)
    return qc.to_instruction()


def cpdg45_instruction() -> qiskit.circuit.Instruction:
    qc = qiskit.QuantumCircuit(2, name='cpdg45')
    qc.cp(-np.pi/4, 0, 1)
    return qc.to_instruction()

# Add here special name
# @quicname gate name
# @qiskitname qiskit instruction
# @special if the gate is special (optional)
# Define the basis gates for the PQCEE
class QuiCGate(enum.Enum):
    IDENTITY_GATE = ("I", qiskit.circuit.library.IGate(), True)
    X_GATE = ("X", qiskit.circuit.library.XGate())
    Y_GATE = ("Y", qiskit.circuit.library.YGate())
    Z_GATE = ("Z", qiskit.circuit.library.ZGate())
    H_GATE = ("H", qiskit.circuit.library.HGate())
    S_GATE = ("S", qiskit.circuit.library.SGate())
    SDG_GATE = ("s", qiskit.circuit.library.SdgGate())
    T_GATE = ("T", qiskit.circuit.library.TGate())
    TDG_GATE = ("t", qiskit.circuit.library.TdgGate())
    CX_GATE = ("CN", qiskit.circuit.library.CXGate())
    CCX_GATE = ("CCN", qiskit.circuit.library.CCXGate())
    CS_GATE = ("CS", qiskit.circuit.library.CSGate())
    CSDG_GATE = ("Cs", qiskit.circuit.library.CSdgGate())
    MEASUREMENT_GATE = ("m", qiskit.circuit.Measure(), True)
    P_GATE = ("P", p45_instruction(), True)
    PDG_GATE = ("p", pdg45_instruction(), True)
    # CP_GATE = ("CP", cp45_instruction(), True)
    CPDG_GATE = ("Cp", cpdg45_instruction(), True)
    CT_GATE = ("CT", qiskit.circuit.library.TGate().control(1))
    CTDG_GATE = ("Ct", qiskit.circuit.library.TdgGate().control(1))
    # New Gates requiring params
    RY_GATE = ("U", qiskit.circuit.library.RYGate(0))
    CU_GATE = ("CU", qiskit.circuit.library.CUGate(0, 0, 0, 0))
    U_GATE = ("U", qiskit.circuit.library.UGate(0, 0, 0))
    CP_GATE = ("CP", qiskit.circuit.library.CPhaseGate(0))

    # to add more gates
    # NAME = (QUIC_REPRESENTATION, QISKIT_INSTRUCTION, SPECIAL=False)
    # SPECIAL is True if the gate is not part of the standard basis gates
    # which can be used for approximations
    # and is used for special pqcee gates

    def __new__(cls, *args):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(
        self,
        quicRepresentation: str,
        qiskitInstruction: qiskit.circuit.Instruction,
        special: bool = False
    ) -> None:
        self.quicRepresentation = quicRepresentation
        self.qiskitInstruction = qiskitInstruction
        self.special = special

    def get_qiskit_instruction(self) -> qiskit.circuit.Instruction:
        return self.qiskitInstruction

    def get_quic_representation(self) -> str:
        return self.quicRepresentation

    def is_special(self) -> bool:
        return self.special

    @staticmethod
    def get_gates_name() -> list[str]:
        return list(map(lambda x: x.name, list(QuiCGate)))

    @staticmethod
    def get_gates_quic_name() -> list[str]:
        return list(map(lambda x: x.quicRepresentation, list(QuiCGate)))

    @staticmethod
    def get_gates_qiskit_name() -> list[str]:
        return list(
            map(
                lambda x: x.get_qiskit_instruction().name,
                list(QuiCGate)
            )
        )

    @classmethod
    def from_quic_name(cls, value: str):
        for member in cls.__members__.values():
            if member.quicRepresentation == value:
                return member
        raise KeyError(
            f"Quic Gate {value} is not part of the QuiCGate enum."
        )

    @classmethod
    def _missing_(cls, value: str):
        for member in cls.__members__.values():
            if member.name == value.upper():
                return member
        raise KeyError(f"Gate {value} is not part of the QuiCGate enum.")

    @classmethod
    def from_qiskit_name(cls, value: str):
        for member in cls.__members__.values():
            if member.get_qiskit_instruction().name == value:
                return member
        raise KeyError(
            f"Qiskit Gate {value} is not part of the QuiCGate enum."
        )
