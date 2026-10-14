"""Reproduce Week 4 model comparison from the bundled monthly source CSVs.
Run: python -m pip install -r reproducibility/requirements.txt
     python reproducibility/verify_week4.py
"""
from pathlib import Path
import json, hashlib, warnings
import numpy as np
import pandas as pd
import statsmodels
from statsmodels.tsa.holtwinters import Holt
warnings.filterwarnings('ignore',category=RuntimeWarning)
ROOT=Path(__file__).resolve().parents[1]
def forecast(y,model):
 if model=='Last value baseline':return float(y[-1])
 if model=='Drift':return float(y[-1]+(y[-1]-y[0])/(len(y)-1))
 if model=='Seasonal naive (12m)':return float(y[-12])
 if model=='Linear trend (36m)':
  a=y[-36:];return float(np.polyval(np.polyfit(np.arange(len(a)),a,1),len(a)))
 if model=='Holt damped trend':return float(Holt(y,damped_trend=True,initialization_method='estimated').fit(optimized=True).forecast(1)[0])
 raise ValueError(model)
MODELS=['Last value baseline','Drift','Seasonal naive (12m)','Linear trend (36m)','Holt damped trend']
def run():
 results={}
 for city in ['brooklyn','philadelphia']:
  p=ROOT/f'assets/data/{city}-condo-2020-2026.csv';df=pd.read_csv(p);df.columns=df.columns.str.strip().str.lower();dates=pd.to_datetime(df['month']);y=df.price.to_numpy(dtype=float)
  assert len(y)==81 and dates.is_unique and np.isfinite(y).all() and (y>0).all()
  assert dates.tolist()==pd.date_range('2020-01-01','2026-09-01',freq='MS').tolist()
  leaderboard=[]
  for model in MODELS:
   residual=np.array([y[t]-forecast(y[:t],model) for t in range(37,len(y))]);pred=forecast(y,model)
   leaderboard.append(dict(model=model,mae=float(np.abs(residual).mean()),rmse=float(np.sqrt((residual**2).mean())),forecast=pred,residual_p10=float(np.quantile(residual,.1)),residual_p90=float(np.quantile(residual,.9))))
  leaderboard.sort(key=lambda a:a['mae']);best=leaderboard[0]
  results[city]=dict(observations=len(y),backtests=44,initial_training_months=37,first_backtest='2023-02',last_backtest='2026-09',selected_model=best['model'],forecast=best['forecast'],latest=float(y[-1]),momentum_pct=(best['forecast']/y[-1]-1)*100,relative_mae_pct=best['mae']/y[-1]*100,range80=[best['forecast']+best['residual_p10'],best['forecast']+best['residual_p90']],historical_avg=float(y.mean()),historical_high=float(y.max()),historical_low=float(y.min()),growth_since_2020_pct=(y[-1]/y[0]-1)*100,source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),leaderboard=leaderboard)
 out=dict(protocol='Expanding window, 37 initial training observations, 44 one-month forecasts. Model selected on these same validation windows; no independent post-selection test.',numpy=np.__version__,pandas=pd.__version__,statsmodels=statsmodels.__version__,results=results)
 (ROOT/'reproducibility/week4-model-results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':run()
