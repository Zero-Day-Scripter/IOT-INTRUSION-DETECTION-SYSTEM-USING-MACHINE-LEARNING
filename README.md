# IoT Intrusion Detection System

A Streamlit dashboard for classifying network traffic as normal or suspicious using Random Forest models trained on NSL-KDD and TON_IoT data. The dashboard supports offline PCAP/PCAPNG analysis and live packet capture.

## Requirements

- Python 3.10 or newer
- The model artifacts in the root `models/` directory
- Npcap on Windows for live packet capture; elevated permissions may also be required

## Setup

From the project root, create and activate a virtual environment in PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in that terminal, then activate the environment again.

## Run the dashboard

Run from the project root so the app can find `models/`:

```powershell
streamlit run src/app.py
```

Choose a model in the sidebar, then upload a `.pcap` or `.pcapng` file for offline analysis. Live capture requires a supported network interface and the platform permissions needed by Scapy.

## Training

The trained model artifacts are already stored in `models/` and are needed by the dashboard. To retrain the NSL-KDD model, place `KDDTrain+.txt` at `data/KDDTrain+.txt` and run:

```powershell
python src/train.py
```

To train the TON_IoT model, place `train_test_network.csv` in `data/ton/`. Note that `src/train-ton.py` currently uses a machine-specific absolute dataset path; update that path in the script before running it on another computer.

Datasets are not required to run the dashboard. When sharing this project, check the dataset terms and consider linking to the official dataset sources instead of committing the data files.

## Other scripts

- `python src/pcap-gen.py` generates a synthetic `strong_attack.pcap` for testing.
- `python src/ppt.py` generates a project presentation in the current directory.
