# Blue-Green-Deployment-System-with-Ansible
## 📌 Project Overview
This project demonstrates a **Blue-Green Deployment strategy** using:
- Docker (for infrastructure)
- Ansible (for automation)
- Flask (sample application)
- NGINX (load balancer)

It ensures **zero-downtime deployment** by switching traffic between two environments:
- 🔵 Blue
- 🟢 Green

---

## 📁 Project Structure
ansible/
├── inventory.ini
├── group_vars/
│   └── all.yml
├── deploy.yml
└── roles/
    ├── common/      # Common tasks like installing Python
    ├── app/         # Deploys the Flask app and sets up systemd
    ├── load_balancer/ # Configures NGINX
    ├── health_check/  # Validates app health
    └── rollback/      # Reverts NGINX to the previous version


