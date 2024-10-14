# qiskit_quicscript_translator

<p align="left">
    <a href="./release" alt="Version 0.0.1-beta">
        <img src="https://img.shields.io/badge/version-0.0.1--beta-brightgreen.svg" />
    </a>
</p>

Qiskit to QuICScript Translator. This repo is open source for developers to translate Qiskit to QuICScript language.

Check out QuICScript at https://pqcee.github.io/QuICScript/

> [!WARNING]  
> Current version might **not** have all gates.
> Submit [issue](https://github.com/pqcee/qiskit_quicscript_translator/issues) for gate implementation.

# Installation

### Installing Latest

```bash
pip install git+https://github.com/pqcee/qiskit_quicscript_translator
```

### Installing Specific Version

```bash
pip install git+https://github.com/pqcee/qiskit_quicscript_translator@<VERSION>
```

> [!NOTE]  
> Fill `<VERSION>` with specific version, check [Tags](https://github.com/pqcee/qiskit_quicscript_translator/tags) for avaliable versions

# Usage

### Example

```python
from qiskit_quicscript_translator import get_quic_circuit_string
from qiskit import QuantumCircuit
qc = QuantumCircuit(1)
qc.h(0)
qc.h(qc)
```

## Methods

### get_quic_circuit_string

```python
get_quic_circuit_string(circuit: QuantumCircuit) -> str
```

Return QuICScript `string` format of circuit

### get_quic_circuit_file_string

```python
get_quic_circuit_file_string(circuit: QuantumCircuit) -> str
```

Return QuICScript file `string` format of circuit

# Maintenance

This section list the instruction on how to maintain this repo

## Using Venv (Recommended)

Instructions from [Link](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

### Step 1: Create Virtual Environment

```bash
python3 -m venv .venv
```

### Step 2 (Unix/macOS): Activate a virtual environment

```bash
source .venv/bin/activate
```

### Step 2 (Windows): Activate a virtual environment

```bash
.venv\Scripts\activate
```

### Step 3: Using a requirements file

```bash
pip install -r requirements.txt
```

### Test Run

```bash
hatch run python
```

In Python Terminal

```python
>>> from qiskit_quicscript_translator import get_quic_circuit_string
>>> from qiskit import QuantumCircuit
>>> qc = QuantumCircuit(1)
>>> qc.h(0)
>>> qc.h(qc)
'H:'
```

Result `'H:'` should be shown

## Acknowledgements

This repo is a subset of [qiskit-pqcee-provider](https://github.com/pqcee/qiskit-pqcee-provider) repo. Work done by [@sdcioc](https://github.com/sdcioc) and [@sianliu](https://github.com/sianliu).
