# 🎓 EduChain – Blockchain Governance Simulation

EduChain is a lightweight simulation of blockchain governance using Python and Streamlit. It models the proposal, voting, and crisis-resolution processes of decentralized systems, inspired by the paper _“A system-based view of blockchain governance”_.

---

## 🚀 Features

- 🧾 Create proposals by actors like Admin, Teacher, Student
- 🗳️ Token-weighted on-chain voting system
- 💰 Rewards for participation (voting/proposing)
- 🚨 Crisis simulation and off-chain decision override
- 🔁 Lifecycle flow: `Design → Operate → Crisis`
- 🖥️ Interactive frontend with Streamlit

---

## 📂 Folder Structure

```
educhain-governance/
├── actors.py             # Actor roles and reward system
├── proposal.py           # Proposal and voting system
├── crisis.py             # Crisis and override logic
├── app.py                # Streamlit frontend app
├── main.py               # CLI version (for testing)
├── requirements.txt      # Python package dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Installation

### 📌 Prerequisites
- Python 3.8 to 3.12 recommended

### 🧰 Setup
```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
```

### 📦 Dependencies to Install
Install packages directly:
```bash
pip install streamlit tabulate
```

Or use the included `requirements.txt`:
```bash
pip install -r requirements.txt
```

| Package      | Purpose                                              |
|--------------|------------------------------------------------------|
| `streamlit`  | Runs the interactive web-based frontend              |
| `tabulate`   | Displays actor/token data neatly in CLI and tables   |

---

## ▶️ How to Run

### 🖥️ Streamlit Web Interface
```bash
streamlit run app.py
```
> Opens at [http://localhost:8501](http://localhost:8501)

### 🔧 CLI (Terminal Simulation)
```bash
python main.py
```

---

## 🧠 Governance Model Summary

| Component    | Description                                 |
|--------------|---------------------------------------------|
| Actors       | Admin, Teachers, Students, Core Members     |
| Proposals    | Anyone can propose rule changes             |
| Voting       | Token-weighted voting (YES/NO)              |
| Rewards      | +2 tokens for proposing, +1 for voting      |
| Crisis       | Triggered on tie or rejection               |
| Override     | Core team decides in case of crisis         |

---

## 📋 Example Flow

1. Teacher proposes “Increase max courses per semester”
2. All other actors vote (weighted by tokens)
3. Voting result displayed — Accepted, Rejected, or Tie
4. If tie → Crisis → Off-chain override by Core Team

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Credits

Created by **Vamsi Kiran**  
M.Tech (Information Security), NITK Surathkal, 2025
