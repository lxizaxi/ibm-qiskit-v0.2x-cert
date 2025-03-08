# ibm-qiskit-v0.2x-cert
「IBM Certified Associate Developer - Quantum Computation using Qiskit v0.2X」試験のためのqisikit実行環境を簡単に用意するためのリポジトリです。

試験で指定されているv0.2xの環境（v0.25.3）を作成します。
実行は「marimo」を使用しています。「[uv](https://docs.astral.sh/uv/getting-started/installation/)」はインストールしておいてください。

## 使い方

```sh
$ uv sync
$ . .venv/bin/activate
$ uv run marimo edit main.py
```
