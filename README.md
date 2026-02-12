# 📊 Real Time Stock Analytics

> Professional project by Gabriel Demetrios Lafis

[![Python](https://img.shields.io/badge/Python-3.12-3776AB.svg)](https://img.shields.io/badge/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://img.shields.io/badge/)
[![NumPy](https://img.shields.io/badge/NumPy-1.26-013243.svg)](https://img.shields.io/badge/)
[![Pandas](https://img.shields.io/badge/Pandas-2.2-150458.svg)](https://img.shields.io/badge/)
[![Plotly](https://img.shields.io/badge/Plotly-5.18-3F4F75.svg)](https://img.shields.io/badge/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.31-FF4B4B.svg)](https://img.shields.io/badge/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[English](#english) | [Português](#português)

---

## English

### 🎯 Overview

**Real Time Stock Analytics** is a production-grade Python application that showcases modern software engineering practices including clean architecture, comprehensive testing, containerized deployment, and CI/CD readiness.

The codebase comprises **314 lines** of source code organized across **1 modules**, following industry best practices for maintainability, scalability, and code quality.

### ✨ Key Features

- **📊 Interactive Visualizations**: Dynamic charts with real-time data updates
- **🎨 Responsive Design**: Adaptive layout for desktop and mobile devices
- **📈 Data Aggregation**: Multi-dimensional data analysis and filtering
- **📥 Export Capabilities**: PDF, CSV, and image export for reports
- **🐳 Containerized**: Docker support for consistent deployment
- **🏗️ Object-Oriented**: 1 core classes with clean architecture

### 🏗️ Architecture

```mermaid
graph LR
    subgraph Input["📥 Data Sources"]
        A[Stream Input]
        B[Batch Input]
    end
    
    subgraph Processing["⚙️ Processing Engine"]
        C[Ingestion Layer]
        D[Transformation Pipeline]
        E[Validation & QA]
    end
    
    subgraph Output["📤 Output"]
        F[(Data Store)]
        G[Analytics]
        H[Monitoring]
    end
    
    A --> C
    B --> C
    C --> D --> E
    E --> F
    E --> G
    D --> H
    
    style Input fill:#e1f5fe
    style Processing fill:#f3e5f5
    style Output fill:#e8f5e9
```

### 🚀 Quick Start

#### Prerequisites

- Python 3.12+
- pip (Python package manager)

#### Installation

```bash
# Clone the repository
git clone https://github.com/galafis/Real-Time-Stock-Analytics.git
cd Real-Time-Stock-Analytics

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### Running

```bash
# Run the application
python app.py
```

### 📁 Project Structure

```
Real-Time-Stock-Analytics/
├── tests/         # Test suite
│   ├── __init__.py
│   └── test_main.py
├── Dockerfile
├── LICENSE
├── README.md
├── app.py
└── requirements.txt
```

### 📊 Performance Metrics

The engine calculates comprehensive performance metrics:

| Metric | Description | Formula |
|--------|-------------|---------|
| **Sharpe Ratio** | Risk-adjusted return | (Rp - Rf) / σp |
| **Sortino Ratio** | Downside risk-adjusted return | (Rp - Rf) / σd |
| **Max Drawdown** | Maximum peak-to-trough decline | max(1 - Pt/Pmax) |
| **Win Rate** | Percentage of profitable trades | Wins / Total |
| **Profit Factor** | Gross profit / Gross loss | ΣProfit / ΣLoss |
| **Calmar Ratio** | Return / Max Drawdown | CAGR / MDD |
| **VaR (95%)** | Value at Risk | 5th percentile of returns |
| **Expected Shortfall** | Conditional VaR | E[R | R < VaR] |

### 🛠️ Tech Stack

| Technology | Description | Role |
|------------|-------------|------|
| **Python** | Core Language | Primary |
| **Docker** | Containerization platform | Framework |
| **NumPy** | Numerical computing | Framework |
| **Pandas** | Data manipulation library | Framework |
| **Plotly** | Interactive visualization | Framework |
| **Streamlit** | Data app framework | Framework |

### 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### 👤 Author

**Gabriel Demetrios Lafis**
- GitHub: [@galafis](https://github.com/galafis)
- LinkedIn: [Gabriel Demetrios Lafis](https://linkedin.com/in/gabriel-demetrios-lafis)

---

## Português

### 🎯 Visão Geral

**Real Time Stock Analytics** é uma aplicação Python de nível profissional que demonstra práticas modernas de engenharia de software, incluindo arquitetura limpa, testes abrangentes, implantação containerizada e prontidão para CI/CD.

A base de código compreende **314 linhas** de código-fonte organizadas em **1 módulos**, seguindo as melhores práticas do setor para manutenibilidade, escalabilidade e qualidade de código.

### ✨ Funcionalidades Principais

- **📊 Interactive Visualizations**: Dynamic charts with real-time data updates
- **🎨 Responsive Design**: Adaptive layout for desktop and mobile devices
- **📈 Data Aggregation**: Multi-dimensional data analysis and filtering
- **📥 Export Capabilities**: PDF, CSV, and image export for reports
- **🐳 Containerized**: Docker support for consistent deployment
- **🏗️ Object-Oriented**: 1 core classes with clean architecture

### 🏗️ Arquitetura

```mermaid
graph LR
    subgraph Input["📥 Data Sources"]
        A[Stream Input]
        B[Batch Input]
    end
    
    subgraph Processing["⚙️ Processing Engine"]
        C[Ingestion Layer]
        D[Transformation Pipeline]
        E[Validation & QA]
    end
    
    subgraph Output["📤 Output"]
        F[(Data Store)]
        G[Analytics]
        H[Monitoring]
    end
    
    A --> C
    B --> C
    C --> D --> E
    E --> F
    E --> G
    D --> H
    
    style Input fill:#e1f5fe
    style Processing fill:#f3e5f5
    style Output fill:#e8f5e9
```

### 🚀 Início Rápido

#### Prerequisites

- Python 3.12+
- pip (Python package manager)

#### Installation

```bash
# Clone the repository
git clone https://github.com/galafis/Real-Time-Stock-Analytics.git
cd Real-Time-Stock-Analytics

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### Running

```bash
# Run the application
python app.py
```

### 📁 Estrutura do Projeto

```
Real-Time-Stock-Analytics/
├── tests/         # Test suite
│   ├── __init__.py
│   └── test_main.py
├── Dockerfile
├── LICENSE
├── README.md
├── app.py
└── requirements.txt
```

### 📊 Performance Metrics

The engine calculates comprehensive performance metrics:

| Metric | Description | Formula |
|--------|-------------|---------|
| **Sharpe Ratio** | Risk-adjusted return | (Rp - Rf) / σp |
| **Sortino Ratio** | Downside risk-adjusted return | (Rp - Rf) / σd |
| **Max Drawdown** | Maximum peak-to-trough decline | max(1 - Pt/Pmax) |
| **Win Rate** | Percentage of profitable trades | Wins / Total |
| **Profit Factor** | Gross profit / Gross loss | ΣProfit / ΣLoss |
| **Calmar Ratio** | Return / Max Drawdown | CAGR / MDD |
| **VaR (95%)** | Value at Risk | 5th percentile of returns |
| **Expected Shortfall** | Conditional VaR | E[R | R < VaR] |

### 🛠️ Stack Tecnológica

| Tecnologia | Descrição | Papel |
|------------|-----------|-------|
| **Python** | Core Language | Primary |
| **Docker** | Containerization platform | Framework |
| **NumPy** | Numerical computing | Framework |
| **Pandas** | Data manipulation library | Framework |
| **Plotly** | Interactive visualization | Framework |
| **Streamlit** | Data app framework | Framework |

### 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para enviar um Pull Request.

### 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

### 👤 Autor

**Gabriel Demetrios Lafis**
- GitHub: [@galafis](https://github.com/galafis)
- LinkedIn: [Gabriel Demetrios Lafis](https://linkedin.com/in/gabriel-demetrios-lafis)
