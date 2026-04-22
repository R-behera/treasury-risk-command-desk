from pathlib import Path
    import json
    from fastapi import FastAPI
    from fastapi.responses import FileResponse, JSONResponse
    from fastapi.staticfiles import StaticFiles

    BASE = Path(__file__).resolve().parent
    WEB = BASE / 'web'
    DATA = {
  "signals": [
    {
      "signal": "EUR receivable concentration",
      "severity": "Elevated",
      "impact": "$1.8M margin sensitivity"
    },
    {
      "signal": "July refinancing window",
      "severity": "Watch",
      "impact": "170 bps spread risk if delayed"
    },
    {
      "signal": "APAC cash buffer",
      "severity": "Healthy",
      "impact": "7.4 weeks runway at current burn"
    }
  ],
  "scenarios": [
    {
      "scenario": "USD +5%",
      "ebitda_delta": "-2.1%",
      "liquidity_delta": "-$3.4M"
    },
    {
      "scenario": "Rate shock +75 bps",
      "ebitda_delta": "-0.8%",
      "liquidity_delta": "-$1.1M"
    },
    {
      "scenario": "Demand drawdown 12%",
      "ebitda_delta": "-3.3%",
      "liquidity_delta": "-$4.6M"
    }
  ]
}

    app = FastAPI(title='Treasury Risk Command Desk', version='0.1.0')
    app.mount('/static', StaticFiles(directory=str(WEB)), name='static')

    @app.get('/')
    def root():
        return FileResponse(WEB / 'index.html')

    @app.get('/health')
    def health():
        return {'status': 'ok', 'project': 'treasury-risk-command-desk'}

    @app.get('/api/overview')
    def overview():
        return JSONResponse(DATA)
