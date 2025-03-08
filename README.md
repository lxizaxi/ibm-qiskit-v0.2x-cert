# ibm-qiskit-v0.2x-cert
「IBM Certified Associate Developer - Quantum Computation using Qiskit v0.2X」試験のためのqisikit実行環境を簡単に用意するためのリポジトリです。

試験と同じver帯の0.25.3の環境を作成します。
実行は「marimo」を使用しています。「[uv](https://docs.astral.sh/uv/getting-started/installation/)」はインストールしておいてください。

## 使い方

```sh
$ uv sync
$ . .venv/bin/activate
$ uv run marimo edit main.py
```
