import marimo

__generated_with = "0.11.17"
app = marimo.App(width="medium")


@app.cell
def _():
    from qiskit import QuantumCircuit, Aer, execute
    from math import sqrt
    qc = QuantumCircuit(2)

    # Insert fragment here
    qc.h(0)
    qc.cx(0,1)

    simulator = Aer.get_backend('statevector_simulator')
    result = execute(qc, simulator).result()
    statevector = result.get_statevector()
    print(statevector)

    return (
        Aer,
        QuantumCircuit,
        execute,
        qc,
        result,
        simulator,
        sqrt,
        statevector,
    )


if __name__ == "__main__":
    app.run()
