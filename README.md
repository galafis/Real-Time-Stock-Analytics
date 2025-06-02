# Real-Time Stock Analytics Dashboard

[English](#english) | [Português](#português)

## English

### Overview
An interactive real-time stock analytics dashboard built with Streamlit. Features comprehensive technical analysis, real-time data fetching, and professional visualizations for stock market analysis.

### Features
- **Real-Time Data**: Live stock data from Yahoo Finance
- **Technical Indicators**: RSI, MACD, Moving Averages, Bollinger Bands
- **Interactive Charts**: Candlestick charts with technical overlays
- **Stock Information**: Company details, market cap, P/E ratio, dividend yield
- **Multiple Timeframes**: 1 day to 5 years of historical data
- **Quick Selection**: Popular stocks for easy access
- **Professional UI**: Clean, responsive Streamlit interface

### Technologies Used
- **Python 3.8+**
- **Streamlit**: Web application framework
- **yfinance**: Real-time stock data API
- **Plotly**: Interactive charting library
- **Pandas**: Data manipulation
- **NumPy**: Numerical computing

### Installation

1. Clone the repository:
```bash
git clone https://github.com/galafis/Real-Time-Stock-Analytics.git
cd Real-Time-Stock-Analytics
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

### Usage

#### Web Interface
1. Open your browser to `http://localhost:8501`
2. Enter a stock symbol (e.g., AAPL, GOOGL, MSFT)
3. Select time period (1 day to 5 years)
4. Click "Analyze" or use quick select buttons
5. View interactive charts and technical indicators

#### Features Overview
- **Price Chart**: Candlestick chart with moving averages and Bollinger Bands
- **RSI Indicator**: Relative Strength Index with overbought/oversold levels
- **MACD**: Moving Average Convergence Divergence with signal line
- **Stock Metrics**: Real-time price, daily change, market cap, P/E ratio
- **Data Table**: Recent trading data with technical indicators

### Technical Indicators

#### Moving Averages
- **MA20**: 20-day moving average
- **MA50**: 50-day moving average

#### RSI (Relative Strength Index)
- Momentum oscillator (0-100)
- Overbought: > 70
- Oversold: < 30

#### MACD
- Trend-following momentum indicator
- Signal line crossovers for buy/sell signals
- Histogram shows momentum changes

#### Bollinger Bands
- Volatility indicator
- Upper and lower bands (2 standard deviations)
- Price touching bands indicates potential reversal

### Supported Stocks
- All stocks available on Yahoo Finance
- Quick access to popular stocks: AAPL, GOOGL, MSFT, AMZN, TSLA, NVDA, META, NFLX

### Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Português

### Visão Geral
Dashboard interativo de análise de ações em tempo real construído com Streamlit. Apresenta análise técnica abrangente, busca de dados em tempo real e visualizações profissionais para análise do mercado de ações.

### Funcionalidades
- **Dados em Tempo Real**: Dados de ações ao vivo do Yahoo Finance
- **Indicadores Técnicos**: RSI, MACD, Médias Móveis, Bandas de Bollinger
- **Gráficos Interativos**: Gráficos de candlestick com sobreposições técnicas
- **Informações de Ações**: Detalhes da empresa, valor de mercado, P/L, dividend yield
- **Múltiplos Períodos**: 1 dia a 5 anos de dados históricos
- **Seleção Rápida**: Ações populares para acesso fácil
- **Interface Profissional**: Interface Streamlit limpa e responsiva

### Tecnologias Utilizadas
- **Python 3.8+**
- **Streamlit**: Framework de aplicação web
- **yfinance**: API de dados de ações em tempo real
- **Plotly**: Biblioteca de gráficos interativos
- **Pandas**: Manipulação de dados
- **NumPy**: Computação numérica

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/galafis/Real-Time-Stock-Analytics.git
cd Real-Time-Stock-Analytics
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
streamlit run app.py
```

### Uso

#### Interface Web
1. Abra seu navegador em `http://localhost:8501`
2. Digite um símbolo de ação (ex: AAPL, GOOGL, MSFT)
3. Selecione o período (1 dia a 5 anos)
4. Clique em "Analisar" ou use os botões de seleção rápida
5. Visualize gráficos interativos e indicadores técnicos

#### Visão Geral das Funcionalidades
- **Gráfico de Preços**: Gráfico candlestick com médias móveis e Bandas de Bollinger
- **Indicador RSI**: Índice de Força Relativa com níveis de sobrecompra/sobrevenda
- **MACD**: Convergência e Divergência de Médias Móveis com linha de sinal
- **Métricas de Ações**: Preço em tempo real, variação diária, valor de mercado, P/L
- **Tabela de Dados**: Dados recentes de negociação com indicadores técnicos

### Indicadores Técnicos

#### Médias Móveis
- **MA20**: Média móvel de 20 dias
- **MA50**: Média móvel de 50 dias

#### RSI (Índice de Força Relativa)
- Oscilador de momentum (0-100)
- Sobrecompra: > 70
- Sobrevenda: < 30

#### MACD
- Indicador de momentum seguidor de tendência
- Cruzamentos da linha de sinal para sinais de compra/venda
- Histograma mostra mudanças de momentum

#### Bandas de Bollinger
- Indicador de volatilidade
- Bandas superior e inferior (2 desvios padrão)
- Preço tocando as bandas indica possível reversão

### Ações Suportadas
- Todas as ações disponíveis no Yahoo Finance
- Acesso rápido a ações populares: AAPL, GOOGL, MSFT, AMZN, TSLA, NVDA, META, NFLX

### Contribuindo
1. Faça um fork do repositório
2. Crie uma branch de feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adicionar nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Crie um Pull Request

### Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

